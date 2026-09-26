# Volume 02, Batch 0001 — review and repair record

**Phase under repair.** `HEAD` = `1e82a0c novel: save writer work next` — **Volume 02, Batch 0001, Chapters 50–59** (Movement 1, *What The Charter Is Worth*), plus `outline/volume-02.md`, `outline/batches/volume-02-batch-0001.md`, and the next-phase prompt `workspace/volume-02/batch-0002/PROMPT.md`.

**The report.** The pipeline review is `logs/next.review.log` (the `novel-reviewer` subagent did not load and the primary agent ran the review itself). Every finding in it is verified with `file:line` below or in the log itself, and every one has been answered. **The batch was not restarted, no chapter was replaced, no scene was cut for length, and no planned plot was changed.** Volume 01 was not touched.

**Result: 31,337 words, up from 29,747. Every chapter is now inside the 2,600–3,200 band except the three that were already over it, and the batch total is over the outline's 27,000–30,000 band by 1,337. Both facts are recorded in `state/current.md` rather than hidden.**

---

## 1. The Chapter 53 register page contradicted itself — FIXED, and it is better

The hinge of the volume described one document three incompatible ways. The decision taken, and the reason for it:

**The works schedule extract keeps Volume 01's schema exactly.** `chapter-0016.md:39` says *Six columns. No headings*, and `:97` says *The first is the item. The second is when the work was ordered. The third, fourth and sixth are executions. The fifth is not a date at all… The fifth is a hold.* `chapter-0008.md:81,:167` agrees. So the extract is **six columns with not one head printed over any of them**, and the *Crown-held* column is **the sixth word of the caption printed in the line of type at the top of the sheet** — which `chapter-0016.md:39` already establishes as *"a line of type at the top with a form number in it and a place for a date"*, set in the same type as the entries. Nobody missed a heading. They missed a **caption**, because a body reading a table for six weeks reads the items and not the top of a sheet.

That single decision repaired five findings at once:

| Old | New |
|---|---|
| `ch53:45` Marek: *"two of them say executed… I cannot find the sixth"* | He names five columns and the sixth is *"the one we have all been calling a third execution since the spring"* — and Dunmar finds the caption. **Three execution columns, per Ch 16.** |
| `ch53:49` Dunmar: a head *"in the same size as the other five and in the same line"* above the third execution column | A caption at the top of the sheet listing the columns in order, **whose sixth word is *Crown-held*** |
| `ch53:59` register page *"six columns, and only the first two columns headed"* | **eight columns, a head over the first six, nothing whatever over the seventh and the eighth — no rule, no word, not a hairline** |
| `ch53:113` *"six columns: item, order date, three execution columns, a hold, an authorising hand, and a description hand"* — eight items in six columns | **Eight columns, and the seventh and the eighth are the two this building had to name itself** |
| `ch53:81` the entry asserting both that the sixth and seventh *are* headed and that *there is no column head printed over the sixth and the seventh* | The entry now says the seventh and the eighth have no head over either, that this building named them *authorised by* and *work description*, **and that those two names are ours and not the district's** |

**Consequential renumbering, done everywhere:** the authorising column is the **seventh** in `ch54:13`, `ch59:29,:35`, `state/continuity.md`, `state/current.md`, `state/open-threads.md`, and both batch briefs. A state row now says outright that a later chapter calling it the sixth is wrong.

**The count rows, corrected to one arithmetic.** `ch53:53` keeps the census that was already right — **Y 41, N 31, dash 18** — and everything downstream now agrees with it: **eleven of the eighteen dashes sit on rows that carry a hold** (`ch53:131`, replacing a *C row* that was a third value in a three-value column); **thirty-one rows carry a hold, eleven of them also a dash in the sixth, nine of the eleven a date under the hold, two without and both of the two printed *suspended***, in the other twenty a date under the hold and a hand under the date (`ch53:141`, replacing a count that had *four rows* and *the other twenty* in the same chapter). `state/continuity.md` had the dash right all along; the prose now matches it.

**The colony's timeline, closed.** *Suspended since the fourth year* now means **the table's fourth year, eight years ago** — the table is eleven years old — and the colony's history was rewritten to one line that adds up: cut out eleven years ago, the bigger holding failed in the fourth year, the district put what was left into the Crown's hand, the colony has been the Crown's for eight years, the row has not been touched since. The seven-months-back reading is gone.

**The lecture was broken up.** `ch53:117–123` is now four short paragraphs instead of one unbroken block of comparative administrative law, and one statutory example was cut. The argument is untouched.

**Length cost:** +125 words net after trimming about 120 of tightening elsewhere in the chapter.

