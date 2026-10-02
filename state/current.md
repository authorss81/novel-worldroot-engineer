# Current State

**Budget: about two thousand five hundred words. A phase that needs more than this is
looking for history, and history is in `reviews/state-archive-2026-10-02/`, which holds
the four state files exactly as they stood before 2026-10-02 at roughly nine times a
single context window. Measurements belong in `reviews/`, which no prompt reads.**

**Read this file whole, and the other three whole.**

This file was rewritten on 2026-10-02, in the review-fix pass on Volume 14 Batch 0002, and
again the same day by the writing pass on Volume 14 Batch 0003. Everything below is carried
forward, and every figure is re-derived from the rule beside it. Nothing is inherited on
trust.

---

## 1. Where the manuscript is

| | |
|---|---|
| **Last morning on disk** | day 880, `workspace/volume-14/batch-0003/chapter-0667.md` |
| **Volume** | 14 of 16, *The White Mercy*, days 851 to 899, **thirty mornings written of forty-nine** |
| **Manuscript** | 1,864,598 words across 667 chapter files |
| **Per volume** | 01 166,022, 02 141,818, 03 142,952, 04 141,727, 05 144,846, 06 146,883, 07 140,227, 08 139,423, 09 141,658, 10 141,223, 11 143,305, 12 118,058, 13 91,321, 14 65,135 |
| **Batch 0003** | 27,313 words across ten files, 658 to 667, days 871 to 880 |
| **Batch 0003 per file** | 2,356, 2,271, 2,596, 2,624, 3,012, 2,587, 2,545, 3,084, 3,264, 2,974 |

Volumes 01 to 13 are closed at forty-nine mornings each. Volume 14 is thirty mornings
in. Volume 15 takes chapters 687 to 735 and Volume 16 takes 736 to 780, and
`outline/ending.md` is the lock on both.

---

## 2. The standings at day eight hundred and eighty

Every figure here is re-derivable from the rule beside it. **A later pass inherits the
rule and re-derives the figure. A later pass does not inherit a figure.**

| Series | Figure at day 880 | Rule |
|---|---|---|
| Third launder | one thousand and two hundred and fifty-nine hundredweight | day minus 450, plus 8 on an even morning and minus 5 on an odd one, anchored at one thousand and two hundred and nine on day 851 |
| Ordinal of the run | four hundred and thirtieth | day minus 450 |
| Window | three hundred and ninety-seven | day minus 483 |
| Falling half | a hundred and ninety-three | 145 plus half of everything above 300, floor; **moves on an ODD morning** |
| Rising half | two hundred and four | the window less the falling half; **moves on an EVEN morning** |
| Aggregate | four hundred and twenty-eight | day minus 452 |
| Its clause | the four hundred and twenty-seventh out of four hundred and twenty-ninth | day minus 453, day minus 451 |
| Near board | eight hundred and fourteen | day minus 66 |
| Far board | eight hundred and sixty-one | day minus 19; always forty-seven from the near one |
| Read aloud | one hundred and eighty-five of three hundred and fifty-three on day 879, nothing on day 880 | numerator one hundred and forty-seven at day 803 plus one on every odd morning; denominator day minus 526 |
| Count in force | a hundred and forty-six, twenty-nine taken, a hundred and seventeen not | rises by one on a fourth-line morning only, being a day congruent to two modulo four; next at day 882 |
| The two reckonings | ninety-fourth and eighty-first, thirteen apart | step by one on every fourth-line morning; second is carried, not printed |
| Register form | three hundred and twenty-four days | day minus 556 |
| Charter | two hundred and thirty days | day minus 650 |
| Silling's second ruled line | three hundred and eighteen days, and nothing written on it | day minus 562 |
| The letter | a hundred and twenty-seven days | day minus 753 |
| Compost line | **paid at thirty-one** | thirty before day 873; the one fall to thirty-one is on day 873 and it stays there for the rest of the volume |
| Count of blanks | thirty-nine, never moved | and the second rule under them stands empty at the thirty-ninth time |
| Sessions | seven, entered on none of the thirty mornings | |
| Requests, section-nine notes | fifty-three and fifty-three | never added, never the same list |
| Use log | fifteen lines | |
| Barrow | eleven journeys, and eleven is a floor | |
| The mark | four inches, forking twice, no third fork | |
| Ladder | climbed zero rungs | |
| Ring of bare ground | not walked, not measured, not priced | |
| Offer on the low board | undated, unpicked, not withdrawn | |
| Drawer behind the near board | shut at every hour, key on its nail at every hour | |
| Three papers on the long table | unentered, unrefused, uncolumned; the first a hundred and twenty-seven days old, about nine inches of bare board either side | |
| Man of about seventy | twenty-nine fetchings, not fetched in this volume, asked nothing at any site | |
| Door nine hundred yards off | walked past on every morning and read on none | |

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

