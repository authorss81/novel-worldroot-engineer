# Volume 16 Batch 0003 — the review-repair pass of 2026-10-03, Chapters 756–765, days 969–978

**FIVE FINDINGS FROM `logs/batch-0003.review.log`. ALL FIVE PAID, AND FINDING FOUR PAID SIX SITES WHERE THE REVIEW NAMED FOUR. NO CHAPTER RESTARTED, NO SCENE REPLACED OR MOVED, NO DAY, CLOCK, NAME, LOCK, CARD-DIRECTED BEAT, SERIES FIGURE, THREAD OR PLANNED PLOT TOUCHED, NO CONTROLLER FILE EDITED, NO MARKER FORGED, NO SUCCESSOR CREATED, NO GOVERNING FILE TOUCHED. THE PROSE REPAIRED IS SIX DATES IN ONE MORNING AND NOTHING ELSE. EIGHT FILES EDITED, ONE FINDINGS FILE CREATED.**

**THE REVIEW ITSELF IS STRONGER THAN THE BATCH'S RECORD AND THE BATCH'S RECORD WAS RIGHT ABOUT EVERY FIGURE. It re-derived every series independently for all ten mornings and all of them reproduce, including the one class of error every gate in this repository is blind to: the parity of the split window halves, correct on ten mornings out of ten. Read the review's *What holds up* section before anything else in this file, because a repair pass that hides it will leave the next writer believing the batch's own self-check was sufficient.**

## 1. The defect report that named a clean file — Finding 1, and the one to read first

**A DEFECT REPORT NAMES A FILE, AND A REPORT THAT NAMES THE WRONG FILE COSTS MORE THAN NO REPORT, BECAUSE THE NEXT PASS GOES AND LOOKS AT THE FILE IT WAS SENT TO.**

The Batch 0003 writing pass reported in three places that six of the forty-five cards at `outline/batches/volume-16-cards.md` print Silling's second ruled line with the wrong rule beside it, and it published a supporting statistic for that file: the wrong form six times, the right form forty-five times. **That file is clean, and it was clean.**

```
grep -c "five hundred and fifty-two"     outline/batches/volume-16-cards.md   ->   0
grep -c "five hundred and sixty-two"     outline/batches/volume-16-cards.md   ->  46
grep -c "^\*\*THE FIGURES\.\*\*"          outline/batches/volume-16-cards.md   ->  45
```

Forty-six is forty-five cards plus the rule table. Not one Silling line on any of the forty-five cards takes the wrong rule. **The six defective cards were the six the same pass had written into its own successor prompt at `workspace/volume-16/batch-0004/PROMPT.md`, and the statistic it published for the clean file was wrong on both counts for that file while being roughly right for the prompt.**

The three reports are corrected in place, by attribution and by measurement, in `workspace/volume-16/batch-0003/SELF-CHECK.md` section nine, in the closing section of `state/open-threads.md`, and in section three of the successor prompt. **`outline/batches/volume-16-cards.md` is untouched.** The successor prompt no longer tells its writer to record the finding against that file.

## 2. One document with two answers — Finding 2

`workspace/volume-16/batch-0004/PROMPT.md` printed the rule correctly in its section three table and wrongly in six of its ten card blocks: the cards for days 981 and 984 to 988 wrote *day less five hundred and fifty-two*, which is the aggregate's rule. **A writer working from the cards met the wrong rule first and the warning second.**

**All ten card blocks now carry *day less five hundred and sixty-two*, and the six figures beside the wrong rule were never wrong:** 419, 422, 423, 424, 425 and 426, which are those six days less 562, re-derived here from the rule and not copied from the card.

**Why the figure check never saw it, which is the part worth carrying:** day less 452 gives 529, 532, 533, 534, 535 and 536 on those same six days, and those are the aggregate's own figures. **A check that asks whether a figure is present cannot tell two series apart, and a wrong rule that lands on a neighbouring series' value is invisible to every instrument in the house except a derivation.** The rule table in the same prompt was always right, which is the only reason the defect was findable at all.

