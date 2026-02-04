"""
Rule-based similarity logic stub for PEP.

This module intentionally avoids embeddings or learned weights.
Similarity is explainable and descriptive only.
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JUDGMENT_DIR = os.path.join(BASE_DIR, "logs", "judgment_log")


def load_judgments():
    records = []
    if not os.path.isdir(JUDGMENT_DIR):
        return records
    for fname in os.listdir(JUDGMENT_DIR):
        if fname.endswith(".json"):
            with open(os.path.join(JUDGMENT_DIR, fname)) as f:
                records.append(json.load(f))
    return records


def explain_similarity(query_text, record):
    reasons = []

    context = record.get("context", {})
    desc = context.get("description", "").lower()

    if any(word in desc for word in query_text.lower().split()):
        reasons.append("Shared contextual language")

    domain = context.get("domain", [])
    if domain:
        reasons.append(f"Overlapping domain: {', '.join(domain)}")

    return reasons


def find_similar(query_text, limit=3):
    records = load_judgments()
    scored = []

    for r in records:
        reasons = explain_similarity(query_text, r)
        if reasons:
            scored.append((r, reasons))

    return scored[:limit]
