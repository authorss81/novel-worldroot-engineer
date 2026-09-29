# VOLUME 09 BATCH 0005, CHAPTERS 433 TO 441, DAYS 646 TO 654, MOVEMENT 5 — THE REVIEW REPAIR PASS, AND THE RECORD TO READ BEFORE THE VOLUME 09 CLOSE

**THE REVIEW AT `logs/batch-0005.review.log` WAS RUN BY AN INDEPENDENT REVIEWER AND THIS FILE IS THE REPAIR PASS THAT FOLLOWED IT. TEN FINDINGS. SEVEN APPLIED AS STATED, TWO APPLIED TOGETHER WITH THE CHAPTER REPAIRS THEY EXPOSED, ONE DECLINED WITH ITS REASON. FOUR CHAPTERS OF THIS BATCH AND ONE SENTENCE IN THREE MORE WERE TOUCHED, AND ONE CHAPTER OF BATCH 0001 WAS AMENDED. NO CHAPTER WAS RESTARTED, NO SCENE WAS MOVED OR REPLACED, NO DAY, CLOCK, NAME, LOCK, CARD, SERIES FIGURE, PROHIBITION, THREAD OR ENDING LOCK WAS TOUCHED, AND THE PLANNED PLOT OF ALL NINE CHAPTERS IS UNCHANGED.**

**THE BATCH'S OWN REPAIR WORK WAS SOUND AND EVERY WORD COUNT ON THE PAGE WAS RIGHT, AND THIS PASS SAYS SO AT THE HEAD BECAUSE THE HEADLINE FINDING IS NOT ABOUT THE PROSE AT ALL. EVERY FIGURE THE REVIEW RETURNS AGAINST IS A FIGURE THAT WAS TAKEN BY A RULE APPLIED BY HAND, AND EVERY FIGURE THAT WAS RUN WITH `wc -w` OR WITH A SCRIPT IS RIGHT. THAT IS THE FIFTH TIME THIS VOLUME HAS HAD THAT SHAPE.**

**READ FINDING ONE FIRST. IT IS THE ONE THAT WAS WORTH THE MOST AND IT IS NOT A PROSE DEFECT: THE GATE HAS TWO WRITTEN DEFINITIONS IN THIS REPOSITORY, BOTH OF WHICH CALL THEMSELVES *THE WRITTEN DEFINITION*, AND THE STATE LAYER HAD BEEN PUBLISHING A THIRD SET OF FIGURES THAT MATCHED NEITHER — NOT 1, AND NOT 22, AND NOT 67.**

---

## ONE. THE NEAR-DUPLICATE GATE: THE FIGURES DID NOT REPRODUCE, THE NAMED PAIR WAS NOT A GATE RESULT, AND THE PROSE HAD A REAL PAIR UNDERNEATH IT

`state/continuity.md`, `state/open-threads.md` and the new close prompt all carried this sentence: *"The one pair remaining across the whole volume on the first run is the inherited 0.854 between `batch-0001/chapter-0401.md:7` and `batch-0002/chapter-0405.md:8`, being the rota-taken count sentence. Run 1 total 1, run 2 total 22, cap-removed diagnostic 67 and 22, byte-identical nil across 2,045 paragraphs."*

**NOT ONE OF THOSE FIGURES IS WHAT THE WRITTEN GATE RETURNS UNDER ANY VARIANT, AND THE NAMED PAIR IS NOT A GATE RESULT AT ALL.** Re-derived with script:

- Ch 405's rota sentence is on **physical line 7**, not 8; line 8 is blank. As **paragraphs**, `0401:7` is the third-launder sentence and `0405:8` is the day-minus pair — the state was pointing at a blank line and a wrong paragraph.
- Between the two actual rota sentences: **shared eight-word runs = 0**, `difflib` = **0.510**, not 0.854. The written 1.25 length factor skips the pair outright at 67 words against 20.
- The written definition in `workspace/volume-09/batch-0005/PROMPT.md`, run verbatim over all five directories, returns **2 pairs across the volume and 1 involving Batch 0005**, not 1 and nil.
- With a >12-paragraph cap on shared eight-word runs applied on top: **0 and 0**. With the cap removed, the same rule returns **2 and 1** — not 67 and 22.

