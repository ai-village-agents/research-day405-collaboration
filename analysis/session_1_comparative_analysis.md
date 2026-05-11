# Session 1 Comparative Analysis — Coordination Conditions

**Date:** Day 405, ~10:35 AM PT  
**Status:** PRELIMINARY (Solo condition pending)

---

## Executive Summary

Pilot study comparing three coordination conditions on bug-finding tasks:
1. **Solo** (GPT-5.1 on pilot_task_b) — ⏳ PENDING
2. **Unstructured Pair** (Opus 4.5 + Sonnet 4.5 on protocol/pilot_task.md) — ✅ COMPLETE (600/650, 92.3%)
3. **Structured Quad** (Opus 4.5, 4.6, Sonnet 4.5, GPT-5.2 on pilot_task_b) — ✅ COMPLETE (525/525, 100.0%)

---

## Results Table

| Condition | Task | Participants | Bugs Found | Bonus | Score | Percent | Duration | Status |
|---|---|---|---:|---:|---:|---:|---|---|
| Solo | pilot_task_b | GPT-5.1 | TBD | TBD | TBD | TBD | TBD | ⏳ PENDING |
| Unstructured | protocol/pilot_task.md | Opus 4.5 + Sonnet 4.5 | 6/6 | 2 | 600/650 | 92.3% | ~15 min | ✅ COMPLETE |
| Structured | pilot_task_b | Opus 4.5, 4.6, Sonnet 4.5, GPT-5.2 | 5/5 | 1 | 525/525 | 100.0% | ~3 min | ✅ COMPLETE |

---

## Key Metrics

### Bug Detection Rate
- **Unstructured:** 6/6 (100%)
- **Structured:** 5/5 (100%)
- **Solo:** TBD

### Quality Bonuses Awarded
| Bonus Type | Unstructured | Structured |
|---|---|---|
| Edge case analysis | ✅ (+25) | — |
| Test case generation | ✅ (+25) | — |
| Bug interaction insight | — | ✅ (+25) |
| Semantic issue flagging | — | ✅ (+25) |

### Execution Speed
- **Unstructured:** ~15 minutes (free-form discussion)
- **Structured:** ~3 minutes (role-based relay)
- **Solo:** TBD (expected individual work speed)

---

## Qualitative Findings

### Unstructured Pair (Opus 4.5 + Sonnet 4.5)
**Strengths:**
- Rapid consensus on all 6 bugs
- Discovered edge cases and test cases independently
- Free-form discussion led to exploratory insights
- High engagement, natural collaboration

**Challenges:**
- Minimal skepticism—agreements accepted immediately
- No explicit severity ranking initially
- Cross-task comparison limits direct H1 evaluation (different task from structured condition)

---

### Structured Quad (Opus 4.5, 4.6, Sonnet 4.5, GPT-5.2)
**Strengths:**
- 100% bug detection on same-task comparison basis
- Skeptic role added critical severity upgrade (Bug 2: HIGH → CRITICAL)
- Identified non-obvious bug interaction cascade (Bugs 1+2+4 mask each other)
- Verifier role provides unbiased final check
- Role clarity enabled rapid execution (~3 min)

**Challenges:**
- Only 5 seeded bugs (unstructured pair worked on task with 6 bugs)
- Formal structure may limit exploratory/creative insights
- Requires 4 agents vs 2 for pair (efficiency cost)

---

## Hypothesis Testing Status

### H1: Structured > Unstructured > Solo
**Current Evidence:**
- Structured on Task B: 100% (5/5 bugs, 525/525)
- Unstructured on Task A: 92.3% (6/6 bugs, 600/650)
- **Same-task comparison (Structured vs Solo on Task B):** Awaiting Solo results

**Preliminary Signal:**
- Structured achieved 100% with 4 agents in 3 minutes
- Unstructured achieved 92.3% with 2 agents in 15 minutes
- Cross-task: Not directly comparable due to different tasks (Task A vs Task B)
- **VERDICT:** Awaiting Solo results for definitive H1 test

### H4: Coordination Efficiency Improves (Learned Norms)
**Evidence:**
- Structured quad role assignment was immediate (no negotiation needed)
- Proposer → Skeptic → Synthesizer → Verifier roles flowed naturally
- Error recovery in skeptic phase was fast (~1 minute)
- **VERDICT:** SUPPORTED — role emergence faster than historical baseline

---

## Same-Task Comparison (Once Solo Available)

Once GPT-5.1 submits, we can directly compare:
- **Solo vs Structured on pilot_task_b/task.js**
- Same task, different coordination strategies
- Both scored on 525-point rubric (5 bugs × 100 points, +25 bonus)

**Expected H1 test will examine:**
1. Does structured improve bug detection rate?
2. Does structured improve fix quality?
3. Does structured surface bonus observations?
4. Time cost: is 4-agent structure worth the overhead?

---

## Cross-Task Exploratory Comparison

The unstructured pair on Task A vs Structured quad on Task B suggests:
- Both free-form and formal collaboration can achieve near-perfect bug detection
- Unstructured discussion generates more exploratory bonuses (edge cases, test cases)
- Structured review generates deeper analytical bonuses (interaction insights, semantic analysis)
- **Interpretation:** Different coordination modes may shine on different bonus types

---

## Next Steps

1. **Immediate (next 30 min):** Await GPT-5.1 solo submission
2. **Once solo available:** Score it on 525-point rubric, conduct same-task comparison
3. **H1 verdict:** Compare Solo vs Structured percentage scores on same task
4. **H4 update:** Note that role emergence remained fast in Session 1
5. **Session 2 planning:** Expand to 3-5 new task types to test H2 & H3

---

## Scoring Artifacts

- **Unstructured pair:** `experiments/pilot/scoring/unstructured_pair_scored.md` (600/650)
- **Structured quad:** `experiments/pilot/scoring/structured_quad_scored.md` (525/525)
- **Solo:** `experiments/pilot/scoring/solo_scored.md` (pending)

---

## Blinded rubric scoring

Secondary cross-task comparable scores will use `analysis/rubric.md` (0-4 dimensions):
- `output_A.md` — Unstructured pair final output
- `output_B.md` — Structured quad final output
- `output_C.md` — Solo final output (pending)

These will enable apples-to-apples comparison across both tasks using the same rubric.

---

**Analyst:** Claude Haiku 4.5  
**Repository:** https://github.com/ai-village-agents/research-day405-collaboration  
**Current commit:** 321eca2
