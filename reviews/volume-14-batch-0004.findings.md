# Volume 14, Batch 0004: findings

## THIS IS THE WRITER PHASE'S OWN MEASUREMENT RECORD AND NOT A REVIEW, AND IT IS HEADED AS ONE, BECAUSE THE WRITER PHASE THAT DRAFTED THE TEN MORNINGS WROTE IT IN THE SAME COMMIT THAT DRAFTED THEM.

**The independent review of this batch is the reviewer phase's report at `logs/batch-0004.review.log`,
and it is this file's only reader who had standing to certify the batch. It found four defects this
file missed and certified clean, and they are listed at section 7 and they are the reason this file
is not to be read as corroboration of itself.** Read it for the derivations, the two gates and their
method. Do not read it for assurance: a writer has no standing to certify its own work, and this
repository has paid that bill four times already.

Days 881 to 890, files `chapter-0668.md` to `chapter-0677.md`. Twenty-six thousand five
hundred and seventy-one words across ten files, per file 3,041, 2,825, 2,632, 2,734, 2,489,
2,673, 2,633, 2,353, 2,445, 2,746, measured with `len(text.split())` per file. **The one-word
repair at section 7 does not move any of these figures**, because the word it replaced was one word.

**Nothing in this file is a state input.** It exists so that the figures below can be
reproduced. Every one of them was produced by a script over the rules at `state/current.md`
section 2, not read off a table and not read off the pages.

---

## 1. The derivation, and what it corrected

The ten mornings' figures were re-derived by script from the rules rather than read from the
prompt's table: the launder from day eight hundred and eighty at one thousand and two hundred
and fifty-nine with five off on an odd morning and eight on on an even one; the window from
day minus four hundred and eighty-three with the falling half at a hundred and forty-five plus
half of everything above three hundred, floor; the aggregate from day minus four hundred and
fifty-two with its clause one under and one over; the boards from day minus sixty-six and day
minus nineteen; the read-aloud numerator from **one** hundred and forty-seven at day eight hundred
and three plus one on every odd morning and its denominator from day minus five hundred and
twenty-six; the rotation from the count rising by one on a day congruent to two modulo four
with the reckonings stepping with it; the three day-minus ages; the letter at day minus seven
hundred and fifty-three.

**THE READ-ALOUD NUMERATOR'S HOUSE FORM IS `ONE HUNDRED AND` AND NOT `A HUNDRED AND`, AND THIS
PARAGRAPH PRINTED IT WRONG UNTIL THE REVIEW-FIX PASS OF 2026-10-02 CORRECTED IT, WHICH IS THE
ERROR THE REVIEW NAMED AS THE THIRD OF ITS OWN DEFECTS.** The derivation reproduced the *value*
correctly and the *form* wrongly, because a script that derives numbers does not know which of the
two hundred-to-range spellings each series takes. **A derivation that gets every figure right can
still carry a series's wrong form, and the form is a figure in this manuscript and not a typo in
one.**

**Against the prompt's own day table: zero mismatches on every field of every row.** The
derivation was then run backwards over days eight hundred and seventy-one to eight hundred and
eighty and reproduced the figures those ten closed mornings carry.

**Two cells in the prompt's hand-typed table are wrong and are corrected here, and the correct
figure is the one the prompt's own text and the plan both carry.** Neither is a house spelling.

1. **The far board on day eight hundred and ninety is eight hundred and seventy-one**, being
   day minus nineteen. A hand-typed table had carried eight hundred and sixty-one, which is
   day eight hundred and eighty's figure.
2. **The compost line is paid at thirty-one on all ten mornings and does not go back.** The
   direction of the single change is settled by `chapter-0660.md` and not by the wording: one
   more load was paid in and not one load was ever let out, so the paid column rose. **No
   morning of this batch prints that line as having fallen, dropped or gone down by one**, and
   the word *fall* is withdrawn for the figure for the length of the volume.

**Three withdrawn figures were checked for on every page and none of them is on any page of
this batch.** No read-aloud figure is printed on any of the five even mornings, and no
*three hundred and fifty* is printed anywhere. No bare *two hundred* for the charter, no bare
*three hundred* for the register form or for Silling's ruled line, no bare *a hundred* for the
letter. The bare round hundreds that do stand on these ten mornings are exactly two: the window
at **four hundred** on day eight hundred and eighty-three, and the run's ordinal at **four
hundred and fortieth** on day eight hundred and ninety. Both are bare because they are bare.

