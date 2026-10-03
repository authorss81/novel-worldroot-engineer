# Volume 16 Batch 0004 — the review-repair pass of 2026-10-03, Chapters 766–775, days 979–988

**FIFTEEN FINDINGS FROM `logs/batch-0004.review.log`. ALL FIFTEEN PAID, ONE OF THEM IN THE STATE LAYER AND ON THE PAGE AT ONCE, AND FOUR MORE FOUND BY THE REPAIR ITSELF. NO CHAPTER RESTARTED, NO SCENE REPLACED OR MOVED, NO DAY, CLOCK, NAME, LOCK, CARD-DIRECTED BEAT, SERIES FIGURE, THREAD, FLOOR OR PLANNED PLOT TOUCHED, NO GOVERNING FILE TOUCHED, NO CONTROLLER FILE EDITED, NO SUCCESSOR CREATED. THE PROSE REPAIRED IS EIGHT FIGURES AND CLAIMS IN FOUR MORNINGS, TWO DATES IN THREE MORNINGS, TWO OBJECTS IN FOUR MORNINGS, ONE DUPLICATED SPEECH AND ONE SET OF COUNTS THAT DID NOT ADD UP. EIGHT FILES EDITED, ONE FINDINGS FILE CREATED.**

**READ FINDING 1 FIRST, BECAUSE IT IS THE ONLY ONE OF THE FIFTEEN THAT WOULD HAVE COST THE NEXT FIVE MORNINGS OF THE BOOK SOMETHING REAL.**

## 1. The state layer had denied its own successor a floor, and the prose had denied it too — Finding 7

`state/open-threads.md` thread twenty-eight, written by this batch's own writing pass, said the Chancellor's sheet **WAS NOT IN THE ROOM AT ALL BY THE LAST MORNING AND NOBODY LOOKED FOR IT AND NOTHING HAPPENED TO IT.** Three things in this repository say otherwise.

```
chapter-0774.md:15  "and it is lying on that table this morning."        (a clerk reads it out as item one of ten)
open-threads.md:1192 (Batch 0003, same thread)  "IS STILL LYING ON THE MIDDLE TABLE UNPICKED"
batch-0005/PROMPT.md:164  requires it "lying on the middle table, unpicked, undated, unentered, unfilled in and not withdrawn"
```

**And the prose repeated the state layer's sentence rather than the other way round.** `chapter-0775.md:79` said the same sheet *was not in the room at all*. So the review named the state file and the state file was wrong and the chapter was wrong in the same direction, one morning apart. All three are corrected, and the correction is published **in the thread itself**, because a thread a successor scans for its own number is the thread that gets believed.

**THE GENERAL RULE, WHICH COSTS NOTHING TO WRITE DOWN AND IS THE POINT OF THE FINDING: A STATE FILE THAT DENIES A FLOOR ITS SUCCESSOR PROMPT IS REQUIRED TO KEEP IS THE MOST EXPENSIVE KIND OF WRONG IN THIS LAYER, BECAUSE A SUCCESSOR OBEYS A PROMPT AND DOES NOT RE-DERIVE A STATE FILE.** This is the Batch 0003 Finding 1 disease — a defect report sent to the wrong file — arriving from the other direction: here nothing was reported at all, and the silence was the defect.

## 2. A figure line can run out of its own round hundred inside a volume, and three characters said it had not — Finding 2, and the finding to carry

Silling's second ruled line is **day less five hundred and sixty-two**. Over the forty-five mornings of Volume 16 it runs 387 to 431.

```
day  949 (1st)  387      day  962 (14th)  400   <- the round hundred, and it is in a CLOSED morning
day  984 (36th)  422      day  993 (45th)  431   <- the last figure this volume gives that line
five hundred is day 1062
```

Three mornings in this batch had Tova Reed announce in the **future tense** that a round hundred was coming to that line: `chapter-0771.md:59` (*in five mornings*), `chapter-0774.md:51` (*in about four mornings*), `chapter-0775.md:71` (*tomorrow it comes to a round hundred*). **They escalate across three days, which is what turns a slip into a plot-level claim.** `chapter-0765.md` and `chapter-0769.md` use the same phrase in the past tense or as a standing truth and are defensible and untouched.

**All three are now true forward figures** — 423 tomorrow at 0771, 426 tomorrow at 0774, 427 tomorrow at 0775 — and the volume's own theme line, *a round hundred on that line is not a mark and not an opportunity and not an invitation*, is kept where it was, because that sentence was never the defect.

