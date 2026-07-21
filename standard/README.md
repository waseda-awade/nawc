# Submission Standard — Non-Assisted Human Writing Corpus (v1.0.0-draft)

This package defines the institutional submission standard for the corpus: what a contributing
institution must document for one collection condition, in both human-readable and
machine-validated form.

## Contents

| File | Purpose |
|---|---|
| `TOPSHEET_FORM.md` | Human-readable top sheet: field definitions, instructions, attestation text. The reference document for administrators. |
| `topsheet.schema.json` | JSON Schema (draft 2020-12) encoding the same fields with mandatory-field rules, controlled vocabularies, and per-tier conditional requirements. The machine-enforced standard. |
| `example-submission.json` | A complete, validating example (fictionalized Tier 2 submission). Contributors should copy and edit this. |
| `topsheet_submitter_form.docx` | Fillable Word version of the top sheet for non-technical submitters (editors transcribe it to `submission.json`). |
| `validate.py` | Validator. `pip install jsonschema`, then `python validate.py submission.json`. Also applies semantic checks JSON Schema cannot express (date ordering, min/max word count, license placeholder warning). |

## Core design rules

1. **One top sheet per collection condition**, not per session. Mixed-condition sessions
   require separate top sheets and manifests.
2. **Physical proctoring is the one hard requirement; the tier structure is descriptive,
   not gatekeeping.** Every submission requires a full-prose `proctoring_description` —
   that's the actual basis for acceptance. Tiers 1-3 are common reference patterns for
   describing a condition, not the only acceptable configurations:
   - **Tier 1** — in-person, handwritten (transcription method documented)
   - **Tier 2** — in-person, institutional machines with technical controls
     (network-level or application-level isolation, verification method documented)
   - **Tier 3** — in-person, typed on personal devices (proctoring controls documented)
   - **Excluded, regardless of documentation quality:** all remote collection (including
     remote with keystroke logging) and all self-attested data. Rationale: physical
     proctoring is the corpus's minimum verification standard; remote logging cannot rule
     out second-device composition without process-data audit capacity the project does
     not currently have. This is the one place description cannot substitute for the
     underlying condition.
   - The structured tier-specific checklists (`tier1_handwritten`,
     `tier2_institutional_machines`, `tier3_personal_devices`) are **optional**
     supplementary detail, not required even when their tier is selected. A submission
     whose conditions don't map cleanly onto any tier (a hybrid handwritten-then-typed
     workflow, for instance) is accepted on the strength of `proctoring_description`
     alone, with the closest tier chosen for broad filtering.
   - The tiers remain **collection modes, not a strict quality ranking**: Tier 1 is
     strongest on the non-assistance claim but carries transcription-fidelity risk;
     Tier 2 yields verbatim born-digital text but depends on the technical configuration.
3. **"Unknown" is a first-class answer** for assistance-feature fields (spellcheck,
   autocorrect, predictive text, grammar tools). False precision is grounds for removal;
   an honest "unknown" is not.
4. **Hard gates** (schema `const` constraints — a submission cannot validate without them):
   consent covering redistribution; PII removed; prompt attached verbatim; in-person
   attestation; single-condition attestation; verbatim error preservation (Tier 1);
   originals retained locally but not submitted (Tier 1); UTF-8 / NFC.
5. **Composition dates are mandatory** and appear both on the top sheet (range) and in the
   per-text manifest, so downstream users can filter by pre/post-LLM-era composition.
6. **Permanent text IDs.** `text_id` values are never reused or reassigned across corpus
   versions; every release ships a changelog of added/removed/corrected texts.
7. **`protocol_notes` documents deviations, never excuses hard-requirement violations.**
   A general, optional free-text field (collection-level, plus a per-text `notes` column
   in the manifest) exists for context that doesn't compromise a hard requirement — an
   interrupted session, a substitute proctor. It is explicitly not for disclosing texts
   that failed a hard requirement while still including them; those texts must be
   excluded from the submission, with the exclusion and its reason noted in this field
   instead. See `docs/CONTRIBUTING.md` for a worked example.
8. **Predictive text is disclosed, not blanket-permitted.** Unlike spellcheck and
   autocorrect, predictive text use must be reported (tiers 2-3) and, when on or
   unknown, described via `predictive_text_note` — device and word-level vs.
   sentence-level sophistication. Sentence-level prediction sits closer to generative
   assistance than basic word completion, so it doesn't get spellcheck's automatic pass.
   This is a disclosure requirement, not an exclusion.

## Suggested repository / release workflow

- GitHub hosts this standard, the validator, documentation, and the issue tracker.
- Data releases are cut as GitHub releases archived to Zenodo, which mints a
  version-specific DOI per release plus a concept DOI resolving to the latest version.
  Versioning: minor = corrections/additions within existing subcorpora; major = new
  institutional subcorpora or schema-breaking changes.
- Submissions arrive as: `submission.json` + `manifest.csv` + text files + attachments
  (prompt, rubric, consent template, ethics document). CI runs `validate.py` plus
  encoding/ID-collision checks before maintainer review.

## Resolved project decisions

- **License: CC BY-NC 4.0**, fixed corpus-wide (decision 2026-07-07). The schema enforces it
  as a `const`; consent forms must name it. Verify final wording with the institutional
  research ethics office before printing consent forms.
- **Archive: Zenodo** (GitHub releases auto-archived; version DOI + concept DOI per release;
  records immutable after publication). GitHub remains the home of this standard, the
  validator, and community discussion.

## Open decisions (blockers before public release)

1. **L1 vs. L2 English framing** — the schema accepts both (`english_relationship`), but the
   v1.0 publication's framing should state the intended population.
2. **Text ID convention** — the manifest requires permanent `text_id`s; the exact format
   (e.g., `{subcorpus}-{seq}`) needs to be fixed in the contributor documentation.

## Verification status of this draft

- The schema itself passes `Draft202012Validator.check_schema` (well-formed).
- The example submission validates, and 8 negative tests (wrong tier block, missing
  guardian consent, remote collection, missing lockdown software under application-level
  isolation, malformed proctor ratio, etc.) are correctly rejected; valid Tier 1 and
  Tier 3 variants are correctly accepted.
- `format: "date"` and `format: "email"` were tested and are enforced when `validate.py`'s
  `FormatChecker` is used. Note that jsonschema's built-in email check is lightweight
  (it will catch obviously malformed values, not all invalid addresses), and `format`
  constraints are annotation-only if a validator is run without a format checker —
  use `validate.py`, not ad-hoc validation.
- This is a draft standard produced with AI assistance and reviewed tests, not a
  legally reviewed instrument. The ethics/consent and license sections in particular
  should be reviewed by the institution's research ethics office before adoption.
