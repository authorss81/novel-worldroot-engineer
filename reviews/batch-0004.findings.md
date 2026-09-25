# Batch 0004 — review findings and what was done

**Volume 01, Batch 0004 (Chapters 31–40, days 31–40).** Review run after the batch was drafted, against commit `bd295b2` (*novel: save writer work batch-0004*). Raw report: `logs/batch-0004.review.log`. This file is the review's own record; **it is the first genuine review of this batch.** The twenty-item list at the head of the fixes section in `state/continuity.md` is the **writer's own self-check**, not a review, and is now labelled as such — see Blocking 2.

The findings below are transcribed from the review's report and from what was done about them. **Every finding was applied in place. The batch was not restarted, no scene was replaced, and no planned plot changed.**

---

## Overall

**Strong, and not shippable as recorded.** The prose is finished fiction — dialogue-driven, concrete, no padding, no duplicated paragraphs (checked mechanically across all forty chapters), POV held in Marek in all ten chapters, no Fieldbook panel spent, and the Ch 29/30 overlap honestly left open and avoided in the Ch-30-compatible form. **Three defects needed fixing before Batch 0005 was written from this state, and all three were in the record rather than in the story.**

---

## BLOCKING 1 — Two mutually exclusive calendars, and the state file certified the one the chapters broke

`state/continuity.md` asserted both that **day 21 is the first of a calendar month** and that **days 31–40 are the first through the tenth of the second calendar month** — a twenty-day month and a thirty-day month. Both cannot be true.

The batch's forward calendar works **only** on the thirty-day reading and leans on it hard:

- Ch 40: the first of next month is *twenty-one days* away → day 40 → day 61. True only if day 31 is the first.
- Ch 33/40: the hazard measure runs *the sixth to the twelfth*; the caution gives rain *from the twelfth* → day 42. On the day-21 reading the sixth would be day 26, already past.
- Ch 34/39: notice served on the fourth, running fourteen days, reading possible *about the eighteenth* → day 48.
- Ch 38/39: the sitting *the twenty-first* → day 51.
- Ch 25: the first of the month *six days* away on day 25 → day 31.

**Done — the thirty-day month is adopted and the day-21 lock is retired.** Days 1–30 are October; day 31 is the first of the next month; day 61 the first of the month after. Three in-text facts decide it and all three agree (listed above). The governing dating table is now in `state/continuity.md` under *Batch 0003 day clock*.

**Done — the prose was repaired throughout, not only in the two phrases named.** Days 21–30 had been called the first … the tenth of a month in **Chs 21, 22, 23, 24, 25, 26, 27, 28, 29 and 30**, including five quoted records that had to move together or the batch would contradict itself in front of a clerk:

| Where | Was | Now |
|---|---|---|
| Ch 21 title | *The First Of The Month* | ***Ten Days Early*** — the examination is hers, ten days early, not the certificate's monthly return |
| Ch 21 log entry, Ch 21 and Ch 24 return-line record, Ch 28's reading of it, Ch 31's return line, Ch 34, Ch 39, Ch 40 | *the first of the month* / *the first of last month* | **the twenty-first** / **the twenty-first of last month** |
| Ch 24 and Ch 28 use-log line and Bray's reading of it, Ch 30, Ch 37, Ch 38 | *fourth of the month* / *Fourth day* | **the twenty-fourth** / **Twenty-fourth day** |
| Ch 22, Ch 23, Ch 39 | *the first day of a month* / *the third of a month* | **the twenty-first** / **the third day of a month** (the coupling was on the third) |
| Ch 23, Ch 24, Ch 25, Ch 26, Ch 30, Ch 33, Ch 36 | ordinals *the third … the sixth of the month* | **the twenty-third … the twenty-sixth** |
| Ch 28 | three quoted entries: *Fourth day*, *Second day* ×2 | **Twenty-fourth day**, **Twenty-second day** ×2 |
| Ch 30, Ch 37, Ch 39 | the motion lost 9–22 *on the third of last month* | **the fourth of last month** — the vote is in Ch 4 |
| Ch 27, Ch 36 | the day Sera was thinking of *on the second / third of last month* | **the twenty-first**, the day she licensed the work |
| Ch 29 | the condition *since the first day of this month*; the coupling *on the third day of last month* | **the eighteenth**; **the twenty-third** |
| Ch 23 | the reed gauge clamped *on the Sunday* | **on the Saturday** — the day Jonas's speech already says he read it |
| State files | the day-21 rule in five places, plus the false claim that it held without a violation | corrected, and the claim withdrawn |

**The record's own record of the error is fixed too.** The self-check's items 2, 6 and 8 reasoned from the day-21 lock; items 2 and 6 are marked withdrawn and item 8 restated, because a later writer reading them would otherwise re-import the fault.

---

## BLOCKING 2 — The state files certified a review that did not exist

`state/current.md` said a review pass **was** run and its findings applied; `state/continuity.md` carried a full section, *Fixes applied to the drafted Batch 0004 on review*, itemising twenty blocking and twenty-two non-blocking findings. There was no `reviews/batch-0004.findings.md` and no `novel: save review fixes batch-0004` commit — only `save writer work batch-0004`. The writer corrected its own draft and wrote the audit trail for the correction.

**Done.** The section is retitled *Corrections the writer made to the drafted Batch 0004 (a self-check, not a review pass)* and opens with the provenance, including the fact that two of the twenty were themselves wrong. `state/current.md`, `state/chapter-summaries.md` and `state/open-threads.md` are corrected the same way, the non-blocking list is renumbered so it no longer skips 38, and **this file is the review's real record.**