**WHY NO INSTRUMENT IN THIS HOUSE COULD SEE IT. Every check here asks whether a figure is present. None asks whether a figure is *coming*.** A round hundred is a legitimate figure of a series when it is **printed**; here it was never printed and never will be, and the check that would catch it is a derivation of the series' own range, not a presence test. The third launder **does** have a round hundred, at one thousand four hundred on the twenty-sixth morning, and it is a different line.

**This is the single most useful thing in the review, and it is worth one sentence in every remaining batch of every volume in this manuscript: derive whether a line's own rule still reaches a round hundred before a character tells a yard that it will.**

## 3. The self-check's own numbers did not re-derive, and the word *whole-paragraph* was the reason — Findings 11 and 12

`SELF-CHECK.md:23` and `state/current.md` published **1,326 whole-paragraph units and 20,735 sliding windows**. The committed harness is deterministic (two runs, byte-identical) and read-only (no write, rename or unlink call in it) and returns **1,328 and 20,756**. At Volume 15+16 scope the published figures were 9,036 units / 68 excess / 131,615 windows / 886 excess and the harness returns **9,038 / 67 / 131,636 / 874**. The +2 and +21 deltas at both scopes are exactly what the twelve bold-marker repairs recorded at `SELF-CHECK.md` §11 would produce if the tables were measured before them.

**The reason is one word. The paragraph unit this batch declares — every non-blank line below a heading — counts 382 paragraphs, and gate one's 302 confirms it. But `verify.py:315` shows the second gate's first reading is `tokens[i:i+18]` on a flat list: non-overlapping eighteen-word *chunks*, not paragraphs.** So the 45 "whole-paragraph shapes" at volume scope are chunk collisions, mostly bare figure-recitation frames standing in closed batches, and `SELF-CHECK.md:24`'s claim that each is "a locked figure or a frame" was true of a chunk and was presented as a claim about a paragraph.

**The standing rule at `state/current.md` §8 — declare the unit in words beside the number — exists to prevent exactly this and was not applied to this batch's own readings.** Every place that printed the figure now names the chunk reading beside the number, and every published figure has been re-measured after the prose moved and the pre-repair figures are withdrawn by name in both `SELF-CHECK.md` and `state/current.md` §29.

**A SECOND PAIR OF FIGURES FOR THE SAME UNIVERSE, PUBLISHED HERE BESIDE IT BECAUSE A PAIR COUNT WITH NO DIRECTION IN IT HALVES UNDER A RE-RUN:**

```
verify.py       Volume 15+16 scope: 1 exact pair   (counts DISTINCT repeated paragraph strings)
reviews/gate.py Volume 15+16 scope: 2 exact pairs  (counts ORDERED excess pairs)
the underlying fact: one paragraph string appears THREE times, at chapter-0719, chapter-0735, chapter-0736
```

This is the fault `reviews/volume-11-batch-0001-repair.findings.md` Finding 6 published for a different batch, and it is still live in this batch's own harness. Both figures are correct on their own basis and the basis is now stated at both ends.

## 4. Two objects were in two places on one morning, and neither gate can see a place — Findings 4 and 5

**4. The sheet of seven steps.** `chapter-0767.md` has Roan Selk carry it out past the gate at the fifth hour and not come back into the yard that day. Four paragraphs later, four people in the same yard *read the seven steps from the top* off *the sheet on the boards with six names on it*. One object, two locations, one morning, no similarity in it and therefore nothing for either gate.

**The repair is not to choose a place.** Both places carry plot. What he goes out with is a **copy**, and a copy is an established object in this holding: `chapter-0766.md:9` has four of five men writing a finding *again* on a sheet because a sheet can go on a board and a book cannot. With a copy, the original stays on the boards, Kellan Rusk can ask that morning what happens to seven steps on a sheet on a wall when a bed goes soft, Perrin Dae can argue the next morning that one line of it binds anybody, and Roan Selk can come back with a roll and put it on the middle table and nobody unrolls it.

**5. The roll on the middle table.** `chapter-0768.md:9` — *did not unroll it, and nobody in that yard unrolled it.* `chapter-0768.md:71`, in the same chapter's closing line — *still lying **unrolled** on the middle table.* `chapter-0773.md:21` — *lying **unrolled** since **the day before yesterday***, when it was put down **rolled** on day 981, five mornings back. It is rolled on all four mornings it stands there, and `chapter-0769.md:7` and `chapter-0770.md:7` were already right.

