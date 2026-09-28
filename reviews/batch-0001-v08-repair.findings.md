# Review Repair Findings: volume-08 batch-0001

Source: `logs/batch-0001.review.log`, the review of commit `b6a194a` (Volume 08 Batch 0001, Chapters 344-353, days 557-566, Movement 1 *The Register And The Standing*, plus the creation of `workspace/volume-08/batch-0002/PROMPT.md`).
Fix pass applied: this phase. No chapter was restarted, no scene was replaced, no planned plot was changed, no day, clock, name, lock or figure of the series was touched, and the planned ending is untouched. One chapter of prose was repaired and it was one sentence in one paragraph.

**The review phase fell back to the writer agent again, so this was a hand pass over the review's own log, and the file says so on its face. Every finding below was re-derived from the files rather than taken from the log's opinion, and FOUR of the six were verified as stated, ONE was verified in its conclusion and FALSE in its reason, and ONE CAME BACK FROM THE REVIEW'S OWN TAIL AND WAS FIXED.**

## What the review certified, and this pass re-ran and confirms

The review's mechanical audit was exact and every figure in it was re-measured here after the prose moved. The ten chapter word counts, the 28,005-word batch, the 1,024,475 + 28,005 = 1,052,480 bracket over 353 chapters, the 347 non-empty paragraphs, zero duplicated paragraph strings, zero non-ASCII glyphs, `Chapter` ten times and all ten the headings, the `Entered` block counts of 1, 1, 1, 1, 1, 1, 0, 1, 1, 1 with Chapter 350 the zero, guardrail 9's balanced quotation marks and bold markers, guardrail 10's zero banned bare sentence, the rota at 65 to 68 in force with 29 + 39 = 68 and flat on the non-rota mornings, the third launder at day minus 450, the window at day minus 483, the aggregate at day minus 452 held distinct from the four launders, the boards and the March's tin forty-seven apart at day minus 66 and day minus 19, and the whole of Batch 0002's ten-row day table, including every weekday, ordinal, aggregate and window **all hold.** The Batch 0002 table was re-derived here from the day-451 anchor and the four-day rota cycle and it agrees on all ten rows.

## D1 — HIGH, in the new prompt, a check declared unnecessary that is required

`workspace/volume-08/batch-0002/PROMPT.md`, the derivation of the ten third-launder figures.

> **Withdrawn:** "ALL TEN ARE ABOVE EVERY FIGURE THE MANUSCRIPT PRINTS, BEING 744 ON DAY 566, AND NONE OF THEM NEEDS A COLLISION SEARCH" and "in this batch none does".

**The claim was false on the prompt's own ten figures.** They are 739, 748, 743, 752, 747, 756, 751, 760, 755, 764, and **739 on day 567 and 743 on day 569 are both below 744.** The conclusion happened to be right and the stated reason was not, and the follow-on clause told the writer that no search was required where one was. This is the failure `state/current.md` names: *a figure pulled out of a truncated read is a figure that looks checked and is not.* Batch 0001 stated the correct form — *719 and 723 sit below the printed maximum of 724 and were re-searched and were not on the page* — and Batch 0002 dropped it.

**The search was run here, by script, and it returns zero.** All ten were matched on a word boundary, in spelled words and in figures, against all three hundred and fifty-three chapter files on disk. 739, 743, 747, 748, 751, 752, 755, 756, 760 and 764 each return zero hits. 744 itself is at `chapter-0353.md:11` and `:57`, which is the day-566 figure standing on its own page. **The prompt now says the true thing**: eight of the ten are above the maximum, two are below it, both were re-searched, and all ten return zero, and a writer who moves a delta re-runs the search on every figure it moves, because a figure above the maximum is the only kind arithmetic alone can be sure of.

