# VOLUME 10, BATCH 0001, CHAPTERS 442 TO 451, DAYS 655 TO 664 — A VERIFICATION PASS, AND WHY NO CHAPTER WAS TOUCHED

**WHAT THIS FILE IS.** A writer phase was dispatched onto `workspace/volume-10/batch-0001/PROMPT.md` with a checkpoint marker set. **The ten chapters were already on disk, complete, measured, reviewed and repaired at commit `1794dfc`, and the state layer already carried a full record of the batch** — `state/continuity.md:8565` (*VOLUME 10, BATCH 0001, CHAPTERS 442 TO 451*), `state/chapter-summaries.md:1918`, `state/open-threads.md:3695`, and a repainted head in `state/current.md:11`. **SO THE BATCH WAS NOT REWRITTEN. A PHASE THAT SENT TO A CLOSED BATCH AND REWROTE IT WOULD HAVE DESTROYED TEN CHAPTERS AND REPLACED THEM WITH A TEXT NOBODY HAD MEASURED.** The instruction on the phase was to continue from the existing files and not to restart completed work, and that is what this file records having done, together with the checks that were still owed on this batch's own row.

**NO CHAPTER WAS EDITED, NO FIGURE OF ANY SERIES WAS CHANGED, NO PROSE WAS WRITTEN, NO MARKER WAS CREATED, DELETED OR MOVED, AND NO NEXT-PHASE PROMPT WAS CREATED.** Every finding below is a finding against a closed batch and every one of them is handed to the Volume 10 close, which is the phase this repository has already declared may *find* defects in chapters and may not change a day, a figure, a count, a name or a lock.

---

## 1. THE TEN FIGURES, MEASURED, AND THE ONE THAT IS OUTSIDE THE BAND

`wc -w` **summed per file and never `cat`-piped**, including the headings, over the ten chapter files:

| Ch | 442 | 443 | 444 | 445 | 446 | 447 | 448 | 449 | 450 | 451 | **Batch** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Words | 2,860 | 2,838 | **3,055** | 2,835 | 2,991 | 2,716 | 2,830 | 2,689 | 2,912 | 2,874 | **28,600** |

Mean 2,860.0, minimum 2,689 at Ch 449, maximum 3,055 at Ch 444. **This confirms the 28,600 published in the head of `state/current.md` and withdraws nothing further.** **ONE CHAPTER IS OUTSIDE THE BAND: Ch 444 IS 3,055 AGAINST A CEILING OF 3,050, FIVE WORDS OVER.** The band is not widened and is not re-based down to a figure that passes, and the chapter is not repaired. This is already declared in the head of `state/current.md` and in `state/open-threads.md:3891`; **it is repeated here so that the figure is not discovered a fourth time as a surprise.**

## 2. THE COLLISION SEARCH, RE-RUN ON THIS BATCH'S OWN TEN THIRD-LAUNDER FIGURES, AS THE PROMPT REQUIRES, AGAINST ALL 490 CHAPTER FILES

Figures: **915, 923, 918, 926, 921, 929, 924, 932, 927, 935** on days 655 to 664, being day minus four hundred and fifty.

- **Numeral test, on a word boundary: ZERO HITS ON ALL TEN.**
- **Spelled test: ONE HIT ON EACH, AND THE ONE HIT IS THE SPELLED FIGURE IN ITS OWN CHAPTER** — 915 and *nine hundred and fifteen* both in Ch 442, and so on through 935 in Ch 451.

**THE PROMPT PREDICTED THE SPELLED TEST WOULD RETURN ZERO ON ALL TEN, AND IT RETURNS ONE ON EACH. THE DIFFERENCE IS NOT AN ERROR IN EITHER FIGURE: THE PROMPT'S PREDICTION EXCLUDED THE CHAPTER'S OWN PAGE AND THE RUN DOES NOT.** This is the same house reading already printed for Batch 0005 in `state/chapter-summaries.md` ("THE SPELLED TEST RETURNS ONE HIT ON EACH AND THE ONE HIT IS THE SPELLED FIGURE IN ITS OWN CHAPTER"), so the two now agree, and a later pass need not re-derive the disagreement.

