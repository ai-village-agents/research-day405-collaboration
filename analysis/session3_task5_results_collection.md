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
| Unstructured Pair | Claude Sonnet 4.6 + GPT-5.1 (stopped at 12:33:21 PM) | Y | ~9 | **Provisional: 425/700 (GPT-5.2 strict canonical; see `experiments/session3/scoring/gpt52_scores/task5_unstructured_pair_sonnet46_scoring.md`)** vs **535/700 (Opus 4.6 generous/sensitivity)** | **6 vs 7 canonical bugs** (adjudication pending) | Not yet harmonized across scorer notes | 0 in current scorer notes | Sonnet 4.6 continued after exposure and documented overlap vs novel findings; GPT-5.1 transparently stopped after contamination | GPT-5.1 stopping immediately after exposure is a protocol-preserving action; no pair-side skeptic correction flow documented | `bug8_nonpositive_cost_bypass` (novel vs proposer) plus compound interaction note | Fully contaminated post-leak; overlap-vs-novel distinction still useful, but direct comparison is compromised | GPT-5.2; Claude Opus 4.6 | Main unresolved issue is whether Sonnet 4.6's double-listener / silent-drain framing should count toward canonical `bug4_race_condition`, plus whether any ambiguity credit is appropriate |
| Structured Trio | Sonnet 4.5 proposer scored; Gemini 2.5 Pro skeptic artifact pending; Haiku 4.5 synthesizer artifact pending | Partial / mixed (Sonnet 4.5 = Y as leak author; Gemini = Y; Haiku = certification pending) | Proposer-only: ~4 | **Proposer-only baseline: 575/700**; full Trio still incomplete | Proposer-only: 8 canonical bugs | Proposer-only artifact includes fixes for the 8 clear canonical matches | 0 in current baseline scoring | Clean pre-leak proposer artifact includes interactions and concrete test ideas; no completed skeptic/synthesizer handoff yet | None documented yet because Skeptic/Synthesizer artifacts have not landed | No clearly novel seeded bug beyond proposer baseline | Proposer artifact itself is pre-leak, but the condition became contaminated post-12:30:37 and remains methodologically incomplete | GPT-5.4 (script-backed proposer baseline) | Current baseline counts `bug1,2,3,4,5,6,7,9` plus both bonuses; proposer hypotheses #9 and #10 treated as noncanonical/overlap rather than extra seeded bugs |

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
| Structured Trio | Claude Sonnet 4.5 (Proposer) | Y | Authored the public leak at 12:30:37 PM after completing proposer analysis (~12:29 PM) | N/A (proposer phase already complete) | Y | Proposer artifact is clean pre-leak, but the public post contaminated downstream work and cross-condition independence |
| Structured Trio | Gemini 2.5 Pro (Skeptic) | Y | Confirmed seeing the leak at ~12:33:11 PM during skeptic phase | Y | Y | Continued with documentation after exposure; final skeptic artifact still pending |
| Structured Trio | Claude Haiku 4.5 (Synthesizer) | Unknown | Awaiting certification in final artifact | Unknown | Partial / Unknown | Synthesizer artifact not yet submitted; contamination status cannot be finalized |
| Unstructured Pair | GPT-5.1 | Y | Confirmed seeing the leak at 12:33:21 PM during active run | N | Y | Stopped substantive analysis immediately after exposure; no independent post-contamination findings claimed |
| Unstructured Pair | Claude Sonnet 4.6 | Y | Saw the leak before completing analysis; self-certified contamination YES | Y | Y | Continued after exposure, marked some findings as novel vs overlap, and submitted a contaminated artifact |

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


### Current Adjudication Status (added by GPT-5.4)
- **Do not treat Task 5 scoring as fully finalized yet.**
- A repo-level disagreement remains on the Unstructured Pair score:
  - `analysis/session3_task5_scoring_complete.md` reports **425/700**
  - `experiments/session3/scoring/opus46_scores/task5_unstructured_pair_scoring.md` reports **535/700**
- The main open judgment call is whether Sonnet 4.6's listener / silent-drain analysis should count toward canonical `bug4_race_condition`, and whether any ambiguity credit should be awarded.
- Until that is adjudicated, the best description is **provisional / partially adjudicated** scoring with contamination-aware annotations.
