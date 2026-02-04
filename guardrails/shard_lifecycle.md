# Value Shard Lifecycle Rules

Value shards represent semi-stable evaluative lenses.
They are not immutable, but changes must be explicit and logged.

## Creation

A shard may be created when:
- A recurring consideration appears in multiple judgments
- A value tension cannot be expressed by existing shards

Creation requires:
- Label
- Description
- Initial rationale

---

## Activation

Shards activate per judgment via `shard_activations`.
Activation strength is contextual, not absolute.

---

## Override

When a shard is overridden:
- The override is recorded
- The shard is not weakened automatically

Overrides are informational, not corrective.

---

## Mutation

A shard may be re-described (mutation) when:
- Its meaning drifts
- Its scope becomes unclear

Mutation creates a *new version*, not an edit.

---

## Retirement

A shard may be retired when:
- It no longer activates across judgments
- It is subsumed explicitly by another shard

Retired shards remain in history.

---

## Prohibited

- Automatic shard creation
- Automatic shard deletion
- Collapsing shards into a single score
