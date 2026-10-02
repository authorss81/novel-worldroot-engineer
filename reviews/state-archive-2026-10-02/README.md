# State Layer Archive, 2026-10-02

These are the four state files exactly as they stood on the morning of 2026-10-02,
before the compaction that answered the review at `logs/batch-0002.review.log`.

## Why they were moved and not deleted

Measured on disk before the compaction:

| file | words | approximate tokens |
|---|---|---|
| `state/current.md` | 149,623 | ~202k |
| `state/continuity.md` | 620,919 | ~840k |
| `state/open-threads.md` | 266,112 | ~360k |
| `state/chapter-summaries.md` | 351,358 | ~474k |
| **total** | **1,399,611** | **~1.89M** |

`AGENTS.md` says: *"Do not load the entire manuscript into every prompt. Use rolling
summaries and a volume index."* The layer had grown to roughly nine times a single
model context window and had therefore failed at the only job it has. Every block in
it was a verification log: gate methods, item enumerations, per-file measurements and
withdrawal notices, written in capitals and appended rather than replaced, so that
`state/current.md` carried two disagreeing copies of four figures and told the reader
to prefer the one on top.

`outline/volume-14.md` at section 12b already named this: *"The state layer's own
size, which is append-only and past any safe whole-file read, and the first phase
permitted to compact it is the one that builds an index."* This pass is that phase.

## What is here

`current.md`, `continuity.md`, `open-threads.md` and `chapter-summaries.md`, byte for
byte as they stood. Nothing in them is deleted or rewritten. Git history also holds
every one of them, and the commit that moved them is the compaction commit.

## What a later pass should take from them

Almost nothing as prose. They are a record of how the figures were derived and proved,
which is a review artefact and belongs here.

Two things in them are still live and were carried forward into the compacted files
rather than left behind:

1. **The numbered thirty-five open questions**, last enumerated in full as a table at
   day 713 inside the block headed for Volume 11. The compacted `state/open-threads.md`
   carries all thirty-five by name and number and points here for the standing detail.
2. **The withdrawn figures.** Four figures were printed once in a plan and then
   withdrawn, and they must not be reprinted in any form: an in-between allowance of
   five is three; six house-spelling sites are seven; a door read three times is a
   door carrying four statements; *a twelfth volume* is ten volumes counting the one
   now closed. This list is also in the compacted `state/current.md`.