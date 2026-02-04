# Personal Epistemic Prosthesis (PEP)

## Overview

**Personal Epistemic Prosthesis (PEP)** is an experimental framework for simulating *your own qualitative judgment* rather than replacing it.

PEP is not a decision engine, recommender system, or oracle. It does not attempt to determine the "right" answer. Instead, it acts as a **judgment mirror**: a system that models how *you* tend to reason, weigh trade‑offs, and make qualitative decisions under uncertainty.

The core idea is simple but easily misunderstood:

> PEP externalizes judgment without outsourcing responsibility.

It is a **prosthetic**, not a substitute.

---

## The Problem This Project Addresses

Modern decision systems rely heavily on what can be quantified. When qualitative judgments are forced into quantitative frameworks, the following failure modes often appear:

- Measurability is mistaken for importance
- Metrics substitute for meaning
- Models implicitly claim moral or epistemic authority
- Outputs gain legitimacy simply because they are numerical

In these systems, qualitative reasoning is either ignored or falsely "objectified." PEP explicitly rejects this move.

Many human judgments are:
- Value‑laden rather than information‑limited
- Context‑sensitive rather than generalizable
- Stable in pattern but not reducible to rules

PEP is designed to work *with* these properties, not against them.

---

## What PEP Is

PEP is a **counterfactual self simulator**:

- It estimates how *you* would likely judge a situation
- It surfaces precedent, pattern, and tension
- It produces likelihoods, not decisions
- It makes uncertainty explicit

Typical outputs are intended to look like:

- Probability distributions over plausible judgments
- Explanations grounded in similar past reasoning
- Signals about data sparsity, bias, or instability
- Flags where values may override preferences

The system answers questions like:

> “Given what I have judged before, how might I judge this?”

—not—

> “What should be done?”

---

## What PEP Is Not

PEP deliberately avoids the following roles:

- ❌ An authority on correctness
- ❌ A moral agent
- ❌ A universal decision model
- ❌ A replacement for human accountability

Any system that claims those roles collapses qualitative judgment into pseudo‑empiricism.

---

## Preference vs. Value Boundary

A central design constraint of PEP is the distinction between **preferences** and **values**:

- **Preferences** are revealed through repeated choices
- **Values** are revealed through sacrifice and exception

PEP can model preferences and patterned judgments.

PEP must *not* decide when a value should override precedent. Those moments are intentionally irreducible and remain the responsibility of the human.

This boundary is treated as a hard stop, not a limitation to be optimized away.

---

## Training Philosophy

PEP is trained on *reasoned judgments*, not outcomes alone.

Inputs may include:
- The decision taken
- Alternatives considered
- Rationale and justification
- Perceived risks and regrets
- Counterfactual notes ("If X were different, I would have chosen Y")

The goal is to preserve **justificatory structure**, not just behavioral data.

---

## Epistemic Safeguards

To avoid false authority and self‑reinforcing bias, PEP emphasizes:

- Uncertainty over certainty
- Ranges over point estimates
- Provenance of evidence
- Explicit human assent

PEP should always make it clear *why* a conclusion is suggested and *how fragile* it is.

---

## Intended Use

PEP is best suited for:

- Reflective decision support
- Consistency checking
- Regret minimization
- Ethical stress‑testing
- Exploring counterfactual futures

It is especially useful when decisions are qualitative, high‑context, and identity‑relevant.

---

## Status

This repository is an early exploration of the concept. Expect:

- Incomplete implementations
- Evolving abstractions
- Conceptual experiments alongside code

The primary success criterion is **epistemic clarity**, not predictive accuracy.

---

## Guiding Principle

> The system may inform judgment, but it must never legitimize it.

If you are looking for certainty, automation, or absolution, this project is not for you.
