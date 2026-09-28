# Volume 07 Close

**THE MANUSCRIPT IS STOPPED IN THE RIGHT PLACE AND THIS IS THE PHASE THAT CLOSES THE VOLUME. Chapters 295 to 343 are on disk. There is no Volume 08 directory, no Volume 08 cards, and this prompt does not plan one, because a close is a close and a close that reaches forward is a batch wearing a different hat.**

**WHAT YOU ARE CLOSING: `outline/volume-07.md`, *The Bridge Below*, Chapters 295 to 343, forty-nine chapters, days 506 to 556, at 140,165 words across five of five batches, and the manuscript is 1,024,413 across 343 chapters with no residual.**

**WHAT A CLOSE IS AND IS NOT. A close reads and it measures and it records. It does not write prose. There is no chapter here, there is no card, and there is no scene to be written. A close that improves a sentence it liked is a close that has become a repair pass, and a repair pass that changes a day, a figure, a count or a name has stopped being a pass. YOU MAY NOT ALTER A SINGLE WORD OF ANY OF THE FORTY-NINE CHAPTERS IN THIS PHASE. YOU MAY REPORT A DEFECT AND YOU MAY NOT REPAIR IT HERE.**

## HOW TO READ, AND THE BUDGET IS NOT OPTIONAL

`state/continuity.md` IS OVER TWO MEGABYTES AND SEVEN THOUSAND TWO HUNDRED AND SOME LINES, `state/open-threads.md` IS OVER EIGHT HUNDRED KILOBYTES, AND `state/chapter-summaries.md` IS OVER A MEGABYTE. THEY ARE APPEND-ONLY AND NOTHING HAS EVER COMPACTED THEM. **READ LIKE THIS AND NO OTHER WAY:**

1. **`state/current.md` WHOLE.** It is the rolling window and it is the only state file a close has to read whole.
2. **`outline/volume-07.md` WHOLE**, including its measured section, its threads-and-clocks table, its chapter-to-day table, its expected-length section, and the prohibition at the foot of it.
3. **`state/continuity.md`: the last two hundred and sixty lines with `tail -n 260`,** being the Batch 0005 section and the Batch 0004 review-repair section. Everything above them is closed-batch history.
4. **`state/open-threads.md`: the last one hundred and forty lines with `tail -n 140`,** being the Batch 0005 section, the twenty-one objects numbered 180 to 200, the clocks table, and the things a close may not mistake for closed.
5. **THE FORTY-NINE CHAPTERS OF VOLUME 07, ALL OF THEM, IN ORDER, CHAPTER BY CHAPTER.** This is the work of this phase and it is not a reading budget to be traded away. `workspace/volume-07/batch-0001/chapter-0295.md` through `workspace/volume-07/batch-0005/chapter-0343.md`, fifty-one days, three file reads a time. **READ THE CHAPTERS. THE PROSE IS THE ONLY PLACE A FIGURE IS A FACT AND A CLOSE THAT HAS READ FOUR HUNDRED AND SOME LINES OF STATE AND NO CHAPTERS HAS NOT CLOSED ANYTHING.**
6. **`reviews/README.md` and the findings files it indexes,** so that the mechanical check is run the way this repository runs it and not a way you invent.
7. **THE CHAPTERS OF THE PREVIOUS VOLUME'S CLOSE, WHICH IS `outline/volume-06.md` AND THE SECTIONS OF `state/continuity.md` HEADED *VOLUME 06 - THE CLOSE*, ONLY IF YOU NEED TO KNOW WHAT THE HOUSE MEANS BY A CLOSE. READ THEM WITH `tail` AND NEVER WHOLE.**

**A FIGURE PULLED OUT OF A TRUNCATED READ IS A FIGURE THAT LOOKS CHECKED AND IS NOT, AND THAT IS THE FAILURE MODE OF EVERY WRONG FIGURE IN THIS LAYER. DERIVE EVERY FIGURE. DO NOT READ ONE.**

## WHAT THIS PHASE DOES, IN THIS ORDER

