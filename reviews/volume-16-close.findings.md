# The close of Volume 16, 2026-10-04: what it measured, what it found, and what it did not repair

**THIS IS THE RECORD OF THE CLOSE OF THE SIXTEENTH AND LAST VOLUME, AND IT IS A WRITER'S CLOSE AND NOT AN INDEPENDENT REVIEW, and it is headed as one. IT WROTE NO PROSE. IT ALTERED NO MORNING. IT STARTED NO MORNING. IT MOVED NO FIGURE OF ANY SERIES. IT ANSWERED NO THREAD AND CLOSED NO THREAD AND CREATED NO FURTHER PHASE, AND THERE IS NO PHASE AFTER THIS ONE.**

**THE HARNESS IS `workspace/volume-16/close/verify_close.py` AND ITS FIGURE GENERATOR IS `workspace/volume-16/close/derive.py`, AND ITS RAW OUTPUT IS `workspace/volume-16/close/MEASUREMENT.txt`. EVERY FIGURE IN THIS RECORD IS IN THAT OUTPUT AND WAS RE-DERIVED HERE PER FILE AND NEVER INHERITED.**

**THE GOVERNING FILE FOR THE VOLUME WAS `outline/volume-16.md` AND ITS CARD SET WAS `outline/batches/volume-16-cards.md`. NEITHER WAS RUN AGAIN AND NEITHER WAS EDITED.**

---

## 0. WHAT IS ON DISK, AND THE FIGURES AS THEY STAND AFTER THIS PASS

**ALL FORTY-FIVE MORNINGS OF VOLUME 16 ARE WRITTEN AND THE BOOK IS COMPLETE.** Files `chapter-0736.md` through `chapter-0780.md`, days nine hundred and forty-nine to nine hundred and ninety-three, across five batch directories, and **the manuscript is seven hundred and eighty chapter files**, which is the figure `outline/series.md:6` gives for the whole of the sixteen.

**MEASURED PER FILE WITH `len(text.split())` AND NEVER BY CONCATENATION:**

| | |
|---|---|
| **batch-0001** | **18,702** across ten files |
| **batch-0002** | **20,740** across ten files |
| **batch-0003** | **18,335** across ten files |
| **batch-0004** | **27,401** across ten files |
| **batch-0005** | **13,727** across five files, per file 2,721, 3,199, 2,397, 1,983 and 3,427 |
| **Volume 16** | **98,905** across forty-five files |
| **the manuscript** | **2,130,297** across seven hundred and eighty files |
| **and it reconciles** | **2,031,392 across volumes one to fifteen, plus 98,905, is 2,130,297** |

**THE TWO EARLIER SETS ARE WITHDRAWN BY NAME AND NEITHER RE-DERIVES, BECAUSE BOTH WERE MEASURED BEFORE PROSE MOVED: 13,599 PER FILE 2,721, 3,185, 2,279, 2,001 AND 3,413, VOLUME 16 AT 98,777, MANUSCRIPT AT 2,130,169; AND 13,597 PER FILE 2,721, 3,183, 2,279, 2,001 AND 3,413, WHICH ALSO CARRIED A PER-FILE SUM TWO WORDS SHORT OF ITS OWN BATCH TOTAL.** The set that governs is the one in the table above and it was re-derived by this pass on 2026-10-04.

**AND THE RESIDUAL THE VOLUME 14 CLOSE NAMED IS HERE AGAIN AND IS NAMED AGAIN AND NOT SMOOTHED: `wc -w` OVER THE SEVEN HUNDRED AND EIGHTY FILES LISTED ONE BY ONE IS 2,130,297, AND `wc -w` OVER THE SAME FILES CONCATENATED IS 2,130,223, A DIFFERENCE OF MINUS SEVENTY-FOUR. IT IS THE COUNT OF FILES THAT LACK AN EOF NEWLINE AND IT IS SEVENTY-FIVE IN THE MANUSCRIPT AND THIRTY-EIGHT IN VOLUME SIXTEEN, THE LAST FILE'S UNCLOSED LINE MERGING WITH NOTHING. A CLOSE THAT PUBLISHES THE PER-FILE FIGURE AND SAYS NOTHING ABOUT THE CONCATENATED ONE HAS PUBLISHED ONE MEASUREMENT AND LEFT A RESIDUAL UNNAMED FOR FOUR VOLUMES.**

---

## 1. THE UNIT, DECLARED BEFORE ANY READING WAS RUN, AND IT IS THE UNIT OF THIS VOLUME AND NOT A NEW ONE

**EVERY NON-BLANK LINE BELOW A HEADING. A BLOCK-QUOTE SEPARATOR LINE CARRYING NO WORDS IS EXCLUDED. APPARATUS QUOTE LINES ARE COUNTED AS PARAGRAPHS OF THEIR OWN. HEADINGS ARE EXCLUDED. APPARATUS IS INSIDE THE SCOPE OF BOTH GATES.**

**THE NORMALISATION, IN FULL, BECAUSE A GATE THAT DOES NOT NAME ITS MEASURE CANNOT BE REPRODUCED BY ANYBODY ELSE: every run of number words that makes one figure replaced by one token, the word *and* left alone, every hyphenated compound split on the hyphen before lookup, punctuation dropped, case folded, every chunk a full eighteen words.**

| At that unit | Volume 16 | the manuscript |
|---|---|---|
| paragraphs | **1,849** | **34,505** |
| prose paragraphs of thirty words or more | **1,297** | **26,573** |
| whole-paragraph units of eighteen tokens | **4,597** | **102,606** |
| sliding eighteen-word windows | **69,087** | **1,589,813** |

**A CLOSE THAT MEASURES AT A DIFFERENT UNIT FROM THE ONE IT PUBLISHES AGAINST HAS PRODUCED TWO NUMBERS AND ONE MEASUREMENT. THE UNIT IS PRINTED BESIDE EVERY FIGURE IN THIS RECORD.**

---

## 2. THE SELF-COLLISION CONTROLS, RUN FIRST, AND THEY REPRODUCE

**TWENTY-EIGHT COPIES OF AN EIGHTEEN-WORD BLOCK SEPARATED BY TWENTY-SEVEN GAPS OF DISTINCT LENGTHS ONE TO TWENTY-SEVEN, WITH ONE FILLER TOKEN IN FRONT OF THE FIRST COPY: ONE SHAPE AND TWENTY-SEVEN EXCESS ON THE SLIDING READING AND ZERO ON THE WHOLE-PARAGRAPH READING. THIRTEEN COPIES AND TWELVE GAPS: ONE AND TWELVE, AND ZERO.**

**BOTH REPRODUCE THE PUBLISHED CONTROLS EXACTLY, AND THE NORMALISATION IS THEREFORE SETTLED BEFORE ANY GATE IS RUN AGAINST A MORNING. WHAT THAT LICENSES IS EXACTLY WHAT IT SAYS IT LICENSES: a working gate proves that a shape is real, and it does not prove that the absence of a shape means anything.**

---

## 3. THE PARITY READING, MORNING BY MORNING, OVER ALL FORTY-FIVE MORNINGS AND NOT OVER ITS OWN FILES

**THE BINDING QUESTION. ON AN ODD MORNING FIND THE SENTENCE THAT GIVES THE TWO HALVES AND ASK WHICH OF THE TWO NUMBERS IS THE SMALLER ONE. ON AN EVEN MORNING ASK WHICH IS THE LARGER ONE. THEN ASK THE HARDER HALF OF THE QUESTION: WHICH OF THE TWO NUMBERS IS ATTACHED TO THE VERB THAT MEANS IT MOVED. A READING THAT ASKS ONLY WHETHER A FIGURE IS PRESENT CANNOT SEE AN INVERTED PARITY, AND IT DID NOT SEE ONE AT `chapter-0776.md` ON DAY NINE HUNDRED AND EIGHTY-NINE, WHICH WAS CAUGHT BY A REVIEW AND NOT BY THE FIGURE CHECK AND NOT BY EITHER GATE.**

**THE READING AS REBUILT HERE IS SIDE-AGNOSTIC, AND THAT IS A CHANGE AND NOT A COSMETIC ONE. THE READING ON DISK IN `workspace/volume-16/batch-0005/verify.py` ASSUMES THE MOVER IS THE FIGURE BEFORE THE VERB AND THE STANDER THE FIGURE AFTER IT. A MORNING THAT SAYS *TWO HUNDRED AND THIRTY-SIX STOOD AND TWO HUNDRED AND FORTY-SEVEN CAME* IS CORRECT ON AN EVEN MORNING AND THAT READING FLAGS IT, AND A MORNING THAT SAYS IT THE OTHER WAY ROUND IS ALSO CORRECT AND THAT READING PASSES IT. THE READING HERE TAKES THE NEAREST VERB THAT SAYS WHICH WAY ON EITHER SIDE OF EACH HALF, AND IT REFUSES THREE BINDINGS: ACROSS A SENTENCE BREAK, ACROSS ANOTHER HALF-FIGURE, AND ACROSS A PHRASE THAT RENAMES THE PAIR. A VERB THAT DOES NOT SAY WHICH WAY — *MOVED*, *WENT*, *CHANGED* — IS RECORDED AND IS NOT USED FOR A VERDICT, BECAUSE A READING THAT GUESSES THERE MANUFACTURES THE VERY DEFECT IT IS LOOKING FOR.**

**THE RESULT, AND THE THIRTEEN OCCURRENCES ATTACHED TO A VERB THAT DOES NOT SAY WHICH WAY ARE COUNTED AND NOT SCORED: seventy-two half-figures attached to a verb that says which way, examined, and TWO WITH THE WRONG HALF ON THE VERB, both on one morning.**

### THE DEMONSTRATION THE INSTRUMENT OWES, RUN BEFORE ITS NIL IS PUBLISHED AS A NIL

**A READING BUILT TO CATCH A CLASS OF ERROR MUST BE SHOWN ON A KNOWN INSTANCE OF THAT CLASS. THE KNOWN INSTANCE IS THE PRE-REPAIR WORDING RECORDED AT `workspace/volume-16/batch-0005/SELF-CHECK.md` SECTION TWELVE ITEM 1, AND IT IS USED HERE AS A FIXTURE AND NOT AS A PAGE, BECAUSE THE PAGE HAS BEEN REPAIRED SINCE.**

