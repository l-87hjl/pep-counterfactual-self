# PEP Living Checklist

This document exists to keep active design commitments *alive outside conversation context*.
It is intentionally explicit and conservative.

Nothing should be removed from this list without a written justification.

---

## Phase 0 — Epistemic Commitments (Must Always Hold)

- ☐ No automatic decisions
- ☐ No recommendations framed as authority
- ☐ No global scoring or utility function
- ☐ No collapse of values into a single metric
- ☐ Human assent required for every judgment
- ☐ Regret never rewrites history

---

## Phase 1 — Prerequisites (Must Exist Before Any Functionality)

- ✔ README.md with clear non-goals
- ✔ MANIFEST.md epistemic commitments
- ✔ SQL schema finalized
- ✔ Shard lifecycle rules defined
- ✔ Failure modes documented
- ✔ Value Override Zone (VOZ) spec locked
- ✔ VOZ signals and CLI rendering rules locked

---

## Phase 2 — Critical Milestones (Gate Functional Code)

The following **must be completed in order** before PEP is considered functional.

### Milestone A — Judgment Fixtures (Required First)

- ☐ Baseline fixture (clean judgment)
- ☐ Ambiguous fixture (unresolved tension)
- ☐ VOZ-triggering fixture (instability without override)
- ☐ Regret-bearing fixture (known bad judgment)

No code should be trusted without fixtures.

---

### Milestone B — Similarity Logic (Stub)

- ☐ Explicit similarity rules implemented
- ☐ Similarity explanations surfaced
- ☐ Novelty / sparsity flags supported

Embeddings are explicitly deferred.

---

### Milestone C — CLI Skeleton

- ☐ `pep new`
- ☐ `pep synthesize`
- ☐ `pep regret`
- ☐ `pep shards`

Constraints:
- No advice language
- No defaults
- No auto-activation
- Must respect VOZ rendering rules

---

## Phase 3 — Guarded Future Work

- ☐ Embeddings (only after misuse testing)
- ☐ UI (only after CLI resistance validated)
- ☐ Visualization (must not imply certainty)

---

## Stop Conditions (Hard)

Do NOT proceed if:
- Outputs feel convenient to obey
- You stop writing justifications
- Regret updates feel unnecessary
- The system feels smarter than you

That indicates epistemic failure, not success.
