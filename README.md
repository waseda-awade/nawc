# Non-Assisted Human Writing Corpus (NAWC)

A versioned, openly licensed corpus of **verified non-assisted human writing** in English,
collected under physically proctored conditions and documented with a standardized
institutional top sheet. Contributions from institutions worldwide are welcome, subject to
the submission standard in [`standard/`](standard/).

## Why this corpus exists

Since late 2022, text of verified human authorship — composed without generative AI
assistance, under documented conditions — has become a scarce research resource. This
corpus provides such texts with per-text composition dates and graded, auditable evidence
of non-assistance, for use in applied linguistics, language assessment, automated essay
scoring, and AI-text detection research.

## What "non-assisted" means here

All texts were composed **in person, with a proctor or instructor physically present**.
That requirement doesn't bend. How the rest of the collection condition is documented does:
every submission includes a required, full-prose **proctoring description** — this is what's
actually evaluated for acceptance. Tiers 1–3 are common reference patterns for describing
that condition, not the only acceptable configurations:

- **Tier 1** — handwritten (transcription method documented)
- **Tier 2** — institutional machines with technical controls (network- or
  application-level isolation, verification method documented)
- **Tier 3** — personal devices under documented proctoring controls

The structured checklists under each tier are optional supplementary detail, not a
mandatory match — if a submission's actual conditions don't map cleanly onto one (a hybrid
handwritten-then-typed workflow, for instance), the contributor describes it fully in prose
instead, and that description is the basis for acceptance. Remote collection (including
remote with keystroke logging) and self-attested data remain excluded regardless of how
well documented they are — in-person supervision is the one requirement that isn't
descriptive. Every record carries the metadata needed to filter by tier and by composition
date.

**Assistance policy.** The exclusion is generative AI/LLM assistance — including AI-powered
writing tools such as Word's AI Editor and Grammarly — translation tools, and help from
another person. Spellcheck, autocorrect, and standard word-processor functions are
**permitted** and are simply documented in the top sheet for transparency, not treated as
risk factors. **Predictive text is not blanket-permitted without comment** — its use must
be disclosed (on/off/unknown) and, when on or unknown, described: which device(s), and
whether prediction was word-level or sentence-level. Sentence-level prediction sits closer
to generative assistance than basic word completion, so visibility matters here in a way it
doesn't for plain spellcheck. Known use of an AI-powered
grammar/rewriting tool is grounds for rejection or a clarification request during editorial
review; "unknown" is an acceptable answer when the contributor did not verify. Full
definitions: [`standard/TOPSHEET_FORM.md`](standard/TOPSHEET_FORM.md).

## Attribution and citation model

The corpus follows an **edited-volume model**:

- Each institutional **subcorpus** is published as its own Zenodo record. Its **creators**
  (dataset authors) are the submitting researchers, named in the submission's
  `attribution` block, with ORCID/ROR identifiers where available. Attribution to them is
  a condition of the CC BY-NC 4.0 license.
- Each **corpus release** (v1.0, v1.1, ...) is an umbrella Zenodo record listing the
  project team as **editors** (DataCite contributor role), linked to subcorpus records via
  `HasPart` / `IsPartOf` relations.

**Citing a specific subcorpus** (recommended form):

> Author(s) of subcorpus (Year). *Subcorpus name* (Version X.Y) [Data set].
> In Editor(s) (Eds.), *Non-Assisted Human Writing Corpus*. Zenodo. https://doi.org/...

**Citing the whole corpus:**

> Editor(s) (Eds.) (Year). *Non-Assisted Human Writing Corpus* (Version X.Y) [Data set].
> Zenodo. https://doi.org/...

Machine-readable citation metadata: [`CITATION.cff`](CITATION.cff).

## Repository structure

```
standard/    The submission standard: top sheet forms (markdown + Word), JSON Schema,
             validator, example submission
tools/       Editor-side intake pipeline (scripted raw-material conversion)
data/        One directory per accepted subcorpus (submission.json, manifest.csv, texts/)
docs/        Contributor documentation
.github/     CI validation run on every pull request
```

## Contributing a subcorpus

See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md). In brief: complete and sign the top
sheet (Word form in `standard/`), and email it to the maintainers together with your texts
in whatever reasonable form you have them (original files preferred). The editors convert
your materials with a logged, scripted pipeline and publish with full attribution to you
upon acceptance — there is no pre-publication contributor review step. No technical
knowledge required. Git-comfortable contributors may open a pull request directly instead.
Ethics approval documents are transmitted privately, never published. Consent adequacy is
the contributing institution's own responsibility, attested on the top sheet, not reviewed
by the editors.

## Licensing

The entire repository — corpus data, submission standard, and code —
is licensed under [CC BY-NC 4.0](LICENSE): attribution required,
non-commercial use only. Copyright (c) 2026 Waseda University.

## Versioning

Releases are tagged on GitHub and archived to Zenodo, which mints a version-specific DOI
per release and a concept DOI resolving to the latest version. Text IDs are permanent and
never reused; every release documents added/removed/corrected texts in
[`CHANGELOG.md`](CHANGELOG.md). Minor versions = corrections/additions within existing
subcorpora; major versions = new subcorpora or schema-breaking changes. **Corrections to an
already-published subcorpus are handled by resubmission**, published as a new version of
the *same* Zenodo record via Zenodo's built-in versioning — the same mechanism used for the
whole-corpus releases above. The subcorpus's concept DOI moves to point at the new version;
the prior version remains accessible and citable at its own version DOI.

## Maintainers / editors

- John Maurice Gayed, Waseda University, Global Education Center — https://orcid.org/0000-0002-7028-3291
- Randy Appel, Waseda University, Global Education Center — https://orcid.org/0000-0001-7715-9560
- May Kristine Jonson Carlon, Waseda University, Global Education Center — https://orcid.org/0000-0002-7346-2332
