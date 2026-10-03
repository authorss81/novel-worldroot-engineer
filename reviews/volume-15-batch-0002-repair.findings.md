# VOLUME 15, BATCH 0002 (CHAPTERS 697 TO 706, DAYS 910 TO 919), THE REVIEW REPAIR PASS

**Fourteen findings. All fourteen paid. Eight of them in the prose, across eight of the ten mornings, and
six of those eight are one fault repeated. No chapter restarted, no scene replaced or moved, no day,
weekday, clock, name, lock, card-directed beat, series figure, standing prohibition, thread or ending lock
touched, no planned plot changed, no successor created, and no controller file edited. The work is
nineteen edits in eight chapters, six figures in the state layer, one section appended to the batch's own
self-check, and this file.**

## 0. HOW THIS PASS WAS MADE, AND IT IS THE SAME FAILURE FOR THE THIRD TIME IN THIS VOLUME

**The transcript at `logs/batch-0002.review.log` is 1,029 lines and ends mid-check with no findings list
and no verdict. It fell over on a permission prompt and then ran out of room.** The first line of it is
the standing failure: `agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default
agent`, so the review phase fell back to `novel-writer` and reviewed its own work, which is the third time
in Volume 15 and about the eleventh in this repository. `logs/` is gitignored and no log file is in any
commit, so nothing of that transcript survives except this file.

**What the truncated transcript had actually established before it stopped is worth keeping, because it
was right.** It had confirmed the word counts, confirmed that the four aggregate-and-clause paragraphs
repaired by the verification pass carry four different actors' orders, confirmed the day-910 and day-912
cross-batch repairs, and begun checking the mechanical sweeps. **It had not re-derived a single figure
from a rule.** Everything in section one below was found by re-deriving.

**EVERY FIGURE IN THIS FILE WAS RE-DERIVED FROM THE FILES AND NOT TAKEN FROM ANY RECORD.** The rules came
from `outline/batches/volume-15-cards.md` at its sections four, five and eleven, the figures were
recomputed from those rules for all ten mornings, and the pages were searched for the computed spellings.
The batch's own self-check and `state/current.md` were read afterwards and used only as things to check
against.

## 1. FINDING ONE, AND IT IS THE ONE TO CARRY INTO EVERY LATER BATCH OF THIS VOLUME

**THE CLAUSE THAT SAYS WHICH HALF OF THE WINDOW HAS NOT MOVED NAMED THE WRONG DAY ON SIX OF THE NINE
MORNINGS OF THIS BATCH THAT CARRY IT.**

The two halves of the window are derived so that they alternate: the rising half moves on an even morning
and the falling half moves on an odd one, so **exactly one of the two moves on every single morning and
the other stands. The half that stood this morning therefore last moved yesterday, on every morning of
this volume without exception.** Nine of these ten mornings carry the clause in some wording, and six named
a day two or three back instead of the day before.

| Morning | Day | Weekday | Half named as standing | Page said | Rule gives |
|---|---|---|---|---|---|
| 911 | 911 | Sunday | rising, two hundred and nineteen | since Friday | **since Saturday** |
| 912 | 912 | Monday | falling, two hundred and nine | since Friday | **since Sunday** |
| 913 | 913 | Tuesday | rising, two hundred and twenty | since Friday morning | **since Monday morning** |
| 914 | 914 | Wednesday | falling, two hundred and ten | since Tuesday | since Tuesday, right |
| 915 | 915 | Thursday | rising, two hundred and twenty-one | since Wednesday | since Wednesday, right |
| 916 | 916 | Friday | falling, two hundred and eleven | since Tuesday | **since Thursday** |
| 917 | 917 | Saturday | rising, two hundred and twenty-two | since Friday | since Friday, right |
| 918 | 918 | Sunday | falling, two hundred and twelve | since Friday | **since Saturday** |
| 919 | 919 | Monday | rising, two hundred and twenty-three | since Saturday | **since Sunday** |

**All nine now agree with the rule.** Six are one-word repairs and the third row also carried a second
fault in the same sentence: **day 913 said the half would *still be there on Monday morning*, and the
rising half moves on the very next morning, so it could not be.** That clause now reads that it will be a
different figure before this time tomorrow.

