---
name: find-unknowns
description: Surface decision-changing unknowns when the user asks what is missing, requests an architecture or unknowns sweep, invokes find-unknowns log or close, or repeated plan deviations reveal an incomplete understanding.
---

# Find unknowns

Find gaps that could change a decision or invalidate the plan. Read the relevant
instructions, task artifacts, code, and primary evidence. Distinguish intended
outcomes, observed facts, assumptions, and open questions.

Inspect independent perspectives that can falsify the current understanding:
user needs, code and data, runtime conditions, external dependencies, and failure
modes. Delegate separate perspectives when independence improves coverage.

Verify findings against source artifacts. Resolve accessible repository and
environment questions directly. For each material unknown, capture the affected
decision, missing evidence, cheapest reliable resolution, and next owner. Ask the
user about consequential intent or authority that the evidence cannot establish.

With `log`, update the current map after a changed assumption or observation.
With `close`, move established facts to their owning artifacts and leave a compact
set of unresolved questions and next actions. Use the standing authoring guidance
to keep the map useful for ongoing work.