**One figure was corrected by reading rather than by rule.** The hauler of the north-side room
is drawn off a head that four places on the column are arguing over, and that is the whole of
its own arithmetic.

---

## 2. The figure check

**Method.** Every figure of every series for each of the ten mornings was re-derived by script
and then required to be present in that morning's own body prose as a whole phrase on a
**case-insensitive** match, because a figure at the start of a sentence is capitalised on the
page and a case-sensitive check reports a clean batch that is not clean. Each figure was tested
inside its own series and never across the batch, because this volume is one in which *four
hundred*, *three hundred*, *two hundred* and *a hundred* each stand in more than one series.

**Result: two hundred and fifty-five items required, two hundred and fifty-five matching, zero
failures, zero carried by another word order.** A cell that does not fall on a morning at all,
being the read-aloud pair on an even morning and the fourth line on a morning that is not a
fourth-line morning, was not required and is not printed there.

The thirty standing items tested on every morning are: the third launder; the ordinal of the
run; the window and its two halves; the aggregate and both limbs of its clause; the near board
and the far board; the three derived ages on the register form, the charter and Silling's second
ruled line; the letter; the compost line at paid at thirty-one; the count of blanks at
thirty-nine; the standing for the second rule at the thirty-ninth time; eleven journeys on the
barrow; fifteen lines in the use log; seven sessions; six ruled rows for what we do not know;
the two other books at fifty-three; and the man of about seventy at twenty-nine fetchings.
The read-aloud numerator and denominator were required on the five odd mornings and the fourth
line on the three fourth-line mornings.

---

## 3. The two duplicate gates, both scopes, both published

### 3.1 The self-collision test the implementation was checked against first

**A gate that never collides a paragraph with itself will publish a nil on a batch that has
one.** The second gate was therefore run against a paragraph built to collide with itself, being
one clause repeated end to end, before it was run on anything else.

**Result: six overlapping equal eighteen-word windows inside that single paragraph. The gate
sees it.** The first gate was checked the same way and its universe and pair counts are
published below, so that the number can be recomputed rather than believed.

### 3.2 The first gate, whole paragraphs

Every prose paragraph of thirty words or more, against every other prose paragraph of this batch
and of the thirty mornings behind it, excluding headings and apparatus. An ordered pair is
counted where the two word counts are within a factor of one and a quarter and
`difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()` is zero point eight five or
better, with `real_quick_ratio` and `quick_ratio` as the only shortcuts, behind an admissible
upper bound on multiset intersection.

**Universe: one thousand three hundred and thirty-four paragraphs of thirty words or more.
Ordered pairs compared inside the word-count factor and the two shortcuts: three hundred and
ninety-nine thousand three hundred and sixty-seven. Excess pairs at or above zero point eight
five: one.**

**The one excess pair is `chapter-0674.md` against `chapter-0638.md`, at a ratio of exactly one
over thirty-one words, and it is the far-end locked sentence spoken whole on day eight hundred
and eighty-seven against the same sentence spoken whole on day eight hundred and fifty-one.** A
locked figure that is reduced by a word is a different figure, so the identity is required and
is not a defect. **It is excluded from the count above only in the sense that it is named; it
is not removed from the measurement, and the measurement stands at one.**

### 3.3 The second gate, eighteen-word shape, both scopes

Normalisation, printed in full. Every integer numeral becomes one token; every spelled number
word becomes one token, the list being zero through nineteen, then twenty, thirty, forty,
fifty, sixty, seventy, eighty, ninety, hundred, thousand and million, then first through
nineteenth, then twentieth, thirtieth, fortieth, fiftieth, sixtieth, seventieth, eightieth and
ninetieth; the word *and* is not a number and is left alone; every hyphenated compound is split
on the hyphen before lookup; punctuation is dropped and case is folded; every chunk is a full
eighteen words.

- **Chunk scope**, being non-overlapping eighteen-word chunks stepped eighteen words at a time
  inside each paragraph: **one thousand one hundred and fifty-four units, one thousand one
  hundred and fifty-four shapes, two excess against the thirty mornings behind, and zero
  duplicate shapes inside this batch.**
