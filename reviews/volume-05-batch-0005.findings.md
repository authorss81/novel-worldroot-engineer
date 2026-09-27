# Volume 05, Batch 0005 — the review of Chapters 237–245, and the repair pass that followed it

**This is the findings file for the review of `logs/batch-0005.review.log` and for the repair pass that was run on the strength of it. It is named `volume-05-batch-0005.findings.md` and not `batch-0005.findings.md` because that file is Volume 01, Chapters 41–49, and a close reading the `reviews/` directory should not be able to confuse the two. `reviews/volume-05.findings.md` is the Volume 05 close's own file and is not written here.**

**The batch is nine chapters, 237–245, days 431–450, and Chapter 245 is the last chapter of Volume 05. It is structurally complete and it was not restarted. The repair pass opened all nine files for writing, which no earlier fix pass in this volume did, and it took no plot beat, moved no day, altered no figure's meaning, touched no outline, and created, deleted or moved no marker.**

## The findings as they came in, and what happened to each

| # | Finding | Disposition |
|---|---|---|
| 1 | The refrain *Nobody said anything and the fen entered that nobody said anything.* had become paragraph furniture: a verbatim identical standalone paragraph 26 times across nine chapters, 16 of them in Ch 242, and Ch 245 ended on it | **REPAIRED IN PROSE IN SEVEN CHAPTERS.** 21 of the 26 rewritten as prose that says what the silence was made of; 5 kept where the silence is the event. Ch 245's last line replaced |
| 2 | Every word-count figure was stale and had propagated into the next-phase prompt | **REPAIRED IN FIVE FILES.** All figures re-derived with `wc -w` after the last prose edit |
| 3 | `state/current.md` carried a false live claim that `workspace/volume-05/batch-0003/` held no marker | **REPAIRED, and the claim was false** |
| 4 | Ch 242 narrated the twenty-fourth as past during a scene set on the twenty-third | **REPAIRED** |
| 5 | Ch 242 used the disabled hand in the action | **REFUSED AS A MISREAD, with the evidence** |
| 6 | Ch 242, one subject–verb disagreement | **REPAIRED, minimally** |
| 7 | Do not merge `origin/novel-wip/batch-0005` wholesale | **NOT MERGED. One line taken in minimal form, one refused** |
| 8 | The review phase is not reviewing; the reviewer agent is `mode: subagent` | **FLAGGED, NOT TOUCHED — controller-owned** |
| 9 | `state/phase-ledger.json` still reads `phase-000-bootstrap` / `planned` | **FLAGGED, NOT TOUCHED — controller-owned** |
| 10 | The state files are 2.8 MB and are loaded whole every phase | **FLAGGED, NOT TOUCHED — controller-owned** |

## 1. The refrain, and why the disposition is repair and not disclosure

The manuscript's method is that a body keeps a book and enters what happened, including what nobody said. That sentence *is* the method and it is not the fault. What had happened to it is that it had been used as a paragraph break with nothing after it, twenty-six times as a bare paragraph in nine chapters, sixteen of those in one chapter, and the escalation across the volume was four, eight, nine, thirty-nine, twenty-six — a steep climb that a reviewer measured and a reader feels without measuring.

A ledger line that records a silence is the book. A ledger line that says *the fen entered that nobody said anything* and stops is furniture.

**The 21 rewrites say what the silence was made of.** The man of about fifty holding a satchel with a crate in it for four minutes and not putting it down. About six of six looking at the oilcloth and not at the bead. The man of about fifty bringing a coat out to a north branch at about the fifth hour of the evening, and the reader of this body not putting it on and not saying why, and the coat going back. The rain coming down the ditch first and taking about an hour to reach the branch, and about four people watching it do it. The two men saying the number out loud at the same time, neither asking the other whether he had got it, and comparing the figures a minute later without either of them asking. The light going off the west cut and the book shutting and two men going up a shoulder in the dark. About nineteen people reading four lines and not one of them asking who had written them. About four of the nineteen looking at the woman who had just finished, and the count of that being a number about the lookers and not about the person.

**The 5 that stand alone are the 5 places where the silence is the event:** Ch 237 after the word ENOUGH, Ch 241 before the fieldbook's three lines, Ch 242 after the mark came, Ch 244 after the covenant's six lines, Ch 245 after the first eleven seconds. Five is where Batch 0001 and Batch 0002 stood. The escalation is broken and the ritual is intact.

**Chapter 245 no longer ends on the formula.** Its last line is now a man of about sixty-eight taking a lamp off a stone in his left hand, because the inside of the right one has three inches on it that do not branch, carrying it to the cart shed himself, and the reader of this body walking about nine feet behind him saying nothing the whole way, and the fen entering the lamp and the nine feet and the nothing and nothing else. It keeps the method and the injury and it ends the volume on a man carrying his own light.