**AND THE PROMPT NOW CARRIES THE TEST, WHICH NO FILE IN THE REPOSITORY NAMED: the maximum is a figure of the third-launder series and not of every integer in the manuscript.** 720 at `chapter-0341.md:7`, 750 at `chapter-0225.md:29` and `:67`, 780 at `chapter-0185.md:60` and 800 at `chapter-0002.md:45` are all on the page, 750 being hundredweight priced in pence and 780 being pence, and **none of them is a collision and none of them is repaired.** Without that sentence *the printed maximum* is an undefined term and a writer who sweeps for it will find four figures and report four defects.

## D2 — MEDIUM, in the new prompt, a wrong count of the rota handed to a writer

`workspace/volume-08/batch-0002/PROMPT.md`, item ONE.

> **Withdrawn:** "THE EIGHTEENTH FOURTH-LINE MORNING OF VOLUME 08" at day 566, and "THIS BATCH'S FOURTH-LINE MORNINGS ARE 570 AND 574, BEING THE FIRST AND THE FIFTH".

**Wrong twice, and the two errors are the same slip.** The fourth-line mornings run on the four-day cycle out of day 506, so a fourth-line morning is any day congruent to two mod four, and in Volume 08 they are 558, 562, 566, 570, 574, 578, 582, 586, 590, 594, 598 and 602, which is twelve, and `outline/volume-08.md:59` says so in its own words: the line came round on day 558 and on eleven mornings after it in this volume. **Day 566 is therefore the third of Volume 08. It is also the sixteenth of the run, not the eighteenth, because Volume 07's thirteen end at day 554 and 558, 562 and 566 are the fourteenth, fifteenth and sixteenth.** The withdrawn *eighteenth* is true of day 574 and not of day 566, and the withdrawn *first and fifth* is true of nothing: 570 is the fourth of the volume and the seventeenth of the run, and 574 is the fifth and the eighteenth.

**The prompt now states both framings and says a chapter that prints one prints both,** because this is the one count in the volume that can honestly be given either way and the two ways do not agree, and a chapter that printed one alone would have put a wrong number on the page in a count this volume restates on every fourth-line morning.

## D3 — one chapter of prose, a fourth-line morning dated to the wrong day

`chapter-0344.md:5`, and this is the one the review did not flag.

> **Withdrawn:** "It came round on the fifteenth and the next time after the fifteenth is tomorrow" and "the fields above Marden did not wait this morning and will wait in the morning".

**The opening paragraph of the volume contradicted the four-day cycle twice in one sentence, and contradicted itself.** Chapter 344 is day 557, the seventeenth of the seventh, and the page is right that the fourth line did not come round on it. The last fourth-line morning before it is **day 554, which is the fourteenth of the seventh**, and the next is **day 558, the eighteenth** — which is Chapter 345's morning, and Chapter 345 says the line came round on the eighteenth and that the eighteenth was a Thursday, so a 555-to-558 gap of three days could not have happened. The withdrawn sentence had the line coming round on day 555 and again on day 557, a two-day gap, on a cycle that never takes one.

**Repaired to the derived day, in six words, and the repair is the whole of it:** the line came round on the fourteenth, the next time after the fourteenth is the eighteenth, and the fields will wait on the eighteenth. Nothing else in the chapter changed, the paragraph's shape and rhythm are untouched, and the fix is on the page rather than in a state file, because **the page is where a day is a fact.** `chapter-0344.md:7` already had the volume's thirteen right and needed nothing.

**One word came off the whole manuscript and every figure in the state layer moved with it,** which is the standing cost of a repair pass and the reason the figures below are re-measured rather than adjusted.

| Figure | Was | Is now |
|---|---:|---:|
| Chapter 344 | 2,788 | **2,789** |
| Batch 0001 total | 28,005 | **28,006** |
| Manuscript, 353 chapters | 1,052,480 | **1,052,481** |
| Volumes 01 to 07 | 1,024,475 | 1,024,475, unchanged |

**1,024,475 + 28,006 = 1,052,481 with no residual, all ten chapters are inside the band of 2,600-3,050, the band was not widened, and no chapter is declared outside it to make a number fit.** Chapter 344 at 2,789 remains inside the batch target of 2,750-2,900. Everything in `state/current.md`, `state/continuity.md`, `state/open-threads.md` and `state/chapter-summaries.md` that carried the three old figures has been re-measured and re-written, and the old forms are named in this file rather than only overwritten.