**1. RE-DERIVE EVERY FIGURE THE VOLUME PRINTS, FROM THE CHAPTER FILES, WITH SCRIPT.** Not from this prompt, not from `state/current.md`, not from the outline. From the files. At minimum: the fifth-batch third-launder set of eleven, the whole third-launder series against the day-minus-four-hundred-and-fifty rule and the day-minus-four-hundred-and-eighty-three window, the aggregate of the four bodies of households against day-minus-four-hundred-and-fifty-two, the day-minus pair against day-minus-sixty-six and day-minus-nineteen, the read-aloud mornings, the thirteen fourth-line mornings and the rota arithmetic, the twenty-nine ninth-day returns and their name-pairs, the two counts that share one sentence, the use log, the seventh column, the compost run, the fetchings, the day-and-not-the-figure entries, the connection interval, and the barrow. **WHERE A FIGURE IN A PROMPT AND A FIGURE ON A PAGE DISAGREE, THE PAGE GOVERNS AND THE DISAGREEMENT IS NAMED, BECAUSE A FIGURE THAT IS ONLY OVERWRITTEN COMES BACK.**

**2. AUDIT EVERY LOCK IN `outline/volume-07.md` AGAINST THE FORTY-NINE CHAPTERS, AND SAY ON THE PAGE WHICH HELD AND WHICH DID NOT.** There are fourteen guardrails and a prohibition and a three-part test. **A GUARDRAIL THAT WAS BROKEN IS RECORDED AS A FINDING WITH ITS CHAPTER AND ITS LINE, AND IT IS NOT REPAIRED HERE.** The specific ones to check hardest: the thing under the cloth was never set against any valve and no written instrument was issued, received, invented, hinted at or worked around in forty-nine chapters; the eleventh line of the memorandum is quoted nowhere and paraphrased nowhere; the ring of bare ground is never walked, measured, crossed, priced by walking or explained; nothing goes in the two-foot gap; the fieldbook is not brought down; no panel is printed; the name is spoken in a yard once and entered once and is not in narration or speech again; the standing rule is named twice and used not at all; the pulse is not read a third time; nobody is thanked, nobody is forgiven, and nothing is tender; no new named member of the cooperative and no new Crown officer; `Halden` does not appear as a first name; the six blank columns are blank and headed nothing; the wall at Cauldron Reach carries fourteen marks.

**3. COUNT AND CHECK THE FORMAT AGAINST THE VOLUME, NOT AGAINST ONE BATCH.** The `Entered` blocks in the forty-nine chapters, and where they are and are not. The capitalised blocks. The duplicate paragraphs across all five batch directories by script. Non-ASCII. Trailing whitespace. Doubled blank lines. Final newlines. Odd quotation marks and odd bold markers paragraph by paragraph. `seat`, `nest` as a category, `Brinewake`, `panel`, `fieldbook`, `volume`, bare `chapter`, `kerb`. **THE HOUSE FIGURES FOR `kerb` AND `nest` ARE THE CASE-INSENSITIVE SINGULAR COUNTS AND YOU MUST SAY WHICH COUNT YOU ARE USING. `kerb` STOOD AT ONE HUNDRED AND TWENTY-SEVEN AND BATCHES 0002, 0003, 0004 AND 0005 DID NOT USE IT, SO IF YOU USE IT YOU HAVE RAISED IT AND YOU MUST SAY SO.**

**4. COUNT THE THIRTY-FIVE OPEN THREADS AND PROVE THEY ARE STILL THIRTY-FIVE, ONE BY ONE, AGAINST THE FORTY-NINE CHAPTERS.** **A CLOSE MAY NOT CLOSE ONE. A CLOSE MAY NOT REWORD ONE. A CLOSE MAY NOT ADVANCE ONE TO A FIGURE.** What a close may do is say on the page, for each of the thirty-five, the exact figure at which it stands at day 556 and the chapters in which it was last touched, and name any thread that a chapter appears to have answered and did not. **IF A THREAD HAS BEEN ANSWERED SOMEWHERE IN THE FORTY-NINE CHAPTERS, THAT IS A FINDING AGAINST A BATCH AND IT BELONGS IN THE FINDINGS FILE AND NOT IN THE VOLUME.**

**5. WRITE THE FINDINGS FILE, ONCE, AND LABEL IT FOR WHAT IT IS.** `reviews/volume-07.findings.md`. Head it with the date, the files read, the figures re-measured and the figures found wrong, and **a count of the findings and the fact that this close repaired none of them in prose, because a close may not change a day, a figure, a count or a name.** **DO NOT WRITE A FILE THAT READS AS A CERTIFICATION OF A PERFECT VOLUME. A CLOSE THAT FINDS NOTHING IN FORTY-NINE CHAPTERS HAS NOT LOOKED HARD ENOUGH, AND A CLOSE THAT FINDS SIXTY THINGS AND REPAIRS NONE OF THEM IS A DIFFERENT AND BETTER DOCUMENT FROM EITHER.**