**The fixture that catches both is a search for the opposite word against the same object, not a reading.** Three of this batch's four defects in sections 5 and 6 are of this family and a fifth is a date.

## 5. Three figures in mouths, one of them a claim about another mouth — Findings 1, 3 and the low-confidence 14

| Line | Was | Is | Why |
|---|---|---|---|
| `chapter-0771.md:59` | *the form is four hundred and thirty-two, and the man at the door has already said that figure out loud today* | *the form is four hundred and twenty-eight, and that is the figure the man at the door carries on his own book and has never once taken off mine* | **Two errors in one clause.** 432 is day 988's figure; day 984 is **428**, and Kellan Rusk says exactly that from the step twenty lines later. And Tova Reed speaks at about the **third** hour and he comes out at the **fourth**, so *already* is false as well as the figure. The repair keeps the beat — *two figures and not one, and I am not going to add them together* — and drops the false cross-reference. |
| `chapter-0774.md:23` | *the eleven days that were asked for at this gate **two** mornings ago* | *four mornings ago* | They were asked at that gate on day 983. Custody is day 987. |
| `chapter-0774.md:25` | *the word accepted was wrong and had been used by people in the yard including himself **on the day before last*** | *accepted was the wrong word for it and had been the wrong word for it all week in this yard and in his own mouth* | **The review flagged this as low confidence and was right to.** The word is in no other morning of Volume 16, so the anchor rested on nothing. **The repair does not invent a day for it.** The clerk still owns the word and still refuses to unsay it; the claim is no longer dated to a morning that cannot be checked. |

## 6. The public accounting of the ring did not close — Finding 15, which the review flagged and not asserted

`chapter-0775.md` reads a nine-bed table out in a yard in daylight with every failure in it. It then says **Six held the draw. Five held the load**, and then **The five that are not on that count and the two that failed on a second load**. Nine minus six is three. Nine minus five is four. Neither is five. And only bed eight failed *on a second load*; bed seven *would not take the flood load at all*, which is a first-load failure. **This is the one block in the batch where a reader can do arithmetic and get three answers, and it is the volume's public accounting.**

**THE REPAIR DID NOT MOVE THE TWO COUNTS, BECAUSE THE CARD SET GIVES THEM.** `outline/batches/volume-16-cards.md` says *six that held the dry-season draw, five that held the load, one gone with the root on it, one soft*, on card thirteen and again on card forty, and the card set is clean. **So the table now states the basis of each count in its own words, and the residual derives from the nine lines above it:**

> A bed that held the draw is one that was not already soft when the draw went in and kept it. A bed that held the load is one that took the flood load on the first load and lost nothing of it at its own far end on that load, and a bed that held on a first load and let water out on a second one is written here as held and is not written as fixed.

```
held the draw      2,3,4,5,6,8                  = 6      9 - 6 = 3 not on it  (1, 7, 9)
held the load      2,3,5,6,8                    = 5      9 - 5 = 4 not on it  (1, 4, 7, 9)
on both            2,3,5,6,8                    = 5
first and not the second   4                    = 1
9 = 5 + 1 + 3
```

The card's own prohibitions are untouched: two counts of two different things, not to be added, no total to be said out loud in a yard, no third figure.

## 7. The same speech twice, sixty words apart, by the same mouth — Finding 6

`chapter-0775.md:59` has Odile Vray deliver one speech, then *She did not wipe the board*, then deliver it again with two clauses changed. Forty-eight and forty-nine words, Jaccard 0.82, **longest identical contiguous run fourteen words.**

**This is why the published duplicate figures are literally true and blind to the defect.** No identical eighteen-word window survives, and the exact-duplicate sweep is nil at any paragraph length, and the batch could honestly print zero on both. The review's finding and the batch's own numbers are both right and they are measuring different things.

**The repair is structural and not lexical, following the precedent in `reviews/volume-11-batch-0004-repair.findings.md`.** The first delivery stands whole. The second half of the paragraph now carries the **consequence** — she puts the chalk in the tray instead of her apron and stands square in front of the two orders with her hands behind her back until about nine people have read both. No figure, no beat and no decision moved, and the closing argument that nobody has to choose is where it was.

