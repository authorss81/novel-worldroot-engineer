# VOLUME 11 OUTLINE FINDINGS - WHAT THE PLANNING PASS MEASURED, WHAT IT CORRECTED, AND WHAT IT DECLINED

**DATE OF THIS PASS: 2026-09-29. THIS IS THE RECORD OF A PLANNING PASS AND IT IS NOT A CLOSE OF A VOLUME AND IT IS NOT AN INDEPENDENT REVIEW. IT CERTIFIES NOTHING. THERE ARE NO CHAPTERS OF VOLUME 11 ON DISK AND THIS FILE MEASURED NO PROSE BECAUSE THERE IS NONE TO MEASURE.**

**WHAT THIS PASS PRODUCED: `outline/volume-11.md`, AND ONE SUCCESSOR, `workspace/volume-11/batch-0001/PROMPT.md`. NOTHING ELSE. NO CHAPTER. NO PROSE. NO STATE FIGURE OF ANY VOLUME 11 SERIES EXISTS ON ANY PAGE BECAUSE NO CHAPTER HAS GIVEN ONE, AND THE OUTLINE PRINTS NO SUCH FIGURE AS A STANDING.**

**THE GOVERNING RECORD IS `outline/volume-11.md`. THIS FILE IS ITS AUDIT AND ITS DISAGREEMENT WITH THE PROMPT THAT DISPATCHED IT, AND THE TWO ARE THE SAME AUTHORSHIP AND NEITHER IS A REVIEW OF THE OTHER.**

---

## 0. THE THREE-PART TEST THE PHASE PROMPT SET, AND THE ANSWER TO EACH PART

**PART ONE. DOES THE CENTRAL PRESSURE ANSWER Volume 10's NEXT QUESTION - *what does freedom cost the neighbours who depend on a system someone else rejects?* - WITHOUT PRETENDING Volume 10's OPEN THREADS ARE CLOSED?**

**YES, AND THE ANSWER IS GIVEN ON THE FIRST MORNING OF THE FIRST MOVEMENT AND THEN NOT IMPROVED ON.** `outline/volume-11.md` puts it in the central-pressure section in the holding's own words: **the charter that let a body decline an inspection said nothing about the machine, AND MOST OF THE NEIGHBOURS ARE STILL CUSTOMERS.** Four bodies of households signed a charter in a room nine miles off and went on signing, in a second hand, for stored light out of a machine about nine miles off, and **the two signatures are on two correct documents in two different hands and neither hand knows about the other.** That is an answer and it is an uncomfortable one, and it is the whole reason Volume 11 exists.

**AND IT DOES NOT PRETEND ANY THREAD IS CLOSED.** All thirty-five are named in the outline's threads table with the chapter each advances in, and none is answered, closed, reworded, advanced to a figure, summed or grouped. **The six that Volume 10 opened on its last morning are carried in the outline's refusals section and in the last-morning description: the far end of a thing held by two people and neither of them him; the man who walked nine miles and is still on the south wall of the seed house and is not asked his name; the man in the cart shed with no name, no figure and no outcome; the four clauses read out once in a room with one door with one of the two declining bodies absent and unasked; the thirty-five themselves, which no page may tally; and the forty-nine mornings in one column four ruled lines deep.** **Ostrey is a village of about thirty households with a name on a map and this volume does not go there and no later volume may use the name as a symbol.**

**PART TWO. DOES THE CHAPTER-TO-DAY TABLE'S DAY ARITHMETIC RECONCILE WITH THE DAY CLOCK ON EVERY ROW, WITH BOTH MONTH TURNS PLACED CORRECTLY?**

**YES, ALL FORTY-NINE ROWS, AND IT WAS CHECKED BY SCRIPT AGAINST THE ANCHOR AFTER THE FILE WAS WRITTEN AND NOT BEFORE.** The anchor is day 451 as the first of the fourth month and a Tuesday, with months running thirty days. The check re-parses all forty-nine rows out of the file on disk and re-derives every column:

