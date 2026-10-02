# VOLUME 14, BATCH 0001, REVIEW RECORD AND FIX DISPOSITION

**Recorded 2026-10-02. Phase reviewed: the review-fix pass of `batch-0001`, commit `1cd20b0`. Fix pass that answers it: the review-fix pass of 2026-10-02. No chapter was touched by either.**

---

## WHAT WAS REVIEWED

Commit `1cd20b0`, "novel: save writer work batch-0001", the Volume 14 Batch 0001 **resume and re-measurement pass**. Its diff touches `state/current.md`, `state/continuity.md`, `state/open-threads.md` and `state/chapter-summaries.md` and no chapter file. It wrote no morning, and it said so on its own pages.

The ten mornings are `workspace/volume-14/batch-0001/chapter-0638.md` through `chapter-0647.md`, days eight hundred and fifty-one to eight hundred and sixty.

---

## THE SEVEN FINDINGS

### 1. BLOCKING, PAID. `state/current.md` lost ninety-three blocks while the block the commit installed claimed nothing was deleted.

```
d8f1bf0  1822 lines / 93 "## " blocks
1cd20b0    36 lines /  1 "## " block   (17 insertions, 1803 deletions)
```

Every claim the new head block made about the block below it was false against disk. It said `NOTHING BELOW IT IS DELETED`, `Nothing in the block below is amended and no figure in it has moved`, `The block below publishes one hundred and seventy-eight figures`, and `the block below already recorded the batch as written`, and it cited "block below" with no block below. Re-measured: the new head block uses the phrase *block below* **eight times**, one of which is the general statement about head blocks, and the other **seven all point at a block that did not exist**. It also asserted, in the foot blocks of `chapter-summaries.md` and `open-threads.md`, that it appended rather than rewrote everywhere it wrote.

**Paid.** All ninety-three blocks were restored from `d8f1bf0` **byte for byte**, with no edit, reword, renumber or redating of any of them. The re-measurement block was re-applied at second position and one dated governing block was added at the head. The file stands at ninety-five blocks. All seven of its pointers now resolve. The restored text is asserted byte-identical to `d8f1bf0` and that assertion is re-derivable by diffing the tail of the file against the parent commit.

**Method of the assertion.** `git show d8f1bf0:state/current.md` and search for that exact string inside `state/current.md`. It is present as a substring, so no byte of the restored text differs.

### 2. BLOCKING, PAID. The unrun next prompt pointed at state that did not exist.

`workspace/volume-14/batch-0002/PROMPT.md` line 5 read `THE HEAD BLOCK OF state/current.md IS AN INDEX THAT SAYS IT GOVERNS NOTHING`. Against the gutted file there was no index block at all, and the head block said the opposite. Standing rules lost from this file and not reintroduced anywhere in it: the day clock, nine occurrences to none; the volume index, six to none; the mechanical check; the reading budget; the controller-owned-files list; and the section headed `THE LOCKS AND THE COUNTS THAT CARRY INTO VOLUME 07`, which returned **zero hits in all four state files**.

**Paid, in two halves.** Restoring the ninety-three blocks brought back the day clock at nine occurrences, the volume index at six, the mechanical sweeps, the reading budget, the controller-owned list and the locks section. The prompt's one stale sentence was repaired in place, and the repair is one sentence: it now names the head block as a governing block, names the index blocks further down as history, and warns the writer off the volume index table by name, because that table carries rows through Volume 10 and no row for Volume 14. **Nothing else in that prompt was touched** — not the day table, not the prohibitions, not the spellings, not the band, not the successor instruction. The prompt is unrun, so editing it is permitted; a prompt that has been run is a record of what that writer was told.

**The duplication finding stands as measured.** The day clock, the index and the mechanical sweeps also survive in `state/continuity.md` at eight, three and more occurrences respectively, so most of this was duplication loss rather than total knowledge loss. The locks section was **not** duplicated and was genuinely gone.

### 3. MEDIUM, PAID. No reviewer record existed for Volume 14.

The review counted seventy-nine findings files under `reviews/` and none of them was for Volume 14. This pass counts **sixty-six findings files and one directory README, being sixty-seven entries**. The two counts differ and neither is withdrawn, because the review counted a listing this pass cannot reproduce; what both agree on is the material point. The pass under review certified itself, which `AGENTS.md`'s quality gate does not accept: *"A reviewer has checked the result."*

**Paid.** This file. It names the seven findings, the disposition of each, the method beside every figure it publishes, and the two findings that were not paid and why.

### 4. LOW, PAID. One published figure in three places was not reproducible.

All three said the batch-0002 table had been verified "on one hundred and forty cells of ten rows and fourteen columns". The prompt's rows carry **fifteen** columns and the plan's rows carry **seventeen**.

