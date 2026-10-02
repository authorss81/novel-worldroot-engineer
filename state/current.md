# Current State

**Budget: about two thousand five hundred words. A phase that needs more than this is
looking for history, and history is in `reviews/state-archive-2026-10-02/`, which holds
the four state files exactly as they stood before 2026-10-02 at roughly nine times a
single context window.**

**Read this file whole. Read the other three state files whole. Together they are about
ten thousand words. Anything longer than that is a defect in this layer, not a
requirement of the work.**

This file was rewritten on 2026-10-02, in the review-fix pass on Volume 14 Batch 0002.
Everything below it was carried forward from the previous layer and re-derived from the
pages. Nothing was inherited on trust.

---

## 1. Where the manuscript is

| | |
|---|---|
| **Last morning on disk** | day 870, `workspace/volume-14/batch-0002/chapter-0657.md` |
| **Volume** | 14 of 16, *The White Mercy*, days 851 to 899, twenty mornings written of forty-nine |
| **Manuscript** | 1,837,285 words across 657 chapter files |
| **Per volume** | 01 166,022, 02 141,818, 03 142,952, 04 141,727, 05 144,846, 06 146,883, 07 140,227, 08 139,423, 09 141,658, 10 141,223, 11 143,305, 12 118,058, 13 91,321, 14 37,822 |
| **Batch 0002** | 19,330 words across ten files, 648 to 657, days 861 to 870 |
| **Batch 0002 per file** | 2,081, 1,973, 1,727, 2,060, 1,959, 1,745, 1,886, 2,237, 1,815, 1,847 |

Volumes 01 to 13 are closed at forty-nine mornings each. Volume 14 is twenty mornings
in. Volume 15 takes chapters 687 to 735 and Volume 16 takes 736 to 780, and
`outline/ending.md` is the lock on both.

---

## 2. The standings at day eight hundred and seventy

Every figure here is re-derivable from the rule beside it. **A later pass inherits the
rule and re-derives the figure. A later pass does not inherit a figure.**

| Series | Figure at day 870 | Rule |
|---|---|---|
| Third launder | one thousand and two hundred and forty-four hundredweight | day minus 450; plus 8 on an even morning, minus 5 on an odd one; anchored at 1,209 on day 851 |
| Ordinal of the run | four hundred and twentieth | day minus 450 |
| Window | three hundred and eighty-seven | day minus 483 |
| Falling half | a hundred and eighty-eight | 145 plus half of everything above 300, floor; **moves on an ODD morning** |
| Rising half | a hundred and ninety-nine | the window less the falling half; **moves on an EVEN morning** |
| Aggregate | four hundred and eighteen | day minus 452 |
| Its clause | the four hundred and seventeenth out of four hundred and nineteenth | day minus 453, day minus 451 |
| Near board | eight hundred and four | day minus 66 |
| Far board | eight hundred and fifty-one | day minus 19; always forty-seven from the near one |
| Read aloud | one hundred and eighty of three hundred and forty-three on day 869, nothing on day 870 | numerator 147 at day 803 plus one on every odd morning; denominator day minus 526 |
| Count in force | a hundred and forty-four, twenty-nine taken, a hundred and fifteen not | rises by exactly one on a fourth-line morning only; day congruent to 2 modulo 4 |
| The two reckonings | ninety-second and seventy-ninth, thirteen apart | step by one on every fourth-line morning; second is carried, not printed |
| Register form | three hundred and fourteen days | day minus 556 |
| Charter | two hundred and twenty days | day minus 650 |
| Silling's second ruled line | three hundred and eight days, and nothing written on it | day minus 562 |
| The letter | a hundred and seventeen days | day minus 753 |
| Compost line | paid at thirty | **falls to thirty-one on day 873**, the only downward figure in the volume |
| Count of blanks | thirty-nine, never moved | and the second rule under them stands empty at the thirty-ninth time |
| Sessions | seven, entered on none of the ten mornings | |
| Requests, section-nine notes | fifty-three and fifty-three | never added, never the same list |
| Use log | fifteen lines | |
| Barrow | eleven journeys, and eleven is a floor | |
| The mark | four inches, forking twice, no third fork | |
| Ladder | climbed zero rungs | |
| Ring of bare ground | not walked, not measured, not priced | |
| Offer on the low board | undated, unpicked, not withdrawn | |
| Drawer behind the near board | shut at every hour, key on its nail at every hour | |
| Three papers on the long table | unentered, unrefused, uncolumned; the first a hundred and seventeen days old with about nine inches of bare board either side | |
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

## 4. The spellings, and the three places a writer will get them wrong

Every figure in this manuscript is spelled out in body prose. There is no digit in the
prose of any chapter and there may not be one.

- **One hundred to 199 is `a hundred and [WORD]`,** not `one hundred and`. Two hundred
 and above is `[WORD] hundred and [WORD]`. A round hundred is bare: `two hundred`,
 `eight hundred`, `three hundred`, `a hundred`.
- **A thousand and above keeps both `and`s** in the panel: `one thousand and two hundred
 and forty-four hundredweight`. The panel form and the spoken form are two forms.
- **`hundredweight` is attached to the figure** with no hyphen and no space. Tens are
 hyphenated and round tens are not: `twenty-nine`, `ninety`. The hyphen is the house
 form and is not a dash.
- **A window half under two hundred is `a hundred and [WORD]`. The read-aloud numerator
 in its range is `one hundred and [WORD]`.** They are two different figures with two
 different forms and they sit side by side all volume. The plan's own day table prints
 the numerator in the window half's form; that cell is **withdrawn on every odd morning
 of the volume** and a page prints it as `one hundred and`.