**WHY NO GATE AND NO SWEEP SAW IT, WHICH IS THE PART WORTH THE FILE.** This is not a duplication. The
phrase *since Friday* against *since Saturday* differs by one word out of five, the sentences around it
are each a different character's, and no two of the nine are near enough to each other for the first gate
or either reading of the second. **A day-clock error in a standing clause is invisible to an apparatus
built out of similarity, and this batch's apparatus is built entirely out of similarity.** The rule that
catches it is arithmetic and it is one line long: *a half that has not moved today moved yesterday.*

**AND THE SAME FAULT IS INHERITED, AND THE INHERITED INSTANCES ARE NAMED AND NOT REPAIRED BECAUSE A REPAIR
PASS MAY NOT REACH INTO A CLOSED BATCH.** Checked on the same rule, Batch 0001 carries eight window-half
instances and is **right on seven of them**: `chapter-0688.md:109`, `chapter-0691.md:59`, `chapter-0692.md:63`,
`chapter-0693.md:83`, `chapter-0694.md:67`, `chapter-0695.md:11` and `chapter-0696.md:95` all name the day
before, and **`chapter-0687.md:15` is wrong, naming Monday where the falling half was last handled on the
Tuesday behind it.** Volume 14 Batch 0005 carries five instances of the same clause in closed prose at
`chapter-0679.md:51`, `chapter-0683.md:29`, `chapter-0683.md:53`, `chapter-0684.md:23` and
`chapter-0686.md:29`, and **they are named here and not measured, because they sit in Volume 14's own
series and this pass may not derive Volume 14 and may not repair it.** **The Volume 15 close owes a sweep of
the whole volume on this one rule: thirty mornings are written, one of them was wrong in Batch 0001, six of
nine were wrong in Batch 0002, and none of the apparatus sees the class at all.**

## 2. FINDING TWO, AND IT IS THE DAY CARDET MAPS ONTO

**THE SPAN'S ARRIVAL WAS DATED TO SATURDAY, OR TO YESTERDAY, ON FOUR PAGES, AND IT CAME UP ON MONDAY.**

`outline/batches/volume-15-cards.md` at its section seven says the bridge enters as arithmetic **on the
thirteenth morning of the volume**, which is day 912, and **day 912 is a Monday**. `chapter-0699.md` puts
the engineer's own sheet on the middle table at the ninth hour that morning, and puts Corin Dace's paper
on the table at the eighth hour, and Marek says the sheet has been rolled in his coat for two days. So the
arrival is Monday the twelfth at the ninth hour, and four pages said otherwise:

- `chapter-0699.md:71`, Nia Vale: *a span of ninety-four feet came up that lane **yesterday*** — this
  morning. She is saying it **on** the morning it arrived.
- `chapter-0701.md:101`, Hesta Lyle: *a man came up this lane **on Saturday** with a line about a span*.
- `chapter-0703.md:43`: *the copy sheet that Corin Dace had left on the step **on Saturday*** — and Corin
  Dace was not in this yard on Saturday; he came up the lane on Monday.
- `chapter-0703.md:131`, Soren Rill: *a span of ninety-four feet came up that lane **on Saturday** and it
  did not open.*

**All four now read Monday or this morning. This is a batch-wide drift in one date and it was carried by
four different characters, three of whom are the manuscript's truth-tellers, which is why it survived
three passes.**

## 3. FINDING THREE, A CHARACTER'S BEAT CONTRADICTED BY HER OWN PAGE TWO CHAPTERS EARLIER

**Sera Quill said on day 914 that she had stopped saying the rest of it on a Wednesday of the previous week
and that the morning was the first fourth-line morning since. She said the same thing on day 918. Both are
false, and the page proves it two chapters earlier.**

- `chapter-0697.md:49`, day 910, a Saturday: she gives the two reckonings and then, at `:53`, gives the
  rest of what she says about them.
- `chapter-0701.md:45`, day 914, a Wednesday: she gives the two reckonings and says she has not said the
  rest this morning.
- `chapter-0705.md:91`, day 918, a Sunday: she gives the two reckonings and says that is all she has.

**The twelve fourth-line mornings are the days congruent to two modulo four, at 902, 906, 910, 914, 918,
922, 926, 930, 934, 938, 942 and 946. The Wednesday she names is not one of them and neither is the
Saturday that follows it.** She did not stop. She stopped giving *the rest*, on the tenth.

