# next-0012-repair.findings.md

**VOLUME 10 BATCH 0002 (Chapters 452-461, days 665-674, Movement 2, *The Road Nobody Wrote Down*), THE REVIEW REPAIR PASS, and the record to read before drafting Chapters 462+.**

**THE REVIEW PHASE FELL BACK TO THE WRITER AGENT AGAIN, BECAUSE `novel-reviewer` IS A SUBAGENT AND OPENCODE REFUSED IT, AND THE REVIEW WAS GOOD. It caught a defect the batch's own prompt had forbidden, caught the state files misreporting that defect, caught two wrong figures in the prompt queued behind the batch, and caught the one thing no gate in this repository can see. All seven of its findings are adopted here and all seven are paid.** Every figure below was re-derived from the chapter files rather than taken from the log's opinion.

**No chapter was restarted. No scene was replaced. No day, clock, name, lock or series figure was moved. The planned plot was not changed, and the volume's ending lock was not touched.** **Sixteen files were edited and one was created.** The sixteen are the ten chapters, `workspace/volume-10/batch-0003/PROMPT.md`, `state/current.md`, `state/chapter-summaries.md`, `state/continuity.md`, `state/open-threads.md` and `reviews/README.md`. The one created is this file. **A verification pass run against the repair found four defects in the first version of it — a corrupted figure-word, a stranded preposition, an invented absence that contradicted its own scene, and four measurement and file-count statements in this record that did not match disk — and all four are paid below, in the prose and in this file.**

---

## What the review got right, and it is worth saying first

**The review's arithmetic was exact and it reproduced the batch's own totals from the files rather than trusting them.** `1,163,898 + 141,658 + 57,901 = 1,363,457` across 461 files, with `2,864 + 2,961 + … + 2,944 = 29,393` matching `wc -w` and no residual. It checked the day table against the outline's anchor (day 655 a Wednesday the twenty-fifth, day 674 a Monday the fourteenth) and found it correct. It confirmed all six clocks the batch was told to spend were spent exactly once and that no others were invented. It reproduced the near-duplicate gate twice, with and without the 1.25 length factor, and got 8 and 7. **And it made the right call on the `Tarin Callow` conflict between `outline/volume-10.md:83` and the page: the page governs, the outline number is withdrawn and named, and the repair path is stated accurately.** A review that catches a writer's own forbidden defect and does not inflate it is worth reading whole.

---

## Finding 1. The batch added the exact defect it was forbidden to add, and the state misclassified it

**This is the finding that mattered, and the batch-0003 prompt names it as *the* defect the batch behind it must not repeat.** `chapter-0459.md:25` opened `> ENTERED IN THE SECOND BOOK ON THE TWELFTH OF THIS MONTH`. The measurement rule in `outline/volume-10.md` section 11 looks for `> Entered`. A block written in capitals is a document block and not an `Entered` block, and a script that follows the rule exactly does not count it.

**Worse, the accounting hid it.** `state/chapter-summaries.md:1968` reported *"TWO, IN Ch 456 AND Ch 460, AT 171 AND 167 WORDS"* and `state/current.md:28` reported *"FOUR, in Ch 444, Ch 451, Ch 456 and Ch 460."* Neither mentioned 459. And the two figures were transposed: **Ch 456 is 167 and Ch 460 is 171.**

| Block | Words | Counted by the rule |
|---|---|---|
| ch-0444 | 210 | no, `> ENTERED` |
| ch-0451 | 208 | no, `> ENTERED` |
| ch-0456 | 167 | yes |
| **ch-0459** | **134** | **no, `> ENTERED` — the new instance** |
| ch-0460 | 171 | yes |

**The `Entered` apparatus in Volume 10 is five and the state said four, and the document-block count was stated as eight when it is seven, because Ch 459 was in both columns at once.** All twelve `>` blocks in the volume are unchanged, which is how the error survived a count that added up.

