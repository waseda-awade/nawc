# Contributing a Subcorpus

This corpus uses an **editorial model**: you send us your materials in whatever reasonable
form you have them, and the corpus editors convert them into the published format. You do
not need to know JSON, git, or anything technical. What we cannot do for you is document
the collection conditions or determine that your consent is adequate — only you can do
that, so those are yours to attest.

The corpus only accepts English texts composed **in person under physically proctored
conditions**. That's the one requirement that doesn't flex. How you document it does:
you'll write a full, plain-language description of your proctoring conditions — that
description is what actually gets evaluated. Tiers 1–3 (defined in
[`../standard/TOPSHEET_FORM.md`](../standard/TOPSHEET_FORM.md)) are common reference
patterns for that description, not the only acceptable configurations — if your
collection doesn't map cleanly onto one, describe it fully and pick the closest tier for
broad categorization. Remote and self-attested collections cannot be accepted regardless
of other qualities or how well documented they are.

## What "non-assisted" means

The exclusion is **generative AI/LLM assistance — including AI-powered writing tools such
as Word's AI Editor and Grammarly — translation tools, and help from another person**.
Spellcheck, autocorrect, and standard word-processor functions are **permitted** and simply
documented on the top sheet for transparency — they are not treated as risk factors and do
not affect acceptance.

**Predictive text is different: disclose it, don't assume it's fine.** If any students used
a device with predictive text — an iPad, a smartphone, an on-screen keyboard — say so, and
describe whether it was word-level (next-word suggestion) or sentence-level (whole-phrase
completion). Sentence-level prediction is functionally closer to generative assistance than
basic word completion, so it doesn't get the same automatic pass spellcheck does. This is a
disclosure requirement, not a rejection — we're not aware of a reason to exclude predictive
text outright, but we do need visibility into what was actually used. If usage varied by
student, the manifest's per-text `notes` column can record who.

