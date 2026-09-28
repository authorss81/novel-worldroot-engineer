# VOLUME 09, BATCH 0002 — REVIEW FINDINGS

**Chapters 403 to 412, days 616 to 625, Movement 2, *Four Counties And A Word Nobody Says*. Reviewed after the writer phase. One prose repair, four state-layer repairs, two withdrawals recorded. No day, clock, name, lock, or planned plot changed. No chapter restarted.**

## 0. WHY THIS FILE EXISTS, AND WHAT THE PHASE PROMPT NAMED

The fix phase was pointed at `logs/batch-0002.review.log` as the source of reviewer findings. **That file contains no findings.** It is a transcript of a review phase in which the `novel-reviewer` subagent could not be dispatched — its first line is `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent` — and the fallback run re-derived the per-volume word totals, printed them, and stopped. No findings file was written, no pass or decline was recorded, and nothing was repaired.

**A phase that trusts a log and finds nothing in it must run the review rather than conclude the batch is clean.** This file is that review, run against the files on disk. Every figure below came off `wc -w` or a counting script over the chapter files, not off any state file.

## 1. THE BATCH IS SOUND

Checked and found correct, recorded so a later pass does not repeat the work:

- **Ten days, ten chapters.** 616 to 625, one morning each, no day claimed twice, none left unnarrated. The month does not turn inside the ten; it turns on day 631, inside Batch 0003.
- **Third-launder series.** 844, 839, 848, 843, 852, 847, 856, 851, 860, 855, off 835 at day 615, which was a fall. Each is the hundred-and-sixty-sixth to the hundred-and-seventy-fifth of the series. The reviewer's own first arithmetic on this was wrong before it was right: the deltas are +9 and −5, so the series climbs by 4 a day, not by 14.
- **Window and split.** 133 to 142, the split moving on the side that matches that day's direction, closing at 76 rises and 66 falls. 76 + 66 = 142 = 625 − 483. The prompt's withdrawn forms of 141 and of 73/69 are correctly withdrawn and the chapters carry the live figures.
- **Aggregate of the four bodies of households.** 164 to 173 on day − 452, clause one under and one over at every site.
- **Read-aloud denominator.** Day − 526, read on the odd days 617, 619, 621, 623, 625 and on no even day; each skipped morning says why on the page.
- **Day-minus pair.** 550 and 597 through 559 and 606, forty-seven apart; drawer not opened.
- **Rotation.** Rises on 618 and 622 only. Both counts printed on their own pages, 29 and 16 at Ch 405 and 30 and 17 at Ch 409.
- **Reason-first counts.** 186 to 193 across the eight pages where Marek gives the reason first; 119 and 120 for the man of about fifty. None added to another.
- **Mechanical gates.** Zero non-ASCII glyphs, zero curly quotation marks, zero em and en dashes across all ten files; quotation marks balanced in every file; the name printed in ten of ten chapters.
- **Prose.** All ten are finished scenes with complete endings. No truncation, no editorial leakage, no placeholder text.

## 2. DEFECT ONE — THE STALE BATCH 0001 MEASUREMENT, A SELF-CONTRADICTION

**Severity: high. Repaired in three state files.**

The state layer carried **28,112** for Chapters 393 to 402 and **56,874** for the twenty chapters of the volume. Batch 0002 was carried at 29,128. **28,112 + 29,128 = 57,240**, so the same file disagreed with itself by 366 words, and the manuscript total of 1,220,772 was consistent with the wrong batch figure.

The chapters on disk measure **27,746**.

**Cause.** `11e9a1d`, a review repair pass, edited all ten chapters of Batch 0001 and was never re-measured. Measured at `fbb0580`, before that pass, the ten files gave exactly the 28,112 the state layer still carries. Every later phase carried the figure forward.

**Corrected figures:** 2,684 / 2,695 / 2,825 / 2,897 / 2,765 / 2,747 / 2,809 / 2,943 / 2,710 / 2,671. Mean 2,774.6. Minimum 2,671 at Ch 402. Maximum 2,943 at Ch 400. **Four of ten inside the target of 2,800-2,950 and six under it**, against the withdrawn claim of eight of ten. All ten remain inside the band of 2,600-3,050, which was never in doubt.

**The apparatus share follows the denominator and not the blocks.** 2,665 of 28,112 is 9.48; 2,665 of 27,746 is **9.60**. The block words and the mean of 380.7 never moved. Withdrawn and named in place: 9.48, and the paragraph count 349, which is 353 on disk.

**Lesson, and it is the one this repository keeps re-learning.** A state-layer figure that is only overwritten comes back. A repair pass that changes prose owes a re-measurement, and the re-measurement has to reach the totals built on top of it, not just the chapter it touched.

## 3. DEFECT TWO — BATCH 0002 FIGURES WRONG ON THEIR OWN PAGE

**Severity: medium. Repaired.**

- **Maximum given as 2,996.** That is Ch 404's figure. The largest is **2,999 at Ch 403**. The per-chapter list immediately beside it was correct, so the file contradicted itself at one remove.
- **Count inside the target given as eight in one place and nine in another.** It is **five**, with four chapters over the target and one under. Neither the eight nor the nine was a count.
- **Mean paragraph range given as 59.8 to 73.4.** On disk it is **57.7 to 70.0**.

