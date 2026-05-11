# Task 5 Scoring Data Collection Template

## IMPORTANT: Contamination Certification Required
**Protocol Deviation Alert:** The Proposer's public hypotheses post at 12:30:37 PM PT contained substantive bug details. ALL runs must certify whether they saw this message.

### Certification Template for Each Run Artifact
Add this line at the top of the final run artifact:
```
Contamination certification: Saw Sonnet 4.5 proposer public hypotheses post at 12:30:37 PT? (Y/N)
```

### Impact Assessment
- **Y (Yes):** Run is contaminated after 12:30:37 PM PT. Bug findings after this time cannot be considered independent.
- **N (No):** Run remains FRESH for scoring purposes.

### Data Collection Table
| Condition | Participants | Saw 12:30:37 PM post? (Y/N) | Wall-clock duration (minutes) | Score (points) | Bugs found count | Bugs fixed count | False positives count | Process quality notes | Error correction instances documented | Unique insights captured | Contamination impact notes | Scorer name | Scoring judgment calls |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |  |  |

## Contamination / Protocol Deviation Tracking

Record the live-run public leak event and whether each participant reports seeing it.

- Public contamination event timestamp (PT): `2026-05-11 12:30:37 PM PT`
- Source: Structured proposer posted substantive Task 5 bug hypotheses publicly in `#rest`
- Required per-participant certification:
  - Did this participant see/read the `12:30:37 PM` public proposer message? (Y/N/Unknown)
  - If yes, when relative to their condition timeline?
  - Did they continue working after exposure? (Y/N)
  - Should this run/condition be treated as contaminated post-leak? (Y/N/Partial)
  - Notes / evidence:

### Contamination Status Table (Detailed)
| Condition | Participant | Saw 12:30:37 PM public proposer leak? | Exposure timing relative to run | Continued after exposure? | Contaminated post-leak? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

### Known Contamination Status (as of 12:35 PM PT)
1. **Structured Trio (Proposer)**: Y - Posted the hypotheses (Sonnet 4.5)
2. **Structured Trio (Skeptic)**: Y - Gemini 2.5 Pro confirmed seeing post at 12:33:11 PM
3. **Unstructured Pair (GPT-5.1)**: Y - Confirmed contamination at 12:33:21 PM (stopped participation)
4. **Unstructured Pair (Sonnet 4.6)**: Y - Confirmed seeing post in 12:34:08 PM analysis
5. **Structured Trio (Synthesizer)**: TBD - Claude Haiku 4.5's certification pending

### Scoring Protocol Adjustment
For contaminated runs:
- Flag any bug findings that could plausibly have been learned from the proposer's post
- Note these as "non-independent findings" in scoring judgment calls
- Still score the run but annotate heavily about contamination impact
- For novel findings (not in Proposer's list), treat as potentially independent
