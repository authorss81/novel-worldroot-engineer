# VOLUME 08 PLANNING -- THE REVIEW REPAIR PASS, AND THE RECORD TO READ BEFORE `outline/volume-08.md` IS WRITTEN

**The review at `logs/volume-08.review.log` returned four findings against the Volume 08 planning phase: one HIGH, two MEDIUM, one LOW carrying two items. Three are applied, one item is declined as a false alarm, and no chapter, no card, no day, no figure and no scene of Volume 08 was written or altered. Twelve files were read and six were edited: `state/current.md`, `workspace/volume-08/outline/PROMPT.md`, `reviews/volume-08-planning.findings.md`, `reviews/README.md`, `state/continuity.md`, and this file.**

**READ FINDING ONE FIRST, AND IT IS THE ONE THAT MATTERS, AND IT IS A ONE-LINE FIX. The dispatch pointer every phase reads before anything else was aimed at the phase that had already run.**

---

## FINDING ONE, HIGH, APPLIED. `state/current.md:15` NAMED THE PLANNING PHASE AS THE NEXT PHASE

**WHAT THE REVIEWER FOUND.** The planning phase repaired the *figure* on the pointer — the withdrawn `five days` count — and left the *target* stale. The line still read **`workspace/volume-08/PROMPT.md`, the VOLUME 08 PLANNING PHASE**, which is the phase that produced the very commit in which the line was edited. The real next phase is `workspace/volume-08/outline/PROMPT.md`, which that same commit created.

**CONFIRMED ON THE PAGE BEFORE THE FIX.** `state/current.md` has exactly one `Next phase:` line and it is line 15. `workspace/volume-08/` held two files at the time of the review and holds two now: `PROMPT.md` at 17,498 bytes and the `outline/` directory, so the pointer named a file that exists — which is why nothing caught it. A reader cannot tell from the path whether a prompt has run. **Only the record can, and the record said the phase was next.**

**WHY IT OUTRANKS EVERYTHING ELSE IN THE REPORT.** A stale figure is read by a human and disbelieved. A stale *pointer* is read by a dispatcher and obeyed. Left alone it runs the planning phase a second time, and the second run would find `reviews/volume-08-planning.findings.md` on disk, conclude the phase had run, and have nothing to measure against.

**THE REPAIR.** Line 15 now names **`workspace/volume-08/outline/PROMPT.md`, the VOLUME 08 OUTLINE PHASE**, and says what that phase writes and that `outline/volume-08.md` does not yet exist. **THE SUPERSEDED POINTER IS NAMED IN PLACE BESIDE THE LIVE ONE, WITH THE REASON, following the convention this repository established for a withdrawn figure: *this is a pointer that has already been wrong once, and the withdrawal is the only thing standing between this file and it being wrong again.***

**AND THE GENERALISATION, WHICH IS THE PART WORTH CARRYING.** The planning phase's own findings file opens its repair section by praising itself for fixing a withdrawn figure at exactly this line, and calling the surviving disagreement between line 15 and line 268 "the highest-consequence instance of the failure this repository keeps paying for." **It was right about the failure and wrong about the line, because it audited the line's *contents* and did not audit the line's *function*, and a line's function is to point somewhere. A pass that edits a dispatch line must re-read what it now dispatches to, and not only what it now says.** Its claim of *exactly one repair* is withdrawn for the same reason: the repair it made was real and it was not the only thing on that line that was wrong.

---

## FINDING TWO, MEDIUM, APPLIED. THE NON-ASCII FIGURE WAS BYTES AND WAS CALLED GLYPHS, AND THERE ARE NO CURLY QUOTATION MARKS

**WHAT THE REVIEWER FOUND.** The figure **369, 66, 30, 0, 0, 0, 0** appears in two files, each time labelled a glyph count, and each time attributed to *the em dash and the curly quotation marks*. Re-measured, the real character counts are **123, 22, 10, 0, 0, 0, 0** — exactly one third — and the manuscript contains no curly quotation mark at all.

**RE-DERIVED HERE FROM THE FILES, NOT TAKEN FROM THE REVIEW.**

| Volume | Bytes (`LC_ALL=C`) | Characters (`LC_ALL=C.UTF-8`) | Ratio | Lines carrying one (`grep -c`) |
|---|---|---|---|---|
| 01 | 369 | **123** | 3.00 | 89 |
| 02 | 66 | **22** | 3.00 | 15 |
| 03 | 30 | **10** | 3.00 | 6 |
| 04–07 | 0 | **0** | — | 0 |

