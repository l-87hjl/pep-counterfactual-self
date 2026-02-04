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

### Milestone A — Judgment Fixtures

- ☐ Baseline fixture (clean judgment)
- ☐ Ambiguous fixture (unresolved tension)
- ✔ VOZ-triggering fixture (instability without override)
- ☐ Regret-bearing fixture (known bad judgment)

---

### Milestone B — Similarity Logic (Stub)

- ✔ Rule-based similarity implemented
- ☐ Similarity explanations refined (still rule-based)
- ☐ Precedent brittleness heuristics added

---

### Milestone C — CLI Skeleton

- ✔ `pep new`
- ✔ `pep synthesize`
- ✔ `pep regret`
- ✔ `pep shards`

- ☐ Language lint pass added
- ☐ Manual output audit completed

---

## Phase 2.5 — Web Capture Interface (Optional, Non-Synthesizing)

- ✔ Static HTML form for judgment capture
- ✔ Client-side only (no storage, no network)
- ✔ Outputs downloadable artifacts only
- ✔ Explicit statement: no analysis or synthesis
- ☐ ZIP exporter (multiple artifacts, README included)
- ☐ Shard capture fields (recording only, no inference)
- ☐ Explicit prohibition on synthesis, similarity, or VOZ

---

## Phase 3 — Optional, Guarded Enhancements

### VOZ Enhancements (Optional)

- ☐ Inspect shard activations during synthesis
- ☐ Incorporate regret history (descriptively)
- ☐ Detect precedent brittleness more deeply

---

### Practice & Audit

- ☐ Run full end-to-end manual session (documented)
- ☐ Audit synthesis language against lint rules
- ☐ Record subjective friction and discomfort

---

## Stop Conditions (Hard)

Do NOT proceed if:
- Outputs feel convenient to obey
- You stop writing justifications
- Regret updates feel unnecessary
- The system feels smarter than you

That indicates epistemic failure, not success.