**AND THE FAITHFULNESS OF THE CHECK IS THE PART THAT MATTERS MORE THAN ITS FIGURE. `outline/volume-09.md` guardrail 12 and `workspace/volume-09/batch-0005/PROMPT.md` print two different gates and both call themselves the written definition:**

| | guardrail 12 | batch-0005 prompt |
|---|---|---|
| measure | `difflib.SequenceMatcher(...).ratio()` on whole paragraphs | overlap of sets of eight words in order |
| universe | headings and `>` blocks dropped, 30-word floor | heading dropped, **`>` blocks kept**, no floor |
| length factor | 1.25 | 1.25 |
| paragraphs in universe | **1,752** | **2,094** |
| Volume 09 result | **177 pairs, 129 involving Batch 0005** | **0 pairs, 0 involving Batch 0005** |

**A GATE DEFINED IN TWO PLACES AND MEASURED IN A THIRD IS THE REASON NOBODY COULD RE-RUN IT. Both figures are now live in the head of `state/current.md` and in the close prompt, each named as the rule that produced it, and the close prompt is ordered to run and report both. The cap that "skips any shared eight-word run appearing in more than twelve paragraphs" is in neither written definition and in no script; applied on top it also returns 0, so it is not load-bearing here and is not described as the reason the volume is clean.**

### THE TWO REAL PAIRS, AND BOTH WERE PAID

1. **`chapter-0438.md:44` against `chapter-0440.md:42`, at 0.857, in this batch.** A containment: **Ch 440's paragraph was the fifty-six words of Ch 438's paragraph with twenty-three words hung on the end.** The previous repair pass had re-shaped Ch 440 by *appending to* the plain house shape instead of re-shaping it, and the plain house shape is the one that pass had deliberately left standing in Ch 438. Re-shaped. Every fact survives: the eleventh year, no dimension on any page, not walked, measured, crossed, priced or explained, the ground going wrong and going slower, and nobody in this holding has called slower better.
2. **`chapter-0398.md:35` against `chapter-0400.md:44`, at 0.873, in Batch 0001.** The same shape: fifty-five words of Ch 400's paragraph standing whole inside Ch 398's.

**Finding 1 said the figures had to be fixed before the close runs, and the close prompt forbids a close from altering one word of any of the forty-nine chapters. Leaving pair two would therefore have written a permanent, unrepairable debt into the volume. On the precedent of `reviews/batch-0002-v08-repair.findings.md`, which amended ten word-for-word sites in Volume 08's Batch 0001, Ch 400's paragraph is re-shaped onto the drawer. It is the first amendment to a prior batch of Volume 09 and it is named as one in `state/chapter-summaries.md`.**

**The gate is now nil on both runs and on the cap-removed diagnostic, and byte-identical paragraphs are nil on every universe this repository defines — 2,094, 2,045, 1,807 and 1,752. The 2,045 denominator is not replaced; it is given its universe, which is the repair Finding Eight turns out to need.**

---

## TWO. THE `>` CEILING WAS ANSWERED ON TWO BASES AND THE STATE PUBLISHED THE ONE THAT PASSES

Guardrail 3 of `outline/volume-09.md` sets a ceiling of **thirty `>` document blocks in the volume, against Volume 08's measured forty-four across forty chapters**. **Volume 08's forty-four is ALL `>` blocks — thirty-nine `Entered` and five document — across forty chapters, four of which carry two.** Volume 09 measures:

| | all `>` blocks | `Entered` | document | chapters with any | chapters with two |
|---|---|---|---|---|---|
| Volume 08 | 44 | 39 | 5 | 40 | 4 |
| Volume 09 | **55** | 28 | **27** | 41 | 14 |

**On the outline's own comparison basis Volume 09 carries fifty-five against a ceiling of thirty and is twenty-five over it. The state published twenty-seven, which is the non-`Entered` count alone, and the batch prompt silently switched basis when it added "two and eight and six and seven" to reach 23.** The Batch 0005 prompt's own per-batch ceilings (two, eight, six, seven) are all non-`Entered` counts, so the switch was consistent within the batch and inconsistent with the ceiling it was measuring against.