- weekday, 49 of 49 correct, from `Tuesday + (day - 451) mod 7`
- ordinal, 49 of 49 correct, from `(day - 451) mod 30 + 1`
- third launder, 49 of 49 correct, at plus eight on an even day and minus five on an odd day, off 987 on day 703
- rises-and-falls window, 49 of 49 correct, and the two halves add on every row without exception
- aggregate, 49 of 49 correct, and the morning-out-of clause correct on all 49
- day-minus pair, 49 of 49 correct, forty-seven apart on every row
- read-aloud run, **24 of 24 read mornings correct** and **25 of 25 unread mornings correctly carrying no figure**, checked by parsing the spelled form back into an integer and comparing it against `(day - 509) / 2` and `day - 526`
- fourth-line mornings, 12 rows, days 706, 710, 714, 718, 722, 726, 730, 734, 738, 742, 746 and 750, and the standing on each of them correct at 103/29/74 rising one per row to 114/29/85, with the two counts of the rotation running 51 and 38 to 62 and 49 and holding the difference of thirteen on all twelve.

**THE TWO MONTH TURNS ARE ON DAYS 721 AND 751 AND BOTH ARE INSIDE THE RANGE.** Day 721 is the first of the thirteenth month and day 751 is the first of the fourteenth, and **neither turn resets any count, and the day-to-month table reconciles on all forty-nine rows.** The four frame columns were derived for the specific day and not copied: days 704 to 720 carry the twelfth month, 721 to 750 the thirteenth, 751 to 752 the fourteenth, and the ten month anchors in the frame table were each re-derived from day 451 and not from the volume behind.

**PART THREE. DOES EVERY FIGURE IN THE OUTLINE APPEAR ON A PAGE OF Volume 10 OR DERIVE FROM A RULE THE OUTLINE PRINTS?**

**YES, AND THE FIGURES THAT WERE HANDED TO THIS PASS AND FAILED ARE THE PROOF, BECAUSE SIX OF THEM DID NOT AND THEY ARE CORRECTED IN `outline/volume-11.md` SECTION 2.** Every other figure is either a `wc -w` result measured for the file, a script result run over the chapter files, a figure on the page of a chapter of Volume 10 named at its line, or a number produced by a formula printed in the same section that produces it. **The outline prints no projection of the manuscript and no projection of Volume 11's length except in the expected-length section, which says on its face that it is a band and not a figure and may not be entered into any state file, any bracket or any total until it is measured.**

---

## 1. THE SIX FIGURES THIS PASS WAS HANDED THAT ARE WRONG, AND WHAT WAS DONE ABOUT EACH

**THIS IS THE HEART OF THE RECORD. THE PROMPT THAT DISPATCHED THIS PHASE CONTAINED SIX FIGURES THAT FAIL THEIR OWN RULE. FOUR OF THEM ARE THE SAME ERROR AND THE ERROR IS NAMED FIRST.**

### 1a. THE WEEKDAY ERROR, AND IT IS ONE ERROR IN SIX PLACES

**THE PROMPT STATES THAT DAY 703 IS A MONDAY, THAT DAY 704 IS A TUESDAY, THAT DAY 721 IS A FRIDAY, THAT DAY 751 IS A SUNDAY AND THAT DAY 752 IS A MONDAY. ALL FIVE ARE WRONG BY ONE DAY AND THE CORRECT FIGURES ARE: DAY 703 IS A TUESDAY, DAY 704 IS A WEDNESDAY, DAY 721 IS A SATURDAY, DAY 751 IS A MONDAY AND DAY 752 IS A TUESDAY.**

**THE RULE IS DAY 451 IS THE FIRST OF THE FOURTH MONTH AND IS A TUESDAY AND MONTHS RUN THIRTY DAYS. `state/current.md` AND THE PROMPT AGREE ON THAT ANCHOR AND BOTH DISAGREE WITH THEMSELVES ABOUT DAY 703.**

| Day | Derivation | Weekday |
|---|---|---|
| 691 | 451 + 8 x 30 = 691; 240 mod 7 = 2; Tuesday + 2 | **Thursday** |
| 703 | 691 + 12; 12 mod 7 = 5; Thursday + 5 | **Tuesday** |
| 704 | 703 + 1 | **Wednesday** |
| 721 | 451 + 270; 270 mod 7 = 4; Tuesday + 4 | **Saturday** |
| 751 | 451 + 300; 300 mod 7 = 6; Tuesday + 6 | **Monday** |
| 752 | 751 + 1 | **Tuesday** |