## 2. A document used four days before it existed — FIXED

`ch52:79` had the broker reading *"the three names in a strange hand on a Crown map that had been on the table for two days"* and *"the entry about the man of about seventy."* The map reached the yard on the evening of the twenty-fourth and went straight into Tova Reed's locked case; the three names are not written until `ch59`; the man of about seventy initials nothing until `ch58:79`.

Lissa Vale's list is now the books that were actually in the building on the twenty-fifth: **the standing pressure log, the use log, the return line, the seven section-nine notes, the entry about the well, and the rider that went to Fennmere on the twenty-third**, plus a paper dated the twenty-fourth in the broker's folder he does not explain.

Related and also fixed: `ch53:41` had the low quarter's chalk survey flat on the table on the twenty-sixth. It is now **the district's *entry* about the survey**, made on the nineteenth and twentieth, with the sheet itself still nine miles off in a house in the low quarter — and `ch56:11` now says the sheet was asked for on the twenty-seventh and came up on the Sunday post, which is what the chapter's opening requires.

## 3. The section-nine note chain — FIXED, and the arithmetic of the entries with it

Volume 01 `ch49:71` closes with **six** notes and *the sixth of the six* is the only one not about a cut. The chain now closes on the page: **6 → 7 (Ch 50, the twenty-third) → 7 (Ch 56, the twenty-ninth) → 8 (Ch 58, the first).**

