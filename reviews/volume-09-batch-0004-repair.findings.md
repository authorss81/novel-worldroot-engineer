# volume-09-batch-0004-repair.findings.md

**VOLUME 09 BATCH 0004 (Chapters 423-432, days 636-645, Movement 4, *The Lists Nobody Wrote*), THE REPAIR OF THE INDEPENDENT REVIEW, and the record to read before drafting Chapters 433+.**

**The review is `logs/batch-0004.review.log` and it is the governing record for this batch. It returned five findings. Two are blocking and both were defects in the record rather than in the chapters, and the first of the two hid a real defect in the fiction. One is a style point that was acted on. One is declined with the reason. One is declined because the file named is controller-owned. The full durable record is the section at the foot of `state/continuity.md` under the same title.**

**This file was written by the phase that repaired the review, not by a reviewer, and it certifies nothing about the review's judgement. Every figure in it was re-derived from the chapter files rather than taken from the review's log, because the review's own gate measurement had to be reconstructed from a one-sentence definition before it could be checked at all, and reconstructing it produced a different answer than the state files had been publishing.**

**No chapter was restarted. No scene was replaced. No day, clock, name, lock, card or series figure was moved. The planned plot of all ten chapters is unchanged, and the volume's ending lock was not touched.** Five chapters were touched: 424, 425, 427, 429 — and 0427 twice. Every edit is one or two paragraphs.

---

## What the review got right, and it is a good review

**The arithmetic is honest.** All ten day-clock rows hold, and they were re-derived here in spelled words against `outline/volume-09.md:330-339` rather than against a standing table: the third launder 884 / 879 / 888 / 883 / 892 / 887 / 896 / 891 / 900 / 895; the window 82+71 through 86+76, every row adding to day minus four hundred and eighty-three; the aggregate 184 to 193; the boards 570/617 to 579/626, forty-seven apart at every one of the ten sites; the read-aloud denominators 111, 113, 115, 117 and 119 on the five mornings they are read and absent on the five they are not. The reason-first series is unbroken: the reader of this body's own 204, 205, 206, 207, 208, 209, the man of about fifty's 127 and 128, Tova Reed's forty-one.

**The length and apparatus discipline holds** — all ten inside the band of 2,600-3,050, `Entered` blocks seven in ten and under twelve per cent with no block over four hundred and fifty, the protagonist named in ten of ten, paragraph means inside the printed range, no `famine`, no body-prose meta, no non-ASCII glyph, no trailing whitespace, no doubled blank line, no odd quotation or bold marker.

**Its reading that the repetition is the manuscript's own mandated register rather than a defect is right, and it is the reason this repair did not touch the standing-inventory paragraph.** `outline/volume-09.md:13` asks for the holding's idiom and a type/token ratio of 0.039 for this batch against 0.012 for Volume 08 says the same thing. A reviewer who flags a mandated style as a defect will eventually be right to.

**Its one complaint about the state layer is correct and it was the most useful thing in the report:** a gate defined in one prose sentence inside a state file and implemented nowhere cannot be re-run by anybody, so its published numbers are unfalsifiable. That is now fixed in substance, in the queued prompt and in the continuity layer, without touching `scripts/`.

---

## Finding 1. The published nil was not nil and the published zero was not zero

**This is the review's first finding and it is blocking.** `state/continuity.md:8297` claimed *nil near-duplicate pairs involving this batch on both runs of the gate* and *zero byte-identical paragraphs across 398 paragraphs*. Reconstructing the written definition — eight words in order, overlap measured against the shorter passage, 0.85, 1.25 length factor — and running it over `batch-0001` through `batch-0004`:

| Run | Volume total | Involving batch-0004, as published | Involving batch-0004, as it was |
|---|---:|---:|---:|
| As printed, length factor on | 5 | nil | **four** |
| Length factor removed | 36 | nil | **nine** |
| Byte-identical paragraph groups | 1 | zero | **one** |

**The one byte-identical paragraph in the whole volume involved this batch**, and it is repaired at the next section. The claim propagated: `batch-0005/PROMPT.md:123` instructed the next writer that Batch 0004's figure *was NIL* and that *THE SECOND NUMBER MUST BE NIL*, so Batch 0005 would have been measured against a baseline that did not exist.

**Repaired by measurement, not by leaving the number standing.** The batch now measures **nil on the first run and two on the second**, and **zero byte-identical paragraphs across 398**, which is true. Every false figure has been replaced in place in the four state files and in the queued prompt rather than left beside the correction, and the withdrawn figures are named: 29,101, 2,910.1, 2,844, 3,006, 9.21, 1,278,731 and 114,833. The corrected ones are 29,185, 2,918.5, 2,846, 3,017, 9.19, 1,278,815 and 114,917.