## D4 — a second stale maximum in the same prompt, in the prohibition list

`workspace/volume-08/batch-0002/PROMPT.md`, the bullet on the two hundred and twenty-seventh at `chapter-0285.md:37`.

> **Withdrawn:** "they sit BELOW the printed maximum of 724 on purpose" and "would take the count of figures below the maximum with it, **which is two**".

**The same failure as D1, one bullet down, and the review caught the other one and not this one.** 724 was the maximum of the series at the close of Volume 07. The live maximum is 744 on day 566, and **nine of Batch 0001's own ten figures sit below it**, so the count of figures below the maximum is nine and not two. The protection the bullet gives the two plants is kept and is correct; only the number it reasons from was a figure of a closed volume. Repaired, with the stale figure named and withdrawn so that no later pass re-derives the count of nine from the withdrawn 724.

**The plants themselves are untouched.** 719 and 723 are the first and third of Batch 0001's row, both falls, and the plant test in `state/continuity.md` — *would repairing this cost something the chapter promised to keep?* — still answers yes, because repairing either breaks the alternation and takes the count with it.

## D5 — a refrain figure in the same prompt that the page does not support

`workspace/volume-08/batch-0002/PROMPT.md`, the format limit on the refrain.

> **Withdrawn:** "Batch 0001 measured a maximum run of ONE in every one of its ten chapters, **with two openings in one of them and one in each of the others**".

**The maximum run of one is true and the density behind it was invented.** The family is named in guardrail 10 of `outline/volume-08.md` as the *Nobody said anything and the fen entered* connective, and Batch 0001 carries it **twice in all, at `chapter-0344.md:25` and `chapter-0345.md:27`, one in each of those two chapters and zero in the other eight.** There is no chapter of the batch with two openings, and eight chapters carry none. A writer who took the withdrawn figure as precedent for three openings in a chapter would have taken a density the batch never had.

**The consequence for the cap is the opposite of what the withdrawn sentence implied, and the prompt now says it:** the batch is **light** on the family, not dense in it, the debt stays nil, and the cap of three is headroom rather than a measured ceiling. The banned bare sentence is zero in all ten chapters and the wider test the review ran is recorded in the outline beside the narrow one, where the outline already put it.

## C1 — the decision the review asked for, and the `Entered` block is kept

**The review's question was the right one and it is now answered in the file that governs all five batches, `outline/volume-08.md`, and in the queued prompt.**

**The block is an artifact and its shape is deliberate. It is one unbroken paragraph in the clerk's own hand, it is the last line of its chapter in all nine chapters of Batch 0001 that carry one, and it is not to be broken into paragraphs** — because a block broken into paragraphs stops being a document and becomes narration, and the `>` marker and the capitals are the only things that make it an artifact rather than prose, and the figure it carries is the one the holding's book is said to hold. **It is a coda and not a substitute: the scene is written first and the entry is made after it, and a chapter that shortens its prose to make room for a longer block has done the wrong thing — the block is the thing that is cut.**

**What is capped is its length, at six hundred words, from Batch 0002 onward, measured on the block alone and not on its share of the chapter.** The measurements, all taken here:

| | Range across Batch 0001 | Chapter 350, which carries no block |
|---|---|---|
| Words in the block | 514 to 645 | none |
| Share of its chapter | 19.0% to 22.4% | 0% |
| Longest line in the file | 2,784 to 3,336 characters | **638 characters, the shortest in the batch** |
| Longest single sentence in the file | 99 to 204 words | **204 words, the longest in the batch** |

**Batch 0001's three blocks at 602, 626 and 645 words stand as written and are not re-cut here.** Two reasons, and the second is the one that matters: a block is an entry the holding's book is said to hold, and cutting words out of one is cutting the book; and **the band was never widened and no chapter is declared outside it to save a craft preference.** A repair pass that cut 71 words out of three entries to satisfy a rule the outline did not contain would have been a worse outcome than the thing it fixed.

