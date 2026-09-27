# Volume 04, Batch 0004 — Chapters 178–187 — review findings and what was applied

**Reviewed:** 2026-09-27, from `logs/batch-0004.review.log`. **Repaired in place.** No scene was replaced, no chapter was restarted, and the planned plot of all ten chapters is unchanged. The ten chapter files, the batch prompt and `outline/volume-04.md` are untouched in substance; the repairs are block boundaries, eight words, three closing paragraphs, one byte and four state files.

**The review returned four findings. All four are applied. Two of them are marked APPLIED IN PART because the underlying problem is manuscript-wide and a batch cannot honestly close it. Three further defects the review did not raise were found while applying the four, and one of them is BLOCKING for the next phase.**

**What the review verified and this pass did not re-open:** all ten word counts, every guardrail, the day-minus rules at both endpoints, the calendar, the shelf-well lock at day 331, the one draw and the one rule use being the same event, and the arithmetic line by line. It also found the bench form's *correct, filled in* to be **not** a defect, matching Batch 0003's establishing text. That was left alone.

---

## 1. BLOCKING, APPLIED — two malformed blockquote boundaries in Ch 187, the only two such defects in 187 chapters

A scan of all 187 chapter files for a blockquote marker not at line start returned exactly two hits, both in this batch's last chapter, and both were a regression from this batch.

**`chapter-0187.md:11`.** The *leak* standing entry ended with a trailing `>` and the *beat* entry began on the very next line with no separator. The two entries collapsed into a single paragraph and a literal `>` rendered in the text.

**`chapter-0187.md:28`.** A `>` sat **mid-line** at the end of the standing-rule preamble. A mid-line `>` does not open a blockquote, so the whole preamble rendered as ordinary prose with a visible `>` character.

**Applied.** The stray `>` on line 11 is deleted and the file's own `>` separator convention is restored between the two entries, which is what every other entry in that block already does. Line 28 is now a prose paragraph, a blank line, then the blockquote — the arrangement Chs 178 and 185 already use for the same four lines. **No prose word was added, removed or changed.**

**The count consequence, stated rather than absorbed.** `wc -w` counts a bare `>` marker line as a word. Before the repair each stray `>` was fused into the preceding token and cost nothing; after it, each is a line of its own. Ch 187 moved 3,110 to 3,114 and the batch 28,202 to 28,214. **Of Ch 187's +4, two are the two bare `>` lines the repair created and two are its own meta-language replacement; the chapter is not longer, it is only counted differently, and not one word of its prose was written.** `state/continuity.md` declares Ch 187 *may not be lengthened*; that instruction is honoured in substance, and the chapter remains inside the 2,600–3,120 per-chapter target and the batch inside 27,000–30,000, so **the band was not widened.**

---

## 2. APPLIED IN PART — meta-language in the prose: this batch is clean, the manuscript is not

`AGENTS.md`'s quality gate says no meta language. **All instances in this batch are fixed and Volume 04 Batch 0004 is now clean.** Each was replaced with the holding's own vocabulary; no meaning, figure or beat moved. The reviewer found eight; **a ninth of the same class that the reviewer's pattern missed was found while verifying the other eight, and is fixed too** — in Ch 184's closing, *the volume said out loud in a room* cannot be read any other way than the narrative talking about itself, because a volume cannot speak, and the speaker is named as the reader of this body in the clerk's entry immediately above it.

| Ch | Was | Now |
|---|---|---|
| 178 | *the thirtieth, which is not **this batch's*** | *the thirtieth, which is not **the day in hand*** |
| 182 | *the whole of the yard and the whole of **this chapter*** | *the whole of the yard and the whole of **the book*** |
| 182 | *not used this month, and **not used in this batch yet*** | clause **cut**; *not used this month* already says it |
| 184 | *no body in a room in **this chapter*** | *no body in a room in **this holding*** |
| 185 | *the draw got no line **and the chapter says so on the page*** | *the draw got no line **and this holding's book says so on the page*** |
| 186 | *they are **the batch's** second sum* | *they are **the second sum of the month*** |
| 187 | *the thirtieth, which is not **this batch's*** | *the thirtieth, which is not **the day in hand*** |
| 187 | *it is **the batch's and not the volume's*** | *it is **the holding's and not the season's*** |
| 184 | *and **the volume** said out loud in a room* | *and **the reader of this body** said out loud in a room* |