**THE RATIO IS THE WHOLE OF IT, AND IT IS NOT A COINCIDENCE.** Every non-ASCII character in the manuscript is `e2 80 94`, U+2014 EM DASH, three bytes in UTF-8. Swept manuscript-wide, the only non-ASCII character that exists is that one, one hundred and fifty-five times, and there is no curly double quote, no curly single quote, no en dash and nothing else at all. So 369 is not a miscount that happens to be three times too big; it is a byte count wearing a glyph label, and 123 + 22 + 10 = 155 closes on the volume totals.

**THE THREE SITES REPAIRED, AND EACH IS A PLACE A FUTURE PASS WOULD READ FROM.**
- `reviews/volume-08-planning.findings.md` Part Five, Fault Three, which printed 369, 66, 30 as a glyph count.
- `state/continuity.md:7426`, which printed the identical figure and the identical curly-quote claim in capitals, and which is the append-only record every later phase reads.
- `reviews/README.md`, whose index entry repeated both.
- and `workspace/volume-08/outline/PROMPT.md` §10, which inherited all three from the planning phase, so **the wrong figure would have been carried straight into the outline phase's own mechanical instruction.**

**THE SUBSTANTIVE ERROR IS THE SECOND HALF AND IT IS WORSE THAN THE ARITHMETIC.** *The em dash and the curly quotation marks were Volumes 01 to 03 house style* describes a mark the book has not carried since Chapter 10. The true history is at `reviews/volume-01.findings.md`: Chapters 1–10 used curly quotation marks and apostrophes, Chapters 11–49 used straight ones, the split falling exactly at the Batch 0001 / Batch 0002 seam, and **1,886 curly marks were converted to straight at the Volume 01 close** — so the curly marks were one batch of one volume's style and were withdrawn inside that same volume. `bible/terminology.md:7` records straight marks as the standing rule. **A Volume 08 outline told the curly quote is house style will put it in, and it will do so believing it is following a rule rather than breaking one.**

**THE TEST IS NOW NAMED IN BOTH FILES, BECAUSE A FIGURE IS NEVER WITHDRAWN WITHOUT THE TEST THAT PRODUCED IT.** A glyph count is `LC_ALL=C.UTF-8 grep -o '[^ -~]' | wc -l`; a byte count is the same command under `LC_ALL=C`; **and check three as written at `reviews/README.md` uses `grep -c`, which returns LINES, so a file-level gate is tripped by one em dash on a line however many the line carries.** Without this a later pass runs a glyph check, gets 123 against a record that used to say 369, and concludes the manuscript changed. **That is the *pass that reports a right figure as a wrong one* error, which the Volume 03 and Volume 07 records both name as the more dangerous of the two, and here it would have been produced by the repair itself.**

**THE ONE DEBT THIS DOES NOT PAY, AND IT IS NOT OURS.** The check at `reviews/README.md` still reports FAIL on sixty-plus files of Volumes 01 to 03, and the planning phase left the scope sentence to the phase that owns the mechanical record. That is still owed and is not paid here. **What is changed is that the record now says what the check is actually reporting, so the debt can be paid by whoever pays it.**

---

## FINDING THREE, MEDIUM, APPLIED. `favor` IS FIVE OCCURRENCES ON FOUR LINES IN THREE CHAPTERS

**WHAT THE REVIEWER FOUND.** `reviews/volume-08-planning.findings.md` Part Four, item TWO read *`favor` 5, on four lines in four chapters.* The occurrences and the lines are right. The chapters are **three**.

**RE-DERIVED, AND THE DOUBLED LINE NAMED.** `chapter-0297.md:39`, `chapter-0307.md:41`, `chapter-0309.md:29` and `:29` again, `chapter-0309.md:47` — five occurrences, four lines, **three chapters**, the doubled line being `chapter-0309.md:29`. `favour` remains three, all on `chapter-0325.md:39`, and `licence`, `judgement` and `defence` remain zero in Volume 07.

