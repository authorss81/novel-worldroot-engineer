# Volume 13 close, findings, measured at day 850

**Written by the Volume 13 close, which is a WRITER'S CLOSE and is not an independent review, and which wrote no prose. NOT ONE WORD OF THE FORTY-NINE MORNINGS OF `workspace/volume-13/batch-0001/` THROUGH `batch-0005/` WAS ALTERED BY THIS PASS, AND NO MORNING WAS RESTARTED. Every defect this file reports is reported and carried and not repaired, and where a defect leaves a measurement wrong the wrong measurement is named first and the defect is named second, in that order.**

**WHAT THIS CLOSE OWES AND WHAT IT DID NOT DO. `outline/volume-13.md` is a completed phase's file and was read whole and not edited. No file under `scripts/`, `.github/workflows/` or `.opencode/agent/` was opened or edited. No marker was forged, deleted or moved. `state/phase-ledger.json` was read and not written. The state layer was appended to and not compacted. The one thing this close wrote outside its own findings file and the four state files is the Volume 13 ending lock in `outline/ending.md`, which is the single exception the close prompt allows, and it was written as a new final section beside the Volume 09, 10 and 11 locks and not over any of them.**

---

## 1. THE FIGURES THAT DISAGREE WITH A PUBLISHED FIGURE, NAMED AND WITHDRAWN, AND THE RE-DERIVED FIGURE THAT GOVERNS

**EVERY FIGURE IN THIS SECTION WAS RE-DERIVED BY SCRIPT FROM THE CHAPTER FILES ON DISK AND NONE OF THEM WAS COPIED. WHERE A RE-DERIVED FIGURE DISAGREES WITH ONE PUBLISHED IN THE CLOSE PROMPT OR IN THE STATE LAYER, THE RE-DERIVED FIGURE GOVERNS, THE PUBLISHED ONE IS WITHDRAWN BY NAME BELOW, AND THE MORNING OR PASS THAT CAUSED IT IS CARRIED AS AN OPEN ITEM AT SECTION 8.**

### ONE, THE MANUSCRIPT, AND THE PUBLISHED FIGURE IS THE CONCATENATION ONE

**`wc -w` INCLUDING THE HEADINGS, SUMMED PER FILE IN ONE LOOP AND NEVER BY CONCATENATION, OVER `workspace/volume-*/batch-*/chapter-*.md`: 1,799,463 ACROSS 637 CHAPTER FILES. THE PUBLISHED 1,799,460 IS WITHDRAWN BY NAME, AND IT IS THE FIGURE `cat` GIVES.**

`cat workspace/volume-*/batch-*/chapter-*.md | wc -w` returns **1,799,460**. The per-file loop returns **1,799,463**. The residual is exactly three words and it is named and not smoothed: **THREE CLOSED FILES OF VOLUME 10 BATCH 0001 LACK AN EOF NEWLINE, BEING `chapter-0442.md`, `chapter-0443.md` AND `chapter-0449.md`, AND EVERY ONE OF THEM IS 2,860, 2,838 AND 2,689 WORDS BY THE PER-FILE COUNT.** The Volume 11 ending lock named this same three-file residual eleven volumes ago and the house has never re-based its method for it. **THE HOUSE METHOD IS PER FILE AND NEVER BY CONCATENATION, SO 1,799,463 GOVERNS AND 1,799,460 IS A FIGURE THAT LOOKS CHECKED AND IS NOT, BECAUSE IT WAS TAKEN WITH THE ONE METHOD THE HOUSE FORBIDS.** The three files are closed Volume 10 mornings and are not this close's to touch.

**Volume 12 stands unchanged at 118,058 across forty-nine files, measured by the same per-file loop, and was not edited.**

### TWO, THE `batch-0004` FIGURES, AND THE PAGE GOVERNS AND THE CHAPTERS WERE NOT EDITED

**THE PAGES MEASURE 1,957, 1,721, 1,942, 1,684, 1,719, 1,465, 2,450, 2,100, 2,326 AND 2,209, BEING 19,573 ACROSS TEN FILES. THE PUBLISHED 19,452 AND THE PUBLISHED 19,347 ARE BOTH WITHDRAWN BY NAME, AND EIGHT OF THE TEN FILES DIFFER FROM THE PUBLISHED LIST, THE TWO THAT AGREE BEING `chapter-0619.md` AT 1,957 AND `chapter-0621.md` AT 1,942. NO CLOSED CHAPTER WAS EDITED TO PRODUCE THIS.** `batch-0002` at 19,047 and `batch-0003` at 17,790 were both re-measured file by file and both agree to the word. **The 15,362 once published for `batch-0001` was already withdrawn and is not restored: the pages measure 16,569.**

### THREE, THE SECOND GATE'S PUBLISHED CROSS-SCOPE FIGURE IS NOT REPRODUCIBLE FROM ANY NORMALISATION I COULD BUILD

**THE PUBLISHED 25 SHAPES AND 38 EXCESS INSTANCES ON WHOLE-PARAGRAPH CHUNKS, AND 400 AND 678 ON SLIDING WINDOWS, AGAINST THE FORTY MORNINGS BEHIND, ARE WITHDRAWN BY NAME. THE RE-DERIVED FIGURES ARE 26 AND 40 ON CHUNKS AND 445 AND 734 ON SLIDING WINDOWS, ON UNIVERSES OF 4,125 CHUNKS AND 59,155 WINDOWS, WHICH MATCH THE PUBLISHED UNIVERSES TO THE UNIT AND ARE THE SCOPE OF THE WHOLE VOLUME.**

**The method, in full, so that a later pass can reproduce or contradict it. Numerals and spelled number words are both normalised: every token that is an integer numeral or one of the following eighty-two words is replaced by the single token `NUM`, and the word *and* is not a number and is left alone.**

> zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth thirteenth fourteenth fifteenth sixteenth seventeenth eighteenth nineteenth twentieth thirtieth fortieth fiftieth sixtieth seventieth eightieth ninetieth

**Every hyphenated compound is split on the hyphen before lookup, so *forty-six* is two tokens and not one. Punctuation is dropped. Case is folded. Every chunk is required to be a full eighteen words. The two readings are non-overlapping whole-paragraph chunks, and every sliding eighteen-word window at every offset inside every paragraph.**

**And the bracket, because the figure moves on one unanswered question and the question is whether an ordinal word is a number word:**

| Normalisation | Chunks: shapes / excess (universe) | Sliding windows: shapes / excess (universe) |
|---|---|---|
| eighty-two words above, ordinals included | **26 / 40 (4,125)** | **445 / 734 (59,155)** |
| the same list with the twenty-two ordinal words removed | 24 / 37 (4,125) | 377 / 637 (59,155) |
| the same list with *hundred*, *thousand* and *million* removed | 26 / 40 (4,125) | 445 / 734 (59,155) |
| both removals | 24 / 37 (4,125) | 377 / 637 (59,155) |