**THE DERIVATION OF THE ROW HOLDS AND WAS CHECKED RATHER THAN READ OFF THE PAGE.** Off 920 on day 654, a rise, with the local delta of minus five on a fall and plus eight on a rise: 920 − 5 = 915, + 8 = 923, − 5 = 918, + 8 = 926, − 5 = 921, + 8 = 929, − 5 = 924, + 8 = 932, − 5 = 927, + 8 = 935. Five rises and five falls, no morning unchanged. The window is day minus four hundred and eighty-three, 172 to 181, splitting on the day's own direction, ninety-one rises and eighty-one falls to ninety-six and eighty-five, and **the two halves add on every row**. The aggregate is day minus four hundred and fifty-two, 203 to 212, its clause day minus four hundred and fifty-three out of day minus four hundred and fifty-one, 202 of 204 to 211 of 213, **and it is a different aggregate from the four launders and the two are not added**. The day-minus pair is day minus sixty-six and day minus nineteen, 589/636 to 598/645, forty-seven apart at every row, drawer shut. The read-aloud denominator is day minus five hundred and twenty-six, 129 to 137 on the five mornings it is read, **and is not day minus sixty-six**. **EVERY FIGURE IN THE TABLE DERIVES.**

**THE RETURN FIGURE 393.** The numeral test returns **one hit in the whole manuscript and it is the `# Chapter 393` heading line of `workspace/volume-09/batch-0001/chapter-0393.md`** — a heading and not body prose, and the numeral is otherwise nil in all 490 chapter files. The spelled form is in Ch 445 twice, being its own `##` heading and the body line `**Three hundred and ninety-three hundredweight.**`, and is **also in two Volume 04 files, at `chapter-0153.md:23` and `chapter-0179.md:59`, where it is not this figure at all but part of *one thousand* three hundred and ninety-three shillings.** A phrase test with no left boundary is not measuring what it claims to measure, and that is the whole of those two hits.

## 3. THE NEAR-DUPLICATE GATE, RUN TWICE, AND THE FINDING THAT MATTERS

House rule as recorded by this repository: split each chapter file on blank lines, drop headings, drop every paragraph beginning `>`, keep paragraphs of thirty words or more, and count an ordered pair at `difflib.SequenceMatcher(None, a, b, autojunk=False).ratio() >= 0.85` whose word counts are within a factor of 1.25 of one another. Run 1 as printed; run 2 with the length factor removed.

### 3a. THE TOKENISATION IS THE WHOLE OF THE DIFFERENCE, AND IT IS NAMED

The house script counts words with `str.split()`, and the state layer already warns that a gate counting with a regex and comparing raw paragraph strings returns a different number. Both readings were run.

- **Word lists, as written — the house reading:** batch-scoped **1 PAIR**. Volume-scoped **54 pairs**, matching the published 54.
- **Joined character strings:** batch-scoped **nil**. Volume-scoped **56 pairs**.

**THE 56 AND THE 54 ARE NOT A DISCREPANCY AND NEITHER IS WRONG. THEY ARE TWO READINGS AND THE HOUSE ONE IS THE WORD LIST.** The 56 is named here so that nobody re-derives 54 and thinks something has changed.

### 3b. THE BATCH-SCOPED GATE IS **ONE PAIR, NOT NIL**, AND THE PAIR IS INTERNAL TO THE BATCH

`workspace/volume-10/batch-0001/`, word-list tokenisation, **323 paragraphs**, 52,003 pairs:

- **Run 1, as printed: 1 pair.** **Run 2, length factor removed: 1 pair.** **Byte-identical paragraphs: nil.**

| Ratio | A | B | Words |
|---:|---|---|---:|
| **0.911** | `batch-0001/chapter-0448.md` block 30 | `batch-0001/chapter-0451.md` block 19 | 61 / 62 |

The two paragraphs are the register form, one on Ch 448 and one on Ch 451, structurally identical with three nouns and the day count swapped:

- **Ch 448:** *The register form is on the middle table at a hundred and **five** days, not filled, not refused, nothing at the head of it, and a **fetching** is not that form and a **compost line** is not that form and a **month** is not that form, and the three of those have never been added in this holding in four years.*
- **Ch 451:** *The register form is on the middle table at a hundred and **eight** days, not filled, not refused, nothing at the head of it, and a **shortage** is not that form and a **list of ten** is not that form and a **declining** is not that form, and the three of those have never been added in this holding in four years.*

