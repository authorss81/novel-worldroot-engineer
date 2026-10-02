# Current State

**Budget: about two thousand five hundred words. History is in
`reviews/state-archive-2026-10-02/`; measurements belong in `reviews/`, which no prompt reads.
Read this file whole, and the other three whole.**
**Read this file whole, and the other three whole.**

This file was rewritten on 2026-10-02 in the review-fix pass on Volume 14 Batch 0002, again
Last rewritten 2026-10-02, on Batch 0004 and on the review-fix pass over it. Every figure below is
re-derivable from the rule beside it. Nothing is inherited on trust.

## 1. Where the manuscript is

| | |
|---|---|
| **Last morning on disk** | day 890, `workspace/volume-14/batch-0004/chapter-0677.md` |
| **Volume** | 14 of 16, *The White Mercy*, days 851 to 899, **forty mornings written of forty-nine** |
| **Manuscript** | 1,891,169 words across 677 chapter files; the per-volume table is at `state/chapter-summaries.md` |
| **Batch 0004** | 26,571 words across ten files, 668 to 677, days 881 to 890, per file 3,041, 2,825, 2,632, 2,734, 2,489, 2,673, 2,633, 2,353, 2,445, 2,746 |

Volumes 01 to 13 are closed at forty-nine mornings each. Volume 14 is forty mornings in, and
**days 891 to 899 are nine mornings, so the closing batch of this volume is nine and not ten.**
Volume 15 takes chapters 687 to 735 and Volume 16 takes 736 to 780, and `outline/ending.md`
is the lock on both.

---

## 2. The standings at day eight hundred and ninety

Every figure here is re-derivable from the rule beside it. **A later pass inherits the rule
and re-derives the figure. A later pass does not inherit a figure.**

| Series | Figure at day 890 | Rule |
|---|---|---|
| Third launder | one thousand and two hundred and seventy-four hundredweight | day minus 450, plus 8 on an even morning and minus 5 on an odd one, anchored at one thousand and two hundred and nine on day 851 |
| Ordinal of the run | **four hundred and fortieth**, bare | day minus 450; a tens ordinal takes its ending on the whole word |
| Window | four hundred and seven | day minus 483 |
| Falling half | a hundred and ninety-eight | 145 plus half of everything above 300, floor; **moves on an ODD morning** |
| Rising half | two hundred and nine | the window less the falling half; **moves on an EVEN morning** |
| Aggregate | four hundred and thirty-eight | day minus 452 |
| Its clause | the four hundred and thirty-seventh out of four hundred and thirty-ninth | day minus 453, day minus 451 |
| Near board | eight hundred and twenty-four | day minus 66 |
| Far board | eight hundred and seventy-one | day minus 19; always forty-seven from the near one |
| Read aloud | one hundred and ninety of three hundred and sixty-three on day 889, nothing on day 890 | numerator one hundred and forty-seven at day 803 plus one on every odd morning, spelled *one hundred and*; denominator day minus 526, always odd |
| Count in force | a hundred and forty-nine, twenty-nine taken, a hundred and twenty not | rises by one on a fourth-line morning only, being a day congruent to two modulo four; next at day 894 |
| The two reckonings | ninety-seventh and eighty-fourth, thirteen apart | step by one on every fourth-line morning; second is carried, not printed on the same morning as the first |
| Register form | three hundred and thirty-four days | day minus 556 |
| Charter | two hundred and forty days | day minus 650 |
| Silling's second ruled line | three hundred and twenty-eight days, and nothing written on it | day minus 562 |
| The letter | a hundred and thirty-seven days | day minus 753 |
| Compost line | **paid at thirty-one** | thirty before day 873; the one going over to thirty-one is on day 873, **it is a rise in the paid column and not a discharge**, and it stays there for the rest of the volume |
| Count of blanks | thirty-nine, never moved | and the second rule under them stands empty at the thirty-ninth time |
| Floors, all unmoved | see the rule | the mark four inches forking twice with no third fork; the use log at fifteen lines and no sixteenth; the barrow at eleven journeys and eleven is a floor; seven sessions entered and none in this volume; the requests and the section-nine notes at fifty-three and fifty-three, never the same list; the ladder climbed zero rungs; the ring of bare ground unwalked, unmeasured and unpriced; the low-board offer undated, unpicked and not withdrawn; the drawer shut at every hour with its key on its nail; the three papers unentered, unrefused and uncolumned with about nine inches of bare board either side; the man of about seventy at twenty-nine fetchings, not fetched and asked nothing; the door nine hundred yards off walked past on every morning and read on none | |