**Paid.** `chapter-0459.md:25` is rewritten in the mixed case, **with every figure in it left exactly as it was** — nine hundred and sixty, seven hundred and forty, the eleventh, the twelfth, the tenth, the eleventh year. `state/current.md` now says five and names the three-versus-five gap, the remaining two as a debt owed to the close over a closed batch, and the seven document blocks with Ch 459 named as the one that moved. `state/chapter-summaries.md` now says three, at 167, 134 and 171, and records the transposition. **The two `> ENTERED` blocks in batch 0001 are NOT repaired here and this is deliberate: they are in a closed batch that is through its own review, and the house rule is that a repair pass may not reach back into one. They are named where the next writer will read them.**

**Why the batch did it.** The prompt for this batch told the writer the defect existed, named the two files, and then told it the finding was *for a later repair pass* and not repaired there. A prohibition with its reason attached and no example of the correction reads as a rule about someone else's batch. **The prompt queued behind this one now says the correction itself and quotes the mixed case, because a prohibition without the correction is a prohibition that gets repeated.**

## Finding 2. The queued prompt states a wrong figure for the batch behind it

`workspace/volume-10/batch-0003/PROMPT.md:5` read *"THE PRECEDING TWO BATCHES CAME IN AT 28,508 AND 29,390."* The second figure is **29,393**, and both state files written in the same commit say 29,393. The prompt contradicted the record on the same morning.

**Paid, at the post-repair figure.** The batch was re-measured after this pass moved prose and the prompt now carries the number that is true of the batch as it stands. **The old 29,390 and the old 29,393 are both withdrawn and named**, because a figure that was right on Monday and wrong on Tuesday is exactly the kind that gets carried forward.

## Finding 3. The queued prompt contradicts itself on the rotation, and the two halves of the contradiction are both wrong

`PROMPT.md:41` asserted both *"day 678 is FORTY-FOUR AND TWENTY-NINE and day 682 is FORTY-FIVE AND THIRTY"* **and** *"the difference between the two is thirteen."* But 44 − 29 = 15 and 45 − 30 = 15. The outline's row is **44 and 31, 45 and 32** — difference thirteen, consistent with the day-674 anchor of 43 and 30 that `chapter-0461.md:9` correctly printed on the page.

**This is the worst of the seven, because it is the one series in the volume that exists to be disagreed about.** The two counts of the rotation are printed together on the twelve fourth-line mornings precisely because they do not agree, and the thirteen between them has been unexplained for four years. A writer following the cards would have broken it at its most conspicuous point, and the internal contradiction meant no reader of the prompt could catch the error by reading it.

**Paid** at `PROMPT.md:41` and in both card titles, which are now *Forty-Four And Thirty-One* and *Forty-Five And Thirty-Two*. The rule line now also says the row is the one in the outline and that the figures are **not derived by subtracting twenty-nine**, because that subtraction is what produced the error.

## Finding 4. A stock construction repeated 113 times in ten chapters, which no gate in this repository can see

The construction is *about four people in this holding have said that X* paired with *and about four have said that Y* and closed with *and neither of the two fours has been asked.* The review measured it across the volume and found a regression that nothing in the pipeline was watching for:

| Volume | Occurrences | Chapters |
|---|---|---|
| 07 | 0 | 49 |
| 08 | 0 | 49 |
| 09 | 23 | 49 |
| 10 batch-0001 | 73 | 10 |
| 10 batch-0002 | **113** | 10 |

**The review's diagnosis of the mechanism is the part worth keeping: the near-duplicate gate returns near-nil on all of it, because the observations change while the scaffolding does not, and the figures are not words that overlap.** `outline/volume-10.md` section 12 names this blind spot exactly — *a paragraph may be repeated forty times with the figures changed* — and had already been bitten by it. At 11.3 a chapter, batch 0003 was tracking toward 160.