**THE PER-CHAPTER RULE HOLDS ON BOTH BASES: twenty-seven chapters carry one document block each and none carries two. THE `Entered` CEILING OF THIRTY CHAPTERS IS SEPARATE AND IS MET AT TWENTY-EIGHT.**

**THE BREACH IS DECLARED, NOT REPAIRED.** The outline is a completed phase's file; re-basing a ceiling down to the figure that passes is not a repair, it is moving the line. The close prompt now orders the close to report the breach and forbids it from repairing the outline.

---

## THREE. A RULE THAT IS NOT THIS HOLDING'S RULE STOOD ON FIVE PAGES

`chapter-0433.md:19`, `-0435`, `-0437:13`, `-0439`, `-0441:13` all read: *"The pair is read out at the seventh hour on the four mornings of a fortnight it is read on."*

**That is not a rule of this holding and never was, and it is new in Batch 0005 — Batches 0001 to 0004 use a different and correct formulation.** The pair is read at the seventh hour on **every other morning** of the volume and on no other: the twenty-four odd days from 607 to 653, and not on the twenty-five even ones. The four run figures on the page prove it independently: **69 of 121, 70 of 123, 71 of 125, 72 of 127 on days 647, 649, 651 and 653 — a numerator rising by one and a denominator by two every other morning.** A fortnight holds **seven** of this holding's read mornings, not four.

**All five pages are repaired in the words of the page, each in its own shape so that the fix does not become a fifth repeated sentence. No run figure moved. The reason-first frame and the reason attached to it are kept whole in every chapter, and the batch's own pattern of saying why a morning carried no figure is preserved, because the reason is a real thing that happened to two men on that morning and the page is right to say it.**

---

## FOUR. THE `NEXT MONTH` SWEEP WAS A CHAPTER COUNT PRINTED AS A MATCH COUNT, AND A DOCUMENT BLOCK IN CAPITALS WAS INVISIBLE TO IT

The state reported eight strings, split five and three. **There are nine paragraphs in eight chapters.** The missing one is **`batch-0002/chapter-0410.md:31`, a `>` document block in capitals carrying "the fourth day of next month"** in the Assembly's resolution to send four persons to the node. It resolves to **day 634, inside the volume, and correct.** A narrative-only sweep cannot see it; a case-sensitive sweep cannot see it either.

**The state also gave `chapter-0408.md:41` as day 623. It is day 621.** 623 is Ch 410's day. The 5 + 3 split only balanced because Ch 413's two paragraphs were being counted as one.

**The true split is six inside the volume and three outside, and the true positions are `0393:27` (606 → 633), `0395:16` (608 → 633), `0408:20` (621 → 631 and 632), `0410:31` (623 → 634), `0413:5` (626 → 631), `0413:40` (626 → 636), `0417:16`, `0428:15` (641 → 661), `0431:17` (644 → 661).** The full table is in `state/open-threads.md` at its foot.

---

## FIVE. "ALL THREE OF WHICH ARE DAY 661" IS WRONG FOR ONE OF THE THREE, AND THAT ONE IS A FINDING OF A DIFFERENT KIND

`chapter-0417.md:16` reads *"it is read again tomorrow and not on any morning after that until the turn of the next month."* **Ch 417 is day 630, the thirtieth of the ninth, so the turn of the next month from that page is day 631 — inside the volume — and the same sentence says the column is read again tomorrow.** The state classified it as a day-661 finding on an arithmetic that had not been done.

**So the three become two plus one. `chapter-0428.md:15` and `chapter-0431.md:17` really are day 661 and are a real finding against a rule that post-dates those pages. `chapter-0417.md:16` is not a day-661 finding at all, and it is a finding of a different kind: the sentence contradicts itself on its own morning, and read the other way, as day 661, it is one morning past the thirtieth — which is the next reading under the rule in its own first clause.**

**Finding 5 was a finding about the state's measurement and not a request to re-adjudicate a closed chapter's series statement. The rewrite is DECLINED and the sentence is LEFT STANDING, and the reason is written down rather than assumed: this is a closed chapter of an open volume, the ambiguity is a defensible reading of a deliberately terse house idiom, and a repair pass that re-opens a closed page on a question nobody put to it is the failure this repository has paid for repeatedly. It is handed to the close by name, in `state/open-threads.md`, in `state/continuity.md` and in the close prompt, so that the decision is visible and is not silently inherited.**