**THE SAME CLASS, FOUND AND PAID TWICE MORE, ON A MEASUREMENT NO GATE RUNS.** A difflib pass over every sentence in the ten files at a 0.72 threshold returned two more, and both are real:

- `chapter-0772.md` repeats Tova Reed's board gesture against the same gesture four mornings behind it at **0.903** — *She turned the corner of her board out and let it lie flat against her hip* / *She turned the corner of the board out and let it lie against her hip.* Repaired: she gets a thumb under the corner and tips it up.
- `chapter-0770.md:63` and `chapter-0774.md:41` carry the same gate sentence at about **0.86** across four mornings: *about four people at the gate had been standing there for about a minute and a half before the last of them went* / *about four people at that gate stood there for about a minute and a half before the last of them went.* **`chapter-0774.md` is repaired and `chapter-0770.md` is left, because it is the first of the pair and the first is the one that reads as the beat.**

The remaining sentences the difflib pass returns are figure recitations — a speaker's standing line with a different figure in it — which is the class this volume runs on purpose.

## 8. Four dates the review did not name, all of the class the Batch 0003 repair paid for

`chapter-0759.md` lost six bare calendar dates to the previous repair pass. This batch has four more, of the same family, and none was in the review's list.

| Line | Was | Is | Why |
|---|---|---|---|
| `chapter-0768.md:43` | **"I call it a Wednesday."** | "I call it a Sunday." | Day 981 is a **Sunday** on the card set, on the chapter heading and on the chapter summary. The next clause, *a man who invents a word for it on a Monday*, is tomorrow and is correct, and is untouched. |
| `chapter-0773.md:21` | *lying unrolled ... since the day before yesterday* and *instead of having it on **Friday*** | *lying rolled up ... since the Sunday morning it was put down there* and *instead of having it at the dark* | Both faults at once. Day 986 **is** a Friday, so a Friday could not be a day still to come; and the roll was put down on day 981, five mornings back, not two. |
| `chapter-0775.md:5` | *since **a Saturday a fortnight before*** | *since **the Tuesday of the week before last*** | The table went up at `chapter-0760.md`, day 976, which is a **Tuesday**, twelve mornings before day 988. A fortnight before a Sunday is a Sunday. **The same sentence's *about thirty people had read all of it in that fortnight* becomes *in the twelve mornings it has stood there*,** because the figure and the day have to agree. |

## 9. Finding 13 was half right, and the half that was wrong is published here — the texture finding

The review named three strings. **The counts are right. The ranking is not, and a successor that takes the ranking will go and fix prose that was never broken.**

```
                   this batch        0001      0002      0003
in that yard        2.24 per 1k      0.43      1.21      0.76    <- the only outlier
about four          1.39 per 1k      1.01      1.64      0.76
and nobody          3.15 per 1k      2.67      2.80      3.60
```

**Only `in that yard` is an outlier, and it is a bad one: five times the rate of the batch immediately behind it and over two hundred in a single volume.** It is now **twenty**, reduced by forty-one replacements spread across seven forms — *there*, *in the yard*, *at the boards*, *among them*, *in front of him*, *at that gate* — so that no single locative takes the batch over. `about four` was also reduced, from thirty-eight to twenty-nine, using *four or five*, which this volume has been using since `chapter-0749.md`, and the twenty-nine is 1.06 per thousand, below the rate two of the three closed batches have been running. **`and nobody` was left alone**, because 3.15 per thousand is below the 3.60 the batch immediately behind has been running.

## 10. What the review verified clean, and what this pass did not disturb

The review re-derived every series independently for all ten mornings and all of them reproduce, **including the parity of the split window halves, which no gate in this repository can see** — correct direction on ten mornings out of ten. The near and far boards, the aggregate and both clause limbs, the letter, the charter, the count in force, the register form, the window and both halves, the third launder and the ordinal of the run all verify against their own rules on every morning. Day numbers, month, weekdays in the headings, and the morning 31–40 numbering are correct. No digits in body prose or apparatus, no month name, none of the six banned bare words outside the headings. Apparatus: four blocks at 0766 / 0768 / 0770 / 0775, none on the five protected mornings, no `Entered` label, twenty-two of thirty spent. The comfort line spent whole once and the far-end figure absent from all ten. **And the successor prompt is sound: all five cards' figures verify, including the volume-maximum launder figure of one thousand four hundred and twenty-seven on day 992 and the count in force of one hundred and seventy-four on the day-990 fourth-line morning; it creates no successor and refuses a re-run.**

