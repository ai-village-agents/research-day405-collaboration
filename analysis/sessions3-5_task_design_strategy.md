# Sessions 3–5 Task Design Strategy

## 1. Why Sessions 1–2 Hit a Ceiling
- **Perfect scores masked differences.** Session 1 (`analysis/session_1_comparative_analysis.md`) and Session 2 (`analysis/session2_full_comparison.md`) both ended with all conditions at ~95–100% rubric scores (e.g., 525/525 on Pilot Task B), confirming a ceiling effect.
- **Bug inventory was too shallow.** Each task packed a finite set of self-contained defects. Any competent solo agent could enumerate them without deep synthesis, so structured workflows could not generate additive quality.
- **Single-module scope limited interaction effects.** Most defects lived within one file or function. Cross-module reasoning—and therefore coordination advantages—was rarely required.
- **Specifications were deterministic.** Rubrics rewarded finding enumerated bugs, not weighing ambiguous requirements, so there was minimal room for judgment or divergent strategies.

## 2. Design Principles for Harder Tasks
- **Multi-file, interdependent systems.** Require analysis across services/modules (API contract + client + tests). Include version drift or inconsistent interface assumptions that force cross-file reconciliation.
- **Subtle interaction bugs.** Seed issues that only emerge when multiple components interact (e.g., caching layers + feature flags + async jobs). Force synthesis of partial clues from separate files.
- **Ambiguous or incomplete specs.** Provide product notes that leave room for interpretation (e.g., conflicting stakeholder requests). Agents must justify a chosen interpretation and assess risk.
- **Performance vs. correctness tradeoffs.** Include decisions where naïve fixes improve correctness but regress latency or footprint. Reward exploration of Pareto-optimal options.
- **Security/adversarial thinking.** Hide vulnerabilities (e.g., auth bypass, injection via complex serialization) that require threat modeling, not just static linting.
- **Process evidence matters.** Tasks should incentivize validation steps (profiling, simulation, scenario testing) so structured roles can exhibit differentiated behaviors.

## 3. Candidate Tasks for Sessions 3–5

| Session | Concept | Core Challenge | Estimated Difficulty* |
|---------|---------|----------------|-----------------------|
| 3 | **Distributed feature flag regression** | Diagnose a rollout failure where a backend service, React frontend, and analytics job disagree on flag states after a partial deployment. Requires tracing state propagation, versioned schemas, and stale cache invalidation. | 8/10 |
| 4 | **Secure async job queue audit** | Audit a task worker processing untrusted payloads. Subtle deserialization and sandbox escape bug spans queue config, worker code, and policy docs. Agents must balance correctness hardening with throughput guarantees. | 9/10 |
| 5 | **Spec reconciliation for payments refactor** | Merge two divergent design memos and partial code branches (API + billing microservice + mobile client). Performance budget conflicts with PCI compliance. Success demands synthesizing ambiguous requirements and proposing a justified plan. | 9/10 |

*Difficulty scale is relative to Sessions 1–2 (which scored 5/10 or lower). Values reflect anticipated effort for a strong solo agent; structured teams should gain leverage at 8+.

## 4. Rubric Updates Emphasizing Depth
- **Layered scoring dimensions:**  
  - *System understanding (0–150 pts):* Evidence of mapping inter-module dependencies, data flows, and failure modes.  
  - *Insight generation (0–200 pts):* Identification of interaction bugs, threat vectors, or tradeoff analyses beyond surface defect lists.  
  - *Decision quality (0–150 pts):* Justified recommendations addressing ambiguity, including explicit tradeoff evaluation.  
  - *Validation rigor (0–100 pts):* Quality of testing, simulation, or adversarial checks performed.  
  - *Communication clarity (0–50 pts):* Structured reasoning artifacts (tables, timelines, risk matrices) enabling reviewer confidence.
- **Partial credit for exploration.** Award points for disproven hypotheses when agents document investigative steps, encouraging breadth.
- **Penalty for unexamined assumptions.** Deduct when agents ship fixes without checking downstream consumers or side effects.
- **Bonus for risk-weighted prioritization.** Encourage ranking findings by impact/severity, not raw count.

## 5. Predicted Impact on Structure vs. Unstructured Modes
- Harder, ambiguous tasks should expose **coordination leverage**: structured roles will split discovery (proposer), adversarial probing (skeptic), synthesis (synthesizer), and validation (validator) in ways solo agents cannot parallelize.
- Depth-weighted rubrics turn **process advantages into points**, allowing structured teams to capitalize on richer analysis even if bug counts tie.
- Security/performance tradeoffs and spec reconciliation require **negotiating conflicting evidence**, a scenario where structured dialogue historically shines.
- By forcing cross-file synthesis, we expect structured teams to maintain quality while **solo/unstructured agents incur oversight gaps**, revealing the structural value that Sessions 1–2 obscured.
