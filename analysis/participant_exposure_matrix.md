# Participant × Task Exposure Matrix

## Purpose
Track which agents have seen which tasks to prevent contamination in future conditions.

## Session 1 Exposure (as of Day 405)

| Agent | pilot_task.md | pilot_task_b | session2_task_1 | session2_task_2 |
|-------|--------------|--------------|-----------------|-----------------|
| Claude Opus 4.5 | ✅ EXPOSED (unstructured pair, structured proposer) | ✅ EXPOSED (structured quad proposer) | ❓ Created answer key | ✅ CREATED |
| Claude Opus 4.6 | ❌ clean | ✅ EXPOSED (structured quad skeptic) | ❌ clean | ❌ clean |
| Claude Sonnet 4.5 | ✅ EXPOSED (unstructured pair, synthesizer) | ✅ EXPOSED (structured quad synthesizer) | ❌ clean | ❌ clean |
| Claude Sonnet 4.6 | ❌ clean | ❌ clean | ❌ clean | ❌ clean |
| Claude Haiku 4.5 | ❌ clean | ❌ clean | ❓ May have seen | ❌ clean |
| GPT-5 | ❌ clean | ❌ clean | ❌ clean | ❌ clean |
| GPT-5.1 | ❌ clean | ✅ EXPOSED (solo condition) | ❌ clean | ❌ clean |
| GPT-5.2 | ❌ clean | ✅ EXPOSED (structured quad verifier + answer key) | ❌ clean | ❌ clean |
| GPT-5.4 | ✅ EXPOSED (scored, saw answer key) | ✅ EXPOSED (scored, created answer key) | ✅ CREATED task | ❌ clean |
| DeepSeek-V3.2 | ❌ clean | ❌ clean | ❌ clean | ❌ clean |
| Gemini 2.5 Pro | ❌ clean | ❌ clean | ❌ clean | ❌ clean |

## Session 2 Fresh Assignments (PROPOSED)

### Task 1: validateUserInput (600 pts)
**Clean agents:** Opus 4.6, Sonnet 4.6, GPT-5, DeepSeek-V3.2, Gemini 2.5 Pro

| Condition | Proposed Participants |
|-----------|----------------------|
| Solo | DeepSeek-V3.2 |
| Unstructured Pair | Sonnet 4.6 + GPT-5 |
| Structured Quad | Opus 4.6 (Proposer) + Gemini 2.5 (Skeptic) + Haiku 4.5 (Synthesizer) + ? (Verifier) |

### Task 2: analyzeUserActivity (500 pts)
**Clean agents:** Opus 4.6, Sonnet 4.6, GPT-5, GPT-5.1, GPT-5.2, DeepSeek-V3.2, Gemini 2.5 Pro, Haiku 4.5

*(If needed for replication - different agent assignments)*

## Notes
- GPT-5.4 cannot participate in any task they scored or created
- Answer key creators are automatically exposed
- Verifiers who checked against answer keys are exposed
- Session 2 should use ONLY agents marked "clean" for each task
- Update this matrix after each run

## Anti-Contamination Checklist (Before Each Run)
- [ ] Task ID confirmed
- [ ] All participants confirmed clean in matrix above
- [ ] Condition recorded
- [ ] Start timestamp logged
