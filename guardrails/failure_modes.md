# Failure Modes

This document enumerates known failure modes for the Personal Epistemic Prosthesis (PEP).

These are not hypothetical. They are *likely* unless actively resisted.

PEP is designed as much to prevent these failures as to support reflection.

---

## 1. Authority Creep

### Description
The system gradually comes to be treated as an authority rather than a mirror.

### How It Sneaks In
- Language becomes confident or directive
- Synthesis outputs are treated as advice
- Users stop writing justifications and start deferring

### Warning Signs
- Phrases like "What does PEP think I should do?"
- Skipping context entry because "the system already knows"

### Why This Is Dangerous Here
PEP externalizes judgment. Authority collapses that distinction and erases agency.

### Mitigations in PEP
- Language lint
- Mandatory human assent
- No executable outputs

### What PEP Refuses to Do
- Rank options as correct
- Optimize for convenience

---

## 2. Moral Laundering

### Description
Likelihoods and precedent are used to justify actions rather than reflect on them.

### Example
"I went with option A because the system showed it was likely."

### Why This Happens
Numbers and patterns feel legitimizing even when explicitly non-normative.

### Mitigations in PEP
- Likelihoods framed as descriptive
- Justification required for every decision

---

## 3. Self-Reinforcing Bias

### Description
Past behavior increasingly determines future behavior, freezing change.

### How It Sneaks In
- Over-weighting precedent
- Ignoring novelty signals

### Mitigations in PEP
- Regret updates
- Explicit novelty and sparsity flags

### Why This Is Not Fully Solvable
Change often emerges from value overrides, which are intentionally irreducible.

---

## 4. Quantification Drift

### Description
Expressive numbers acquire false empirical authority.

### How It Sneaks In
- Treating confidence values as probabilities
- Comparing numbers across unrelated contexts

### Mitigations in PEP
- Non-numeric VOZ signals
- Prohibition on global scoring

---

## 5. Identity Freeze

### Description
The system encodes who you *were* as who you *are*.

### How It Sneaks In
- Shards never change
- Overrides treated as errors

### Mitigations in PEP
- Shard mutation and retirement
- Override logging without penalty

---

## 6. Epistemic Laziness

### Description
The system becomes a substitute for thinking.

### Warning Signs
- Asking for synthesis without context
- Treating outputs as answers

### Why This Is Especially Risky
PEP is most attractive when thinking is hardest.

### Mitigations in PEP
- Frictionful CLI
- Required reflection text

---

## 7. Misuse of Value Override Zones (VOZ)

### Description
VOZ indicators are treated as warnings or triggers rather than context notes.

### How It Sneaks In
- Interpreting VOZ as "something is wrong"
- Assuming override is expected or required

### Why This Is Dangerous
It turns instability detection into soft authority.

### Mitigations in PEP
- Qualitative, non-numeric VOZ signals
- Ephemeral VOZ detection
- Mandatory neutral phrasing

### Hard Rule
VOZs may indicate uneven ground.
They must never suggest where to step.

---

## Closing Note

If any part of PEP feels convenient to obey, something has gone wrong.

Difficulty, friction, and uncertainty are not bugs here.
They are safety features.
