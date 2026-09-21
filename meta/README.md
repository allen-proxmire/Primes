# meta — how the collection was made

**Nothing here is a result.** These are working documents: the record of what was tried, what was recovered, and what was decided. They live apart from the papers so that the five reading series and the root files stay reader-facing.

If you arrived looking for the mathematics, go back to the [root README](../README.md).

| file | what it is |
|---|---|
| [`ARCHIVE_SURVEY.md`](ARCHIVE_SURVEY.md) | A pass through three discontinued repos kept as reference, asking of each piece: is it cited by the live collection, does it carry a result, or is it dead? Recovered one complete paper, 17 derivation modules, a plain-language field guide, a literature review, and six verification reports — and lists what was deliberately left behind. |
| [`WORKLOG_2026-09.md`](WORKLOG_2026-09.md) | The blow-by-blow of the September 2026 session: every route tried, the range it was measured on, the null it was measured against, and what came out. Dead ends included. |
| [`NOTES_Carry_Forward.md`](NOTES_Carry_Forward.md) | The keepers from that session — one entry per durable finding, each tagged with the paper it was folded into. Also the corrections, kept deliberately so wrong versions do not get re-derived. |
| [`check_repo_health.py`](check_repo_health.py) | Three checks for mistakes this repository has actually made and shipped: stray control characters (a scripted edit turning a LaTeX command into an invisible byte — this broke `\approx` and `\arctan` in `RESULTS.md` unnoticed), broken relative links, and **links to files git is ignoring** — the root `.gitignore` is an allowlist, so two "start here" documents were 404 on GitHub across three releases while passing every filesystem link check. Run it before tagging a release. |
| [`CONSOLIDATION_2026-07.md`](CONSOLIDATION_2026-07.md) | How four separate project repos became one collection in July 2026. Describes a folder layout that no longer exists; kept because its decisions still bind. |

## Why these are public

They record the collection correcting itself. Over one session in September 2026 this work retracted two published claims, corrected a theorem's threshold, flagged a percentage that only held at one range, found two circular rows in existing tables, and discovered it had proved the same conjecture twice from unrelated geometries without noticing.

All of that is in the papers where it belongs — but the *process* is here, and a reader deciding whether to trust the results may reasonably want to see it. [How We Know](../HOW_WE_KNOW.md) is the readable version.
