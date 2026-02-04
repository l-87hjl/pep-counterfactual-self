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

## Phase 1 — Core Implementations (In Progress)

### CLI-Based Flow

- ☐ `pep new` — create judgment records with required justification
- ☐ `pep synthesize` — read-only synthesis with uncertainty flags
- ☐ `pep regret` — append-only regret updates
- ☐ `pep shards` — read-only shard inspection

Constraints:
- No defaults
- No advice language
- No auto-activation of shards

---

### Judgment Fixtures

- ☐ Fixture: Autonomy vs Pay (clean, confident)
- ☐ Fixture: Growth vs Stability (ambiguous, conflicted)
- ☐ Fixture: Known bad judgment (anticipates regret)

Fixtures must:
- Feel human
- Include counterfactuals
- Preserve doubt and tension

---

### Failure Modes Documentation

- ☐ Authority Creep
- ☐ Moral Laundering
- ☐ Self-Reinforcing Bias
- ☐ Quantification Drift
- ☐ Identity Freeze
- ☐ Epistemic Laziness

Each failure mode must include:
- How it sneaks in
- Warning signs
- Why it is dangerous *here*
- What PEP refuses to optimize

---

### Language Lint (Synthesis Output)

Forbidden language:
- should
- recommend
- optimal
- best choice
- must
- decide

Required language:
- historically
- in similar cases
- plausible
- limited precedent
- uncertain

Goal:
Prevent authority creep via tone.

---

### Similarity Engine (Stub Only)

Allowed signals:
- Domain overlap
- Shared shard activations
- Constraint keyword overlap
- Time horizon match

Explicitly deferred:
- Embeddings
- Learned weights
- Semantic similarity via LLMs

---

## Phase 2 — Conceptual (Design Before Code)

### Value Override Zones (Important)

- ☐ Identify patterns where defaults historically break
- ☐ Surface *possibility* of override without predicting it
- ☐ Explicitly flag low-confidence, high-meaning contexts

Key rule:
The system may *highlight risk of override*, never predict it.

---

## Phase 3 — Guarded Future Work (Do Not Rush)

- ☐ Embeddings (only after failure modes are tested)
- ☐ UI (only after CLI resistance is validated)
- ☐ Visualization (must not imply certainty)

---

## Stop Conditions

Do NOT proceed if:
- Outputs feel convenient to obey
- You stop writing justifications
- Regret updates feel unnecessary
- The system feels smarter than you

That indicates epistemic failure, not success.
