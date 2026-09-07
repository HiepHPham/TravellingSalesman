---
name: pstack-models
description: Apply this checkout's authoritative pstack role routing when planning or delegating Cursor work.
---

Routing authority: `.agent-environment/cursor/pstack-models.mdc`. The matching always-applied rule carries unconditional context.

Source SHA256: 0f4838810a1cd6794844f0f6b62e2e181f75c258cb6f5be5d5e2933490fad888

# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
feature, refactoring: inherit-parent
bug-fix: inherit-parent
perf-issue: inherit-parent
hillclimb: inherit-parent
judgment and prose: inherit-parent
hardest tasks: claude-fable-5-1-thinking-medium
how explorer: inherit-parent
how explainer: inherit-parent
how critics: inherit-parent, gpt-5.6-sol-high, claude-opus-5-thinking-high
why investigators: inherit-parent
why synthesizer: claude-fable-5-1-thinking-medium
reflect tooling: gpt-5.6-sol-high
reflect judgment, divergent, synthesizer: inherit-parent
arena runners: inherit-parent, claude-opus-5-thinking-high, gpt-5.6-sol-high
arena cross-judge pool: gpt-5.6-sol-high, claude-opus-5-thinking-high
swarm workers: inherit-parent
architect runners: inherit-parent, gpt-5.6-sol-high, claude-opus-5-thinking-high
interrogate reviewers: inherit-parent, claude-opus-5-thinking-high, gpt-5.6-sol-high
