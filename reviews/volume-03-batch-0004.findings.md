# Volume 03, Batch 0004 — review findings and what was done

**Volume 03, Batch 0004 (Chapters 129–138, days 211–230), Movement 4, *The Unfit Category*.** Review run after the batch was drafted and after the next-phase prompt was written, against commit `e7a824c` (*novel: save writer work batch-0004*). Raw report: `logs/batch-0004.review.log`.

**The review phase fell back to the writer agent** (`logs/batch-0004.review.log:1` — *agent "novel-reviewer" is a subagent, not a primary agent*), so this was a hand review. It is named here because the pipeline did not do it, which is the standing condition in this repository and not a fact about this batch.

**Twenty-one findings: nine blocking, three wrong month names, five errors the next-phase prompt had inherited, four minor. All twenty-one are closed.** The batch was not restarted, no scene was replaced, no card was dropped, and the planned plot of all ten chapters is unchanged. The full record is in `state/continuity.md` under *The Batch 0004 review pass — independent, and what it changed*.

---

## The one thing to read before drafting Chapters 139–147

**The batch had a day-arithmetic fault running through it, and the fault had been copied into the state files and into `batch-0005/PROMPT.md`. That second half is the expensive half.** Findings 1, 2, 4, 5 and 8 are all cases where a number in the prose was written into `continuity.md` or into the next prompt and would have been read as fact by Batch 0005. A writer who trusts a state file is trusting a document that was written from prose rather than checked against a clock.

**The repair is a rule, and it is now on the face of three chapters, of the continuity file and of the next prompt:**

> **The plateau road is four days up and four days down. A man is four shillings a day. A whole hire is thirty-two shillings, entered four on the day he is hired and twenty-eight when he is paid off. A man hired on day X and out on day X is back in the fen on day X plus eight. There is no other form.**

Batch 0004's three hires obey it and are the worked examples: **hired on the fourth and out on the fifth; hired on the ninth, out on the ninth, paid off on the seventeenth; hired on the twelfth, out on the twelfth, at a windlass on the sixteenth and in the fen on the twentieth.**

## The three structural repairs, and why the carrier had to change

The ninth, the tenth, the eleventh, the fourteenth and the twentieth were all fixed by the cards and by a four-day road, and together they were not satisfiable. **A question sent on the ninth cannot be answered on the fourteenth. Not by a hired man, and not by anybody.** The batch's own sentence about a question that travels four days each way being *a thing sent to arrive after the answer* was already on the page in Ch 134; the repair completes it.

1. **The four lines came down on a rider the occupier hired at her own cost, not on the man this fen hired.** They were written on the tenth, on the back of her own reading, before anything was signed, and she sent them down that afternoon: four days one way puts them in this fen on the fourteenth. **The fen's man was on the road from the ninth to the seventeenth with a question in his satchel that four houses had answered on the tenth without him, and his twenty-eight shillings stand in the ledger undischarged.** Ch 136 now says on the page that this body did not pay for the second half of that conversation, does not know what it cost, did not ask, **and the reason it did not ask is that the fen was afraid of the figure.** No date was moved and no card was rewritten. **This body spent thirty-two shillings on a road and was beaten home by a household's own expense, which is the batch's own argument about fear and four places and not a patch on a date.**
2. **The growth came up on the sixteenth and not on the eighteenth, and the figure on the households' sheet is six days and not eight.** A sheet written on a shelf four hundred miles off on the eighteenth cannot be in this yard on the twentieth. Two days was the only degree of freedom and it is the one that had to give. **The drafted line *found out four days afterwards*, which the review read as a slip, is now correct rather than wrong, and it is why the sixteenth is the right day and not merely a permitted one.**
3. **The man who comes down the road in Ch 138 is hired on the twelfth.** The card hired him on the eighteenth and had him in the fen two days later, and the draft's own repair to the sixteenth was also impossible, because a man cannot be hired on the day a licensed man writes the page that goes into his satchel. He is at a windlass on the sixteenth — the day the green came up, and the day the occupier put four lines and a figure into his satchel herself — and in this fen at the seventh hour of the evening of the twentieth.

## The other blocking findings, in one line each

- **The seventh column was twenty-six on the fourteenth, not twenty-seven.** The twenty-seventh reading is made on the sixteenth in Ch 137. All four places in Ch 136 are corrected, and the reader now says on the page that the next one is not read because this body reads a door on a day it has appointed and had appointed none. **That clause is the batch's own practice made explicit and it is why the fourteenth and the sixteenth do not collide.**
- **The trestle reading was produced two days earlier, not four.**
- **The office at the foot of the plateau is nine miles and a day's cart, not the four-day road.** Ch 130 already had a records officer walking it in a day; Ch 136 had a cart calling it four days each way.
- **The hired man's dates were mutually exclusive across three chapters** — engaged on the ninth in Ch 133, hired on the tenth in Chs 134 and 136 — and are now the ninth throughout, with the whole order of the days entered at the bench: a day into the road by the tenth, at a windlass on the thirteenth, paid off on the seventeenth.
- **Ch 133's rule was made six days before it was described, not nine.** The rule is of the second; the eighth is the sixth.

