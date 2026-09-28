# VOLUME 09 OUTLINE, THE REVIEW REPAIR PASS

**The record to read before drafting Chapters 393-401.** It repairs the Volume 09
outline phase — `outline/volume-09.md` alone — against the findings at
`logs/volume-09.review.log`. **Six findings applied, three flagged as
controller-owned and not touched, and one of the six was a defect the review
itself did not report. One file edited. No chapter touched, no planned plot
changed, no movement, no card, no day and no chapter moved.**

**The review phase fell back to the writer agent again** — `logs/volume-09.review.log:1`
records `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to
default agent` — so this was a hand pass, and the file says so on its face. Every
finding below was **re-derived from the chapter files by running the command** and
not taken from the log's opinion.

---

## PART ONE — WHAT THE FINDINGS WERE, AND WHAT THEY HAD IN COMMON

**Findings 1, 2, 3 and 4 all sit inside the block at line 456 that asserts the file
had been re-measured.** That block is the load-bearing claim of the whole phase: it
says a pass ran the commands instead of reading the figures, and it lists what
survived. Three of the four defects are *in the list of things that survived*. This
is the exact failure mode the file itself is written about, and it is worth stating
plainly for whoever writes the next one:

> **A LIST OF FIGURES THAT VERIFIES BY BEING RESTATED IS NOT A MEASUREMENT.**

Every figure that survived this pass was confirmed by a command. Every figure that
failed was in a sentence that had been written to *sound* like a verification.

### 1. THE FOUR AND A HALF MILES WERE TWENTY-SIX ON TWENTY-FIVE LINES AND ARE TWENTY-TWO ON TWENTY-ONE

`outline/volume-09.md:55` read *walked twenty-six times on twenty-five lines in
eleven chapters of Volume 07, over both word orders*. Measured:

```
grep -rho "four and a half miles\|four miles and a half" workspace/volume-07/batch-*/chapter-*.md | wc -l   # 22
grep -rh  "four and a half miles\|four miles and a half" workspace/volume-07/batch-*/chapter-*.md | wc -l   # 21 lines
grep -rl  "four and a half miles\|four miles and a half" workspace/volume-07/batch-*/chapter-*.md | wc -l   # 11 chapters
```

**The chapter count of eleven was right; both other figures were wrong.** The split
is **twenty in the order *four miles and a half* and two in the order *four and a
half miles***, and there is no third order anywhere in the volume — no singular
*mile*, no hyphenated *four-and-a-half*, no numeral. The three doubled-chapter cases
are `chapter-0308.md` and `chapter-0325.md` at two occurrences each and
`chapter-0322.md` at seven across six lines, which is where lines and occurrences
diverge.

**No rule this file can find returns twenty-six.** The broadest plausible reading —
*half* within two words of a mile word — returns **5 occurrences on 4 lines in 3
chapters** across Volume 07, and those are the north row and are a different errand
entirely, a distinction the sentence already made and then lost.

**APPLIED**: `:55` now reads twenty-two on twenty-one in eleven, prints the
twenty/two word-order split, and names the withdrawn twenty-six and twenty-five
where they stood. This is a **floor figure for Volume 09** — the walk is walked
again in Ch 415 and 421 — so a wrong base here would have propagated into the two
chapters that move it.

### 2. THE FORTY-SIX PHYSICAL LINES ARE NOT A THING

`:456` listed *the forty-six physical lines* among the figures that held. **No
paragraph anywhere in Volume 08 spans forty-six physical lines.** The widest span of
any paragraph in the entire volume is **3**, being the `>` block at
`chapter-0357.md`. The longest *file* is **91** lines at `chapter-0350.md`, and
forty-six is not that either. Several chapters carry a paragraph of exactly 46
*words*, which is the likeliest way the figure was manufactured.

**APPLIED**: the figure is **withdrawn and named, with no number put in its place**,
because there is none to put. Inventing a replacement would have repeated the
defect. The real measured fact — the three-line span at `chapter-0357.md` — is
retained and separately verified.

