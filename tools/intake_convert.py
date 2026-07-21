#!/usr/bin/env python3
"""intake_convert.py - editor-side conversion of raw submitted texts to corpus format.

Converts a directory of .txt/.docx files, or a spreadsheet with one text per row,
into NFC-normalized UTF-8 text files plus a manifest skeleton and a processing log
with SHA-256 checksums of every source file (chain of custody).

Usage:
  # Directory of files (one essay per .txt or .docx file):
  python tools/intake_convert.py --input raw_submission/ --outdir data/kyoto-argumentative-2026 --prefix kyo26

  # Spreadsheet (one essay per row):
  python tools/intake_convert.py --input essays.xlsx --outdir data/kyoto-argumentative-2026 \
      --prefix kyo26 --text-col "essay" [--id-col "student"] [--sheet "Sheet1"]

Outputs under --outdir:
  texts/<prefix>-NNNN.txt      one per essay, UTF-8, NFC, LF line endings
  manifest_skeleton.csv        text_id + word_count filled; editors complete the rest
  processing_log.json          tool version, timestamps, per-source SHA-256, transformations
                               (KEEP PRIVATE - may contain original filenames with student names)

ID REGISTRY (collision prevention across multiple submissions sharing one prefix):
  If you reuse the same --prefix across separate runs -- e.g. one institution submitting
  several exam-type subcorpora (awade-expository, awade-comparative, awade-argumentative)
  that should share one continuous ID pool ("awade-0001", "awade-0002", ... regardless of
  which submission a text belongs to) -- this tool tracks the next available number per
  prefix in a registry file (default: data/_id_registry.json) so each new run continues
  from where the last one left off instead of restarting at 0001 and colliding with an
  earlier submission's IDs. The registry is updated automatically after a successful run;
  commit it alongside the new submission. Use --start-at to override (e.g. first-ever
  seeding, or recovering from a manually-corrected collision) -- this bypasses the
  registry's stored value for this run and prints a warning.

Transformations applied (exactly these, nothing else):
  - docx: paragraph text extraction (python-docx; body paragraphs in document order)
  - decode (UTF-8 with BOM tolerance for .txt; cp932/shift-jis fallback is NOT attempted -
    undecodable files are skipped and reported so the editor resolves encoding explicitly)
  - Unicode NFC normalization
  - CRLF/CR -> LF
  - strip UTF-8 BOM; ensure single trailing newline
Word-internal characters (curly quotes, dashes, students' errors) are NOT altered.

Requires: pip install python-docx openpyxl
"""
import argparse
import csv
import datetime
import hashlib
import json
import sys
import unicodedata
from pathlib import Path

TOOL_NAME = "intake_convert.py"
TOOL_VERSION = "1.1.0"


def normalize(text: str) -> str:
    text = text.lstrip("\ufeff")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = unicodedata.normalize("NFC", text)
    if not text.endswith("\n"):
        text += "\n"
    return text


def read_docx(path: Path) -> str:
    from docx import Document
    doc = Document(str(path))
    return "\n".join(p.text for p in doc.paragraphs)


def read_txt(path: Path) -> str:
    return path.read_bytes().decode("utf-8")  # strict; BOM handled in normalize()


