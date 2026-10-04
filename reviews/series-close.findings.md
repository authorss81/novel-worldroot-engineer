# Series Close, 2026-10-04: the manuscript at seven hundred and eighty mornings, and the two corrections the close of the sixteenth owed

**THIS PASS WROTE NO PROSE. IT ALTERED NO MORNING. IT STARTED NO MORNING AND RESTARTED NONE. IT
MOVED NO FIGURE OF ANY SERIES. IT ANSWERED NO THREAD AND CLOSED NO THREAD AND CUT NO NOT-KNOWN
ROW. IT EDITED TWO GOVERNING FILES AND NOTHING ELSE, AND WHAT IT EDITED IN THEM WAS OWED TO IT BY
`reviews/volume-16-close.findings.md` SECTION 31g ITEMS TWO AND THREE, WHICH NAMED BOTH FILES AND
SAID THAT BOTH ARE OWED A CORRECTION BY A PASS WITH THE STANDING TO EDIT THEM. IT TOUCHED NO
CONTROLLER FILE: NOT `scripts/`, NOT `.github/workflows/`, NOT `.opencode/agent/`, NOT `AGENTS.md`,
NOT `PHASE_SYSTEM.md`, NOT `REPO_PLAN.md`, NOT `OUTLINE_GUIDE.md`, NOT `opencode.json`, AND NOT
`state/phase-ledger.json`.**

**ITS HARNESS IS `workspace/series-close/verify_series.py` AND ITS RAW OUTPUT IS
`workspace/series-close/MEASUREMENT.txt`, AND EVERY FIGURE IN THIS FILE IS IN THAT OUTPUT OR NAMED
AS A SOURCE HERE.**

---

## 1. WHY THIS PHASE IS NOT A VOLUME-PLANNING PHASE

**THE PROMPT THIS PHASE RAN UNDER OFFERED TWO SHAPES AND NEITHER OF THEM FITS THE REPOSITORY.**

It said: *if the current volume is complete, plan the next volume and write its first batch.* The
current volume is complete. **THERE IS NO NEXT VOLUME TO PLAN, AND THE REASON IS NOT THAT THE
WORK RAN OUT BUT THAT THE CONTRACT ENDS.**

| the contract | where it is written |
|---|---|
| Length target 780 chapters | `NOVEL_SPEC.md:7` |
| 16 volumes; the first fifteen run 49 chapters and the final volume runs 45, for 780 total | `outline/series.md:6` |
| The final volume is Chapters 736–780 | `outline/ending.md:3` |

Fifteen volumes of forty-nine and one of forty-five is 780. **A seventeenth volume would make the
manuscript longer than the specification, the series outline and the ending outline all say it is,
and the first volume plan would have to be written against a shape three separate files forbid.**
No phase may plan one, and this one did not. **THE CORRECT SHAPE AT A SERIES BOUNDARY IS A SERIES
CLOSE, AND THAT IS WHAT THIS PASS IS.**

It also said: *read the previous 20 chapters.* Read: `chapter-0761.md` to `chapter-0780.md`, being
the last twenty mornings of the book, with the last morning read whole. Nothing in them needed
repair and nothing in them was touched.

---

## 2. THE CONTRACT MAP, MEASURED

| | |
|---|---|
| chapter files on disk | **780** |
| chapter numbers | **1 to 780, no duplicate, no gap, none above 780** |
| volumes | **sixteen, every one contiguous in its chapter numbers** |
| lengths | **fifteen of forty-nine and one of forty-five, and 15 × 49 + 45 = 780** |
| batches | **five batch directories per volume for fifteen volumes and five for the sixteenth, `batch-0001` to `batch-0005`, and volume 12 is the one volume that ran four, its fourth being its closing batch at nineteen mornings: 10 + 10 + 10 + 19 = 49** |

**NO VOLUME'S LENGTH DISAGREES WITH THE CONTRACT AND NO FILE IS OUT OF ITS VOLUME. Volume 12's
four batches against fifteen other volumes' five is that volume's own batch count and is not a
missing file, a merged file or an unwritten morning.**

### 2a. The word figures, per file and never by concatenation

