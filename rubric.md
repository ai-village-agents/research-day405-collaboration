# Evaluation Rubric for AI Village Collaboration Study

This rubric is applied to de-identified final outputs only. Judges must not see condition labels (solo/unstructured/structured), participant identities, or timestamps during scoring.

## Judge Instructions (Blinded Scoring)
1. Score each output independently using the 0-4 scales below.
2. Use task packet references/answer keys for factual checks; do not infer facts not in evidence.
3. Record short evidence notes for each non-max score.
4. Do not discuss scores with other judges before submission.
5. If uncertain between two scores, assign the lower score unless explicit evidence supports the higher one.

## Dimension 1: Factual Accuracy (0-4)
Operational definition: correctness of checkable factual claims in final output.

- 4: >=95% of checkable claims correct; no major factual error.
- 3: 85-94% correct; only minor factual errors.
- 2: 70-84% correct; at least one major or multiple minor errors.
- 1: 50-69% correct; several major errors.
- 0: <50% correct or factually unreliable overall.

Scoring rule:
- Let C = number of checkable claims, K = number correct.
- Accuracy rate = K/C when C >= 4.
- If C < 4, judge qualitatively but cite each claim.

## Dimension 2: Unsupported Claims (0-4)
Operational definition: claims presented as fact without support from provided sources, code evidence, or verifiable reasoning.

- 4: 0 unsupported claims.
- 3: 1 unsupported claim.
- 2: 2 unsupported claims.
- 1: 3 unsupported claims.
- 0: >=4 unsupported claims.

Notes:
- Speculative language is acceptable only if clearly labeled as speculation.
- Repeated versions of the same unsupported claim count once.

## Dimension 3: Error Detection Before Finalization (0-4)
Operational definition: extent to which output reflects correction of errors identified prior to final submission.

- 4: >=80% of available errors detected and corrected pre-finalization.
- 3: 60-79% detected/corrected.
- 2: 40-59% detected/corrected.
- 1: 20-39% detected/corrected.
- 0: <20% detected/corrected.

Scoring inputs:
- Use transcript metadata/error log to count opportunities.
- For seeded-bug tasks, denominator is seeded bug count.
- For source-summary tasks, denominator is planted discrepancy count or adjudicated error opportunities.

## Dimension 4: Novelty / Insight (0-4)
Operational definition: non-obvious, useful synthesis beyond surface restatement.

- 4: Multiple original, well-supported insights that change interpretation or decision quality.
- 3: At least one clear, useful non-obvious insight with support.
- 2: Mostly competent summary; limited new synthesis.
- 1: Largely derivative restatement with little added value.
- 0: No meaningful insight or misleading pseudo-insight.

## Dimension 5: Clarity (0-4)
Operational definition: organization, readability, and unambiguous communication of claims and evidence.

- 4: Clear structure, precise language, minimal ambiguity, easy to audit.
- 3: Generally clear with minor ambiguity or structure issues.
- 2: Mixed clarity; important points require interpretation.
- 1: Hard to follow; major ambiguity/organization problems.
- 0: Unclear to the point of unusable.

## Dimension 6: Completion Time (0-4)
Operational definition: speed to final output within session constraints.

- 4: <=15 minutes.
- 3: >15 to 25 minutes.
- 2: >25 to 35 minutes.
- 1: >35 to 45 minutes.
- 0: >45 minutes or not completed.

Time is scored from logged start/end timestamps by study lead, not by judges.

## Composite Metrics
1. Primary Quality Index (PQI):
   - `PQI = Accuracy + Unsupported + ErrorDetection`
   - Range: 0-12.
2. Secondary Quality Index (SQI):
   - `SQI = Novelty + Clarity`
   - Range: 0-8.
3. Efficiency-Adjusted Score (EAS):
   - `EAS = PQI + SQI + Time`
   - Range: 0-24.

## Adjudication Rules
1. Two blinded judges score each output.
2. If any dimension differs by >1 point, send to tie-break judge for that dimension.
3. Final dimension score:
   - If no tie-break needed: average of two judges (can be 0.5 increments).
   - If tie-break used: median of three scores.
4. Preserve all raw and adjudicated scores in archive.

## Data Entry Template (Per Output)
- Output ID:
- Task family:
- Judge ID:
- Accuracy (0-4):
- Unsupported Claims (0-4):
- Error Detection (0-4):
- Novelty/Insight (0-4):
- Clarity (0-4):
- Time Score (0-4):
- Evidence notes (1-3 lines per non-max dimension):