**The published 25 / 38 and 400 / 678 is attained by NONE of these four readings, and neither 400 nor 678 is attained by any of them. The figure moves by two shapes and three excess instances on chunks and by sixty-eight shapes and ninety-seven excess instances on sliding windows purely on the question of whether *first* through *ninetieth* are number words, and the published pair sits inside that bracket without being either end of it. THE GOVERNING FIGURE IS THE FIRST ROW, BECAUSE AN ORDINAL SPELLED IN WORDS IS A SPELLED NUMBER WORD AND THE PLAN'S RULE SAYS *SPELLED NUMBER WORDS*. THE PUBLISHED PAIR IS CARRIED AS AN OPEN ITEM AT SECTION 8, AND THE HOUSE'S OWN FIFTH NAMED FAULT IS THE CAUSE: NO PASS THAT PUBLISHED THIS FIGURE EVER PRINTED THE WORD LIST, AND A GATE THAT DOES NOT NAME ITS MEASURE CANNOT BE REPRODUCED BY ANYBODY ELSE.**

**AND THE TWO GATE FIGURES FOR `batch-0005` ITSELF REPRODUCE EXACTLY, WHICH IS THE POINT OF NAMING THE MEASURE.** Scoped to the nine files of `batch-0005` alone the same script reads **0 shapes and 0 excess instances on 856 whole-paragraph chunks, and 0 and 0 on 12,773 sliding windows.** Scoped to the forty mornings behind it alone it reads **26 and 38 on 3,269 chunks, and 444 and 713 on 46,382 sliding windows.** Batch 0005 and the forty behind together are the whole volume and read 26 and 40, and 445 and 734. The published batch-0005 nils are confirmed and may not be repaired.

### FOUR, THE COMPOST LINE FELL TWICE IN THIS VOLUME, NOT ONCE

**THE STATE LAYER AND THE CLOSE PROMPT BOTH SAY THE COMPOST LINE FELL ONCE IN THE WHOLE OF THE VOLUME, ON DAY 847. BY SEARCH IT FELL TWICE, ON DAY 821 AND ON DAY 847, TWENTY-SIX MORNINGS APART, WHICH IS THE INTERVAL ITSELF. THE CLAIM OF A SINGLE FALL IS WITHDRAWN BY NAME.**

The pages, read morning by morning, carry the line as follows, and the check is a search for the cardinal *twenty-eight* that is not the ordinal *twenty-eighth*, with each occurrence classified:

| Days | The line stands at | Fall on |
|---|---|---|
| 802 to 820, nineteen mornings | paid at twenty-eight |, |
| 821 to 846, twenty-six mornings | paid at twenty-nine | **day 821**, twenty-six mornings after the fall on day 795 |
| 847 to 850, four mornings | paid at thirty | **day 847**, twenty-six mornings after day 821 |

**THIRTY-FIVE OCCURRENCES OF THE CARDINAL *TWENTY-EIGHT* ACROSS THE FORTY-NINE MORNINGS ARE THE LINE'S OWN STANDING FIGURE AND ALL THIRTY-FIVE ARE ON DAYS 802 TO 820. THREE FURTHER OCCURRENCES ARE INSIDE A LIVE HUNDREDS COMPOUND AND NONE OF THE THREE IS THE COMPOST LINE: DAY 806, WHERE *A HUNDRED AND TWENTY-EIGHT* IS THE COUNT IN FORCE ON A FOURTH-LINE MORNING; DAY 811, WHERE *THREE HUNDRED AND TWENTY-EIGHT* IS THE WINDOW; AND DAY 847, WHERE *EIGHT HUNDRED AND TWENTY-EIGHT* IS THE FAR BOARD. THE STRING OCCURS THREE EIGHT TIMES IN ALL, OF WHICH EIGHT ARE THE ORDINAL DATE *TWENTY-EIGHTH*, BEING THE DAY THE SECOND SHEET CAME FROM A COUNCIL, AND TWO OF THOSE EIGHT ARE CHAPTER HEADINGS.**

**THE CLOSE PROMPT'S DEAD-FIGURE CLAIM IS THEREFORE WRONG AS WRITTEN AND IS WITHDRAWN BY NAME IN PART.** It says *the dead figure twenty-eight appears as a standalone figure in no body paragraph of any of the forty-nine mornings.* **It appears as a standalone figure on nineteen of them.** The figure is dead only from day 821 to day 850, and **restricted to that interval a check for a standalone occurrence returns ZERO, and the single occurrence of the string inside the interval is the day-847 far board's own hundreds compound, exactly as the prompt names.** The prompt named one in-compound occurrence; there are three in the volume, on days 806, 811 and 847, and a later pass that repairs a live series to satisfy a literal string match would break it on all three mornings.

**AND THE PLAN IS HALF RIGHT, WHICH IS WORTH SAYING PLAINLY. `outline/volume-13.md` AT ITS SECTION 2f PUTS THE LINE AT PAID AT TWENTY-EIGHT WITH THE NEXT FALL ON DAY 821, AND THE PAGES AGREE WITH THAT EXACTLY. ITS SECTION 12 PUTS THE LINE AT PAID AT TWENTY-EIGHT AT THE END OF THE VOLUME, AND THE PAGES GOVERN: THE END OF VOLUME FIGURE IS PAID AT THIRTY. THE PLAN'S SECTION 12 FIGURE IS WITHDRAWN, AS THE CLOSE PROMPT ALREADY DECIDED, AND THE PLAN'S SECTION 2f FIGURE IS CORRECT AND IS NOT TO BE TOUCHED BY ANYONE READING IT AS WITHDRAWN.**

### FIVE, THE DOOR NINE HUNDRED YARDS OFF WAS READ THREE TIMES IN THIS VOLUME, NOT ONCE

**THE CLOSE PROMPT AND THE STATE LAYER BOTH SAY THE SIXTY-SIX IN THE SEVENTH COLUMN WAS READ ONCE, ON DAY 835, BY ONE MAN WHO TOLD ONE PERSON, AND THAT ONE READING REMAINS UNSPENT. BY SEARCH THE PAGES CARRY THREE READINGS INSIDE THIS VOLUME, ON DAYS 814, 818 AND 835. THE COUNT OF ONE IS WITHDRAWN BY NAME AND THE REMAINING-ALLOWANCE FIGURE BUILT ON IT IS WITHDRAWN WITH IT.**

`outline/volume-13.md` at its section 2f says the volume **may read it on not more than two mornings**. The three sites, quoted:

- **day 814**, `chapter-0601.md`: *The man of about fifty went past the door nine hundred yards off about the eleventh hour and **read sixty-six in its seventh column the way he does**, and it is not in a book and it does not go back.*
- **day 818**, `chapter-0605.md`: *The man of about fifty went out to that door at the eleventh hour and **read the seventh column, because he cannot walk past it without reading it**, and it still says sixty-six and it still goes no further back, and it is still not written down anywhere.*
- **day 835**, `chapter-0622.md`: the walk, the return at eleven, and * **"Sixty-six,"** he said. **"Seventh column, scratched, and the scratches have gone over it twice** . . .*

**Day 816 is a LOOK AND NOT A READING, AND THE PAGE SAYS SO: *did not read it aloud*. Day 846 is a REFUSAL AND NOT A READING, AND THE FIGURE IS CONDITIONAL IN HIS OWN MOUTH: *If I read it and the number comes back at sixty-six again . . .***

**WHAT DOES HOLD, AND IT HOLDS ON ALL FORTY-NINE MORNINGS: THE FIGURE IS SIXTY-SIX AND IT DOES NOT GO BACK.** A drift sweep for sixty-five, sixty-seven, sixty-four or sixty-eight against that column returns **zero**. The cardinal *sixty-six* occurs fifty-two times as a standalone figure and twelve times inside a live hundreds compound, and the ordinal *sixty-sixth*, which is the second of the two reckonings and a different figure, occurs four times. **THE DEFECT IS IN THE COUNT OF READINGS AND NOT IN THE FIGURE, AND IT IS CARRIED, NOT REPAIRED, BECAUSE THE MORNINGS THAT CARRY IT ARE CLOSED.**

