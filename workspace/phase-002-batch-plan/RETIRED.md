# Retired: phase-002-batch-plan

This phase prompt is retired and must not be restored.

Both `workspace/phase-002-batch-plan/PROMPT.md` and `workspace/volume-01/batch-0001/PROMPT.md` were scaffolded in `5eed797` with the same instruction: write Chapters 1–10. The runner (`scripts/novel_runner.sh`) picks the first `PROMPT.md` in sorted order whose directory has no `.done`, so after one of them completed it would have dispatched the other and re-drafted the same ten chapters, overwriting the prose.

**Resolution:** the volume-scoped prompt is authoritative, because `AGENTS.md` establishes `workspace/<volume>/<batch>/PROMPT.md` as the convention the pipeline continues with. `workspace/phase-002-batch-plan/PROMPT.md` was deleted on 2026-09-25 during the phase-001-outline review fixes. The next prose phase is `workspace/volume-01/batch-0001`, and there is exactly one Chapter 1–10 prompt in the tree.

No planned plot changed. Chapters 1–10 are still written once, from `outline/batches/volume-01-batch-0001.md`.
