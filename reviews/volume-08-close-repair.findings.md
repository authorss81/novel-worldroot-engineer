# VOLUME 08 CLOSE -- THE REVIEW REPAIR PASS, TWO FIGURES REFUSED, ONE MARKER FIXED, AND ONE THING HANDED ON

**Date of this pass: the twenty-eighth of September, 2026.**

**WHAT THIS DOCUMENT IS.** It is the record of the repair pass run over the review of the Volume 08 close. The review is at `logs/close.review.log` and it raised seven findings across three priorities. The governing record is the section headed *THE REVIEW OF THE VOLUME 08 CLOSE* at the foot of `state/continuity.md`, which is the last section of that file and governs over *VOLUME 08 - THE CLOSE* above it. **It is not a review of the forty-nine chapters.** That is `reviews/volume-08.findings.md`, and that file stands except where this file names a figure or a claim in it as withdrawn.

**NOTHING IN THE FORTY-NINE CHAPTERS WAS TOUCHED, AND NOTHING IN THE THIRTY DEFECTS THE CLOSE REPORTED WAS PAID.** A close may not alter a word of the volume, and a repair pass over a close may not either unless the defect is in a chapter and the pass is willing to re-measure the volume and the manuscript and repaint every figure that depends on them. **This pass was not, and it says so rather than doing a one-word fix and calling the volume clean.** Measured after these edits: Volume 08 is 139,423 words across forty-nine chapters and the manuscript is 1,163,898 across 392, both unchanged, and no file under any `batch-*/` directory was modified.

**THE HEADLINE IS THAT TWO OF THE REVIEW'S THREE PROPOSED FIGURE CORRECTIONS WERE WRONG, AND APPLYING THEM WOULD HAVE INTRODUCED THE ERRORS THEY SET OUT TO REMOVE, AND THE REVIEWER'S OWN MEASUREMENTS ARE WHAT PROVED IT.** That is the second time this repository has had a review propose a correction and had the correction refused on a measurement, and the mechanism is the same both times: a review that measures under a different rule than the one that produced the figure will always find a contradiction where there is only a second rule.

---

## PART ONE -- THE TWO REFUSED CORRECTIONS

### 1. THE `>` BLOCK COUNT IS FORTY-FOUR AND NOT FORTY-SIX, AND THE REVIEW PROPOSED TO MAKE IT FORTY-SIX

**THE REVIEW REPORTED:** "The `>` block count is wrong. `findings.md:199` claims FORTY-FOUR `>` DOCUMENT BLOCKS ACROSS FORTY CHAPTERS: THIRTY-SIX CHAPTERS CARRY ONE, FOUR CARRY TWO, AND NINE CARRY NONE. Disk: **46** blocks; 36x1 + 3x2 + 1x4 + 9x0."

**MEASURED BOTH WAYS, AND BOTH NUMBERS ARE REAL AND ONLY ONE OF THEM IS A BLOCK COUNT.**

| test | command | result |
|---|---|---:|
| physical lines beginning with `>` | `grep -c '^>'` per file, summed | **46** |
| paragraphs beginning with `>` | split each file on blank lines | **44** |

**A BLOCK IS A PARAGRAPH AND NOT A LINE, AND THE FINDINGS FILE'S FORTY-FOUR IS CORRECT.** Per chapter: nine chapters carry none, thirty-six carry one, four carry two, and 36 + 4 = 40 chapters carry at least one, and 40 + 9 = 49. The distribution the review measured is also correct as a *line* distribution -- 9x0, 36x1, 3x2 and 1x4 -- and 9 + 36 + 3 + 1 = 49 also holds, so the review's arithmetic was sound and its unit was wrong. **The two extra lines are two blocks that wrap: `chapter-0357.md`'s first `>` block runs to three lines and one other block runs to two.** Verified by paragraph: `chapter-0357.md` carries two `>` paragraphs, the first of 115 words across three `>` lines and the second of 595 words across one.

**THE REVIEW'S SECOND CLAIM ABOUT THE SAME SENTENCE IS ALSO A MISREADING.** It reports that the findings file's "own enumeration sums to 49 chapters, not 40." It does not: the sentence counts nine chapters carrying *none* in the same breath, and 40 + 9 = 49 is the enumeration working. The findings file's table is arithmetically closed.

**THE REPAIR APPLIED IS NOT TO THE FIGURE BUT TO THE FAILURE MODE.** The figure stands at forty-four and the word *withdrawn* is now written against the forty-six, in the findings file, in `state/current.md` and in `workspace/volume-09/PROMPT.md`, each with the test beside it -- split on blank lines, count paragraphs, do not count lines. **A repair that has been proposed once in a review log will be proposed again by the next pass that reads the log or the review, and a proposal to change a correct figure is more dangerous than no proposal, because it looks like diligence.**

