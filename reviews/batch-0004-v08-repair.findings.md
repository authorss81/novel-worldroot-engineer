# Volume 08, Batch 0004 — Review Repair Findings

**Source of the findings: `logs/batch-0004.review.log`, the review of commit `c297b05` "novel: save writer work batch-0004". Scope: Chapters 374 to 383, days 587 to 596, Movement 4. The batch was NOT restarted. Fourteen edits were made across eight chapters, and every one of them was a figure, a copy error, a malformed clause or a pointer. No day, no clock, no standing count, no lock, no scene and no planned plot was touched.**

## 1. The gates, re-run after the prose moved

| Check | Result |
|---|---|
| `wc -w` incl. headings | 2,898 / 2,788 / 2,774 / 2,796 / 2,822 / 2,775 / 2,752 / 2,782 / 2,763 / 2,800 = **27,950**; ten of ten inside 2,750-2,900 and inside 2,600-3,050 |
| `Entered` blocks, cap 600 | 585 / 590 / 589 / 588 / 590 / 599 / 597 / 588 / 592 / 568; one per chapter; one `>` document block in the batch, at Ch 374, which the prompt permits once |
| Near-duplicate gate, all four batches | 484 inherited; **pairs involving this batch = 0**, before and after |
| Banned bare refrain / non-ASCII | 0 / 0 |
| Banned words; bare `chapter` | 0; 10, all ten headings |
| `about four` | 53 case-sensitive, 62 case-insensitive, **0 inside any `Entered` block** |
| Bold parity, quote parity, trailing space, consecutive blanks, final newline | clean in all ten |
| Double spaces, doubled function words, space before punctuation, space inside a bold opening | **0** in all ten (one legitimate bold paragraph opening at `chapter-0382.md:27`) |
| `workspace/volume-08/batch-0005/PROMPT.md` | untouched, 52,472 words, eleven sections, nine chapter cards |

**The band was not widened and no chapter was declared outside it. No chapter crossed the target of 2,750-2,900 in either direction.**

## 2. The three hard contradictions, repaired

**Ch 383's fetching interval.** The page said *six mornings off* in the prose at `chapter-0383.md:49` and in the block, while the man of about fifty said *the first of the next month is the fifth* thirty lines above it. The run is correct everywhere else: 374 not stated, 375 thirteen, 376 twelve, 377 eleven, 378 ten, 379 nine, 380 eight, 381 seven, 382 six, **383 five**. The rule is sixty-one minus the day, and the first of the next month is day 601. Both instances repaired to **five**. No other figure in the chapter was touched.

**Ch 374's spoken claim.** Iona Vey said *I am in this building once* and was in the room again on days 588 and 589. In this book a speech act is the thing a person is held to, so this was a claim, not a description. Replaced with *I am not here about the two papers*, which is true on day 587 and is what she says on day 588. **The `Entered` block of Ch 374 keeps *WAS IN THIS BUILDING ONCE* and that is correct there**, being a clerk's count of what had happened up to the seventh hour of that evening. The batch prompt is itself inconsistent on this point and a chapter may not inherit a prompt's inconsistency into a character's mouth.

**Ch 375's record asserted a future.** The prose said *this was the last morning she was in this building in this season* and the block said *was in this building twice and not three times*, and Ch 376 gave her a third morning and printed the figure. A clerk's entry for day 588 cannot know there is no day 589, and the word *NOT* turned a count into an assertion. Block clause replaced with *WAS IN THIS BUILDING ON HER OWN ACCOUNT AND NOT SENT FOR*; prose replaced with *nobody in this holding had asked whether she was coming, and nobody had sent her*. **This is the standing rule the repair established: a block enters what the day was and may not enter what the day was not going to be.**

## 3. The eleven remaining prose edits