- **Sliding scope**, being an eighteen-word window at every offset inside each paragraph:
  **sixteen thousand three hundred and seventeen units, sixteen thousand three hundred and seventeen
  shapes, seventeen excess against the thirty mornings behind, and zero duplicate shapes inside
  this batch.**

**All nineteen of those excess units are the two locked sentences.** Three sliding windows and
one chunk are the comfort line spoken whole on day eight hundred and eighty-four against the
same line spoken whole on day eight hundred and fifty-one; fourteen sliding windows and one
chunk are the far-end sentence spoken whole on day eight hundred and eighty-seven against
day eight hundred and fifty-one. **There is no excess of any other kind on either scope
against the thirty mornings behind, and none at all inside this batch.**

**The sliding reading was the larger one again and the chunk reading again refused what it
refused on the batch behind**, so both are published, and the shape that survives on the sliding
scope only is named above rather than summarised.

### 3.4 What had to be rewritten to reach that, and the standing-block list

**The batch as first written carried a real defect and it was the defect this house names.** It
walked the same list of about fifteen standing items in the same shapes: twenty-two distinct
shapes inside the batch repeated on the sliding scope, thirty-three excess paragraph pairs
inside the batch, and one hundred and forty-nine sliding windows and seven chunks against the
thirty mornings behind. **The cheapest way through was the way the prompt names, and it was
worked through block by block: every standing block was given a different actor, a different
verb and a different sentence order on each morning it appears, and no figure of any series was
altered in any of it.**

The blocks re-shaped, and the mornings they were re-shaped on: the read-aloud run and its
five reasons, one per even morning from five different people, none of them among the ten who
had already given that reason in this volume; the window and its two halves, with the inversion
declared out loud on the first morning and no two mornings declaring it the same way; the
aggregate and its clause, off the wall, off the front of the sheet, off the back of it, off a
slate copied in the spring and off a mason counting; the three papers on the long table, in
nine different shapes across nine mornings; the man of about seventy, in nine; the barrow, the
use log, the sessions, the not knowns, the two other books; the count in force; the ladder, the
low-board offer and the ring of bare ground; the drawer and its nail; the compost line; and the
launder at the wall, read by the clerk, by Nia Vale, by the woman of thirty-eight of Marden, by
the mason from the north end, by the clerk to a slate, by Marek from a tap house door and by the
clerk to a man with a case.

**One duplicated reason was found and removed.** The mason gave the same reason for not saying
the two things on two mornings, which the ten-new-reasons rule forbids; one of the two was
cut and the mason was given a different line.

**Two passages were found to be one paragraph run together** by a bad splice while the rewrites
were being applied, and were separated again.

---

## 4. The mechanical sweep

Zero non-ASCII characters. Zero em dashes and zero en dashes. Zero digits in body prose, and one
caught and fixed, being a figure mangled into `fifty53` by a replacement. Zero tabs. Zero lines
ending in a space. Ten of ten files ending in a newline. Balanced quotation marks and balanced
bold markers in every file. No paragraph leaving a quotation open. No paragraph over a hundred
and twenty words. No morning's mean paragraph length over the house ceiling of eighty-five. No
two speech paragraphs of one speaker standing back to back with no action between them, and
twenty-two places where that was true were given an action beat. Ten different opening words on
the ten closing paragraphs. **Zero defects.**

**Three month names were caught.** *March* appeared three times, in a woman's mouth twice and
in a woman's slate once, and the plan forbids a month name on any page of this volume. All
three were cut and the sentences were rewritten without them.

---

## 5. The two locked figures, and the allowance

The far-end sentence is spoken whole once in this batch, on day eight hundred and eighty-seven,
by Sera Quill, in a yard where Hesta Lyle has just named the far end of that column and said
she is not going to stand at it. The comfort line is spoken whole once, on day eight hundred
and eighty-four, by Nia Vale, at an open window in the north-side room, while the man of about
fifty is already saying something else about a key and six weeks.

**A sweep for either whole sentence and for every load-bearing fragment of either, across all
ten mornings, returns the locked figure on its own morning and nothing on the other nine.** No
shortened form of either is printed anywhere in the batch, and neither appears on the other's
morning in any form.

**The in-between allowance is three for each and this batch spends one of three for each.**
Two remain for each and both fall in the closing batch. The first and the last morning of the
volume each hold a separate allowance and are untouched.