**AND THE TWO DAY-661 FINDINGS CANNOT BE PAID BY THE CLOSE, WHICH IS FORBIDDEN TO ALTER ONE WORD OF ANY CHAPTER. They enter the volume's record as two named open items rather than as a repair nobody owes.** The Batch 0005 continuity section had said a close "may repair them only under the narrow exception its own prompt gives it"; the close prompt grants no such exception. That contradiction is resolved in favour of the close prompt, which is the live instruction.

---

## SIX. `state/current.md` WAS REPAINTED BY THE PREVIOUS PASS AND STILL NAMED A VOLUME THAT WAS NOT IN FLIGHT

The head of the file — the pointer every phase reads before anything else — carried four faults, three lines after asserting that an index naming the wrong volume is a bug:

- the arrangement paragraph said **the volume in flight is VOLUME 08** and named *VOLUME 08 BATCH 0004, CHAPTERS 374 TO 383, DAYS 587 TO 596* as the governing section, and named the live threads section as *ADDED BY VOLUME 08 BATCH 0004*;
- reading-budget item 2 said **`outline/volume-09.md` is 51 KB**; the file is **156 KB**;
- reading-budget item 3 pointed **`tail -n 200 state/continuity.md` at the "Volume 09 Batch 0003 section"** — the foot of that file has been the Batch 0005 section for a full batch, so a writer obeying it would have taken the day clock from nineteen chapters and 55,920 words back;
- reading-budget item 5 carried **1,249,630 words across 422 chapter files**, twice — once in the head and once inside the Batch 0004 section, which is why repainting the head alone was not enough.

**All four are corrected in the head, because a head is an index and an index is edited rather than appended to, and the withdrawn forms are named beside the replacements.** The file's own rule — *a pointer in this file is only worth anything if the string in it can be found in the file it points at* — was then run against every pointer this pass wrote, and all four resolve.

**TWO MORE FOUND WHILE FIXING THOSE, BOTH IN THE SAME HEAD, BOTH THE SAME CLASS:**

- the size paragraph opened *"IS OVER 2.21 MB"* against its own exact figure of 2,212,700 bytes, which is **2.11 MB** — a rounded form disagreeing with the exact form beside it, in the paragraph whose entire job is to catch that;
- **the "Next phase" line said the close prompt "does not exist yet" and "is to be created by the phase that runs next." It exists, at 25 KB, and Batch 0005 created it.** A close obeying that head would have written its own prompt over the one it was dispatched by. **This is the `reviews/volume-08-planning-repair.findings.md` fault exactly — a pointer aimed at the phase that had already run — and it is the third class of pointer fault this head has now carried, after the wrong volume and the wrong file size. A stale figure is read and disbelieved; a stale pointer is obeyed.**

---

## SEVEN. THE CLOSING TELL IS WORSE THAN THE STATE SAID, AND THE CLOSE PROMPT WAS POINTING THE WRONG WAY AT IT

The Batch 0005 repair recorded that five of the nine chapters end their last body paragraph on the mark paragraph in some shape. **That is right and still is — Chs 435, 436, 437, 438 and 440**, three of them in the plain form that opens *The mark on that arm is four inches* and two of them in the re-shaped forms. **Two more carry it as the paragraph immediately before the last — Chs 439 and 441 — so the mark paragraph stands inside the closing movement of seven of the nine and is genuinely absent from two, Chs 433 and 434, where it sits four and seven paragraphs from the end. That second figure was not disclosed before and is given here so that a close counting by eye starts from seven rather than from five.**

**What it did not record is that a paragraph opening "Nobody thanked anybody" appears in SEVEN OF THE NINE, all but 436 and 439, while only Ch 441 ends its last body paragraph on it — and that the batch's own chapter cards end EIGHT OF NINE with the same two words.** The close prompt told the next phase to *"count the repeated closing constructions by eye"* and named five on the closing. It now names seven on the opening, which is the larger and the more visible measure.

**A threshold of 0.85 on eight shared words in order cannot see either, and never will. This is the fifth time that finding has been carried in this repository and the first time the disclosure has been the weaker of the two available measures.**

---

