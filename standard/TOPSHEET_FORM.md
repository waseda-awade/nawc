# Institutional Submission Top Sheet
## Non-Assisted Human Writing Corpus — Schema v1.0.0-draft

**Read before completing.** One top sheet describes exactly **one collection condition**. If a session mixed conditions (e.g., most students on locked-down lab machines but overflow students on personal laptops), file **separate top sheets** and separate manifests for each condition. Wherever this form offers an **"unknown"** option, use it if you did not verify the true state — an honest "unknown" is acceptable; false precision is grounds for removal of the subcorpus.

Submitters complete this form (or its Word version) in plain language and sign it; the corpus editors transcribe it into machine-validated `submission.json` and publish upon acceptance. There is no pre-publication review step for you to complete -- if a correction is later needed, resubmit; a resubmission publishes as a new version of the same record (via Zenodo's built-in versioning), receiving its own version DOI while the subcorpus's concept DOI moves to point at it. This document is the reference for what each field means.

**Assistance policy.** The corpus excludes generative AI/LLM assistance (including AI-powered writing tools such as Word's AI Editor and Grammarly), translation tools, and help from another person. Spellcheck, autocorrect, and standard word-processor functions ARE permitted and are simply documented below for transparency. **Predictive text is not blanket-permitted without comment** — disclose whether it was used and, if so or if unknown, describe the device and whether prediction was word-level or sentence-level (sentence-level sits closer to generative assistance). Known use of an AI-powered grammar/rewriting tool is grounds for rejection or a clarification request during editorial review; "unknown" is an acceptable, honest answer if you did not verify. Fields marked ▢ are checkboxes; fields marked ✱ are mandatory.

---

## 1. Administrative

- ✱ Submission date: `YYYY-MM-DD`
- ✱ Target corpus version: `___` (e.g., 1.1)
- Resubmission of (previous submission ID, if correcting): `___`
- ✱ Institution name: `___`
- Department / program: `___`
- ✱ Country (ISO 3166-1 alpha-2): `___`
- ✱ Contact person — name: `___`  email: `___`  ORCID (recommended): `___`  role: `___`

### Dataset authors (attribution)
List the person(s) to be credited as **authors of this subcorpus** in its DOI record and citations, in citation order. May differ from the administrative contact. Attribution to these names is a condition of the CC BY-NC 4.0 license.
- ✱ Author 1 — family name: `___`  given name(s): `___`  affiliation: `___`  ORCID (recommended): `___`  ROR ID (optional): `___`
- Author 2 — `___` *(repeat as needed)*
- Preferred citation string (optional; otherwise generated as *Authors (Year). Subcorpus (Version) [Data set]. In Editors (Eds.), Corpus name. Zenodo. DOI*): `___`

## 2. Subcorpus identification

- ✱ Subcorpus name (lowercase, hyphenated, stable): `___` (e.g., `awade-2025`)
- ✱ Language: `eng` (fixed for corpus v1.x)
- ✱ Genres/task types included in this subcorpus (list all that apply; free text, not a fixed list — e.g. expository, comparative, argumentative): `___`
  *If this subcorpus spans multiple task types, list them all here. Use short, consistent, lowercase terms — they should roughly match the per-text genre column in the manifest (Section 9), which is what researchers actually filter on.*
- Local task name(s) (institution's own label, any language — if multiple tasks, list or describe collectively): `___`

## 3. Ethics and legal — *gatekeeping section; incomplete submissions are rejected*

- ✱ Approval type: ▢ IRB approval ▢ Ethics committee approval ▢ Documented exemption
- ✱ Approval / exemption reference number: `___`
- ✱ ▢ **I attest that informed consent was obtained covering public redistribution and derivative research use under CC BY-NC 4.0** (not merely "research use"). *Determining and obtaining adequate consent is your institution's own responsibility; corpus editors do not review consent forms for adequacy.*
- Consent form template attached (optional — retained for reference only, not reviewed): ▢ yes ▢ no
- ✱ Writers under 18 included? ▢ yes ▢ no
  - If yes: ✱ ▢ Guardian consent documented (must be true)
- ✱ ▢ License granted to the corpus: **CC BY-NC 4.0** (fixed corpus-wide; the consent form signed by writers must name this license — submissions under any other license are rejected)

## 4. PII removal

- ✱ ▢ All personally identifying information removed from texts (must be true)
- ✱ Method: ▢ manual ▢ automated ▢ manual + automated
- ✱ Replacement convention: `___` (e.g., `<NAME>`, `<PLACE>`, `<INSTITUTION>`)
- Notes: `___`

## 5. Writer cohort

- ✱ Number of writers: `___`
- ✱ Relationship to English: ▢ L1 ▢ L2 ▢ mixed
- ✱ L1 background(s) (ISO 639-3 preferred; "unknown" permitted): `___`
- Proficiency evidence (repeat per evidence type; strongly encouraged for L2 cohorts):
  - Framework: ▢ CEFR ▢ TOEFL iBT ▢ TOEIC ▢ IELTS ▢ EIKEN ▢ institutional placement ▢ other → `___`
  - Level or range: `___`
  - Recency relative to writing: ▢ ≤6 months ▢ ≤1 year ▢ ≤3 years ▢ older/unknown
- Age range: `___`  Education level: ▢ secondary ▢ undergraduate ▢ graduate ▢ adult education ▢ mixed ▢ other ▢ unknown
- Major / field: `___`
- ✱ Recruitment: ▢ required coursework ▢ operational exam ▢ volunteer (unpaid) ▢ volunteer (incentivized) ▢ other
- Recruitment notes (selection bias context): `___`

## 6. Task conditions

- ✱ ▢ Prompt(s) attached **verbatim** (must be true). Number of prompts: `___`
- ✱ Prompt reuse: ▢ first use ▢ reused across sessions ▢ reused across years ▢ unknown
- ✱ Time limit (minutes, writing only): `___`  Separate planning time (minutes): `___`
- ✱ Revision: ▢ revision within single sitting ▢ multiple drafts across sessions ▢ no revision permitted
  - *Note: multi-draft data is accepted but flagged to corpus users as weaker condition control.*
- Word count requirement — min: `___` max: `___` target: `___`; ▢ enforced ▢ advisory ▢ none
- ✱ Stakes as announced to writers: ▢ graded coursework ▢ high-stakes exam ▢ low-stakes practice ▢ research only ▢ research, incentivized
- Audience specified in the task (if any): `___`

## 7. Collection condition (verification core)

- ✱ ▢ **In-person attestation:** a proctor or instructor was physically present for all texts (must be true — remote collection is excluded from this corpus, including remote collection with keystroke logging)
- ✱ Composition dates: start `YYYY-MM-DD` end `YYYY-MM-DD`  Sessions: `___`
- ✱ ▢ **Single-condition attestation:** this sheet describes exactly one condition (must be true)
- ✱ AI/internet prohibition communicated to writers: ▢ yes, explicitly ▢ implied by exam rules ▢ no ▢ unknown

- ✱ **Proctoring description** (required — this is what we actually evaluate): `___`
  *Describe in full how proctoring/supervision was conducted — who supervised, how, and what was and wasn't controlled. This is the primary basis for acceptance, not exact agreement with one of the tier checklists below. A few complete sentences, not "proctored" or "yes." If your setup doesn't map cleanly onto Tiers 1–3, describe it fully here — that's fine, the tiers are common reference patterns, not the only acceptable configurations.*

- ✱ **Tier** — closest reference pattern (pick one; this is a broad category for filtering, not a technical requirement you must match exactly): ▢ 1 — handwritten ▢ 2 — institutional machines ▢ 3 — personal devices

- Structured detail for the subsection matching your tier (below) is **optional** — fill in what you know; anything that doesn't fit these checklists belongs in the proctoring description above, or in Protocol deviations below if it's a caveat rather than part of the baseline description.

- Protocol deviations / caveats (optional): `___`
  *For context that doesn't affect the attestations above — an interrupted session, a substitute proctor, unusual timing. **Not** for exceptions to in-person or single-condition attestation: if some texts didn't meet a hard requirement (e.g., a school's absence policy let some students submit from home), exclude those specific texts from this submission — the rest of the in-person data is still good. Use this field to say so: "3 students submitted under the school's absence policy and were excluded from this dataset."*

*A note on the ✱ marks in the tier subsections below: they mean "required within this subsection, if you choose to complete it" — not "required for every submission." None of Tiers 1–3 is mandatory; the proctoring description above is what's actually required.*

### Tier 1 — In-person, handwritten (optional structured detail, if it applies)
- ✱ Transcriber role (who keyed the texts): `___`  Transcriber L1: `___`
- ✱ Keying method: ▢ double-keyed with reconciliation ▢ single pass + verification sample → sample %: `___` ▢ single pass
- ✱ ▢ **Errors-preserved attestation:** spelling, punctuation, and grammar errors transcribed verbatim; no silent correction (must be true)
- ✱ Illegible-word convention: `___` (e.g., `<illegible>` per unreadable word)
- ✱ Crossed-out/deleted text: ▢ final state only *(corpus default for v1.0)* ▢ deletions preserved with markup
- ✱ ▢ Originals/scans retained by the institution for audit (must be true)
- ✱ ▢ Originals **not** submitted to the corpus (must be true — handwriting is quasi-identifying)

### Tier 2 — In-person, institutional machines with technical controls (optional structured detail, if it applies)
- ✱ Isolation type: ▢ network-level (air-gapped / network disabled) ▢ application-level (lockdown browser or kiosk on a networked machine)
  - If application-level: ✱ lockdown software name: `___` version: `___`
- ✱ How was isolation verified (not merely asserted)? ▢ physically air-gapped ▢ adapters disabled ▢ firewall rules ▢ lockdown vendor configuration ▢ verified by IT staff ▢ unknown
- ✱ Writing software — name: `___` version: `___` (e.g., Notepad; MS Word 2021; Moodle essay field)
- ✱ Spellcheck: ▢ on ▢ off ▢ unknown  ✱ Autocorrect: ▢ on ▢ off ▢ unknown
- ✱ Predictive text: ▢ on ▢ off ▢ unknown — if on/unknown, describe device(s) and level: `___` *(e.g., school-issued iPads; word-level or sentence-level. Not assumed off just because the machine is institutional — school-issued tablets are Tier 2, not Tier 3.)*
- ✱ Grammar/suggestion tools: ▢ on ▢ off ▢ unknown — if on/unknown, name the tool: `___` *(AI-powered tools, e.g. Word's AI Editor or Grammarly, are EXCLUDED — known use is grounds for rejection or a clarification request; "unknown" is acceptable if not verified. Basic rule-based spelling/grammar highlighting is not the concern here.)*
- Text retrieval method (chain of custody): `___`

### Tier 3 — In-person, personal devices (optional structured detail, if it applies)
- ✱ Devices permitted: ▢ laptop ▢ tablet ▢ phone *(all device types permitted, incl. predictive text on phones -- recorded for transparency, not treated as a risk factor)*
- ✱ Proctor-to-writer ratio: `___ : ___`
- ✱ Screens visible to proctor: ▢ yes, all ▢ partially ▢ no ▢ unknown
- ✱ Device configuration check: ▢ yes, before writing ▢ spot checks during ▢ no ▢ unknown
- ✱ Spellcheck: ▢ on ▢ off ▢ unknown  ✱ Autocorrect: ▢ on ▢ off ▢ unknown  ✱ Predictive text: ▢ on ▢ off ▢ unknown — if on/unknown, describe device(s) and level: `___` *(e.g., "iPads, word-level"; "personal phones, sentence-level suggestions for some students." Sentence-level prediction sits closer to generative assistance than basic word completion.)*
- ✱ Grammar/suggestion tools: ▢ on ▢ off ▢ unknown — if on/unknown, name the tool: `___` *(AI-powered tools, e.g. Word's AI Editor or Grammarly, are EXCLUDED — known use is grounds for rejection or a clarification request; "unknown" is acceptable if not verified.)*
- ✱ Submission method: `___` (e.g., LMS upload at session end under proctor observation)

## 8. Scoring (optional section; complete if scores exist)

- Rubric attached verbatim: ▢ yes ▢ no
- Scale description: `___` (e.g., 0–5 holistic, half points permitted)
- Raters per text: `___`  Rater training: `___`
- Inter-rater reliability — statistic: ▢ QWK ▢ ICC ▢ exact agreement % ▢ adjacent agreement % ▢ Krippendorff's α ▢ Pearson r ▢ other
  - Statistic detail (**required for ICC**: model/type, e.g., ICC(2,1), two-way random, absolute agreement): `___`
  - Value: `___`
- Adjudication procedure: `___`
- Scores operational (counted toward grades/decisions)? ▢ yes ▢ no (research-only)

## 9. Data processing

- ✱ Encoding: UTF-8 (mandatory)  ✱ Unicode normalization: NFC (mandatory)
- ✱ Normalization applied beyond encoding: `___` ("none" if none; e.g., "line endings → LF, nothing else")
- ✱ ▢ Filenames comply with corpus ID convention (must be true)
- ✱ Per-text manifest filename: `___.csv`

### Manifest CSV — columns
| Column | Requirement | Notes |
|---|---|---|
| `text_id` | required, unique, permanent | Assigned per corpus convention; never reused across versions |
| `writer_id` | required | Pseudonymous. Must be stable within this subcorpus — since exam types are now bundled together, this already covers linking one student's expository, comparative, and argumentative texts within one cohort's submission. May optionally stay stable **across separate submissions** too (e.g., the same student appearing in a later term's cohort), if you want that person's texts linkable across cohorts — see "Tracking the same writer across submissions" in `docs/CONTRIBUTING.md` before doing this, since it's a real privacy trade-off, not just a convenience. |
| `genre` | required | The specific genre/task type of this text, e.g. `expository`, `comparative`, `argumentative`. Free text, matching (or close to) the subcorpus-level `genres_included` list — this is what lets researchers filter a multi-task subcorpus by task type. |
| `prompt_id` | required | Maps to attached prompt files |
| `composition_date` | required | `YYYY-MM-DD`; session date acceptable if per-text date unavailable |
| `word_count` | required | Whitespace-token count of the submitted text |
| `score` | optional | Repeatable as `score_1`, `score_2`, ... for multiple raters; final adjudicated score as `score_final` |
| `notes` | optional | Per-text caveats that don't apply to the whole submission — e.g., "session interrupted by fire drill, resumed after 10 min." Same scope limit as `protocol_notes` in Section 7: document context, don't use to excuse a text that didn't meet a hard requirement — exclude that text instead. |

## 10. Attachments checklist

- ✱ ▢ Prompt file(s), verbatim
- ▢ Rubric file(s), verbatim
- ▢ Consent form template (optional)
- ✱ ▢ Ethics approval / exemption document — **transmitted privately to corpus maintainers, not published** (only the reference number appears publicly)
- ▢ Other (list): `___`

## 11. Submitter attestation

> I attest that the collection conditions described in this top sheet are accurate; that all texts were composed in person under the condition described; that the raw materials transmitted to the corpus editors are unaltered; that any Tier 1 transcription followed the stated method with errors preserved verbatim; and that "unknown" was selected wherever the true state was not verified, with no field answered by assumption.

- ✱ Attested by (name, role): `___`
- ✱ Signature: `___`  ✱ Date: `YYYY-MM-DD`

## 12. Editorial processing — *completed by corpus editors; submitters leave blank*

Filled in by the editorial team after conversion of the raw materials, and validated as part of `submission.json`. Records: who processed the submission and when; the formats the texts arrived in; the conversion tool and version (manual copy-paste conversion is prohibited); an exhaustive list of transformations applied; whether SHA-256 checksums of the received files were logged; and whether this top sheet was machine-readable from the submitter or transcribed from a signed form (if transcribed, the signed original is archived privately). Submissions are published upon editorial acceptance -- there is no pre-publication contributor sign-off step.
