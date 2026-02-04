"""
Value Override Zone (VOZ) detection logic.

This module surfaces qualitative signals only.
It must not score, predict, or recommend.
"""

from engine.voz_signals import __doc__  # marker import to tie spec

IDENTITY_KEYWORDS = [
    "who i am",
    "identity",
    "integrity",
    "become",
    "not who",
    "live with"
]


def detect_voz(judgment, similar_records):
    signals = []

    # 1. Concurrent core pressures (heuristic: >1 shard)
    shards = judgment.get("shard_activations", [])
    if len(shards) >= 2:
        signals.append("Several core considerations are strongly present at the same time.")

    # 2. Historically unsettled tradeoff
    if similar_records:
        signals.append("Similar tradeoffs have not resolved cleanly in the past.")

    # 3. Identity-adjacent framing
    text = judgment.get("rationale", {}).get("justification", "").lower()
    if any(k in text for k in IDENTITY_KEYWORDS):
        signals.append("This situation appears closely connected to how you see yourself.")

    # 4. Sensitivity to small changes
    if judgment.get("counterfactuals"):
        signals.append("Small changes in conditions could significantly change how acceptable options feel.")

    # 5. Atypical decision process
    aff = judgment.get("affective_signal", {})
    if aff.get("doubt") and aff.get("confidence"):
        try:
            if float(aff["doubt"]) > float(aff["confidence"]):
                signals.append("Your decision process here differs from your usual pace or clarity.")
        except Exception:
            pass

    return signals