## The wrong month names, which violate the batch's own table

- **Ch 129** had the flock going up the fen road on the tenth of a month *seven* months back. Day 10 is the first month and is **eight** months back. The *twenty-seventh of a month three months back* in the same sentence was already right, which is how the table was known to have been in hand.
- **Chs 136 and 137** had the trestle reading on the seventeenth of a month *four* months back. That day is 167 and 151–180 is **three** months back. Ch 132 already had the neighbouring date right.

## What the next-phase prompt had inherited, all five repaired

`batch-0005/PROMPT.md` said the volume's question was asked *on the seventeenth of last month* (it was the twentieth of the eighth, Ch 138); gave days 164, 166 and 170 as *a month four months back* against its own two naming tables, which say three; put the growth at day 228 and *last month* for Chapters 139–143, where day 226 is *of this month*; said *twenty-seven on the sixteenth of last month* in a column governed by the day-231 frame; and pointed the writer at *the two naming tables* in the Batch 0004 section of `continuity.md`, which holds one. **The pointer is corrected to *the dating table and the day clock* and the prompt's own two tables are named as the ones that govern its prose.** The stray day number in the beat's row is removed — see below.

## Two things the review did not find, recorded so they are not re-litigated

- **The beat's log day is inconsistent between two batches and has been left inconsistent on purpose.** Batch 0003's table gives day 171; Ch 138 of this batch names the same log *the twenty-first of last month*, which in this batch's frame is day 201. **Neither figure was changed, because correcting either reopens a reviewed and closed batch and the alternative is a fresh contradiction on the page.** It is flagged in `continuity.md`, in `open-threads.md` and in the next prompt, and Batch 0005 is told not to restate that day in prose and not to add an interval to the column.
- **Batch 0003's hired man is also internally inconsistent** — hired on the twelfth, paid off on the sixteenth, and on the page on the seventeenth, against an eight-day hire on a four-day road. It is inherited, it is in two closed batches, and it was not raised by this review. **It is the same defect as this batch's and the reason this batch's rule is now written down rather than left to be re-derived.**

## What held, and is recorded so that a later pass does not spend it again

- **Length.** 29,333 words by `wc -w` over the chapter files including their headings, range 2,781–3,120, inside both bands. **The review forced 164 words into a batch whose two chapters were already at the ceiling, and the trimming that paid for it removed restatement and not scene.** Ch 136 is at 3,119 and Ch 138 at 3,120.
- **Mechanics, re-run after the pass.** Quotation marks even in all ten files; **zero non-ASCII glyphs and zero em dashes**; no month named in narration or in any document; the only capitalized *March* is *the March's tin*; the word *seat* absent; no Brinewake, no Continuity Office, no Crown Engine, no Iona Vey, no Thornwild, no Kellan Rusk; no British spellings.
- **Duplicates.** A scan run after the pass, with the emphasis marks stripped, returns **four duplicate sentences of ten words or more in three places, and all four are standing texts of this manuscript**: the class definition in Chs 132 and 137, *Not one hundredweight of anything has ever come back to this holding* twice in Ch 129, and *a hundred and forty-one trees of bearing left standing and the grass under them cut twice a year* twice in Ch 134. **Separately, the three clerk's four-word observations in Chs 132, 133 and 137 share a formula and are each never explained.** No pass should strip any of them.
- **Arithmetic.** Unchanged and re-checked: 402cwt at 4s is eighty pounds eight; 452cwt is ninety pounds eight; 109cwt at 9s is forty-nine pounds one shilling; 16 × 28 pails is 448, which is twenty-two pounds four, and 448 taken thirty days over seven is 1,920 shillings, which is ninety-six pounds, which is worse than eighty pounds eight; nine feet less five feet two inches is three feet ten inches, which is three and a half feet and four inches.
- **All sixteen locks respected.** One draw only, the fieldbook unopened, the leak measured once with no cause and no interval, the man at the second house absent and not looked for, Sabin Roell correct and obstructive to nobody, the rows decided by their owners and not called a lesson, no panel spent, nobody thanked.
- **Craft, which the review recorded as landing and did not touch.** The man of about fifty's *we are spreading a rumour of a record and the reason is fear*; Renner's coat that no office can list and a man can lose; the four places being two buildings, a counter and two men; Lissa Vale's fourth-wall question; the twenty-seven counted by a stranger from outside. **The repair added one beat to that list and altered none of the others.**

## A note on the four-line repair, for a writer who thinks it is a convenience

It is the opposite. **Before the repair, the fen's man brought the four lines home and the reader never learned that four households had sent their own answer down a road at their own expense, which meant the batch's cost — thirty-two shillings and a hired man for nothing — was a bookkeeping line instead of an argument.** After it, the thirty-two shillings are the argument, and the sentence the batch already contained about not paying for the second half of that conversation has something to be true about. **A repair that makes an existing sentence mean more is a repair, and a repair that only moves a number is a patch. This one is the first kind.**