## EIGHT. THE BYTE-IDENTICAL ZERO IS TRUE, AND THE DENOMINATOR NEEDED A UNIVERSE RATHER THAN A REPLACEMENT — WHICH CORRECTS THE REVIEW'S OWN WORDING AND THIS FILE'S FIRST DRAFT

State: *"NIL, ACROSS 2,045 PARAGRAPHS."* The review called 2,045 *a count of a universe nobody can name*, and this file's first draft of the finding repeated that. **Both were wrong, and the truth is better than the review's version.**

**2,045 is a real universe and not a wrong figure. It is every non-empty paragraph of the forty-nine files with BOTH headings dropped** — the `# Chapter N` line and the `## ` subheading line. **2,094 is the same thing with only the `#` line dropped, and that is what the definition in `workspace/volume-09/batch-0005/PROMPT.md` produces, because that definition says *drop the heading* and the heading is singular, and its own implementation kept the subheading.** The two differ by forty-nine, being one subheading a chapter. Two further universes are 1,807 (the 30-word floor of guardrail 12) and 1,752 (the Volume 08 script, which also drops `>` blocks).

**THE DEFECT WAS NEVER THE NUMBER. IT WAS THAT A STATE FILE PUBLISHED A DENOMINATOR WITHOUT NAMING WHICH UNIVERSE PRODUCED IT — AND A DENOMINATOR IS THE ONLY FIGURE IN THIS WHOLE COMPARISON THAT CANNOT BE RECOVERED FROM ITS NEIGHBOURS, BECAUSE THE NUMERATOR IS NIL UNDER EVERY ONE OF THEM AND A NIL CARRIES NO INFORMATION ABOUT THE THING IT IS A COUNT OF.** Every other figure in this file can be checked against a sibling; this one could not, and it was quoted anyway.

**THE ZERO HOLDS ON ALL FOUR UNIVERSES. AND THE GATE RETURNS NIL ON BOTH READINGS OF *DROP THE HEADING* — all four figures, 0 and nil, either way — so the ambiguity in the rule changes no result and is now named in the close prompt rather than left sitting in it. All four universes are published so that nobody quotes one and believes it is another.**

---

## NINE. TWO PROSE DEFECTS IN THIS BATCH, BOTH REPAIRED IN THE WORDS OF THE PAGE

1. **`chapter-0441.md:5` — an antecedent muddle.** *"those fields have waited for the sixty-first morning, and this is the thirteenth of them"* sent *them* back to the sixty-one mornings when the thirteen is a count of fourth-line mornings in the volume. **The underlying claim checks out** — all thirteen fourth-line mornings of Volume 09 came round and went away empty, across days 606, 610, 614, 618, 622, 626, 630, 634, 638, 642, 646, 650 and 654 — so this is wording, not a false fact. The page now says *this is the thirteenth morning that line has come round empty on*, and the count of the twelve before it is unmoved.
2. **`chapter-0433.md:33` — a time collision.** The ditch paragraph put Marek in the boundary ditch finishing the last eleven yards standing in water at about the fifth hour; the yard paragraph put the water through the yard at about the fifth hour with Marek in the yard at the time, and the six had been on the west side of that ditch from the second hour to the seventh. **The water now comes through the yard before the six go out**, which is also what the fourth-hour reading in the porch requires, with the man of about fifty reading it behind two inches of standing water.

**AND ONE MORE FOUND WHILE REWRITING THE CLAUSE FOR FINDING ONE, WHICH NOBODY FLAGGED: `chapter-0440.md:42` put the county's shortage on "a sheet nine hundred yards off." Nine hundred yards is the distance of the well house door. The shortage figure came up to the one room in Tova Reed's own hand on the Saturday evening and is on a sheet in that room, where the chapter's own `>` block puts it.** The page now says the sheet is in the one room.

---

## TEN. WHAT WAS WITHDRAWN, AND WHAT WAS DECLINED

**WITHDRAWN AND NAMED, IN EVERY FILE THAT CARRIED IT:** a gate of **1 / 22 / 67**; the named pair of **0.854**; an unnamed byte-identical denominator of **2,045**; a `next month` sweep of **eight in seven**; `chapter-0408.md:41` at **day 623**; ***all three of which are day 661***; ***the volume reaches twenty-seven*** as the answer to the ceiling; **26,746**; **2,971.8**; **27,746**; **141,663**; **1,305,561**; **3,000 / 2,996 / 2,960 / 2,912 / 2,982 / 2,914 / 2,990 / 2,994 / 2,998**; **1,249,630**; **422 chapter files**; **51 KB**; **VOLUME 08 BATCH 0004** as the governing section; and the close prompt's "does not exist yet".