### 2. THE NEAR-DUPLICATE FIGURES DO NOT CONTRADICT EACH OTHER, AND THE REVIEW SAID THAT 118 AND 21 APPEAR NOWHERE IN THE FINDINGS FILE

**THE REVIEW REPORTED:** "`reviews/volume-08.findings.md:385` -- 173 PAIRS ACROSS 104 PARAGRAPHS AND 30 CHAPTERS; `state/current.md:527` -- 484 pairs; 118 distinct paragraphs; 21 chapters. The 118/21 figures appear **nowhere** in the findings file. Both cannot be true."

**THEY BOTH APPEAR IN THE SAME TABLE, AT `reviews/volume-08.findings.md` section 4, under the rows *Distinct paragraphs involved* and *Distinct chapters involved*, a few lines above the row that gives the 173/104/30.** The two sets are two rules and the table says so in its own second row. The review ran at a twelve-word floor and a 0.80 and a 0.75 cutoff; the 484 came from a thirty-word floor and an 0.85 cutoff with the `Entered` blocks exempt.

**THE HOUSE RULE IS STATED IN THE REPOSITORY AND IT REPRODUCES THE FIGURE TO THE UNIT.** It is the near-duplicate guardrail of `workspace/volume-08/batch-0005/PROMPT.md` and the script printed under it. **Run verbatim against the forty-nine files in this pass:**

| figure | house rule | this pass |
|---|---:|---:|
| pairs | 484 | **484** |
| distinct paragraphs | 118 | **118** |
| distinct chapters | 21 | **21** |
| words standing in those paragraphs | 7,420 | **7,420** |
| of the 118, containing a numeral of any kind | 114 | **114** |
| pairs with both endpoints in one chapter | 0 | **0** |
| distribution | 106 / 259 / 118 / 1 | **106 / 259 / 118 / 1** |

The distribution is 106 within Batch 0001, 259 between Batches 0001 and 0002, 118 within Batch 0002, and 1 between Batch 0002 and Batch 0003, and the twenty-one chapters are all ten of Batch 0001, all ten of Batch 0002, and `chapter-0364.md`, and the single Batch 0003 endpoint is `chapter-0355.md:22` against `chapter-0364.md:20`, verified as a pair. **None of the three disputed figures was wrong. The review's own runs, at 0.80 and 0.75 over twelve-word paragraphs, returned 435/138/39 and 291/106/30 in its own shell and 577/176/47 at 0.70, and it obtained 173 at no cutoff it tried -- which is the shape of a second rule being hunted rather than the first rule being wrong.**

### 3. THE ONE REAL REPAIR THE REVIEW UNCOVERED, AND IT IS NOT ONE OF THE THREE

**§ 4 of the findings file stated that the four hundred and eighty-four were unreproducible and that the rule was unstated, in the table and again in the paragraph beneath it, and both statements are false.** The rule was never unstated: it is in the batch prompt, with the test in words and the script beneath it. What was missing was the rule printed *beside the number in the close prompt*, which is a prompt defect and not a measurement defect.

**AND THE CONSEQUENCE OF THE FALSE CLAIM WAS NOT COSMETIC, WHICH IS WHY IT IS REPAIRED RATHER THAN LEFT.** A figure that cannot be reproduced is a figure that cannot be acted on, and this one had a repair pass scheduled against it. The state layer, the findings file and the Volume 09 prompt were all telling a later phase that the debt was measured under an unknown rule, and a phase that cannot trust the rule of a debt it has been told to pay will either decline it again or invent a rule of its own. **The rule is now printed in all three places beside the figure.**

**The second withdrawal falls with the first.** The close withdrew and named *no pair involves Batch 0004 or Batch 0005* as wrong, on the evidence of its own looser 0.80 and 0.75 rules. Under the house rule the zero is correct and nothing in the four hundred and eighty-four touches either batch. Both facts stand, and the withdrawal of the zero is withdrawn and named. **The form a repair pass needs is one sentence: the debt is twenty-one chapters at the house rule and it grows if the rule is loosened -- at 0.80 by eight pairs and at 0.75 by fourteen -- so the rule goes with the debt and may not be changed on either side of the rewrite.**