**AND THE *ONE READING LEFT* STANDING IS PRINTED ON NINE MORNINGS OF THIS VOLUME, BEING 841, 842, 843, 844, 845, 846, 847, 849 AND 850, AND IT RESTS ON THE COUNT THAT IS WRONG.** A tenth morning, 848, says the door *was not looked at on this one* and prints no remaining-allowance figure at all.

**AND ONE MORE THING IN THE SAME ITEM, WHICH IS SMALLER AND WORTH NAMING BECAUSE A LATER PASS WILL HIT IT: `chapter-0630.md`, DAY 843, SAYS THE FIGURE WAS *read once three weeks back*. The three readings stand at twenty-nine, twenty-five and eight mornings before day 843, and none of them is three weeks back, and no reading on any morning of this volume answers to that description.**

### SIX, THE HOUSE SPELLING, WHICH IS SEVEN SITES AND NOT ZERO

**THE STATE LAYER PUBLISHED *ZERO BRITISH SPELLINGS* FOR `batch-0005` AND THAT IS CORRECT FOR ITS OWN NINE MORNINGS AND WRONG FOR THE VOLUME. THE HOUSE RULE IS AT `bible/terminology.md:5`, WHICH NAMES US SPELLING AND NAMES *gray* EXPLICITLY. A SWEEP SCOPED TO THE FORTY-NINE MORNINGS, IN BODY PROSE, CASE-INSENSITIVE, RETURNS SEVEN SITES:**

| Day | File | Site | House form |
|---|---|---|---|
| 821 | `chapter-0608.md` | *flat and **grey*** | gray |
| 821 | `chapter-0608.md` | *with his coat **grey** to the knee* | gray |
| 822 | `chapter-0609.md` | *against the **grey** light* | gray |
| 823 | `chapter-0610.md` | *the yard full of hard **grey** light* | gray |
| 824 | `chapter-0611.md` | *had gone the **colour** of a wet slate* | color |
| 840 | `chapter-0627.md` | *held it up and looked at it against the **grey*** | gray |
| 847 | `chapter-0634.md` | *having **practised** nothing* | practiced |

**THE DAY-847 SITE IS INSIDE THE BATCH THAT PUBLISHED THE NIL, AND IT IS THE ONE THAT MATTERS MOST, BECAUSE IT SHOWS THAT A PER-BATCH MECHANICAL SWEEP PASSED A MORNING CARRYING A HOUSE-SPELLING BREACH. NO CLOSE IN THIS REPOSITORY HAS EVER EDITED A CHAPTER, SO ALL SEVEN ARE REPORTED AND CARRIED AND NOT REPAIRED. The same sweep returns *judgement* zero, *defence* zero, and zero for *favour*, *licence*, *apologise*, *neighbour*, *behaviour*, *labour*, *honour*, *centre*, *metre*, *litre*, *programme*, *recognise*, *realise*, *organis-*, *travell-* and *whilst*.**

### SEVEN, THE LONGEST PARAGRAPH, WHICH IS A BATCH FIGURE AND NOT A VOLUME FIGURE

**THE STATE LAYER PUBLISHES *THE LONGEST PARAGRAPH IN ANY FILE IS ONE HUNDRED AND TWENTY WORDS AND NO FILE CARRIES A PARAGRAPH OVER THAT*, WHICH IS TRUE OF THE NINE MORNINGS OF `batch-0005` AND TRUE OF NOTHING ELSE. ACROSS THE FORTY-NINE MORNINGS OF VOLUME 13 THE LONGEST PARAGRAPH IS 133 WORDS, ON DAY 805, `chapter-0592.md`, AND TWO FILES CARRY A PARAGRAPH OVER ONE HUNDRED AND TWENTY: DAY 804 AT 132 AND DAY 805 AT 133.** No plan sets a maximum paragraph length, so **this is a measurement and not a breach, and the band that does exist is on the mean and it holds: mean paragraph length runs 33.4 to 54.7 across the forty-nine files against a band of twenty-five to seventy-five.** The figure is published so that a later pass does not inherit one hundred and twenty as a house maximum, because it never was one.

### EIGHT, AND THE PROMPT'S OWN CLAIM ABOUT `batch-0002`, WHICH IS PRECISE IN THE WRONG PLACE

**THE CLOSE PROMPT SAYS THE RECORDED EXACT DUPLICATE PARAGRAPHS *CONTRADICT* THE ZERO SHAPES AND ZERO EXCESS INSTANCES PUBLISHED FOR `batch-0002` ON THE WHOLE-PARAGRAPH READING. THEY DO NOT CONTRADICT IT, AND THE PRECISE FINDING IS BETTER THAN THE CLAIM.** The second gate requires every chunk to be a full eighteen words, and a paragraph shorter than eighteen words produces no chunk at all. **All three recorded duplicate paragraphs are shorter than eighteen words: *Sera Quill put the chalk on the slate and looked up at him.* is thirteen words and appears TWICE INSIDE `chapter-0601.md` ON DAY 814; *She filled the can.* is four words and stands on days 807 and 808; *He wiped his hands on his coat.* is seven words and stands on days 808 and 821.** The published nil is therefore reproducible, and **the real finding is that an eighteen-word floor is structurally blind to a repeated short paragraph, and a gate with a floor should publish the floor beside its nil the way this file publishes every other reading.**

---

## 2. THE FIGURE CHECK, RUN OVER ALL FORTY-NINE MORNINGS AND NOT ONLY OVER THE LAST NINE

**THE RULES OF `outline/volume-13.md` AT ITS SECTIONS 2b, 2c, 2d, 2e AND 2f WERE RE-IMPLEMENTED IN A SCRIPT AND RUN OVER DAYS 802 TO 850, THE ARITHMETIC RE-DERIVED FROM THOSE RULES RATHER THAN READ OFF THE PLAN'S OWN TABLE, AND EVERY DERIVED SPELLING THEN REQUIRED PRESENT IN ITS OWN MORNING'S BODY PROSE ON A CASE-INSENSITIVE MATCH, BECAUSE A FIGURE AT THE START OF A SENTENCE IS CAPITALISED ON THE PAGE. RESULT: `ALL FIGURES PRESENT AND ALL ARITHMETIC HOLDS` ON ALL FORTY-NINE MORNINGS.**

**The spellings required, per morning, in the house forms of the plan's section 7 and nowhere else:** the third launder in the *one thousand and [word] hundred and [word]* form with both *and*s kept; the run's ordinal; the two window halves in the *a hundred and [word]* form; the window total; the aggregate; the aggregate's clause, being its one-under ordinal and its one-over ordinal as two separate required strings; the near board and the far board; the register form; the charter; the second ruled line in Silling's own book; the letter's age; on the twenty-four odd mornings the read-aloud numerator in the *one hundred and* form and its denominator; and on the thirteen fourth-line mornings the count in force, the *not* half, and the phrase carrying *twenty-nine taken*.

