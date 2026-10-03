# Volume 14 Close — Review-Fix Findings

**This pass read an independent review of the Volume 14 close, re-derived the figures the repair rests
on, corrected seven state-layer and handoff defects, recorded two controller faults it may not touch,
wrote no prose, altered no morning of the forty-nine, closed none of the thirty-five, and moved no
figure of any series. The manuscript is unchanged at 1,915,609 words across 686 chapter files.**

**The reviewed phase is `workspace/volume-14/close/`, its record is `reviews/volume-14-close.findings.md`,
and its lock is the final section of `outline/ending.md`. The review is at `logs/close.review.log`.**

---

## 1. WHAT THIS PASS WAS AND WAS NOT ALLOWED TO DO

**It was a repair pass over a close, and a close wrote no prose, so there was no prose to preserve and
nothing to restart.** The forty-nine mornings of Volume 14 are closed prose and were not opened. **No
chapter file was read for editing, none was edited, and no batch was resumed or begun.** The planned
plot is untouched: Volume 15's central pressure, its major turn, its climax, its resolution and its
next question are fixed at `outline/series.md` and `outline/ending.md` and this pass moved none of
them and had no standing to.

**Markers, scripts, workflows and agent files are controller-owned and were not touched.** No `.done`,
no `.retired`, no `.blocked` and no `.attempts` file was created, moved or deleted anywhere in
`workspace/`. No file under `scripts/`, `.github/workflows/` or `.opencode/agent/` was edited, and no
dispatch, phase-selection, timeout, retry or checkpoint behaviour was altered. `state/phase-ledger.json`
was read once and not written.

---

## 2. WHAT WAS RE-DERIVED BEFORE ANYTHING WAS CHANGED

**Every measurement below was recomputed from the chapter files in this pass and not taken from the
review or from the close.** The close's arithmetic is sound and reproduces to the word.

| | measured now | agrees with the close |
|---|---|---|
| chapter files | 686 | yes |
| manuscript, per file with `len(text.split())` | 1,915,609 | yes |
| manuscript, concatenated | 1,915,598, residual of 11 | yes |
| files lacking an EOF newline | 12, of which 9 are Batch 0005 | yes |
| Volume 14 | 116,146 across 49 | yes |
| Volume 13 | 91,321 across 49 | yes |
| `batch-0005` | 24,440 across 9: 2,771 / 2,320 / 2,096 / 2,919 / 2,482 / 2,300 / 2,653 / 2,961 / 3,938 | yes |
| *far end of a thing* inside Volume 14 | 6 | yes |
| the far-end sentence spoken whole | 5 mornings, 851, 887, 891, 894, 899 | yes |
| the comfort line spoken whole | 5 mornings, 851, 884, 893, 896, 899 | yes |
| *Aldren*, case-insensitive, inside Volume 14 | 1 morning, `chapter-0655.md` | yes |
| *Iona Vey* inside Volume 14 | 1 morning, `chapter-0686.md` | yes |
| *hundredweight* inside Volume 14 | 53, a separate word in every one | yes |
| day 899 | Tuesday, the twenty-ninth of the eighteenth | yes |

**The clock was then run forward across the boundary, because one of the defects is a clock defect.**
Day 900 is a Wednesday and the thirtieth of the eighteenth; the turn to the nineteenth is day 901; the
turn to the twentieth is day 931; and day 900 is the first morning of Volume 15, so **day 931 is its
thirty-second morning.** Every morning heading from `chapter-0638.md` to `chapter-0686.md` was
checked against the standing rule and all forty-nine agree.

**AND THE SIX IN-BETWEEN FIGURES WERE COUNTED MORNING BY MORNING RATHER THAN ACCEPTED, BECAUSE THE
REPAIR BELOW RESTS ON THAT COUNT.** The far-end sentence was in between on 887, 891 and 894 and the
comfort line on 884, 893 and 896. **That is six, three of each, and four of the six fell in the closing
batch alone.**

---

## 3. THE SEVEN DEFECTS REPAIRED

### ONE, AND IT WAS THE ONLY ONE THAT COULD HAVE CHANGED WHAT A SUCCESSOR WRITES

**`state/current.md` ended its paragraph on the sheets by handing the four forward as *entered and
none refused*, which is the opposite of the two lines above it and the opposite of the page.**

The paragraph two lines above says *none of the four has been entered, none refused and no column cut
under any of them*. `chapter-0686.md` line 161 says, in Nia Vale's own mouth: **"Not one of the four
entered, not one refused, and no column cut under any of them in this holding's book."** The close had
repaired the first of those two clauses and then written the opposite claim into the handoff sentence,
so the file said both things inside three lines and the handoff carried the wrong one.