**AND THE DERIVATION IS CHECKED AGAINST EIGHT ROWS OF `outline/volume-10.md`'s OWN CLOSED TABLE**, being days 655, 660, 661, 690, 691, 692, 694 and 703, **and all eight agree on weekday, ordinal and month.** It is checked a second time against the closed pages: **`workspace/volume-10/batch-0005/chapter-0490.md:21` writes day 703's third-launder figure as *FIVE UNDER MONDAY*, which puts day 702 on a Monday and day 703 on a Tuesday; `chapter-0484.md:35` names day 697 a Wednesday; `chapter-0480.md:35` names day 693 a Saturday; `chapter-0488.md:79` names day 701 a Sunday; and `chapter-0476.md:83` names day 689 a Tuesday. All five agree with the derivation and none agrees with the Monday.**

**THE ERROR IS THE ONE `reviews/volume-10.findings.md` NAMES AS THE THING THAT COST Volume 10 ITS FIFTH NINTH-DAY RETURN: A FIGURE WAS CARRIED ACROSS A BOUNDARY INSTEAD OF BEING DERIVED FROM A RULE. IT IS THE SAME FAILURE, IN A DIFFERENT SERIES, COMMITTED BY THE PROMPT THAT WARNED AGAINST IT, AND IT WAS CAUGHT BY DERIVING.**

**CORRECTED IN `outline/volume-11.md` SECTION 2 ITEM ONE, WITH ALL FIVE WITHDRAWN FIGURES NAMED AS WITHDRAWN. `state/current.md` LINE 33 AND THE PROMPT BOTH CARRY THE MONDAY AND NEITHER IS EDITED BY THIS FILE.** A marked correction block HAS been inserted at the head of `state/current.md` and nothing has been deleted from it; see section 6 below.

### 1b. THE READ-ALOUD RUN AT THE END OF THE VOLUME

**HANDED: 121 OF 201 AT DAY 752. BOTH FIGURES ARE WRONG.** The denominator is day minus five hundred and twenty-six, so day 752 gives **226** and not 201. And the numerator is `(day - 509) / 2`, so day 752 gives **121 and a half, which is not a count of anything**, and day 751 is the last morning in this volume on which the run is a whole number at all, at **121 of 225**. The 121 of 201 is withdrawn. **THE PROMPT ITSELF SAYS THE RUN *DOES NOT* GO ON EVERY SECOND DAY, AND THE FIGURE IT PRINTS FOR DAY 752 IS THE FIGURE OF A CADENCE THAT HAS BEEN DECIDED AGAINST.**

**THE CADENCE WAS NOT CHOSEN BY THIS PASS. IT IS FORCED. THE NUMERATOR `(day - 509) / 2` IS INTEGRAL ON ODD DAYS AND HALF-INTEGERAL ON EVEN DAYS, AND IT REPRODUCES Volume 10's OWN CLOSING FIGURES EXACTLY: 73 OF 129 AT DAY 655 AND 97 OF 177 AT DAY 703.** So Volume 11 reads it on twenty-four odd mornings and not on twenty-five even ones, and **the volume's first morning carries no figure for the run and says why, which is an inversion of Volume 10's first morning and is declared as one in the outline's decisions block.**

### 1c. THE SECOND OF THE FOUR LINES IN THE MAN OF ABOUT THIRTY-ONE OF SILLING'S OWN BOOK

**HANDED: 90 DAYS AT DAY 752. THE CORRECT FIGURE IS 190, AND THE RULE IS DAY MINUS FOUR HUNDRED AND SIXTY-TWO.** The rule is checked against two closed pages: `chapter-0489.md` gives one hundred and forty on day 702 and `chapter-0482.md` gives one hundred and thirty-three on day 695, and 702 - 140 = 562 and 695 - 133 = 562. **THE NINETY DROPS A DIGIT. THE FIGURE IS 142 AT DAY 704 AND 190 AT DAY 752 AND IT IS NOT DAY MINUS FOUR HUNDRED AND FIFTY-TWO, WHICH IS A DIFFERENT AGGREGATE AND IS NEVER ADDED TO IT.**

### 1d. WHAT WAS HANDED CORRECTLY AND WAS THEREFORE NOT TOUCHED