- **The two window halves invert at the volume boundary.** A fall goes on an odd morning
 and a rise on an even one, so from day 851 onward **the falling half moves first.**
 Carrying the order of Volume 13 into Volume 14 is wrong on every odd morning.
- **Both halves cross two hundred inside this volume.** The rising half sits at exactly
 two hundred, bare, on days 872 and 873, on two consecutive mornings, against a falling
 half of a hundred and eighty-nine and then a hundred and ninety. The falling half
 reaches two hundred near the end. In each pair the round side is the side a writer
 drops the `and` from.
- **The read-aloud denominator is odd at every value it takes in this volume,** so
 *three hundred and fifty* is never a denominator here. No parity claim is made or may
 be made about the numerator.
- **No month name appears in any chapter and no month number in any spoken line.** The
 read-aloud frame is *of a month nine months back* and does not move, including on the
 month turn. A chapter says *the seventeenth* or *the eighteenth* only inside a heading
 that names an ordinal.

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

`workspace/volume-14/batch-0003/`, days 871 to 880, files `chapter-0658.md` through
`chapter-0667.md`, ten mornings, one `PROMPT.md` on disk and unrun.

It opens on the one month turn inside the volume. It carries the compost line's fall to
paid at thirty-one on day 873, the only downward figure in forty-nine mornings. It
carries the rising half sitting at exactly two hundred on days 872 and 873. It opens on
the board figures at day 870 as given in section 2 above.

**Two placements already moved and may not move back.** The abandonment of the seed
vault was paid on day 864, against a card that placed it at day 879; the page governs,
and no later morning may pay it again or have anybody describe her as having given
something up. The Aldren memory was paid on day 868, on an even morning, against a plan
that named no morning.

---

## 9. What the last pass did

Review-fix pass, 2026-10-02, on Batch 0002. **It did not restart a morning, and every
paragraph it touched already existed on disk.**

- **Repaired five chapters of bare inventory.** In `chapter-0648.md`, `0650`, `0652`,
  `0654` and `0656` the closing standing block was narration with no actor in it. The
  same figures now arrive through a named character doing something: Nia Vale on her
  shelves, Harlan Vetch at the far side of the long table, Tova Reed at the glass,
  Marek doing the Sunday round on the morning the chapter is about. No figure of any
  series changed and no scene, decision or beat was removed.
- **Fixed the word `halfe`**, three times in `workspace/volume-14/batch-0003/PROMPT.md`
  and four times in `outline/batches/volume-14-cards.md`. Both are live files and both
  carry the misspelling inside a spelling rule a writer is told to obey. **It survives in
  seven closed files** and was left there on purpose: `outline/volume-13.md`,
  `workspace/volume-13/outline/PROMPT.md`, the four Volume 13 batch prompts,
  `workspace/volume-14/batch-0001/PROMPT.md` and `workspace/volume-14/batch-0002/PROMPT.md`.
  A completed phase's file is not this phase's to edit, and the misspelling is in an
  archived spelling rule rather than in a morning. A sweep for `halfe` returns those
  seven plus the four archived state files and this line.
- **Compacted this state layer** and moved the previous layer, byte for byte, to
  `reviews/state-archive-2026-10-02/`.
- **Rewrote the state-reading and state-writing instructions in the next batch's prompt**,
  which told the writer to read the head of one file and the feet of three and warned that
  a phase reading a state file whole had spent its context. All four files are now a
  single governing section each and the whole layer is about eight thousand words.
- **Withdrew an unverifiable claim.** A standing note in the old layer said the
  nobody-is-asked-to-choose streak was *"the eleventh volume running."* It could not be
  checked against the manuscript and Volume 14 is the fourteenth. The streak is real and
  it is not counted here.
- **Corrected one false finding rather than acting on it.** The review reported that
  `workspace/volume-14/batch-0001/` has no `.done` marker. It has one. `batch-0002/` has
  none because the runner writes that marker at phase completion and the phase is open,
  and its `.wip-conflict` is a controller marker from a merge conflict. Nothing was
  forged, moved or deleted.

### The three measurements this pass re-derived rather than inherited

- **Figure check.** Every figure of section 2 was re-derived from the rules by script,
 spelled at the house forms of section 4, and required present as a whole phrase in its
 own morning's body prose on a case-insensitive match, because a figure at the start of
 a sentence is capitalised and a case-sensitive check reports a clean batch that is not
 clean. **One hundred and sixty-two items over fifteen kinds, one hundred and sixty-two
 present, zero failures.**
- **Mechanical sweep.** Zero non-ASCII characters, zero em and en dashes, zero digits in
 body prose, zero tabs, zero lines ending in a space, ten of ten files ending in a
 newline, balanced quotation marks and bold markers, no paragraph leaving a quotation
 open. **Zero defects.**
- **Two duplicate gates.** Paragraph near-duplication at a SequenceMatcher ratio of
 0.85 over paragraphs of thirty words or more: zero pairs on a universe of 282. Sliding
 eighteen-word shape with every numeral and every spelled number word normalised to one
 token and hyphens split: 12,866 windows, 12,866 shapes, zero excess instances.

**A clean gate is a number and not a finding.** The inventory-recitation problem is not
visible to either gate: ten paraphrases of one standing list pass both. See
`state/open-threads.md` for what was done about it and what was deliberately not done.