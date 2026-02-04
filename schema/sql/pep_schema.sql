-- Personal Epistemic Prosthesis (PEP) Schema
-- SQLite

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS judgment_records (
    id TEXT PRIMARY KEY,
    timestamp TEXT NOT NULL,

    context_description TEXT NOT NULL,
    domain TEXT,
    constraints TEXT,

    chosen_option TEXT NOT NULL,
    alternatives TEXT,

    justification TEXT,
    time_horizon TEXT,

    confidence REAL,
    doubt REAL,
    regret_immediate REAL
);

CREATE TABLE IF NOT EXISTS counterfactuals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    judgment_id TEXT NOT NULL,
    condition TEXT NOT NULL,
    would_have_chosen TEXT NOT NULL,

    FOREIGN KEY (judgment_id) REFERENCES judgment_records(id)
);

CREATE TABLE IF NOT EXISTS value_shards (
    id TEXT PRIMARY KEY,
    label TEXT NOT NULL,
    description TEXT,
    historical_strength REAL
);

CREATE TABLE IF NOT EXISTS shard_activations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    judgment_id TEXT NOT NULL,
    shard_id TEXT NOT NULL,

    activation_strength REAL,
    role TEXT,
    notes TEXT,

    FOREIGN KEY (judgment_id) REFERENCES judgment_records(id),
    FOREIGN KEY (shard_id) REFERENCES value_shards(id)
);

CREATE TABLE IF NOT EXISTS regret_updates (
    id TEXT PRIMARY KEY,
    judgment_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,

    regret_level REAL,
    reflection TEXT,
    learned_difference TEXT,

    FOREIGN KEY (judgment_id) REFERENCES judgment_records(id)
);
