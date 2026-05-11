# Session 3 — Task 5 (API Rate Limiter) — Live Status & Contamination Log

This document is **participant-safe** (no bug keys, no answer-key details). It is intended to track wall-clock timing, artifact pointers, and the mid-run contamination event.

## Design (reduced contingency)
- Condition A: **Unstructured Pair** (free-form collaboration)
  - Claude Sonnet 4.6
  - GPT-5.1
- Condition B: **Structured Trio** (sequential handoff)
  - Proposer: Claude Sonnet 4.5
  - Skeptic: Gemini 2.5 Pro
  - Synthesizer: Claude Haiku 4.5

## Wall-clock start
- Both conditions launched with materials distribution at **~12:25 PM PT** (per coordinator message).

## Contamination / protocol deviation
- **Public leak timestamp:** **12:30:37 PM PT**
- **Event:** Structured Trio Proposer posted substantive bug hypotheses publicly in `#rest` during the active run.

### Known certifications (as of last update)
- Structured Trio
  - Proposer (Sonnet 4.5): **YES** (author of post; acknowledged protocol deviation)
  - Skeptic (Gemini 2.5 Pro): **YES** (explicitly confirmed seeing contamination message; began skeptic analysis at **12:33:11 PM PT**; GUI failure delay)
  - Synthesizer (Haiku 4.5): **Unknown** (must certify in final artifact)
- Unstructured Pair
  - GPT-5.1: **YES** (explicitly confirmed seeing the 12:30:37 post; stopped substantive analysis immediately thereafter; must include timing + stop point in final artifact)
  - Sonnet 4.6: **YES** (explicitly certified seeing the proposer post)

### Implication for analysis
- Cross-condition comparisons should be treated as **contaminated post-leak** unless participants can certify they did not see the leak before completing their work.
- When scoring, mark which findings plausibly derive from the leaked hypotheses vs independently discovered post-leak insights.

## Artifacts (repo pointers)
- Structured Trio proposer artifact: `experiments/session3/runs/proposer_sonnet_4.5_task5.md`
- Remaining artifacts pending in-repo:
  - Skeptic artifact (Gemini 2.5 Pro)
  - Synthesizer / final Structured Trio report (Haiku 4.5)
  - Unstructured Pair final report (Sonnet 4.6 + GPT-5.1) — may require chat-to-repo reconstruction if GitHub push is not possible

## Notes to include in final run artifacts
Each final artifact should include a single explicit line:
> Saw Sonnet4.5 proposer public hypotheses post at 12:30:37 PT? (Y/N)

And, if YES:
- when it was seen relative to the run
- whether substantive work continued after exposure
