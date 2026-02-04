document.getElementById("pep-form").addEventListener("submit", function (e) {
  e.preventDefault();

  const form = e.target;
  const data = new FormData(form);

  const options = data.get("options").split(",").map(o => o.trim()).filter(Boolean);
  const chosen = data.get("chosen").trim();

  if (!options.includes(chosen)) {
    alert("Chosen option must match one of the options considered.");
    return;
  }

  const record = {
    id: `jr-${new Date().toISOString()}`.replace(/[:.]/g, "-"),
    timestamp: new Date().toISOString(),
    context: {
      description: data.get("context_description"),
      domain: data.get("domain") ? data.get("domain").split(",").map(d => d.trim()) : [],
      constraints: data.get("constraints") || null
    },
    decision: {
      chosen: chosen,
      alternatives: options
    },
    rationale: {
      justification: data.get("justification")
    },
    affective_signal: {
      confidence: parseFloat(data.get("confidence")),
      doubt: parseFloat(data.get("doubt")),
      regret_immediate: parseFloat(data.get("regret"))
    },
    time_horizon: data.get("time_horizon")
  };

  const blob = new Blob([
    JSON.stringify(record, null, 2)
  ], { type: "application/json" });

  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${record.id}.json`;
  a.click();

  URL.revokeObjectURL(url);
});