**DECLINED, WITH THE REASON:** the compaction of the three append-only state files, on the reason written four times at the head of `state/current.md`, with the reading budget's internal staleness repaired in its place instead; `state/phase-ledger.json`, which is controller-owned and is the fifth time it has been reported and declined; `outline/volume-09.md` and `outline/ending.md`, which are completed phases' files and are reported against and not edited, including the ceiling breach; and the rewrite of `chapter-0417.md:16`, for the reason at Finding Five.

**THE FIGURES AFTER THE PROSE MOVED, RE-MEASURED WITH `wc -w` INCLUDING THE HEADINGS, AFTER THE PROSE AND NOT BEFORE:**

**BATCH 0005: 2,994 / 2,996 / 2,958 / 2,912 / 2,981 / 2,914 / 2,983 / 2,997 / 2,999, BEING 26,734, A MEAN OF 2,970.4, A MINIMUM OF 2,912 AT Ch 436 AND A MAXIMUM OF 2,999 AT Ch 441, ALL NINE INSIDE THE BAND OF 2,600 TO 3,050 WHICH WAS NOT WIDENED AND ALL NINE INSIDE THE BATCH TARGET OF 2,900 TO 3,000.** The whole of Volume 09 is forty-nine chapters at a minimum of 2,671 at Ch 402 and a maximum of 3,017 at Ch 429, all forty-nine inside the band.

**BATCH 0001 IS 27,753, THE ONLY OTHER BATCH THAT MOVED, BEING THE SEVEN WORDS THE Ch 400 REPAIR ADDED.**

**VOLUME 09: 27,753 + 29,178 + 28,808 + 29,185 + 26,734 = 141,658 ACROSS FORTY-NINE CHAPTERS. THE MANUSCRIPT IS 1,163,898 ACROSS THE 392 CLOSED CHAPTERS PLUS 141,658 = 1,305,556 ACROSS 441 CHAPTER FILES, WITH NO RESIDUAL. NOTHING IS PROJECTED.**

**MECHANICAL, ALL ZERO, ALL 49 FILES:** non-ASCII, curly marks, trailing whitespace, consecutive blank lines, unbalanced quotation marks, unbalanced bold markers, missing final newline. Zero instances of `this batch`, `this chapter`, `this volume`, `famine`, `seat`, US spellings, or a bare `batch`/`chapter` outside a heading. Three `nest` hits are all inside *honest*.

---

## THE RULE, AND IT IS THE FIFTH WRITING OF IT

**A FIGURE TAKEN BY A RULE RATHER THAN BY A SCRIPT IS NOT A FIGURE. The gate, the ceiling, the sweep, the day arithmetic and the denominator were all taken by hand and all five were wrong. The fifteen word counts were run and all fifteen were right. A close that inherits a figure without the script that produced it is inheriting the five, not the fifteen — and the fifth of those five had been sitting in the state layer, in two state files and in the prompt that dispatches the next phase, since Batch 0005 shipped.**

**AND THE GENERALISATION THIS PASS ADDS, WHICH IS THE SIXTH WRITING OF IT AND THE ONE THAT COST THE MOST: A CHECK THAT EXISTS IN TWO WRITTEN DEFINITIONS AND HAS BEEN MEASURED IN A THIRD CANNOT BE RE-RUN BY ANYBODY, AND THE FIGURES IT PRODUCES ARE NOT WRONG, THEY ARE UNATTRIBUTABLE. THE REPAIR FOR THAT IS NOT TO PICK ONE DEFINITION AND HIDE THE OTHER. IT IS TO RUN BOTH, PUBLISH BOTH, AND NAME THE RULE THAT PRODUCED EACH — WHICH IS NOW WHAT THE CLOSE PROMPT ORDERS, AND WHICH IS THE FIRST TIME IN THIS VOLUME THAT A MEASUREMENT HAS BEEN HANDED ON WITH THE TOOL THAT MADE IT.**