1. **Ch 374, a sentence that ended on a comma.** *…the two documents upstairs are correct and cannot be put down,* with a paragraph break and nothing after it. Completed as *and nobody here is going to put them down* — the corridor sheet and the sealing order, the lock this volume carries. No new fact on the page.
2. **Ch 374, the bridge interval.** *A month and four days back* was one day short. 587 − 552 = 35 days. Repaired to *a month and five days back*.
3. **Ch 381, the bridge interval.** *Five weeks back* was one week short. 594 − 552 = 42 days. Repaired to *being forty-two days back*, in words rather than weeks so it can be checked by subtraction.
4. **Ch 381, the vault, moved off the bridge's day.** That repair put *six weeks* in the same paragraph as the seed vault's own *on a day six weeks back*, and six weeks before day 594 is day 552, which is the bridge's own day — so the text would have said a bridge and a vault went under on the same morning. The vault is now *a day about two months back*. **No date for that vault is fixed by the prompt, the outline or any page**, and `chapter-0204.md:39` already has it as *about a month ago*, so nothing fixed was broken.
5. **Ch 381, the count of the anchor sentence, one low.** *A person who cannot afterward be asked whether it was right is the third thing an anchor is not* has now been said out loud three times — the sixth month by Tova Reed, the nineteenth by the reader of this body with her name given first, the twenty-fourth by her. The chapter printed two, in the prose and in the block. Repaired to **three**. The adjacent count on the same page, *the count of times the word has been used in this holding with no meaning on it*, is two, is a different series, and **did not move**. The two figures are one sentence apart and must not be made the same figure again.
6. **Ch 377 block:** *THE DRAWER IS SHUT AND AND THEY WERE NOT SAID ALOUD* — doubled `AND`, removed.
7. **Ch 380 block:** *AND WITHOUT A CONVERSATION, AND AND IT CAME THE WAY A THING GOES OUT OF A HAND* — a second doubled `AND`, removed.
8. **Ch 380 block:** a lost sentence break at *AND WAS NOT WALKED THE ENTRY WAS MADE AT THE FIFTH HOUR*, now *AND WAS NOT WALKED. THE ENTRY WAS MADE*.
9. **Ch 380 block:** a double space after *A PERSON HOLDING IT ALONE,*, reduced to one.
10. **Ch 381 block:** the bold opening ran *\*\* THE FOURTH LINE* with a space inside it, and two double spaces sat after full stops at *THE LAUNDERS.* and *AT THE HEAD OF THEM.* All three repaired. The same scan found nothing in the other nine files.
11. **Ch 376 block:** a space before a comma at *THE THIRD THING AN ANCHOR IS NOT , WHICH HE SAID*, removed.

**Six of the eleven were in `Entered` blocks and not in narration, which is the whole argument for the six-hundred-word cap and for the gate that reads blocks as well as prose.**

## 4. The three low findings

**A malformed clause appeared twice and was a dangling ellipsis both times.** Ch 382 read *the four that had been waiting were sorry about it and the four that had not were not*, and Ch 383 read *about four had not, and the four that had not were sorry afterwards* — in both cases with nothing after *had not* for it to be the complement of. Both rebuilt with the complement spelled out. **Neither is a count and neither figure of any count was touched.** The near-duplicate gate passed both of them, which is the strongest argument in this repair for the reviewer reading and not trusting the gate.

**Ch 378 described a sheet that already had its third column ruled six paragraphs before the clerk ruled it.** Repaired without moving a beat, by changing the tense of the first paragraph so that it is now a statement about the finished page: *and there is nothing at the head of the third column and nothing in it*. The column is still ruled by the clerk at the man of about fifty's request, is still empty, and no heading is still written on it.

**The "no yard" date drifted mid-batch.** Ch 373 of batch 0003 and Ch 374 of this batch both said *there has not been a yard in this holding since Sunday*; five chapters of this batch said *since the twelfth of this month*, which is day 582 against Sunday's day 583. **Settled once, in the state layer and on the five pages: the anchor is *since Sunday*, day 583, the thirteenth of the eighth month, and Chs 376, 378, 380, 381 and 383 now read *since Sunday the thirteenth of this month*.** Ch 373 was not touched, because a closed batch is not repaired from inside a later one, **and the anchor was chosen to be Ch 373's and not Ch 376's for that reason and not because one is better.** The count of five things said out loud in a yard and got wrong did not move and could not have, because the batch had no yard on any of its ten mornings.

## 5. The state-layer findings, and the two places the reviewer was itself wrong

**The pointers had fallen two phases behind.** `state/current.md` still named batch 0003 as the current phase, still named `workspace/volume-08/batch-0003/PROMPT.md` as the next phase, and still pointed at the batch 0003 sections of `state/continuity.md` and `state/open-threads.md`. All four are now on batch 0004 and batch 0005 respectively, with the withdrawn forms named beside the new ones. The volume-08 table row also carried four trailing asterisks and now carries none. **This file's own header says an index that names the wrong volume is a bug and that the next-phase line has now been wrong three times; it was wrong a fourth time before this pass, because no gate in the repository checks whether the next-phase line names a batch whose ten chapter files are already on disk.**