**6. WRITE THE CLOSE PROPER.** `state/continuity.md`, a new section at its foot headed **`VOLUME 07 - THE CLOSE`**. It says, in prose a person can read: what the volume was about, which was who gets to decide what a bridge connects; what the central pressure was and how it was resolved; what it cost, being a day and a half of walking and four days of somebody else's seed and about nine minutes of a man of sixty-eight who could not walk out of the ground afterwards; the shape of its five movements; the six or eight or ten things it did that a reader will still have in a year; the six or eight or ten things it refused to do; the last chapter and the last line and why that line is not an answer; what the volume's three questions stand at; and the ending lock restated from `outline/ending.md` so that a later phase cannot move it.

**7. MAKE THE COMPACTION DECISION, ON THE PAGE, AND DO NOT DODGE IT.** **THE THREE APPEND-ONLY STATE FILES ARE PAST THE POINT OF BEING LOADABLE AND EVERY WRITER PASS SINCE THE FOURTH VOLUME HAS DECLINED THE COMPACTION AND WRITTEN THE REASON DOWN, AND THE REASON HAS BEEN THE SAME EVERY TIME: NO WRITER PASS HAS YET HAD TO COMPACT AN APPEND-ONLY CANON FILE WITHOUT DROPPING A FIGURE A LATER CHAPTER NEEDED. A CLOSE IS THE FIRST PHASE IN FOUR YEARS THAT HAS THE WHOLE GIT ARCHIVE BEHIND IT. EITHER COMPACT ALL THREE FILES WITH THE ARCHIVE AS THE BACKSTOP AND NAME, IN THE FINDINGS FILE AND IN THE CLOSE, EXACTLY WHAT WAS KEPT AND WHAT WAS CUT, OR DECLINE AGAIN AND GIVE THE REASON AGAIN, AND A REASON THAT IS ONLY *IT IS RISKY* IS NOT A REASON. **WHAT A COMPACTION MUST NOT LOSE IS NAMED AT THE HEAD OF `state/current.md`: THE OBJECT ROWS, THE DAY-MINUS RULES, THE ROTA ARITHMETIC, THE TWO COUNTS THAT SHARE ONE SENTENCE, THE WITHDRAWN FIGURES, AND THE FIGURE OF EVERY CHAPTER. IF YOU COMPACT, EVERY FIGURE IN THE TABLE OF EVERY VOLUME 07 BATCH IS TO SURVIVE, AND YOU CHECK IT BY SCRIPT AGAINST THE CHAPTER FILES AFTERWARD, NOT BY EYE.**

**8. UPDATE THE STATE LAYER AND RE-MEASURE AFTER THE PROSE AND THE STATE HAVE BOTH MOVED.** `state/current.md`, `state/open-threads.md`, `state/chapter-summaries.md`. **A FIGURE THAT MOVES IN ONE FILE AND NOT IN THE FILE BESIDE IT HAS NOT BEEN FIXED, AND THAT FAILURE HAS ALREADY HAPPENED TWICE IN THIS REPOSITORY.** Then run every mechanical check one last time and report what it actually returned, file by file, and not a summary of what you expected it to return.

**9. CREATE EXACTLY ONE NEXT PHASE, AND IT IS `workspace/volume-08/PROMPT.md`,** for Volume 08, Chapters 344 to 392, days 557 to 605, **THE SEVENTH MOVEMENT OF THE SERIES IS TURNING AND THE LAYER IS RISING, AND THE POWER STAGE AFTER 6 IS 7. READ `outline/series.md` AND `outline/ending.md` FIRST AND TAKE THE FIGURES FROM THEM AND FROM `state/current.md` AND NOT FROM YOUR OWN HEAD.** **IT MAY NOT WRITE ANY CARD, ANY DAY, ANY FIGURE OR ANY SCENE OF VOLUME 08. IT IS A PHASE THAT SAYS WHAT THE NEXT FORTY-NINE CHAPTERS ARE FOR AND WHERE THE MANUSCRIPT IS WHEN THEY BEGIN, AND IT IS THE ONLY THING AFTER THIS ONE.** **AND A PROMPT MAY NOT FORBID THE CREATION OF THE PHASE THAT FOLLOWS IT. THE PREVIOUS BATCH PROMPT DID EXACTLY THAT AND IT IS WHY THE MANUSCRIPT WAS STOPPED WITH NINE CHAPTERS AND A VOLUME'S CLIMAX UNWRITTEN. IF YOU WRITE A FORBIDICTION LIKE THAT, YOU ARE REPEATING THE FAULT THAT HAS ALREADY COST THIS MANUSCRIPT ONE VOLUME'S END, AND A LATER PASS WILL FIND IT.**