| | measured | published | difference |
|---|---|---|---|
| the manuscript | **2,130,297 across 780** | 2,130,297 across 780 | **0** |
| volumes one to fifteen | **2,031,392 across 735** | 2,031,392 | **0** |
| volume sixteen | **98,905 across 45** | 98,905 | **0** |
| reconciliation | 2,031,392 + 98,905 = 2,130,297 | | **0** |
| files lacking an EOF newline | **75** | 75, the named residual | **0** |

**EVERY PUBLISHED TOTAL IN THE STATE LAYER REPRODUCES TO THE WORD, AT WHOLE-MANUSCRIPT SCOPE, ON A
MEASUREMENT NO PASS HAD TAKEN BEFORE.** Per volume, one to sixteen: 166,022 / 141,818 / 142,952 /
141,727 / 144,846 / 146,883 / 140,227 / 139,423 / 141,658 / 141,223 / 143,305 / 118,058 / 91,321 /
116,146 / 115,783 / 98,905.

---

## 3. THE DAY MAP, WHICH NO FILE STATES AND WHICH FIVE MORNINGS DISAGREE WITH

**THE STATE LAYER PRINTS A CLOCK AND NEVER PRINTS THE MAP THAT CONNECTS A CHAPTER TO A DAY. The
map is `day = chapter + 213`, and it was read back out of the book's own dated headings rather than
assumed: day = 451 + 30 × (month − 4) + (day of month − 1), and the offset counted against the
chapter number.**

| | |
|---|---|
| headings naming a day of month and a month | **193** |
| headings naming no date at all | 581 |
| distinct offsets across the 193 | **six** |
| the offset two hundred and thirteen | **188 headings** |
| the other five offsets | **one heading each**, and every one of the five is in Volume Two or Volume Three |

**THE FIVE MORNINGS THAT DISAGREE, ALL IN THE EARLY BOOK AND NONE IN THE THIRTEEN VOLUMES BEHIND:**

| file | chapter | its heading gives day | the map gives |
|---|---|---|---|
| `chapter-0129.md` | 129 | 571 | 342 |
| `chapter-0144.md` | 144 | 601 | 357 |
| `chapter-0159.md` | 159 | 631 | 372 |
| `chapter-0178.md` | 178 | 661 | 391 |
| `chapter-0204.md` | 204 | 361 | 417 |

**REPORTED AND NOT REPAIRED. All five are closed prose, all five are headings, and a heading is the
one line of a morning that no reader of the prose will ever cross-check against a day.**

### 3a. Two dated headings use cardinals where a hundred and eighty-odd use ordinals

**`chapter-0618.md` reads *The Twenty-One Of The Sixteenth* and `chapter-0626.md` reads *The
Twenty-Nine Of The Sixteenth*, being days 831 and 839. BOTH DATES ARE CORRECT AND BOTH FORMS ARE
WRONG: the house form for a day of month is the ordinal, and every other dated heading in the book
uses it. REPORTED AND NOT REPAIRED, both mornings being closed.**

Four further headings match the shape and carry something else: *The Name Of The President*,
*The Order Of The Work*, *The Sixteenth Of The Month*, *The Top Of The Valley*. **NOT DEFECTS. The
first instrument to read a heading as a date has to be able to say it found four of these and not
count them.**

### 3b. The printed clock has no months before day three hundred and sixty-one

`month(d) = 4 + (d − 451) // 30` returns a month below one for any day before 361. **THE STATE
LAYER PRINTS THAT CLOCK AS IF IT COVERED THE WHOLE BOOK AND IT COVERS NO MORNING BEFORE CHAPTER
148.** A successor who dates an early morning from the printed rule gets a month of zero or less.
This was not found before because no pass had ever needed to date a morning this early, and the
day map had never been written down.

---

## 4. THE PREMISE DRIFT, MEASURED AND NOT RESOLVED

| where | `Worldroot` | `Rootway` |
|---|---|---|
| all 780 chapter files | **0** | **0** |
| `NOVEL_SPEC.md` | 1 | 0 |
| `outline/series.md` | 1 | 11 |
| `outline/ending.md` | 4 | 10 |
| `bible/premise.md` | 2 | 5 |
| `bible/world.md` | 0 | 5 |
| `bible/themes.md` | 1 | 1 |