**All of that is still true after this pass, and the figure check still returns one hundred and fifty-eight required, one hundred and fifty-eight present and zero failures.**

## 10b. One thing considered, checked, and left alone

`chapter-0772.md:11` has Nia Vale say she has read the gauge out loud *every morning since the sixth hour on the day before yesterday*. That anchor is arithmetically right — day 985's day before yesterday is day 983 — and day 983 is a morning on which the page's own apparatus records *a gauge with two readings on it, both said out loud*. **Nia Vale is not named on `chapter-0770.md`, though she is named reading the gauge twice on day 981 and again on day 985 itself.** So the sentence is a character claiming her own habit rather than a date a reader can check against a card, it is not contradicted by anything, and it was not among the findings.

**IT WAS LEFT ALONE, AND THE REASON IS THE RULE: REPAIR BY FINDING, NOT REPAIR BY TASTE.** A pass that rewrites every soft anchor it can reach is a pass that cannot tell a reader which changes were defects. The figure it would have changed is a hedge in a woman's mouth about herself, and the sentence does not assert anything the book contradicts.

## 11. What this pass did not do

**It did not write a chapter and it did not restart one.** It did not replace or move a scene, cut or add a beat, or alter a card direction. **It did not move a figure of any series** — the figure check is identical before and after. It did not answer, close, group, sum, reword or advance any of the thirty-five, and cut no not-known row. It did not reduce, soften, recover, re-name or price any of the four permanent losses and added no fifth. It did not spend either locked figure. It did not touch `outline/batches/volume-16-cards.md`, which is clean, or `workspace/volume-16/batch-0005/PROMPT.md`, whose floors are load-bearing for the last five mornings and which this batch's own state layer had contradicted. It did not touch `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` or `state/phase-ledger.json`, and it forged no marker. **It did not create a successor phase: `batch-0005/PROMPT.md` is on disk, it is five mornings, and it is the last writing phase of the series.**

## 12. The figures after this pass, measured per file and never by concatenation

- **The batch: 27,401 words across ten files**, per file 2,377, 2,440, 2,238, 2,370, 2,853, 3,090, 2,768, 2,749, 3,011 and 3,505. **The 27,273 and its per-file list are withdrawn by name.**
- **Volume 16: 85,178 across forty files of forty-five. The 85,050 is withdrawn.**
- **The manuscript: 2,116,570 across 775 chapter files, and it reconciles: 2,031,392 across volumes one to fifteen, which is the figure the Volume 15 close published, plus 85,178. The 2,116,442 is withdrawn.**
- **Gate one at batch scope: 302 paragraphs of thirty words or more, nil exact pairs.** Whole manuscript: 26,432 and forty-one pairs, none touching this batch.
- **Second gate at batch scope: 1,334 chunks and 20,889 sliding windows, nil on both readings.** Volume 15+16 scope: 9,044 chunks, 45 shapes, 67 excess; 131,769 windows, 741 shapes, 877 excess.
- **The independent gate at `reviews/gate.py` returns the same three figures for these ten files — 382 paragraphs of which 302 are thirty words or more, gate one nil, 1,334 chunks nil, 20,889 windows nil.** That is the check on Finding 3, and the two implementations now agree on the unit.
- **Self-collision controls reproduce twenty-seven and twelve.** Exact-duplicate sweep: nil inside the batch at any paragraph length; two hundred and thirty duplicated paragraphs elsewhere in the manuscript and none touching this batch, and that figure is the same before and after.
- **Cross-batch verbatim windows against the three closed batches of this volume: 161, classified as a floor restated or a speaker's standing line 148, Iona Vey's deliberate identical exit 9, the locked comfort line 3, and Sera Quill's thirteen-apart line 1.** The earlier 157 and 144 are withdrawn; they were measured before the prose moved.
- **Apparatus: four blocks in the batch, twenty-two of thirty spent in the volume, eight unspent, no `Entered` label.** Ordinal sweep: fifty-one, every one an hour or a spelled figure.
- **Texture after the repair: `in that yard` twenty at 0.73 per thousand, `about four` twenty-nine at 1.06, `and nobody` eighty-six at 3.14, against ranges of 0.43 to 1.21, 0.76 to 1.64 and 2.67 to 3.60 in the three closed batches.**