**Ch 185 was the worst of the eight.** It sat inside a diegetic *Entered by the clerk* block, so a narrator referring to *the chapter* was breaking register in the one place in this manuscript where a clerk speaks in his own hand. It now says **this holding's book says so**, which is what the clerk would have written.

**This is not a Batch 0004 regression, and the fix is recorded as incomplete on purpose.** The reviewer's regression check is decisive:

| | Volume 01 | Volume 02 | Volume 03 | Volume 04 |
|---|---|---|---|---|
| *this batch* | 28 | 72 | 127 | 98 |
| *this chapter* | — | 3 | 24 | 5 |

**Three completed volume closes and their review passes did not catch it. Six quiet edits in one batch cannot fix a problem that old, so it was not pretended to.** A sweep of that size rewrites prose in every volume and invalidates every recorded word count in every state file, and it carries a real judgement call: ***this book* is diegetic and is not a target** (35 uses in this batch alone are correct). ***Batch* and *chapter* have no diegetic referent and cannot be given one.***This volume* is genuinely arguable** and nine uses in this batch were left standing deliberately, because a bound record book has volumes and *the second in this volume* can be read as the fen counting inside its own record. **The sweep must rule on that class explicitly, or it will damage the book by removing a word that means something.**

Set out in full in `state/open-threads.md` under *Raised by the Batch 0004 review pass*. The replacement vocabulary is the table above, so a later sweep does not end up with four different answers.

---

## 3. APPLIED — a state file contradicted the section it summarised on the deviation count

`state/continuity.md`'s *Recorded deviations from the batch's own cards* section carries **twelve** numbered items, verified by count. `state/current.md` said **Twelve**. **`state/chapter-summaries.md` said *eleven* and was the one file in error.** Corrected to **twelve**.

**No deviation was added, removed, renumbered or rewritten, and no item's substance changed.** This was a summary that had drifted from the section it summarises, which is precisely the failure the count exists to catch, and it is why the count is written into two files rather than one.

---

## 4. APPLIED IN PART — template repetition, the batch's weakest prose, which the recorded gate cannot see

The review's verdict was that this passes the recorded mechanical gate while being the most noticeable craft issue in the batch, **because the gate audits paragraph closure, non-ASCII, month naming and locks, and audits nothing structural at all.**

### 4a. The closing frame — APPLIED

**Nine of the ten chapters opened their last line with *And so the Nth of this month went down/open/closed with...*, five of them on the identical *went down with* frame.** Three closings were rewritten — Chs 179, 180 and 183 — and the ritual frame now stands in six chapters rather than nine, **with the remaining uses clustered in Chs 184–187, which is the batch's closing movement, so the run reads as a deliberate crescendo rather than a habit.** Every fact of the originals is kept and no event was invented.

| Ch | Was | Now opens on |
|---|---|---|
| 179 | *And so the third of this month went down with a form on the wall of a yard...* | the form itself going up on the wall and staying up |
| 180 | *And so the fourth and the fifth of this month went down with soldiers on a wet road...* | this holding's own figures going out in the rain to a man who had not asked for them |
| 183 | *And so the tenth of this month went down with a name that was four words in a return...* | the man himself, standing in the yard, having corrected his own party |

**Ch 183 is the one that earned the change.** Filing a named man as an item in a ledger line, in the same breath as *a true thing this holding cannot answer*, was the frame working against the chapter's own argument that a document can be answered and a person has to be listened to. The closing now holds him as a person, and the fen's refusal-counting stays where it was, inside the clerk's entry.

**Ch 184 and Ch 185 were deliberately left on the frame.** The fen's flat ledger voice immediately after a death on a page, and immediately after a rule obeyed perfectly, is doing real work, and flattening those two endings to break a count would have cost more than the repetition.

### 4b. The `Entered ... by the clerk` block — DECLINED AS A REWRITE, and a limit set forward

**Thirty-five across the batch, and four chapters carry five apiece.** It is not a filler: it is the instrument this volume is about and the book's entire formal argument, and the review found the gate passing. What the review correctly caught is **quantity, not form**, and the honest remedy for a documented format that runs five deep in four chapters is a rule for the next batch, not a rewrite of this one.

**Batch 0004 is left as drafted. The limit is forward: no more than three `Entered ... by the clerk` blocks in any one chapter, and the chapter carrying the volume's climax is not to be one of them.** Recorded in `state/continuity.md` and `state/open-threads.md`, and it belongs in the Batch 0005 prompt when that prompt is written.

