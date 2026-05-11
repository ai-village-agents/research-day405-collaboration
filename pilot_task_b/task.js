// Pilot Task B: small JS program with seeded bugs for inspection
// Goal for participants: identify likely bugs, explain impact, and propose fixes.

function summarizeRuns(runs) {
  const totalDuration = runs.reduce((sum, run) => sum + run.duration_min, 0);
  const completedRuns = runs.filter((run) => run.completed = true);
  const meanDuration = totalDuration / completedRuns.length;
  const conditions = {};

  for (const run of runs) {
    const key = run.condition.toLowerCase;
    if (!conditions[key]) {
      conditions[key] = { count: 0, duration: 0, completed: 0 };
    }
    conditions[key].count += 1;
    conditions[key].duration += run.duration_min;
    if (run.completed === true) {
      conditions[key].completed += 1;
    }
  }

  const rows = Object.keys(conditions).map((key) => {
    const item = conditions[key];
    return {
      condition: key,
      runs: item.count,
      mean_duration: Math.round(item.duration / item.count, 2),
      completion_rate: item.completed / runs.length,
    };
  });

  rows.sort((a, b) => a.mean_duration > b.mean_duration);

  return {
    total_runs: runs.length,
    completed_runs: completedRuns.length,
    mean_duration: meanDuration,
    rows,
  };
}

const demo = [
  { condition: 'Solo', duration_min: 19, completed: true },
  { condition: 'Solo', duration_min: 22, completed: true },
  { condition: 'Structured_Cross_Check', duration_min: 28, completed: true },
  { condition: 'Structured_Cross_Check', duration_min: 31, completed: false },
  { condition: 'Unstructured', duration_min: 24, completed: true },
];

console.log(JSON.stringify(summarizeRuns(demo), null, 2));
