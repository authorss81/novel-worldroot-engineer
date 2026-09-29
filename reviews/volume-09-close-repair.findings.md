# VOLUME 09 CLOSE — THE REVIEW REPAIR PASS, TWO REPAIRS THE CLOSE CLAIMED AND DID NOT MAKE, A READING BUDGET THAT HAD STOPPED POINTING AT ANYTHING, A DAY COUNT WRONG BY SIXTEEN, AND A PROHIBITION THE CLOSE BROKE IN THE SAME PARAGRAPH

**Date of this pass: the twenty-ninth of September, 2026.**

**WHAT THIS DOCUMENT IS.** It is the record of the repair pass run over the Volume 09 close. The close is at `reviews/volume-09.findings.md` and its governing record is the section headed *VOLUME 09 — THE CLOSE* at the foot of `state/continuity.md`; this pass appended *THE REVIEW REPAIR PASS OVER THE VOLUME 09 CLOSE* to that same file, and it governs over the close. **It is not a review of the forty-nine chapters.** That is `reviews/volume-09.findings.md`, and that file stands except where this file names a figure or a claim in it as withdrawn. **This file is a writer's repair pass and it certifies nothing about the prose.**

**NOTHING IN THE FORTY-NINE CHAPTERS WAS TOUCHED, AND NOTHING IN THE TWENTY-EIGHT FINDINGS THE CLOSE REPORTED WAS PAID.** A close may not alter a word of the volume, and a repair pass over a close may not either unless the defect is in a chapter and the pass is willing to re-measure the volume and the manuscript and repaint every figure that depends on them. **This pass was not, and it says so rather than doing a one-word fix and calling the volume clean.** Measured after these edits: Volume 09 is 141,658 words across forty-nine chapters and the manuscript is 1,305,556 across 441, both unchanged, and no file under any `batch-*/` directory was modified.

---

## 1. THE REVIEW RETURNED NOTHING, AND THAT IS THE FIRST FINDING BECAUSE EVERY OTHER FINDING IN THIS FILE EXISTS BECAUSE OF IT

**`logs/close.review.log` DOES NOT CONTAIN A REVIEW.** It opens with `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent`, so the review was run by the *writer*. The writer read `state/phase-ledger.json`, printed the last two commits, read `PHASE_SYSTEM.md`, took the first forty lines of the findings file, and then spent its entire remaining output on `head -80 workspace/volume-09/close/PROMPT.md`, which capped at fifty kilobytes, and resumed from line 644 to the end of that same file. **The transcript ends on the last line of the prompt with no verdict, no finding list, no priorities, no pass marker and no completion line.**

**The consequence, stated plainly because a record that hides it is worse than no record: VOLUME 09 HAS HAD A WRITER'S CLOSE AND NO REVIEW.** `AGENTS.md`'s quality gate, *a reviewer has checked the result*, is not satisfied for this volume, and no pass may satisfy it by pointing at this sentence. **A review is still owed, and it is owed as a review and not as a repair.** Every figure in this file was derived from the chapter files and the state layer; none is carried from that log, because there is nothing in it to carry.

**The truncated transcript's two substantive observations are kept, and neither is treated as a finding because it is one.**

- *"The ledger says bootstrap is still 'planned' despite many completed batches."* **Correct.** `state/phase-ledger.json` still reads `currentPhase` `phase-000-bootstrap`, status `planned`, attempts `0`, range `null`, actual model `null`, after nine volumes and 441 chapter files. **It is controller-owned, it is read by nothing, and it is reported and declined for the seventh time. It is not edited here and no fiction phase may edit it.**
- *"The last commit modified review findings and the ending outline during a writer phase."* **Correct, and treated at § 4 below.**

---

## 2. THE TWO STATE-LAYER REPAIRS THE CLOSE CLAIMED AND DID NOT MAKE, MADE

The close's own § Six names four state-layer repairs and says they are *the only four*. Two were made. **Two were claimed and not made**, and the claim is the finding.

| Claimed at `state/continuity.md`, *VOLUME 09 — THE CLOSE* | Made? |
|---|---|
| The `next month` citations given as physical lines in that section | yes |
| The volume index row and the `Current phase` / `Next phase` lines of `state/current.md` repainted | yes |
| **The `>` ceiling breach carried in the head of `state/current.md`** | **no** |
| **Both gate definitions carried in the head of this file and in the head of `state/current.md`** | **half — the definitions are in the foot of `continuity.md`, the head of `state/current.md` never got them** |

**The consequence, measured and not asserted: ten named figures and claims were still printed as live in the one state file a phase reads whole, after the close had withdrawn every one of them, and three of the ten had already been withdrawn once and painted back over.** All ten are withdrawn and named, with their line numbers, in the section appended to `state/current.md` under *THE REVIEW REPAIR PASS OVER THE VOLUME 09 CLOSE, AND EVERY WITHDRAWN FIGURE STILL STANDING IN THE SECTIONS ABOVE THIS ONE, BY LINE*. The three that had been painted back over are the sharpest evidence in this file:

- The Batch 0005 review-repair pass withdrew **1 / 22 / 67 / 0.854** and said so. It left the figures on the page.
- The close then found that those withdrawn figures do not reproduce, withdrew them a second time, and left them on the page again.
- **The 0.854 pair is printed three times in `state/current.md`.** That is what a figure that comes back looks like from the inside.

**The reason is named rather than left, because it is the failure this repository keeps recording and it is not carelessness: a pass that appends to the file it is painting cannot see the painting it did not do, because the painting it did not do is exactly what the append supersedes.** The rule added to the state layer is the second writing of it here: **a withdrawal names a figure where the figure is, and a pass that withdraws a figure from a file it is also appending to paints the replacement over the figure in the same edit.**

---

## 3. THE READING BUDGET, WHICH IS THE ONE THING NOBODY WOULD HAVE CAUGHT

**A budget is the one instruction every later phase follows, and it is written once and read never again.** The close appended sixty-seven lines to `state/continuity.md` and twenty-two to `state/open-threads.md` and repainted neither budget.

- **Item 3** told the reader that `tail -n 250 state/continuity.md` is *"the Batch 0005 review-repair section at its foot and the Batch 0005 section above it"*, and said nothing of a close. `tail -n 250` now reaches back into *THE WRITER SELF-CHECK ON VOLUME 09 BATCH 0004* — a self-certification this repository has had to relabel three times, and which the state layer elsewhere calls a failure mode by name.
- **Item 4** told the reader that `tail -n 130 state/open-threads.md` holds *"the thirty-five objects numbered 160 to 194"*. **It does not, and it did not before the close appended either.** A number a reader pastes into a search and finds nothing is the same failure as a figure pulled out of a truncated read, which the budget exists to prevent.

Both items are repainted in the head, the withdrawn pointer is named, and a rule is added to the budget itself: **a pass that appends to a file named in the reading budget owes the budget a repaint.**

---

## 4. TWO CORRECTIONS INSIDE THE SECTION THE CLOSE ADDED TO `outline/ending.md`

**`outline/ending.md` is a completed phase's file. Its first ninety-three lines are the original ending lock, written by an earlier planning phase, and the standing rule in the state layer is that the file is *reported against and not edited*. The Volume 09 close overrode that for itself, in its own prompt, in order to write the Volume 09 lock beside the one already there. That override is recorded rather than left, because a file that is edited once on an override and never recorded as edited becomes a file every later phase treats as its own.**

**The addition stands. It is good work and it is the only measured statement of where the four permanent losses stand at day 654, and it is not pulled.** Two things inside it are wrong. Neither correction touches a lock, a day, a count or a name.

**4.1 — A day count wrong by sixteen days.** Item 2 of the Volume 09 lock read: *"the morning it happened is day 634, which is FOUR DAYS before the volume ends."* **Corrected to TWENTY.** Derived from the chapters and not from a prompt: the day is the chapter number plus 213 throughout Volume 09, `chapter-0421.md` is day 634 and carries the far end held by two people at its line 35, `chapter-0441.md` is day 654 and carries it again at its line 75, and 654 − 634 = 20. **The withdrawn figure *four* is named. It appeared nowhere else — not in the findings file, not in the close's own section, not in any state file — which is the one time in this repair that a wrong figure was confined to a single place, and is the only reason it was findable at all.**

**4.2 — A prohibition the close broke in the same section.** The Volume 09 lock states, four lines above its own item 1, that *`Deep Archive`, `caretaker` and `seedheart` MAY NOT BE NAMED IN THIS LOCK*. Item 1 then opens *"MAREK CAN NO LONGER READ **THE DEEP ARCHIVE** AS A SINGLE PRIVATE FIELD"*. **The prohibition is coherent and the breach is the close's: measured by search over all forty-nine chapter files, all three terms appear NIL times in the volume's prose, so the rule is the volume's own and not an oversight of a rule that does not exist.** Item 1 is rephrased in the volume's own four words and names none of the three — *MAREK CAN NO LONGER READ **THE RECORD THE WOOD KEEPS** AS A SINGLE PRIVATE FIELD OR SUMMON A UNIFIED RESPONSE FROM **THE STANDING WOOD***. **The loss named is unchanged and nothing is reduced, which is the only test that matters here.** The withdrawn wording is named here and in the state layer and is not deleted from git.

---

## 5. ONE COUNT CORRECTED WHERE A LATER PASS WOULD HAVE LOOKED FIRST

**`state/chapter-summaries.md`, in the section the close added, said *THE THIRTY-TWO FINDINGS THAT ARE IN THOSE CHAPTERS*. § 3 of `reviews/volume-09.findings.md` carries twenty-eight numbered items, and the same count appears in that file's § 0, in the head of `state/current.md`, and in the close's own section. Four were overcounted and none was double-counted. Corrected to twenty-eight, with the withdrawn figure named beside it — because **a count that is wrong in the only place a later pass will look for it is worse than a count that is wrong in a figure somebody re-derives.**