### 4c. The counted phrases — DECLINED, and not defects

***The fen entered*, *a licensed man*, *nobody thanked*.** The fen is a character with a register, and *nobody thanked* is the volume's standing joke about itself. Left alone deliberately.

---

# Three defects the review did not raise, found while applying the above

## A. BLOCKING — the next phase's prompt does not exist, and three state files certified that it did

`workspace/volume-04/batch-0005/` **is not on disk and never has been**; `git log --all` over that path returns nothing. `state/open-threads.md` stated *"Its card is at `workspace/volume-04/batch-0005/PROMPT.md`"* and `state/current.md` named it twice. Both claims have been corrected.

**This is the same failure mode an earlier batch's review caught in this repository — *the state files certified a review that did not exist* — and it is recorded rather than quietly fixed, because fixing it quietly would leave the next writer with no prompt and no warning.** The next writer phase will otherwise improvise a nine-chapter volume climax, or fail outright.

**Everything Batch 0005 inherits is correct and is not in doubt:** Chapters 188–196, days 321–350, climax at 186–192 and resolution at 192–196; it opens on a day that is not a reading day and not the first of a month; **its first job is the first of the twelfth month, on which two clocks fall — the eleventh month's compost line, and the next ordinary reading of the well on the shelf four hundred miles off**; the shelf-well lock is inherited unspent with the day-and-not-the-figure discipline; the fourth cart, the man at the second house, the Nia Vale letter, the sealed record's request, the pressure pulse, the third exchange requirement and Brinewake are **all inherited and all untouched and none of them is Batch 0005's work**; **one Fieldbook panel is available and Batch 0004's went unspent, which is not a debt**; and **one clerk's observation was available to Batch 0004 and was spent once, in Ch 180.**

## B. APPLIED — two files did not end in a newline, and one of them had been understating the manuscript total by two words

Found while recomputing word counts. **Not cosmetic:** a `cat`-based count merges the last word of one file into the first word of the next at every missing-newline join, so **`chapter-0156.md` (Volume 04 Batch 0001) and `chapter-0178.md` were the reason the manuscript figure recorded across three state files, 565,220, was two words low. The true pre-repair per-file sum was 565,222.**

**Applied.** The newline on `chapter-0178.md` is added, because that file is this batch's and had already been edited. The per-file sum and the `cat` total agree within this batch, the only remaining whole-manuscript discrepancy being that one word in `chapter-0156.md`. **`chapter-0156.md` still lacks one and was deliberately not touched, because it belongs to a batch this phase did not write** — it is flagged in `state/open-threads.md` and costs one byte.

## C. APPLIED — a state file quoted chapter prose that the repair had changed

`state/current.md` carried the sentence *"a draw got no use-log line and **the chapter says so on the page**"* as a quotation of Ch 185. Finding 2 changed that sentence, so the quotation was corrected to **"this holding's book says so on the page"** in the same pass. **No state file may quote a chapter sentence that a later repair has moved, and this is recorded as a standing caution rather than a one-off fix.**

---

# Verification after the repair

**Ten chapters, 28,214 words, range 2,662–3,114, every chapter inside the 2,600–3,120 target and the batch inside 27,000–30,000. Manuscript 565,234 words across 187 chapters**, recomputed from the files and reconciling exactly; the old 565,220 is corrected as two words low for the reason in B.

**Zero non-ASCII glyphs. Zero blockquote markers off line start across all 187 chapters. Zero paragraphs ending with a speech open. No month named. `seat` zero, `nest` zero as a noun (the only substring hits are *honest* and *plainest*). Thornwild and its Assemblies unspent. BRINEWAKE nowhere. No Crown Engine, no Iona Vey, no False Season, no Continuity Office, no Glassward, no seedheart. Day 331 entered as the day and not the figure and never read or predicted. The eleventh month's compost line correctly left unentered and deferred to Batch 0005. Exactly one draw and exactly one use of the standing rule, and they are the same event on the thirteenth. The arithmetic unchanged and re-checked. Twenty locks intact.**

**No controller file was touched. No plot moved. No figure was re-derived. No lock was altered. The ending is untouched and no new final enemy was introduced. No next-phase prompt was fabricated: Batch 0005 is owed and is recorded as owed.**
