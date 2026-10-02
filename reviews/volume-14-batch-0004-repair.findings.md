# VOLUME 14, BATCH 0004, THE REVIEW-FIX PASS, AND THE RECORD TO READ BEFORE THE VOLUME 14 CLOSE

**Phase reviewed: Volume 14 Batch 0004, days 881 to 890, `chapter-0668.md` to `chapter-0677.md`,
committed as `a5d8467`. Review read at `logs/batch-0004.review.log`. This is the fix pass. No
morning was restarted, no scene was replaced, no planned plot changed, and no figure of any series
was touched. Two words were edited in the whole batch, both of them in a plan or a record rather
than in a scene, and the third edit was in the manuscript and was one word in one line.**

**Eight findings came back. Three are repaired here. One is repaired in the state layer and named.
Four are left to a pass with the standing to pay them, and the reason each is left is written
below rather than implied. The prose of the batch is unchanged apart from one word and the review
itself calls it finished fiction; nothing in the findings required a sentence to be rewritten.**

---

## 1. The two edits in the batch itself

### 1.1 A banned bare word on one page, `chapter-0676.md:95`

The clerk says the last part of his reading over, and the sentence stood:

> **"I have said that last part out loud five mornings running at the same volume every time and
> it does not get quieter or louder."**

**`volume` is now `level`, and nothing else in the line moved.** The card set at
`outline/batches/volume-14-cards.md:125` bars the bare words *volume, batch, chapter, seat,
fieldbook* and *panel* from body prose, and *volume* was the only one of the six standing anywhere
in four batches; the sweep is now zero on all four.

**The writer's own measurement file did not catch it, and the reason is the part worth keeping.**
Its mechanical sweep at `reviews/volume-14-batch-0004.findings.md` section 4 runs non-ASCII, dashes,
digits, tabs, trailing spaces, quotation and bold balance, paragraph length, closing openers and
quote adjacency, and **banned bare words are not in it.** A sweep is a list of the checks it runs
and a clean result on a page that carries a breach is a check that did not run. **The next pass that
builds the standing-item gate owes the banned-word list as its first item, because it is six words
long and it catches a page that every other check calls clean.**

### 1.2 The queued prompt named a morning that is not a fourth-line morning

`workspace/volume-14/batch-0004/PROMPT.md:56` read *days eight hundred and eighty-two, eight hundred
and eighty-six and eight hundred and eighty-nine*. **The third is day eight hundred and ninety**,
being a day congruent to two modulo four; eight hundred and eighty-nine is not, and a fourth-line
morning is nothing else.

**Every other statement of the same fact in that prompt already said ninety**: the count-in-force
paragraph at line 49, the day table at line 38, and the three card headers at lines 102, 169 and 233,
which call 882, 886 and 890 the eighth, ninth and tenth of the twelve. **One clause in one paragraph
was wrong and the rest of the file was right, which is the shape of error that only a rule catches,
because a reader checks a sentence against the file it sits in and the file agrees with itself.**
The pages were right throughout: the count is carried in `chapter-0669.md`, `chapter-0673.md` and
`chapter-0677.md`.

**A prompt is the one file nobody re-measures**, because the writer who inherits it did not write
the chapters it describes. This one had been checked field by field against a regenerated table
and the check was not run on the sentences around the table.

---

## 2. The record that was not what it was headed

`reviews/volume-14-batch-0004.findings.md` was written by the writer phase that drafted the ten
mornings, in the same commit, and it sat in this directory under this directory's naming rule,
where a reader would take it for the independent review. **It is now headed as what it is, on its
first line, and the header names this file as the review and states that the self-check is not
corroboration of itself.** This is the fifth time this repository has had to relabel a writer
self-check; the precedent is `reviews/batch-0004-v07.findings.md` and it is recorded in
`reviews/README.md`.

**Its own error is also corrected there.** Its restatement of the read-aloud rule printed the
numerator in the window half's form, `a hundred and forty-seven`, where the plan's spelling section
mandates `one hundred and` and where all twenty read-aloud mornings on disk are right. **The
derivation got every value correct and the form wrong, and that is the generalisable half of the
finding: a script that derives numbers does not know which spelling each series takes, so a
derivation can be wholly right and still carry a series's wrong form.**

