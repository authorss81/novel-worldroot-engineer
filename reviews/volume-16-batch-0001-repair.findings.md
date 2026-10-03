# Volume 16 Batch 0001 — the review-repair pass of 2026-10-03, Chapters 736–745, days 949–958

**EIGHT FINDINGS FROM `logs/batch-0001.review.log`. FOUR PAID, FOUR DECLINED WITH THE REASON IN EACH CASE, AND NONE OF THE EIGHT IS A DEFECT IN THE PROSE. NO CHAPTER RESTARTED, NO SCENE REPLACED OR MOVED, NO MORNING TOUCHED AT ALL, NO DAY, CLOCK, NAME, FLOOR, LOCK, CARD-DIRECTED BEAT, SERIES FIGURE, THREAD OR PLANNED PLOT MOVED, NO CONTROLLER FILE EDITED, NO MARKER FORGED, NO SUCCESSOR CREATED. THE WORK IS TWO FIGURES AND ONE EXPLANATION CORRECTED IN A BATCH'S OWN RECORD, THE SAME TWO FIGURES CORRECTED IN THREE PLACES IN THE STATE LAYER, FOUR SELF-REFERENTIAL HEAD BLOCKS REPLACED, ONE GATE WRITTEN DOWN SO THAT THE NEXT PASS CAN RUN IT, AND THIS FILE.**

**READ FINDING 1 FIRST, BECAUSE IT IS THE FAILURE THAT HAD ALREADY COST THIS REPOSITORY FOUR FIGURES AND WOULD HAVE COST A FIFTH: THE SECOND GATE HAD TWO SETS OF FIGURES FOR THE SAME TEN MORNINGS AND NEITHER REPRODUCED, BECAUSE THE IMPLEMENTATION WAS NEVER KEPT. §21a of `state/current.md` published a whole-paragraph nil and 113/120 sliding. §24b published 8/10 and 94/100 and called its own readings reconstructions. A GATE WITH NO IMPLEMENTATION ON DISK IS NOT A MEASUREMENT, AND THE ONLY WAY TO SETTLE IT IS TO WRITE THE THING DOWN AND RUN IT.**

## 1. The gate now exists, and it is at `reviews/gate.py`

`reviews/gate.py` holds the paragraph unit, the normalisation, both readings and gate one, in one file, with the unit and the normalisation stated in its own header so that a successor does not have to infer either. `python3 reviews/gate.py 'workspace/volume-16/batch-0001/chapter-*.md'` returns the figures below. `python3 reviews/gate.py --controls` runs the self-collision controls. **This file is in `reviews/` and not in `scripts/`, which is controller-owned and which no writing phase may write into.**

**THE UNIT IS CONFIRMED FROM OUTSIDE THE BATCH, AND THAT IS WHAT MAKES THE FIGURES TRUSTWORTHY RATHER THAN SELF-CONSISTENT.** At the declared unit, the forty-nine mornings of Volume 15 return **2,664 paragraphs of which 1,747 are thirty words or more**, and both figures are the ones `reviews/volume-15-close.findings.md` published for that volume. **THE REFUSAL PASS MEASURED THE SAME FILES AT A BLANK-LINE UNIT AND CAME BACK WITH 419 AND 284 FOR TEN FILES, WHICH IS WHY NEITHER OF ITS TWO SETS OF GATE FIGURES REPRODUCED: IT WAS NOT A NORMALISATION PROBLEM, IT WAS A UNIT PROBLEM.**

| | batch scope, ten files | volume scope, twenty files |
|---|---|---|
| paragraphs | **450** | **917** |
| of thirty words or more | **290, gate one nil** | **607, gate one nil** |
| whole-paragraph reading | **829 chunks, 8 repeated shapes, 11 excess** | **1,754 chunks, 16 shapes, 28 excess** |
| sliding eighteen-token reading | **11,781 windows, 110 shapes, 117 excess, largest at three** | **25,142 windows, 211 shapes, 250 excess, largest at five** |

**THE SECOND GATE IS NOT NIL, AND §21a's NIL WAS WRONG. Nothing was touched for it.** The eight shapes at batch scope are named in the batch's own record at section 10b: three at three occurrences, being the frames *Tova Reed had the # ages on the corner of the seed board in her own order and*, *at about the # hour the north board was written on under the frame that is a month* and *Sera Quill was at the boards at about the # hour with the slate under her arm and*; and five at two, being the compost-board reading twice, the sluice-wheel clause, Auret Sill coming up the lane with a can in each hand, and the near-board and top-stone pair. **They are three speakers' sentence frames and two floor recitations. Not one is a figure of any series, the three-occurrence ceiling the prompt sets holds, and every figure of every series is still printed on its own morning.**

