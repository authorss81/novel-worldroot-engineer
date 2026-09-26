# Volume 02, Batch 0005 — Chapters 89–98 — review findings

**Scope.** `workspace/volume-02/batch-0005/chapter-0089.md` through `chapter-0098.md`, ten chapters, the last prose batch of Volume 02, together with the state updates made with them, the Batch 0005 prompt, and `workspace/volume-02/volume-close/PROMPT.md`.

**Provenance, stated plainly.** The review phase's standing failure to load the `novel-reviewer` subagent meant the automated pass did not produce this file; the attempt and its fallback are in `logs/batch-0005.review.log`, and that log's closing section carries the eight findings this file records and applies. **This is the written record of that pass plus the verification of its claims. Every finding below has been applied in place, without restarting the batch and without changing the planned plot.** The full record of what changed is in `state/continuity.md` under *The Batch 0005 review pass — Volume 02, Chapters 89–98, and what it changed*.

**Ten chapters is correct.** `outline/volume-02.md` ends Volume 02 at Chapter 98 and the batch prompt says *ten chapters*. The batch closes with `workspace/volume-02/volume-close/PROMPT.md`, which the dispatcher picks up correctly.

---

## Blocking

**1. Ch 98 dated an answer five days before the question.** `chapter-0098.md:59`: *"on the fourteenth of last month this holding told a district office in writing… and the answer came on the ninth of last month."* Day 104 is the fourteenth of last month; day 99 is the ninth of last month. **The district answers the fen before the fen writes.** This is the volume's closing speech, the paragraph the whole book builds to, and the verification pass had rewritten it.

*Fixed.* The answer is **the ninth of this month** (day 129), twenty-five days after the letter of day 104. The fen's letter, the answer and the rate now stand in that order in the sentence, which is the order they happened.

**2. Root cause: day 129 was relabelled "the ninth of last month."** The month begins on day 121, so **day 129 is the ninth of *this* month** and day 99 is the ninth of last month. The governing rule in `state/continuity.md` says exactly that — *"inside a scene on days 121–149, days 121–150 are this month"* — and four chapters then applied the opposite band:

| Ch | Line | Text | Event dated |
|---|---|---|---|
| 91 | 23 | "since the ninth of last month as a local holder" | the four points, day 129 |
| 94 | 27 | "I have wanted to be an operator since the ninth of last month" | as above |
| 96 | 21 | "I have been trying since the ninth of last month" | as above |
| 98 | 59 | "the answer came on the ninth of last month" | as above |

Three chapters already said *this month* for the same event and were right: Ch 89:13, Ch 90:27 and Ch 93:61.

The source is the batch prompt, which is internally contradictory: `batch-0005/PROMPT.md`'s day clock and its weekday paragraph both place day 129 in the month beginning day 121, and its **day table alone** says *the ninth of last month (129)*, in a row whose interval of twenty days is correct and whose band is not. The pass recorded the prompt's error as the fix instead of catching it.

*Fixed.* **All four lines now say the ninth of this month.** The prompt is annotated at its head with the mislabel, its two contradictory readings, the four chapters it cost, and an instruction that a Volume 03 writer must not carry it — and the day table's band column is named as the one place in that prompt that is wrong while its intervals stand.

**3. The wrong band was recorded as canon in three state locations and would have propagated.** Two entries in the verification table in `state/continuity.md`, the ledger line that said *the district's four points are day 129, the ninth of last month*, and the same claim in `state/current.md` and `state/chapter-summaries.md`. The volume close and Volume 03 would have inherited it as settled fact.

*Fixed in all of them.* The two stale table rows are **struck rather than deleted**, so the record of what the first pass did remains visible, and each carries the correction and the reason.

**4. Ch 98 contradicted itself inside one paragraph, and contradicted Ch 89.** *"The answer was a class of use, and it came on the tenth of this month with a rate on it."* The sentence before it dated the answer to the ninth; Ch 89:13 has the schedule sent under the third point of the letter of the ninth, and the four sheets arrive on the district's cart on the tenth; Ch 90:27 says *"Since the ninth it is a class of use in a district's book."* The sentence assigned the class to the tenth.

*Fixed.* **The two events are split:** *"The answer was a class of use, and the rate on it came on the tenth."*

**5. Ch 98: "a printer in Fennmere who has set four hundred pages of our book."** The book is **two hundred pages** in Chs 60 (×2), 61, 73, 74 (×2), 76 (×2), 77, 80 and 82. **No second printing of the book appears anywhere in the prose** — "second printing" exists only in a continuity summary line. The four hundred copies belong to the Ashcombe table at Auberron; a hundred and forty is the map's run, and the pass had already fixed that half correctly against Ch 56 in the same paragraph.