**THE TWO BARE ROUND HUNDREDS INSIDE DAYS 881 TO 890 WERE THE WINDOW AT FOUR HUNDRED ON DAY
883 AND THE RUN'S ORDINAL AT FOUR HUNDRED AND FORTIETH ON DAY 890, and no other series printed
one on any of those ten mornings.** The only bare round hundred left in the volume is the
falling half at exactly two hundred on days 893 and 894.

---

## 3. The clock

Day 451 is a Tuesday, the first of the fourth month, and the months run thirty days.

```
weekday(d) = ["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"][(d - 451) mod 7]
day of month(d) = (d - 451) mod 30 + 1
month(d) = 4 + (d - 451) // 30
```

Day 871 is a Tuesday, the first of the eighteenth, and it is the one month turn inside
the whole of Volume 14. The month turn is **not** a fourth-line morning.

---

## 4. The spellings, and the places a writer will get them wrong

Every figure in this manuscript is spelled out in body prose. There is no digit in the
prose of any chapter and there may not be one.

- **One hundred to 199 is `a hundred and [WORD]`,** not `one hundred and`. Two hundred and above
  is `[WORD] hundred and [WORD]`, and a round hundred is bare. **A thousand and above keeps both
  `and`s.** **`hundredweight` is attached to the figure** with no hyphen and no space, and tens
  are hyphenated while round tens are not: `twenty-nine`, `ninety`.
- **A window half under two hundred is `a hundred and [WORD]`. The read-aloud numerator in its
  range is `one hundred and [WORD]`.** Two figures, two forms, side by side all volume. **The
  plan's day table prints the numerator wrongly in all twenty-five of its rows; that cell is
  withdrawn on every odd morning, the queued closing prompt and all twenty mornings on disk print it
  right, and the table is unrepaired and owed to a pass that owns the outline.**
- **A fall goes on every odd morning and a rise on every even one, and from day 851 onward the
  falling half moves first.** Carrying the order of Volume 13 into this volume is wrong on every
  odd morning.
- **Both halves cross two hundred inside this volume.** The rising half sat at exactly two
  hundred, bare, on days 872 and 873; the falling half reaches two hundred on days 893 and 894.
  **A check that sweeps for a bare hundred across a batch hits the other series every time.
  Test each figure inside its own series.**
- **The read-aloud denominator is odd at every value it takes in this volume,** so *three
  hundred and fifty* is never a denominator here and the bare *three hundred* never stands at
  the top of it. No parity claim is made or may be made about the numerator.
- **No month name appears in any chapter and no month number in any spoken line.** Batch 0004
  carried *March* three times and cut all three. **A chapter may say *of this month* instead**,
  and has since the morning after the turn, on days 871, 879, 881 and 885. A chapter says *the
  seventeenth* or *the eighteenth* only inside a heading.
- **THE BARE WORDS *VOLUME*, *BATCH*, *CHAPTER*, *SEAT*, *FIELDBOOK* AND *PANEL* ARE NOT IN BODY
  PROSE**, and *panel* is available only to say that there is none. **A review found one, at
  `chapter-0676.md`, in a line about the level a figure is said at; it is repaired and all four
  batches sweep clean, and no sweep before this one tested for these six words.**