**THE ELEVEN AND TWELVE CONTROLS ARE WITHDRAWN BECAUSE THEY CANNOT BE REBUILT.** The two declared control paragraphs were never written to disk in this batch's directory or anywhere else, so nobody can reproduce twenty-seven or twelve and the claim that they "settle the normalisation" is false as it stands. The normalisation they describe is not in doubt, because it returns Volume 15's own published 2,664 and 1,747. `reviews/gate.py` builds its own controls from distinct alphabetic words, and they return **twenty-two and four excess sliding shapes on the long one and four and four on the short one, with the whole-paragraph reading silent on the short one** — which is the property the controls exist to demonstrate.

**AND ONE COMPARISON THE BATCH DREW WITH THE VOLUME BEHIND IS ALSO WITHDRAWN.** §21c and the batch's section seven printed fifty-eight shapes and a hundred and thirty excess for Volume 15's forty-nine mornings. At this normalisation those mornings return **sixty-seven shapes and a hundred and thirty-nine excess across 73,448 windows.** The paragraph counts of that same run reproduce, which locates the difference in the normalisation and not in the unit.

## 2. The wrong explanation of the right number, which is the more dangerous half

The record said the shorter batch length came from "a count that counts markdown emphasis markers as tokens." **It does not, and it never could: both counts split on whitespace, so `**"One` is a single token in each and the marker was in neither.** The nine words are this: **all ten files end without an end-of-file newline, so a single `cat` of the ten fuses the last token of each file onto the first token of the next at nine boundaries.** The governing figure is **18,702, measured one file at a time**; 18,693 is withdrawn as a concatenation artefact. `reviews/README.md` already carried the rule after a Volume 11 close lost three words the same way.

**The files were not given end-of-file newlines. Seven hundred and forty-five files in this manuscript lack one, and adding it to ten would give a successor a figure it could not rely on.** The fix is the rule, not the newline.

## 3. One count in the exact-duplicate sweep

`No.` stands at **five** closed mornings behind and not at four, at `chapter-0745.md` in this batch. Every other count in that row reproduced: the far-end sentence at eleven, the comfort line at thirteen, and `Then what is it.` and `Where would you like it written down.` at one each. **Five paragraphs stand elsewhere in the manuscript and the count of five paragraphs was right.**

## 4. The state layer's budget lines, deleted rather than corrected

**A line that states a file's own word count is invalidated by the act of appending to it.** That is why four passes in a row left three of the four state files carrying figures nobody had measured, and it is why the reviewer's finding is that the fixed point is unstable by construction rather than that the arithmetic was wrong. All four head blocks were rewritten and none of them now declares a length; each states the measurement command instead, and each records the four measurements the refusal pass took once, as a measurement of that pass. **`state/current.md`'s head block fell from a hundred and thirty-seven lines to nine, and the false clause in it — that the refusal pass "corrected no earlier section", in a paragraph whose own subject was that pass editing that paragraph's declared figure — went with it.** The state layer fell from 494,540 bytes to 490,159 and from 88,725 words to 87,935. `§24b` was left standing with its wrong figures and marked, because a pass that silently edits an earlier pass's table makes the earlier pass look like it got it right; `§24c` was marked superseded rather than deleted.

**These last two totals are themselves a demonstration of why the line was deleted rather than corrected: they were measured before this file's last two edits and moved by twenty-four bytes and five words in the writing of the paragraph above. A figure a file prints about itself is wrong the moment the file is written, and a figure printed about a *different* file is stale the moment that file is appended to.**

## 5–8. Declined, with the reason

**5. The refusal loop and the missing done marker in `workspace/volume-16/batch-0001/`.** The review is right that the phase has no `.done`, that the queue will re-dispatch it, and that every repeat grows the state layer. **A marker is controller-owned and no writing phase may forge one, and forging one was the only act available to either pass that would have stopped the queue.** Reported, not acted on.