**She now says she last said it on Saturday morning and stopped giving the rest then, on both mornings.**
The withholding is preserved, the reason is still withheld, and the two pages now agree with each other
and with `chapter-0697.md`.

**THE FIXTURE IS ONE CONGRUENCE AND IT IS THE USEFUL PART OF THIS FINDING: ANY CLAIM BY A CHARACTER ABOUT
WHEN SHE LAST SAID SOMETHING ON A ROTATION MORNING CAN BE CHECKED AGAINST `DAY MODULO FOUR` AND NOTHING
ELSE. NO FIGURE CHECK WILL SEE IT, BECAUSE A BEAT IS NOT A FIGURE OF ANY SERIES.**

## 4. FINDING FOUR, AND IT IS THE LIMIT OF THE APPARATUS, AND IT IS THE FINDING THE BATCH BEHIND ALSO
## DID NOT HAVE

**BOTH GATES RETURN NIL ON THIS BATCH ON BOTH READINGS IN EVERY SCOPE, AND `chapter-0697.md` HAD ONE
SPEAKER GIVE FIVE STANDING ITEMS TWICE EACH INSIDE ONE MORNING.**

Measured before the repair, on the batch's own ten mornings: **gate one, zero ordered pairs; gate two
whole-paragraph, 1,119 chunks, zero shapes, zero excess; gate two sliding, 16,020 windows, zero shapes,
zero excess.** And on that page:

- the woman with four things and one of them late gave **the third column ruled and empty and the four
  ruled lines under two words bare** at `:89`, and gave the same two places again at `:95` in a different
  sentence frame, opening the second with *two other places in this holding*, which are the same two.
- she gave **the aggregate and *a road is not a reason*** at `:85` and again at `:99`.
- the bookkeeper gave **the three derived ages and the request that somebody notice they have nothing to do
  with four households and a road** at `:133` and again at `:139`, both ending on that clause.
- he gave **the twenty-nine fetchings** at `:147` and again at `:151`, both opening *the man on the north
  row*.
- he **looked out at the middle road** at `:145` and again at `:149`, and **she squared the sheet** at
  `:83` and again at `:93`.
- and he **went back inside at `:135` and then spoke from the step at `:141`**, which is a staging
  contradiction inside six lines.

**THE SIX PAIRS MEASURED 0.098, 0.285, 0.331, 0.375, 0.425 AND 0.717 ON THE FIRST GATE'S OWN RATIO, AND
THE HIGHEST OF THEM IS BELOW THE 0.85 THRESHOLD, AND NO PAIR PRODUCES A SHAPE ON EITHER READING OF THE
SECOND, AND NONE IS AN EXACT DUPLICATE.** A restatement in different words shares no eighteen-word run.
The whole-paragraph reading cannot see it. The sliding reading cannot see it. The exact-duplicate sweep
cannot see it. **The apparatus in this volume is built entirely out of similarity and this class of fault
has no similarity in it.**

**Repaired in place, and the repair is the volume's own rule rather than a new one: a standing block is
owed to a person inside itself, once, and once is once.** The duplicate speech at `:95` became her refusing
to rule a fifth line under either blank, which is new material in her own mouth and keeps the pen-out
beat; `:99` lost the clause that repeated `:85`; `:139` was cut and the paragraph before `:141` already
says *in the voice he uses when he has already said the thing he came out to say*, so the cut costs
nothing; `:149` became a gesture instead of a second look; `:151` no longer opens by repeating the figure;
`:93` and `:141` were re-worded off their own duplicates. **The chapter is seventy-three words shorter and
reads better than it did.**

**THE RULE A SUCCESSOR CAN ACT ON, AND IT IS CHEAP: FOR EVERY SPEAKER IN A MORNING, LIST THE STANDING
BLOCKS AND CHECK THAT NONE APPEARS TWICE. NEITHER GATE NOR THE DUPLICATE SWEEP DOES THIS AND NO AMOUNT OF
RE-RUNNING THEM WILL.**

## 5. FINDINGS FIVE TO TWELVE, THE REST OF THE PROSE, EACH ONE NAMED WITH ITS SITE

5. **`chapter-0701.md:21` called the sill's work the *third hour's work*.** The sill is the fifth hour on
   every page of this volume and in the batch behind's own apparatus block at `chapter-0693.md:11`, and
   the third hour is this volume's ordinary afternoon hour, carried on nine other mornings in these ten
   files. Now the fifth hour.