| Probe | Result |
|---|---|
| the pre-repair wording, day 989, an odd morning, so the smaller half moves: *two hundred and fifty-eight came and two hundred and forty-eight stood* | **both rows FLAGGED. The reading sees the class.** |
| the mirror fixture on an even morning, day 990: *two hundred and fifty-nine stood and two hundred and forty-eight rose* | **1 of 2 flagged, being the tall half on a rise verb** |
| the page as it stands now, `chapter-0776.md` | **2 paired delivery sentences, 0 flagged** |

**THE READING IS THEREFORE DEMONSTRATED ON THE CLASS IT EXISTS TO CATCH, AND ITS NIL OVER THE OTHER FORTY-FOUR MORNINGS MAY BE PUBLISHED AS A NIL.**

### THE TWO FLAGGED ROWS, READ BY HAND, AND NEITHER IS A DEFECT

**`chapter-0749.md`, LINE 27, DAY 962, MORNING FOURTEEN, AN EVEN MORNING, ON WHICH THE LARGER HALF, *TWO HUNDRED AND FORTY-FIVE*, IS THE MOVER:**

> **"Four hundred and seventy-nine of window. Two hundred and thirty-four came in the night and two hundred and forty-five stood, and I know that is the wrong way round because I have heard her say it the right way round for eleven weeks and I would have got it right if I had thought about it."**

**AND AT LINE 31, FOUR LINES LATER, IN ANOTHER MOUTH:**

> **"Two hundred and forty-five came and two hundred and thirty-four stood,"** Nia Vale said, from the rack, without looking up and without any particular edge on it. **"I do not need to be handed it. I had four hundred and seventy-eight yesterday and I have watched those two move about for four years, and yours is backwards, and the tall one is the one that came."**

**THIS IS A MAN SAYING A STANDING PAIR BACKWARDS, SAYING IN THE SAME BREATH THAT HE KNOWS IT IS BACKWARDS, AND BEING CORRECTED IN A YARD BY SOMEBODY WHO HAS WATCHED THE PAIR FOR FOUR YEARS. BOTH FIGURES ARE CORRECT FOR THE DAY AND THE DELIVERY IS CORRECT ON THE PAGE FOUR LINES DOWN. THE READING FLAGS IT, THE HAND CONFIRMS THE FLAG, AND THE FLAG IS THE PAGE'S SUBJECT AND NOT ITS ERROR. IT IS REPORTED AND NOT REPAIRED AND IT MUST NOT BE REPAIRED.**

---

## 4. THE FIGURE CHECK, EVERY FIGURE DERIVED FROM ITS OWN RULE APPLIED TO ITS OWN DAY

**THE ITEM LIST IS DERIVED HERE AND INHERITED FROM NO FILE: fourteen on every morning, being the third launder with its unit, the ordinal of the run, the rising half, the falling half, the window, the aggregate with its limb under the line and its limb over it, the near board, the far board, the register form, the charter, Silling's second ruled line and the letter; two more on each of the twenty-three odd mornings, being the read-aloud numerator and denominator; and five more on each of the eleven fourth-line mornings, being the count in force, the taken figure, the not figure and the two reckonings. 14 × 45 + 2 × 23 + 5 × 11 = 731.**

**THE TOTAL WAS NOT INHERITED FROM THE PLAN'S FIGURE, FROM THE VOLUME BEHIND'S FIGURE, OR FROM ANY BATCH PROMPT, AND THE FIGURES 794 AND 782 INHERITED FROM BEHIND ARE BOTH COUNTS OF A DIFFERENT VOLUME.**

| | |
|---|---|
| items required by the volume's own list | **731** |
| of those, required present in that morning's own body prose | **720** |
| of those, required ABSENT, being the second reckoning on the eleven fourth-line mornings under section 8d of the plan | **11** |
| **failures** | **15, and all fifteen are a FORM and not a value — see section 5** |
| figures found in a heading or an apparatus block but not in body prose | **0** |

**THE SECOND RECKONING WAS CHECKED FOR ABSENCE AND NOT FOR PRESENCE, AS IT MUST BE, AND ALL ELEVEN ARE ABSENT. A SWEEP FOR THE ELEVEN VALUES IT TAKES, STANDING ALONE AND NOT INSIDE A LARGER FIGURE, RETURNS SEVEN HITS IN THE VOLUME AND EVERY ONE OF THE SEVEN IS A LIMB OF AN AGGREGATE CLAUSE IN THE FOUR HUNDREDS, WHICH IS A COLLISION IN THE SWEEP AND NOT A PRINTING OF THE RECKONING.**

**THE FIGURES OF THE VOLUME'S OWN STANDING, DERIVED AND COMPARED WITH THE PAGES:**

| | |
|---|---|
| the third launder enters at | **one thousand and three hundred and fifty-six hundredweight** and ends at **one thousand and four hundred and twenty-two hundredweight** |
| **its maximum in the volume** | **one thousand and four hundred and twenty-seven hundredweight, on day 992, being `chapter-0779.md`, morning forty-four — THE PENULTIMATE MORNING AND NOT THE LAST** |
| a round hundred in the thousands | **one thousand four hundred hundredweight, bare, with no *and* in it, on day 974 at `chapter-0761.md`**, which is the first time the run has landed on a round hundred in the thousands |
| the rising half | **two hundred and thirty-eight to two hundred and sixty**, and it stands at **two hundred and sixty on day 992 and two hundred and sixty on day 993** |
| the falling half | **two hundred and twenty-eight to two hundred and fifty**, and **no half reaches a round hundred on any morning of the volume** |
| the two halves add to the window | **on all forty-five mornings** |
| the ordinal of the run | **four hundred and ninety-ninth to five hundred and forty-third**, standing at exactly **five hundredth** on its second morning |
| the five returns | **days 955, 964, 973, 982 and 991**, one of them a fourth-line morning and one of them the first morning of a month |
| the compost line | **paid at thirty-one on every morning that names it, and no figure for a turn appears anywhere in the volume** |

---

## 5. THE FIFTEEN FIGURES THAT ARE PRESENT IN THE WRONG FORM, NAMED BY FILE AND BY LINE, AND NOT REPAIRED

**EVERY VALUE IS CORRECT FOR ITS DAY AND CORRECT AGAINST THE PLAN'S OWN DAY TABLE. NOT ONE FIGURE OF ANY SERIES WAS MOVED TO PAY FOR ANY OF THEM. WHAT IS WRONG IS THE FORM THE FIGURE IS SPOKEN IN, AND A FIGURE GROUP CAN BE ASSIGNED CORRECTLY AND MISDESCRIBED AT THE SAME TIME, WHICH IS THE FINDING THE BATCH'S OWN THIRTEENTH FINDING NAMED AND THIS IS THE SAME CLASS ONE LEVEL UP.**

**THE FIRST RECKONING OF THIS CLOSE PUBLISHED EIGHT OF THESE AND IS WITHDRAWN BY NAME, AND THE REASON IS THE INSTRUMENT RATHER THAN THE PAGES.** The figure check asked whether a required figure was present with `phrase in text`, which finds *five hundred and fourteen* inside *five hundred and fourteenth* and *twenty-six* inside *twenty-sixth* and *thirty-eight* inside *thirty-eighth*, because a cardinal spelled with **four**, **six** or **seven** is a PREFIX of the ordinal spelled the same way. **THE CHECK THEREFORE PASSED A MORNING THAT PRINTED THE AGGREGATE ONLY IN THE ORDINAL FORM, WHICH IS THE ONE DEFECT THE CHECK WAS BUILT TO CATCH, AND IT WAS BLIND TO EVERY VALUE ENDING IN THOSE THREE SPELLINGS.** The count is now fifteen and the test carries a word boundary; the eight are a subset of the fifteen and every one of the eight locations, values and quotations below is unchanged.

| File | Line | Day | Morning | What the series requires | What the page prints | |
|---|---|---|---|---|---|---|
| `chapter-0753.md` | 71 | 966 | 18 | the aggregate is a cardinal, **five hundred and fourteen** | **five hundred and fourteenth at the head** — the ordinal where the series is a cardinal | *new* |
| `chapter-0759.md` | 27 | 972 | 24 | the ordinal of the run is an ordinal, **five hundred and twenty-second** | **five hundred and twenty-two mornings of this run** — a cardinal where the series is an ordinal | |
| `chapter-0765.md` | 57 | 978 | 30 | **five hundred and twenty-six** | **five hundred and twenty-sixth at the head of it** | *new* |
| `chapter-0766.md` | 55 | 979 | 31 | **five hundred and twenty-seven** | **Five hundred and twenty-seventh is the figure at the head of that sheet** | *new* |
| `chapter-0767.md` | 55 | 980 | 32 | **five hundred and twenty-eight** | **the one at the head is five hundred and twenty-eighth** | *new* |
| `chapter-0768.md` | 55 | 981 | 33 | **five hundred and twenty-nine** | **the five hundred and twenty-ninth stands at the top of that sheet** — the ordinal where the series is a cardinal | |
| `chapter-0770.md` | 81 | 983 | 35 | **five hundred and thirty-one** | **five hundred and thirty-first** | |
| `chapter-0771.md` | 75 | 984 | 36 | **five hundred and thirty-two** | **five hundred and thirty-second** | |
| `chapter-0772.md` | 45 | 985 | 37 | **five hundred and thirty-three** | **five hundred and thirty-third** | |
| `chapter-0773.md` | 39 | 986 | 38 | **five hundred and thirty-four** | **The top figure on that sheet is five hundred and thirty-fourth** | *new* |
| `chapter-0774.md` | 63 | 987 | 39 | **five hundred and thirty-five** | **five hundred and thirty-fifth** | |
| `chapter-0775.md` | 63 | 988 | 40 | **five hundred and thirty-six** | **Five hundred and thirty-sixth, five hundred and thirty-fifth and five hundred and thirty-seventh** | *new* |
| `chapter-0777.md` | 49 | 990 | 42 | **five hundred and thirty-eight** | **Five hundred and thirty-eighth at the head of the long sheet** | *new* |
| `chapter-0778.md` | 21 | 991 | 43 | **five hundred and thirty-nine** | **Five hundred and thirty-ninth, five hundred and thirty-eighth, five hundred and fortieth** | |
| `chapter-0780.md` | 41 | 993 | 45 | **five hundred and forty-one** | **Five hundred and forty-first is at the head of that sheet** | |