## 3. Two sentences that said the volume's major turn was unwritten — Finding 3

`state/current.md:19` (the Batch 0002 row) and `state/current.md:1756` (the close of section twenty-five) both still printed **THE MAJOR TURN IS THE TWENTY-FIRST MORNING AT DAY 969 AND IS NOT YET WRITTEN**, written by the pass before last and contradicted by the Batch 0003 row thirteen lines above the first of them. `chapter-0756.md` is the major turn and is on disk.

**Both now say it was unwritten when they were measured and is written now, at `chapter-0756.md`,** which keeps the history and stops a successor inheriting a false statement about the spine of the volume.

## 4. The undisclosed sweep, and six dates where the review named four — Finding 4

**A SWEEP THAT IS RUN AND NOT PUBLISHED IS A FIGURE NOBODY CAN CHECK, INCLUDING THE PASS THAT RAN IT.** The batch's harness swept thirteen ordinal words standing as dates outside a heading and returned fifty-three. The batch's own record listed twelve sweeps and not this one; batches 0001 and 0002 never ran it.

Forty-seven of the fifty-three are an hour, a masonry course, a numbered blank or a spelled figure, read one at a time. **Six are bare calendar dates and all six stand in `chapter-0759.md`:**

| Line | Was | Is |
|---|---|---|
| 9 | `Fourth place. Nine houses. Tested on the ninth.` | `Tested yesterday.` |
| 11 | `Third place. Six houses. Tested on the ninth.` | `Tested yesterday.` |
| 13 | `The four at the end of the second branch. Four houses. Tested on the tenth.` | `Tested the day before that.` |
| 15 | `The middle row. Twenty-two houses. Tested on the tenth.` | `Tested the day before that.` |
| 39 | `had been tested on the ninth along with the fourth place, we would have known by the tenth` | `had been tested yesterday along with the fourth place, we would have known by the dark` |
| 81 | `where it has lain since the fourteenth morning` | `where it has lain since it was put down` |

**THE REVIEW NAMED THE FIRST FOUR. Lines 39 and 81 are two more of the same class in the same morning, and they were in the harness's own output: the review's confirming grep required an ordinal to be followed by *of*, which no date on this page is.** Both are cut. The sweep returns forty-six and every one of the forty-six is an hour, a course, a numbered blank or a spelled figure.

Three things about the repair:

- **The relative-day form was chosen over the hour form deliberately.** The house form for naming a moment is an hour, a place and a count of mornings, but this sheet's fifth column holds a *day*, and the sentence under it says so — *the four rows above it have a day in the fifth column and that row does not*. Writing hours into that column would have required rewriting that sentence too, and would have changed what the page is about. **`yesterday` and `the day before that` keep the column a column of days, keep the region's row the only one with nothing in it, and put the two days in the same order they were in.** Day 972 is a Friday, so those are day 971 and day 970, which are exactly the days the ordinals named.
- **The cut at line 81 removed a date that was also wrong.** The sheet came up the lane on Friday, day 965, which is the volume's seventeenth morning, and that is established on the page at `chapter-0756.md:77`, in the successor prompt's own floors at its section ten, and in the state layer. **The sentence said the sheet had lain there since the fourteenth morning.** The replacement is `chapter-0755.md`'s own wording for the same sheet.
- **Line 19 was left alone** and is still true: the fifth column still holds days.

**The harness now reports a file line and not a paragraph index.** It printed paragraph positions before, which for this file meant that its line 18 was file line 39 — the reader had to re-grep before he could open what the report named. `paragraphs()` now returns `(file line, text)` pairs, one definition of the unit rather than two, and an offset map carries a match in the joined text back to the line it stands on.

The sweep is now published in the batch record at section two's table and as item thirteen of its list of sweeps, and the successor prompt's section nine now says what the batch behind it found, so that the class is not rediscovered from nothing.

## 5. Three handoffs naming the wrong morning — Finding 5

