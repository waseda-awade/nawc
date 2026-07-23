# Changelog

All notable changes to the corpus data and submission standard.
Text IDs are permanent; removed texts are listed here as tombstones.

## [Unreleased]
### Standard
- Clarified that original raw submitted files (the Excel spreadsheet, individual
  docx/txt files, whatever a contributor sent) are read-only inputs to
  `tools/intake_convert.py` -- never modified, never committed -- and documented why
  editors should retain their own copy privately rather than discard it after
  conversion: the processing log's SHA-256 checksums are only meaningful if the file
  they were computed from still exists, and a raw spreadsheet can carry an identifying
  key column that has no place in git history. Added as a fourth item alongside the
  three previously-documented never-committed artifacts in "What the published folder
  actually looks like."
- `tools/intake_convert.py` now automates matching scores to texts, closing a real gap:
  previously nothing pulled score data in at all, and an editor would have had to
  hand-match scores against auto-generated text IDs. Two paths: `--score-cols` pulls
  score column(s) from the same spreadsheet as the essay text (xlsx input only);
  `--scores-file` matches a separate CSV/XLSX against individual text/docx files by
  original filename (tried exact, then extension-stripped) or against an xlsx's
  `--id-col` value. Multiple score columns map to the manifest's documented
  `score_1`/`score_2`/... convention. Unmatched texts and unmatched scores-file rows are
  both surfaced explicitly (console output + processing log) rather than silently
  dropped, so partial score coverage or a key typo is visible, not hidden. Tested against
  both an xlsx-with-inline-scores scenario and a directory-of-files-plus-separate-scores
  scenario, including the filename-extension fallback and missing/orphaned-row cases;
  confirmed the existing no-scoring-args path is unchanged.
- Documented the exact published folder structure in `docs/CONTRIBUTING.md` ("What the
  published folder actually looks like"), with an explicit public/private breakdown --
  clarifying that the signed top sheet, the ethics document, and the intake tool's
  processing log/manifest skeleton are never committed, only their JSON transcription
  and finished manifest are.
### Standard
- **Subcorpora now bundle by collection effort, not by task type.** `subcorpus.genre`
  (a required, closed-enum, single value) is replaced by `subcorpus.genres_included`
  (a required, open, multi-value list) plus a new required per-text `genre` column in
  the manifest. A program with several exam types (expository, comparative,
  argumentative) now submits ONE subcorpus covering all of them -- matching a single
  ethics approval and consent process -- with genre tracked per text so researchers can
  still filter by task type. This supersedes an earlier draft of this guidance that
  recommended splitting by task type; that added avoidable duplication for collection
  efforts governed by one ethics approval, without a strong enough benefit to justify it.
- `tools/intake_convert.py`: added a persistent ID registry (`data/_id_registry.json`)
  so reusing the same `--prefix` across separate submissions over time (e.g. later
  cohorts/terms) continues numbering instead of restarting at 0001 and colliding with
  an earlier submission. Added `--start-at` for manual override/recovery, and a
  `genre` column in the generated manifest skeleton. Tested against a simulated
  multi-submission scenario with zero collisions.
- Documented optional cross-submission `writer_id` stability (same pseudonym across an
  institution's separate submissions over time, e.g. tracking a student who appears in
  a later term's cohort) with explicit privacy trade-off guidance in
  `docs/CONTRIBUTING.md`. Tracking a student across task types no longer needs this --
  bundling means that's already covered by within-subcorpus writer_id stability.
- CI's manifest column check now also requires `genre`.
### Data
- Reference example renamed `waseda-expository-2026` -> `awade-2025` (dropped the
  task-specific suffix now that the example bundles multiple genres) and populated
  with real (non-sensitive) data: AWADE coordinator as contact, real ethics exemption
  reference (2025-HN028, documented_exemption), accurate consent-process description,
  and `genres_included: [expository, comparative, argumentative]` -- based on Waseda's
  actual ethics notice and consent letter.
### Standard
- v1.0.0-draft of the submission top sheet, JSON Schema, and validator.
- Editorial curation model: submitters send a signed top sheet (Word form provided)
  plus raw texts in any reasonable format; editors convert via scripted pipeline
  (tools/intake_convert.py) with SHA-256 chain of custody. Submissions publish upon
  editorial acceptance (no pre-publication contributor sign-off step); corrections are
  handled by resubmission, published as a new version of the same Zenodo record via
  Zenodo's built-in versioning (same mechanism as whole-corpus releases) -- a new
  version DOI is minted, the concept DOI moves to point at it, and the prior version
  remains accessible at its own DOI. Attestation split: submitters attest
  conditions/raw materials (Section 11); editors record conversion details (Section 12
  / editorial_processing).
- Assistance policy clarified: generative AI/LLM assistance, translation tools, and
  help from another person are excluded; spellcheck, autocorrect, predictive text
  (including on smartphones), and standard word-processor functions are permitted and
  documented for transparency only.
- AI-powered grammar/rewriting tools (e.g. Word's AI Editor, Grammarly) explicitly named
  as excluded, not "standard word-processor functions." Known use is grounds for
  editorial rejection or a clarification request; "unknown" remains acceptable. Added
  `grammar_tool_name` field (tiers 2-3) and `grammar_tools` field to tier 3, which was
  previously missing.
- Added general `collection.protocol_notes` field (applies regardless of tier) plus an
  optional per-text `notes` manifest column, for deviations/context that don't
  compromise a hard requirement. Explicitly scoped: not for disclosing texts that failed
  a hard requirement while still including them -- those must be excluded, with the
  exclusion reason recorded here instead. Consolidated away the narrower, tier-3-only
  `notes` field it superseded.
- **Tiers restructured from gatekeeping to descriptive.** Added required
  `collection.proctoring_description` (full-prose, minLength enforced) as the actual
  basis for accepting a submission's collection conditions. Tiers 1-3 remain as
  reference patterns, but their structured checklists (`tier1_handwritten`,
  `tier2_institutional_machines`, `tier3_personal_devices`) are now optional
  supplementary detail rather than a mandatory match -- a submission whose conditions
  don't map cleanly onto any tier is now accepted on the strength of
  `proctoring_description` alone. In-person attestation is unchanged and remains a hard
  requirement; this change loosens *how* conditions are documented, not *whether*
  physical proctoring is required.
- Predictive text moved out of the blanket-permitted assistance list and into a
  disclosure requirement: `predictive_text` is now tracked in tier 2 as well as tier 3
  (school-issued tablets are Tier 2, not Tier 3), and a new `predictive_text_note` field
  (both tiers) asks for device and word-level vs. sentence-level detail when in use or
  unknown. Not an exclusion -- a visibility requirement, since sentence-level prediction
  sits closer to generative assistance than basic word completion.
- Consent responsibility: contributors attest that consent adequate for CC BY-NC 4.0
  public redistribution was obtained; adequacy is the contributing institution's own
  determination, not reviewed by editors. Consent form attachment is optional.
- License fixed corpus-wide: CC BY-NC 4.0 for the entire repository (data, standard, and code), copyright Waseda University.
- Mandatory `attribution` block: subcorpus authors credited as creators on
  per-subcorpus DOI records.
### Data
- (pending) waseda-expository-2026 subcorpus.