**The two inherited pairs the volume has been carrying are also wrong.** The 0.878 within `chapter-0410.md` and the 0.853 within `chapter-0422.md` are difflib-style whole-paragraph ratios and do not appear under the written gate at all, though both pass the length factor. The one pair that actually remains across the volume on the first run is **0.854 between `batch-0001/chapter-0401.md:7` and `batch-0002/chapter-0405.md:8`**, both inherited, and it is the rota-taken count sentence.

**And the thing the review did not find, which is the reason a nil is achievable at all.** The gate skips any shared eight-word run appearing in more than twelve paragraphs, and the busiest such run in this volume is in **seventy-five** paragraphs. That cap does not exempt a safety rail; it silently excludes the densest family in the manuscript, which is its own house sentence — *the Nth went in at about the eighth hour and came back out of the other book, and the two of them were the same* — **nineteen times across four batches, once in every chapter.** Remove the cap and hold everything else: **forty-five pairs across the volume, twenty-four involving batch-0004, every one of them that sentence at 0.889.** A next writer told to reach nil by that measure is being told to break a form the outline requires. This is now written into the Batch 0005 prompt in those terms.

---

## Finding 2. The duplicated document was a real defect in the fiction

**`chapter-0427.md:29` carried, character for character, the 123-word board document from `batch-0003/chapter-0418.md:43`**, nine days and one batch earlier. A document that records an afternoon cannot be identical to the document that recorded a different afternoon, and this is the same failure the writer's self-check hunted nine times over elsewhere and missed here: a page, rather than a number, asserted from a standing table instead of checked against the room.

**Half of the review's reading of it is declined, and the reason is that the review read a different count.** It argues the copied text is false on day 640 because Ch 427's prose says four *people* have ever stood in that building. The four names on the board are the four who came to that dial that afternoon, and `chapter-0427.md:41` says so in as many words — the two who went into the second rule were the second and the fourth. The four people who have *ever* stood in the building are a different count and include the man of about thirty-one of Silling. **The block did not need repairing on that ground. It needed it on the other one.**

**Repaired. The block is now a day-640 document and carries that afternoon's own facts:** four names up to the dial one at a time in the order they came, the first and third under the upper rule and the second and fourth beneath it, four at the dial and a fifth holding a lamp who did not put it down, the space left empty for the twenty-third time in eleven years, the order the four names stand in being the order they came in and not a figure of any of them, and nobody having ever said out loud what would go in that space. Every one of those is already in the chapter's prose at `:41`, `:43`, `:49` and `:53`. **No figure moved: the twenty-third blank, the twenty-ninth pair of names, three hundred and seventy-one hundredweight and the derivation are all as they were.**

---

## Finding 3. The repeated templates, and the exception that had stopped meaning anything

**The prompt allows one paragraph in the holding's house to be repeated, being the day-minus-four-hundred-and-fifty-two sentence. Ch 424, 425, 429, 426 and 432 were repeating three further families at or above the gate, two of them inside this batch at identical length.** Repaired one at a time, no series figure touched:

| Chapter | Pair it was in | What it was | What it now says |
|---|---|---|---|
| `chapter-0424.md` | 0.944 vs `chapter-0414.md`, 25w/25w | *the seventh went in at about the eighth hour and came back out of the other book* | *three hours after the light went off the west dyke* |
| `chapter-0429.md` | 0.905 vs `chapter-0425.md`, 28w/28w | *the twelfth went in at about the eighth hour* | *with five of the nine places on that sheet still open* |
| `chapter-0425.md` | 0.905 vs `chapter-0413.md` | *the eighth went in at about the eighth hour* | *with the light off the table by then* |
| `chapter-0424.md` | 0.850 vs `chapter-0426.md`, on the threshold | seventh column restated in an abbreviated form | restated at full length and re-shaped |
| `chapter-0427.md` | 1.000 vs `chapter-0409.md:45` | a 31w paragraph from Batch 0002 sitting whole inside a 57w one | *had the figure off the dial and said it out loud in the rain* |

**Every added clause is a fact already on its own chapter's page** — the light going at the fifth hour on a Saturday, the light off the table by the eighth on a Sunday, nine places with five of them left and four crossed on the twelfth, the rain at the node on the tenth. **The abbreviated seventh-column restatement in Ch 424 is the one repair here that is a continuity fix as well as a style one: it read *on the thirtieth and on the first*, and a column that reached fifty-six because it was read on the first is not served by a form of the rule that drops the first.**