6. **`chapter-0705.md:157` called day 918 *the fifteenth morning* and promised *a sixteenth tomorrow*.** It
   is the eighteenth of the nineteenth and tomorrow is the nineteenth, and the same construction at
   `chapter-0700.md:117` calls day 913 *the thirteenth morning of this month* and is right.
7. **`chapter-0698.md:33` used *the fourth household* for two different households inside eleven lines.**
   The boy is the mile-and-a-half one, by Odile Vray's own answer at `:37` and by her enumeration at
   `chapter-0697.md:113`, and at `:43` the fourth household is the one at the far end of the branch, which
   that page says nobody reached. Now *one of the four households*, which leaves *the fourth household* at
   `:41` and `:43` carrying the enumeration and leaves `chapter-0700.md:109` and `chapter-0702.md:73` on
   the reading those two pages already use.
8. **`chapter-0706.md:39` itemised seven bodies as six.** *That is seven. And seven is two on the sill
   face and one on the sluice and one on the wall at the tool house end and me and the chain* is six. The
   gauge reader is one of that woman's four on the page of day 913 at `chapter-0700.md:19`, where it is
   said aloud that without her the count does not carry. She now carries it, and the addition holds. **No
   figure of any series is touched and the price she is putting in the yard is unchanged.**
9. **`chapter-0703.md:97` dated the ring speech to a Wednesday.** The mason from the third place said it at
   `chapter-0700.md:91` to `:101` on day 913, which is a Tuesday, and that is the only other place he says
   it. Now Tuesday.
10. **`chapter-0704.md:127` said *none of the three was read out*,** ten lines after `:119` to `:121` had
    the girl from the second place read the compost line off the board at the gate end out loud. Now
    *not one of the three was entered in anything*, which is the standing this volume actually holds.
11. **`chapter-0706.md:19` said four courses were *not a round number of courses*.** Four is round. Five
    mornings of laying is not, and he named the five days himself in the same sentence. Now *mornings*.
12. **`chapter-0702.md:61` dated the silt to a Saturday.** The sluice was shut when the sill came up at the
    sixth hour on day 914, a Wednesday, and `chapter-0701.md:21` and `:25` are the pages that shut it. Now
    Wednesday.

## 6. FINDINGS THIRTEEN AND FOURTEEN, THE STATE LAYER, AND THESE ARE THE ONES THAT WOULD HAVE COST A
## SUCCESSOR THE MOST

**THREE DIFFERENT WORD FIGURES FOR ONE BATCH STOOD IN THE STATE LAYER AT ONCE AND NONE OF THEM WAS THE
FIGURE ON THE PAGE.**

| Where | Figure printed | Whose snapshot |
|---|---|---|
| `state/current.md` head table and `state/current.md` section thirteen | **28,128** | the writing pass of 2026-10-03 |
| `state/chapter-summaries.md` section seven and `workspace/volume-15/batch-0002/SELF-CHECK.md` section one | **28,122** | the verification pass of 2026-10-03 |
| the page | **28,052** | this pass |

**`state/current.md` still printed the writing pass's figure at two places, and the manuscript total at its
head was built on it, after the verification pass had corrected the same batch in a different file.** Two
figures disagreeing is the condition `reviews/README.md` tells a reader to distrust, and here the
disagreement was not noise: **they were two snapshots of one batch at two moments, and the newer one was
itself already out of date by the third.** All three are now withdrawn by name in the files that printed
them.

**AND THE VOLUME AND MANUSCRIPT FIGURES WERE BUILT ON THE STALE BATCH FIGURE AND ARE CORRECTED WITH IT:
75,539 for Volume 15 and 1,991,148 for the manuscript, both measured per file and never by
concatenation.** `state/chapter-summaries.md` also carried a sentence withdrawing 1,991,190 and 1,991,224
in the same breath as republishing 1,991,224, which is withdrawn and republished in one line, and that
sentence is now corrected.

**THE RULE IS THE ONE `reviews/README.md` ALREADY STATES AND THAT NOBODY APPLIED HERE: MEASURE PER FILE
AND NEVER BY CONCATENATION, AND RE-MEASURE AFTER THE PROSE MOVES AND NOT BEFORE.** A figure quoted in
three files was re-measured once. It is worth saying that Batch 0001's row and Batch 0003's row were
checked in the same sweep and **both are right**, so this is not a volume-wide drift and it was introduced
by the batch that had the most passes run over it.