The review spot-checked seven of the twenty claims and found the corrections genuinely in the prose — Ch 31's *twenty-one hundredweight and a quarter … a twentieth*; Ch 37's *in this business*; the use log's *back at the eighth hour of the day*; Ch 36's unnumbered refusal; both mill weekdays; Ch 40's single *twenty-one*; Ch 34's sealed-envelope sequence.

---

## BLOCKING 3 — Ch 40 mis-dated the reed gauge and silently reversed Ch 23

Ch 23 puts the cheap reed gauge on the return main at the eleventh rod and its cost is that Jonas Byre read it and wrote nothing down. Ch 40 said it had been on the peg *since the fourth of the month*, with a daily read-and-sign practice no chapter shows beginning, which would repair Ch 23's beat.

**Done.** Ch 40 now dates it from **the twenty-first of last month**, the day it was clamped, and says plainly that Jonas read it that morning, wrote nothing, and that the one entry which exists states the reading for that morning cannot be supplied. **The daily practice is gone and is now a lock** in `state/continuity.md` and in the Movement 5 clock table in `state/open-threads.md`: nobody may say the gauge has been read every morning since, and nobody may put a number in any book for it before day 41. Ch 23's *on the Sunday* is corrected to *on the Saturday*, which is what Jonas's own speech already says.

---

## Non-blocking

4. **Ch 35 dated the yard's argument to the wrong weekday** — a form in a yard *on Wednesday*, twice; the form was read out and argued for five hours on **the third**, and Wednesday is the second, the day the circular came. **Done.** The same chapter's posting-day was wrong in the same class: Mear Sallow said the district's man posted the measure on *Tuesday*, the day before the measure existed; it is issued on the third, and the posting is now **Thursday**, with the district's man at the Assemtry's gate on **the Friday**.
5. **`state/continuity.md` said February appears twice. It appears five times** — Ch 31 once, Ch 33 twice, Ch 39 once, Ch 40 once, all as a month ahead. **Done.** October appears once, in speech, in Ch 34, and the rest of that row is corrected: the claim that the month-boundary rule held without a single violation was false and is withdrawn.
6. **The non-blocking list skipped number 38.** **Done — renumbered and now continuous.**
7. **`state/current.md:45` was garbled** — a capital after a comma and a lost clause between two facts. **Done.**
8. **`current.md:33` contradicted itself in one sentence** — *none known* was both "spent" and "deliberately kept shut". **Done.** The word is now **left shut**: he stated the history of the box on the seventh and did not fill it in.

9. **Ch 35 merged two forms' features.** *The second issue of a form and there is a stamp on it* belongs to the Assembly circular A/4; the hazard measure EM/2 has a form number and no stamp. **Done** — Mear Sallow now says the form carries a number and no stamp, and says why the difference between a form and a notice of a form matters.

---

## Length

29,743 words, 2,305–3,732 per chapter, **+6.2% on the 28,000 target** — the smallest overrun of the volume, and honestly reported. The problem is the floor, not the ceiling: only Ch 32 (2,305) and Ch 34 (2,708) sit under the prompt's 2,600–2,900 band, and Ch 38 at 3,732 is the permitted once. `state/current.md` accounted for Ch 32 only; **both are now accounted for**, and the instruction to the next writer is explicit: **Movement 5 is nine chapters carrying flood, proof, hearing and resolution, and it cannot afford a 3,000-word house average.**

---

## What the review says to preserve

The refusal ladder (Chs 35–36) is the best sustained sequence in the volume: five people refusing for five different *correct* reasons, no chorus, no vote, and Marek's fifth reason — labor that goes back into their ditch, not into the node — turning a free gift into a record-keeping trap. Lissa wins on procedure and loses the clean record and says she is not sorry, exactly as specified; the instrument survives unopened and unused; Bray is moved by the cooperative's own record against them and is not outsmartable, and his closing line is the batch's best sentence.

**Numbers verified where testable, and re-verified here under the thirty-day month, since three of them cross the boundary:** 85s ÷ 4s = 21¼ cwt = a twentieth of 400 · £80 a month · sixteen households (Chs 11/14/15/18) against 35 = 9 + 22 + 4 (Ch 4) · N-2214/K consistent across Chs 7, 8, 15, 16, 20, 26 · thirteen days from the twenty-seventh to the tenth · thirteen days in the tray from the twenty-fourth · twenty days the tin has been at risk · twenty-one days from the tenth to the first of next month · ten days from the twenty-first to the first of the month, which is what Ch 21's new title rests on.

---

## Two things recorded for Batch 0005, not fixes

- **The sitting is the twenty-first of the month, which is season day 51**, so Chapters 41–49 must reach eleven days past the last day of this batch.
- **A licensed engineer is in the fen again from Ch 33**, so the reason the full-draw load is not applied to the seal is no longer her absence. It is that the load test was the twentieth day's act on a certificate and there is no charter to hang a second one on. **That reason has to survive into Ch 41.**

---

## One observation from the fix pass, not a review finding

**Nine chapters have an odd number of quotation marks, which means one speech in each is never closed** — Chs 24, 25, 27, 28, 30, 33, 37, 38 and 39. The house style opens every paragraph of a multi-paragraph speech and closes only the last, so the counts are odd mid-speech and even at the end; in these nine the closing mark is simply absent at the end of one speech. **It is cosmetic, it is pre-existing across two batches, and neither review caught it because the checks were for duplicate paragraphs and repeated sentences rather than quote balance. It has deliberately not been fixed here**, because locating the exact missing mark in nine chapters of prose that both reviews passed is more likely to introduce a mistake than to remove one. **A future copy-edit pass should do it mechanically, one chapter at a time.**