def rows_from_xlsx(path: Path, sheet: str | None, text_col: str, id_col: str | None):
    import openpyxl
    wb = openpyxl.load_workbook(str(path), read_only=True, data_only=True)
    ws = wb[sheet] if sheet else wb.active
    rows = ws.iter_rows(values_only=True)
    header = [str(h).strip() if h is not None else "" for h in next(rows)]
    if text_col not in header:
        sys.exit(f"Column '{text_col}' not found. Available: {header}")
    t_idx = header.index(text_col)
    i_idx = header.index(id_col) if id_col and id_col in header else None
    for n, row in enumerate(rows, start=2):
        text = row[t_idx] if t_idx < len(row) else None
        if text is None or str(text).strip() == "":
            continue
        src_id = str(row[i_idx]) if i_idx is not None and i_idx < len(row) else f"row{n}"
        yield src_id, str(text)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_registry(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as ex:
        sys.exit(f"Registry {path} exists but is not valid JSON ({ex}). Fix or remove it before continuing.")


def save_registry(path: Path, registry: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(registry, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)  # atomic on POSIX; avoids a half-written registry on interruption


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True, help="Directory of .txt/.docx files, or an .xlsx file")
    ap.add_argument("--outdir", required=True, help="Subcorpus directory, e.g. data/kyoto-argumentative-2026")
    ap.add_argument("--prefix", required=True, help="text_id prefix, e.g. kyo26. Reuse the same prefix across multiple submissions to share one continuous ID pool (see ID REGISTRY above).")
    ap.add_argument("--text-col", help="(xlsx) header of the column containing essay text")
    ap.add_argument("--id-col", help="(xlsx) optional header of a source-identifier column (logged privately, NOT used as text_id)")
    ap.add_argument("--sheet", help="(xlsx) worksheet name; default: active sheet")
    ap.add_argument("--registry", default="data/_id_registry.json", help="Path to the ID registry JSON tracking next-available-number per prefix (default: data/_id_registry.json)")
    ap.add_argument("--start-at", type=int, help="Override the registry-derived starting number for this run (e.g. first-ever seeding, or manual collision recovery). Prints a warning; still updates the registry afterward.")
    args = ap.parse_args()

    inp, outdir, registry_path = Path(args.input), Path(args.outdir), Path(args.registry)
    texts_dir = outdir / "texts"
    texts_dir.mkdir(parents=True, exist_ok=True)

    registry = load_registry(registry_path)
    if args.start_at is not None:
        start_n = args.start_at
        print(f"WARNING: --start-at {start_n} overrides the registry (which has "
              f"{registry.get(args.prefix, 'no entry')} for prefix '{args.prefix}'). "
              f"Make sure this doesn't collide with IDs already in use.")
    else:
        start_n = registry.get(args.prefix, 1)

    entries, skipped = [], []
    transformations = [
        "NFC normalization", "CRLF/CR -> LF", "BOM strip", "single trailing newline"
    ]

    if inp.is_dir():
        sources = sorted(p for p in inp.iterdir() if p.suffix.lower() in (".txt", ".docx") and not p.name.startswith("~$"))
        if not sources:
            sys.exit(f"No .txt or .docx files found in {inp}")
        readers = {".txt": read_txt, ".docx": read_docx}
        if any(p.suffix.lower() == ".docx" for p in sources):
            transformations.insert(0, "docx paragraph extraction (python-docx)")
        n = start_n
        for src in sources:
            tid = f"{args.prefix}-{n:04d}"
            try:
                raw = readers[src.suffix.lower()](src)
            except UnicodeDecodeError:
                skipped.append((src.name, "not UTF-8; resolve encoding explicitly and re-run"))
                continue
            except Exception as ex:  # unreadable/corrupt file - report, don't guess
                skipped.append((src.name, f"read error: {ex}"))
                continue
            out = normalize(raw)
            (texts_dir / f"{tid}.txt").write_text(out, encoding="utf-8")
            entries.append({
                "text_id": tid, "source_file": src.name,
                "source_sha256": sha256_file(src),
                "word_count": len(out.split()),
            })
            n += 1
    elif inp.suffix.lower() == ".xlsx":
        if not args.text_col:
            sys.exit("--text-col is required for spreadsheet input")
        transformations.insert(0, "extraction from spreadsheet cells (openpyxl, values only)")
        sheet_sha = sha256_file(inp)
        n = start_n
        for src_id, raw in rows_from_xlsx(inp, args.sheet, args.text_col, args.id_col):
            tid = f"{args.prefix}-{n:04d}"
            out = normalize(raw)
            (texts_dir / f"{tid}.txt").write_text(out, encoding="utf-8")
            entries.append({
                "text_id": tid, "source_file": f"{inp.name}:{src_id}",
                "source_sha256": sheet_sha,
                "word_count": len(out.split()),
            })
            n += 1
    else:
        sys.exit("--input must be a directory or an .xlsx file")

    # manifest skeleton: editors complete writer_id/genre/prompt_id/composition_date from submitter materials
    with open(outdir / "manifest_skeleton.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["text_id", "writer_id", "genre", "prompt_id", "composition_date", "word_count", "notes"])
        for e in entries:
            w.writerow([e["text_id"], "", "", "", "", e["word_count"], ""])

    log = {
        "tool": {"name": TOOL_NAME, "version": TOOL_VERSION},
        "run_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "input": str(inp),
        "transformations_applied": transformations,
        "texts_converted": len(entries),
        "skipped": [{"source_file": s, "reason": r} for s, r in skipped],
        "entries": entries,
        "note": "KEEP PRIVATE: source_file values may contain student-identifying original filenames.",
    }
    (outdir / "processing_log.json").write_text(json.dumps(log, indent=2), encoding="utf-8")

    if entries:
        registry[args.prefix] = start_n + len(entries)
        save_registry(registry_path, registry)

    print(f"Converted {len(entries)} text(s) -> {texts_dir}")
    if entries:
        print(f"ID range used: {entries[0]['text_id']} .. {entries[-1]['text_id']}")
        print(f"Registry updated: {registry_path} (prefix '{args.prefix}' next starts at {registry[args.prefix]:04d}) -- commit this file alongside the submission.")
    print(f"Manifest skeleton: {outdir/'manifest_skeleton.csv'} (complete writer_id/genre/prompt_id/composition_date)")
    print(f"Processing log (PRIVATE, do not commit): {outdir/'processing_log.json'}")
    for s, r in skipped:
        print(f"SKIPPED {s}: {r}")
    return 1 if skipped else 0


if __name__ == "__main__":
    sys.exit(main())

