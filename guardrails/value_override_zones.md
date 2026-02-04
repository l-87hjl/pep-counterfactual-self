# Value Override Zones (VOZ)

This document formalizes **Value Override Zones** in the Personal Epistemic Prosthesis (PEP).

A Value Override Zone is **not a prediction** and **not a recommendation**.
It is a descriptive flag indicating that a situation exhibits characteristics where *default judgment patterns have historically broken down*.

PEP must never claim that an override will occur.
PEP may only indicate that **special care and reflection are warranted**.

---

## Definition

A **Value Override Zone (VOZ)** is a contextual condition in which:

- Multiple high-salience value shards activate simultaneously
- Those shards have unresolved historical tension
- Prior precedent shows brittleness, regret, or caveating
- The situation carries amplified meaning or identity implications
- Tradeoffs exhibit non-linear cost behavior

VOZs describe **instability**, not outcomes.

---

## What VOZ Is Not

- ❌ A probability score
- ❌ A prediction of behavior
- ❌ A moral judgment
- ❌ A trigger for automated action
- ❌ A "warning" that implies danger

Language implying inevitability or correctness is prohibited.

---

## Non-Numeric Signals to Surface

PEP must surface VOZ indicators using **qualitative signals only**.

### 1. High-Intensity Shard Co-Activation

Signal:
> "Multiple core considerations are strongly active at once."

Criteria:
- Two or more shards with high activation strength
- Historical tension recorded between them

---

### 2. Unresolved Historical Tension

Signal:
> "Similar situations have not resolved cleanly in the past."

Criteria:
- Prior judgments involving the same shard pair
- Presence of caveats, overrides, or later regret

---

### 3. Precedent Brittleness

Signal:
> "Past decisions in this area required exceptions or later reflection."

Criteria:
- Medium confidence paired with high doubt
- Counterfactual sensitivity present
- Regret updates associated with similar judgments

---

### 4. Meaning / Identity Amplification

Signal:
> "This situation appears closely tied to identity or self-concept."

Criteria:
- Language involving identity, integrity, or self-narrative
- Expressions of "becoming someone" or "not being able to live with"

---

### 5. Non-Linear Cost Sensitivity

Signal:
> "Small changes in conditions may significantly alter acceptability."

Criteria:
- Counterfactuals indicating sharp discontinuities
- Statements where incremental change leads to categorical refusal

---

### 6. Process Deviation

Signal:
> "Your decision process here differs from your usual pace or clarity."

Criteria:
- Increased hesitation
- Repeated reframing
- Explicit uncertainty about why the case feels different

---

## How VOZ Appears in CLI Synthesis

VOZ indicators must be presented as **contextual notes**, not alerts.

Example:

> "Note: This situation shares features with past cases where your usual patterns did not fully apply. You may want to slow down and reflect more deliberately."

Rules:
- No exclamation points
- No urgency framing
- No directive verbs
- No implication that an override is expected or desirable

---

## Logging and Memory

- VOZ detection is **ephemeral**
- VOZs are not stored as facts
- Only resulting judgments or regret updates become permanent records

This prevents reifying instability into identity.

---

## Design Constraint (Hard)

PEP may help you notice when the ground is uneven.
It must never tell you where to step.

If VOZ output feels ominous, urgent, or authoritative, the implementation is incorrect.