- **One hundred to 199 is `a hundred and [WORD]`,** not `one hundred and`. Two hundred and
  above is `[WORD] hundred and [WORD]`. A round hundred is bare: `two hundred`,
  `eight hundred`, `three hundred`, `a hundred`.
- **A thousand and above keeps both `and`s**: `one thousand and two hundred and forty-four
  hundredweight`.
- **`hundredweight` is attached to the figure** with no hyphen and no space. Tens are
  hyphenated and round tens are not: `twenty-nine`, `ninety`. The hyphen is the house form
  and is not a dash.
- **A window half under two hundred is `a hundred and [WORD]`. The read-aloud numerator in
  its range is `one hundred and [WORD]`.** Two figures, two forms, side by side all volume.
  The plan's day table prints the numerator in the window half's form; that cell is
  **withdrawn on every odd morning of the volume**.
- **A fall goes on every odd morning and a rise on every even one, and from day 851 onward
  the falling half moves first.** Carrying the order of Volume 13 into Volume 14 is wrong on
  every odd morning.
- **Both halves cross two hundred inside this volume.** The rising half sat at exactly two
  hundred, bare, on days 872 and 873, two consecutive mornings, and has been above it since.
  The falling half reaches two hundred near the end. In each pair the round side is the side
  a writer drops the `and` from.
- **The window reaches exactly four hundred, bare, on day 883, and the run's ordinal the bare
  *four hundred and fortieth* on day 890.** The bare three hundred in the register form is on
  day 856 and does not recur. **A check that sweeps for a bare hundred across a batch hits
  the other series every time. Test each figure inside its own series.**
- **The read-aloud denominator is odd at every value it takes in this volume,** so *three
  hundred and fifty* is never a denominator here. No parity claim is made or may be made
  about the numerator.
- **No month name appears in any chapter and no month number in any spoken line.** The
  read-aloud frame is *of a month nine months back* and does not move, including on the
  month turn. A chapter says *the seventeenth* or *the eighteenth* only inside a heading.

---

## 5. The two locked figures

Two sentences are locked whole through the closing volume. Neither has been spent. The
in-between allowance is three shortenings each and neither has been used; the first and
last morning of the volume each hold a separate allowance, untouched.

The two sentences themselves are not restated in this file. They are in
`outline/volume-14.md` at section 3 and in `outline/ending.md`. **Do not print them
here, and do not print them anywhere in the state layer**, because a state file that
carries them whole is a file every prompt pays for them in.

---

## 6. The four permanent losses

Three are paid and may not be recovered, softened or enlarged. The fourth is paid.

1. **Marek can no longer read the record the wood keeps as a single private field.**
2. **Tova Reed's hearing is permanently damaged in one ear.** Not healed, not excused,
 not thanked for.
3. **The far end of a thing is given up,** on the page, in Volume 13.
4. **The Aldren memory is PAID**, on day 868, in `chapter-0655.md`. The name is spoken
 once on that page and on no other page of the batch. It was not foreshadowed as a
 bargain, not priced, and nobody offered or refused anything in exchange for it. After
 that morning Marek cannot revisit it.

**No fifth loss is added anywhere in this volume.** No new final enemy is named:
Iona Vey is the fixed antagonist of the series and she is not new, is not killed, and
is not in custody at the end.

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

`workspace/volume-14/batch-0004/`, days 881 to 890, ten mornings, one `PROMPT.md` on disk
and unrun. It opens on the standings at day 880 in section 2 above, on the Friday after the
month turn, and may say *of this month* in place of the frame from its first morning. It
carries the compost line at paid at thirty-one throughout, the window at exactly four
hundred bare on day 883, a return on day 883, the bare *four hundred and fortieth* ordinal
on day 890, and three fourth-line mornings, being days 882, 886 and 890.

