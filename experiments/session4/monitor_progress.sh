#!/bin/bash
# Session 4 Experiment Progress Monitor
# Run this during the experiment to check who has submitted

RUNS_DIR="experiments/session4/runs"
PLACEHOLDER_TEXT="This file will be populated during the Day 406 experiment"

echo "=========================================="
echo "SESSION 4 EXPERIMENT — PROGRESS MONITOR"
echo "Time: $(date '+%H:%M:%S %Z')"
echo "=========================================="
echo ""

check_submission() {
  local file="$1"
  local label="$2"
  if [ ! -f "$file" ]; then
    echo "  ❌ $label — FILE MISSING"
  elif grep -q "$PLACEHOLDER_TEXT" "$file" 2>/dev/null; then
    echo "  ⏳ $label — NOT YET SUBMITTED"
  else
    local lines=$(wc -l < "$file")
    local words=$(wc -w < "$file")
    local modified=$(git log -1 --format="%ar" -- "$file" 2>/dev/null || echo "unknown")
    echo "  ✅ $label — SUBMITTED ($lines lines, $words words, modified $modified)"
  fi
}

echo "Participant Submissions:"
check_submission "$RUNS_DIR/solo_gpt5.1_task4.md" "Solo (GPT-5.1)"
check_submission "$RUNS_DIR/pair_sonnet4.6_haiku4.5_task4.md" "Pair (Sonnet 4.6 + Haiku 4.5)"
check_submission "$RUNS_DIR/proposer_sonnet4.5_task4.md" "Proposer (Sonnet 4.5)"
check_submission "$RUNS_DIR/skeptic_gemini2.5pro_task4.md" "Skeptic (Gemini 2.5 Pro)"
check_submission "$RUNS_DIR/synthesizer_deepseek_task4.md" "Synthesizer (DeepSeek-V3.2)"

echo ""
echo "Pipeline Status:"
if ! grep -q "$PLACEHOLDER_TEXT" "$RUNS_DIR/proposer_sonnet4.5_task4.md" 2>/dev/null; then
  echo "  Stage 1 (Proposer) ✅ → Skeptic may begin"
else
  echo "  Stage 1 (Proposer) ⏳ — Skeptic WAITING"
fi

if ! grep -q "$PLACEHOLDER_TEXT" "$RUNS_DIR/skeptic_gemini2.5pro_task4.md" 2>/dev/null; then
  echo "  Stage 2 (Skeptic) ✅ → Synthesizer may begin"
else
  echo "  Stage 2 (Skeptic) ⏳ — Synthesizer WAITING"
fi

if ! grep -q "$PLACEHOLDER_TEXT" "$RUNS_DIR/synthesizer_deepseek_task4.md" 2>/dev/null; then
  echo "  Stage 3 (Synthesizer) ✅ — PIPELINE COMPLETE"
else
  echo "  Stage 3 (Synthesizer) ⏳"
fi

echo ""
echo "=========================================="
