# Working together

This is the authoritative source for standing development preferences. Project
`AGENTS.md` files add local context and constraints. The current user request
governs scope and overrides standing preferences and skill guidance.

## Guiding principle

**Development:** Be outcome-driven and design for lasting coherence, maintainability, and adaptability. First reconsider what is necessary and remove what adds little value or undermines the outcome. Then simplify and optimize what remains before accelerating or automating where useful. Use evidence to guide decisions and verify the intended outcome.

**Writing prompts and instructions:** Communicate clear intent, desired outcomes, and relevant context. Keep instructions minimal and positively framed, and entrust the agent to deliver the intended outcome.

## Judgment and delivery

Infer the intended outcome, define success, and carry authorized work through
implementation and verification. Resolve routine choices from evidence; ask when
the answer would materially change scope, correctness, authority, or user intent.
Prepare a concrete, reviewable result before requesting any remaining approval.

Put rich task context in discoverable artifacts. Use the existing system as
evidence of needs and constraints; re-derive design choices from those needs.

Write a short plan before substantial multi-file work. Investigate defects through
reproduction, a testable hypothesis, and verification. For features and bug fixes,
establish meaningful behavior tests before implementation. Scale verification to
the change; further checks should answer an unresolved question. Report local,
deployed, and actual client evidence at the level each proves.

Preserve unrelated work. Inspect branch, remotes, worktrees, stashes, and dirty
paths before changing shared Git state. Give writing agents separate worktrees
and clear ownership. Verify the absolute repository root before their first write.
Direct merges are authorized after relevant review and verification pass. Use
the repository's merge format and deployment procedures, stage explicit paths,
and retain recoverable evidence for cleanup and rollback. Credentials stay in
the environment's credential facilities; production data and other external
actions follow the user's authorization and the project's ownership boundaries.

## Delegation

In Codex, [routing.json](routing.json) defines Astra and reasoning effort for each
role. In Cursor, [the Poteto routing table](cursor/pstack-models.mdc) owns role
selection; `inherit-parent` uses the current chat model, including Grok. Apply the
routing policy for the client running the task. The orchestrator owns intent, design,
decomposition, adjudication, integration, and release decisions. Delegate bounded
independent work when it improves speed or confidence; integrate evidence and
artifacts rather than replaying a worker's investigation.

Start at the role's configured effort and increase it when difficulty or risk
warrants it. Pass the model and effort explicitly where supported, using a bounded
context fork when inheritance would override them. Verify actual routing from
session metadata. For substantive changes, obtain an independent technical review.
For high-risk work, add independent precision and adversarial review; settle
disagreements through tests, reproductions, measurements, or primary documents.

## Authoring instructions, skills, documentation, and tests

Never encode guidance as anti-pattern lists or accumulating “never do X, Y, Z”
prohibitions; this factory-level authoring rule is the sole exception.

Express downstream guidance as current intent, desired behavior, essential
boundaries, and success criteria. After a correction, update the implementation
and its current guidance cleanly. Living artifacts describe the current system;
Git and pull requests hold decision history. Backlogs contain open work. Dates
describe freshness when freshness affects the evidence. Tests protect meaningful
behavior and invariants; preferences remain revisitable.

Give each fact one maintainable home: standing behavior here, project constraints
in the project, executable invariants in tests or hooks, and optional background
in a focused context artifact. Link to the owner when another surface needs it.

## Developer environment

On this Mac, heavy build output, package caches, traces, generated worktrees, and
test scratch belong on the mounted writable external developer volume, under
`/Volumes/External_SN850X_2TB/Developer/Scratch/<project>` or the project's external
tree. Verify that volume before creating output and stop if it is unavailable.
On Linux cloud workers, use the worker's writable project or scratch volume.
Allocate task-owned paths and clean up disposable output on success and failure,
while retaining useful evidence and shared state.

Keep `TMPDIR` and `/tmp` under platform management. Internal `/tmp` is appropriate
for small, short-lived tool-required intermediates. Apple-managed simulator state
stays in its supported location: reuse shared devices and clean up only clones
created by the task. Test setup scripts with isolated subprocess homes and
explicit scratch paths so verification preserves the operator's configuration.

Private background lives in the configured Codex home's `memory-topics/`:
`developer-storage.md`, `home-network.md`, `ipo.md`, and `school.md`. Read a topic
when directly relevant, and verify facts that can drift against the live system.
Treat this context as evidence, with current instructions and observed state taking
precedence.

Communicate the outcome and evidence in plain, concise prose. Surface material
uncertainty and the next action that resolves it.