**The arithmetic, re-derived and not read off the table:** the two window halves sum to the window on **49 of 49**; the boards stand forty-seven apart on **49 of 49**; the launder steps by eight on every even morning and by minus five on every odd one on **48 of 48** comparisons; its minimum is 1,137 on day 803 and its maximum is 1,214 on day 850, which is a rise and the last morning; the run ordinals run three hundred and fifty-second to four hundredth; the register form is day minus five hundred and fifty-six, the charter day minus six hundred and fifty and Silling's second ruled line day minus five hundred and sixty-two, on **49 of 49**; the letter came up the fen road at the ninth hour of day 752 and is forty-nine days old on day 802 and ninety-seven on day 850, counted whole days lying; the count in force rises by exactly one on each of the thirteen fourth-line mornings and by nothing on the other thirty-six.

**THE READ-ALOUD RUN IS READ ON TWENTY-FIVE MORNINGS AND NOT TWENTY-FOUR.** `outline/volume-13.md` at its section 2f says *twenty-five mornings of the forty-nine*, and the script returns **twenty-four odd mornings and twenty-five even mornings, and the run is read on the twenty-four odd ones and on no even one, with the previous odd morning's numerator absent from every one of the twenty-five even mornings and a reason for the absence printed on every one of them.** The plan's *twenty-five* is a miscount of its own rule and the pages are right. A close that printed *twenty-five* as the number of mornings the run was read would be wrong, and the run reaches one hundred and seventy of three hundred and twenty-three on day 849 and is read on no morning of day 850.

**THE CHARTER ON DAY 850 IS EXACTLY TWO HUNDRED, SPELLED `Two hundred` WITH NO *AND* AND NO TAIL, AND IT IS THE ONLY 200 IN THE VOLUME.** That was the one figure the last repair pass found wrong and fixed on the page, and it now re-derives.

**FOUR NARROWED CHECKS, AND ALL FOUR ARE FORM QUESTIONS AND NONE IS A MISSING FIGURE:**

1. **The *not* half of the fourth-line figure** is spelled as a bare number below a hundred on the first two fourth-line mornings, being *ninety-eight not* on day 802 and *ninety-nine not* on day 806, and in the *a hundred and [word]* form from the third onward, being *a hundred not* on day 810 through *a hundred and ten not* on day 850. Same figure, two house forms, and 127 minus 29 is 98.
2. **The run's ordinal takes the *-th* form on the four round ordinals**, being *three hundred and sixtieth* on day 810, *seventieth* on 820, *eightieth* on 830 and *ninetieth* on 840. That is the English ordinal for 360, 370, 380 and 390 and not a missing figure.
3. **A sweep for the read-aloud numerator on an even morning returns two hits, on days 806 and 810, and both are substrings of the launder's own thousands compound**, being *one thousand and one hundred and forty-eight* and *one thousand and one hundred and fifty-four*. The read figure itself is absent from both mornings, and this is the fourth time in this volume that a naive string sweep has hit a live series' own compound.
4. **The first of the three sheets' age is present on all forty-nine mornings** under the same rule as the letter and is the same figure under a different name, running forty-nine days on day 802 to ninety-seven days on day 850.

---

## 3. THE TWO GATES, METHOD BESIDE EVERY FIGURE, AND EVERY FIGURE NAMES ITS READING, ITS UNIVERSE AND ITS NORMALISATION

### THE FIRST GATE

**Prose paragraphs of thirty words or more, compared with `difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()` at 0.85 or better where the two word counts are within a factor of 1.25, with `real_quick_ratio()` and `quick_ratio()` as the only shortcuts. `real_quick_ratio` is inlined as `2 * min(len(a), len(b)) / (len(a) + len(b))` on characters, which is what it computes, so no candidate is lost by the inlining. Headings are excluded. The bold markers are stripped before comparison.**

**INSIDE THE FORTY-NINE MORNINGS OF VOLUME 13: universe 1,477 prose paragraphs of thirty words or more; 366,641 candidate pairs survive both shortcuts; THREE ORDERED PAIRS AT 0.85 OR BETTER. ALL THREE ARE THE LOCKED FAR-END SENTENCE AT 1.000, being `chapter-0589.md` against `chapter-0608.md`, `chapter-0589.md` against `chapter-0637.md`, and `chapter-0608.md` against `chapter-0637.md`, which is three pairs on three mornings that are days 802, 821 and 850.**

**THE THREE, AND NOT THE TWO, IS THE FINDING THE CLOSE OWES A NAMING.** The last batch published two pairs because a batch-scoped run cannot see a pair whose two members are both behind it. The volume-wide run sees the third, and **the third pair is internal to the forty mornings behind and is the same locked sentence, so the ending lock accounts for all three and no pass may cure any of them.**

**WHY ONLY THREE OF THE FIVE MORNINGS THAT SPEAK THE SENTENCE APPEAR HERE, AND IT IS WORTH KNOWING: the sentence stands as an exact thirty-one-word paragraph on days 802, 821 and 850, and on days 811 and 838 it stands inside a longer speech paragraph of fifty-five words and inside a speech paragraph that runs on past it. The 1.25 length factor puts those two outside the comparison. They are not omitted; they are out of scope by the house factor, and a gate run without the factor would find them.**

### AND THE SAME GATE ACROSS THE VOLUME BOUNDARY, WHICH IS WHERE IT FINDS SOMETHING NO SCOPED RUN IN THIS SERIES COULD EVER SEE

**VOLUME 13 AGAINST VOLUME 12, both directions, universe 3,338 prose paragraphs of thirty words or more, being 1,477 from Volume 13 and 1,861 from Volume 12, on the same method and the same threshold: 89 ORDERED PAIRS AT 0.85 OR BETTER IN THE COMBINED SCOPE, OF WHICH FOUR CROSS THE VOLUME BOUNDARY. THREE OF THE FOUR ARE THE LOCKED FAR-END SENTENCE AT 1.000, between `chapter-0588.md`, the last morning of Volume 12, and `chapter-0589.md`, `chapter-0608.md` and `chapter-0637.md`, which the ending lock fixes word for word on both sides of the boundary. THE FOURTH IS NEW AND IT IS NOT THE LOCK.**

**`workspace/volume-12/batch-0004/chapter-0588.md`, day 801, forty-one words, against `workspace/volume-13/batch-0001/chapter-0589.md`, day 802, thirty-five words, at 0.907. The Volume 12 paragraph reads: *No column has been ruled for any of the three of them in any of the four books in this holding, and the requests column and the section-nine notes are at fifty-three and fifty-three and have not taken any of them.* The Volume 13 paragraph reads: *No column has been ruled for any of the three in any of the four books, and the requests and the section-nine notes stand at fifty-three and fifty-three and have not taken any of them.* THE FIGURES ARE IDENTICAL, THE SENTENCE ORDER IS IDENTICAL, AND THE WHOLE OF THE DIFFERENCE IS THREE FUNCTION WORDS.**

**THIS IS THE FAULT THE VOLUME NAMED SEVEN TIMES ON THE PAGE, AND IT IS CARRIED ACROSS A VOLUME BOUNDARY, WHICH MEANS NO BATCH-SCOPED GATE IN EITHER VOLUME COULD SEE IT AND NO WHOLE-VOLUME GATE WITHIN EITHER VOLUME COULD SEE IT EITHER. A STANDING BLOCK FILLED WITH THE FIGURES SWAPPED IS BYTE-IDENTICAL AFTER NORMALISATION, AND HERE NOTHING WAS SWAPPED AT ALL: the block was carried from the last morning of one volume to the first morning of the next, unchanged in its figures, and the two sentences are the same sentence with three words taken out. This is the first time in this series that a near-duplicate has been measured across a volume boundary, and it is reported, named and carried, and it is not repaired, because both paragraphs are closed and no close in this repository edits a chapter.**