**AND THE SCOPE WAS ONE CHAPTER SHORT, IN THREE FILES, WHILE NAMING ITS OWN PAIR.** All ten of Batch 0001, all ten of Batch 0002, **and `chapter-0364.md` in Batch 0003.** The twenty-first chapter was left out of the scope sentence while the pair that put a Batch 0003 endpoint into the debt was named in the same breath, so a repair pass that paid the first twenty chapters and stopped would have left standing the very pair that widened its scope. Corrected in the findings file, in `state/current.md` and in the Volume 09 prompt.

---

## PART TWO -- THE TWO FINDINGS THAT WERE REAL, AND ONE OF THEM WAS NOT A FIGURE AT ALL

### 4. THE CLOSE RAN AND LEFT NO MARKER, AND THE PIPELINE WAS GOING TO RUN IT AGAIN

**`workspace/volume-08/close/` carried no `.done` when this pass began.** The dispatcher takes the first sorted `PROMPT.md` under a directory with no `.done` and no `.blocked`, and `workspace/volume-08/close` sorts before `workspace/volume-09`. Simulated at the start of this pass:

```
SELECTED: workspace/volume-08/close      <- the close, a second time
```

and after the marker was created:

```
SELECTED: workspace/volume-09
```

**The marker is an empty file, it is the one the runner creates for itself, and it is now on disk. No controller file was touched: the dispatcher, the workflow and the agent definitions are unmodified, and the marker is a workspace artifact that the runner's own completion step had not reached.** Every other phase in this repository carries one; the close is the only phase that had run without it. **This was the one finding in the review that would have cost a full run of the pipeline, and it was the only finding that was not a figure.**

### 5. THE NEXT PHASE WAS LABELLED A BATCH, AND IT IS AN OUTLINE

**`state/current.md` named `workspace/volume-09/PROMPT.md` *THE VOLUME 09 BATCH 0001 PHASE*.** That prompt says *THERE IS NO CHAPTER IN THIS PHASE* and *THIS PHASE WRITES THE OUTLINE AND NOTHING ELSE*. There is no `outline/volume-09.md` on disk, no Volume 09 card and no Volume 09 batch directory, all three verified. **A writer believing the label would have written chapters 393 to 402 on days 606 to 615 with no volume plan under them, and nine of the fifty days the outline owes.**

**AND A SECOND SENTENCE IN THE SAME FILE STILL POINTED AT THE CLOSE THAT HAD ALREADY RUN**, thirty lines below the first, which is the third recorded time two lines in that file have disagreed about the next phase. Both are repainted and both withdrawn forms are named in place. The lesson is one this repository already cards: **a pointer to a phase is a figure, and it goes wrong the moment the phase it names finishes.**

### 6. THE VOLUME IS NO LONGER FICTION, AND IT IS NOT REPAIRABLE INSIDE VOLUME 08

**Measured from the chapter files, in this pass:**

| | v03 | v04 | v05 | v06 | v07 | **v08** |
|---|---:|---:|---:|---:|---:|---:|
| `Entered` apparatus, share of the volume's words | 4.9% | 13.0% | 14.4% | 13.5% | 14.0% | **16.5%** |
| mean words in one `Entered` block | — | 190.7 | 442.4 | 460.0 | 501.7 | **590.2** |
| chapters with no quotation mark | | | | | | **2** |

**Volume 08 spends 23,018 of its 139,423 words in 39 ledger blocks across 39 of its 49 chapters, the worst share in the series and the steepest trend since Volume 05. `chapter-0392.md`, the chapter the volume ends on, has zero quotation marks, no speech, no interior monologue and no named protagonist: twenty-nine paragraphs, a mean of 100 words, the longest 216, every one a declarative close on a negation, with the figures in it inert by the chapter's own admission. The name Marek occurs in none of the forty-nine chapters. `chapter-0387.md` and `chapter-0392.md` carry no quotation mark at all.**

**Against `AGENTS.md`, which asks that information be shown through character action, conversation, work and consequence, that sentence length and paragraph rhythm vary, and that a number matter because of what it changes. The four hundred and eighty-four near-duplicate pairs are the symptom and not the disease: a close structurally barred from writing prose can count repetition, and counting confirms it, and it cannot fix it.**

**This pass did not repair it and did not try.** No chapter of Volume 08 was touched, the planned plot is unchanged, and a repair of a sixteenth of a volume's words is not a repair pass, it is a rewrite. **It is handed to the one phase that can act on it before prose is appended, being the Volume 09 outline phase, which now carries a seventh decision and a table of its own figures. The minimum is written into that prompt: the `Entered` share below sixteen and a half per cent and expected to fall, the mean block below five hundred and ninety words, no chapter planned at zero quotation marks, the protagonist named in the majority of chapters, and not two chapters at zero. A Volume 09 outline may not plan a fifty-day volume on the premise that the register is a house style, and it may not settle the matter by planning a fighter.**