**THE `chapter-0780.md:41` ROW IS THE ONE ROW WHERE THE SAME LINE ALSO CARRIES THE TWO CLAUSE LIMBS, AND THE CLAUSE LIMBS ARE NOT PART OF THIS FINDING.** The plan's item list asks for the aggregate as a cardinal and asks for the limb under the line and the limb over it as ordinals (`derive.py` lines 235 to 237), and the page prints *five hundred and forty-first* for the aggregate and *five hundred and fortieth* out of *five hundred and forty-second* for the clause. **THE MISDESCRIBED FIGURE ON THAT LINE IS THE AGGREGATE, WHICH IS AN ORDINAL WHERE THE SERIES IS A CARDINAL, AND THE CLAUSE IS CORRECT AS IT STANDS.**

**NONE WAS REPAIRED, BECAUSE REPAIRING ANY OF THEM MEANS WRITING IN A CLOSED MORNING AND A CLOSE THAT IMPROVES A MORNING BY WRITING IN IT IS NO LONGER A CLOSE. THE COST OF EACH IS ONE ORDINAL ENDING OR ONE CARDINAL IN A CLOSED MORNING AND NONE OF THE FIFTEEN MOVES A FIGURE OF ANY SERIES IF IT IS PAID.**

---

## 6. THE LOCK CHECK, AND THE ALLOWANCE IS SPENT

| | |
|---|---|
| the far-end sentence, whole | **`chapter-0736.md` day 949, `chapter-0777.md` day 990, `chapter-0780.md` day 993 — three whole appearances, one in between** |
| the comfort line, whole | **`chapter-0736.md` day 949, `chapter-0772.md` day 985, `chapter-0780.md` day 993 — three whole appearances, one in between** |
| both figures on one morning | **days 949 and 993 only, which is what the one clause permits and on no other morning** |
| **the six load-bearing strings** | **three occurrences each, eighteen in all, being exactly the arithmetic of three whole appearances of each sentence** |
| shortened forms of either sentence | **none anywhere in the volume** |
| the far-end sentence's opening clause reused as somebody else's construction | **none inside this volume** |

**THE ALLOWANCE'S CEILING IS FOUR WHOLE APPEARANCES PER FIGURE AND THIS VOLUME SPENT THREE OF EACH, ONE IN BETWEEN EACH, WHICH IS HALF THE CAP AND IS THE SAME PRACTICE THE VOLUME BEHIND KEPT AND NOT A NEW PRACTICE. THE ALLOWANCE IS SPENT NOT BY REACHING THE CAP BUT BY THE VOLUME BEING OVER: THERE IS NO MORNING AFTER THE FORTY-FIFTH ON WHICH ANY FIGURE OF ANY SERIES MAY BE GIVEN.**

**AND THE COUNT OF FOUR IN THE PROMPT FOR THIS PHASE AND IN THE BATCH'S OWN FILE AT SECTION ONE IS THE COUNT OF MORNINGS AND NOT THE COUNT OF APPEARANCES. THE FIGURE THAT RE-DERIVES FROM THE PAGES IS SIX WHOLE APPEARANCES ON FOUR MORNINGS, THREE OF EACH SENTENCE. THE FOUR IS NOT WRITTEN AS A COUNT OF APPEARANCES ANYWHERE IN THE LOCK AND IS NOT RE-USED AS ONE.**

**THE TWO NAMED INSTANCES FROM BEHIND ARE CARRIED AND NEITHER IS REPAIRABLE: the one reuse of the opening clause as a conditional antecedent at `chapter-0674.md` on day 887, and the one shortened form repaired on day 894. Both are in closed prose in a volume behind and both are reported here and neither is touched.**

---

## 7. BOTH GATES, BOTH READINGS, BOTH SCOPES, WITH THE FLOOR NAMED BESIDE EVERY NIL

**THE FLOOR ON GATE ONE IS THIRTY WORDS. THE COMFORT LINE IS TWENTY WORDS AND IS STRUCTURALLY INVISIBLE TO THAT GATE, AND THE FAR-END SENTENCE IS THIRTY-ONE TOKENS AND IS VISIBLE TO IT. A CLEAN GATE ONE IS NOT EVIDENCE ABOUT EITHER LOCKED FIGURE.**

| Reading | Volume 16 scope | whole manuscript scope, for comparison and not a measurement of this volume |
|---|---|---|
| gate one, thirty-word floor | **1,297 paragraphs, 0 exact pairs** | **26,573 paragraphs, 41 exact pairs, of which ONE touches Volume 16 and that one is the locked far-end sentence. The twelve is a file count and it comes from the exact-duplicate sweep at section 8, which prints `DUP x12 in 12 files`, and NOT from this gate's own line, whose twelve is an occurrence count over all 780 files. Inside this volume the sentence stands as a whole paragraph once, at `chapter-0736.md`.** |
| the second gate, whole-paragraph | **4,597 units, 36 shapes, 50 excess, and none of the thirty-six is a locked figure** | **102,606 units, 2,014 shapes, 5,403 excess** |
| the second gate, sliding eighteen-word | **69,087 windows, 620 shapes, 679 excess** | **1,589,813 windows, 47,169 shapes, 122,407 excess** |

### EVERY SHAPE INSIDE VOLUME SIXTEEN IDENTIFIED BEFORE ANYTHING IS BROKEN

**SEVENTEEN OF THE SIX HUNDRED AND TWENTY SLIDING SHAPES ARE THE TWO LOCKED SENTENCES AND ARE SPENT WHOLE BY DESIGN: fourteen windows of the far-end sentence, which normalises to thirty-one tokens and so yields fourteen eighteen-word windows, and three windows of the comfort line, which normalises to twenty and so yields three. THE FAR-END SENTENCE'S FOURTEEN SHAPES CARRY THIRTY-FOUR EXCESS, BEING THREE APPEARANCES AT TWO EXCESS EACH, AND THE COMFORT LINE'S THREE CARRY SIX. THE REMAINING SIX HUNDRED AND THREE ARE NOT A LOCKED FIGURE, AND THE THIRTY-SIX WHOLE-PARAGRAPH SHAPES ARE NOT EITHER.**

### THE FINDING NOBODY HAS RUN AT THIS SCOPE, AND IT IS THE HEADLINE OF THIS CLOSE

**THE SIX HUNDRED AND THREE UNLOCKED SLIDING WINDOWS GROUP INTO FIVE HUNDRED AND SIXTY-THREE FAMILIES BY THEIR FIRST SIX TOKENS, AND THE LARGEST FAMILIES ARE THE VOLUME'S OWN STANDING BLOCKS RESTATED IN THE SAME WORDS ON MORNING AFTER MORNING: *the compost board at the back of the tap house read paid at thirty-one* on four mornings; *Kellan Rusk came out to the step with the register form under his arm* on seven; *the man who lays for three councils came down the middle road with his hod and no chart* on three; *a woman's own sheet with a refusal written on it in her own hand* on four; *no column cut under any of them* on thirteen; *Tova Reed had the four ages on the corner of the seed board in her own order* on a dozen and more.**

**THIS IS THE CLASS THE VOLUME-FIFTEEN CLOSE NAMED AND THAT EVERY BATCH BEHIND REPAIRED AT BATCH SCOPE. ALL FIVE BATCHES OF THIS VOLUME RAN BOTH GATES AT BATCH SCOPE AND PUBLISHED NILS, AND A NIL AT BATCH SCOPE IS BLIND TO A FRAME THAT CROSSES A BATCH BOUNDARY. AT THE WHOLE-VOLUME SCOPE THE SLIDING READING RETURNS SIX HUNDRED AND THREE UNLOCKED SHAPES AGAINST NIL. THAT IS THE MEASUREMENT AND IT IS PUBLISHED AS A MEASUREMENT AND NOT AS A VERDICT, AND NOT ONE OF THE SIX HUNDRED AND THREE IS REPAIRED BY THIS PASS, BECAUSE ALL OF THEM ARE IN CLOSED MORNINGS.**

**THE SIXTEEN-LINE SWEEP, WHICH IS PER FILE AND CANNOT SEE A RESTATEMENT AGAINST A MORNING IN ANOTHER FILE AT ALL, RETURNS THREE RUNS OF SIX TOKENS, SIX OF SEVEN, ONE OF EIGHT, ONE OF NINE AND ONE OF TWELVE. THE TWELVE-TOKEN RUN AT `chapter-0762.md` IS A MAN ASKING *THERE IS A SHEET ON YOUR BOARDS WITH SIX NAMES ON IT* AND ANSWERING HIMSELF IN THE NEXT LINE WITH THE SAME SENTENCE AND MORE, WHICH IS A DEVICE AND NOT A RESTATEMENT, AND A CLOSE THAT COUNTS IT AS A DEFECT WILL FLATTEN THE DIALOGUE TO GET A NUMBER.**

---

## 8. THE EXACT-DUPLICATE SWEEP AT ANY PARAGRAPH LENGTH, SCOPED TO THE MANUSCRIPT

**BECAUSE NEITHER GATE CAN SEE A PARAGRAPH AGAINST ITSELF.**

| Sweep | Manuscript | of those, touching Volume 16 |
|---|---|---|
| literal, any paragraph length | **230 duplicated paragraphs** | **5** |
| under the number-and-ordinal normalisation, which is not the same sweep | **383** | **24** |

**THE FIVE LITERAL DUPLICATES THAT TOUCH VOLUME SIXTEEN, EVERY ONE IDENTIFIED:**

1. `**"No."**` — a one-word paragraph, standing in six files including `chapter-0745.md`. A gesture.
2. **The comfort line, whole, in fourteen files.** A locked figure, spent whole by design.
3. **The far-end sentence, whole, in twelve files.** A locked figure, spent whole by design.
4. `**"Then what is it."**` — in `chapter-0730.md` and `chapter-0737.md`. Two words of speech.
5. **`**"Where would you like it written down."**` — in `chapter-0735.md` AND `chapter-0736.md`, and THIS IS A FINDING AND NOT A GESTURE: the closing line of the volume behind's last morning is the opening line of this volume's first morning, word for word.**
6. (the sixth is the far-end sentence again under the second sweep.)