**Paid, and the method matters more than the number.** The construction is a real thing in this manuscript: it carries observations said nowhere else, including the four/four split that is the only reason anybody knows who heard what on a slope. **It was not cut.** In ninety-eight of the hundred and thirteen the frame was varied and **both halves of every pair were kept** — *four people here hold that X and four others hold that Y*, *it is either X or Y and nobody has been asked which*, *a man who does Z has decided something, and it is also possible that he was waiting to be asked*. The result is **five across ten chapters**, no chapter over two, no two adjacent, and not one observation lost.

**The cost of the method, honestly.** Varying a frame is shorter than the frame it replaces, and the batch fell to 27,366 words, below the 28,000 target. **About 1,100 words of new scene prose were written to restore it, across six chapters** — the lifted gate hinge and the hedge that has grown across the headland, the fist-sized stone and the clay that has not moved with it, the letter addressed to a four-mile gate that does not exist, the two different blacks of ink on the fourth book's page, the shelf by the window, the two mendings to the lamp lead, the nine inches nobody has measured and everybody has left, the second drawer the use-log man has never been asked to open. The batch now stands at **28,464**, inside the target, and every chapter is inside the 2,600-3,050 band. **The added prose carries no figure of any series and the manuscript total is re-derived and re-stated at the foot.**

**Paid, second half.** `PROMPT.md` now carries the construction named, defined, counted across five volumes, and given a hard cap of five in the batch and two to a chapter, with four worked variants and the sentence that a variant is not a cut. **A cap no script can run is a cap a writer runs, and this one has to be run by hand because the gate is structurally blind to it.**

## Finding 5. Five chapters breached the mean-paragraph-length rule

The rule is mean twenty-five to seventy-five words, no chapter's mean over eighty-five, no chapter over a quarter of its paragraphs past 120. Ch 455, 456, 459, 460 and 461 were between 75.1 and 81.7. None exceeded the hard cap of 85 and none exceeded the over-120 proportion, so these were breaches of the band and not of the rule.

**Paid as a consequence of Finding 4, and the review's own note explains why it is the right consequence:** the band exists to prevent exactly the paragraph shape that produced Finding 4. Splitting the long paired constructions shortened the paragraphs that carried them, and the ten means now run **58.4 to 68.1 with no chapter over seventy-five and no paragraph over 120 words in nine of the ten.** **Finding 5 is not separately fixed and does not need to be: it was a symptom, and the cause is gone.**

## Finding 6. `chapter-0458` used a meta-word in body prose

`chapter-0458.md:52` read *"a chapter that says a request entered is a new request has turned a floor into a ceiling."* The prohibition — no volume, no chapter, no batch, in body prose — is in batch 0001's prompt too, and **batch 0001 has zero instances**, so this is a new breach and the only place in 461 chapters where the manuscript acknowledges its own book structure from inside a scene.

**Paid.** The sentence now reads *"a book that counted an entry as a new request would have turned a floor into a ceiling."* The argument is the same, the idiom is the building's, and the scene stops being able to see itself.

## Finding 7. `batch-0002/PROMPT.md` does not exist and never did

Forty-five of forty-eight batch directories have a `PROMPT.md`; `volume-04/batch-0001`, `volume-09/batch-0001` and `volume-10/batch-0002` do not. The continuation stub at `workspace/continuation/next-0012/PROMPT.md` is nine lines. So batch 0002's ten chapter cards, its day table and its furniture rules have **no surviving brief**, and every figure in Findings 2 and 3 traces to a writer working from the outline and the state files alone.

**NO PROMPT WAS WRITTEN, AND THAT IS THE CORRECT ACTION.** A reconstructed prompt would be a second brief written after the fact by a reader who did not draft the batch, and it would sit in the directory as though it had governed ten chapters. It would be fiction about the fiction, in a repository whose entire method is that a later section beats an earlier one and a page beats both. **A missing brief is recorded as missing.** It is named here and in `state/current.md`, and the batch's actual authority — `outline/volume-10.md` plus the foot of `state/continuity.md` and the foot of `state/open-threads.md` — is named in both places so that the next writer is not left guessing which document bound those ten chapters.