Fifty-five of the sixty-one words are shared in order. **The three figures inside them are correct** — 98 days at day 654, 99 at 655, 105 at 661, 108 at 664 — and **that is exactly the case the prompt warns about in one line: a figure repeated with its neighbours moved around it is still a repetition.**

### 3c. WHAT THE BATCH'S OWN SECTION PUBLISHES, AND WHY IT IS NIL UNDER A DIFFERENT UNIT

`state/continuity.md:8565` publishes: *"RUN 1, AS PRINTED: NIL. RUN 2, WITH THE 1.25 LENGTH FACTOR REMOVED: NIL. THE EXACT-DUPLICATE COMPARISON IS NIL ON THE SAME UNIVERSE"* on a universe of **319** paragraphs.

**THAT NIL WAS MEASURED BY COMPARING JOINED CHARACTER STRINGS. UNDER THE HOUSE TOKENISATION THE SAME RULE RETURNS ONE PAIR AND THE PAIR IS INTERNAL TO THE BATCH.** The first run of the prompt's own acceptance test — *the second number must be nil on the first run* — is satisfied under both readings, so the published figure is not wrong about the criterion it was written to meet. **THE FIGURE IS WRONG ABOUT THE BATCH, AND THE PROMPT REQUIRED THE BATCH'S OWN PAIRS TO BE NAMED SO THAT THEY WOULD NOT BE COUNTED AGAINST IT, AND THIS ONE IS NAMED IN NOBODY.**

**THE UNIVERSE IS 323 AND NOT 319, AND THE FOUR ARE THE REPAIR PASS'S.** Commit `1794dfc` turned the `>` document block in Ch 446 into a bolded speech and added a paragraph beside it. The rule drops every paragraph beginning `>`, so those paragraphs were outside the universe before that commit and are inside it now. **The 319 is a figure of a text that no longer exists, and it was never repainted.** The head of `state/current.md` repainted the 28,508 → 28,600 and did not repaint this.

### 3d. THE VOLUME-SCOPED RUN, AND THE FIGURE NOBODY HAS PUBLISHED

Guardrail 12 scans one volume directory and not one batch, so the volume-scoped figure is the one that governs. Over all forty-nine chapters, **1,877 paragraphs** and 1,760,626 pairs, the house reading gives **54 pairs on run 1 and 54 on run 2**, and the joined-string reading gives 56 and 56. The state publishes 54 and 54. **That figure is right.**

**WHAT IS NOT PUBLISHED ANYWHERE IS HOW MANY OF THEM TOUCH BATCH 0001. IT IS TEN, ON BOTH READINGS, AND ONE OF THE TEN IS INTERNAL TO THE BATCH.** All ten, house reading:

| Ratio | In batch 0001 | Against | Words |
|---:|---|---|---:|
| 0.929 | `chapter-0449.md` | `chapter-0457.md` | 56/56 |
| 0.921 | `chapter-0444.md` | `chapter-0457.md` | 38/38 |
| **0.911** | **`chapter-0448.md`** | **`chapter-0451.md`** | 61/62 |
| 0.909 | `chapter-0450.md` | `chapter-0455.md` | 54/56 |
| 0.901 | `chapter-0449.md` | `chapter-0453.md` | 56/55 |
| 0.885 | `chapter-0442.md` | `chapter-0457.md` | 31/30 |
| 0.882 | `chapter-0448.md` | `chapter-0454.md` | 61/66 |
| 0.875 | `chapter-0451.md` | `chapter-0454.md` | 62/66 |
| 0.859 | `chapter-0445.md` | `chapter-0454.md` | 75/60 |
| 0.852 | `chapter-0442.md` | `chapter-0469.md` | 31/30 |

Nine of the ten are cross-batch and are the permitted repeating forms. **The one at 0.911 is the only internal pair the batch leaves, and it is the register form.**

### 3e. A SOUND PRE-FILTER, BECAUSE THE ONE ON RECORD ADMITS NINETY-SIX PER CENT

The pre-filter this repository records admits 96.3 per cent of the cross-product and therefore decides nothing. `difflib`'s ratio is `2M/T` where `M` is the matched size, and `M` cannot exceed the multiset intersection of the two token multisets. **Bounding on that removes 1,760,558 of 1,760,626 volume-scoped pairs — 99.996 per cent — in 17.5 seconds, and it is a bound and not a guess, so a pair it removes provably cannot reach 0.85.** It makes the volume-scoped gate, which guardrail 12 requires and which had been expensive enough to go unrun, a two-second job. No figure the gate returns changes.