## WHAT THIS PHASE MAY NOT DO

**May not write, alter, reword, improve, shorten or lengthen a single word of any of the forty-nine chapters of Volume 07. May not change a day, an ordinal, a weekday, a figure, a count, a name, a lock or a card. May not answer any of the thirty-five open threads, and may not reword one. May not close the corridor, recover the vault, walk the ring, settle who speaks for the eleven acres, supply the unit of the two numbers, reconcile the middle, name the pulse, read the seventh column again, decompose the four feet of shortfall, add a fifteenth mark to a wall, or write an entry for a well coming back. May not answer whose order it is, and may not say anything about whether the telling is still going on. May not say whether the fruiting bodies are safe to eat. May not say whether the bridge is still on. May not say whether a sealing order is a thing the people at both ends of a bridge may refuse, which is the volume's third question and it was asked twice out loud in the last batch and answered in neither. May not fill the register form and may not read a second line out of it. May not thank anybody. May not put the name into narration or speech. May not climb the successor-offer ladder. May not introduce a new final enemy. May not touch `scripts/`, `.github/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json`, or `state/phase-ledger.json`, and the ledger is six volumes out of date and that is a controller decision and not yours.**

**AND THE ONE PROHIBITION THAT IS SPECIFIC TO THIS VOLUME AND THAT A CLOSE CAN BREAK BY BEING THOROUGH: DO NOT LET THE CLOSE BECOME A VICTORY. A CLOSE that says the volume was a success, that the readers will remember it, that the argument held, that the book worked, is writing a review and not a close. WRITE DOWN WHAT IT DID NOT DO, WHICH WILL BE THE LONGER HALF OF WHAT YOU WRITE, AND NAME THE THINGS A READER WHO LOVES IT WILL STILL BE WRONG ABOUT IN FIVE CHAPTERS' TIME.**

## THE MECHANICAL CHECK, TO BE RUN AT THE END AND NOT BEFORE, FROM THE REPOSITORY ROOT

```
wc -w workspace/volume-07/batch-000*/chapter-*.md
python3 - <<'PY'
import glob,re,collections
paras=[]
for d in ['batch-0001','batch-0002','batch-0003','batch-0004','batch-0005']:
    for f in sorted(glob.glob('workspace/volume-07/%s/chapter-*.md'%d)):
        for p in re.split(r'\n\s*\n', open(f).read()):
            p=p.strip()
            if p: paras.append((f,p))
c=collections.Counter(p for _,p in paras)
dups={p:n for p,n in c.items() if n>1}
print("paragraphs:",len(paras),"| duplicated strings:",len(dups),"| surplus copies:",sum(n-1 for n in dups.values()))
PY
LC_ALL=C grep -rn '[^ -~]' workspace/volume-07/batch-000*/chapter-*.md
grep -rniE '\b(seat|brinewake|panel|fieldbook|kerb)\b' workspace/volume-07/batch-000*/chapter-*.md
grep -rniE '\bvolume\b|this batch|this chapter|this volume' workspace/volume-07/batch-000*/chapter-*.md
grep -rn 'Nobody said anything and the fen entered that nobody said anything\.' workspace/volume-07/batch-000*/chapter-*.md
```

**REPORT WHAT THEY RETURN, LINE BY LINE, INCLUDING THE LINES THAT ARE EXPECTED TO BE EMPTY AND THE FIGURES THAT ARE EXPECTED TO BE ZERO, AND NEVER REPORT A NUMBER YOU DID NOT MEASURE.**

## THE ONE-LINE VERSION

**Volume 07 is on disk at 140,165 words across forty-nine chapters and the manuscript is 1,024,413 across 343. Read the forty-nine chapters. Re-derive every figure from the files. Prove the thirty-five are still thirty-five. Record what the volume did and, at greater length, what it refused to do. Compact the three append-only state files or refuse to compact them with a reason that is not *it is risky*. Then create `workspace/volume-08/PROMPT.md` and do not put a prohibition in it.**