**Re-measured after the pass: the sentence occurs 75 times, of which 5 are alone in their own paragraph and 70 open a longer sentence. It is still the only paragraph of nine words or more in the batch that appears more than once, and that is now measured by script over all nine files rather than asserted.**

## 1b. Three more mechanical repetitions, all the same construction

`About four of the N said nothing in a way that was different from the other M` stood four times. **Ch 241's was a verbatim nineteen-word duplicate of Ch 237's**, which the earlier pass had missed because it measured paragraphs and not clauses. It now stands twice. `A man who counts the hands on a board is a man reading a room` duplicated Ch 237's `a man who counts the faces in a yard is a man reading a room`, and the second is now `a man counting a room instead of working in it`.

**No clause of nine words or more now appears verbatim in two chapters except the manuscript's own date, hour and character formulas, which are its notation and not prose.**

To pay for the rewrites, restatement was cut and only restatement — one whole paragraph in Ch 242 that restated the sentence before it, and seven clauses. No beat, no figure, no day.

## 2. The stale figures, and the seventh time this has happened

`b1a6614` edited eight chapter files after the counts were taken. Every figure was stale and had spread to `current.md`, `continuity.md`, `open-threads.md`, `chapter-summaries.md` and the Volume 05 close prompt, which the close will open on.

**Re-derived after the last prose edit, with `wc -w` including chapter headings:**

| | was | is |
|---|---|---|
| Ch 237 | 3,076 | **3,113** |
| Ch 238 | 3,121 | **3,098** |
| Ch 239 | 3,099 | **3,105** |
| Ch 240 | 2,954 | **3,070** |
| Ch 241 | 3,005 | **3,082** |
| Ch 242 | 3,111 | **3,099** |
| Ch 243 | 3,063 | **3,112** |
| Ch 244 | 3,080 | **3,099** |
| Ch 245 | 2,921 | **3,093** |
| Batch | 27,430 | **27,871** |
| Volume 05 | 144,381 | **144,822** |
| Manuscript | 736,900 | **737,341** |
| Mean | 3,046.0 | **3,096.8** |
| Range | 2,921–3,121 | **3,070–3,113** |

`166,022 + 141,818 + 142,952 + 141,727 + 144,822 = 737,341` exactly. All nine chapters are inside the 2,600–3,120 band, the band was not widened, and no chapter is declared outside it. **The two false claims that came with the stale figures are withdrawn: that Ch 238 sat one word outside the band, which it never did, and that Ch 242 was the longest-reading chapter in the batch at 3,111, which is now Ch 237 at 3,113.**

The recorded figures for the end of Batch 0004 — 709,470 for the manuscript, 116,951 for Volume 05 — are correct for that point in the volume and stand.

## 3. The false marker claim, which was false

`state/current.md` asserted, in the paragraph headed *WHAT IS LIVE INSTEAD, AND MEASURED*, that `workspace/volume-05/batch-0003/` carries no marker at all and that the runner may therefore select it again. **It carries `.done`, added in `9fe0b74 novel: complete batch-0003`.** The claim had been carried forward unchanged through four passes. It is corrected in place, and the measured position is now written down instead: batches 0001 through 0004 all carry `.done`, `batch-0005/` carries no marker and is in flight, `volume-close/` carries no marker. **No marker was created, deleted or moved by this pass.**

## 4, 5 and 6. Three findings in one chapter, and one of them is a misread

**The timeline error is real and is repaired.** Ch 242's closing speech is given at about the third hour of the afternoon of the twenty-third and said that the man of the north row with the cough had asked on **the twenty-fourth** to be struck off the count of the two. Ch 243 is the twenty-fourth and is where that happens. The same sentence gave the count as holding **on the day after tomorrow**, which is the twenty-fifth and is a figure nowhere in the volume. The speech now says the count is two, was two when he stood on the stone yesterday and is two tonight, that one of the two has three inches on the inside of his right forearm that do not branch, that a mark is not a figure, and that he is not going to say what the count will be in a month. **The lock is held by a refusal on the page two chapters later and is no longer forecast in the wrong chapter.**

**The subject–verb fault is real and is repaired in place.** `Neither of the two men who has a figure of that middle has asked` is now `who have`. The WIP branch replaced the whole sentence instead and lost the specific that the man of about fifty had it put to him on the sixteenth and answered that he did not know. **The specific was not taken and the branch was not merged.**

**The disabled hand is not a fault and nothing was changed.** The mark is four inches along the inside of the **left** forearm and branches twice — Chs 197, 204, 216, 233 and 241 say so. The man of the north row with the cough takes three inches on the inside of his **right** forearm. The hand that lost its use is therefore the left. Ch 242 reads: *he put his **right** hand on the stone, because the north is the one that has the most on it, and his **left** hand was in his coat and was not used all day.* **The action honours the disability and says in its own words that it does**, and the old man's own page says of him that he *had no use of one hand from the wrist down* and *did not tell me that before I asked him*.