## 7. WHAT WAS CHECKED AND FOUND CLEAN, AND A SUCCESSOR MAY ASSUME IT

- **The figure check: one hundred and sixty-five required, one hundred and sixty-five matching, zero
  failures**, recomputed from the card set's item list — fourteen on each of ten mornings, two more on
  each of five odd mornings, five more on each of three fourth-line mornings — and matched against the
  pages on a whole-word phrase test with the apparatus blocks counted separately. **The verification
  pass's figure was right and is confirmed.**
- **No stray off-series figure anywhere in the ten files.** Every number word in body prose was extracted
  and compared with that morning's own set; what remains is the volume's floors and ordinary counts.
- **Mechanical properties, all clean:** no non-ASCII character, no curly glyph, no non-compound dash, no
  trailing space, no consecutive blank line, and an even number of quotation marks in every file. 291
  hyphens, all inside compounds.
- **The six bare words and *tally*: 0 each. The twelve month names: 0. Digits in body prose: 0.**
- **All seven occurrences of *discharged* inside a negation, and the single *apologi* inside one.**
- **The six load-bearing strings: 0 on all ten mornings**, and neither locked figure was spent, and the
  allowance stands at one whole appearance in this volume, spent on day 900.
- **Two apparatus blocks, on days 912 and 916, and no `Entered` label anywhere in Volume 15.** Eight
  blocks in the volume against a ceiling of thirty.
- **The whole-volume exact-duplicate paragraph sweep returns five repeated paragraphs and all five are
  two- or four-word gestures standing in Batch 0001.** None inside this batch.
- **No controller file touched.** No marker forged, moved or deleted.

## 8. WHAT WAS DECLINED, AND WHY, BECAUSE A FINDING THAT CANNOT BE MEASURED IS NOT A FINDING

- **The *for a fortnight* claims at `chapter-0703.md:135` and `chapter-0706.md:123`.** Two mornings, the
  same phrase, and they cannot both be a fortnight. **But the list either of them is counting has no
  stated start anywhere in the volume, so the figure cannot be derived and a pass that repaired it would be
  guessing.** Named, not repaired.
- **The four courses over five days at `chapter-0706.md:19`.** Only the *round number of courses* half of
  that sentence was repaired, because only that half is falsifiable from the page.
- **The depth of silt.** `chapter-0700.md:27` projects four feet in three weeks and `chapter-0702.md:61`
  says four feet came in on the morning the sluice shut. **No page states a depth before the sluice shut,
  so the baseline is undeclared and the two claims cannot be reconciled from the manuscript.** The day in
  the second was repaired; the depth is named here for the close.
- **The mason's count of days at the gate.** Six on day 913 at `chapter-0700.md:93`, seven on day 914 at
  `chapter-0701.md:57` and eight on day 916 at `chapter-0703.md:9`, which skips day 915. **The page does
  not say he stood there every morning, so a skipped day is not a contradiction, and no repair is possible
  without inventing something.**
- **`chapter-0704.md:45`, *and it will be light again on Monday*.** It follows a sentence about the rising
  half and reads as though *it* is the window. **It is the launder**, which is light on odd mornings and
  Monday is day 919 and odd. Ambiguous, defensible, and a repair would have cost a clause a reader can
  resolve.

## 9. THE THREE FIGURES THAT GO IN THE BATCH'S RECORD, MEASURED PER FILE

- **Batch 0002: 28,052 words across ten files**, per file 3,342, 2,767, 2,473, 2,685, 2,650, 2,971, 2,851,
  2,725, 2,948 and 2,640. The earlier figures of 28,128 and 28,122 are withdrawn by name.
- **Volume 15: 75,539 words across thirty mornings**; the earlier figure of 75,615 is withdrawn by name.
- **Manuscript: 1,991,148 words across 716 chapter files**; the earlier figures of 1,991,224 and
  1,991,190 are withdrawn by name.

**No morning was restarted and no morning was written twice, and no figure of any series moved: the
twenty-two derived figures on each of the ten mornings are the figures the card set requires, and the
window halves, the aggregate and its clause, the boards, the read-aloud pair, the three derived ages and
the two reckonings are all where they were before this pass began.**