**THE SPECIFICATION, THE BIBLE AND THE SERIES OUTLINE SPECIFY *THE WORLDROOT ENGINEER*, AND
NEITHER WORD IS ON A SINGLE PAGE OF SEVEN HUNDRED AND EIGHTY MORNINGS. THE BIBLE IS STILL
AUTHORITATIVE AND STILL DESCRIBES A STORY THAT WAS NOT WRITTEN, AND THE MANUSCRIPT IS NOT EVIDENCE
THAT THE PREMISE IS RETIRED.**

**THIS IS A HUMAN DECISION AND NOT A WRITING ONE, AND IT IS THE HEAD OF THE QUEUE AND IT IS NOW
THE ONLY THING IN THE REPOSITORY THAT NO PASS CAN SETTLE.** A human decides whether to re-plan what
is left against the bible or to retire the bible and re-specify the novel. **There is no volume left
to carry that decision into, which is exactly what `state/current.md` section 31g item one said, and
this pass did what that item said a pass could not do: it measured it, at the scope of the whole
book, and put the figure where the decision can be made against it.**

---

## 5. THE TWO CORRECTIONS PAID, AND WHAT WAS NOT TOUCHED

**`reviews/volume-16-close.findings.md` section 31g named two defects in two governing files and
said both are owed a correction by a pass with the standing to edit them. This pass paid both. The
pages governed every word of both.**

### 5a. The surrender, which both series files placed in a volume whose mornings do not carry it

| the claim | measured |
|---|---|
| `outline/series.md:307` gave Volume 13's climax as Marek surrendering the Aldren memory | **a case-insensitive sweep for `aldren` across Volume 13's forty-nine mornings, chapters 589 to 637, returns ZERO** |
| `outline/ending.md:39` said *the specific Aldren memory he surrendered in Volume 13* | **the name is on four pages of the whole book: chapters 0002, 0059 and 0108 in the first three volumes, and `chapter-0655.md` at day 868** |
| | **Volume 14 carries it once, in his own mouth, on day 868: *My father's name was Aldren*** |

**CORRECTED IN THREE PLACES, ALL AGAINST THE PAGE:** `outline/series.md:307`, `outline/series.md:310`
(the Power line, which repeated the same misplacement) and `outline/ending.md:39`. Each now names
Volume 14, day 868 and `chapter-0655.md`, and states the Volume 13 nil beside the correction so that
the file cannot be read as inheriting the wrong placement again.

### 5b. The chapter range in `outline/ending.md`'s first line

The line read *the immediate climax in Chapters 756–773 and a full aftermath through 780*. Measured
against `outline/batches/volume-16-cards.md` section seven, which is the only file in this
repository that owns the placement:

| | morning | day | chapter | inside 756–773? |
|---|---|---|---|---|
| major turn | 21 | 969 | **756** | inside, **and it is not the climax** |
| climax | 32 | 980 | **767** | inside |
| final irreversible act | 36 | 984 | **771** | inside |
| resolution | 42 | 990 | **777** | **outside** |
| last morning | 45 | 993 | 780 | outside, and the aftermath through 780 was right |

**THE RANGE WAS WRONG AT BOTH ENDS: it began the climax on the major turn and ended it three
mornings before the resolution it was supposed to precede. Corrected to the card set's own
placement, one figure per event, and the shape of the volume was not touched.**

### 5c. What this pass did NOT repair, and why

- **`outline/volume-16.md` sections 9 and 10a**, which the close found wrong on the second
  reckoning's crossing and the first reckoning's starting value and which contradict their own day
  table on both. **REPORTED AND CARRIED. Repairing a rule set means re-deriving forty-five days of
  every series in it, and that is a volume-plan repair, not a series close.**
- **The bible.** Untouched. See section four.
- **`outline/ending.md`'s sixteen locks.** Untouched. **A seventeenth lock would name a seventeenth
  volume, and there is none.** This pass's correction to that file is inside the canon-constraint
  text, not in a lock, and this record is where it is recorded.
- **Every closed morning.** See sections six and seven.

---

## 6. THE FINDINGS OF THE CLOSE OF THE SIXTEENTH, RE-CHECKED AGAINST THE PAGE