### 3. THE REPAIR RECORD MISCOUNTED ITS OWN SCOPE AS FIVE PLACES WHEN IT WAS FOUR

`:456` read *which read* *not asked a sixth time* **in five places** and is *not asked
a fifth time* **in all five**. `git show HEAD~1:outline/volume-09.md | grep -c "sixth
time"` returns **4** — the header at `:21`, the thread-table preamble at `:188`, the
first guardrail at `:230`, and the refusals at `:390`. The record overstated its own
reach by one.

**The ordinal itself is right and is NOT touched.** The state layer carries the
question as *asked four times* in `state/continuity.md` (at `:4423`, `:4583`, `:4778`,
`:4907` and onward), so the fifth is the one refused, and the direction of that repair
holds. Only the count was wrong.

**APPLIED**: *in four places* and *in all four*, with the four locations named and a
sentence stating that the fifth occurrence of the words *sixth time* anywhere in the
file is the one inside the record itself, which quotes the form in order to withdraw
it. A self-describing record that cannot count its own edits is the same defect as a
figure that cannot be reproduced.

### 4. THE DIFF CARRIED FIVE CHANGES AND THE RECORD NAMED FOUR

The `Series layer` field was rewritten from the bare numeral `3` to *World-building
layer 5 with the edge of layer 2*. This is a **genuine fix** — all eight other volume
outlines carry the `World-building layer N` form, so a bare digit was a schema
break — and the writer's log disclosed it. But the in-file record did not, and that
record is the one place a reader would look for it.

**APPLIED**: the record now reads **FOUND FIVE THINGS** and names the fifth, with the
layer choice justified from the volume's own content (four counties, three councils,
an assembly, a charter of plural stewardship) rather than asserted.

### 5. THE HEADER SAID THE WORD *SEVENTEEN* OCCURS IN NO FILE UNDER `outline/`, AND IT OCCURS IN SIX

**This is the one the review did not report**, found while re-verifying the record's
own supporting citation. `grep -rl seventeen outline/` returns **seven files**, six
besides this one: `volume-01.md`, `volume-02.md`, `volume-04.md`, `volume-07.md`,
`volume-08.md` and `batches/volume-01-batch-0001.md`.

The *argument* the sentence was making survives, and the correction makes it
stronger. `outline/series.md` contains **zero** occurrences — that is the file the
count would have to come from. Of the six, five are ordinary counts of days,
chapters or name-pairs. The single use that IS a count of volumes is
`outline/volume-08.md:104` — *a shape invented in the seventeenth volume* — which is
**the inherited count walking about inside the closed volume**, and that is a
positive reason the count is not derivable rather than a reason against it.

**APPLIED**: `:7` now says the word occurs nowhere in `series.md`, names the six
files, names the one volume-count use, and marks the withdrawn claim as *"one of the
kind this file wants to be rid of, a figure that looks checked because it is easy to
say and is not a measurement."*

### 6. NO REVIEW ARTIFACT WAS COMMITTED

There was no `reviews/volume-09*.findings.md`, though the Volume 08 outline phase
committed one (`f5c224e`). The four repairs and their evidence existed only inside
the outline being repaired, which means a reader auditing this phase has nothing to
audit against.

**APPLIED**: this file.

---

## PART TWO — WHAT WAS RE-DERIVED AND HELD

Every figure below was **reproduced by command** in this pass, not read out of the
previous pass's list. This is the part that would otherwise have been the risky
one, because the previous pass is the one under suspicion.