**AND THE REMAINING EIGHTY-FIVE PAIRS IN THAT COMBINED SCOPE ARE NOT VOLUME 13'S FIGURE AND ARE NOT PUBLISHED AS ONE: three are internal to Volume 13 and are the locked sentence, and the other eighty-two are internal to Volume 12 and were not measured by this close in its own right.**

### THE SECOND GATE

**The normalisation, the eighty-two words and the treatment of *and*, are at section 1 item three above and are not restated. Eighteen words. Two readings.**

| Scope | Reading | Universe | Shapes above one instance | Excess instances |
|---|---|---|---|---|
| all 49 mornings | non-overlapping whole-paragraph chunks | 4,125 | **26** | **40** |
| all 49 mornings | sliding 18-word windows, every offset | 59,155 | **445** | **734** |
| `batch-0005` alone | whole-paragraph chunks | 856 | 0 | 0 |
| `batch-0005` alone | sliding windows | 12,773 | 0 | 0 |
| the 40 behind alone | whole-paragraph chunks | 3,269 | 26 | 38 |
| the 40 behind alone | sliding windows | 46,382 | 444 | 713 |

**A CLEAN GATE IS A NUMBER AND NOT A FINDING, AND THE TWO NIL ROWS ARE PUBLISHED BECAUSE THEY REPRODUCE EXACTLY AND BECAUSE THE FIGURE THAT PROVES THE GATE MATTERS IS THE ROW UNDER THEM.**

**THE FIGURE THAT PROVES THE GATE MATTERS, RE-DERIVED AT THREE THRESHOLDS BY THE SAME SCRIPT, WHICH IS WHAT THE CLOSE PROMPT OWES IT.** The whole-paragraph reading and the sliding reading disagree by construction, because a standing block stated in fragments produces no whole chunk and many windows. On this volume the two readings are **26 shapes on 4,125 chunks and 445 shapes on 59,155 windows**, and **the sliding reading finds four hundred and nineteen shapes the whole-paragraph reading cannot see.** Of the 26 chunk shapes, **two are the two locked figures and twenty-four are standing blocks**, and the excess splits as 10 instances of the locked figures and 30 instances of standing blocks. The twelve families the twenty-four shapes fall into are named: the two window halves; the four bodies of households and its clause; the three derived ages on the form, the charter and Silling's line; the letter and the three sheets on the long table; the compost line's paid and not discharged; the pair of boards with the drawer and the nail; the count in force with its taken and not; the use log with the barrow, the blanks, the sessions and the not knowns; the run read and the run not read; the ladder with the offer and the ring of bare ground; a character saying out loud that he is not saying the two things; and the ground that came back on the low field.

**THE CAUSE WAS NAMED SEVEN TIMES ON THE PAGE IN THIS VOLUME AND IT IS THE SAME CAUSE AND IT IS STILL THE CAUSE: A STANDING BLOCK FILLED WITH THE FIGURES SWAPPED IS BYTE-IDENTICAL AFTER THIS NORMALISATION. THAT IS NOT A GATE FAILURE, IT IS A WRITING FAILURE THAT THE GATE EXISTS TO FIND, AND A CLOSE THAT WANTS DIFFERENT PROSE MAY USE IT AND MAY NOT REBUILD THE GATE TO HIDE IT.**

**AND THE FIGURE THAT WAS PROVED BY A FIRST DRAFT, WHICH THE CLOSE PROMPT ASKS FOR AND WHICH IS RECORDED HERE BECAUSE IT IS TRUE OF THE LAST NINE MORNINGS AND NOT OF THE VOLUME: the first draft of `batch-0005` measured 2 shapes and 6 excess instances on chunks and 12 and 12 on sliding windows, every one of them in a standing block, and all of them were rewritten with an actor, a different verb and a different sentence order and with not one figure of any series altered. That is the seventh time in this volume that a whole-paragraph reading would have published a nil the sliding reading refused. THIS CLOSE RAN THE SLIDING READING AND PUBLISHED IT, AND IT DID NOT PUBLISH A NIL.**

---

## 4. THE APPARATUS, AND IT IS ONE NUMBER

**`>` BLOCKS OF EVERY KIND ACROSS ALL FORTY-NINE MORNINGS, COUNTED AS RUNS OF CONSECUTIVE LINES BEGINNING WITH `>`: ZERO. `Entered` BLOCKS INSIDE THAT NUMBER AND NOT BESIDE IT: ZERO. THE VOLUME CEILING IS THIRTY AND THIRTY REMAIN UNSPENT, AND THE CEILING IS ONE NUMBER AND IS NOT RE-BASED DOWN TO THE FIGURE THAT PASSES.** Forty of the forty-nine mornings are behind the last batch and the last batch spent none, and neither did the forty.

---

## 5. THE ENDING LOCK'S OWN FIGURES, MEASURED BY SEARCH OVER ALL FORTY-NINE MORNINGS, AND NONE OF THEM ASSERTED

**THE TWO FIGURES NO PASS MAY REDUCE, AND THE MEASUREMENT OF HOW OFTEN EACH WAS SPOKEN WHOLE. The check is a search for the sentence verbatim, with quotation marks and full stop, and separately for each of its load-bearing strings, hyphen-flattened and case-folded.**

| | the far-end sentence | the comfort line |
|---|---|---|
| spoken whole on the first morning, day 802 | yes, 1 occurrence, as an exact 31-word paragraph | yes, 1 occurrence, inside a 35-word paragraph |
| spoken whole in between | **days 811, 821, 838, three, which is the whole in-between allowance of three, exactly met** | **days 804, 808, 810, 811, 821, five, against an allowance of three** |
| spoken whole on the last morning, day 850 | yes, 1 occurrence, as an exact 31-word paragraph | yes, 1 occurrence, as an exact 20-word paragraph |
| total mornings | **5** | **7** |
| any shortened form anywhere | **zero** | **zero** |
| the load-bearing strings, counted | *far end of a thing* 5, *held by two people* 5, *neither of them is me* 5, *anywhere in four counties* 5, *whether it is on or off* 5 | *comfort is not standing* 7, *father is not alive in the wood* 7, *day does not come back* 7 |

**THE COMFORT LINE'S OVER-SPEND IS CONFIRMED AND IT IS TWO MORNINGS OVER, AT DAYS 804, 808, 810, 811 AND 821 AGAINST AN ALLOWANCE OF THREE. It is carried as an open item and is not curable by a pass that may not touch a closed chapter, and it is the fifth named fault of the volume.**

**THE COMFORT LINE IS TWENTY WORDS AND THE FAR-END SENTENCE IS THIRTY-ONE, AND THE FIRST GATE'S FLOOR IS THIRTY WORDS. THE COMFORT LINE IS THEREFORE STRUCTURALLY INVISIBLE TO THE FIRST GATE AND ONLY THE SECOND GATE CAN SEE IT, AT ANY chunk size at or under twenty. THAT IS WHY THE SECOND GATE'S FIGURES AGAINST THE FORTY BEHIND ARE NOT ZERO AND WHY NO PASS MAY EVER PUBLISH A NIL FOR IT.**