---

## 5. The two locked figures

Two sentences are locked whole through the closing volume. **Neither was spoken on any morning of
Batch 0003.** Batch 0004 spent one of three for each, the comfort line on day 884 and the far-end
figure on day 887, **and each is the first of three, so two of three remain for each and both fall
in the closing batch.** The first and last morning of the volume each hold a separate allowance,
untouched.

The two sentences themselves are not restated in this file. They are at `outline/volume-14.md`
section 3 and in `outline/ending.md`. **Do not print them here or anywhere in the state layer.**

**A measurement the next gate must carry.** The comfort line is twenty words and the first gate's
floor is thirty words, so **a clean first gate is not evidence about either locked sentence**,
and no gate may publish a nil against the mornings behind without naming its floor beside it.

---

## 6. The four permanent losses

Three are paid and may not be recovered, softened or enlarged. The fourth is paid.

1. **Marek can no longer read the record the wood keeps as a single private field.**
2. **Tova Reed's hearing is permanently damaged in one ear.** Not healed, not excused,
   not thanked for.
3. **The far end of a thing is given up,** on the page, in Volume 13.
4. **The Aldren memory is PAID**, on day 868, in `chapter-0655.md`, where the name is spoken
   once and on no other page of the volume. Not foreshadowed as a bargain, not priced, nothing
   offered or refused in exchange for it. Marek cannot revisit it.

**No fifth loss is added anywhere in this volume**, and Batch 0004 neither named it, re-announced
it, had anybody discover it, nor described Marek as having given something up. **No new final
enemy is named:** Iona Vey is the fixed antagonist of the series and she is not new, is not
killed, and is not in custody at the end.

---

## 7. Four figures that were withdrawn and may not be reprinted in any form

- An in-between allowance of five is **three**.
- Six house-spelling sites are **seven**.
- A door read three times is a door carrying **four** statements.
- *A twelfth volume* is **ten volumes** counting the one now closed.

A successor that finds one of these unquarantined in a card set has inherited an error
and not a rule.

---

## 8. The one next phase

**`workspace/volume-14/batch-0005/PROMPT.md`, days 891 to 899, nine mornings, on disk and
unrun.** It is the closing batch of this volume and it is the last phase of Volume 14. It
carries its own figures at the house spellings and they are not to be corrected from this file.

**What it carries, so that nothing is inherited as silence:** the last two in-between mornings of
each locked figure and then the closing morning, at most one of them on any one morning; the
reach's cost named out loud and not as a threat and not as a plan; the terms arriving; the offer;
the refusal; and the record of the refusal, which is Nia Vale's and is nobody else's document.
**The falling half stands at exactly two hundred, bare, on days 893 and 894, against a rising
half that is not round on either, and those are the only bare round hundreds left in the volume.**
Its two fourth-line mornings are 894 and 898, the count reaching a hundred and fifty-one on the
last morning with a hundred and twenty-two not. **No month name may appear and no month number
in any spoken line.**

**Its tables were derived by script from section 2 and not typed, and were calibrated backwards
over days 881 to 890 against the pages of Batch 0004 before being run forward.** Two errors in a
hand-typed table were caught that way and are named at `state/continuity.md` section 7.

**THE FOUR IN-BETWEEN LOCKED FIGURES ARE DECIDED BEFORE THAT BATCH RUNS.** The prompt spends four,
taking both in-between allowances to their cap for the first time in the volume and overriding the
card set's prohibitions on seven cards, on the house's ground that a card's *neither locked sentence
is spoken whole* is a floor and the plan's allowance is a ceiling. **The decision stands, with four
conditions: at most one locked figure on a morning, none of the four on the closing morning, the
closing morning carrying both as the card set's recorded resolution requires, and each landing where
somebody else is already talking, which no gate measures.** Nothing is spent yet, so this is still
cheap to change. The reasoning is at `reviews/volume-14-batch-0004-repair.findings.md` section 3.