| Claim | Measured |
|---|---|
| Manuscript 1,163,898 words / 392 files | exact |
| Volume 08 139,423 words / 49 chapters | exact |
| V08 batch totals 28,006 / 28,581 / 28,362 / 27,950 / 26,524 | exact, summing with no residual |
| V08 mean 2,845.4; min `chapter-0351.md` 2,701; max `chapter-0389.md` 2,963 | exact |
| `kerb` singular, manuscript-wide: 142 (94/32/1/15) | exact |
| Thornwild 6 / 6 / 17 / 0 | exact |
| `>` distribution: 36 chapters with one, 4 with two, 9 with none = 44 across 40 | exact |
| `Entered` apparatus: 39 blocks, 23,018 words, mean 590.2, 16.5% | exact |
| V08 near-duplicate @0.85: 484 pairs / 118 paras / 7,420 words / 21 chapters | exact |
| V08 @0.80: 582 (**+98**); @0.75: 723 (**+239**) | exact — the withdrawn 8 and 14 were genuinely wrong |
| V07 @0.85: 3,241 pairs / 281 paras / **49** chapters | exact — the withdrawn 48 was wrong |
| 49 day rows vs the day-451-Tuesday anchor | **zero mismatches**; chapters 393-441 and days 606-654 both contiguous, chapter-day +3 throughout |
| Fourth-line mornings: 13 | exact — day 605 is the *third* line per `batch-0005/PROMPT.md:118`, so 606 is the fourth |
| `series.md:6` = 16 volumes; `:253` = V08 power; `:265` = V09 power; `:287` = V11 power | exact |
| 35 thread rows, 49 day rows, 5 movements, ending lock intact | exact |

**On the near-duplicate method**, because it has burned this repository twice: the
canonical script at `workspace/volume-08/batch-0005/PROMPT.md:133` compares **lists
of words**, not joined strings. A joined-string comparison returns 601 at the same
rule and a Jaccard word-set pre-filter is **not** a sound lower bound for
`SequenceMatcher.ratio()` (it returns 173). Only `quick_ratio()` is sound, since
`ratio() <= quick_ratio()`. The 484 figure is correct and reproduces unfiltered.

---

## PART THREE — FLAGGED, NOT FIXED

**7. The reviewer subagent is not dispatching.** `logs/volume-09.review.log:1` opens
with `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to
default agent`. The specialized reviewer named in the system prompt is not running,
and this is the **third** logged fallback in the series. The volume-08 outline repair
record says the same thing about its own log. **Controller-owned — flagged, not
edited.**

**8. `state/phase-ledger.json` still reads `phase-000-bootstrap` / `planned`** with
nine volumes shipped and 392 chapters on disk. **Controller-owned — flagged, not
edited.** The volume-08 close and this phase both left it alone, correctly.

**9. Commit traceability.** The outline landed under a *checkpoint* commit and the
repairs under a message reading *save writer work volume-09*, where the Volume 08
equivalent was split into *save writer work outline* + *save review fixes outline*.
**Controller-owned — flagged, not edited.**

A tenth item, cosmetic and not present in the outline: `logs/volume-09.log` gives
`chapter-0392.md` body words as 2,904, actual **2,903** (the mean of 100.1 and the
longest paragraph of 216 both hold). A log is not a state file and is not corrected
in place.

---

## PART FOUR — SCOPE

**One file edited: `outline/volume-09.md`.** No chapter file touched, no batch
directory created, no card written, no movement moved, no day or chapter number
changed, no thread answered, no state file rewritten. The five movements, the
chapter ranges 393-441, the days 606-654, the 49-row day table, the 35 thread rows
and the ending lock are all byte-identical to the file that was reviewed.

The prose of the file was **preserved and extended, not rewritten**. Repairs 1, 3, 5
and 6 corrected a figure, a count, a citation and a scope statement. Repairs 2 and 4
added sentences, because the house rule this file sets for itself is that a withdrawn
figure is **named where it now stands** rather than silently overwritten, and a
withdrawal with no number needs words around it.

**The rule that governs the next phase is unchanged and is restated in the file:** a
volume-09 chapter may not answer, close, reword, advance to a figure, sum or group
any of the thirty-five threads. A thread may advance. **Whose order it is** is not
asked a fifth time and is not named. **Whether the telling is still going on** may
not be mentioned at all. The figure corrected in repair 1 — the four and a half
miles at **twenty-two on twenty-one lines in eleven chapters** — is a **floor** for
Chapters 415 and 421, and the next writer subtracts from twenty-two.