**THE MANUSCRIPT AT 1,446,779 ACROSS 490 FILES, Volume 10 AT 141,223 ACROSS FORTY-NINE, THE TWO CLOSED-VOLUME TOTALS AT 1,163,898 ACROSS 392 AND 141,658, THE THIRTY-FIVE THREADS AT DAY 703, THE THIRD-LAUNDER STANDING AT 987, THE WINDOW AT 220 SPLIT 115 AND 105, THE AGGREGATE AT 251 WITH ITS CLAUSE AT 250 OF 252, THE DAY-MINUS PAIR AT 637 AND 684, THE FOURTEEN-DAY CYCLE OFF DAY 506, THE NEXT NINTH-DAY RETURN ON DAY 712, THE NEXT FETCHING ON DAY 721, THE NEXT READING OF THE WELL ON THE SHELF ON DAY 706, THE WINDOW OF THE OFFICE'S WORK AT 726 TO 731, THE REGISTER FORM'S TENURE AS DAY MINUS FOUR HUNDRED AND FIFTY-SIX AT 196 DAYS ON DAY 752, AND THE SIXTH OF THE TWELVE AND FOURTEENTH MONTH TURNS.** **ALL OF THESE WERE RE-DERIVED OR RE-CONFIRMED INSTEAD OF BEING COPIED, AND ALL OF THEM REPRODUCE.** The manuscript was measured again for this file in a loop with `wc -w` per file and returns 1,446,779, and `cat` returns 1,446,776 for the named reason of three files in a closed batch without an EOF newline.

---

## 2. WHAT WAS DECIDED BY ARITHMETIC RATHER THAN BY TASTE, AND WHY THAT MATTERS

**THREE DECISIONS IN THE OUTLINE ARE ARITHMETIC AND NOT PREFERENCE, AND A LATER PASS THAT DISAGREES WITH ONE OF THEM CAN SHOW THE ARITHMETIC RATHER THAN MAKE AN ARGUMENT.**

1. **THE THIRD LAUNDER KEEPS PLUS EIGHT AND MINUS FIVE.** Four deltas were computed off the day-703 standing of 987 across the forty-nine mornings: **plus eight and minus five gives forty-nine distinct figures; plus nine and minus five gives forty-nine; plus nine and minus six gives twenty-seven; plus seven and minus six gives thirty-one.** A run that never writes the same number down twice, which is on the page of every one of Volume 10's forty-nine mornings, cannot have a delta that produces a repeat, so the two that give twenty-seven and thirty-one are ruled out and the smaller of the two that give forty-nine is the one taken.
2. **THE READ-ALOUD CADENCE IS FORCED BY THE NUMERATOR'S PARITY AND IS NOT A CHOICE.** See section 1b.
3. **THE RISES-AND-FALLS WINDOW IS IN THE TWO HUNDREDS ON ALL FORTY-NINE MORNINGS AND EVERY ONE OF ITS FORTY-NINE SPELLINGS IS PRINTED.** `reviews/volume-10.findings.md` finding one measured nineteen chapters of the closed volume carrying a nonsense spelling of this total, in two different misspellings, once the total crossed two hundred on day 683. **Volume 11's window never goes below two hundred and never above two hundred and seventy, so the defect's condition holds on all forty-nine mornings of this volume and the outline prints the correct spelling of every figure from 221 to 269 so that five batch prompts cannot invent one.** A measurement for this file finds twenty-five instances of the pattern `A HUNDRED AND [WORD] HUNDRED` across all four hundred and ninety files, twenty-one of them inside Volume 10 and four in earlier volumes where the pattern is a hundredweight figure and is correct.

**AND THE TWO OTHER HUNDRED-CROSSINGS OF THIS VOLUME ARE DECLARED IN THE SAME PLACE:** the third launder crosses one thousand on **day 708**, Chapter 495, a Sunday, at one thousand and one hundredweight, off nine hundred and ninety-three the day before; and the read-aloud denominator crosses two hundred on **day 727**, Chapter 514, where the correct spelling is *two hundred and one* and is not *a hundred and two hundred and one*. **The read-aloud numerator crosses one hundred on day 709 at one hundred of one hundred and eighty-three.**

---

## 3. THE COLLISION SEARCHES, RUN FOR THIS FILE

**RUN OVER ALL FOUR HUNDRED AND NINETY CHAPTER FILES NOW ON DISK, ON A WORD BOUNDARY, IN FIGURES AND IN SPELLED WORDS.**