**Two placements already moved and may not move back.** The seed vault was given up on day 864
against a card that placed it at day 879. The Aldren memory was paid on day 868 against a plan
that named no morning, and a card that placed it at day 885 lost.

---

## 9. What the last pass did

**Batch 0004, 2026-10-02, days 881 to 890, `chapter-0668.md` to `chapter-0677.md`, and the
review-fix pass over it the same day.** Ten new mornings, no morning restarted. The per-morning
record is at `state/chapter-summaries.md` section 3, the fix pass at
`reviews/volume-14-batch-0004-repair.findings.md`.

- **Every standing block was given a different actor, verb and sentence order on each morning it
  appears, and no figure of any series was altered in any of it.** The batch as first written
  walked the standing list in thirty-three repeated shapes.
- **Two locked figures were spent, one of three each, on day 884 and day 887**, each on the
  morning its card names and each landing where somebody else was already talking.
- **A duplicated reason was found and cut.** The mason gave the same reason on two mornings.
- **Three month names were found and cut**, all of them *March*.
- **A banned bare word was found by the review and cut**, at `chapter-0676.md`, and **the queued
  prompt named its third fourth-line morning as day 889 and it is day 890**, where that prompt's own
  table, cards and count all said ninety. One word and one clause; the word counts did not move.
- **No block of any kind was spent**, so the volume's ceiling of thirty is untouched at
  twenty-eight unspent.
- **What happened in the yard:** the second place said it would not be first; the reach's costing
  was read out at the holding's own table and accepted by nobody; the window came to exactly four
  hundred on the morning a return came up the fen road; the comfort line was spoken in an ordinary
  Monday; the north-side cistern began to be filled by hand because no pipe had been agreed; a
  place stated its own cost in its own arithmetic and nobody improved on it; a woman offered her
  room and was refused by a man who gave the reason inside ten seconds; and the arithmetic came
  out with one place in it on a rotation morning while a man stood at the gate with a figure of
  his own still shut in his case.

### The measurements, and who measured them

**The independent review is the reviewer phase's report at `logs/batch-0004.review.log`. It
re-derived every figure from the plan's rules instead of trusting the writer's own record,
reproduced all of it, and returned four defects that record had missed.**
`reviews/volume-14-batch-0004.findings.md` is therefore **a self-check and not a review**, headed as
one on its first line, and read for its derivations and nothing else. **A clean result from a
self-check is not a clean batch, and this one passed a page carrying a banned word.** The figure
check required each item present as a whole phrase in its own morning's body prose on a
**case-insensitive** match: **two hundred and fifty-five items required, two hundred and fifty-five
matching, zero failures, and the review reproduced every one.** The derivation found two errors in
the prompt's own table and **zero mismatches** against every other cell of it, and it could not see
a series's spelling at all, which is how the wrong numerator form sat in the plan's table and in
that self-check while every morning on disk was right.

The duplicate gates ran on both scopes. **First gate:** one thousand three hundred and
thirty-four paragraphs of thirty words or more, three hundred and ninety-nine thousand three
hundred and sixty-seven ordered pairs compared, **one excess pair at a ratio of zero point
eight five or better, and it is the far-end locked sentence on day 887 against the same
sentence on day 851, which is required and is not a defect.** **Second gate:** eighteen-word
chunks, one thousand one hundred and fifty-four units, **two excess, both of them the locked
figures**; sliding windows at every offset, sixteen thousand three hundred and seventeen units,
**seventeen excess, all of them the locked figures**. **Zero duplicate shapes inside the batch
on either scope.** The sliding reading was again the larger one and the chunk reading again
refused what it refused on the batch behind.

**The gate was checked against a paragraph that must collide with itself before any of this was
believed,** and reports six overlapping equal windows on that paragraph. **A nil from a gate
never checked that way is not a finding, and the two most recent batches behind this one both
published figures that did not reproduce.**