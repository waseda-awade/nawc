#!/usr/bin/env python3
"""Validate a corpus submission top sheet against topsheet.schema.json.

Usage:
    python validate.py submission.json [more_submissions.json ...]

Exit code 0 if all files validate; 1 otherwise.
Requires: pip install jsonschema
"""
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    sys.exit("Missing dependency: pip install jsonschema")

SCHEMA_PATH = Path(__file__).parent / "topsheet.schema.json"


def validate_file(path: Path, validator: Draft202012Validator) -> bool:
    try:
        instance = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"[FAIL] {path}: not valid JSON ({e})")
        return False

    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path))
    if errors:
        print(f"[FAIL] {path}: {len(errors)} error(s)")
        for err in errors:
            loc = "/".join(str(p) for p in err.absolute_path) or "<root>"
            print(f"  - {loc}: {err.message}")
        return False

    # Semantic checks beyond JSON Schema's reach
    warnings = []
    coll = instance.get("collection", {})
    start, end = coll.get("composition_date_start"), coll.get("composition_date_end")
    if start and end and start > end:
        print(f"[FAIL] {path}: composition_date_start ({start}) is after composition_date_end ({end})")
        return False
    wc = instance.get("task", {}).get("word_count_requirement", {})
    if "min" in wc and "max" in wc and wc["min"] > wc["max"]:
        print(f"[FAIL] {path}: word_count_requirement min > max")
        return False

    print(f"[OK]   {path}")
    for w in warnings:
        print(f"  ! warning: {w}")
    return True


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    ok = all(validate_file(Path(a), validator) for a in sys.argv[1:])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