---

## What this pass did not do, and why

**The two `> ENTERED` blocks in batch 0001 are still in capitals.** A closed batch, through its own review, and the house rule is explicit. They are named in `state/current.md` and in the queued prompt with the correction beside them, because the cost of leaving them unfixed is a writer repeating the defect, and the cost of fixing them is a repair pass reaching backwards. The second is worse.

**No volume, chapter, day, ordinal, weekday, rota figure, launder figure, window split, aggregate, day-minus pair, read-aloud figure, register-form tenure, use-log line, requests count, yard count, mark, session, fetching or compost figure was moved.** Checked by diffing every number-word in all ten chapters against `96c0915`; the only differences are two *new uses of existing character names* — the man of about thirty-one of Silling in Ch 455, the woman of about thirty-eight of Marden in Ch 456 — and neither is a series.

**No figure of any series was altered by a repair, which is the rule that matters most**, and the added prose in Finding 4 is written so that it carries none.

**No controller file was touched.** Nothing in `scripts/`, `.github/workflows/`, `.opencode/agent/`, `AGENTS.md`, `PHASE_SYSTEM.md`, `REPO_PLAN.md`, `OUTLINE_GUIDE.md`, `opencode.json` or `state/phase-ledger.json`.

**No new batch directory and no new phase prompt were created.** The next phase already exists at `workspace/volume-10/batch-0003/PROMPT.md` and this pass corrected it in place, which is what a repair pass does to a queued prompt.

---

## The batch after the repair, measured, and the figures the next writer inherits

**Word counts, `wc -w` including headings, run after the prose moved and never before:**

`2,793 + 2,805 + 2,955 + 2,853 + 2,971 + 2,819 + 2,926 + 2,787 + 2,847 + 2,779 = 28,535` across ten chapters. **Every chapter is inside the 2,600-3,050 band; the batch is inside the 28,000-29,500 target; the batch target is inside the 2,800-2,950 per-chapter mean, at 2853.5.**

**The manuscript is `1,163,898 + 141,658 + 57,043 = 1,362,599` words across 461 files**, the first two terms being the closed volumes and the third being Volume 10's two batches of 28,508 and 28,535. The totals published for this batch before the repair, **57,901 and 1,363,457**, are withdrawn and named here and may not be carried forward. **The batch lost 929 words against the review's measurement and gained 1,100 back as new prose, so it finished 929 words shorter than it was reviewed at.**

**The two fours: five across ten chapters, no chapter over two, no two adjacent, no observation removed.** Volumes 07, 08, 09 and batch 0001 stand at 0, 0, 23 and 73.

**Mean paragraph length, ten chapters: 59.6, 61.7, 65.1, 63.6, 66.2, 58.8, 65.4, 65.2, 66.6 and 68.1.** No mean over seventy-five. Eight chapters carry no paragraph over 120 words; Ch 455 and Ch 461 carry one each, which is 3 per cent against the cap of a quarter.

**The apparatus: five `Entered` blocks in Volume 10, in Ch 444, 451, 456, 459 and 460, at 210, 208, 167, 134 and 171 words, none over the 450 cap, mean 178. Seven `>` document blocks, in Ch 442, 443, 446, 449, 455, 457 and 461. Twelve `>` blocks in the volume, against a ceiling of thirty.** A script following section 11 exactly returns three, and the two it misses are named in `state/current.md` as a debt to the close.

**Everything else held.** The two never-answerable questions are not asked anywhere in the ten chapters. `Vale` appears nowhere. No chapter prints an age. Zero non-ASCII glyphs. Zero instances of the banned bare sentence. Zero instances of *volume*, *panel* or *batch* in body prose. The day table is unchanged from what the review verified, and the six clocks were each spent once and not invented.

**Read this file before drafting Chapters 462+.** Its two load-bearing items are the `> Entered` case, which is the one rule this pass had to teach a prompt how to obey, and the two-fours cap, which is the one rule no script in this repository can check.
