---
id: julie-recovery-and-comparison-baseline
title: Julie recovery and comparison baseline
status: active
created: 2026-09-23T21:25:01.007Z
updated: 2026-09-23T21:55:18Z
tags:
  - revival
  - recovery
  - comparison
---

## Goal
Restore Julie as a working code-intelligence service using julie-extractors v3.5.0, then compare its real agent workflows and operating cost with code-kb and Miller before deciding what to simplify further.

## Why now
Julie v8 work stopped before release, while code-kb became a lighter alternative. The current Codex session reports Julie MCP as failed despite a valid local registration.

## Constraints
Keep Julie's language coverage and source-edit behavior intact. Prefer targeted fixes and removal of stale instructions over a speculative rewrite. Do not push, tag, publish, or release as part of recovery. Honor the repo's full-gate retry budget.

## Success criteria
A fresh stdio shim initializes, lists tools, opens and searches Julie; service and workspace status agree. Current extractor contract tests and service tests pass. The Linux full gate is either green or precisely marked pending under its owner-decision rule. Historical v8 Windows and Plan 5 qualification branches remain explicit follow-up work.

## Current state
Recovery changes are in `fix/revival-recovery` under `.worktrees/revival-recovery`. The release binary and machine service have been rebuilt with extractor v3.5.0; direct MCP initialize, tools/list, workspace open, search, and live status checks pass. The first full run stopped on a missing worktree temp directory; its allowed retry found a stale extractor fixture expectation. The owner-approved third run found two mixed-traversal fixture expectations changed by v3.5.0. All reported failures now pass exact tests; a fourth full run awaits an owner decision. The current Codex UI still needs a fresh-session check.

## References
- `docs/plans/2026-09-07-julie-revival-program.md`
- `fix/revival-qualification` (unmerged Plan 5A/B)
- `fix/revival-deployment` (unmerged Windows restart experiments)