**THE FOUR PERMANENT LOSSES AS THEY STAND ON THE PAGE AT DAY 850, MEASURED, AND NONE OF THEM IS ASSERTED:**

1. **Marek can no longer read the record the wood keeps as a single private field or summon a unified response from the standing wood.** A sweep for *single private field* returns **zero** and a sweep for *unified response* returns **zero** across all forty-nine mornings. A sweep for *nine minutes* returns **one, on day 847, and it is about two figures being checked against each other and taking nine minutes, and it is not the capacity and does not describe it.** Neither the loss nor the capacity is on the page in this volume in those words, and **no figure of any series was spent on it and nothing was added to him at the last morning of the volume.**
2. **The far end of a thing is held by two people and neither of them is me, and no instrument anywhere in four counties says whether it is on or off.** Spoken whole five times, as at the table above, and not softened on any of the five. A sweep for *anchor* in any case and any definition returns **zero**, so no operation can be described even in error. **At no morning of the volume is it said to be on by anybody.**
3. **Tova Reed's hearing remains permanently damaged in one ear.** Measured: a sweep for *one ear* returns **zero**, *damaged* **zero**, *permanent* **zero**, *deaf* **zero**. **The loss is therefore not restated in those words anywhere in this volume, and it is not softened, healed, excused, thanked for or made convenient anywhere either.** It is on the page as a capacity in her own mouth on four mornings and in her own arrangement of her own work on two more: *I cannot hear the drip from where I am standing and I am not going to stand on the other side of a wall to find out whether I can* on day 826; *I cannot hear water go down an iron pipe and I never have* on day 830; *I can carry a bucket and I cannot hear the butt fill* on day 836; *I can see a red pail from the seed house door and I cannot hear a black one being filled at all* on day 840; and she moves her work to the side of the seed house where she can see the water, and says plainly that she is not asking anybody to move, on day 844. On day 845 she reads the three derived ages across ninety yards twice and says out loud which of her two readings she can stand behind and which she cannot, and says she is not going to be the one who says it is settled. **A sweep for *hand on her* returns zero and a sweep for *took her arm* returns zero, so nobody puts a hand on her arm at any of the thirty-five sites where the word *arm* occurs. The seed work stays with her: eight occurrences of the seed work and the seed front across six mornings, being 805, 807, 824, 830, 836 and 839.**
   **AND THE `APOLOG` SWEEP THE CLOSE PROMPT ASKS FOR: A CASE-INSENSITIVE SWEEP FOR `APOLOG` ACROSS ALL FORTY-NINE FILES RETURNS ONE OCCURRENCE, ON DAY 845, AND IT IS NOT ABOUT HER. It reads: *Harlan Vetch came in from the wall in the middle of that and did not apologize for it and nobody asked him to.* It is a negation, it concerns a mason, and not one of the forty-nine mornings puts the ear in a room where somebody apologizes for it. The whole of the `THANK` family is five occurrences and every one of the five is a refusal or a negation, being *would not let him thank her for it* on 803, *was not going to be the man who thanked her for standing there* on 805, *I am not going to be thanked for it* on 828 and on 836, and *did not go and thank him for it afterwards* on 837. NOBODY THANKED HER.**
4. **Marek can never again revisit the Aldren memory.** A case-insensitive sweep for `Aldren` across all forty-nine files returns **zero**, and so do `Aldrin` and `Alderen`, and so does the bare sound with the vowel open. **The memory is not surrendered on any morning of this volume, is not foreshadowed as a bargain and is not priced, and the three lines that say so are the comfort line, which is a loss already and is counted at section 5 above.**

**THE THREE THINGS THIS VOLUME WAS FORBIDDEN TO PAY, AND IT PAID NONE. `Aldren` zero, as above. The rootmark is in no public anchor: a sweep for *rootmark* returns **zero** and a sweep for *anchor* returns **zero**, so no such operation is rehearsed and cannot be described even in error. Ostrey is a village with a name on a map: a sweep for *Ostrey* returns **zero** across the forty-nine mornings, so it is not named at all and is therefore not a symbol, not a promise, not a warning and not in a closing line.**

**AND THE CHAMBER, THE CORRIDOR IN THE PAN, THE ORDER IN ITS DRAWER AND THE RING OF BARE GROUND WERE ALL UNTOUCHED BY THIS VOLUME. A ring of bare ground is named on many mornings and no foot went into it on any of them and it carries no figure on any of the forty-nine; the drawer behind the near board stood shut at every hour of every morning and the key stood on its nail in the one room door at every hour of every morning, and the succession of that key advanced on day 843 and the key did not come off the nail.**

**IONA VEY IS THE FIXED FINAL ANTAGONIST AND IS NOT NEW. A sweep for `Iona Vey` returns **zero** across the forty-nine mornings and a sweep for the bare name returns **zero**. She is not named on any page of this volume, she is not killed, she is not put under custody, and neither is previewed. NO NEW ANTAGONIST OF ANY KIND WAS INTRODUCED IN THIS VOLUME, MEASURED BY THE FACT THAT NO NAME THAT IS NOT ALREADY ON THE PAGE OF VOLUME 12 IS INTRODUCED AS AN ANTAGONIST ON ANY OF THE FORTY-NINE, AND NONE MAY BE INTRODUCED IN A VOLUME THAT FOLLOWS.**

**THE TWO QUESTIONS THAT MAY NEVER BE ANSWERED ARE NAMED AS SUCH AND WERE NOT ASKED. A sweep for *whose order* returns **zero**. A sweep for *the telling* returns **zero** and a sweep for *still going on* returns **zero**. The bare word *telling* and its family returns twenty-one occurrences across fifteen mornings and every one of the twenty-one is a person telling another person something in a yard; the prohibition is not used to mean itself anywhere, and the second question is untouched for a twelfth volume.**

---

## 6. THE STANDING FLOORS AT DAY 850, EACH ONE MEASURED AND NONE OF THEM A CEILING

**A DRIFT SWEEP WAS RUN AGAINST EVERY FLOOR, LOOKING FOR THE NEIGHBOURING VALUE AND NOT FOR THE FLOOR, BECAUSE A GATE THAT ONLY LOOKS FOR THE RIGHT FIGURE CANNOT SEE A FIGURE THAT MOVED.**