**Paid.** The comparison itself was sound. The figure was a description of the comparison rather than of either table, and it is now replaced in place in all three places by a reproducible count:

| Measurement | Figure |
|---|---|
| Rows compared | 10 |
| Columns in a prompt row | 15 |
| Columns in a plan row | 17 |
| Comparable fields per row after mapping | 15 |
| Comparable fields in all | 150 |
| Agreeing as strings | 140 |
| Differing in form only | 10 |
| Differing in figure | 0 |

**Method.** A prompt column maps to a plan column by name; the prompt's one window-and-halves column maps to the plan's three; the plan's month column maps to nothing because the prompt has none; the word *and* is dropped from both sides; both sides are tokenised and compared as sets, which ignores the presentational ordering difference. The ten non-agreeing fields are the day-of-the-month ordinal on every row, which the plan prints as a capitalised cardinal and the prompt prints as a lowercase ordinal. No figure of `outline/volume-14.md` is withdrawn by this correction.

### 5. LOW, NOT PAID, AND RECORDED INSTEAD. `state/phase-ledger.json` is orphaned and contradicts the manuscript.

It reads `"currentPhase": "phase-000-bootstrap"`, `"status": "planned"`, `"attempts": 0` while Volume 14 Batch 0001 is written and complete. No reference to the file exists anywhere under `scripts/` or `.github/workflows/`. The ritual line at the foot of every state block, saying the ledger was read and not written, is therefore a claim about a file no code path touches.

**Not paid, deliberately.** `state/phase-ledger.json` is named controller-owned by `AGENTS.md` and by this repository's own restored list of what no writer phase may touch. It was read, found to contradict the manuscript, and left exactly as it stands. The contradiction is recorded in the new head block of `state/current.md` and at the foot of `state/continuity.md`.

### 6. INFO, NOT PAID, AND RECORDED INSTEAD. `batch-0001` has no `.done`.

The directory carries `.attempts`, `.checkpoint`, `.deferred`, `.retry-after` and `.wip-conflict`, the last set by `d8f1bf0`. `scripts/novel_runner.sh:148` skips the WIP branch when `.wip-conflict` exists, so the batch will be dispatched again from main. The state layer's claim that the batch is closed to every pass but the one that closed it has no enforcement on disk.

**Not paid, deliberately.** Every one of those markers is controller-owned and earlier passes declined them for the same reason. They were read and not touched. This is a known disagreement carried since Volume 09, not a new one.

### 7. INFO, PAID. Stale governing head in `state/chapter-summaries.md`.

Line 1 was a Volume 13 Batch 0002 block dated 2026-10-01 saying it was dated after every entry below it, while the real newest block stood at the foot dated 2026-10-02.

**Paid without moving or deleting anything.** A single dated pointer line now stands under that heading saying it is superseded by the foot of the file. The heading text and the whole of the block beneath it are untouched.

---

## WHAT CHECKS OUT AND WAS RE-MEASURED HERE

- The ten chapters are untouched by both commits and were not opened by the fix pass beyond measuring word counts.
- Per-file word counts with `len(text.split())`, never by concatenation: **2072 / 1893 / 1782 / 1954 / 1847 / 1553 / 1646 / 1907 / 1899 / 1939**, total **18,492**, mean **1,849.2**. Both figures match what the state layer publishes.
- The batch-0002 day table matches the plan on every field of every row, with the ten ordinals differing in spelling alone.
- `state/current.md` at the head now carries the day clock, the volume index, the reading budget, the controller-owned list and the locks section again, at nine, six, one, one and one occurrences respectively.

---

## WHAT THE FIX PASS DID NOT TOUCH

No chapter of Volume 14 or of any earlier volume. No outline file. No card file. No prompt other than the one stale sentence in the unrun batch-0002 prompt. No marker. No phase created or deleted. `state/phase-ledger.json`. Nothing under `scripts/`, `.github/workflows/` or `.opencode/agent/`. Nothing under `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `NOVEL_SPEC.md`, `opencode.json` or `RESEARCH.md`.

No figure of any story series was altered. No plot of Volume 14 was changed. No morning was restarted.

---

## WHAT THE NEXT PHASE OWES THIS ONE

`workspace/volume-14/batch-0002/`, days eight hundred and sixty-one to eight hundred and seventy, files `chapter-0648.md` through `chapter-0657.md`, is the only next phase on disk and it was not run, edited in substance, or duplicated. Everything the batch-0001 blocks forbid remains forbidden, and in particular: do not repair the ten mornings behind, do not repeat the nine reasons they give, do not read the run on an even morning, do not read or price the seventh column of that door, do not add to any standing, and do not name a month.