**It now reads that a successor inherits the four as NONE ENTERED AND NONE REFUSED, with the page
quoted beside it and the reason stated: a handoff that inverts a count is the one defect in this layer
that a successor cannot detect on its own, because it arrives agreeing with the shape of the sentence
it replaced.** No figure moved and no morning was touched.

### TWO, THE STATED BUDGETS OF THREE OF THE FOUR FILES, AND THE SIZE OF THE LAYER

Measured with `len(text.split())` on each file alone, before this pass edited anything:

| file | it claimed | it was | out by |
|---|---|---|---|
| `state/current.md` | about three thousand four hundred | 4,639 | about 1,200 |
| `state/continuity.md` | about two thousand eight hundred | 3,310 | about 500 |
| `state/chapter-summaries.md` | about one thousand seven hundred | 2,390 | about 700 |
| `state/continuity.md`, on the layer | about eleven thousand together | 13,202 | over 2,000 |

**A budget line that understates its own file by a thousand words is not a rounding error, it is a
figure a later pass inherits as a rule, and this layer's own head promises that nothing in it is an
append-only residue.** All four now print a measured figure rounded to the nearest hundred, the method
beside it, the date, and the statement that the figure moves with every edit and is therefore a
measurement and not a promise. **Each was measured again after its own edit was written, so none of
them is a figure that its own correction moved.**

### THREE, THREE COUNTS THAT A SUCCESSOR WOULD HAVE READ AS RULES

- **The close's named open items are eleven and the layer called them nine.**
  `reviews/volume-14-close.findings.md` section 7 is numbered one to eleven and the layer's pointer to
  it now says eleven, numbered one to eleven. **The count was wrong in the pointer and not in the
  list, which is the worst place for a count to be wrong, because the pointer is what a reader trusts.**
- **The heading that said the close's findings held TWO items a Volume 15 writer is most likely to walk
  into then listed three.** It now says three, and it names the count in the sentence rather than
  leaving a reader to count the list.
- **`state/continuity.md` said the close added six findings of its own and repaired none of the six,
  and then enumerated four of them as items fifteen to eighteen.** It now says four and names the range,
  so the claim is checkable inside the file that makes it.

### FOUR, AND FOUR PLACES, THE IN-BETWEEN LOCKED FIGURES WERE LABELLED FOUR WHERE THE VOLUME SPENT SIX

**Four is the closing batch's count. The volume's count is six, three of each, and a handoff that
prints four has silently dropped two mornings of the volume behind it.** The allowance resets per
volume and no remainder crosses the boundary, so nothing downstream is arithmetically harmed — but an
allowance section built on four would be built on two mornings that are not there, which is exactly the
class of fault the close spent its whole length hunting.

Corrected in four places, and the days are now printed beside the number in each: the closing sentence
of `reviews/volume-14-close.findings.md` section 9, the four-things paragraph at the foot of
`state/chapter-summaries.md` section 5, decision-queue item ten in `state/open-threads.md`, and sections
5 and 7 of the successor's prompt. **Where a count of four was correct — the closing batch's own count
in `state/chapter-summaries.md` section 4 and `state/open-threads.md` — it was kept and labelled as the
batch's, with the volume's six added beside it so that neither reader can take it for the other.**

### FIVE, THE ORDINAL IN THE SUCCESSOR'S CALENDAR

**`workspace/volume-15/outline/PROMPT.md` said the turn to the twentieth falls on day 931, being the
thirtieth morning of your volume. Day 900 is your first morning, so day 931 is your thirty-second:
931 − 900 + 1 = 32, and the printed figure was two short.** Both turn days were right and the companion
claim that day 901 is the second morning was right; only the ordinal was wrong. It is corrected, and
the correction carries the generalisation, because an off-by-one on a day clock is an off-by-one on
every figure built on it: **count the days and then add one, because a morning is a day and not a
difference, and never derive an ordinal by subtracting two mornings and reading the result as a
count.** The turn days themselves were re-run against the standing rule and stand.

### SIX, THE DIRECTORY NAME

**The close created the Volume 15 plan phase at `workspace/volume-15/plan/`, and `plan/` is this tree's
name for the card-set phase, being Volume 14's.** Volumes 11, 13 and 14 all called a volume-plan phase
`outline/`. The close gave its own successor a name that already meant something else, and the successor
prompt then compounded it by naming its own successor `plan-cards/`, a third name for a second thing.

