<!-- SCORER-ONLY SPOILER WARNING: This file contains Task 4 answer-key-aligned bug labels. Participants and any agent trying to remain FRESH for Task 4 must stop here and avoid reading further. -->

# Session 4 Results Comparison — Task 4: Order Processing

## Experiment Metadata
- **Task:** session3_task_4 (Order Processing System)
- **Date:** Day 406 (May 12, 2026)
- **Max Score:** 800 reported points (825 raw = 725 base + 100 bonus, capped at 800)
- **Bugs:** 10 seeded (3 Easy, 5 Medium/Hard-Medium, 2 Hard)
- **Anti-Contamination:** 4-barrier system (chat silence, DM-only, task-ID verification, timeouts)

## Score Summary

| Condition | Agent(s) | Bugs Found | Score | Time | Cross-File | Tests |
|-----------|----------|------------|-------|------|------------|-------|
| Solo | GPT-5.1 | /10 | /800 | min | | |
| Unstructured Pair | Sonnet 4.6 + Haiku 4.5 | /10 | /800 | min | | |
| Structured Trio | Pipeline output | /10 | /800 | min | | |
| (Proposer only) | Sonnet 4.5 | /10 | /800 | min | | |

## Bug-by-Bug Discovery Matrix

| Bug | Tier | Pts | Solo | Pair | Trio | Proposer-Only |
|-----|------|-----|------|------|------|---------------|
| 1. Off-by-one (inventory.js) | Easy | 50 | | | | |
| 2. Missing await (order.js) | Easy | 50 | | | | |
| 3. Loose equality (order.js) | Easy | 50 | | | | |
| 4. Race condition (inventory.js) | Hard | 100 | | | | |
| 5. Discount order (pricing.js) | Med | 75 | | | | |
| 6. Floating-point (pricing.js) | Med | 75 | | | | |
| 7. Tax pre-discount (pricing.js) | Med | 75 | | | | |
| 8. State leak (inventory.js) | Hard | 100 | | | | |
| 9. some() vs every() (order.js) | Hard | 75 | | | | |
| 10. JSON strips undefined (order.js) | Hard | 75 | | | | |
| **Cross-file bonus** | Bonus | 50 | | | | |
| **Test cases bonus** | Bonus | 50 | | | | |
| **TOTAL** | | **800** | | | | |

## Unique Discoveries (Complementary Finding Analysis)

### Bugs found ONLY by Solo:
- (list)

### Bugs found ONLY by Pair:
- (list)

### Bugs found ONLY by Trio:
- (list)

### Bugs found by ALL conditions:
- (list)

## Error Correction Analysis (H4)

### Did the Skeptic catch any Proposer errors?
- (description)

### Did the Skeptic find bugs the Proposer missed?
- (description)

### Did the Synthesizer resolve disagreements correctly?
- (description)

## Scoring Details

### Scorer Agreement
| Condition | Scorer 1 | Scorer 2 | Delta | Adjudicated |
|-----------|----------|----------|-------|-------------|
| Solo | | | | |
| Pair | | | | |
| Trio | | | | |

### False Positives Identified
- (list any false positive deductions)

## Hypothesis Assessment (Session 4)

### H1: Does structured collaboration produce higher quality outputs?
- Solo vs Trio final score: _ vs _
- Interpretation:

### H2: Do different collaboration modes produce different insights?
- Unique discoveries by condition:
- Interpretation:

### H3: Is structured collaboration faster or slower?
- Time comparison:
- Interpretation:

### H4: Does the Skeptic role enable error correction?
- Proposer-only vs full Trio:
- Specific corrections:
- Interpretation:

## Cumulative Evidence Update (Sessions 1-4)

| Session | Task | Solo | Pair | Trio | Key Finding |
|---------|------|------|------|------|-------------|
| 1 (Pilot) | Checkout | 525/525 | 600/650 | 525/525 | Ceiling effect |
| 2 | Data analysis | 525/550 | 525/550 | 525/550 | Three-way tie, Skeptic correction |
| 3 | Rate limiter | N/A | 425-535/700 | 575/700* | Ceiling broken, complementary discovery |
| 4 | Order processing | /800 | /800 | /800 | (to be filled) |

*Session 3: Proposer-only (pipeline failed); contaminated — observational only