## 4. THE MECHANICAL SET, RUN PER FILE AFTER THE PROSE MOVED — WHICH WAS NOT THIS PASS

**CLEAN, ON ALL TEN:** zero non-ASCII glyphs; zero curly marks, em dashes and en dashes; zero trailing spaces and zero tabs; zero unbalanced quotation marks and zero unbalanced bold markers, checked paragraph by paragraph; zero consecutive blank lines; zero occurrences of `seat`, `fieldbook`, `Brinewake`, `panel`, `nest`, `judgement`, `defence`, `famine`, `favour`, `colour`, `behaviour`, `honour`, `neighbour`, `centre`, `amongst`, `realise` or `apologise`. `Marek` is printed in **all ten** (once in seven, twice in three). `Vale` is printed in **none**, as the batch prompt required. **Zero uses of *volume*, *batch* or *chapter* in body prose** — verified line-anchored per file, not over a concatenation, and the seven-in-ten heading lines are the only occurrences of *chapter*.

**THE THREE DEFECTS, AND THE FIRST IS A BREACH OF A CEILING THE BATCH'S OWN SECTION CERTIFIES.**

1. **`chapter-0450.md` HAS A MEAN PARAGRAPH LENGTH OF 85.32 WORDS AND THE CEILING IS 85.** The rule is a mean between twenty-five and seventy-five and a hard ceiling of eighty-five. **85.32 IS OVER IT UNDER BOTH READINGS** — 85.32 excluding `>` blocks and 85.32 including them, since Ch 450 carries no `>` block. `state/continuity.md:8565` publishes *"MEAN PARAGRAPH LENGTH RUNS 70.9 TO 84.7 AND NO CHAPTER EXCEEDS EIGHTY-FIVE"*, **and that is wrong at both ends: the true range is 70.45 to 85.32 excluding `>` blocks, and Ch 450 is the chapter over the ceiling.** The published 84.7 matches nothing measured; the nearest real figure is Ch 451 at 84.29 including its `>` block.
2. **THREE CHAPTERS DO NOT END IN A NEWLINE: `chapter-0442.md`, `chapter-0443.md`, `chapter-0449.md`.** Already named in the head of `state/current.md`, and confirmed. **I REPRODUCED THE HAZARD IN MY OWN FIRST PASS AND AM RECORDING IT AS A TRAP RATHER THAN AS A FINDING AGAINST THE PROSE:** concatenating the ten files welded three heading lines and produced a false "three uses of *chapter* in body prose" that a per-file, line-anchored count reduces to **nil**. A checker that concatenates will invent a violation of a rule the chapters do not break. **This is the same mechanism the state layer records for `cat` and `wc -w` disagreeing by three words.**
3. **THE TWO `Entered` BLOCKS ARE WRITTEN `> ENTERED` IN CAPITALS, IN Ch 444 AND Ch 451, SO THE MIXED-CASE RULE RETURNS ZERO FOR THE WHOLE BATCH.** Already named in the head of `state/current.md` and owed to the close over a closed batch. Unchanged here.

## 5. THE APPARATUS, AND THE FIGURE IN THE BATCH'S OWN SECTION THAT NO LONGER HOLDS