**One correction to the review's own report, recorded because the repair depends on it.** The review
described that item as giving the anchor day as eight hundred and eighty-three. **The file says
eight hundred and three, which is correct.** The error was the form and not the day, and repairing
the day would have put a second, worse error into a correct file.

---

## 3. The four this pass may not pay, and why

**These are recorded, not repaired, and each one is a refusal with a reason rather than an omission.**

1. **The plan's day table prints the read-aloud numerator in the wrong form on all twenty-five of
   its rows** (`outline/volume-14.md` section 9), against the same file's section 7, which mandates
   `one hundred and` for that series. **The manuscript is right on all twenty occasions and the
   queued closing prompt is right on all nine of its rows, and the state layer already withdraws
   that cell on every odd morning of the volume including days 891 to 899**, so nothing is
   inherited wrong by the next writer. **`outline/volume-14.md` is a completed phase's file and this
   pass has no standing to edit it, and a twenty-five-cell edit to a generated table is exactly the
   change that introduces a second error.** The correction is owed by whoever owns the outline and
   is now named in `state/continuity.md` section 7 and in `state/current.md` section 4.
2. **The plan's allowance clause and its separation clause contradict each other** on the volume's
   first and closing morning, where both locked sentences are required and are also forbidden. The
   card set records the contradiction at its section 11 and resolves it in favour of the allowance
   on those two mornings. **Unrepaired in the plan; now carried as the third unrepaired conflict in
   `state/continuity.md` section 6.**
3. **`state/phase-ledger.json` reads `phase-000-bootstrap` while fourteen volumes are written**, and
   `workspace/volume-14/plan/` holds a prompt with no marker that the runner can retire, so after
   the closing batch the selector may pick the planning phase instead of building the volume's
   close. **Both are controller-owned. A writing phase may not forge, move or delete a marker and
   may not edit the ledger**, and the second item was already standing at
   `state/open-threads.md` section 4 item 6 before this review found it independently. **The
   control plane owns it and the chain stalls once Batch 0005 is written unless it is fixed there.**
4. **Whether the closing batch spends four in-between locked sentences, running both allowances to
   their cap and overriding prohibitions on seven cards.** The queued prompt's section 5 reasons it
   out under the house's existing allowance-over-floor logic and was written before the review ran.
   **The review is right that this is the first time in the volume both allowances go to the cap,
   and right that it should be decided before the batch runs and not after.** The decision is now
   recorded in `state/open-threads.md` section 4 and `state/current.md` section 8, together with the
   three things the closing batch must be measurable against if the decision stands. **No morning
   of the closing batch is written, so nothing is spent yet and the decision is still cheap to
   change.**

---

## 4. What was re-measured after the edits, and what came back

**The figure work in the self-check was reproduced independently by the review and not one value
moved: two hundred and fifty-five items required, two hundred and fifty-five present, zero
failures; both duplicate gates reproduced on both scopes; the two locked figures each standing
whole once and once only, on their own mornings, with no shortened form anywhere.** Those findings
are the review's and they are adopted here.

Re-run after this pass's two edits, on the batch and on the four batches behind it:

| Check | Result |
|---|---|
| Banned bare words, six of them, four batches | **zero**, was one |
| Non-ASCII characters | zero in all ten files |
| Digits in body prose | zero |
| Per-file word counts | **unchanged**, 3,041, 2,825, 2,632, 2,734, 2,489, 2,673, 2,633, 2,353, 2,445, 2,746, total twenty-six thousand five hundred and seventy-one |
| Day 890's thirteen standing figures in `chapter-0677.md` | all present |
| Files ending in a newline | ten of ten |
| Controller files touched | **none**: no marker, no ledger, no workflow, no agent definition, no `AGENTS.md` |

**The word counts do not move, because the word repaired was one word.** A repair that cannot be
seen in the batch's own measurements is a repair to a rule or a record; this pass made two of those
and one that a single sweep now returns clean.

---

## 5. The one thing in the batch no gate can judge, left standing

The review named it and did not overrule it. **The batch's central pressure is the reach's cost and
nobody in this holding is asked to choose anything on any of the ten mornings.** Whether the
arithmetic stays honest while nobody chooses is a judgement about a condition and not about a stall,
and it belongs to the close. **Nothing in this pass touches it, and the closing batch inherits an
arithmetic that has already given one answer on day 890 and may not quietly give a second**, which
is at `state/chapter-summaries.md` section 4.