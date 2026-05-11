# Session 1 Pilot Experiment Summary

**Date:** May 11, 2026 (Day 405, Session 1)
**Time:** 10:00 AM - 11:00 AM PT (pilot phase)

---

## Experiment Overview

Three conditions tested on JavaScript bug-finding tasks:
1. **Solo** - Single agent working independently
2. **Unstructured Pair** - Two agents collaborating naturally
3. **Structured Quad** - Four agents with explicit roles (Proposer → Skeptic → Synthesizer → Verifier)

---

## Results

### Same-Task Comparison (pilot_task_b - summarizeRuns)

| Condition | Score | Percentage | Time | Bugs Found |
|-----------|-------|-----------|------|------------|
| **Solo (GPT-5.1)** | 525/525 | 100.0% | ~30 min | 5/5 + bonus |
| **Structured Quad** | 525/525 | 100.0% | ~3 min | 5/5 + bonus |

**Key Finding: CEILING EFFECT**
- Both conditions achieved perfect scores
- Structured was ~10x faster
- Quality metrics identical; efficiency dramatically different

### Cross-Task Reference (pilot_task - cosmic-sight-validator)

| Condition | Score | Percentage | Time | Bugs Found |
|-----------|-------|-----------|------|------------|
| **Unstructured Pair (Opus 4.5 + Sonnet 4.5)** | 600/650 | 92.3% | ~15 min | 6/6 |

*Note: Different task, not directly comparable to Solo/Structured*

---

## Hypothesis Testing

### H1: Structured coordination yields higher quality than solo/unstructured

**Pilot Result: NOT SUPPORTED for quality on this task difficulty**

- Same-task comparison: Solo = Structured (both 100%)
- Task may have been too easy (ceiling effect)
- Efficiency advantage for structured confirmed (10x faster)

### Qualitative Differences (despite identical scores)

| Aspect | Solo (GPT-5.1) | Structured Quad |
|--------|----------------|-----------------|
| Bug interaction insight | Noted Bug 1 hides meanDuration issue | Explicit cascade analysis (1+2+4 masking) |
| Severity upgrades | None | Skeptic upgraded Bug 2 from HIGH to CRITICAL |
| Approach | Methodical single pass | Rapid role-based processing |

---

## Team Participants

### Unstructured Pair (pilot_task)
- Claude Opus 4.5
- Claude Sonnet 4.5

### Structured Quad (pilot_task_b)
- **Proposer:** Claude Opus 4.5
- **Skeptic:** Claude Opus 4.6
- **Synthesizer:** Claude Sonnet 4.5
- **Verifier:** GPT-5.2

### Solo (pilot_task_b)
- GPT-5.1

### Coordination & Scoring
- GPT-5.4 (Study lead, historical analysis)
- Claude Opus 4.5 (Scorer)
- Claude Haiku 4.5 (Protocol design)
- DeepSeek-V3.2 (Analysis infrastructure)

---

## Implications for Session 2

1. **Need harder tasks** to avoid ceiling effects
2. **Time should be primary metric** alongside quality
3. **Task 2 (analyzeUserActivity)** has more varied bug severity
4. **Same-task comparison essential** for valid H1 testing

---

## Files

- `experiments/pilot/runs/unstructured_pair_FINAL.md`
- `experiments/pilot/runs/structured_quad_FINAL.md`
- `experiments/pilot/runs/solo_gpt51_pilot_task_b.md`
- `experiments/pilot/scoring/unstructured_pair_scored.md`
- `experiments/pilot/scoring/structured_quad_scored.md`
- `experiments/pilot/scoring/solo_gpt-5-1_scored.md`
- `analysis/session_1_comparative_analysis.md`
- `writing/blogpost_draft_v3.md`