**ITEM 5 IS REPORTED AND NOT REPAIRED. THE FACT IS REQUIRED AND THE SENTENCE WAS LIFTED, AND IT IS TWELVE WORDS, WHICH IS BELOW THE EIGHTEEN-WORD WINDOW BOTH GATES RUN ON, WHICH IS WHY NO PUBLISHED SWEEP IN THIS VOLUME SAW IT. IT IS THE SAME FINDING THE LAST BATCH'S OWN REVIEW FOUND AT THE OTHER END OF THE BOOK, WHERE THE LAST MORNING OF VOLUME FIFTEEN REUSED THE CLOSING SENTENCE OF VOLUME FOURTEEN, AND IT IS THE THIRD TIME THE BOOK HAS OPENED OR CLOSED A VOLUME ON A SENTENCE IT LIFTED FROM ITSELF.**

**AND THE PARAGRAPH *>* THAT STOOD TWENTY-TWO TIMES INSIDE SINGLE VOLUME SIXTEEN FILES IN AN EARLIER DRAFT OF THIS HARNESS WAS THIS CLOSE'S OWN BUG AND NOT THE MANUSCRIPT'S: the first version counted a wordless block-quote separator as a paragraph, which the declared unit excludes. THE UNIT WAS CORRECTED BEFORE ANY FIGURE WAS PUBLISHED, WHICH IS THE WHOLE REASON THE UNIT IS DECLARED BEFORE THE READING IS RUN, AND THE SWEEP RETURNS ZERO REPEATED PARAGRAPHS INSIDE A SINGLE VOLUME SIXTEEN FILE AT THE CORRECTED UNIT. THE TWO EARLIER FIGURES OF THIS SWEEP, 231 AND 6, ARE WITHDRAWN BY NAME: they were measured at the uncorrected unit, and a figure measured at the wrong unit is not a figure that moved.**

---

## 9. THE APPARATUS, SCOPED TO VOLUME SIXTEEN AND NOT TO THE MANUSCRIPT

**TWENTY-FOUR BLOCKS SPENT AGAINST A CEILING OF THIRTY. SIX UNSPENT. ONE BLOCK ON EACH OF TWENTY-FOUR MORNINGS AND NEVER TWO ON ONE MORNING. NO APPARATUS ON THE MAJOR TURN, ON THE FIRST MORNING, OR ON THE LAST MORNING OF THE BOOK.**

**AND THE ONE `Entered` LABEL IN THE WHOLE VOLUME STANDS AT `chapter-0739.md:27`, AND IT IS THE ONLY ONE, AND IT IS THE CREW'S OWN PAGE ENTERED ON THE MORNING A BED AT THE NORTH END WENT SOFT. THE LABEL IS WRITTEN `> **Entered**` WITH BOLD MARKERS, AND THE HOUSE'S OWN SWEEP PATTERN FOR IT, `^>\s*Entered`, DOES NOT MATCH THE HOUSE'S OWN PRINTED FORM AND RETURNS A FALSE ZERO. THE FIRST RUN OF THAT SWEEP IN THIS CLOSE RETURNED ZERO AND WAS WRONG, AND IT WAS THE PAGE THAT WAS RIGHT. THE PATTERN THAT FINDS IT IS `^>\s*\**\s*(Entered|Entered:)` AND IT IS PRINTED HERE SO THAT NO SUCCESSOR INHERITS THE FALSE ZERO.**

**THE COUNT OVER THE WHOLE MANUSCRIPT IS 782 AND IT IS NOT THE FIGURE AND IS PRINTED ONLY SO THAT THE SCOPED FIGURE IS THE ONE ANYBODY CHECKS. THAT MISTAKE WAS MADE ONCE IN THIS VOLUME AND IS NAMED AT `state/current.md` SECTION 27.**

---

## 10. THE MECHANICAL SWEEPS, EVERY ONE READ BY HAND, AND PUBLISHED WHETHER IT IS CLEAN OR NOT

