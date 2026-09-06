---
name: ship
description: Carry an authorized change or existing pull request through review, merge, and documented deployment with live verification. Also use for ship loop or ship babysit requests.
---

# Ship

Deliver the change through the repository's actual release path. Follow standing
model, ownership, storage, and authoring guidance. Scope the work and verification
to the user's request and the surfaces the diff changes.

## Prepare and verify

Read the project's instructions and release documentation. Establish the actual
remote, default branch, existing work, required checks, merge authority, and each
affected shipped surface. Use an isolated branch or worktree that preserves
unrelated changes. Build the requested result and keep a recoverable checkpoint.

Run checks that establish the changed behavior and required project gates. Obtain
independent review, resolve factual disagreements with evidence, and rerun checks
affected by fixes. Exercise the real consumer: rendered UI for visual changes,
actual parsing/loading for configuration, synthetic isolated data for migration
rehearsals, and the supported client path for integration changes.

## Release

Create or update the pull request using the configured host's tooling. Describe
the concrete problem, resulting behavior, and verification. Stage the intended
paths and use a body file for multiline CLI descriptions. Wait for required
checks and address material review findings; distinguish absent CI from passing
CI. If a failure repeats, investigate its mechanism before another fix attempt.

Merge through the documented owner and policy when the required gates pass.
Verify the resulting default-branch commit. Deploy changed runtime surfaces using
the project's documented procedure and observe the changed behavior live.
Development-only changes need their consumer's loading evidence; a service
redeploy is relevant when its shipped behavior changes.

For compiled clients, validate packaging before merge and distribute from the
documented release ref. Treat processing acceptance and available releases as
separate states. Use existing unattended release credentials. If credentials or a
required verification surface are unavailable, complete the independent work and
report the exact outstanding prerequisite and shipment status.

## Close out

Keep the backlog focused on open work and record useful follow-ups at their
owning source. Confirm remote and deployed state, then remove only task-owned
disposable worktrees, branches, scratch, and devices. Preserve modified,
unpublished, shared, and evidentiary state. Use PR state and the actual merge
commit when checking squash-merged branches.

Report the result, commit and PR, what was observed working, and any incomplete
release gate. External notifications follow the user's communication request.

## Repeated work

`ship babysit` follows the existing PR through the same release path. Wait on
meaningful state changes while checks run. A later wakeup uses the environment's
supported scheduler when requested.

`ship loop` chooses actionable backlog work in project priority order, completes
one release at a time, and continues within the requested limit. Items needing
new authority or unresolved user intent remain open with a concrete next action.
Resolve a failed deployment or restore service before starting another item.