**One claim this file carried was wrong and is corrected here. The bare three hundred in the
register form falls on day 856, in Batch 0001, and does not recur; on day 886 the register
form is three hundred and thirty, and no bare three hundred appears anywhere in days 881 to
890.** A writer handed the withdrawn day would have gone looking for a figure that is on
none of those ten mornings and could have written one. So is the bare four hundred at the
top of the read-aloud denominator, which falls on no morning of this volume.

**Two placements already moved and may not move back.** The seed vault was given up on day
864 against a card that placed it at day 879, and the page governs. The Aldren memory was
paid on day 868, on an even morning, against a plan that named no morning.

---

## 9. What the last pass did

**Batch 0003, 2026-10-02, days 871 to 880, `chapter-0658.md` to `chapter-0667.md`.** A
checkpoint existed when the pass resumed and the first eight mornings were already on disk.
**No completed morning was restarted and no completed morning's scene was removed.**
Mornings 871 to 878 stand as the earlier pass wrote them, apart from four repairs. Mornings
879 and 880 are new.

- **Wrote `chapter-0666.md` and `chapter-0667.md`**, on cards nine and ten, and put a person
  inside every standing block in both, in that person's own order, so the figures arrive
  inside what the person is doing. The woman of about thirty-eight of Marden gives the
  compost line and the two fifty-three books at dusk, Hesta Lyle gives the aggregate with the
  small hand first, Marek reads the launder off the wall, Kellan Rusk gives the count in
  force and the drawer, Sera Quill gives the three ages off her own slate, Nia Vale gives the
  boards and the door, the man of about fifty gives the three papers, Soren Rill gives the
  ladder and the ring, the mason gives the tap joint. No figure of any series changed.
- **Four repairs, by file and by fact.** `chapter-0660.md`: one unbalanced bold marker.
  `chapter-0661.md`: an apparatus paragraph carrying word for word a clause a closed morning
  carried. `chapter-0665.md`: two speech paragraphs of one speaker back to back with no
  action between them. `chapter-0666.md`: the aggregate and its clause arrived in Hesta
  Lyle's mouth on day 879 in nearly the words and the order they arrived in on day 876, at a
  ratio of zero point eight six five. `chapter-0667.md`: three standing blocks came back in
  a shape an earlier morning already carried, being the count in force against day 878, the
  blanks and the second rule against day 872, and the two fifty-three books against a closed
  morning. **No figure of any series was altered by any repair.**
- **Three figures were published wrongly and the pages overrode all three**, named at the
  foot of `state/continuity.md`: the compost line, the read-aloud numerator, the day of the
  seed vault.
- **The figures were re-derived by script from the rules in section 2, not read off the
  prompt's table**, then checked field by field against the prompt's table and the plan's.
  Every field agrees. **Run forward over days 881 to 890 and checked against the plan's rows
  for those mornings: one hundred and forty-six fields, zero mismatches, five plan cells
  withdrawn for printing the numerator in the window half's form.** That check found the
  wrong claim in section 8.

### The measurements, with the method beside them

Method, item list and the gate bugs are at `reviews/volume-14-batch-0003.findings.md`.

- **Figure check**, each item required present as a whole phrase in its own morning's body
  prose on a **case-insensitive** match, because a figure at the start of a sentence is
  capitalised: **one hundred and seventy items, one hundred and sixty-four matching exactly,
  six carrying the figure in another word order or in the sentence-initial position, all six
  read and confirmed, zero failures.** A check demanding one fixed phrase reports six
  failures on a clean batch.
- **Duplicate gates, both scopes.** First gate: **one hundred and fourteen thousand six
  hundred and thirty-eight ordered pairs on nine hundred and forty-one paragraphs of thirty
  words or more, zero at a ratio of zero point eight five or better.** Second gate:
  **eighteen-word chunks, one thousand two hundred and twenty-five units, zero excess;
  sliding windows at every offset, seventeen thousand six hundred and fifty-seven units, zero
  excess against the closed mornings and zero duplicate shapes inside the batch.** The
  sliding reading found four defects the chunk reading refused.
- **The previous pass's measurements did not reproduce and are withdrawn.** Its first gate
  read a nil at a different pair count; its second read twenty-seven excess where the fixed
  implementation reads four defects **involving mornings of this batch**. The cause was a
  gate comparing a paragraph with itself and a chunk scope comparing fragments shorter than a
  full chunk. **A nil from a gate never checked against a paragraph that must collide with
  itself is not a finding.**