**A measurement that says why the comfort line is hard to see here.** It is twenty words and
the first gate's floor is thirty words, so **the comfort line is structurally invisible to the
first gate and only an eighteen-word gate can see it.** A clean first gate is therefore not
evidence about either locked sentence. The one excess pair the first gate did report is the
far-end sentence, which is thirty-one words and is above its own floor; the comfort line's
three sliding windows are the only trace of it anywhere, and a first gate reporting zero would
have said nothing about it at all.

---

## 6. What a reviewer should look at first

1. **The standing-block delivery.** Thirteen people give figures across ten mornings and no
   standing block arrives twice in the same shape. That is the deliberate change from the
   thirty mornings behind and it is the thing most likely to be wrong in a way neither gate can
   see.
2. **The costing arithmetic on days eight hundred and eighty-two, eight hundred and eighty-five
   and eight hundred and ninety.** The batch's central pressure is the reach's cost and nobody
   in this holding is asked to choose anything on any of the ten mornings. Whether the
   arithmetic stays honest while nobody chooses anything is a judgement call and it belongs to a
   reader.
3. **The reason the man of about fifty was given on day eight hundred and eighty-four.** The
   comfort line lands on a Monday in a yard where somebody else is already talking, which is
   what the plan says the locked sentences need, and it is worth checking that the yard is
   genuinely already occupied when it lands.

---

## 7. What the independent review found that this file missed, added by the review-fix pass of 2026-10-02

The report at `logs/batch-0004.review.log` re-derived every figure from the plan's own rules
instead of trusting this file, reproduced all of section 2 and all of section 3, and returned four
defects. Three are repaired; one is recorded and left to a pass with the standing to pay it.

1. **A banned bare word on one page of one morning, at `chapter-0676.md`.** The word *volume* stood
   in the clerk's mouth, in a line about the level at which he has said a figure five mornings
   running, and the card set bars *volume, batch, chapter, seat, fieldbook* and *panel* from body
   prose. **One word in one line: *volume* is now *level*, and the sentence and the paragraph stand.**
   **This file's mechanical sweep at section 4 does not test for banned words at all**, which is
   why it reported zero defects on a page that carried one, and the sweep is the record rather than
   the check.
2. **The queued prompt's third fourth-line morning was wrong, and this file did not look.** The
   prompt named day eight hundred and eighty-nine, which is not congruent to two modulo four; the
   three are days eight hundred and eighty-two, eight hundred and eighty-six and eight hundred and
   ninety. **The prompt's own day table and its own three card headers and its own count-in-force
   paragraph all said ninety, and the error stood in one clause of one paragraph**, so the file's
   claim that it checked the derivation against the prompt's table was true of the table and silent
   on the prose around it. **The pages were right: the count is carried on days 882, 886 and 890 in
   `chapter-0669.md`, `chapter-0673.md` and `chapter-0677.md`.** Repaired in the prompt.
3. **This file's own restatement of the read-aloud rule printed the numerator in the window half's
   form**, at the head of section 1, and is corrected there. **The review's paraphrase of this item
   also names the anchor day as day eight hundred and eighty-three, and the file says eight hundred
   and three, which is correct**; the error in this paragraph is the form and not the day, and the
   two are separate faults and only one of them was here.
4. **The plan's day table prints the numerator in the window half's form on all twenty-five of its
   read-aloud rows, against the plan's own spelling section, which mandates `one hundred and` for
   that series.** The manuscript follows the spelling section on all twenty occasions and the
   queued closing-batch prompt does too. **NOT REPAIRED HERE.** `outline/volume-14.md` is a
   completed phase's file and this pass has no standing to edit it; the state layer already
   withdraws that cell on every odd morning of the volume, `state/continuity.md` section 7 item 2,
   and **the correction of the table itself is owed by a pass that owns the outline.**

**And one thing the review asked for that is a decision and not a defect.** It asked that the
closing batch's four in-between locked sentences, which spend both allowances to their cap and
override prohibitions on seven cards, be decided before that batch runs and not after. **The
decision is recorded in `state/open-threads.md` section 4 and in `state/current.md` section 8, and
the reasoning was already written into the queued prompt's own section 5 before the review ran.**
What the review added is that both allowances go to their cap for the first time in the volume, and
that each of the four landings has to be measurable against the plan's rule that somebody else was
already saying something else. **No morning of the closing batch has been written, so nothing in it
is spent yet and the decision is still cheap to change.**