**THE THIRD-LAUNDER FIGURES.** The word-bounded numeral test returns **ZERO hits on all forty-nine**. The spelled test returns **zero on forty-seven** and returns two figures with hits, both named in the outline: *nine hundred and ninety* at twelve hits in four files, all of them spoken arithmetic about days and not hundredweight figures; and *one thousand and forty* at twenty-four hits, all of them pressure frames and wells. **Neither is a collision, because a figure that is not a figure of this series is not a collision.** A first run of this search used a plain substring count rather than a word-bounded one and returned hits on all forty-nine window totals and on figures as small as 221, which is the shape of a search that counts the digits inside other numbers. **The substring result is withdrawn and the word-bounded result is the one published, and the withdrawal is named here because a search that reports a collision where there is none is the same failure as one that reports none where there is one.**

**THE WINDOW TOTALS.** The word-bounded numeral test returns one or two hits on each of the forty-nine and every one is a bare digit inside another figure or a date, not the total spelt out. The spelled test returns hits on twenty-seven of the forty-nine and every one is an ordinary round number already in the manuscript.

---

## 4. WHAT WAS READ, IN FULL AND IN PART, AND WHAT WAS NOT

**THIS SECTION EXISTS BECAUSE THE PROMPT SET A READING BUDGET AND BECAUSE A RECORD THAT CLAIMS A READING BUDGET IT DID NOT MEET IS WORSE THAN ONE THAT DOES NOT MAKE THE CLAIM. THIS IS THE HONEST ACCOUNT.**

**READ WHOLE:** `outline/series.md`, `outline/ending.md`, `outline/volume-10.md` IN ALL ITS LINES INCLUDING ITS MEASURED SECTION, ITS THREADS TABLE, ITS CHAPTER-TO-DAY TABLE, ITS MONTH-FRAME TABLE, ITS EXPECTED-LENGTH SECTION, ALL ITS GUARDRAILS AND ITS ENDING LOCK; `reviews/volume-10.findings.md` IN ALL ITS LINES, WITH ITS SECTION 6 AND ITS SECTION 10 READ TWICE; `state/continuity.md` AT `tail -n 250`; `state/open-threads.md` AT `tail -n 140`.

**READ IN PART:** `state/current.md`, WHICH IS 954 LINES AND WHICH THIS PASS READ THROUGH ITS HEAD AND ITS LIVE-FIGURES SECTIONS, BEING THE PART A PHASE IS REQUIRED TO READ WHOLE, AND NOT THROUGH ITS HISTORICAL SECTIONS.

**READ IN FULL AS CHAPTERS: EIGHT OF VOLUME 10'S FORTY-NINE**, being `chapter-0442.md`, `chapter-0482.md`, `chapter-0483.md`, `chapter-0484.md`, `chapter-0487.md`, `chapter-0488.md` and `chapter-0489.md`, and `chapter-0490.md` TO LINE THIRTY. **THAT IS NOT ALL FORTY-NINE AND THIS PASS DOES NOT CLAIM OTHERWISE. THE CHAPTERS CHOSEN WERE THE VOLUME'S FIRST MORNING AND THE EIGHT CHAPTERS OF ITS CLOSING MOVEMENT, BECAUSE THOSE ARE THE CHAPTERS THAT CARRY THE DAY CLOCK, THE LADDER OPENING, EVERY STANDING AND THE STATE THE NEXT VOLUME INHERITS, AND EVERY FIGURE IN THIS OUTLINE THAT IS NOT IN `outline/volume-10.md` OR DERIVED WAS TAKEN FROM ONE OF THEM AND IS NAMED AT ITS LINE.**

**WHAT THAT MEANS FOR THE RELIABILITY OF THIS OUTLINE, STATED PLAINLY.** The prose voice, the day-clock paragraph form, the closing forms and every floor were read at the source. **The middle twenty-nine chapters of Volume 10 were not read in full and no figure in this outline depends on them.** Any claim about a closed chapter that is not named at a line in this file or in `reviews/volume-10.findings.md` should be treated as unverified.

---

## 5. WHAT THIS PASS DECLINED, AND WHY

**IT DID NOT WRITE PROSE AND IT DID NOT WRITE A CARD.** One successor was created and it is the one the foot of this phase names: `workspace/volume-11/batch-0001/PROMPT.md`, for chapters 491 to 500, days 704 to 713, Movement 1. **NO SECOND PHASE DIRECTORY WAS CREATED AND NO THIRD.**