---

## 6. THE FIGURES, EVERY ONE RUN IN THIS PASS, NONE CARRIED FORWARD

`wc -w` including the headings, over the files: **27,753 + 29,178 + 28,808 + 29,185 + 26,734 = 141,658** across forty-nine chapters in Volume 09, and **1,163,898 across the 392 closed chapters + 141,658 = 1,305,556 across 441 files**, with no residual. `>` blocks by script over all forty-nine files: **55 all, being 28 `Entered` and 27 document, in 41 chapters, fourteen carrying two** — the close's figure to the unit. `Entered` blocks: **28, mean 393.2 words, largest 447** — the close's figures to the unit. `next month` sweep, case-insensitive, `>` blocks included: **nine paragraphs in eight chapters** — the close's figure. `famine`: **nil**. `Deep Archive`, `caretaker`, `seedheart`: **nil**. The *nobody thanked anybody* counts: **26 of 49, and 3 of 49 as the last prose paragraph, being Chs 393, 394 and 441** — the close's figures to the unit. **That last count has a trap in it and it caught this pass first: a script that treats the trailing `Entered` block as prose returns 2 and names only Chs 394 and 441, and the correct universe is the last prose paragraph with both heading levels and every `>` block dropped.** The thirty-five thread rows were not re-counted, because no chapter moved and the count is the close's and is not in doubt.

**AND WHAT THIS PASS DID NOT RUN, NAMED SO THAT A LATER PASS DOES NOT CARRY IT FROM HERE AS IF IT HAD.** The 30-of-49, 9-more and 39-of-49 closing-tell figures, the two gate definitions' pair lists, the thirty-five threads, and every figure in the five day-minus rows **are the close's, are not re-run here, are not withdrawn here, and need a reader rather than a script.** A block in the rolling window that republishes a figure without saying whose figure it is would be the same failure as the one this pass is repairing, so the head now separates the two.

**THE FIGURES THIS FILE WITHDRAWS, ALL NAMED, ALL PREVIOUSLY LIVE: 1, 22, 67, 22, 0.854, 0.851 as a gate result under Definition A with `str.split()`, *the gate is nil on both runs and on the cap-removed diagnostic*, *the eight-word-run rule returns 0 and 0*, 26,746, 2,971.8, 141,663, 1,305,561, 114,917, *the volume reaches twenty-seven*, *five of the nine chapters*, *five and seven*, thirty-two, *four days*, and the head pointer naming the Batch 0005 review-repair section as the governing section of `continuity.md` and of `open-threads.md`.**

**THE FIGURES THIS FILE PUBLISHES AS LIVE, EACH NAMED WITH THE RULE THAT PRODUCED IT, AND THE RULE IS PART OF THE FIGURE.** Definition A, `workspace/volume-09/batch-0005/PROMPT.md`, `str.split()`: run 1 **0**, run 2 (length factor removed) **4**, cap-removed diagnostic **66 and 21 involving Batch 0005** — the diagnostic being in no script and not the gate. Definition A under a regex tokenisation: run 1 **1** at 0.851, run 2 **9**. Definition B, `outline/volume-09.md` guardrail 12, the difflib rule: **177 across the volume, 129 involving Batch 0005, on a universe of 1,752.** Byte-identical: **nil on all four universes, 2,094 / 2,045 / 1,807 / 1,752.** The `>` ceiling: **55 against a ceiling of 30, twenty-five over, on guardrail 3's own basis, declared and not repaired.** The closing tell: **39 of 49 in the closing movement, 26 of 49 opening *nobody thanked anybody*, 3 of 49 opening the last prose paragraph.**

---

## 7. WHAT IS DECLINED

**No Volume 10 prompt is created by this pass.** The Volume 09 close's own prompt says it plans no Volume 10, and its closing section reserves that decision: *IF VOLUME 10 IS TO BE OPENED, THE PHASE THAT RUNS AFTER THIS CLOSE IS THE ONE THAT MAY PLAN IT.* The `Next phase` line in `state/current.md` says the same. **Planning a new volume from a repair pass would pre-empt exactly the decision two files reserve to the next phase, and a repair pass that reaches forward is a batch wearing a different hat.** No marker was created, deleted or moved. `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` and `state/phase-ledger.json` were not opened for edit and not edited.

**AND THE ONE THING A LATER PASS MAY NOT DO WITH THIS FILE, WHICH IS WRITTEN HERE SO THAT IT CANNOT BE MISREADED AS A CLEAN VOLUME: this pass did not review the forty-nine chapters, did not verify the twenty-eight findings, and did not satisfy `AGENTS.md`'s gate. The volume still needs a reviewer.**