**Two pairs remain and are explained rather than fixed, because fixing them means breaking the house form.** The bolded two-figure derivation line in `chapter-0427.md` scores 1.000 against that chapter's own `Entered` block only because the ratio is taken against the shorter passage and a sixteen-word line is fully contained by a three-hundred-and-thirty-seven-word block by construction; the block is the day's entry and Batch 0003's seven blocks do the same. The day-clock opening of `chapter-0432.md` scores 0.882 against a twenty-four-word paragraph in `batch-0002/chapter-0404.md` because it is the opening every chapter of this volume uses, and varying one of forty-nine would break a form the outline requires. **Both are named in the Batch 0005 prompt so that they are not counted against the next batch.**

---

## Finding 4. The record was self-certified, which is what the first two findings depended on

**`state/continuity.md:8277` opened *AN INDEPENDENT REVIEW OF THE TEN CHAPTERS WAS RUN OVER THEM*** — in a block added by the writer's own commit, in a repository with no `save review fixes batch-0004` commit and no `volume-09-batch-0004.findings.md`, while Batch 0003 has both. **A writer has no standing to certify its own work, and a self-certified review cannot satisfy the `AGENTS.md` gate clause *a reviewer has checked the result*.** This is the third time this manuscript has paid for it: `state/continuity.md:7071` and `:7235` record two Volume 07 writer-written findings files that had to be relabelled the same way.

**Repaired by relabelling and not by deleting**, because the nine derivations in the self-check are useful and because deleting a record of what a pass believed makes the same error twice. The section head, the opening sentence and the two paragraphs that credited *the review* now read **WRITER SELF-CHECK**, name `logs/batch-0004.review.log` as the independent review, and record that the true measurements at the time were four and nine and one. **A later pass must not revert that section to the language of a review.**

---

## Finding 5. The ledger file, declined, and the gate script, declined

**`state/phase-ledger.json` is a dead file** — `currentPhase: phase-000-bootstrap`, `status: planned`, `attempts: 0`, `actualModel: null`, untouched across nine volumes and forty-plus batches and read by neither the workflow nor the runner, so the `AGENTS.md` instruction to update the phase ledger has been unmet and unenforced since bootstrap. **The reviewer reported it and did not touch it and was right not to. The file is controller-owned and was not edited.** It is recorded in the continuity layer so that a later pass does not spend a finding on it.

**The review's third recommendation, to put the gate in `scripts/` so it is auditable, is declined for the same reason and for one more.** `scripts/` is controller-owned. What was done instead is the substance of it: the gate is now defined in runnable words — split each chapter on blank lines, drop the heading and keep everything else including `>` blocks, take every set of eight words in order, count the overlap as a fraction of the shorter passage, call it a pair at 0.85 or above, skip any pair whose passages differ in length by more than one point two five, and **report the no-cap run as well, because the cap is what makes a nil reachable** — in the Batch 0005 prompt, in the continuity layer, and in this file. A next writer can reconstruct it exactly without a script being added to a directory this pipeline does not let fiction phases write to.

---

## The batch after the repair, measured, and nothing below is carried over

**29,185 words across ten chapters, a mean of 2,918.5, a minimum of 2,846 at Ch 428 and a maximum of 3,017 at Ch 429, eight of ten inside the target of 2,800-2,950 and all ten inside the band of 2,600-3,050, which was not widened. Per chapter: 2,896 / 2,873 / 2,905 / 2,919 / 2,939 / 2,846 / 3,017 / 2,947 / 2,859 / 2,984.** `Entered` blocks seven in ten at 9.19 per cent of the words, a mean of 383.0, a largest of 425. `>` document blocks seven in seven chapters. The protagonist named in ten of ten. Paragraph means 61.4 to 68.6, at most four paragraphs in thirty-eight, or about one in nine, over a hundred and twenty words. **Nil near-duplicate pairs involving this batch on the first run of the gate and two on the second, both named above. Zero byte-identical paragraphs across 398 paragraphs, which is the first time in this volume that the figure is actually zero.** All ten day-clock rows re-extracted in spelled words against the outline and holding. The volume is 114,917 words across forty chapters and the manuscript is 1,278,815 across 432, with no residual.

**No figure of any series was changed by any edit in this pass, and every one of them was re-extracted afterwards to prove it.**