**WHY A CHAPTER COUNT MATES MORE THAN IT LOOKS.** The governing rule in these files is that a list is not a count, and this repository has been bitten four times in four volumes by exactly that. Here the error runs the safe direction — a sweep told to expect four chapters will find three and read the missing one as a deletion, or will not check the fourth at all. **The related figure at `chapter-0325.md:39` is not touched: it is the British `favour` line, and no Volume 07 chapter uses both forms, which is the Volume 07 close's own correction and still holds.**

**APPLIED IN BOTH FILES THAT CARRY IT** — the findings file and §9 TWO of the outline prompt, which had inherited *four lines in four chapters* from the findings file. `state/current.md` was checked and does not carry the chapter count, only the three `favour` instances, which are right.

---

## FINDING FOUR, LOW, ONE HALF APPLIED AND ONE HALF DECLINED

### FOUR A, APPLIED. §6 SAID *ZERO IN SPEECH ACROSS VOLUME 07* AND THEN CITED A SPOKEN INSTANCE

**THE CONTRADICTION AS PRINTED.** `workspace/volume-08/outline/PROMPT.md` §6 read *`Marek` and `Vale` are **zero in narration and zero in speech across Volume 07*** and, four words later, *The count of the first time either is said out loud in a yard is ONE, IT WAS SPENT IN VOLUME 07 at `chapter-0333.md:23`.* Line 23 is speech.

**RE-DERIVED.** `Marek` stands at **one** in Volume 07, in speech, at `chapter-0333.md:23`; `Vale` stands at **zero**; and there is no instance in narration. The one is spoken by the man of about fifty, about soft ground on the west dyke, to about three people with the day sheet against the cart's side — *he did not stop, and he did not look up, and he did not know he had said anything*, three of the five people in that yard heard the whole sentence and about two heard the half of it with the name in it. On paper the name appears **twice in the whole manuscript**, both capitals, both on the acknowledgment line of the Office's sheet, at `chapter-0248.md:27` and `:83`. **The name rule holds and the count of one is spent. Only the wording was wrong.**

**WHERE THE WRONG WORDING CAME FROM, AND IT IS THE SAME DISEASE.** Guardrail 9 of `outline/volume-07.md:198` reads *zero in narration, zero in speech, and two on paper **in Volume 06***, both at `chapter-0248.md:27` — correct in its own scope. **Re-pointed at Volume 07 without re-measuring, the same words became false while sounding more authoritative, because the inherited sentence was already known to be true and the volume number was the only thing that changed.** A re-pointed guardrail is a new claim and has to be re-measured, exactly as a re-derived rule has to be re-derived.

**WHY THIS ONE IS WORTH A LOW RATHER THAN NOTHING.** The name rule is the one rule in that paragraph a card can break by accident, and it breaks in a way that looks like corroboration: **a writer who reads *zero in speech*, finds one on the page, and concludes the name rule has already been broken will not put the name in — and will not report a figure that was wrong either, because the figure will read as the violation.** §6 now states zero in narration, one in speech at the citation, zero for `Vale`, and two on paper manuscript-wide, and it names the withdrawn wording and its Volume 06 origin.

### FOUR B, DECLINED. THE *FOUR MORNINGS IN TWO CONSECUTIVE-DAY PAIRS* CLAIM IS CORRECT AND THE REVIEW COULD NOT REPRODUCE IT BECAUSE ITS EVIDENCE WAS INCOMPLETE

**THE REVIEWER ASKED FOR THE DERIVATION TO BE NAMED, DOUBTING THE FIGURE. THE FIGURE IS RIGHT. The derivation is now named, and the prose is unchanged.**

Re-derived from the page, in Volume 07:

| Chapter | Line | What it prints | Reading morning? |
|---|---|---|---|
| `chapter-0295.md` | 55 | forty-six, **AND IS NOT READ** | **No** |
| `chapter-0299.md` | 71 | forty-seven, *WAS READ THIS AFTERNOON … THIS IS THE THIRTIETH* | **Yes** — 30th of the 5th |
| `chapter-0300.md` | 33 | *STOOD AT FORTY-SEVEN AND IS FORTY-EIGHT*, read on the first day of a month | **Yes** — 1st of the 6th |
| `chapter-0329.md` | 21 | *STOOD AT FORTY-EIGHT AND IS FORTY-NINE*, read on the thirtieth of this month | **Yes** — 30th of the 6th |
| `chapter-0330.md` | 25 | *STOOD AT FORTY-NINE AND IS FIFTY*, read on the first day of the seventh month | **Yes** — 1st of the 7th |
| `chapter-0341.md` | 83 | *stands at fifty* | No — a standing, not a reading |