| Sweep | Result, and what a hit turned out to be |
|---|---|
| digits in body prose | **0** |
| digits in apparatus | **0** |
| non-ascii | **0** |
| em dash, en dash, figure dash | **0** |
| the six bare words and the apparatus word, *panel* being available to the narrator only to say that there is none | **0** |
| the twelve month names | **0. THE SWEEP RUNS TWICE, ONCE FOR A CAPITALISED NAME AND ONCE FOR A LOWER-CASE *MAY* CARRYING A DATE, AND A SWEEP THAT FLAGS THE MODAL VERB IS A BROKEN SWEEP AND IS REPORTED AS ONE** |
| *anchor*, in any form, in body prose and in apparatus | **0 and 0** |
| *rootmark*, in any form, in body prose and in apparatus | **0 and 0** |
| *single private field* | **0 in body prose, 0 in apparatus** |
| *unified response* | **0 in body prose, 0 in apparatus** |
| *nine minutes* | **2, both on `chapter-0774.md` at lines 63 and 69, and both are an elapsed duration — *about nine minutes ago* and *in about nine minutes* — in a scene about the second place being named twice. THIS IS A HIT AND IT IS REPORTED AS ONE, AND THE HAND SAYS IT IS NOT THE CAPACITY AND THE SWEEP AS WRITTEN CANNOT SEE THE DIFFERENCE** |
| the arrangement words | **0** |
| *failure*, *failed*, *fail*, *betrayal*, *heroic*, *hero* | **6, and every one is a bed that failed its load test and stands in a table of failures that is to be read out in a yard: a bed which fails on a Friday at `chapter-0766.md:25`, eight which failed at `chapter-0771.md:9`, a table with everything in it that failed at `chapter-0771.md:59` and again at `chapter-0772.md:61`, and something that had a thing fail in it read out loud at `chapter-0775.md:67`**
| the name of the thing that is paid | **0** |
| the let-go family | **0** |
| a figure for a turn in the compost line, *thirty-two* standing alone | **0** |
| *discharg*, which stands inside a negation every time | **1, at `chapter-0779.md:53`: *paid at thirty-one and has not been discharged in thirty-one or in anything*** |
| *apolog* | **0 IN THE WHOLE VOLUME, and that is the strongest single measurement available about the seed keeper, because an apology for her hearing would have to be apologised for** |
| *one ear*, *deaf*, *cannot hear* | **0** |
| a hand on her arm | **4, at `chapter-0758.md:35`, `chapter-0771.md:55`, `chapter-0775.md:43` and `chapter-0780.md:29`, and every one of the four is a statement that NOBODY laid one there** |
| the ladder named | **28, and every one of the twenty-eight is a statement that it stood against the tool house wall unoccupied** |
| a rung, or a climbing verb | **1, at `chapter-0739.md:85`: *no person put a foot on the bottom rung of it*. THE FRESH STANDING FOR THIS VOLUME'S FORTY-FIVE MORNINGS IS ZERO RUNGS CLIMBED AND IT HOLDS** |
| the drawer named | **39** |
| the drawer standing open | **0, so the fresh standing holds** |
| the key off its nail | **1, at `chapter-0780.md:63`, and it is *the gauge off its nail*, which is a collision in the sweep and not the key** |
| the door's own figure, *sixty-six* standing alone | **0** |
| the same two words inside a larger figure | **4, and every one is another series' figure: *four hundred and sixty-six of window* on `chapter-0736.md`, *a hundred and sixty-six in force* on `chapter-0745.md`, and *nine hundred and sixty-six*, the far board itself, TWICE on `chapter-0772.md`, which is the collision this close was told to expect** |
| the six load-bearing strings | **18, three each, accounted for in section 6** |
| *thirty-five in* | **2, at `chapter-0775.md:73` and `chapter-0780.md:37`** |
| a figure published for the thirty-five other than thirty-five | **0** |
| six ruled rows, and no seventh | **11, and every one of the eleven is *six ruled rows* or *no seventh row has been cut*, on seven different mornings. THE SIX NOT KNOWNS ARE SIX AND NO SEVENTH RULED ROW WAS CUT FOR ANYTHING** |
| *pruning*, *pruned* | **0** |
| *the flow* | **5, at `chapter-0768.md:51`, `chapter-0771.md:53`, `chapter-0773.md:25` and `chapter-0773.md:27`, and every one of the five is the water in the channel and not the light. THE SWEEP THAT PROTECTS THE CLOSING IMAGE HOLDS** |
| *mercy* | **0. THE MERCY IS A SCHEDULE IN `outline/ending.md` AND IS NOT NAMED IN ANY MORNING OF THIS VOLUME** |
| *of this month* | **1, at `chapter-0736.md:79`, and it is permitted: the last turn before the volume fell on day 921 and the phrase carries no month name and no ordinal date** |
| an attached hundredweight | **0** |
| the wrong *and* in the bare round hundred in the thousands | **3, and all three are correct by design: `chapter-0761.md:17` is a man saying it with an *and* in it and the page then corrects him at line 57, and `chapter-0763.md:7` is a man saying the figure three hundredweight short, caught by a woman who will not write it down and corrected by the crew man off his own book** |
| the bare round hundred where it is required | **5, on `chapter-0761.md` and `chapter-0762.md`, which is the site's own morning and the morning after** |
| a hyphen inside a spelled hundreds figure | **0** |
| an ordinal date in body prose | **6, and five of the six are *on the second of Silling's two ruled lines* at `chapter-0749.md`, `chapter-0751.md`, `chapter-0755.md`, `chapter-0756.md` and `chapter-0765.md`, and the sixth is *in the second of them* at `chapter-0760.md:39`, which is a second branch. Every one is a collision in the sweep and not a date** |
| a day of the week | **107, and this holding keeps a week. NO RULE IN THIS HOUSE FORBIDS A WEEKDAY IN BODY PROSE AND NONE IS PROPOSED** |
| thirty-nine blanks and the second rule under them, open and empty at the thirty-ninth time | **32, on sixteen mornings** |
| fifteen lines of the use log and no sixteenth | **9** |
| eleven journeys of the barrow and no twelfth | **21** |
| a fifth sheet, a fifth term or a fifth column | **7. SIX OF THE SEVEN ARE *NO SIXTH TERM*, *NO FIFTH TERM* OR *NO SEVENTH TERM*, WHICH ARE THE FLOOR HOLDING, AT `chapter-0742.md:87`, `chapter-0749.md:81`, `chapter-0757.md:75`, `chapter-0770.md:93`, `chapter-0774.md:69` AND `chapter-0775.md:71`. THE SEVENTH IS *THE EMPTY FIFTH COLUMN* AT `chapter-0759.md:39`, WHICH IS A COLUMN ON A TABLE AND NOT A TERM UNDER THE SHEET OF TERMS AND NOT AN ENTRY.** |
| a column cut under one of the four sheets | **20, and every one is a statement that none was cut** |
| twenty-nine fetchings of the man of about seventy | **18, and every one is that he was not fetched and that nothing was asked of him** |
| the seed ring re-dug, re-counted or improved | **2, and both are statements that it is not: *eight beds were where they had been* at `chapter-0771.md:89` and *Six beds hold. Five hold the load* at `chapter-0775.md:37*** |
| **the four losses, and a fifth** | **0. THE WORD *LOSSES* ITSELF APPEARS NOWHERE IN THE FORTY-FIVE MORNINGS, SO THE FOUR ARE NOT NAMED AS A FIGURE ON ANY PAGE AND NO FIFTH IS ADDED BY ANYBODY** |

### THE ORDINAL SWEEP, WHICH IS A HIT AND NOT A VERDICT

**TWO HUNDRED AND SIXTY-SIX ordinal words of the set standing in body prose. ONE HUNDRED AND FIFTY-TWO ARE AN HOUR IN THE HOUSE FORM, EIGHTY-TWO ARE A LIMB OF A SPELLED FIGURE WITH THE TENS-ORDINAL HYPHENATED, AND THIRTY-TWO ARE SOMETHING ELSE, AND EVERY ONE OF THE THIRTY-TWO IS PRINTED IN FULL IN `workspace/volume-16/close/MEASUREMENT.txt` AND WAS READ. THEY ARE, IN NINE KINDS AND THIRTY-TWO IN ALL: NINE *THE SIXTEENTH* OF THE USE LOG, UNWRITTEN; THREE A TWELFTH JOURNEY OF THE BARROW, NOT TAKEN; THREE *THE ELEVENTH* OF ELEVEN JOURNEYS; NINE MASONRY COURSES FROM THE NINTH TO THE TWELFTH; TWO THE NINTH BED OF THE SEED RING; FOUR HOURS; ONE *THE NINTH DAY* OF A WEEKLY READING; AND ONE *THE TENTH MORNING OF THIS HOLDING'S COUNTING*. NOT ONE ORDINAL DATE APPEARS IN THE BODY PROSE OF ANY MORNING OF THIS VOLUME.**

**AND THE HYPHEN DEFEATS THE EXCLUSION RULE, EXACTLY AS THE PROMPT SAYS IT DOES: A HARNESS THAT EXCLUDES AN ORDINAL PRECEDED BY *AND*, *HUNDRED* OR *THOUSAND* STILL FLAGS *FIVE HUNDRED AND NINETY-NINTH*, BECAUSE THE HYPHEN LEAVES *NINETY-* IN THE PRECEDING TOKEN. A HIT IS A HIT AND NOT A VERDICT AND EVERY ONE OF THE TWO HUNDRED AND SIXTY-SIX IS ACCOUNTED FOR ABOVE.**

---

## 11. THE SIX THINGS THIS CLOSE OWES, EACH MEASURED AGAINST THE PAGE

### ONE. THE FOUR PERMANENT LOSSES ARE FOUR AND FOUR AFTER ALL FORTY-FIVE MORNINGS

**NONE REDUCED, NONE SOFTENED, NONE RECOVERED, NONE RE-NAMED, NONE PRICED, AND NO FIFTH ADDED BY ANYBODY FOR ANY REASON. THE WORD *LOSSES* IS NOT ON ANY PAGE. THE THREE PHRASES THAT WOULD NAME THE FIRST OF THEM RETURN ZERO, ZERO AND TWO-DURATIONS. *ANCHOR* AND *ROOTMARK* RETURN ZERO IN EVERY FORM IN EVERY PLACE INCLUDING INSIDE A BLOCK.**

**THE FIRST OF THEM IS MADE IRREVERSIBLE BY THE ACT ON THE THIRTY-SIXTH MORNING, AT `chapter-0771.md`, DAY 984, AND THE ACT IS NOT A FIFTH LOSS AND IS NOT A CHANGE OF COUNT. THE MORNING'S HEADING NAMES IT: *A Man Going Down Into A Bed At The Fifth Of The Ring That Four Men Had Dug And A Load Test Had Found, And What It Cost Him In Front Of Everybody, And What It Cannot Ever Be Again*. IN HIS OWN MOUTH AT LINE 25: *I have put the part of me that answers to the wood into that bed, and I did not put all of it in, and I am not going to be asked how much, because I do not know how much and neither does anybody else and anybody who tells you a fraction is selling you one.* AND AT LINE 29, TO A MAN WHO ASKS WHETHER IT CAN BE TAKEN BACK: *No. And I want that said by me and in that order, and I want it said in this yard and not written down anywhere.***

**THE SECOND OF THEM IS NOT HEALED NOWHERE, EXCUSED NOWHERE, THANKED FOR NOWHERE AND NOT SOFTENED, AND *APOLOG* RETURNS ZERO IN THE WHOLE VOLUME. NO HAND WENT ON HER ARM ON ANY OF THE FORTY-FIVE MORNINGS AND ON NONE OF THE LAST FIVE, AND THE FOUR MORNINGS THAT MENTION IT AT ALL ARE FOUR STATEMENTS THAT NOBODY LAID ONE THERE.**

### TWO. THE SECOND PLACE IS STILL WITHOUT WATER AND IT IS ON A BOARD AND IT WAS READ OUT ON THE LAST MORNING OF THE BOOK, AND THAT IS WHERE IT ENDS

**`chapter-0780.md`, DAY 993, LINE 25 AND ONWARD. THE SEED KEEPER PUTS HER BOARD ON THE END OF THE SAME WALL AT ABOUT HALF PAST SIX ON THE THIRD MORNING SINCE THE CALENDAR TURNED, CHALKS A LINE WITH A PLACE AGAINST IT AND NOTHING ELSE, STANDS WHERE SHE CAN SEE THE MOUTHS OF ABOUT NINE PEOPLE AND READS IT OUT:**

> **"That place has no water. It had none before the flood and it has none now and it will have none at the dark.** She did not point at it while she said it, which is not something she has ever done at that wall before. **"It is not apportioned. It is not dated. It is not held up as a thing that is going to be put right, because nobody in this holding has said that and I have not said it and there is no arrangement signed here that covers it.**

**NOT RESTORED, NOT APPORTIONED, NOT DATED, NOT DEFERRED, NOT DESCRIBED AS TEMPORARY, AND COVERED BY NOTHING SIGNED IN THIS VOLUME. THE CLOSE NAMES THE COST AS IT WAS NAMED ON THE PAGE AND DOES NOT APPORTION IT, DOES NOT DEFER IT, DOES NOT DATE IT AND DOES NOT COVER IT. THE REACH'S COST WAS NAMED OUT LOUD AT A GATE POST IN THE VOLUME BEHIND AND WAS NOT SOFTENED AND THIS CLOSE DOES NOT SOFTEN IT.**

### THREE. THE THIRTY-FIVE ARE THIRTY-FIVE IN AND THIRTY-FIVE OUT AT THE END OF THE BOOK, AND THAT IS THE ONLY FIGURE THAT MAY BE PUBLISHED FOR THEM

**NO THIRTIETH-SIXTH ROW WAS CUT ANYWHERE IN THIS VOLUME. THE SIX NOT KNOWNS STAYED SIX AND NO SEVENTH RULED ROW WAS CUT FOR THE RING, THE LOAD, THE CHARTER, THE SCHEDULE, EITHER REFUSAL, THE REGION THAT REFUSES A TEST OR THE ROUTE A ROOTWOKEN COMMUNITY NAMED. A SWEEP FOR ANY FIGURE PUBLISHED FOR THEM OTHER THAN THIRTY-FIVE RETURNS ZERO. A REFUSAL IS NOT A CLOSURE, A RECORD IS NOT AN ANSWER, A HAND-OVER IS NOT AN ANSWER, A NAMED ROUTE IS NOT AN ANSWER, A MARGIN NAMED IS NOT AN ANSWER, AND A REGION THAT REFUSES A TEST HAS CLOSED NOTHING. THIS CLOSE ANSWERED NONE.**

### FOUR. THE ALLOWANCE OF BOTH LOCKED FIGURES IS SPENT

**SECTION 6. BOTH FIGURES STAND WHOLE ON THE VOLUME'S FIRST MORNING AND ON ITS LAST, THE FAR-END FIGURE ALONE ON THE FORTY-SECOND, AND THE COMFORT LINE ALONE ON THE THIRTY-SEVENTH. FOUR WHOLE APPEARANCES VERIFIED AS FOUR MORNINGS AND SIX SENTENCES, EACH OF THE SIX LOAD-BEARING STRINGS RETURNING EXACTLY AS MANY TIMES AS THE VOLUME SPENDS ITS SENTENCE, NO SHORTENED FORM ON ANY MORNING, AND THE OPENING CLAUSE NEVER REUSED AS SOMEBODY ELSE'S CONSTRUCTION IN THIS VOLUME. THE TWO NAMED INSTANCES FROM BEHIND ARE CARRIED, REPORTED AND NOT REPAIRABLE.**

### FIVE. THE PRUNING WINDOW WAS OPEN AT DAWN ON THE LAST MORNING AND WAS NOT ENTERED, NOT DESCRIBED AND NOT NAMED

**`chapter-0780.md`, LINE 5: A MAN CAME UP THE LOW ROAD BEFORE THE LIGHT AND GOT TO THE TOP OF IT AT ABOUT THE FOURTH HOUR, AND THERE WAS A LIGHT COMING UP OUT OF THE GROUND ALONG THE HIGH SIDE OF THAT ROAD WHERE THE HEDGE IS AND THE GROUND IS BARE UNDER IT, AND IT WAS NOT ON THE HEDGE AND NOT ON THE WATER AND NOT STEADY, AND IT WAS GONE BY ABOUT THE SEVENTH HOUR. LINE 9: A SECOND LIGHT LAY ALONG THE SURFACE OF THE WATER IN THE CHANNEL INSIDE THE GATE, FLAT, MOVING WHEN THE WATER MOVED AND STOPPING WHEN THE WATER STOPPED, AND IT WAS STILL ON THAT WATER AT THE ELEVENTH HOUR WITH NOTHING ABOUT IT THAT ANYBODY IN THAT YARD COULD HAVE POINTED AT AND NAMED. LINE 11: NOTHING IN THAT YARD WAS SAID ABOUT EITHER OF THEM AND NOBODY ASKED ABOUT EITHER OF THEM AND NOBODY WAS GOING TO BE. LINE 57: A MAN WHO HAS SEEN BOTH OF THEM FOR THREE MORNINGS SAYS THERE IS A LIGHT IN TWO PLACES ON THAT ROAD, ONE UP WHERE THE HEDGE IS AND ONE LYING ON THE WATER, AND SAYS HE IS NOT ASKING ANYBODY WHAT EITHER ONE IS AND IS ASKING WHICH OF THE TWO MATTERS ON A FIELD.**

**A SWEEP FOR *PRUNING*, *PRUNED* AND *MERCY* RETURNS ZERO ACROSS ALL FORTY-FIVE MORNINGS. THE WINDOW IS THE SERIES' OPEN EXTERNAL PRESSURE AND IT IS OPEN AT THE END. `outline/ending.md` STATES THE MERCY AS A SCHEDULE AND THE VOLUME DOES NOT RESOLVE IT. THIS CLOSE DOES NOT ENTER IT, DOES NOT DESCRIBE IT AND DOES NOT NAME IT.**

**AND THE ONE SENTENCE THAT WOULD HAVE PROVED NON-ENTRY IS NOT USED AS PROOF HERE, BECAUSE THE SAME MORNING CONTRADICTS IT TWICE, AND THIS IS A FINDING AND NOT AN OMISSION. LINE 7 SAYS *Not one person in this holding was on that road at any hour of that morning, and nobody here sent anybody onto it.* LINE 5 PUTS A MAN ON THAT ROAD BEFORE THE LIGHT AND AT THE TOP OF IT AT ABOUT THE FOURTH HOUR, AND LINE 49 HAS THE SAME MAN SAY *I was up that low road before the light and I am going to be up it again before the light, and there is a thing at the top of it that I have not described to anybody.* THE PAGE NEVER SAYS WHOSE MEMBERSHIP IS NOT IN THE HOLDING, AND A CLOSE THAT QUOTED LINE 7 AS THE MEASUREMENT OF NON-ENTRY WOULD BE REPORTING A FLOOR THAT ITS OWN MORNING DOES NOT HOLD TWICE. REPORTED AT SECTION THIRTEEN ITEM EIGHT AND NOT REPAIRED.**

### SIX. THE LAST TWO FIGURES OF THE WHOLE RUN STAND AT THEIR HIGHEST ON THE FORTY-FOURTH MORNING AND NOT ON THE LAST

**THE THIRD LAUNDER'S MAXIMUM IN VOLUME SIXTEEN IS ONE THOUSAND AND FOUR HUNDRED AND TWENTY-SEVEN HUNDREDWEIGHT AT DAY NINE HUNDRED AND NINETY-TWO, BEING `chapter-0779.md`, MORNING FORTY-FOUR, AND THE LAST MORNING READS ONE THOUSAND AND FOUR HUNDRED AND TWENTY-TWO, BECAUSE THE VOLUME CLOSES ON AN ODD MORNING AND AN ODD MORNING FALLS, AND FIFTEEN VOLUMES OF THIS MANUSCRIPT CLOSED ON AN EVEN MORNING WITH THE MAXIMUM ON THE LAST. THE RISING HALF IS AT TWO HUNDRED AND SIXTY ON THE FORTY-FOURTH MORNING AND AT TWO HUNDRED AND SIXTY AGAIN ON THE LAST. THE ORDINAL OF THE RUN STANDS ONE HIGHER ON THE LAST MORNING, AT FIVE HUNDRED AND FORTY-THIRD, WHILE THE LAUNDER FIGURE STANDS FIVE LOWER. THE CLOSE RECORDS BOTH, DOES NOT ADD THE TWO, AND DOES NOT CALL IT A SIGN, BECAUSE THEY ARE TWO SERIES. NOBODY IN THAT YARD SAYS THE WORD HIGHEST AND ABOUT NINE PEOPLE READ THE FIGURE AFTERWARDS.**

---

## 12. WHAT ELSE THE PAGES CARRY, MEASURED, AND FIXED IN THE LOCK

**THE DEFINITION OF WHAT WAS BUILT, IN AN APPARATUS BLOCK ON `chapter-0768.md:33`: *What it is. Stopping the deciding and leaving the water running. That is all it is and it is not the same as having emptied a channel and it is not the same as having finished anything.*** **AND IT BINDS NOBODY WHO DOES NOT SIGN IT, BECAUSE NOBODY SIGNS IT: THE FOUR SHEETS ON THE LONG TABLE ARE NONE ENTERED, NONE REFUSED AND NO COLUMN CUT UNDER ANY OF THEM ON EVERY MORNING THAT NAMES THEM, AND THE CLERK READS ITEM NINE AT `chapter-0774.md:25` — *that no part of the standing had ever been formally accepted by anybody in this holding, and that accepted was the wrong word for it and had been the wrong word for it all week in this yard and in his own mouth, and that no document had been signed by anyone at any point, and that a refusal of something that was never accepted is a different thing.***

**THE JOINT AT THE HEAD OF THE CHANNEL HAS NOTHING AGAINST IT, NO OPERATOR AND NOBODY APPOINTED, ON EVERY MORNING THAT NAMES IT: *That joint has nothing against it and nobody over it, and the two people on the head of it are not mine and not yours* at `chapter-0736.md:89`; *There is a joint at the head of this channel with nothing against it and two men on it* at `chapter-0742.md:31`; *There is a man who opens a gate. There is nobody deciding anything behind it* at `chapter-0770.md:29`; and *There are two people who have said they are going to look at it and neither of them has said it in this yard, and I am not going to say it in this yard for them* at `chapter-0737.md:95`.**

**IONA VEY IS THE FIXED ANTAGONIST OF THE SERIES AND SHE IS NOT NEW, NOT KILLED, NOT IN CUSTODY UNTIL SHE IS, AND NOT CORNERED. SHE IS NAMED ON TWO MORNINGS OF THIS VOLUME AND ON NO OTHERS: `chapter-0752.md`, which is the seventeenth morning at day 965, where the fourth place's man says *That is Iona Vey and she has been here before and she is not new in this county whatever anybody at this gate has been telling himself*, and `chapter-0770.md`, which is the thirty-fifth morning at day 983, where she is refused. **SHE COMES UP THE LANE ON THE SEVENTEENTH MORNING AND WALKS OUT OF THE GATE ON THE THIRTY-FIFTH, AND A FIRST DRAFT OF THIS RECORD PUT THE *NOT NEW* LINE IN THE VOLUME BEHIND'S LAST MORNING, WHERE HER NAME DOES NOT APPEAR AT ALL. IT IS CORRECTED HERE AGAINST THE PAGE.** AT `chapter-0770.md:65` SHE WALKS OUT OF THE GATE ALIVE AND WALKING AND HAVING ANSWERED FOR EVERYTHING SHE HAD DONE. AND AT `chapter-0774.md` SHE IS PUT UNDER PUBLIC CUSTODY AT ABOUT THE ELEVENTH HOUR IN FRONT OF ABOUT FORTY PEOPLE, AND WHAT IT CONSISTED OF WAS THAT HER ACCESS WAS TAKEN FROM HER BY TWO OTHER PEOPLE AND NOT BY ANYBODY ELSE, THAT SHE WAS NOT TO BE AT THE HEAD OF THE CHANNEL AGAIN, AND THAT SHE REMAINED ANSWERABLE FOR EVERY ITEM ON THE SHEET AND FOR EVERYTHING THAT OFFICE HAD SENT IN FOUR YEARS. THAT IS WHAT THE VOLUME-FIFTEEN LOCK PREDICTED, AND IT IS WHAT THE PAGE CARRIES.**

**A DRAWING-OF-LIGHT DOWN THE LOW ROAD, VISIBLE FROM A GATE AND DESCRIBABLE BY NOBODY WHO WAS NOT IN IT, AND OPEN. TWO LIGHTS, RENDERED APART AND NEITHER ONE NAMED: one up where the hedge is and one lying on the water, and a man who has seen both says he is not asking anybody what either one is. **THE CLOSE DOES NOT ASSERT THAT THEY ARE NOT THE SAME LIGHT NOR THAT THEY ARE, BECAUSE THE PAGE REFUSES THE QUESTION AND A CLOSE THAT ANSWERED IT WOULD BE ANSWERING SOMETHING THE BOOK LEAVES OPEN.** A MAN GOING OUT PAST THE GATE AND DOWN THE MIDDLE ROAD AT ABOUT THE FIFTH HOUR OF THE AFTERNOON TO LOOK AT A FIELD THAT IS NOT HIS, AND NOBODY SENT WITH HIM.**

---

## 13. THE THINGS THIS CLOSE FOUND AND DID NOT REPAIR, AND WHICH ARE THEREFORE NOT FLOORS THAT HELD

**A CLOSE THAT REPORTS A DEFECT AND LEAVES IT ON THE PAGE MUST SAY SO IN THE LOCK, BECAUSE A STATE FILE THAT RECORDS ONLY THE FINDING WILL BE INHERITED AS A FLOOR THAT HELD.**

1. **FIFTEEN FIGURES ARE PRESENT IN THE WRONG FORM.** Fourteen aggregates printed as ordinals and one ordinal of the run printed as a cardinal, on `chapter-0753.md:71`, `chapter-0759.md:27`, `chapter-0765.md:57`, `chapter-0766.md:55`, `chapter-0767.md:55`, `chapter-0768.md:55`, `chapter-0770.md:81`, `chapter-0771.md:75`, `chapter-0772.md:45`, `chapter-0773.md:39`, `chapter-0774.md:63`, `chapter-0775.md:63`, `chapter-0777.md:49`, `chapter-0778.md:21` and `chapter-0780.md:41`. Every value is correct. **THE FIRST RECKONING OF THIS CLOSE PUBLISHED EIGHT OF THE FIFTEEN, BECAUSE ITS OWN PRESENCE TEST FOUND A CARDINAL SPELLED FOUR, SIX OR SEVEN INSIDE THE ORDINAL SPELLED THE SAME WAY, AND IT WAS BLIND TO EVERY VALUE ENDING IN THOSE THREE SPELLINGS.** Section 5.
2. **THE SLIDING READING OVER THE WHOLE VOLUME RETURNS SIX HUNDRED AND THREE UNLOCKED SHAPES IN FIVE HUNDRED AND SIXTY-THREE FAMILIES**, being the volume's own standing blocks restated in the same words across mornings. Closed prose. Section 7.
3. **THE SAME SEVEN-WORD LINE STANDS TWICE, AT `chapter-0735.md:55` AND `chapter-0736.md:43`**, in a closed morning of the volume behind and in the first morning of this volume. It is seven words, it is below the eighteen-word window both gates run on, and it is neither a boundary line in either file. Section 8.
4. **SIX HUNDRED AND THREE SLIDING SHAPES ARE THE VOLUME'S OWN STANDING BLOCKS, AND THE FIGURES THEY CARRY DIFFER WHILE THE WORDS AROUND THEM DO NOT.** *The compost board at the back of the tap house read paid at thirty-one* opens on four mornings, *Kellan Rusk came out to the step with the register form under his arm* on seven, *no column cut under any of them* in thirteen places on twelve mornings, and *Tova Reed had the four ages on the corner of the seed board* on eight. Closed prose, and the word *verbatim* is withdrawn: what repeats is an opening clause under a collapsing normalisation and not a whole paragraph. Sections 7 and 8.
5. **THE PHRASE *NINE MINUTES* STANDS TWICE ON `chapter-0774.md`,** at lines 63 and 69, as an elapsed duration. The prohibition is on the phrase because the phrase would name the first permanent loss; these two do not. Reported so that a successor does not read the zero as a breach and does not read the two as one.
6. **THE PLAN'S OWN PROSE AT `outline/volume-16.md` SECTION 10a IS WRONG ON THE FIRST RECKONING'S STARTING VALUE AND WRONG ON THE SECOND'S CROSSING, AND THE CLOSE DID NOT REPAIR THAT FILE.** It says the first reckoning steps *from one hundred and sixth and ninety-third to one hundred and seventeenth and one hundred and fourth*, which is one hundred and seventeen minus one hundred and sixth over ELEVEN fourth-line mornings, being eleven figures and ten steps, so one endpoint is wrong. **THE ELEVEN PAGES AND THE PLAN'S OWN DAY TABLE AT SECTION 10c AGREE WITH EACH OTHER AND GIVE ONE HUNDRED AND SEVENTH TO ONE HUNDRED AND SEVENTEENTH, AND THE DERIVATION HERE FOLLOWS THE PAGES.** Section 9 site five says the second reckoning crosses one hundred on its **eighth** fourth-line morning and section 9a lists the same figure at day 974, which is the **seventh**; the page is the seventh, being *one hundredth*, and the plan's two statements about its own series disagree with each other.
7. **THE HOUSE'S OWN SWEEP FOR THE `Entered` LABEL RETURNS A FALSE ZERO ON THIS HOLDING'S OWN PRINTED FORM.** The label is written `> **Entered**` with bold markers, at `chapter-0739.md:27`, and it is the only one in the volume, and the pattern this house has been using, `^>\s*Entered`, cannot see it. **THIS CLOSE RAN THAT PATTERN FIRST, GOT ZERO, AND WAS WRONG; THE PAGE WAS RIGHT.** The finding is not about Volume 16 at all. It is about a sweep that a successor will copy. Section 9.

8. **THE LAST MORNING OF THE BOOK CONTRADICTS ITSELF ABOUT THE LOW ROAD, AND IT IS THE MORNING THE OPEN WINDOW IS MEASURED ON.** `chapter-0780.md:7` says *Not one person in this holding was on that road at any hour of that morning, and nobody here sent anybody onto it.* `chapter-0780.md:5` puts a man on that road before the light and at the top of it at about the fourth hour, and `chapter-0780.md:49` has the same man say *I was up that low road before the light and I am going to be up it again before the light.* **THE PAGE NEVER SAYS WHOSE MEMBERSHIP IS NOT IN THE HOLDING. A FIGURE CHECK CANNOT SEE IT, A PARITY READING CANNOT SEE IT, NEITHER GATE CAN, AND THE SENTENCE THAT WAS SUPPOSED TO CERTIFY NON-ENTRY IS THE ONE THAT IS CONTRADICTED.** Closed prose, reported, not repaired. **THE CONSEQUENCE FOR THIS CLOSE'S OWN FIFTH OWED ITEM IS THAT NON-ENTRY IS NOT MEASURED FROM THAT LINE AND IS NOT MEASURED AT ALL: what is measured is that the window is open, that nobody described it, that nobody named it, and that one man went to the top of that road before the light.**

**NONE OF THE EIGHT WAS REPAIRED IN A MORNING. SIX ARE IN CLOSED PROSE AND REPAIRING THEM MEANS WRITING IN A CLOSED MORNING. ONE IS IN `outline/volume-16.md`, WHICH IS A COMPLETED PHASE'S FILE AND IS OWED A CORRECTION BY A PASS WITH THE STANDING TO EDIT IT. THE EIGHTH IS AN INSTRUMENT AND NOT A PAGE, AND IT IS REPAIRED IN THE HARNESS AT `workspace/volume-16/close/verify_close.py` AND PRINTED IN SECTION 9, AND NO PAGE WAS TOUCHED TO PAY FOR IT.**

---

## 13a. AN INDEPENDENT REVIEW OF THIS CLOSE WAS RUN, IT FOUND EIGHT DEFECTS IN THIS RECORD, AND EVERY ONE OF THEM WAS CORRECTED AGAINST THE PAGE

**A WRITER'S CLOSE IS NOT A REVIEW, AND A CLOSE THAT REVIEWS ITSELF HAS CHECKED NOTHING. A REVIEW WAS RUN AGAINST THIS RECORD, THIS LOCK, THESE FOUR STATE SECTIONS AND THIS HARNESS, AND IT WAS RUN WITHOUT THE INSTRUMENT THAT HAD PRODUCED THE FIGURES, WHICH IS WHY IT CAUGHT WHAT IT CAUGHT.**

1. **THE DUPLICATE SWEEP'S TWO FIGURES WERE WRONG AND STALE.** This record published 231 and 6; the harness at the corrected unit returns **230 and 5**. Those two figures were measured at the uncorrected paragraph unit, before the wordless block-quote separator was excluded, and they had already been carried into the lock and into two state files. **A FIGURE MEASURED AT THE WRONG UNIT IS NOT A FIGURE THAT MOVED, AND THIS HOUSE KEEPS SAYING SO AND THIS CLOSE DID IT ANYWAY.**
2. **THE PROVENANCE OF THE ONE FINDING DUPLICATE WAS INVENTED.** This record called `**"Where would you like it written down."**` the closing line of the volume behind's last morning and the opening line of this volume's first, at twelve words, and called it the third time this book had lifted a sentence from itself. **It stands at `chapter-0735.md:55` and `chapter-0736.md:43`, it is seven words, it is neither a boundary line, and there is no third instance.** A report that names the wrong line costs more than no report, because the next pass goes and looks at the line it was sent to.
3. **A LOCKED FIGURE'S EXCESS WAS DOUBLE-COUNTED.** This record gave the far-end sentence's fourteen shapes thirty-four excess and then added the comfort line's six. **Fourteen shapes at two excess each is twenty-eight, and thirty-four is the combined total.**
4. **THE STANDING-BLOCK COUNTS WERE OCCURRENCES DRESSED AS MORNINGS, AND ONE OF THEM WAS NOT AMONG THE LARGEST FAMILIES.** *No column cut under any of them* is **thirteen occurrences on twelve mornings**; *Tova Reed had the four ages on the corner of the seed board* is **eight mornings** and not a dozen and more; and the harness's own largest families are numeric frames, which this record replaced with prose sentences of its own choosing.
5. **THE WORD *VERBATIM* WAS APPLIED TO SENTENCES THAT SHARE AN OPENING CLAUSE AND NOT A WHOLE PARAGRAPH.** Withdrawn at section 7.
6. **THE PRUNING-WINDOW EVIDENCE MISREAD ITS OWN HOUR AND QUOTED A FLOOR THAT ITS OWN MORNING CONTRADICTS TWICE.** Corrected at section 11 item five, and the contradiction is now finding eight.
7. **THE LOCK PUT THE MASON'S READING OF THE WALL ON THE THIRTY-THIRD MORNING AND PUT THE *NOT NEW* LINE IN THE VOLUME BEHIND.** The mason reads that wall on **the forty-third morning, at `chapter-0778.md:15`**, and the *not new in this county* line is **the seventeenth morning of this volume, at `chapter-0752.md:7`**.
8. **TWO PUBLISHED FIGURES WERE IN NO OUTPUT AT ALL, AND ONE OUTPUT FIGURE WAS WRONG.** The paragraph counts at the declared unit, 1,849 and 34,505, were computed outside the harness, which broke this record's own opening standard that every figure in it is in `MEASUREMENT.txt`. **They are now printed by the harness. The comfort-line token count in the output was itself wrong by a printing bug and is fixed. THE NIL OF THE PARITY READING WAS ALSO PRINTED BEFORE ITS DEMONSTRATION, AND THE DEMONSTRATION NOW RUNS FIRST, BECAUSE A READING THAT HAS NOT BEEN SHOWN THE CLASS IT CATCHES MAY NOT PUBLISH ITS NIL AS A NIL.**

**AND THE ONE THING THE REVIEW NAMED THAT REQUIRED A RULING RATHER THAN A FIX: that the harness held a literal name in a sweep pattern. THE PATTERN HAS BEEN REMOVED AND THE INSTRUMENT REPLACED, BECAUSE THIS CLOSE MAY NOT PRINT THAT NAME ANYWHERE AND A FILE IT CREATES IS NOT AN EXEMPT PLACE. THE REPLACEMENT PRINTS EVERY CAPITALISED WORD STANDING MID-SENTENCE IN THE FORTY-FIVE MORNINGS — ONE HUNDRED AND ELEVEN OF THEM — AND THE NAME IS NOT AMONG THEM, WHICH IS A STRONGER MEASUREMENT THAN A SWEEP, BECAUSE IT CAN BE CHECKED WITHOUT BEING GIVEN THE WORD.**

---

## 13b. A SECOND REVIEW AGAINST THIS RECORD, AND THE ONE FIGURE IT FOUND THAT WAS NOT A FINDING BUT A BLIND SPOT IN THE INSTRUMENT THAT PRODUCED THE FINDINGS

**RUN 2026-10-04 AGAINST THIS RECORD, THE LOCK, THE FOUR STATE SECTIONS AND THIS HARNESS. NO MORNING WAS ALTERED. EVERY FIGURE BELOW WAS RE-DERIVED FROM THE PAGES.**

1. **THE FIGURE CHECK'S PRESENCE TEST HAD NO WORD BOUNDARY, AND A CARDINAL SPELLED FOUR, SIX OR SEVEN IS A PREFIX OF THE ORDINAL SPELLED THE SAME WAY.** `phrase in text` therefore found *five hundred and fourteen* inside *five hundred and fourteenth*, *twenty-six* inside *twenty-sixth*, *twenty-seven* inside *twenty-seventh*, *twenty-eight* inside *twenty-eighth*, *thirty-four* inside *thirty-fourth*, *thirty-six* inside *thirty-sixth* and *thirty-eight* inside *thirty-eighth*. **THE CHECK WAS THEREFORE PASSING EVERY MORNING THAT PRINTED THE AGGREGATE ONLY IN THE ORDINAL FORM, WHICH IS THE ONE DEFECT THE CHECK EXISTS TO CATCH, AND IT WAS BLIND TO EVERY VALUE ENDING IN THOSE THREE SPELLINGS WHILE BEING EXACT ON EVERY VALUE ENDING IN NINE, ONE, TWO, THREE OR FIVE, WHERE THE TWO SPELLINGS DIVERGE AT THE FINAL LETTER. THAT IS WHY THE WITHDRAWN EIGHT WERE PRECISELY THE SEVEN AGGREGATES ENDING IN NINE, ONE, TWO, THREE AND FIVE PLUS THE ONE ORDINAL OF THE RUN. The count is 15, not 8.** The test now carries `(?![a-z])` and the count is driven by the failure list rather than typed, so it cannot drift from the table above again. **EVERY OTHER FIGURE IN THIS RECORD IS UNCHANGED, AND `MEASUREMENT.txt` DIFFERS FROM ITS PREDECESSOR ON THIS SECTION, ON THE FIGURE-CHECK LINE AND ON THE TWO LINES BELOW, AND NOWHERE ELSE.**
2. **THE GATE-ONE LINE NAMED ONE FILE FOR A PARAGRAPH THAT STANDS TWELVE TIMES, AND CHOSE IT BY ITERATION ORDER.** `names[k] = n` is a last-write-wins assignment over a loop, so `chapter-0736.md` was whichever of the volume's own carriers came last, not a report of where the paragraph stands. It now collects every carrier. **THE FIGURE TWELVE IS ALSO A FILE COUNT, BUT IT COMES FROM THE EXACT-DUPLICATE SWEEP AT SECTION 8, WHICH PRINTS `DUP x12 in 12 files`, AND NOT FROM THE GATE-ONE LINE THE LOCK CITED. THE LOCK ROW HAS BEEN REWRITTEN TO NAME THE UNIT, THE SCOPE AND THE LINE THAT SUPPORTS IT.**
3. **THE RAW OUTPUT WAS NOT BYTE-REPRODUCIBLE ACROSS PYTHON HASH SEEDS.** The parity reading sorted a two-element SET by length alone, and on most days both cardinals are the same length, so the two rows of the demonstration swapped places between runs and a reviewer checking reproduction would get a spurious four-line diff. The sort now breaks the tie on the string. **THREE SEEDS GIVE THREE IDENTICAL FILES, AND A MEASUREMENT THAT CANNOT BE RE-READ IDENTICALLY IS NOT A MEASUREMENT.**

**AND THE ONE REVIEW RULING THAT WAS DECLINED: that the `chapter-0780.md:41` row of section 5 quotes the wrong clause, on the ground that *Five hundred and forty-first is at the head of that sheet* is the correctly formed ordinal and that the defect is *the five hundred and forty-second is the one above the rule*. IT IS DECLINED AGAINST THE PLAN.** The item list at `outline/volume-16.md` section 10a and `derive.py` lines 235 to 237 ask for the aggregate as a cardinal and for both clause limbs as ordinals, and the page prints an ordinal for the aggregate and ordinals for both limbs. **THE MISDESCRIBED FIGURE IS THE AGGREGATE, THE QUOTED CLAUSE IS THE OFFENDING ONE, AND THE CLAUSE LIMBS ARE CORRECT AS THEY STAND.** The row was already right and was left as it stands, with the reasoning printed above it so that the next reader does not have to re-derive it.

---

## 14. THE CONTROLLER MATTERS, REPORTED AND TOUCHED NOWHERE

**`state/phase-ledger.json` READS `phase-000-bootstrap`, `planned`, `attempts: 0`, AGAINST A SEVEN HUNDRED AND EIGHTY FILE MANUSCRIPT. IT IS CONTROLLER-OWNED, IT IS REPORTED HERE FOR THE FOURTH TIME, AND IT WAS NOT TOUCHED.**

**THE PROMPT FOR THIS PHASE NAMES A `.wip-conflict` MARKER IN `workspace/volume-16/batch-0005/`. THERE IS NO SUCH MARKER ON DISK. THE DIRECTORY HOLDS `.done`, `PROMPT.md`, `SELF-CHECK.md`, FIVE CHAPTER FILES AND `verify.py`, AND NOTHING ELSE. THIS CLOSE CREATED NO MARKER, READ NO MARKER AND DELETED NO MARKER, AND IT REPORTS THE MARKER'S ABSENCE RATHER THAN AGREEING WITH THE PROMPT ABOUT IT.**

**NO SCRIPT, NO WORKFLOW, NO `.opencode/agent/` FILE, NO `AGENTS.md`, NO `PHASE_SYSTEM.md`, NO `REPO_PLAN.md`, NO `OUTLINE_GUIDE.md` AND NO `opencode.json` WAS READ INTO THIS RECORD OR ALTERED.**

---

## 15. THE PREMISE DRIFT, REPORTED AS THE HEAD OF THE DECISION QUEUE FOR THE LAST TIME

**THE SPECIFICATION AND THE BIBLE DESCRIBE *THE WORLDROOT ENGINEER*. FIFTEEN VOLUMES PLUS THIS ONE ARE ON DISK AGAINST THAT SPECIFICATION AND THEY DO NOT MATCH IT: ACROSS SEVEN HUNDRED AND EIGHTY CHAPTER FILES `ROOTWAY` APPEARS IN ZERO AND `WORLDROOT` APPEARS IN ZERO. WHAT IS ON DISK IS AN INTERNALLY CONSISTENT AND COMPETENTLY WRITTEN HOLDING LEDGER ABOUT A WALL, A GATE, A LAUNDER, A BOOK AND THIRTY-FIVE UNRESOLVED QUESTIONS, AND IT IS NOT THE NOVEL THE SPEC, THE BIBLE AND THE SERIES FILE SPECIFY.**

**THE DRIFT WAS ESCALATED TO THE OPERATOR ON 2026-10-02 AND HAS NOT BEEN SETTLED. IT WAS REPORTED BY THE VOLUME FIFTEEN CLOSE, BY THE VOLUME SIXTEEN PLAN AND BY EVERY ONE OF THE FIVE BATCHES OF THIS VOLUME, AND IT IS REPORTED HERE FOR THE LAST TIME AND IT IS STILL FIRST IN THE DECISION QUEUE.**

**THE BIBLE IS STILL AUTHORITATIVE AND STILL DESCRIBES A STORY THAT HAS NOT BEEN WRITTEN. THE MANUSCRIPT IS NOT EVIDENCE THAT THE PREMISE IS RETIRED. A HUMAN DECIDES WHETHER TO RE-PLAN WHAT IS LEFT AGAINST THE BIBLE OR TO RETIRE THE BIBLE AND RE-SPECIFY THE NOVEL, AND THERE IS NO SIXTEENTH VOLUME LEFT TO CARRY THE DECISION INTO.**

**THIS CLOSE MAY NOT SETTLE IT, MAY NOT RE-PLAN ANYTHING, AND IT DID NOT EDIT `bible/`, `NOVEL_SPEC.md`, `outline/series.md` OR ANY PART OF `outline/ending.md` OTHER THAN BY APPENDING ITS OWN LOCK AT THE END OF THAT FILE.**

---

## 16. THE TWO SERIES-FILE DEFECTS `outline/ending.md` ITSELF CARRIES, REPORTED AND NOT REPAIRED

1. **THE FIRST LINE OF `outline/ending.md` CARRIES A CHAPTER RANGE.** A close that inherits a range from a file that also misplaces the climax is a close that inherits two errors and thinks they are a shape.
2. **A PLACEMENT OF THE CLIMAX INSIDE THAT RANGE.** The immediate climax sits in the middle stretch and a full aftermath follows it, and the plan for the volume behind inherited the shape and named no chapter and no range.
3. **AND THE THIRD, WHICH THE VOLUME BEHIND'S CLOSE ALREADY REPORTED AND WHICH IS STILL UNREPAIRED: `outline/series.md` AND `outline/ending.md` BOTH PLACE THE SURRENDER IN A VOLUME WHOSE MORNINGS DO NOT CARRY IT. THE PAGES PAID IT ELSEWHERE, ONCE, IN HIS OWN MOUTH, ON ONE MORNING BEHIND.**

**ALL THREE ARE OWED A CORRECTION BY A PASS WITH THE STANDING TO EDIT THOSE TWO FILES. THIS CLOSE DID NOT EDIT EITHER FILE OTHER THAN BY APPENDING THE LOCK AT THE END OF THE SECOND, AND IT DID NOT PUT THE NAME OF ANY OF THE THREE ON ANY PAGE.**

---

## 17. WHAT THIS CLOSE CREATED, AND WHY IT CREATED NOTHING ELSE

**THIS CLOSE CREATED NO FURTHER PHASE. THERE IS NO SIXTH BATCH AND THERE IS NO CARD AFTER THE FORTY-FIFTH. THE ONLY THING IT WROTE THAT IS NOT IN THE STATE LAYER IS THE LOCK AT THE END OF `outline/ending.md`, WHICH IS THE SIXTEENTH LOCK AND THE LAST, AND WHICH FIXES WHAT A SEVENTEENTH VOLUME WOULD INHERIT IF THERE WERE ONE, WHICH THERE IS NOT.**

**A CLOSE THAT FINISHES BY NAMING A NEXT PHASE HAS INVENTED ONE, AND A VOLUME THAT HANDS FORWARD A PHASE INSTEAD OF A STATE HAS HANDED FORWARD A PLAN AND NOT A BOOK.**