**IT DID NOT REPAIR ANY OF THE ELEVEN NAMED OPEN ITEMS IN `reviews/volume-10.findings.md` AND IT DID NOT UNWIND ANY OF THEM.** `chapter-0444.md` stays at 3,055 words against a ceiling of 3,050. The two `> ENTERED` blocks in capitals stay in capitals and the measurement rule stays blind to them. Marek's 219 and the man of about fifty's 137 stay on no page. The nineteen misworded window totals stay as they are. The fifth ninth-day return stays unspent on day 676 and four hundred and fifteen hundredweight stays nowhere. `chapter-0469.md:64` keeps the word open. **AND THE OUTLINE'S OWN TREATMENT OF THE TWO LADDERS IS THE ANSWER TO THE TWO OF THOSE ITEMS: NEITHER LADDER APPEARS IN ANY TABLE, BRACKET OR ROW OF THE OUTLINE, AND THE MAN OF ABOUT FIFTY'S DOES NOT OPEN ON A FIGURE THAT ASSUMES 137 WAS SPENT, AND NO MORNING OF THIS VOLUME MAY PRINT 137 AT ANY SITE.**

**IT DID NOT COMPACT THE THREE APPEND-ONLY FILES.** They are a chain in which a later section exists for the purpose of naming an earlier section's figure as withdrawn, and the withdrawal is the only thing standing between a withdrawn figure and a pass that reads it as live.

**IT DID NOT FORGE A MARKER.** `workspace/volume-10/` carries no `.done` marker on any of its six directories and the runner selects the first unmarked directory in sorted order, which is `batch-0001/`, and that is a controller decision recorded nine times now and not acted on.