`SELF-CHECK.md` section eight told the next writer that **THE ELEVENTH MORNING** must find a bed failing in time. The eleventh morning of Volume 16 is day 959 and has been on disk for two batches. `state/current.md` named the same wrong morning twice, at its section twenty-six heading and at the four standings it hands on. **All three now read the thirty-first morning, which is day 979 and is the next one.** `state/chapter-summaries.md` stated the same obligation without the stray ordinal and was the correct copy.

## 6. Two stale pointer lines found while applying the above, and named because they are the same fault

Not in the review. Both are the Finding 3 family — a state file asserting something about the manuscript that the manuscript has outgrown — and a successor obeys a pointer rather than disbelieving it.

- **`state/continuity.md:9` and `state/open-threads.md:11` both said Volume 16 was open at *twenty* mornings of forty-five.** Thirty are on disk. Both now say thirty.
- **All four state files' head blocks still named the Batch 0001 review-repair pass as the latest pass to write in them**, two batches and one writing pass behind the work. Each head block now names this pass and says what it did. **`state/current.md` also said its latest section was twenty-five; the Batch 0003 pass had added twenty-six, and this pass's own repairs are at twenty-seven.**

Also corrected, in `state/continuity.md` section nineteen: it said the region's row was **ruled across four columns** where `chapter-0759.md:19` says five, and the repair records the four testing days in their new relative form so the layer and the page agree.

## 7. What this pass did not do

**IT DID NOT WRITE A CHAPTER AND IT DID NOT EDIT ONE BEYOND SIX DATES IN ONE MORNING.** It did not restart the batch, replace or move a scene, cut or add a beat, or alter a card direction. It did not move a figure of any series: the figure check is one hundred and sixty-two required, one hundred and sixty-two present, zero failures, before and after. It did not answer, close, group, sum, reword or advance a thread and cut no not-known row. It did not reduce, soften, recover, re-name or price any of the four permanent losses. It did not spend either locked figure, and the six load-bearing strings return zero. It did not touch `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` or `state/phase-ledger.json`, and it forged no marker. **It did not create a successor phase: `workspace/volume-16/batch-0004/PROMPT.md` is on disk and fifteen mornings remain, so no volume-close prompt is due.** It did not edit `outline/batches/volume-16-cards.md`, and that refusal is the point of Finding 1.

## 8. The figures after this pass, for whoever runs it next

- **The batch: 18,335 words across ten files**, per file 2,481, 1,892, 1,843, 1,735, 1,694, 1,642, 1,895, 1,607, 1,757 and 1,789, per file and never by concatenation. The earlier 18,338 and the earlier 1,738 for `chapter-0759.md` are withdrawn by name.
- **Volume 16: 57,777 words across thirty files of forty-five.** The earlier 57,780 is withdrawn by name.
- **The manuscript: 2,089,169 words across 765 chapter files.** The earlier 2,089,172 is withdrawn by name.
- **Gate one at batch scope: 247 prose paragraphs of thirty words or more, zero exact pairs.** Whole manuscript: 26,130 paragraphs and forty-one exact pairs, none touching this batch. **Second gate at batch scope: 831 whole-paragraph units and 12,290 sliding windows, zero repeated shapes and zero excess on both readings.** Both self-collision controls reproduce twenty-seven and twelve.
- **The independent gate at `reviews/gate.py`, which is a different implementation written by an earlier repair pass, returns the same three figures for these ten files — 380 paragraphs of which 247 are thirty words or more, gate one nil, 12,290 sliding windows nil, 831 whole-paragraph chunks nil. That is the check on the harness edit in Finding 4: the paragraph unit is defined once and the two implementations agree.**
- **Exact-duplicate sweep: zero at any paragraph length inside the batch and zero against every other file in the manuscript.** Apparatus: seven blocks in the batch, eighteen spent of thirty in Volume 16, twelve unspent, no `Entered` label anywhere.
- **The ordinal sweep: forty-six hits, all of them an hour, a course, a numbered blank or a spelled figure.**
- **Nothing in the batch fiction moved except six dates, and no figure of any series was re-derived from anything but its own rule.**