If you know (or the top sheet's grammar-tool question indicates) that an AI-powered tool
was used, expect us to follow up with a clarification request, or to decline the
submission if generative assistance is confirmed. If you genuinely don't know whether such
a tool was in use, answer "unknown" — that is an acceptable, honest answer and will not by
itself cause rejection.

## Describing conditions that don't fit a tier

Tiers 1–3 cover the most common patterns, but real collection doesn't always sort neatly
into one. If yours doesn't, you're not blocked — describe it fully in
`proctoring_description` instead, and pick whichever tier is closest for filtering
purposes. The structured checklist under each tier is optional; use whatever parts apply
and explain the rest in prose.

**Worked example.** A school runs a two-stage process that doesn't match any tier exactly:
students handwrite a first draft under full exam-hall proctoring (two invigilators, no
devices), then independently type a clean copy at unsupervised library computers within
the week, with the instructor checking the typed version against the handwritten draft to
confirm no substantive changes beyond legibility fixes. This isn't Tier 1 (there's a typed
stage) or Tier 2 (the typing stage isn't proctored) in the strict sense — but it's fully
explicable, and physical proctoring did occur for the actual composition. Write the whole
process out in `proctoring_description`, choose whichever tier feels closest (or note that
neither fits well), and leave the tier-specific checklists blank or partially filled. What
matters is that we can understand exactly what happened, not that it matches a preset
category.

The one thing this flexibility doesn't extend to: remote collection and self-attested data
remain excluded no matter how thoroughly they're documented. Physical presence during
composition is the one condition that has to be true, not just well-explained.

## Outlier conditions and protocol deviations

Real collection rarely goes exactly to plan. The top sheet's `protocol_notes` field
(Section 7) exists for exactly this — but it has a scope limit worth understanding before
you use it:

- **Use it for context that doesn't affect the hard requirements**: a session interrupted
  by a fire drill, a substitute proctor, a room change, unusual timing. These are honest,
  useful disclosures that don't change whether the data qualifies.
- **Don't use it to explain away a violation of a hard requirement.** Worked example: your
  school has an absence policy that lets students who miss class submit work from home. A
  student who wrote at home did not compose the text in person — that specific text does
  not meet the in-person requirement, full stop, regardless of the reason. The fix is not
  to include it with a note explaining the policy; the fix is to **exclude that student's
  text from the submission** (identify it by `text_id` if you've already assigned one) and
  use `protocol_notes` to disclose the exclusion: *"3 students submitted under the school's
  absence policy and were excluded from this dataset."* The remaining in-person texts from
  the same class are still good data.

The same logic applies to any hard requirement, not just in-person attestation — the
question to ask is always "did this specific text meet every hard requirement, yes or no,"
not "is there a reasonable explanation." A per-text version of the same field exists in the
manifest (`notes` column) for caveats that apply to one text rather than the whole
submission.

If you're unsure whether something you're seeing is a "note it" case or an "exclude it"
case, ask us before you submit — that's a normal, expected question, not a sign your data
isn't good enough.

## Before you collect data

1. **You are responsible for obtaining and determining the adequacy of consent.** The top
   sheet asks you to attest that informed consent was obtained covering public
   redistribution and derivative research use under **CC BY-NC 4.0**. We do not review
   consent forms or adjudicate their adequacy — that determination is your institution's.
   Consent cannot be retrofitted, so settle the license wording before writers put pen to
   paper.
2. **One top sheet per collection condition.** If a session mixes conditions, plan for
   separate submissions.
3. **"Unknown" beats guessing.** Wherever the top sheet offers an "unknown" option, use it
   if you did not verify the true state. An honest "unknown" is acceptable; false
   precision is grounds for removal.

## What to send

Email the corpus maintainers:

1. **The completed, signed top sheet** — use the Word version
   ([`../standard/topsheet_submitter_form.docx`](../standard/topsheet_submitter_form.docx))
   or the markdown form. Plain language is fine; leave Section 12 blank (editor use).
2. **The texts, in the rawest form you have them.** Preference order:
   - original files straight off the collection environment (LMS export, files from lab
     machines, original Word documents, plain text) — **best**
   - scanned-then-transcribed text files (Tier 1)
   - **text pasted into Excel/CSV cells — accepted, but last resort.** Spreadsheet
     applications can silently alter pasted text (autocorrect, autoformat), which matters
     for a corpus whose value is verbatim wording. If a spreadsheet is genuinely all you
     have, send it; we record the transport format in the public metadata either way.
3. **Scores** (if any). If your essays are already in a spreadsheet, put the score(s) in
   their own column(s) in that same file — they'll be pulled in automatically alongside the
   text. If your essays are individual files, send scores as a separate spreadsheet with one
   row per text and a column that identifies which text each row belongs to (the original
   filename works well, with or without its extension; a student/exam ID works too if that's
   what your text spreadsheet or filenames use). Either way, editors don't hand-copy scores
   onto auto-generated text IDs — the conversion tool matches them for you as long as there's
   a consistent identifier to match on.
4. **Attachments**: prompt(s) verbatim, rubric (if any). A consent form template is
   welcome but optional — we retain it for reference only, not for review.
5. **Privately, never published:** the ethics approval/exemption document.
6. **Never send:** Tier 1 handwritten originals or scans (retain them at your institution
   for audit; handwriting is quasi-identifying).

## What the editors then do

1. Convert your texts to corpus format with a **scripted, logged pipeline**
   (`tools/intake_convert.py`) — no manual copy-paste, including matching any scores you
   sent to the right auto-generated text ID. SHA-256 checksums of your received files are
   recorded in a private processing log.
2. Transcribe your signed top sheet into machine-validated `submission.json`
   (your signed original is archived privately alongside the ethics document).
3. CI validates the schema, UTF-8/NFC encoding, and text-ID integrity; a second editor
   reviews, including: confirming `proctoring_description` actually describes what
   happened rather than restating the tier label (this is now the primary basis for
   acceptance, so a thin or generic description gets sent back for more detail); checking
   the grammar-tool field for known AI-powered tool use (Word's AI Editor, Grammarly, or
   similar) that would conflict with the non-assisted claim — following up with the
   contributor for clarification where needed; and reading `protocol_notes` for any
   disclosed deviation that should have resulted in excluded texts but didn't.
4. **Publish upon acceptance.** There is no pre-publication contributor review step —
   once a submission is accepted, it is included in the next corpus release and archived
   to Zenodo with attribution to you.

## What the published folder actually looks like

This is what `data/<subcorpus-name>/` contains once a submission is processed and merged —
useful to know whether you're a contributor curious where your materials end up, an editor
producing this structure, or a git-comfortable contributor assembling it directly yourself.

```
data/awade-2025/
├── submission.json          the top sheet, as validated JSON
├── manifest.csv              per-text metadata (text_id, writer_id, genre, prompt_id, ...)
├── texts/
│   ├── awade-0001.txt
│   ├── awade-0002.txt
│   └── ...                   one file per essay, sequentially renamed -- never the
│                              original filenames a contributor sent
└── attachments/
    ├── prompt_expository.txt
    ├── rubric_holistic.pdf
    └── ...                   prompts (required), rubrics (if any)
```

**Everything above is public** — committed to the repository, visible to anyone browsing
GitHub. Four things are deliberately never committed, even though they exist during
processing:

- **The original raw file(s) a contributor sent** — the Excel spreadsheet, the individual
  `.docx`/`.txt` files, whatever arrived. `tools/intake_convert.py` only *reads* these; it
  never modifies or deletes them, and they are never committed to the repository. Editors
  retain their own copy of what they received, privately, for two reasons: the SHA-256
  checksum recorded in the processing log only means anything if the file it was computed
  from still exists to check against later, and a raw file — especially a spreadsheet —
  can carry an identifying column (a real student ID or name used to key rows) that has no
  business in git history even though the converted, pseudonymized output does.
- **The signed top sheet itself** (the Word document a contributor filled in and signed).
  Only its transcription into `submission.json` is public; the original is archived
  privately by editors alongside the ethics document, since a signed form can carry
  signatures or other detail that doesn't need to be in a public git history.
- **The ethics approval/exemption document** (e.g., the actual PDF). Only its reference
  number (`ethics_legal.approval_reference`) is public in `submission.json` — the document
  itself stays private with the editors.
- **`manifest_skeleton.csv` and `processing_log.json`**, both generated by
  `tools/intake_convert.py` during conversion and both `.gitignore`d. The processing log
  especially, since it records the *original* filenames a contributor sent — which can
  themselves be identifying (e.g., a file named with a student's name) — alongside SHA-256
  checksums for chain-of-custody. An editor fills in `manifest_skeleton.csv`'s blank
  columns and saves the result as `manifest.csv` (or whatever name they choose to record in
  `processing.manifest_file`); that finished file is what actually gets committed.

## Corrections and resubmission

There is no editing of a published subcorpus in place. If a correction is needed, **resubmit**:
send the corrected materials (referencing the original submission in `resubmission_of`) and
the same intake process runs again. A resubmission publishes as a **new version of the same
Zenodo record**, using Zenodo's built-in versioning — the same mechanism used for the
whole-corpus releases. It receives its own version-specific DOI; the subcorpus's concept DOI
moves to point at the new version; and the prior version remains accessible and citable at
its own version DOI, so existing citations are never broken.

## Multiple task types in one submission (e.g., several exam types)

If your program runs more than one kind of writing task — an expository exam, a comparative
exam, an argumentative exam — **bundle them into one subcorpus and one top sheet**, covering
everything from one collection effort (same cohort, same ethics approval, same consent
process). Don't split by task type: that would mean re-describing the same proctoring
conditions and re-citing the same ethics approval multiple times for something that was
actually approved and consented as a single effort.

Instead, task type is tracked **per text**, not per subcorpus:

- List every genre/task type included in `subcorpus.genres_included` (top sheet Section 2) —
  a short summary, e.g. `["expository", "comparative", "argumentative"]`. This is free text,
  not a fixed list, so a new task type your program adds later isn't blocked.
- Record each individual text's specific genre in the manifest's `genre` column (Section 9).
  This is what lets a downstream researcher filter a multi-task subcorpus down to just the
  task type they want — the subcorpus is one citable unit, but fully filterable inside.
- If different task types used different prompts or rubrics, attach all of them and use the
  manifest's `prompt_id` column (and rubric notes, if needed) to map each text to the right
  one.

Split into separate subcorpora instead only if you have a specific reason to — wanting
separate citable credit per task type, or publishing one task type now and another much
later as an unrelated effort. Bundling is the default; splitting is the exception.

**Permanent text IDs across separate submissions over time.** If you submit incrementally —
this term's cohort now, a later term's cohort in a future submission — and want one
continuous ID scheme across all of them (`awade-0001`, `awade-0002`, ... regardless of which
submission a text came from, rather than restarting per submission),
`tools/intake_convert.py` supports this directly: reuse the same `--prefix` across separate
runs, and it tracks the next available number in a small registry file
(`data/_id_registry.json`) so each new submission continues where the last one left off
instead of colliding with it. Commit the updated registry alongside each submission.

**Tracking the same writer across separate submissions.** Within one bundled subcorpus, the
manifest's `writer_id` column already links one student's expository, comparative, and
argumentative texts together — no extra work needed, since it's required to be stable within
a subcorpus and all their task types now live in the same submission. The remaining question
is only whether to keep `writer_id` stable **across separate submissions** too — e.g., the
same student appearing again in a later term's cohort. That's optional, and worth thinking
through before you do it:

- It has real research value: it enables longitudinal analysis of the same writer over time,
  which a fresh pseudonym per submission would rule out.
- It also has a real privacy cost: linking texts across submissions to one pseudonym
  increases what's exposed if any single text is ever identified — instead of one text being
  traceable to a person, everything linked to that pseudonym is. Standard practice in
  longitudinal learner corpora, but a deliberate trade-off, not a default.
- If you do this, the crosswalk from real student identity to pseudonymous `writer_id` stays
  entirely on your side, privately, and is never submitted or published — exactly like the
  handling for any other PII.
- Check that your consent language reasonably covers it. Consent describing anonymized data
  being "made publicly available for research" is generally understood to permit this kind
  of linkage as long as the writer_id itself carries no identifying information, but if
  you're not sure, it's worth a quick confirmation from whoever manages your consent process.

If you'd rather not deal with this, a fresh `writer_id` per submission is simpler and
perfectly fine — cross-submission tracking is an opt-in enrichment, not an expectation.

## Attribution — what you receive

On publication:

- Your subcorpus is deposited as its **own Zenodo record** with its **own DOI**. The
  persons named in the top sheet's attribution section are listed as the record's
  **creators (dataset authors)**, with ORCID and ROR identifiers where provided.
- The record carries an `IsPartOf` relation to the corpus release; the corpus lists the
  project team as **editors**, following an edited-volume model.
- Recommended citation, stated on the record:

  > Your Name(s) (Year). *Your subcorpus name* (Version X.Y) [Data set]. In Editor(s)
  > (Eds.), *Non-Assisted Human Writing Corpus*. Zenodo. https://doi.org/...

- Because the license is CC **BY**-NC 4.0, attribution to the listed creators is a
  license condition, not merely a citation convention.

## Responsibility split (who attests what)

- **You attest** (Section 11): the collection conditions; that the raw materials you sent
  are unaltered; (Tier 1) transcription fidelity; and that consent adequate for CC BY-NC
  4.0 public redistribution was obtained — its adequacy is your institution's
  determination, not ours.
- **The editors record** (Section 12 / `editorial_processing`): conversion details — tool,
  version, and an exhaustive list of transformations applied.

## Git-comfortable contributors

You are welcome to skip the editorial conversion and open a pull request directly with a
complete `data/<subcorpus-name>/` directory — see "What the published folder actually looks
like" above for the exact target structure, and `standard/` for the schema and validator;
run `python standard/validate.py` before submitting. The `editorial_processing` block is
still completed by the editors during review.