*Fixed to two hundred pages.*

---

## Non-blocking

**6. The October offset — the review asked for the wrong file to be changed, and the change was not made.** Three files disagreed: the volume-close prompt said **four months back** by day 130; the batch prompt and `state/continuity.md` both said **five**.

**Four is correct.** Months run thirty days and **day 1 is the first of October** — the flock went up the fen road on the tenth of October, which is season day 10, and days 21–30 are the twenty-first to the thirtieth of October. So days 1–30 are October, 31–60 one month on, 61–90 two, 91–120 three, and 121–150 four; **day 130 sits in the fifth month and October is the first.** This file's own list of prompt mislabels had already worked it out for day 4, and Ch 89's *the fourth of a month four months back* was right all along.

*Fixed, in the other direction from the one proposed.* **The volume-close prompt is left at four and annotated with the reason and with a warning not to revert it.** The batch prompt and `state/continuity.md` are corrected from five to four, each carrying the month arithmetic inline.

**7. Six British spelling tokens in Volume 02, against a bible that forbids them.** `bible/terminology.md` — *"US spelling… do not reintroduce British forms into the prose"* — decided at the Volume 01 close and applied as a single pass over Chs 1–49, which the review verified clean across 166,022 words. Volume 02 had: *favour* ×4 (Ch 57:109; Ch 86:17 twice; Ch 86:43), *defence* (Ch 92:31), *travelled* (Ch 87:87).

*Fixed.* All six are US. **A wider sweep for thirty further British forms across all forty-nine chapters returns nothing.** The volume-close prompt's *"decide once, single pass or leave"* instruction reopened a settled question, so it now **names the six sites, states that both volumes are clean, and tells the close phase to decide nothing** and to limit itself to the straight-mark check.

**8. Continuity's "checked and found sound" list risked being read as a clearance the batch had not earned.** It claims *"straight quotation marks throughout and every multi-paragraph speech opening a mark in each paragraph and closing in the last"* — true and verified, including the volume's final speech. But **the em dash at `chapter-0092.md:27` is the only one in the batch against fifty-five chapters that use it across both volumes**, so it is this manuscript's idiom and not an intruder, and a close pass could reasonably have flagged it.

*Fixed by recording, not by editing.* The continuity line now says so explicitly: **do not flag it, and do not strip dashes across the volume on the strength of a single instance.** The one em dash in the batch is left where it is.

**9. The recorded word counts were wrong, including one the review repeated.** The batch is **28,783** words by `wc -w` over the chapter files including their headings, **range 2,620–3,103**, and Volume 02 is **141,818 — 31,337 + 25,388 + 23,108 + 33,202 + 28,783**. The figures carried in five files were 28,788 and 2,619–3,108; **the low end was wrong by one before this pass as well**, and Ch 98's margin under the ceiling is **seventeen** words, not twelve.

*Fixed.* **Every figure has been recomputed from the chapter files rather than adjusted by the number of words this pass removed**, and all five files now carry the same numbers.

---

## Checked and *not* defects, to save the next phase time

**The repeated long sentence is correct.** *"In this class the condition is that the operator keeps the declared capacity in the ordinary course"* appears in Chs 89 and 91 and is quoted language from the district's own schedule of terms; a document may be quoted twice. **Zero duplicate paragraphs** across the batch. No curly marks anywhere. The multi-paragraph speech convention is intact, including the volume's final five-paragraph speech, whose paragraphs each open a mark and the last of which closes. **No month is named in narration or in any document** — all six instances of *March* are the fen, the March road or the March's line. The *eleven months* (the season) against *eleven years* (a tenure) repair holds across all nine occurrences. **Tin at 130 and bay boards at 83 on day 149** are right on *day minus nineteen* and *day minus sixty-six*. The levy-on-sixteen-houses repair is right and the forty households of Ch 80 are a hundredweight of compost. **The arithmetic repairs in Chs 92, 93, 94, 95 and 97 all check out against the day bands.** The word counts for Volume 01 (166,022) and for Batches 0001–0004 (31,337 / 25,388 / 23,108 / 33,202) are exact and were not touched.

## Unchanged on purpose

**The one recorded deviation stands: the dry-end refusal is spoken on day 142 and reaches the fen on day 143.** It must not be silently re-dated in either direction. **The ending is untouched and no final enemy has been added.** Nothing in this pass changed a plot beat, a Movement 5 date, a locked number other than the printer's page count, a name, or a relationship.