| the close's finding | re-measured here |
|---|---|
| three: a seven-word line standing twice | **reproduces exactly: `chapter-0735.md:55` and `chapter-0736.md:43`, both `**"Where would you like it written down."**`, and neither is either file's boundary line** |
| five: *nine minutes* twice on `chapter-0774.md` | **reproduces exactly, at `:63` and `:69`, both as an elapsed duration** |
| eight: the last morning contradicts itself about the low road | **reproduces exactly: `chapter-0780.md:5` puts Roan Selk on the low road before the light, `:49` has him say he was up it before the light, and `:7` certifies that not one person in this holding was on that road at any hour of that morning** |
| two and four: unlocked sliding shapes at whole-volume scope | **reproduced and then widened. See section seven.** |
| one: fifteen figures in the wrong form in Volume 16 | **not re-measured here. It is a Volume 16 figure check and this is not a Volume 16 pass.** |
| six: the two rule errors in `outline/volume-16.md` | **carried, see 5c** |
| seven: the house's `Entered`-label sweep returns a false zero | **carried. It is an instrument defect and a successor must know it: the house prints `> **Entered**` and the pattern in circulation is `^>\s*Entered`** |

---

## 7. BOTH GATES AT WHOLE-MANUSCRIPT SCOPE, WHICH NO PASS HAS EVER RUN

**EVERY NIL ANY BATCH IN THIS MANUSCRIPT PUBLISHED WAS A BATCH-SCOPED NIL. THE CLOSE OF THE
SIXTEENTH MEASURED THAT A BATCH-SCOPED READING IS BLIND TO A STANDING BLOCK THAT CROSSES A BATCH
BOUNDARY, AND VOLUME SIXTEEN IS THE ONLY VOLUME THAT HAS EVER BEEN MEASURED AT VOLUME SCOPE. The
whole book has never been measured at all. Both self-collision controls were run first, because a
nil published by an instrument not shown to see anything is not a nil.**

**THE UNIT, declared before any reading was run and the close of the sixteenth's and not a new
one: every non-blank line below a heading, a block-quote separator carrying no words excluded,
apparatus quote lines counted as paragraphs of their own, headings excluded, apparatus inside both
gates. THE NORMALISATION: every run of number words that makes one figure replaced by one token,
the word *and* left alone, hyphenated compounds split on the hyphen, punctuation dropped, case
folded.**

| | whole manuscript | Volume 16, the one volume measured at volume scope |
|---|---|---|
| paragraphs at the declared unit | **34,096**, of which **26,613** are thirty words or more | 1,849 / 1,297 |
| whole-paragraph units of eighteen tokens | **29,585** | 4,597 |
| repeated shapes, whole-paragraph reading | **721** | 50 |
| excess, whole-paragraph reading | **2,251** | 50 |
| sliding eighteen-token windows | **1,583,587** | 69,087 |
| repeated shapes, sliding reading | **37,892** | 679 |
| excess, sliding reading | **77,594** | 679 |
| exact repeated paragraphs at thirty words or more | **46** | nil |

### 7a. THE SLIDING READING IS FIVE TIMES THE RATE, AND NOBODY HAD MEASURED THE RATE

**Volume 16 returns 679 excess on 69,087 windows, which is 9.8 per thousand. Applied to the whole
book's 1,583,587 windows that projects about 15,500 excess. The measured figure is 77,594, which is
49.0 per thousand — FIVE TIMES THE RATE THE ONE MEASURED VOLUME SHOWS.**

**THIS IS THE HEADLINE OF THIS PASS AND IT IS A MEASUREMENT AND NOT AN ALLEGATION. A batch that
published a clean nil did not lie; it measured the wrong universe. The instrument is right and the
scope was narrow, and the difference between those two facts is the entire content of this
section.** 27,665 distinct families are involved. The largest by shape are the recurring gestures of
the standing list — *the rota came round at the second hour*, *he gave the reason first*, *in his
own hand at about* — which are the thread of the book and are supposed to repeat.

### 7b. The forty-six exact long-paragraph repeats, and one standing block