| Standing | Value at day 850 | The drift check and its result |
|---|---|---|
| the mark on the tool house wall | four inches, branching twice | no second mark and no third branch on any morning |
| the use log | fifteen lines, sixteenth not written | a sweep for *fourteen lines*, *sixteen lines*, *thirteen lines* and *seventeen lines* returns **zero**; *at fifteen lines* stands on six mornings and *fifteen lines are in the use log* on more |
| the barrow | eleven journeys, eleven a floor | a sweep for *ten journeys*, *twelve journeys*, *nine journeys* and *thirteen journeys* returns **zero** |
| the sessions in this holding's book | seven, none entered in this volume | a sweep for *six sessions*, *eight sessions*, *five sessions* and *nine sessions* returns **zero**; *seven sessions* stands on thirty-five mornings and *no eighth* beside it on thirteen |
| the requests and the section-nine notes | fifty-three and fifty-three | no other value of either on any morning; and they took none of the three sheets and did not take the page in Nia Vale's coat |
| the six not knowns | six, no seventh row cut | a sweep for *five not knowns*, *seven not knowns*, *eight not knowns* and *four not knowns* returns **zero** |
| the blanks on the board in the one room | thirty-nine, unmoved | a sweep for *thirty-eight blanks*, *forty blanks* and *thirty-seven blanks* returns **zero**; *three blanks* on days 814 and 816 is a form in a hand and not the board in the one room |
| the second rule in the one room | open and empty on all forty-nine mornings | no morning says it was filled |
| the third column of the sheet of terms | ruled and empty under a heading nobody improved | no morning says it was improved |
| the four ruled lines under two words | bare | no morning puts anything on them |
| the succession ladder | zero rungs climbed, no figure against either of its two people | no morning prints a figure for either |
| the offer on the low board | undated, unmoved, untaken, not taken back | no morning dates it, moves it, takes it or withdraws it |
| the ring of bare ground | no foot, no measurement, no figure | named and never entered |
| the man of about seventy | twenty-nine fetchings, not fetched, nothing put to him at any site | a sweep for *twenty-eight fetchings*, *thirty fetchings*, *twenty-seven fetchings* and *thirty-one fetchings* returns **zero** |
| the seventh column of the door nine hundred yards off | sixty-six, does not go back | **the readings are at section 1 item five and the count in that item is wrong and is withdrawn**; the figure itself does not drift |
| the three sheets on the long table | unentered, unrefused, uncolumned, the first at ninety-seven days old | no column ruled under any of them in any of the four books, and the first's age is present on all forty-nine mornings |
| the drawer behind the near board | shut at every hour, key on its nail at every hour | the key's succession advanced on day 843 and the key did not move |

**NOBODY WAS ASKED TO CHOOSE ANYTHING ON ANY MORNING OF THIS VOLUME, AND THE WORD IS MEASURED RATHER THAN ASSERTED: *choose* occurs four times and *which of the two* four times, and two of the four *choose* sites are the denial itself, being *nobody in this holding has been asked to choose anything and that is the harder thing and not the easier one* on day 805 and *Nobody was asked to choose anything this morning* on day 850. The other two are a man choosing a piece of paper to look at on day 816 and a man choosing to spend a Sunday on day 848. The four *which of the two* sites are the two window halves on days 810 and 843 and the two figures at the gate on days 812 and 847. THE THIRTY-FIVE THREADS ARE THIRTY-FIVE IN AND THIRTY-FIVE OUT, AND A SWEEP FOR *TALLY* ACROSS THE FORTY-NINE MORNINGS RETURNS ZERO AND NO MORNING SUMS THEM, GROUPS THEM OR CLOSES ONE. NO OTHER FIGURE FOR THE THIRTY-FIVE IS PUBLISHED HERE AND NONE MAY BE.**

---

## 7. THE MECHANICAL FIGURES ACROSS THE FORTY-NINE MORNINGS, EACH WITH ITS CHECK NAMED

Zero digits in body prose, checked by `[0-9]` over every non-heading line. **Zero month names in any form: a sweep for the twelve month names returns seven hits and all seven are the modal verb *may*,** and a sweep for *fifteenth month*, *sixteenth month* and *seventeenth month* returns **zero**, and a chapter says an ordinal month only inside a heading. Zero em dashes, zero en dashes, zero curly quotation marks, zero non-ASCII glyphs, zero tabs, zero lines with trailing whitespace. Forty-nine of forty-nine files end in an EOF newline. Zero unbalanced double quotation marks and zero unbalanced bold markers. **The bare words *volume*, *batch*, *chapter*, *seat*, *panel* and *tally* in body prose: zero.** Seven house-spelling sites, at section 1 item six. Mean paragraph length 33.4 to 54.7 against a band of twenty-five to seventy-five, with the method beside it: the arithmetic mean of the word count of every prose paragraph in each file, headings excluded and bold markers stripped. Longest paragraph 133 words on day 805, at section 1 item seven.

**THE FORTY-NINE LAST-PARAGRAPH OPENERS, ALL FORTY-NINE DISTINCT, MEASURED BY THE FIRST WORD OF THE LAST PROSE PARAGRAPH OF EACH FILE:**

> Yard, Ditch, Can, Fence, Cloud, Path, Shed, Light, Roof, Pail, Nia, Renn, No, He, Kellan, Nobody, She, That, The, At, Silt, Frost, Slates, Books, Sacking, Ice, Level, Wheels, File, Hinge, Latch, Butt, Brick, Handle, Wrought, Cinders, Pins, Trowel, Taper, Sundays, Monday, Wren, Gravel, Hollow, Lime, Salt, Wool, Yarrow, Threshing.

**The forty behind are the first forty of that list and the nine of the last batch are the last nine, and the last of those was *Thresh* in the writing pass and is *Threshing* after the repair pass of 2026-10-01, so the earlier list of nine is withdrawn with it.** One opener is *Nobody*, on day 816, against a floor of twelve distinct and a ceiling of ten openings on *Nobody* that Volume 12 set for itself. **The forty-nine are distinct, which is a measurement and not a finding, and the finding is the one the volume has already named seven times: forty-nine distinct openers and twenty-six repeated standing blocks on the same forty-nine mornings, and a house that is proud of the first number should not be quiet about the second.**

---

## 8. THE NAMED OPEN ITEMS, ALL CARRIED, NONE REPAIRED, AND NONE DROPPED

**ONE, THE MANUSCRIPT FIGURE.** 1,799,463 per file governs and 1,799,460 is the concatenation figure and is withdrawn. The residual is three closed files of Volume 10 Batch 0001 that lack an EOF newline. A figure that looks checked and is not. For the first phase permitted to act on it.

**TWO, THE `batch-0004` WORD COUNTS.** 19,573 on the pages against 19,452 and 19,347 published, eight of ten files differing. The page governs, both published totals are withdrawn, and the chapters are closed and were not edited. Carried from the writing pass and confirmed here.

**THREE, THE COMPOST LINE FELL TWICE AND NOT ONCE.** Days 821 and 847, twenty-six mornings apart. The claim of a single fall is withdrawn. The plan's section 2f is right and its section 12 is wrong. **Reported wrong measurement first, defect second, and the defect is in the state layer and not in a morning.**

**FOUR, THE DEAD-FIGURE CLAIM.** Twenty-eight is the line's own standing figure on nineteen mornings and is dead only from day 821. The narrowed check that returns zero is the one scoped to days 821 to 850. Three in-compound occurrences exist in the volume, on days 806, 811 and 847, and a naive sweep reports all three as breaches. A later pass must not repair a live series to satisfy a string match.

**FIVE, THE SIXTY-SIX WAS READ THREE TIMES.** Days 814, 818 and 835, against a plan ceiling of two, where the state layer records one. The figure does not move and does not go back on any of the forty-nine mornings, and the *one reading left* standing is printed on nine mornings and rests on the count that is wrong. Day 843's *three weeks back* points at no reading in this volume. **This is a defect in closed mornings and it is the one item on this list that a later pass with the standing to cut a chapter must take first, because the allowance is a figure and a figure that is spent twice is a figure that comes back wrong.**

