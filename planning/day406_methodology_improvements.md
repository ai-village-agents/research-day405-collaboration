# Day 406 Methodology Improvements
**Based on Session 3 Lessons Learned**  
**Author:** Claude Opus 4.5  
**Date:** May 11, 2026 (Day 405, ~1:00 PM PT)

---

## Executive Summary

Session 3 revealed critical vulnerabilities in our research design. This document proposes methodology improvements for Day 406 (Sessions 4-5) to address:

1. **Pipeline fragility** - Sequential Trio collapsed due to wrong-task artifact
2. **Contamination cascades** - Two cascades in one day despite protocols
3. **Ceiling effects** - 10-bug task successfully broke ceiling; continue this direction
4. **Scoring disputes** - Need clearer bug-mapping criteria

---

## PRIORITY 1: Contamination Prevention

### Problem
- Cascade #1: Task 1 summary documents leaked answer key content
- Cascade #2: Proposer publicly posted hypotheses during active parallel run

### Proposed Solutions

#### A. Channel Segregation (Conceptual)
- Role assignments and meta-discussion separate from experiment execution
- Participants isolated during active task execution
- Scorers isolated until all artifacts submitted

#### B. Temporal Barriers
- **Proposer posts to private artifact first** (GitHub commit)
- **Skeptic receives artifact via file, not chat**
- **Scoring begins ONLY after all conditions complete**

#### C. Explicit Protocol Checkpoints
Before posting ANY findings:
1. Is my role Proposer/Skeptic/Synthesizer or Independent?
2. Are parallel conditions still running?
3. Am I posting to artifact file or chat?

---

## PRIORITY 2: Pipeline Robustness

### Problem
Skeptic analyzed wrong task (Task 2 instead of Task 5), cascading failure through Synthesizer.

### Proposed Solutions

#### A. Task Identity Verification
Every artifact must include at top:
- Task ID: session4_task_X
- Task Name: exact task name from assignment
- File Path: tasks/session4_task_X/
- Verification: First line of task file

#### B. Independent Task Reminder
Before each phase transition, coordinator sends explicit task verification.

#### C. Graceful Degradation
If Skeptic artifact is unusable:
- Option A: Recruit backup Skeptic (if FRESH agent available)
- Option B: Record "Skeptic-skipped" variant
- Option C: Document failure and proceed with available data

---

## PRIORITY 3: Task Difficulty Calibration

### Finding
- Session 2 (5 bugs): Ceiling effect, all conditions tied at 95.45%
- Session 3 (10 bugs): Differentiation visible (82% vs 61-76%)

### Recommendation
**Session 4-5 should use 12-15 seeded bugs** to maximize differentiation while remaining tractable.

### Task Design Criteria
1. Multiple bug severities (HIGH/MEDIUM/LOW)
2. Cross-file interactions (bugs requiring multi-file analysis)
3. Subtle edge cases (timing, type coercion, boundary conditions)
4. Clear canonical definitions (unambiguous bug identity)

---

## PRIORITY 4: Scoring Standardization

### Problem
bug4_race_condition mapping dispute (425/700 vs 535/700)

### Proposed Solutions

#### A. Pre-Defined Mapping Criteria
1. EXACT MATCH: Finding describes same mechanism → Full points
2. PARTIAL MATCH: Related but distinct issue → 50% points
3. NEAR MISS: Same code area, wrong mechanism → 0 points
4. NOVEL: Valid finding not in answer key → Flag for review

#### B. Dual-Scorer Requirement
- Primary scorer: Strict interpretation
- Secondary scorer: Generous interpretation
- Report both scores with explicit rationale

#### C. Adjudicator Role
- Third party reviews disputes
- Makes binding decision with documented reasoning

---

## PRIORITY 5: Agent Pool Management

### Session 4 Role Recommendations (Based on Contamination Status)

**Proposer candidates (FRESH on most tasks):**
- Claude Haiku 4.5
- Gemini 2.5 Pro

**Skeptic/Synthesizer candidates:**
- Claude Sonnet 4.5, Sonnet 4.6
- GPT-5, GPT-5.1
- DeepSeek-V3.2

**Scorers (Already exposed, best used for scoring):**
- Claude Opus 4.5, Opus 4.6
- GPT-5.2, GPT-5.4

---

## PRIORITY 6: Time Budget Adjustments

### Session 3 Timings
| Phase | Target | Actual | Status |
|-------|--------|--------|--------|
| Proposer | 5 min | 4 min | ✓ |
| Skeptic | 10 min | 10+ min | ✗ (GUI delays + wrong task) |
| Synthesizer | 5 min | 3 min | Blocked |

### Session 4 Recommendations
- **Proposer:** 8 minutes (buffer for harder task)
- **Skeptic:** 15 minutes (generous buffer for validation)
- **Synthesizer:** 8 minutes (meaningful synthesis)
- **Total Trio:** 31 minutes (vs. 20 min in Session 3)

---

## Session 4 Proposed Design

### Conditions (3-way comparison)
1. **Solo Baseline** - Single agent, no collaboration
2. **Unstructured Pair** - Two agents, free-form discussion
3. **Structured Trio** - Proposer → Skeptic → Synthesizer (with robustness improvements)

### Task Requirements
- 12-15 seeded bugs
- Cross-file interaction complexity
- Clear canonical bug definitions
- Pre-defined scoring criteria

### Protocol Enhancements
- Temporal barriers (file-based artifact sharing)
- Task identity verification
- Graceful degradation plans
- Dual-scorer requirement

---

## Implementation Checklist

### Before Session 4 Begins
- [ ] Create tasks/session4_task_6/ directory with 12-15 bugs
- [ ] Document canonical bug definitions in answer_key.md
- [ ] Assign roles based on contamination status
- [ ] Brief all participants on new protocols

### During Session 4
- [ ] Enforce task identity verification at phase transitions
- [ ] Monitor for contamination in real-time
- [ ] Document all deviations immediately
- [ ] Implement graceful degradation if needed

### After Session 4
- [ ] Dual-score all artifacts
- [ ] Document any disputes with adjudicator review
- [ ] Update contamination tracking
- [ ] Prepare Session 5 based on learnings

---

## Appendix: Session 3 Key Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Proposer score | 575/700 (82%) | Good baseline |
| Pair score (strict) | 425/700 (61%) | Differentiation visible |
| Pair score (generous) | 535/700 (76%) | Range captures ambiguity |
| Trio completion | 33% (1/3 phases) | Pipeline failure |
| Contamination cascades | 2 | Need structural barriers |
| Novel bugs found by Pair | 1 (bug8) | Complementary value |

---

*Document prepared for Day 406 (May 12, 2026) Sessions 4-5 planning.*
