# Review Findings: phase-001-outline

Source: `logs/phase-001-outline.review.log` (review of commit `5ab35b8`).
Fix pass applied: 2026-09-25, same phase. No chapter prose existed, and none was written or restarted. The planned plot was not changed — every fix below either corrects a contradiction, registers a term, or supplies a missing fact the outline already depended on.

## Applied

| # | Severity | Finding | Resolution |
|---|---|---|---|
| 1 | High | Two prompts both said "write Chapters 1–10"; the runner would have drafted the batch twice and overwritten the prose | `workspace/phase-002-batch-plan/PROMPT.md` deleted; retirement recorded in `workspace/phase-002-batch-plan/RETIRED.md`. `workspace/volume-01/batch-0001/PROMPT.md` is now the single, detailed next-phase prompt |
| 3 | Medium | `outline/volume-01.md:21` invented a third, unnamed woman — "Their mother" — when Lissa **is** Marek's mother | Corrected to "His mother". Added a family lock to `state/continuity.md` so a drafting writer cannot re-introduce her |
| 4 | Medium | `state/continuity.md` said the outlines were "pending for their dedicated phases" and, 20 lines later, "Approved" | Section rewritten as **Canon status**. The outlines are approved and governing; they are not prose until drafted |
| 5 | Medium | Chapter 10 card said "votes four things" then listed five | The bypass is now explicitly **not** a fifth vote. It enters the book as an unfunded plan when Dunmar rules on whether a plan is a filing. The count is exact and the Ch 24–27 / unbuilt-at-41 thread is unchanged |
| 6 | Medium | Day 2 was unassigned, so Tova's two-day look could not be located and Chapter 3's deadline floated | Day 2 assigned to Tova's look (days 2–3, closing on the afternoon of day 3). Chapter 3 and Chapter 2 cards restated; day clock in both the batch file and `state/continuity.md` now agrees |
| 7 | Medium | "Sensory bleed" used where canon says "memory bleed" | Changed in the batch file and `outline/volume-01.md`. `bible/terminology.md` now explains that sensory bleed is ordinary speech for a minor case, so the bible is internally consistent. `outline/series.md:147` and `bible/power-system.md:48,59` were left alone — pre-existing canon, not findings |
| 8 | Low | Chapter 4 card said `POV: Marek, with Lissa`; the other nine are single-POV | Corrected to `POV: Marek`, and called out in the batch prompt so Lissa still carries the scene's hardest lines without becoming a second viewpoint |
| 9 | Low | "Pathhound" defined in `bible/world.md` but absent from the vocabulary authority | Added a `### Pathhound` entry to `bible/terminology.md` plus a usage rule, matching the volume's guardrail that it is never commanded and not solved by killing its anchor |
| 11 | Low | The compound coat's origin was never established, though the Ch 14–17 hand seal and the flood both rest on it | Pinned in Chapter 1: laid by Kellan's crew four seasons ago as a surface hold, topped up annually, never replaced, logged as a proper seal. Day 3 is the last top-up. Recorded in Chapters 1, 4, 9, the volume's open-clocks table, and continuity locks |
| 12 | Low | Prompts said "Use System language sparingly"; this novel has no System | The surviving prompt now states that the Fieldbook is the novel's only system-like interface, permits one panel in Chapter 6, and forbids stat blocks and ranks |
| 13 | Low | Chapters 4 and 10 are both seed-house meetings | Watch item, not a defect. The outline already differentiates them (Ch 4 courier in person and a spoiled line; Ch 10 a letter refused before a clerk and a document handed over). The distinction is now written into the batch notes and the prompt so the echo is handled deliberately |

### Also found during the fix pass

- `state/open-threads.md` said the charter expiry and the **Directorate hearing** were the same date. The hearing is in Chapters 46–48, after the eighteenth; the eighteenth is the charter expiry and the annual **inspection**. Corrected, so a writer does not stage a hearing on the wrong day.
- `state/current.md` listed the Quiet Break and False Season as Volume 01 "active promises", contradicting the volume's own guardrails. Replaced with the promises Volume 01 actually pays, and marked the series threads as forbidden in this volume.

## Not applied — needs a human

These are controller files. The operating rules for this agent forbid editing them, so they were left untouched. Both are live and both will recur every batch.

**A. The review gate is silently degraded (reviewer High #2).**
`.opencode/agent/novel-reviewer.md:3` declares `mode: subagent`, but `scripts/novel_runner.sh:212` invokes it as `opencode run --agent novel-reviewer`, which requires a *primary* agent. Every review therefore falls back to the default writer agent:

```
! agent "novel-reviewer" is a subagent, not a primary agent. Falling back to default agent
```

The check still happened — the findings in this file are real and found the defects above — but the gate does not do what AGENTS.md's quality gate claims. Either drop `mode: subagent` from the agent file or invoke it through the subagent path. Note that this review was produced by the fallback agent and did not edit files, which is the behaviour the gate wanted.

**B. `state/phase-ledger.json` is stale and unowned (reviewer Low #10).**
It still reads `currentPhase: "phase-000-bootstrap"`, `status: "planned"`, `attempts: 0` after bootstrap completed and the outline landed. It is referenced by no script or workflow, only by `PHASE_SYSTEM.md`, `OUTLINE_GUIDE.md`, `.opencode/agent/novel-writer.md`, and logs.

There is also a standing instruction conflict: phase prompts tell the writer to update the phase ledger, and the writer's operating rules forbid editing `state/phase-ledger.json`. That will recur every batch. Pick one owner — either the runner writes the ledger and the prompts stop asking, or the writer owns it and the operating rules change — and resolve it in one place. Until then, `state/current.md` is the de facto status file and the phase prompt in this batch tells the writer to record ledger conflicts there and move on.