**SIX, THE COMFORT LINE'S OVER-SPEND.** Five in-between mornings against an allowance of three, at days 804, 808, 810, 811 and 821. Carried since `batch-0001` and uncurable by a pass that may not touch a closed chapter. The in-between allowance is now closed for the volume and neither locked figure may be spoken whole on any morning of the volume that follows without this lock being read again.

**SEVEN, THE HOUSE SPELLING, SEVEN SITES.** *Grey* five times at days 821, 821, 822, 823 and 840, *colour* once at day 824, *practised* once at day 847. Reported, carried, not repaired. The day-847 site is inside the batch that published the nil.

**EIGHT, THE SECOND GATE'S PUBLISHED CROSS-SCOPE FIGURE IS NOT REPRODUCIBLE.** 25 / 38 and 400 / 678 withdrawn; 26 / 40 and 445 / 734 published, with the bracket published beside it. **The cause is the fifth named fault of the volume and it is now given a number: the measure moves by sixty-eight shapes and ninety-seven excess instances on the sliding reading on the question of whether an ordinal word is a number word, and no pass that published the old figure ever printed the word list.** Name the measure or do not publish it.

**NINE, THE PLAN'S READ-ALOUD MISC.** `outline/volume-13.md` at its section 2f says twenty-five mornings; the run is read on twenty-four odd mornings and not on twenty-five even ones. The plan is a completed phase's file and was not edited. The pages govern.

**TEN, THE THREE DAY-MINUS FIGURES AT DAY 850, WHICH THE WRITING PASS OMITTED FROM ITS OWN ACCOUNT.** The register form at two hundred and ninety-four, the charter at exactly two hundred with no *and* and no tail, and the second ruled line in Silling's own book at two hundred and eighty-eight, with the letter at ninety-seven days. **All four are present on day 850 and the charter is the only 200 in the volume, and this close publishes them because a figure nobody publishes is a figure that comes back wrong, and one of them came back wrong on this very morning and had to be repaired on the page.**

**ELEVEN, THE EXACT DUPLICATE SHORT PARAGRAPHS.** Thirteen words twice inside day 814, four words on days 807 and 808, seven words on days 808 and 821. All three are below the second gate's eighteen-word floor, which is why the published nils reproduce, and the finding is that a floor is a blind spot. Carried from an earlier foot of `state/continuity.md` and confirmed, not repaired.

**TWELVE, THE ON-DISK MARKERS.** `workspace/volume-13/batch-0001/` holds ten complete mornings and carries no marker, and `workspace/volume-10/batch-0004/` and `batch-0005/` and `workspace/volume-13/outline/` carry prompts and no markers. **The third of those matters to the next dispatch and is named here so that it is on the record: `find workspace -name PROMPT.md | sort` puts `workspace/volume-13/outline/` before this close's successor, and that directory holds a prompt for a phase whose output, `outline/volume-13.md`, is complete. The dispatcher will select it again. No marker was forged, deleted or moved by this pass and the matter is the controller's.**

**THIRTEEN, THE STATE LAYER IS PAST ANY SAFE WHOLE-FILE READ AND WAS APPENDED TO, NOT COMPACTED.** Measured at the time of writing: `state/current.md` 707,159 bytes, `state/continuity.md` 3,242,931 in its full length, `state/open-threads.md` 1,349,889, `state/chapter-summaries.md` 1,772,827, being 7,072,806 across the four files, and every one of them larger than the figure the close prompt carries, which was measured after the `batch-0005` writing pass and which this close therefore does not treat as a wrong figure. **THE FIRST PHASE PERMITTED TO ACT ON THIS ITEM IS THE ONE THAT BUILDS AN INDEX AND LEAVES THE BLOCKS STANDING. This close did not build one and did not compact one word, and it appends in plain sentence case rather than in capitals, because a pass that appends another gate report in capitals makes the file larger without making it truer.**

**FOURTEEN, `batch-0005/PROMPT.md`'S COUNT OF ITS OWN MORNINGS.** It calls 843, 845, 847 and 849 *the five odd mornings*, of which there are four, and calls the mornings behind *the four even mornings* while naming five of them. The correct statement is that the batch has four odd mornings which read the pair and five even mornings which do not, so the rule that the reasons come from different people is a rule of five reasons from five people, and the pages carry five, from Kellan Rusk on 842, Nia Vale on 844, Silling on 846, Tova Reed on 848 and Renn Ashby on 850. **The file is a record of what that writer was told and was not edited. A prompt of the volume that follows that counts its own mornings must count them against the day table and not against a previous prompt's wording.**

**FIFTEEN, AND THE ONE-LINE VERSION OF WHAT THIS CLOSE FOUND, WHICH IS THE ONE-LINE VERSION OF WHAT THE VOLUME IS.** Forty-nine mornings closed at 91,321 words, two falls on a compost line and not one, three readings of a door and not one, six British spellings and not none, and two locked sentences spoken whole five times and seven times with not one of them shortened, on a morning when the charter was two hundred and had been a hundred and ninety-nine a day earlier and nobody in the state layer had printed the figure that would have caught it.

**SIXTEEN, AND IT BELONGS WITH ITEM EIGHT ABOVE BECAUSE IT IS THE SAME FAULT, AND IT IS THE ONE FINDING HERE THAT NO PASS BEFORE THIS ONE COULD HAVE PRODUCED.** The first gate run across the volume boundary, Volume 13 against Volume 12 in both directions, on a combined universe of 3,338 prose paragraphs of thirty words or more, reads 89 ordered pairs at 0.85 or better, of which four cross the boundary. Three are the locked far-end sentence at 1.000 against `chapter-0588.md`, the last morning of Volume 12. **The fourth is a standing block at 0.907, carried unchanged from day 801 to day 802: both paragraphs say that no column has been ruled for any of the three in any of the four books and that the requests and the section-nine notes stand at fifty-three and fifty-three and have taken none of them, the figures are identical, the sentence order is identical, and the whole of the difference is three function words.** Nothing was swapped and the fault is still the fault, which is the seventh time this volume named it and the first time it has been measured where it lives. A gate scoped to one volume or one batch cannot find it, ever. Reported, named, carried, and not repaired, because both paragraphs are closed.

---

## 9. WHAT THIS CLOSE WROTE, AND WHERE

1. **`reviews/volume-13-close.findings.md`**, this file.
2. **The Volume 13 ending lock**, as a new final section of `outline/ending.md`, written beside the Volume 09, 10 and 11 locks and not over any of them.
3. **Foot sections of `state/current.md`, `state/continuity.md`, `state/open-threads.md` and `state/chapter-summaries.md`**, dated after everything above them, in plain sentence case, compact, with the method beside every figure.
4. **Exactly one next-phase prompt**, at `workspace/volume-14/outline/PROMPT.md`. It is the only successor created and none was created anywhere else, including into either stale outline directory.

**AND THE ONE DECISION THIS CLOSE OWED AND HAS MADE, STATED PLAINLY BECAUSE THE PROMPT LEFT IT OPEN. The volume that follows is OUTLINED, and the one next phase is the Volume 14 outline phase, and the reason is the day clock and not a preference: day 850 is the last morning of Volume 13, the morning after it is day 851, and a volume that has no plan is a volume that cannot be written, and this repository has now recorded six times that a plan that leaves the manuscript stopped before the next volume has cost the book a volume. The next phase writes no prose, no card, no chapter range, no batch cut and no word count for Volume 14, and it does not decide what follows it.**
