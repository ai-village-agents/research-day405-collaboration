# Session 4 Task 4 Scoring Template

**Scorer:** [YOUR NAME]
**Condition Being Scored:** [Solo / Pair / Trio]
**Date/Time of Scoring:** [TIMESTAMP]

## Scoring Rubric (800 points max)

### Easy Bugs (50 points each)
| Bug ID | Description | Found? | Points | Notes |
|--------|-------------|--------|--------|-------|
| Bug A | Off-by-one in inventory check | ☐ | 0/50 | |
| Bug B | Missing await on async operation | ☐ | 0/50 | |
| Bug C | Loose equality comparison | ☐ | 0/50 | |

### Medium Bugs (75 points each)
| Bug ID | Description | Found? | Points | Notes |
|--------|-------------|--------|--------|-------|
| Bug D | Discount application order | ☐ | 0/75 | |
| Bug E | Floating-point arithmetic | ☐ | 0/75 | |
| Bug F | Tax calculated on pre-discount price | ☐ | 0/75 | |
| Bug G | some() vs every() logic error | ☐ | 0/75 | |
| Bug H | JSON.stringify strips undefined values | ☐ | 0/75 | |

### Hard Bugs (100 points each)
| Bug ID | Description | Found? | Points | Notes |
|--------|-------------|--------|--------|-------|
| Bug I | Race condition in concurrent orders | ☐ | 0/100 | |
| Bug J | State reference leak (shared mutable) | ☐ | 0/100 | |

### Bonuses (50 points each)
| Bonus | Description | Awarded? | Points | Notes |
|-------|-------------|----------|--------|-------|
| Cross-file | Identified cross-file interaction bugs | ☐ | 0/50 | |
| Test cases | Provided meaningful test cases | ☐ | 0/50 | |

### Total Score
| Category | Points |
|----------|--------|
| Easy (3 × 50) | /150 |
| Medium (5 × 75) | /375 |
| Hard (2 × 100) | /200 |
| Bonuses (2 × 50) | /100 |
| **TOTAL** | **/800** |

## Scoring Notes
- Partial credit: Award if the agent identified the core issue even with imprecise description
- Strict matching: Bug must be correctly identified in the right file with the right mechanism
- Cross-reference: Check answer_key.md for canonical descriptions
- Record any novel bugs found that aren't in the answer key

## Novel Findings (Not in Answer Key)
| # | Description | File | Severity |
|---|-------------|------|----------|
| 1 | | | |

## Scorer Confidence
- [ ] High — clear mapping between submission and answer key
- [ ] Medium — some ambiguity in bug descriptions
- [ ] Low — significant interpretation needed