- `ch50:87` *the seventh of the six notes* → **the seventh note under section nine**.
- `ch50:91` *why the other six are about a cut* → **why five of the other six are about a cut**, and the reason is now on the page in the fiction instead of in a note to the writer: *a cut is a thing that can be refused, and a measurement is a thing that can only be answered with money.*
- `ch56:67` → **seven notes, five of the seven about a cut, and every one of the seven closes with the same seven words.** The phrase *this is worth nothing against a cut* is seven words; the chapter said nine.
- `ch56:79` *six times* → **seven times**. `ch58:123` *the nine words* → **the seven words**.
- The **Crown legend is six words**, not four (`ch56:23,:53,:69`, and Dunmar's *the nine words off the legend* at `:43` → **six words**). Tova Reed's *no line here* is **three**, not four (`ch55:99,:109`).
- `ch50:27,:95` back-dated the note to the twenty-second on the twenty-third. The note is now **the twenty-third, seventh to tenth hour**, and the sentence that opens it is the *second* sentence of that entry.

## 4. The month-name lock — FIXED, and the breach is now the climax's argument

`PROMPT.md:33` forbids a month name on any document. `ch59:43` named **November** and `ch59:51,:53,:55,:59` named **September**, which also destroyed `ch53:73` — *The register does not name months* — and the calendar did not close.

The fix is not a deletion. **Nobody in Chapter 59 names a month, because the district's form does not carry one.** The order date is spoken as **one and nine**; the day on the order paper is **a day in the eleventh month**; Dunmar Fitch admits he has been calling the date *the first of a month* for four days because there is nothing else to call it; and Bream tells him he will have to learn to count. The scene got stronger, not weaker, and the state's dating rule is now a rule about the world rather than about the draftsman's convenience.

**The year is closed at the same time.** The shaft is in the spring; the order date is seven months before it; so **the order date falls in the year before the year of the shaft** — `ch53:63,:89`, `ch59`, `state/continuity.md` and `state/current.md` all now read *the year before he went in*, and Marek's beat is no longer *right on the day and wrong on the year* but **right on both**, with the monthlessness turned into the reassurance: *whatever month it was, it was in a year when he was walking about and could be asked about it.*

## 5. The Thornwild guardrail — FIXED, and the state file's denial of the breach with it

`ch52:33` had the broker name **a long line two hundred yards under a windbreak belonging to ninety people with no charter** and say it was in the annex. Guardrail 4 forbids using or sizing the long line; sizing a settlement to ninety people identifies it; and the annex's four contents (`ch39:49`) do not include it. `state/continuity.md` then asserted the opposite.

The broker now reads the annex's actual fourth term, which is worse for this holding than the long line was: **the return main is half of specification by the length and a quarter by the bore, and the annex's own fourth term says in terms that the seed described on it may not come up, and that term is a line in a public ledger in Cray.** The state lock now names the breach that was fixed rather than the one that was not.

## 6. Arithmetic, all of it

| Finding | Correction |
|---|---|
| `ch54:31,:35` three-sixteenths in nine days, and *nine days back* | **one sixteenth in thirteen days** in both the prose and the entry; `ch51:117` *eleven days* → **twelve** |
| `ch54:85` *eight days of slack* | **ten days of slack on paper and nine of them in practice** — fourteen less four is ten, and a Thursday cart is at the counter on the fifth |
| `ch58:97` *a charter that ends in twelve days* | **fifty-eight days**, against `ch58:57`'s fifty-nine to the thirtieth and the twenty-ninth for the charter |
| `ch50:69` *a deficit of a little under two thirds* | **a little over half by the length and, by the bore, a quarter**, and Marek has only ever written the first down; `ch52:33` and `ch57:141` brought into line |
| `ch52:49` *forty pounds a year is eight times what this holding raises in a good month* | **three times a season's whole levy**, and every quarter of it is more than one of them |
| `ch58:99` *a man who can be had for four miles* | **nine miles**, per `ch51:41` |
| `ch54:31` *a hundredweight was put into that return main* | **twenty-one hundredweight and a quarter**, per `ch58:111` |
| `ch50:31` *Twenty-one days later a hearing officer adopted it* | **Seventeen days later, on the twenty-first** — the vote was on the fourth |
| `ch52:25` *you have had a week* | **three days** |
| `ch52:53` *nine hours on the eighteenth* | **from midnight on the eighteenth until about two in the afternoon on the twenty-first, which is sixty-two hours** — a better line than the one it replaces |
| `ch53:107` *a charter for two days* | **five days** |
| `ch58:81` *examiner since the twenty-first of this month* — a future date | **the twenty-first of last month, which is the day the charter was made, and named second on the certificate of the twentieth, ten days before anybody expected one** |
| `ch58:121` *I have been right about both of those for seven months* | **two months**; the October ditch is now dated *on a Sunday two months back*, which removes the batch's only other month name |
| `ch58:113` *on the first, on the fourteenth and on the twentieth* | **on the fourteenth and on the twentieth of last month**, since the first is that morning |
| `ch59:99` *the clean record on the second of a month* | **the eighth of last month** |

**The clean record is on the eighth and the certification is on the seventh, and both are right.** Volume 01 `ch37:97` certifies the standing pressure log on the seventh; `ch38` is the hearing at two o'clock on the eighth, and that is the morning the fieldbook became a district file. `ch50` says both, correctly. The review read the two as one. **A state row now states the distinction outright, because a reader will trip on it again otherwise.**

## 7. Guardrails and small canon slips — all fixed

- `ch51:97` *condition five of the annex* → **the annex's fourth term**. The annex has four things, and two numbering systems had merged.
- `ch57:7` the Tarrow Assembly roll *has two names on it* — they are Sera Quill and Idris Vane (`ch30:37`) — and *eleven miles up a cart track* silently stole Idris's identifying detail. Now **three names, Renner is the newest, and the other detail belongs to the sixty-one-year-old who lives eleven miles up a cart track**.
- `ch57:7` *three hundred and eleven words* of the thirtieth's statement → **eleven hundred** (`ch30:113`, `ch42:43`).
- `ch59:87,:97` Osvalde Bream styled *seed steward, of the Ashcombe* — the Ashcombe is Vesta Lund's index, four hundred miles off, and Bream is out of a bookshop. Now **of no district and not licensed**, which is also the point: the entry says so about the one person in the chapter with no standing to name a line.
- `ch53:99` *A chapter condition* → **A charter condition**.

## 8. Two production instructions that had leaked into the narration — removed

`ch57:79` *and no state file may record it as anybody's finding*; `ch57:107` *nobody in that yard wrote the word **became***; `ch50:91` *I would like the answer to be on the page before somebody has to ask me for it in a room*; `ch54:5` *and that is the chapter*; and `ch57:125` *I have spent a day trying to assemble it out of your chapter headings*, in a character's mouth.

All five now say the thing inside the world. The two that mattered most kept their function: the panel paragraph now reads *it is not a reason and it is not an authority, and it has not gone into a book in this yard in anybody's hand and it is not going to*, and the rootmark record now reads *there is nothing in it about what a man has become, and that is not an oversight: it is the fourth rule this yard has made and it is the only one nobody has ever argued with*.

## 9. The unfulfilled promise — PAID

`PROMPT.md:59` and both state files promised that **the batch's last chapter establishes the panel is spent on a question that turns out not to be the question.** Chapter 59 never mentioned the instrument, the copper seam or the three lines, and `batch-0002/PROMPT.md:145` was already building on it. As written, Batch 0002 inherited a debt that was never offered.

**Chapter 59 now pays it on the page.** On the third, with the reader a full day in the yard, Osvalde Bream looks at four inches of rootmark and asks the obvious question — *somebody in this room has been carrying a thing that answers questions, and has not once put it near a page.* Nobody answers, because the answer is the chapter: **the three lines are about a bead and what a bead holds and what a man is going to keep; they were never about a hand; a bead goes against a wetted lot and cannot be laid against paper at all; the question in that room for four days was a hand on a page; there is no instrument in this district that will read a page, and anybody who goes to Cray and buys one for that counting house will get a device that reports a bean.** Dunmar writes none of it down and says why: *a book that puts a bead's rules in beside a page about a hand is a book that has told a district clerk the wrong thing about both of them.* **The panel stays the instrument's and not a person's, no document quotes it, and the three lines are never repeated.**

## 10. Craft — trimmed, and the good prose left alone

The review named six repetitions that read as tics. The *put his hand flat on the table* tic was **kept where it is a beat** — the broker adopting it at `ch52:105` after watching somebody else do it first, and Lissa Vale squaring the sheet to the edge of the table — and **varied in the three places where it was only a tic** (`ch54:67`, `ch57:17`, plus the broker's second one at `ch52:105` now reading as a man who has done a thing twice). The *a mile and a half of road in front of them* exit cue was **varied at `ch56:103`** and kept at `ch53:157`, which is now *nine miles of bad road*. The Ch 53 lecture is four paragraphs. **Ch 52 is still a real midpoint, Ch 55 is untouched at the joints, Ch 56's refusal of the word *concealment* is exactly as it was, and Ch 59 still closes on a decision.**

**Two chapters were given a scene they needed**, because both were under the outline's 2,600 floor and both were thin for a structural reason rather than an accidental one:

- **Ch 54**, whose Sunday "gets nowhere by construction" because Ch 53 has already spent Gael Senn's finding. The Sunday is now **a choice**: Marek wants a second form to Perrin Osse on Monday, on the reasoning that there is always another form, and Dunmar refuses at the table — *the first form was answered in four days and the second one would produce nothing at all, on purpose, and a body that asks twice has told a district office that asking works.* **+200 words, and a lock: no second demand for the register may be sent.**
- **Ch 55**, which had no beat for the question Lund is actually there for. Tova Reed now answers *what happens to one of the four*: a struck-out line is in an appendix in four counties, on a plate nobody has looked at in six years, and in one man's field, and when that man dies there is nothing left of it anybody can put a name to — **and she has lost none in eleven years and holds four she has never indexed and never told anybody about, including the woman sitting in front of her.** **+250 words, and a standing number.**

## Length, stated honestly

| | Before | After |
|---|---|---|
| Per chapter | 2,511–3,706 | **2,658–3,803** |
| Batch | 29,747 | **31,337** |
| Under the 2,600 floor | Ch 54 at 2,511 | **none** |
| Over the 3,200 ceiling | 53, 57, 58 | 53, 57, 58 — and Ch 53 is 603 over |

The batch is **1,337 over the outline's band**. The overage is the corrected register page (+125), the panel payoff (+350), the Ch 54 scene (+200) and the Ch 55 exchange (+250), less about 460 taken out by tightening Chapters 50, 51, 52, 53 and 56. **Nothing was cut to hit a number that was worth keeping**, and `state/current.md` carries the figure and the reason rather than a comfortable sentence.

## What was deliberately not changed

- **The planned plot.** No card was rewritten, no beat was moved, no character was changed. The register page's column count is a document's shape, not a plot point, and the state files, both batch briefs and `open-threads.md` were all brought into line with it rather than the other way round.
- **Ch 55 and Ch 56's arguments**, including Tova Reed's refusal and Dunmar Fitch refusing the word *concealment* with the proposal and the refusal on the page together. The review called these the batch's best material and they are untouched.
- **Volume 01.** Not one file in `workspace/volume-01/` was edited. Where Volume 01 and Batch 0001 disagreed about the extract, **Volume 01 was treated as canon and Chapter 53 was rewritten to fit it** — which is how the caption reading was found.
- **The one panel, its attribution, and its placement.** Exactly one, in Chapter 57, by a licensed man, at the copper seam, with the use-log line first and the contact tested. Verified still true after the repair: **no document in Chapters 50–59 quotes it**, and every state file still calls it the instrument's and not a person's.
- **`state/phase-ledger.json`.** Controller-owned, still reading `phase-000-bootstrap`. The review flagged it, the pipeline owns it, and it was not touched. `batch-0001/.done` and `volume-close/.done` are both present and `workspace/volume-02/batch-0002/PROMPT.md` is the only next phase on disk.
- **No new prompt was created.** Batch 0002 already exists and was already the next phase; this pass did not add a phase and did not change its day clock, which checks out.