**Forty-six paragraphs of thirty words or more stand more than once in the whole book. The largest
is one paragraph of thirty-five words standing SIX TIMES, and the next two are a pair at thirty-one
and a pair at thirty-four words, all three of them the same standing rule about the engineer of
record.** The six-copy paragraph reads *this is a record and not an argument and the sentence is
off this note for that*. **A STANDING BLOCK THAT CROSSES A BATCH BOUNDARY IS WHAT THE CLOSE OF THE
SIXTEENTH MEASURED SIX HUNDRED AND THREE TIMES IN FORTY-FIVE MORNINGS, AND THIS IS THE SAME CLASS
AT THE SCOPE OF THE BOOK.**

---

## 8. WHAT THE BOOK IS, MEASURED, AND WHAT IS STILL OPEN ON PURPOSE

**The ending is delivered as `outline/ending.md` and `outline/series.md` fix it and this pass
changed no word of either except the three corrections in section five.** The White Mercy is
stopped; the Engine is a bounded reservoir and archive under public maintenance; the Rootway is a
network of varied local flows; Marek's living resonance is in a tested public bed and cannot be
taken back; Iona Vey is under public custody and alive and standing and loses her access and not
her life; the Root Commons is established; the second place is still without water and is read off
a board on the last morning of the book; the thirty-five are thirty-five in and thirty-five out;
the four losses are four; and the pruning window is open, unentered, undescribed and unnamed.

**WHAT IS STILL OPEN ON PURPOSE, AND IS NOT A DEFECT:** the original builders' deeper intentions,
and the full nature of Rootway memory.

**WHAT IS STILL OPEN AND IS A DEFECT, REPORTED AND NOT REPAIRED:** the five disagreeing dated
headings, the two cardinal headings, the forty-six exact long-paragraph repeats, the seventy-seven
thousand five hundred and ninety-four excess sliding windows, the fifteen wrong-form figures in
Volume 16, and the last morning's contradiction about the low road. **ALL SIX ARE CLOSED PROSE. NO
PASS THAT CAME AFTER THE MORNING WAS WRITTEN MAY REPAIR ONE OF THEM, AND THE ONLY PASS THAT COULD
IS A HUMAN ONE.**

---

## 9. THE CONTROLLER ITEMS, RECORDED AND TOUCHED BY NOTHING

1. **`state/phase-ledger.json` STILL READS `phase-000-bootstrap` AGAINST A SEVEN HUNDRED AND
   EIGHTY FILE MANUSCRIPT. IT IS CONTROLLER-OWNED AND IT IS REPORTED FOR THE FIFTH TIME FROM THE
   STATE LAYER AND THE SIXTH TIME FROM THIS FILE. THIS PASS READ IT, CHANGED NOTHING IN IT AND
   FORGED, MOVED AND DELETED NO MARKER.**
2. **A PHASE WHOSE ONLY OUTPUT ALREADY EXISTS AND BELONGS TO A CLOSED VOLUME WAS RUN AFTER THE
   CLOSE.** `workspace/volume-16/plan/` holds the card set for a volume whose forty-five mornings
   were already written and whose close had already run, and that phase produced a card set no batch
   would read. **THE CONTROL PLANE SELECTS IT BECAUSE A PHASE THAT CANNOT RETIRE ITSELF SORTS
   AHEAD OF A LATER ONE. THE FIX BELONGS TO THE CONTROL PLANE AND NOT TO A WRITING DECISION.**
3. **THE DISPATCHER PROMPT THAT SENT THIS PHASE OFFERED A VOLUME-PLANNING SHAPE THAT THE CONTRACT
   FORBIDS AND A NEXT-BATCH SHAPE THAT DOES NOT EXIST.** A prompt is controller-owned. This pass
   recorded the mismatch and did the only job available.

---

## 10. WHAT THIS PASS CREATED

**ONE SUCCESSOR, at `workspace/continuation/next-0016/PROMPT.md`, AND IT IS NOT A BATCH, BECAUSE
THERE IS NO BATCH TO WRITE AND NO VOLUME TO PLAN.** It is the whole-book audit pass: it runs the
seven instruments per volume across all sixteen, it attributes the seventy-seven thousand five
hundred and ninety-four excess windows to volumes that have never been measured at volume scope,
and it puts the human decisions in front of the human. **It may write no morning, and it says so
in its own first line.**
