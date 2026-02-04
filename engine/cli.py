#!/usr/bin/env python3
"""
PEP CLI Skeleton

This CLI intentionally prioritizes friction, explicit reflection,
and epistemic safety over convenience.

No command produces a decision or recommendation.
"""

import argparse
import json
import os
import sys
from datetime import datetime

from engine.similarity import find_similar
from engine.voz import detect_voz

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, "logs", "judgment_log")


def prompt_required(text):
    while True:
        value = input(f"{text}\n> ").strip()
        if value:
            return value
        print("This field is required.")


def prompt_float(text):
    while True:
        try:
            value = float(prompt_required(text))
            if 0.0 <= value <= 1.0:
                return value
        except ValueError:
            pass
        print("Enter a number between 0 and 1.")


def pep_new():
    print("Creating new judgment record. All responses require deliberate input.\n")

    context_description = prompt_required("Describe the situation as you understand it")
    domain = prompt_required("Domain tags (comma-separated)")
    constraints = prompt_required("Constraints")

    options_raw = prompt_required("Options considered (comma-separated)")
    options = [o.strip() for o in options_raw.split(',') if o.strip()]

    chosen = prompt_required("Option chosen (must match one above)")
    if chosen not in options:
        print("Chosen option must match one of the listed options.")
        sys.exit(1)

    justification = prompt_required("Rationale / justification")
    time_horizon = prompt_required("Time horizon (short / medium / long)")

    confidence = prompt_float("Confidence (0–1)")
    doubt = prompt_float("Doubt (0–1)")
    regret = prompt_float("Immediate regret (0–1)")

    record_id = f"jr-{datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S')}"

    record = {
        "id": record_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "context": {
            "description": context_description,
            "domain": [d.strip() for d in domain.split(',')],
            "constraints": constraints
        },
        "decision": {
            "chosen": chosen,
            "alternatives": options
        },
        "rationale": {
            "justification": justification
        },
        "affective_signal": {
            "confidence": confidence,
            "doubt": doubt,
            "regret_immediate": regret
        },
        "time_horizon": time_horizon
    }

    os.makedirs(LOG_DIR, exist_ok=True)
    path = os.path.join(LOG_DIR, f"{record_id}.json")
    with open(path, "w") as f:
        json.dump(record, f, indent=2)

    print(f"Judgment record saved to {path}")


def pep_synthesize():
    print("Synthesis is descriptive only. No recommendations will be made.\n")
    query = prompt_required("Describe the situation you want to reflect on")

    similar = find_similar(query)

    if similar:
        print("Precedent Summary:")
        for rec, reasons in similar:
            print(f"- {rec.get('id')}: {', '.join(reasons)}")
        print("")

    voz_signals = detect_voz({"rationale": {"justification": query}}, similar)

    if voz_signals:
        print("Contextual Notes:")
        for s in voz_signals:
            print(f"- {s}")
        print("\nThis note is descriptive only and does not imply any particular outcome.\n")

    print("Plausible judgments are intentionally not generated at this stage.")


def pep_regret(judgment_id):
    print(f"Adding regret reflection for {judgment_id}\n")

    regret_level = prompt_float("Regret level (0–1)")
    reflection = prompt_required("What was misjudged?")
    signal = prompt_required("What signal was ignored?")
    future = prompt_required("What would you attend to next time?")

    update = {
        "judgment_id": judgment_id,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "regret_level": regret_level,
        "reflection": reflection,
        "ignored_signal": signal,
        "future_attention": future
    }

    regret_dir = os.path.join(BASE_DIR, "logs", "regret_log")
    os.makedirs(regret_dir, exist_ok=True)
    path = os.path.join(regret_dir, f"rg-{judgment_id}.json")

    with open(path, "w") as f:
        json.dump(update, f, indent=2)

    print(f"Regret update saved to {path}")


def pep_shards():
    print("Shard inspection is not yet implemented.")
    print("This command will remain read-only.")


def main():
    parser = argparse.ArgumentParser(description="Personal Epistemic Prosthesis (PEP)")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("new")
    sub.add_parser("synthesize")

    regret_parser = sub.add_parser("regret")
    regret_parser.add_argument("judgment_id")

    sub.add_parser("shards")

    args = parser.parse_args()

    if args.command == "new":
        pep_new()
    elif args.command == "synthesize":
        pep_synthesize()
    elif args.command == "regret":
        pep_regret(args.judgment_id)
    elif args.command == "shards":
        pep_shards()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