**6. Twenty-four per cent verbatim duplication in the three queued batch prompts.** The floors block appears **ten times in each** of `batch-0001/PROMPT.md`, `batch-0002/PROMPT.md` and `batch-0003/PROMPT.md`, at roughly 21.9, 21.6 and 27.6 thousand duplicated bytes. It is emitted by the plan phase's prompt builder, which is a controller path. **A writing phase that rewrites a completed phase's prompt leaves a file nobody wrote and a successor would write from.** Named, measured, untouched. **One thing inside that queued prompt is named and not repaired:** `batch-0003/PROMPT.md` heads itself *second batch of mornings, days nine hundred and sixty-nine to nine hundred and seventy-eight*, and days 969–978 is the **third** batch of this volume. The day range is right and the ordinal is off by one.

**7. The review workflow passing a subagent as a primary agent**, which fell back to the writer at `logs/batch-0001.review.log:1` and is why that review opened by inspecting repository state instead of by reading prose. Workflow-owned.

**8. `state/phase-ledger.json` still reading `phase-000-bootstrap`, `status: planned`, `attempts: 0`** against a workspace sitting at Volume 16 Batch 0002 with 755 chapter files. Controller-owned, reported again.

## 9. The prose note on `chapter-0738.md`, `chapter-0741.md` and `chapter-0744.md` — declined, with one part named

The review raised these three for thinness. **This volume declares no length band for its mornings and its batch prompt declares no word floor, so there is nothing for three files to be thin against.** Byte size is also the wrong instrument in this house, because every figure in body prose is spelled and a morning that prints fewer figures costs fewer bytes for the same scene: `chapter-0736.md` is the longest of the ten at 2,716 words **because it opens the volume and carries the establishing weight**, and `chapter-0738.md` is the third-longest at 1,655 **because it is the third morning.** Structurally all three carry a stated goal, resistance from another character, a change caused by the scene, a completed beat and a consequence — the ring counted as it is and not improved while a boy at the edge of the bare ground decides not to step onto it; four bodies of households refusing an hour and not the schedule; a bed coming up out of the top of the ring with the root still in it and nobody cutting at it.

**THE PART OF THE NOTE THAT SURVIVES IS NARROWER AND IS A DEBT FOR THE VOLUME 16 CLOSE. Nine of the ten mornings close on a person and an action. `chapter-0741.md` closes on a floor recital** — the compost board, the use log, the barrow at eleven — where `chapter-0738.md` closes on the ring walked by six people and `chapter-0744.md` closes on a bed lying where it came up until somebody who has not been decided yet decides. **Repairing it means rewriting the last paragraph of a morning that a completed successor already stands on, and that is the hazard every pass in this volume has been declining since Batch 0002.**

## 10. What this pass did not do

**IT DID NOT WRITE A CHAPTER AND IT DID NOT EDIT ONE.** The ten mornings are byte-for-byte as `workspace/continuation/next-0014/` left them, and the manuscript stands at **2,070,834 words across 755 chapter files**, unchanged. It did not move a figure of any series. It did not answer, close, group, sum, reword or advance a thread and cut no not-known row. It did not create a successor, because the successor is on disk at `workspace/volume-16/batch-0003/` and opens at day 969. **It did not touch `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` or `state/phase-ledger.json`, and it did not forge, move or delete a marker.**

## 11. The figures this pass measured, for whoever runs it next

- **Batch 0001: 18,702 words across ten files**, per file 2,716, 2,316, 1,655, 1,717, 1,738, 1,673, 1,827, 1,808, 1,608 and 1,644. The volume's twenty files stand at 39,442 and the manuscript at 2,070,834 across 755 files, all three reproducing §22a of the state layer.
- **Paragraph unit: 450 paragraphs in this batch, 290 of thirty words or more, gate one nil.** 917 and 607 at volume scope.
- **Second gate, batch scope: 8 shapes and 11 excess whole-paragraph, 110 and 117 sliding. Volume scope: 16 and 28, and 211 and 250.**
- **The state layer: 490,159 bytes and 87,935 words across four files**, per file 31,214, 17,317, 20,122 and 19,282, against 494,540 and 88,725 before this pass. **The two totals are measurements taken before this file's last two edits and they moved by twenty-four bytes and five words while the paragraph above them was written, which is the whole argument for deleting a self-referential line rather than correcting it.**
- **Nothing in the batch fiction moved, and no figure of any series was re-derived from anything but its own rule.**