**The directory was moved to `workspace/volume-15/outline/`, the successor is pointed at
`workspace/volume-15/plan/PROMPT.md`, and `plan` sorts after `outline`, so the ordering the prompt
requires is satisfied by the names themselves.** No word of the prompt and no figure in it changed; the
one path reference inside it was corrected, and two paragraphs were added at its section 9 naming
its own directory and the reason for the move. The two path references outside it — in
`state/current.md` section 8 and at `reviews/volume-14-close.findings.md` section 9 — were corrected
with the reason beside them, because a record that points at a path which no longer exists is worse than
a record that points at the right one. **`workspace/volume-14/close/PROMPT.md` also names the old path
and was deliberately left alone: a completed phase's prompt is a record of what that writer was told,
and the correction lives in the state layer and in the successor.**

### SEVEN, THE SUCCESSOR PROMPT'S ACCOUNT OF THE CONTROLLER

**The successor prompt recorded the Volume 14 planning phase as untidy. It is blocking, and the
successor is the phase that would have walked into it.** It now carries the ordering consequence in
full: the selector takes the first unmarked prompt in sorted order, that phase sorts ahead of the
Volume 15 plan, and a run of it would try to rewrite `outline/batches/volume-14-cards.md`, which is a
completed phase's output. **It also carries the rule for what to do if it ever is run: add nothing,
name the collision on the page, and stop.**

---

## 4. THE TWO FAULTS THIS PASS RECORDED AND DID NOT TOUCH

**Markers are controller-owned. No writing or planning phase may forge, move or delete one, and this
repository has never cleared a stale phase by touching a marker. Nothing was touched here either.**

1. **`workspace/volume-14/close/` carried no completion marker when this pass began, and so the
   selector would have run the close again instead of Volume 15.** **This one resolves itself and needs
   no operator action:** the control plane writes the marker at the end of its own run, after the fix
   pass, and the absence at the moment of review is the normal state of a phase mid-run. It is recorded
   so that nobody reads it as a fault.
2. **`workspace/volume-14/plan/` cannot retire itself and does not resolve itself.** A script prepended
   a scope header to its prompt, so the retirement guard, which tests the first line for the words
   *outline* and *phase*, cannot match, and the header is re-prepended on every invocation. Its output
   is on disk and complete, it has no `.done` and no `.retired`, and it sorts ahead of the Volume 15
   plan. **The fix belongs to the control plane — a marker, or the guard, or the header — and none of
   those three is a file a writing phase may edit.** It is now recorded at `state/open-threads.md`
   section four item six and at `state/current.md` section eight, with the ordering consequence stated
   rather than the tidiness.

---

## 5. WHAT WAS VERIFIED AND NEEDED NO CHANGE

**The review's praise was tested rather than repeated, and these held exactly.** The 686 files, the
1,915,609 per-file total, the 1,915,598 concatenation and the eleven-word residual, the twelve files
without an EOF newline, Volume 13 unchanged at 91,321, and `batch-0005` at 24,440 with all nine per-file
figures. The six occurrences of *far end of a thing* and its one escape at `chapter-0674.md` line 121.
The far-end sentence and the comfort line whole on five mornings each. *Aldren* once and *Iona Vey*
once inside Volume 14. The fifty-three spaced *hundredweight*s. **No chapter file was altered by the
close, and the close correctly overrode a wrong instruction in its own prompt.** The close's gate
figures, its day-table comparison and its 796-figure check were not recomputed here, because this pass
changed no prose and recomputing them would produce a second number under a name that already has one;
they stand as the close published them and as the review confirmed them.

---

## 6. THE ONE-LINE VERSION

**An independent review of the Volume 14 close raised nine findings; seven were repaired here and two
were recorded because they belong to the control plane.** The worst of the seven was a handoff sentence
that inverted the count of the four sheets on the long table, and it is now the page's own words. Three
stated budgets were short by five hundred to twelve hundred words each and are now measured figures
with their method. Three counts were wrong where a successor reads them as rules: eleven open items
called nine, three likely-written-into items headed two, and four close findings called six. The
volume behind spent six in-between locked figures and four places called it four. Day 931 was called the
thirtieth morning of Volume 15 and is the thirty-second. The successor's directory collided with a name
this tree already used and was moved to the one it uses. **No morning was touched, no prose was
written, no figure of any series moved, no marker was forged, no script was edited, and the manuscript
stands at 1,915,609 words across 686 files.**

**Writer model used: opencode/space-bunny-free**