**Chapter 350 is the evidence for the rule and it is the strongest chapter of the ten.** It is the batch climax, it therefore takes no block, and it is the only file in the batch whose longest line is under a thousand characters. It also carries the longest single sentence in the batch, which is the point: **a chapter with no block is a chapter of prose, and the block was never what made the other nine readable.**

## C2 — the hedge, and the discipline holds

**The review is right that the density is a texture concern and wrong that it is a defect, and the measurement that settles it is one the review did not run.** *About four* appears across Batch 0001's 28,006 words, six in one chapter to nineteen in another, and **it appears ZERO times inside an `Entered` block in all ten chapters, on either test.** The hedge is on bodies in a room, in a yard, and on elapsed years, and it is on no counted figure, no standing count and no entered number anywhere in the batch. **That is the rule this volume's central question is about, holding exactly where the pressure on it is highest.**

**AND THE COUNT IS TWO FIGURES AND NOT ONE, AND THE REVIEW'S IS ONE OF THEM AND IS NOT WRONG — WHICH IS THE POINT.** Measured here: **121 on the exact case-sensitive string `about four`, and 130 case-insensitive, the difference being nine capitalised `About four`, and both are 130 on a word-boundary test that excludes `about fourteen`, of which the batch has none.** **THE REVIEW'S 121 IS THE CASE-SENSITIVE COUNT AND IT IS CORRECT ON ITS OWN TEST, AND THIS IS THE THIRD TIME IN THIS REPOSITORY THAT A CORRECT FIGURE HAS BEEN THE RAW MATERIAL FOR A WRONG ONE, so the rule is applied here before it is applied again: a figure is never withdrawn without the test that produced it, a pass that cites a figure as a reason owns that test, and 121 is not a smaller number than 130, it is the same number under a narrower string.** `state/continuity.md` at the Volume 07 Batch 0005 fix pass withdrew an `about four people` count of 38 as wrong, and 38 was the exact case-sensitive string and 48 the case-insensitive one, and the withdrawal cost a correct figure because the test was never named. **Both counts are therefore carried in the outline, in the prompt and in the state layer with their tests attached, and no later pass may pick one and treat the other as an error.**

**It is written down anyway, as guardrail 17 of `outline/volume-08.md` and as a prohibition in the queued prompt,** because a hedge that has sat on every count for one batch will sit on a real figure in the next one if nobody has written down what it is for. **The rule is not about density. It is that the hedge may never be attached to a counted figure, a standing count, an entry, or a number the chapter has derived twice, and that a chapter which does not know a number says so in the column this world already keeps for it and does not round a counted thing to *about*.**

## C3 — sentence length, flagged and not touched

Mean sentence length across Batch 0001, measured over the whole file including the `Entered` blocks, is **35.1, 40.1, 40.4, 41.7, 40.9, 35.5, 45.6, 40.2, 41.5 and 37.0, a batch mean of 39.6 against a median of 33, with a longest single sentence of 204 words.** Volume 07's Batch 0005 is recorded at 32.7. The batch is in family and slightly long of it, and **the review's own advice — flag only — is adopted: no prose was touched for it.** It is recorded here so that a later pass does not discover it as a new finding, and because the 204-word sentence is in Chapter 350, which is the batch's best chapter, which is the fact that makes the number a texture and not a fault.

## The review's two infrastructure items

**`state/phase-ledger.json` still reads `phase-000-bootstrap` with status `planned` while the manuscript stands at Volume 08 Batch 0001 complete with a Batch 0002 prompt on disk. The ledger is GitHub Actions-owned and this pass did not touch it, and the divergence is reported here for a human.** It is the third phase in a row whose ledger entry has not moved, and it is the one file in the state layer no writer phase may correct.