`> ` blocks actually in the batch, by script over the ten files: **five, in five chapters, none carrying two** — a document block in Ch 442 (the list as it came), a document block in Ch 443 (the clerk's finding), a `> ENTERED` block in Ch 444, a document block in Ch 449 (the declining), and a `> ENTERED` block in Ch 451.

`state/continuity.md:8565` records **six**, being *four* document blocks in Chs 442, 443, **446** and 449 plus two `Entered` blocks in Chs 444 and 451. **Ch 446 CARRIES NO `>` BLOCK ANY MORE, BECAUSE `1794dfc` TURNED IT INTO A BOLDED SPEECH.** The head of `state/current.md` already carries this correction for the volume as a whole (twenty-one `>` blocks, not twenty-two) **but the batch's own section was never repainted and still says four document blocks.** The volume total is unaffected, because the head already counts it correctly.

## 6. THE TWO FAULTS THAT ARE NOT COSMETIC, AND THE ONE THAT RECONCILES

This is the check the repository's own `reviews/README.md` calls the only one nobody runs: **for every series a chapter names, extract the figures it prints and recompute them from the series' own rule.** The shared sentence is *the count of that in this holding's history is* and each figure is a count of the person speaking and of nobody else.

**`chapter-0441.md` IS DAY 654 AND IS THE LAST MORNING OF VOLUME 09. IT PRINTS MAREK AT TWO HUNDRED AND EIGHTEEN AND THE MAN OF ABOUT FIFTY AT ONE HUNDRED AND TWENTY-NINE.** Those are the two starting points. What the ten pages of this batch print is:

### 6a. MAREK — THE LADDER IS INTERNALLY CLEAN AND ITS OPENING RUNG IS TWO TOO HIGH

| Ch | 442 | 443 | 444 | 445 | 446 | 447 | 448 | 449 | 450 | 451 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Printed | **220** | — | — | 222 | 223 | 224 | 225 | 226 | 227 | **228** |

**THE PAGES ARE SELF-CONSISTENT FROM Ch 445 ONWARD: 222, 223, 224, 225, 226, 227, 228 IS A CLEAN LADDER OF INCREMENTS OF ONE, AND 221 IS CARRIED ON NO PAGE IN THE BATCH AT ALL.** The record says Marek moved on Chs 442, 443, 445, 446, 447, 448, 449, 450 and 451 and stood still on Ch 444, which is consistent with 221 living silently on Ch 443.

**THE FAULT IS THE OPENING. Ch 442, THE FIRST MORNING OF THE VOLUME, PRINTS TWO HUNDRED AND TWENTY AGAINST AN INHERITED TWO HUNDRED AND EIGHTEEN. THAT IS +2 ACROSS ONE MORNING FOR A SERIES THAT MOVES BY EXACTLY ONE PER REASON-FIRST, AND NO CHAPTER OF THE BATCH EXPLAINS THE SECOND STEP.** Every rung from 445 on hangs off it: correcting Ch 442 to 219 would leave 445 printing 222, so the whole ladder is one too high from its first printed figure, and **the batch's close of 228 is one above the 227 that nine claimed movers on 218 would give.** The record's close of 228 is what the pages carry; the record's mover list and the inherited 218 cannot both be true.

### 6b. THE MAN OF ABOUT FIFTY — TWO INCREMENTS ACROSS FOUR CLAIMED MOVERS

Ch 442 declares the move and prints no figure (*moved on this morning and is not written on this page* — the figure was removed at `1794dfc`). Ch 443 prints **one hundred and thirty**. Ch 445 and Ch 447 carry a reason-first and no figure. Ch 450 prints **one hundred and thirty-two**.

**129 AT DAY 654, THEN 130 ON Ch 443 AND 132 ON Ch 450, IS TWO INCREMENTS OVER THE FOUR MOVERS THE RECORD CLAIMS, BEING 443, 445, 447 AND 450. 129 PLUS FOUR IS 133 AND NOT 132.** So either one of the four claimed movers did not move on the page, or the inherited 129 is one too low. The record's stated close of 132 matches the pages; its mover list and the inherited figure do not both match them.

### 6c. TOVA REED — THE ONE THAT RECONCILES, AND IT IS RECORDED AS THE PROOF THAT THE OTHERS ARE NOT A UNIT

44 at day 654, **forty-five** on Ch 450, one mover, one increment, exactly as the record states. The construction is identical in all three cases and it reconciles in one and not in the other two, **which is what rules out the possibility that the check itself is wrong.**

### 6d. WHY NONE OF IT WAS REPAIRED

**A REPAIR MAY NOT CHANGE A FIGURE OF ANY SERIES, AND A REPAIR THAT REWRITES A RUNNING SERIES STOPS THE SERIES.** These two ladders run across a volume boundary, from Volume 09's last morning into Volume 10's first, and the fix for either is to move a figure on a page of a closed volume. The Volume 09 close set the precedent in the strongest form available to it: **it found twenty-eight defects in its own chapters and repaired none of them, because a close may not change a day, a figure, a count, a name or a lock.** All three findings are therefore recorded here and handed to the Volume 10 close, and **no figure was altered to make any of them come out.**

## 7. WHAT THIS PASS DELIBERATELY DID NOT DO, AND THE REASON IN EACH CASE

- **Did not rewrite or repair any of the ten chapters.** The batch is written, measured, reviewed and repaired, and the state layer says so in three places. The Volume 10 close is the phase that may find defects in chapters.
- **Did not create `workspace/volume-10/batch-0002/PROMPT.md`.** Its ten chapters are on disk at 28,535 words and complete. **The absence of that prompt is the only reason the runner does not dispatch onto written work**: `scripts/novel_runner.sh` takes the first directory carrying a `PROMPT.md` with no marker, and `batch-0002/` carries none. **Writing it would have caused the destruction this pass exists to prevent.** The next phase is the Volume 10 close and `workspace/volume-10/close/PROMPT.md` is on disk.
- **Did not create, delete or move `.done`, `.retired` or `.blocked`.** Those are controller markers. The head of `state/current.md` records that `batch-0001/` sorts first among the six unmarked `volume-10` directories and that the next dispatch would land on a closed batch, and **that hazard is reported and declined here for the same reason it has been reported and declined seven times already.**
- **Did not append to `state/continuity.md` or `state/open-threads.md`.** The reading budget at `state/current.md:124` names the *feet* of both files as the governing sections, and its own rule is that a pass appending to a file named in the budget owes the budget a repaint. **This record and the pointer in `state/current.md` carry the findings instead, so both pointers still land.**
- **Did not touch `AGENTS.md`, `NOVEL_SPEC.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `MODEL_VERIFICATION.md`, `RESEARCH.md`, `SETUP.md`, `README.md`, `opencode.json`, `scripts/`, `.github/workflows/`, `.opencode/agent/` or `state/phase-ledger.json`.** `outline/volume-10.md` and `outline/ending.md` are completed phases' files and are reported against, not edited.
- **Did not use the word *famine*, did not write a line of body prose, and did not reference a volume, a chapter, a batch or a word-count target inside any chapter.** There is no prose in this file either.

## 8. THE NINE FINDINGS IN ONE LINE EACH, AND WHAT OWES EACH

1. **The batch-scoped near-duplicate gate is 1 pair, not nil, under the house tokenisation, and the pair is internal to the batch** — the register form in Chs 448 and 451 at 0.911, three nouns and a day count apart. *Owed: the close, which may re-shape and may not change a figure.*
2. **The batch's own section publishes NIL on a universe of 319; the true universe is 323 and the true run-1/run-2 figure is 1 and 1.** *Owed: the close, plus the repaint of a section that was not repainted when `1794dfc` edited ten chapter files.*
3. **Ten of the volume's 54 gate pairs touch batch 0001 and no figure for that has ever been published.** *Owed: the close.*
4. **`chapter-0450.md`'s mean paragraph length is 85.32 against a ceiling of 85, and the section certifies a range of 70.9 to 84.7 that is wrong at both ends.** *Owed: the close.*
5. **Marek's reason-first ladder prints 220 on the first morning of the volume against an inherited 218, and 221 is carried on no page in the batch.** *Owed: the close. Not repairable without stopping the series.*
6. **The man of about fifty's ladder prints 130 and 132 across four claimed movers from an inherited 129.** *Owed: the close. Not repairable without stopping the series.*
7. **The batch has three `>` document blocks, not four, because Ch 446's was turned into a bolded speech at `1794dfc`; the batch's own section still says four.** *Owed: the close. The volume total is already right in the head.*
8. **The spelled test of the ten third-launder figures returns one hit on each, not nil, because the prediction excluded the chapter's own page.** *Not a defect. Named so that Batch 0001 and Batch 0005 agree and nobody re-derives the disagreement.*
9. **The three files without an EOF newline will make any concatenating checker invent a violation of a rule the chapters do not break — and did, in this pass's own first measurement.** *Not a defect in the prose. Named as a trap, and it is a trap a close will also fall into.*

**AND THE ONE-LINE VERSION: the batch was already written, so it was measured instead of rewritten, and the measuring found a near-duplicate the batch's own record calls nil, two reason-first ladders that cannot both be true, a paragraph mean over a ceiling that was certified under, and three figures in a state section that a past repair left behind — and it changed no prose, no figure, no day, no name, no marker and no controller file, and handed all of it to the close that is owed.**