**A fourth fault in the same chapter, not raised by the review, is also repaired, and it is the same fault of the same kind.** Ch 242 gave *if it is four inches a day then in nine days it is going to be a foot* to the woman of about thirty-eight of Marden. **Ch 239 has that sentence in the mouth of the man of the north row with the cough, on the second morning, to the reader of this body alone.** The attribution is now to him, on the Sunday evening, which is where Ch 239 puts it. The two *numbers* on the bank remain hers, which is what both chapters say they are.

## 7. The WIP branch

`origin/novel-wip/batch-0005` touches two files and six lines. One Ch 242 grammar fix is taken in minimal form. Four Ch 242 cosmetic rewrites drop a specific and are not taken. One Ch 240 change is `board` → `table`, and `board` is the established term in this batch with six uses in Ch 240 and five in Ch 241 while `table` appears nowhere in it; that change breaks continuity and is refused. **The branch was not merged, not deleted and not checked out.**

## 8, 9 and 10. Controller-owned, flagged, not touched

1. **The review phase is not reviewing.** The log opens with the reviewer agent falling back to the default agent; the default agent is the writer; the log then contains the reviewing session's own commands verbatim. `.opencode/agent/novel-reviewer.md` is declared `mode: subagent` and cannot be dispatched as a primary phase agent. **Every review in this repository has been the writer auditing itself, and the writer wrote finding 1.** Not touched: `.opencode/agent/` is controller-owned.
2. **`state/phase-ledger.json` still reads `phase-000-bootstrap` / `planned`** after 245 chapters and five volumes, with `attempts: 0` and no `actualModel`. Not touched: the ledger is controller-owned.
3. **The state files are 2.8 MB** — `continuity.md` 1.48 MB, `chapter-summaries.md` 838 KB, `open-threads.md` 477 KB, `current.md` 69 KB — against AGENTS.md's instruction not to load the manuscript into every prompt. Not restructured in this pass: re-architecting the state files mid-volume is a controller decision and not a repair of this batch.

## The minor items, one of which is not a defect

- **`reviews/` had no Volume 05 batch findings file and `reviews/batch-0005.findings.md` is Volume 01.** This file closes that gap. The close's own `reviews/volume-05.findings.md` is not written here.
- **`workspace/volume-05/batch-0005/PROMPT.md` was checked for the reported nine/ten ambiguity and there is none.** Its *ten chapters* is in the sentence about **Batch 0004**, which has ten; its *nine chapters* is in the sentence about **this** batch, which has nine. Both are correct. The prompt is a record of the instruction as issued and was not edited.
- **The clearance that no other sentence of nine words or more appears twice was false, and false at two levels.** False at the paragraph level, as the earlier pass found and broke two of; and false at the clause level, where a nineteen-word sentence stood whole in two chapters and no paragraph-level script could see it. Both are fixed and the clearance is re-measured at both levels.

## What was re-measured and re-issued, because the counts were wrong in kind and not only in degree

- **The disclosed refrain.** The record said ninety-five occurrences and ninety-five paragraphs standing alone. Measured: 75 occurrences, **5** standing alone. The second figure was wrong in kind — the sentence was almost never alone, and the pass that reported it as alone ninety-five times had counted an occurrence and called it a paragraph.
- ***March*.** The record said *the March's tin* three times in this batch. **Once**, in Ch 245; the three had been taken from a paragraph about the whole volume.
- ***Thornwild*.** The record said four. **Three** — twice in Ch 244 and once in Ch 245; the four counted a `>` line and its continuation as two.
- **Confirmed unchanged by the pass:** *seat* five times, all on line 19 of Ch 244, in the covenant's refusal clause; *nest* absent, with three substring hits inside *honest*, *honest* and *dishonest*; *uneven* twice, in Chs 244 and 245; *pulse* once, in Ch 245; *five volumes* four times as a duration frame; `Entered ...` block counts 1, 1, 1, 0, 1, 0, 1, 1, 1, unchanged and no chapter at two; zero consecutive blank lines, zero trailing whitespace, zero non-ASCII glyphs, zero unbalanced quotation marks, zero unbalanced bold markers, every file ending in a newline.
- **Every weekday site in all nine files re-listed and checked against Table E. None is wrong.** Table E re-derives from day 361 being a Wednesday on the page in Ch 197 and 431 being 361 plus seventy; its twenty rows are internally consistent.

## What this pass did not do

It did not answer, close, advance or reword any of the thirteen open threads. It did not move any count on a page. It did not touch `outline/volume-05.md`. It did not write a Volume 06 outline or create `workspace/volume-06/`. It did not answer the pulse, and the pulse still has no name but its own shape, two figures, no third reading, and a direction no ground in the volume is. It did not create, delete or move a marker. It did not touch `state/phase-ledger.json`, `.opencode/agent/`, `scripts/`, `.github/workflows/`, or any controller-owned file.