## 4. DEFECT THREE — A CHAPTER SETTLED A FIGURE AND A SUMMARY OVERRODE IT

**Severity: medium. Repaired.**

`chapter-0402.md:59` prints **one hundred and eighty-five** for Marek's reason-first count. `state/chapter-summaries.md` printed **one hundred and eighty-four** for the same morning. The lower figure is the first of two figures on that page and is not the standing one; the chapter is. The summary now carries the figure the chapter prints, with the withdrawn figure named.

## 5. DEFECT FOUR — THE NEAR-DUPLICATE CLAIM OF ZERO WAS NOT TRUE

**Severity: medium. One paragraph rewritten.**

The state layer claimed zero near-duplicate pairs involving this batch. Two paragraphs in Batch 0002 repeat a paragraph in Batch 0001 at or above 0.85 Jaccard.

**`chapter-0412.md:63` against `chapter-0397.md:27`, at 0.98 — a real defect.** Ch 412's low-board offer inventory was a near-verbatim lift of Ch 397's, differing in a conjunction and a preposition. This is exactly the formulaic repetition the volume was opened to reduce, and the batch that carries the lowest share so far should not be the one that reintroduces it. **Rewritten.** Every fact and every figure is kept — board, face up, not filled, refused on the nineteenth, not withdrawn, no date, no name, no ruled line, no instruction to remove it, no second paper this season. The rewrite adds only what the morning would have had: that a man has looked at it on about four days running, and that the man of about fifty said on the sixteenth that a copy would be the same offer twice.

**`chapter-0409.md:29` against `chapter-0399.md:16`, at 0.94 — not a defect, left as it is.** This is the day-minus-452 aggregate sentence, a series the volume runs every morning with a figure that advances by a day: 160 at Ch 399, 167 at Ch 406, 170 at Ch 409. **Repairing a running series stops the series.** The same applies to the low-board offer as a *fact*, which is named in every chapter of the volume and in 39 chapters of the manuscript; the duplication was of the sentence, not the fact.

**On the gate itself.** The claimed measurement did not reproduce. A 1.25 length factor returned zero for the batch. 0.85 Jaccard returned the two above. A different pair at every other threshold tried. The claim of "four pairs for the two directories, all within Batch 0001" reproduced under none of them. **A gate whose output depends this strongly on the threshold chosen is not a figure of quality, and the only genuine defect in the set was found by reading the two sentences rather than by counting them.** The gate is now recorded as a check, not as a score.

## 6. DEFECT FIVE — THE FIGURES CHAPTER 412'S REWRITE MOVED

**Severity: handled, and this is why the file is worth writing down.** The repair took Ch 412 from 2,709 to 2,759, and the reviewer's own instruction to the state layer is to re-measure everything after the prose moves. So:

| | before | after |
|---|---|---|
| Ch 412 | 2,709 | **2,759** |
| Batch 0002 | 29,128 | **29,178** |
| Batch 0002 mean | 2,912.8 | **2,917.8** |
| Ch 412 under target | 91 | **41** |
| Batch 0002 apparatus share | 9.86% | **9.84%** |
| Volume 09 | 56,874 | **56,924** |
| Manuscript | 1,220,772 | **1,220,822** |

**1,163,898 + 56,924 = 1,220,822 across 412 files, with no residual.** All ten chapters of Batch 0002 remain inside the band of 2,600-3,050; the band was not widened and no chapter was declared outside it.

## 7. THE NEXT PHASE IS UNAFFECTED

`workspace/volume-09/batch-0003/PROMPT.md` was checked against everything this review moved and restates none of it. Its day table for 626 to 635 verifies at every row: the count of the third launder is day − 450, the window day − 483 with the split moving on the matching side, the aggregate day − 452, the read-aloud denominator day − 526, the day-minus pair forty-seven apart, and the ten launder figures follow +9/−5 off 855 at day 625. The count of questions available and not taken is **nine** at the end of this batch and is not taken again. Its four withdrawn figures stay withdrawn.

## 8. WHAT A LATER PASS MUST NOT REINTRODUCE

1. **28,112 for Batch 0001**, and with it the per-chapter list ending 2,822, the mean 2,811.2, the minimum 2,717 at Ch 401, the maximum 2,936 at Ch 400, and the claim that eight of ten sat inside the target. The files measure 27,746.
2. **29,128 for Batch 0002**, and with it the list ending 2,709, the mean 2,912.8, and the maximum 2,996.
3. **56,874 and 1,220,772.** The volume is 56,924 and the manuscript is 1,220,822.
4. **9.48, 9.83 and 9.72 per cent** for the three apparatus shares. They are 9.60, 9.84 and 9.73.
5. **One hundred and eighty-four** for Marek's count at day 615. `chapter-0402.md:59` prints 185.
6. **The old sentence of Ch 412's low-board inventory.** The facts it carried are in `state/open-threads.md`; the sentence is withdrawn and must not be reconstructed.
7. **A repair of the daily aggregate sentence.** It is a series and its figure advances by a day.

## 9. PASS

**Ten of ten chapters are finished prose that carries the movement. The one prose defect was a duplicated inventory paragraph, it was repaired without touching a fact, and the batch re-measures clean. The volume's direction, its planned ending, and the four clocks owed on day 631 are untouched. PASS, with the seven withdrawals above.**