**The Tova Reed / Marden separation rested on a false measurement, in both directions.** The state layer claimed Tova Reed was in Chs 378 to 383 and the woman of about thirty-eight of Marden was in Ch 375 alone. Measured on disk, **Tova Reed is named in Chs 376, 377, 378, 379, 381, 382 and 383 and is a pronoun in Ch 380; the woman is named in Chs 375, 376 and 377 and is a pronoun twice in Ch 380.** The two lists overlap at Chs 376 and 377. The conclusion survives — **neither figure is printed on either page** — but the recorded justification was false in both directions, and a later phase trusting it would have reasoned from a false premise. The record now carries the measurement rather than an assurance.

**The *eight hundred* collision search was undercounted, and the review's own correction was also wrong.** The state layer carried ten hits across seven files. The measured figure on a word boundary is **thirteen occurrences on thirteen lines across ten files**, the missing three being `chapter-0186.md:35` twice, `chapter-0217.md:32` and `chapter-0234.md:11`. **The batch prompt said thirteen and was right.** The review said fourteen, which is wrong by one, because a substring search without a word boundary pulls in twelve hits on *eight hundredweight* and *forty-eight hundredweight* — the same words with a unit attached, and not the figure 800 at all. All three forms are now named beside the live one. None of the twenty-five is a collision with this series and none is repaired.

**The no-yard chapter list was wrong, and the review's correction of it was also wrong.** The state layer named Chs 375, 377, 378, 379, 381, 382 and 383. The measured list is **Chs 374, 376, 377, 378, 379, 380, 381 and 383, being eight of the ten; Ch 375 and Ch 382 do not state it.** The review struck Ch 375 correctly and struck Ch 381 incorrectly — Ch 381 states it at `chapter-0381.md:51` — and still omitted Ch 374 and Ch 376. All three lists are now named.

**Every other figure the review recorded was re-derived and holds:** all ten third-launder figures and both word forms, all five day-minus pairs, all ten window splits and their direction rule, all ten aggregates and morning-out-of clauses, all five read-aloud numerators against the day-minus-five-hundred-and-twenty-six denominators, the rota rise on days 590 and 594 alone, the two counts of the fourth-line rotation, the six reason-first runs, the return at Ch 382 with both derivations and the blanks seventeen to eighteen, the sessions three to four entered before the session on day 590, the offer refused and not withdrawn, the register form unfilled, the rootwood unopened with two witnesses, the key unused, the ring unwalked, the seventh column at fifty-two and unread, and no new enemy.

## 6. The three declines, named so they are not re-raised

**The 484 inherited near-duplicate pairs were not touched.** Every one has a batch 0001 or a batch 0002 file in it, both batches are closed and reviewed, and a repair pass does not open a closed batch. The gate's one number that must be zero is still zero. The debt is scheduled and it is the volume 08 close's business.
**Ch 380's second copy of the eleven lines was confirmed, not repaired.** The page already puts the eleven on their own page and the four ruled lines empty, and a second hand on a second sheet is what this holding does with everything that matters.
**Ch 379's and Ch 380's claims about the shape of the rises-and-falls split are claims about a season, not figures in a series.** Ch 380's is true on the page. Neither was touched.

## 7. What the repair established, for the Batch 0005 writer

- **A block may not assert a future, and may not use *NOT* to turn a count into a prediction.** The offer is not withdrawn and not filled and is still open; the register form is not filled; neither document is closed; no block may say otherwise.
- **A count that is the count of a person speaking is printed only on a page where that person gives the reason first**, and Ch 376 and Ch 377 name both Tova Reed and the woman of about thirty-eight of Marden while printing **neither** figure. A Batch 0005 chapter that does the same is safe; a chapter that names both and prints one is a collision waiting to happen.
- **The last yard is before day 583.** Any chapter that needs a yard says which day it is on, or says there has not been one since Sunday the thirteenth of this month.
- **The fetching interval is sixty-one minus the day**, five mornings at day 596, and the twenty-third fetching is on day 601 with no question asked.
- **The live figures after this pass: batch 27,950; volume 08's first four batches 112,899; manuscript 1,137,374 across 383 chapters; the sixth count one hundred and seventy-one, one hundred and seven, twenty-four, fourteen, thirty-six, eighteen.**