---

## PART THREE -- WHAT WAS FLAGGED AND NOT TOUCHED, AND WHY

### 7. THE THIRTY CHAPTER DEFECTS, AND THE BRACKET IS A CLEAN MEASUREMENT AND NOT A CLEAN VOLUME

**The close closed the bracket at 139,423 in the same pass that left thirty defects in the chapters, and a bracket that is correct and a volume that is clean are two different things.** The figure is correct and has been re-measured: 28,006 + 28,581 + 28,362 + 27,950 + 26,524 = 139,423 across forty-nine chapters, manuscript 1,163,898 across 392. The thirty defects are still in the chapters, each with a chapter and a line in section 2 of the findings file. Volume 07's own precedent is three passes against six known-wrong numbers and a bracket reopened to take them, so **139,423 is now stated in the head of `state/current.md` as a clean measurement and not a clean volume, and a phase that touches Volume 08 prose owes a re-measurement and may not inherit it as a baseline silently.**

**One of the thirty is a British spelling -- `colour` at `chapter-0357.md:15` -- in a volume whose own guardrail demands US spelling. It is a one-word fix that moves no figure, and it is not made here.** Any prose edit in Volume 08 obliges a full re-measurement of all forty-nine files and a repaint of every figure in the table, and a pass that fixes one spelling and reopens a closed volume for it is a pass that has chosen its scope by what was easy. It goes with the other twenty-nine.

### 8. THE STATE LAYER IS 4.7 MB AND THE COMPACTION IS DECLINED A THIRD TIME

**13,443 lines across four files, and `AGENTS.md` asks for summaries that are compact and useful for the next batch while every writer phase is told to load them.** Declined again, for the close's reasons, which still hold: these files are a chain in which a later section exists to name an earlier section's figure as withdrawn, and a compaction that drops a withdrawal brings a withdrawn figure back. **The relief that is free is the reading budget, and it is now written down: `tail -n 300` of `continuity.md`, `tail -n 140` of `open-threads.md`, `tail -n 100` of `chapter-summaries.md`, and `current.md` whole. If a compaction is ever run it must be a move and not a rewrite, and a figure that cannot be found after the move is the figure that proves the move was unsafe.**

### 9. THE LEDGER, WHICH IS NOT OURS, AND A FINDING THE REVIEW DID NOT MAKE

**`state/phase-ledger.json` still reads `phase-000-bootstrap` at zero attempts and has not been written since initialization, while eight phases have run. It is controller-owned and is flagged, not edited.** It is also not what broke the pipeline; the marker is.

**AND A FLAG FOUNDED BY THIS PASS, WHICH THE REVIEW DID NOT RAISE: THE MANUSCRIPT IS NOT ASCII-CLEAN AS A WHOLE.** Volumes 04 to 08 are clean. **Volumes 01, 02 and 03 carry 155 em dashes between them -- 123 in Volume 01 across 35 chapters, 22 in Volume 02 across 10, and 10 in Volume 03 across 4 -- written before the ASCII guardrail existed.** No claim in the state layer is false, because every *zero non-ASCII* claim in it is scoped to a batch or a volume, and Volume 08 is clean. **A pass that greps all 392 chapters will find 155 glyphs, none of them in the volume under review, and must not read them as a new defect.** Not repaired here: 155 glyphs across three closed volumes is its own repair pass, it moves word counts, and it is not this pass's scope.

---

## WHAT A NEXT PHASE NEEDS FROM THIS FILE, IN FIVE LINES

1. **The dispatcher is fixed and the next phase is `workspace/volume-09`, which is an OUTLINE phase and not a batch.** The mislabelled pointer is corrected in `state/current.md` and its withdrawn form is named.
2. **The near-duplicate debt is 484 pairs, 118 paragraphs, 7,420 words, 21 chapters including `chapter-0364.md`, measured at `difflib` 0.85 over paragraphs of thirty words or more with the `Entered` blocks exempt. The rule goes with the debt.**
3. **The `>` block count is 44 paragraphs, not 46 lines, and the forty-six is withdrawn and named so that no later pass "corrects" it.**
4. **Volume 08's thirty chapter defects are still in the chapters. 139,423 is a clean measurement and not a clean volume.**
5. **Volume 08 spends a sixth of its words in capitals and ends on a chapter with nobody speaking and nobody named. The Volume 09 outline owns the fix, with numbers, before the first chapter of Volume 09 is written.**