**IT DID NOT TOUCH A CONTROLLER FILE.** `AGENTS.md`, `NOVEL_SPEC.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `MODEL_VERIFICATION.md`, `RESEARCH.md`, `SETUP.md`, `README.md`, `opencode.json`, `scripts/`, `.github/workflows/`, `.opencode/agent/` and `state/phase-ledger.json` were not opened for writing.

**IT DID NOT EDIT A CLOSED OUTLINE OR A CLOSED CHAPTER.**

**IT DID NOT ENTER A PROJECTION OF THE MANUSCRIPT, OF Volume 11, OR OF ANY LATER VOLUME, INTO ANY FILE.** The only projection in the outline is its expected-length band, which says on its face that it is a projection and not a measurement.

**IT NAMED NO NEW FINAL ENEMY AND NO NEW ANTAGONIST OF ANY KIND.** Iona Vey is the fixed antagonist position of `outline/series.md:101`, `outline/series.md:288` and `outline/ending.md`, and she is not new, and she is named nowhere in the outline as anything else.

**IT NAMED NO DEEP ARCHIVE, NO CARETAKER LINK AND NO SEEDHEART** outside the guardrail that forbids the three, and it minted no fifth word for the thing.

---

## 6. THE THREE STATE-LAYER EDITS THIS PASS MADE, AND WHAT IT DID NOT MAKE

**A FIGURE THAT IS ONLY OVERWRITTEN COMES BACK. THE WITHDRAWAL IS THE ONLY THING STANDING BETWEEN A WITHDRAWN FIGURE AND A PASS THAT READS IT AS LIVE. THE WRONG WEEKDAY IS LIVE AT THE HEAD OF THE ONE STATE FILE A PHASE IS REQUIRED TO READ WHOLE, SO LEAVING IT THERE UNRECORDED WOULD BE THE FAILURE AND NOT THE CAUTION.**

**ONE. A MARKED CORRECTION BLOCK WAS INSERTED AT THE HEAD OF `state/current.md`. NOTHING WAS DELETED AND NO EXISTING FIGURE WAS REPLACED.** It names the six wrong figures, gives the rule under each, and points at `outline/volume-11.md` section 2. **The head of that file already carries a marked block from the Volume 10 close, which is the precedent for this move and the reason it is an insertion and not a rewrite.**

**TWO. A MARKED SECTION WAS APPENDED TO `state/continuity.md`** carrying the day clock for days 704 to 752, the six corrections, and the standing of every floor at day 703, so that the next batch prompt reads the correction in the governing record and not only in the outline.

**THREE. A MARKED SECTION WAS APPENDED TO `state/open-threads.md`** carrying the thirty-five threads at day 703 with the Volume 11 chapter each is planned to advance in, and naming the two that may never be answered.

**WHAT THIS PASS DID NOT MAKE.** `state/chapter-summaries.md` was not appended to, because no chapter of Volume 11 exists and a chapter summary for a chapter that has not been written is a figure invented in advance. `state/phase-ledger.json` was not touched and is controller-owned.

---

## 7. THE OPEN ITEMS THIS PASS HANDS FORWARD, NAMED

1. **THE WEEKDAY OF DAY 703 AND THE FIVE THAT FOLLOW IT.** Corrected in `outline/volume-11.md` section 2 and named in the state layer. **Whoever reviews this outline should re-run the eight-row check against `outline/volume-10.md`'s table before believing it.**
2. **THE READ-ALOUD NUMERATOR IS `(day - 509) / 2` AND THIS PASS FIT IT FROM Volume 10's TWO CLOSING FIGURES.** It reproduces 73 of 129 at day 655 and 97 of 177 at day 703 exactly. **It was not found written as a formula on any page and it is a two-point fit, so a writer who finds a third figure that disagrees with it should bring the third figure back and not overwrite the two that agree.**
3. **THE READ-ALOUD DENOMINATOR CROSSES TWO HUNDRED ON DAY 727 AND THE THIRD-LAUNDER CROSSES ONE THOUSAND ON DAY 708.** Both are declared in the outline with the correct spellings. **Neither has been on a page in this manuscript and a writer who writes the crossing badly on the day will not know it was a crossing and will write it as muscle memory.**
4. **THE RUN IS READ ON TWENTY-FOUR MORNINGS AND NOT TWENTY-FIVE, AND THE VOLUME OPENS ON A MORNING THAT DOES NOT CARRY IT.** That is an inversion of Volume 10's first morning and it is declared as one.
5. **THE THIRD-LAUNDER DELTA IS KEPT RATHER THAN CHANGED, AND THAT IS THE FIRST VOLUME SINCE Volume 10 NOT TO TAKE A NEW ONE.** If a later close finds the run has gone above a figure this holding cannot say in one breath, that is the price of keeping it and the run has been in the low hundreds of figures for eleven volumes.
6. **THE THIRTY-FIVE THREADS ARE THIRTY-FIVE AND THE SIX THAT Volume 10 OPENED ARE NOT AMONG THE THIRTY-FIVE.** Volume 10's own close says so. They are carried in the outline and they are not counted into anything.
7. **THE OPERATOR HAZARD IS UNCHANGED AND RECORDED AND NOT ACTED ON** for the tenth time.

---

## 8. THE THREE-PART TEST, ONE LAST TIME, AND THE ONE-LINE VERSION

**THE CENTRAL PRESSURE ANSWERS Volume 10's NEXT QUESTION ON THE FIRST MORNING AND DOES NOT CLOSE A THREAD TO DO IT. THE FORTY-NINE ROWS OF THE CHAPTER-TO-DAY TABLE RECONCILE WITH THE DAY CLOCK ON EVERY COLUMN AND BOTH MONTH TURNS ARE IN THE RIGHT PLACE. EVERY FIGURE IN THE OUTLINE IS A MEASUREMENT, A PAGE, OR A PRINTED RULE, AND THE SIX THAT WERE NOT HAVE BEEN CORRECTED AND NAMED.**

**THE ONE-LINE VERSION: Volume 11 is planned as Chapters 491 to 539 on days 704 to 752 in five movements of ten, ten, ten, ten and nine, a sheet comes up the fen road with a date at the foot of it and the date is inside the month, most of the neighbours who signed the charter are still signed to the machine and that is the price of the freedom, the schedule is correct and the cut is real and the two are not put in one sentence, the woman who kept the gauges is a person and not a villain, the third launder keeps its delta because it is the only one of four that gives forty-nine distinct figures and crosses one thousand on a Sunday in Chapter 495, the window is in the two hundreds on all forty-nine mornings and every one of its spellings is printed because the volume behind this one spent nineteen chapters getting it wrong, the five ninth-day returns are derived from the nine-day cycle and not from an ordinal, neither ladder is in the day table and one of them does not open on a step that was never spent, Tova Reed's ear is permanent and is the first of four losses and none of the four is reduced, the manuscript measures 1,446,779 across 490 files and Volume 10 is closed at 141,223, and the single most expensive thing this pass had to do was correct six figures it was handed rather than copy them, four of which were the same mistake the volume behind this one made in a different series.**