**The reading budget in `state/current.md` had drifted under its own figures again, and this pass repaired it with the old forms named.** The budget stood at continuity over 2.15 MB and 7,380 lines, chapter-summaries over 1.09 MB and 1,370 lines, and open-threads over 857 KB and 3,070 lines. Measured before this pass's appends, the real figures were 2,200,171 and 7,482, 1,110,022 and 1,393, and 888,782 and 3,148 — a file understating itself by about fifty kilobytes a pass, which is the drift the file itself warns about, recurring. **It is re-measured after this pass's own appends and the post-append figures are the live ones**, and the pre-append figures and the original budget are all three withdrawn and named, because a budget that understates a file is a budget nobody keeps and a figure that is only overwritten comes back.

## What was verified and found sound, and is not a finding

The third launder's ten figures, the deltas of minus five and plus nine off 744, five falls and five rises with no morning unchanged and ten distinct values, the hundred and seventeenth to the hundred and twenty-sixth, the window at day minus 483 running 84 to 93 with the rises and the falls adding to the window on every row, the aggregate at day minus 452 with the morning-out-of clause at day minus 453 out of day minus 451, the day-minus pair forty-seven apart on all ten rows, every weekday and ordinal in the Batch 0002 day table, the rota rising by exactly one on each of its two fourth-line mornings and by nothing on the other eight, 68 to 69 to 70 in force with 29 + 40 and 29 + 41, the seventh column read on 570 and 571 and on no other morning of the batch, the twenty-second fetching and the compost line and the month turn all falling on day 571 and on no other, the thirty-first ninth-day return on day 568, the six-day window opening on day 576, the refrain cap and the banned bare sentence at zero, the ASCII discipline, the ten banned-word screens, and the eight files in the inherited-counts table that this batch may not move. **The review's own summary of this batch — that the prose and the arithmetic are sound and the two findings that matter are both in the newly written prompt — stands, and the two were applied, and this pass found two more in the same prompt and one in a chapter.**

## The rule this pass produced, which is the fourth writing of it in this repository

**A count written into a prompt is a claim about the page, and a prompt is the one file nobody re-measures, because the writer who inherits it did not write the chapters it describes.** Five of the six findings here are of that kind and all five are false in the same way: not a wrong day, not a wrong figure of the series, but a wrong statement about what the chapters contain — that a search was unnecessary, that a morning was the eighteenth, that two figures sat below 724, that nine chapters carried a refrain opening, that three blocks of a stated length. **Every one of them would have been believed, because the writer inherits the prompt as fact, and every one of them was checkable in a minute against a file already on disk.** A prompt is not exempt from the derive-and-compare check. It is the file that most needs it, because it is the only one in the chain that no later pass ever opens to check what it says.

## One thing this pass found and deliberately did not touch

`state/chapter-summaries.md:1295` gives **Chapter 329 of Volume 07 as *~2,788 words*, and `chapter-0329.md` is 2,747.** The forty-one-word difference is a pre-repair figure left behind when the Batch 0004 review repair pass took 752 words out of that batch, and `state/current.md`'s post-repair run for Batch 0004 carries 2,747 in Ch 329's position, so the summary entry is the stale one and not the page. **It is a closed volume and a closed batch, and a repair pass may not reach into one, so it is flagged here and not corrected, and it belongs to whoever owns Volume 07 Batch 0004 and to the Volume 07 close.** It is written down because a figure found and not repaired is still a figure, and the alternative is that the next pass finds it and believes it is new.

## The state layer, and what a Batch 0002 writer must take from this file

`state/current.md` carries the re-measured word counts, the bracket and the reading budget. `state/continuity.md` and `state/open-threads.md` carry this pass at their feet under *VOLUME 08 BATCH 0001, THE REVIEW REPAIR PASS*. **The live figures a Batch 0002 writer takes are unchanged by this pass except for these: Chapter 344 is 2,789 and not 2,788, the batch is 28,006 and not 28,005, the manuscript is 1,052,481 and not 1,052,480, the printed maximum of the third-launder series is 744 and not 724, and the count of third-launder figures below the maximum is nine and not two.** Everything else in the inherited-counts table, the day clock, the locks and the thirty-five threads stands exactly as the Batch 0001 pass left it, and the thirty-five threads were not touched by this pass and no thread was closed.