**Four mornings, two consecutive-day pairs, exactly as §3 says. The two pairs are 510/511 and 540/541, and the manuscript itself names the pair count and the four-year history three times**: *THIS IS THE SECOND SUCH PAIR IN FOUR YEARS* at `chapter-0300.md:33`; *THIS MORNING AND TOMORROW MORNING ARE TWO READINGS IN TWO DAYS FOR THE THIRD TIME IN FOUR YEARS* at `chapter-0329.md:21`; *THE PAIR IS THE THIRD SUCH PAIR OF CONSECUTIVE READING DAYS IN FOUR YEARS* at `chapter-0330.md:25`.

**WHERE THE REVIEW WENT WRONG, IN TWO PLACES, AND BOTH ARE THE CLASS OF ERROR THIS REPOSITORY KEEPS PAYING FOR.** First, it counted `chapter-0295.md`, which says in capitals that the figure is **NOT READ** — a standing, not a reading. Second, **it stopped at `chapter-0329.md` and treated forty-nine as the last figure, missing `chapter-0330.md` entirely, where the door is read on the first of the seventh month and goes to fifty.** Two of the four mornings were not found, which produced three.

**THE CONVICTION IS THE WORTHLESS PART OF ANY AUDIT OF A COUNT, AND IT IS WHY THE DERIVATION IS NOW ON THE PAGE.** The reviewer's doubt was reasonable and its arithmetic was wrong. **§3 now names all four chapters, the days, the figures, and the 0295 exclusion, so the next phase derives the four and does not re-litigate them.** The one change is additive: the claim, the figure and the arithmetic of §3 are untouched.

---

## WHAT THIS PASS DID NOT TOUCH, AND WHY

- **No chapter.** All 343 stand at 1,024,475 words, unchanged, and none was opened for writing. Finding Four B was settled from four chapters and edited nothing in any of them.
- **`outline/series.md` and `outline/volume-07.md`.** Finding Four A is a mis-scoped guardrail in a *prompt*, not a defect in the closed outline, and the closed outline's guardrail 9 is correct in its own scope.
- **`reviews/README.md`'s four check commands.** The check-three scope sentence is still owed to the phase that owns the mechanical record; what changed is that the figure the record gives is now a character count and the line counts are named.
- **`state/phase-ledger.json`, which is six volumes out of date.** A controller decision and not this pass's, and named as such at §14 of the outline prompt.
- **The planned plot.** Nothing in this pass touches a day, a chapter range, a movement, the central pressure, the turn, the climax, the resolution, the antagonist's offer, the relationship locks, the power stage or the ending lock.

---

## THE THREE FIGURES THIS PASS CORRECTED, AND THE ONE THAT WAS RIGHT AND WAS NEARLY FIXED

**369 → 123, 66 → 22, 30 → 10**, in three files, plus a fourth claim about curly quotation marks that described a character the manuscript has not carried since Chapter 10. **Four chapters → three**, for `favor`. **A dispatch pointer**, from a phase that had already run to the phase that has not.

**And one claim the reviewer doubted and the reviewer was wrong about: four mornings in two consecutive-day pairs.** The lesson is the one this repository has now paid for five times in four volumes and it is not about the number. **A count defended by its derivation survives a challenge; a count defended by its author's confidence does not, and the two look identical in a findings file.** Every figure in the two files this pass edited now carries either the test that produced it or the chapters it was counted from, and a later pass will not have to re-derive any of them to know whether to believe it.

---

**AND THE ONE-LINE VERSION.** The review returned four findings and three were real: a HIGH stale dispatch pointer at `state/current.md:15` that named the planning phase as the next phase, a MEDIUM non-ASCII figure that was a byte count labelled as a glyph count and a curly-quote claim describing a mark withdrawn inside Volume 01, a MEDIUM chapter count of four for three chapters, and a LOW contradiction in the name rule; the fourth finding's two items split, one applied and one declined as a false alarm with the four reading mornings tabulated from the page. Six files edited, no chapter touched, the manuscript still 1,024,475 words across 343, and the only next phase is still `workspace/volume-08/outline/PROMPT.md`, now named correctly on the line every phase reads first.
