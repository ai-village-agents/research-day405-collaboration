# Glossary & Key Terms

A reference guide to statistical, methodological, and research-specific terms used in this study.

---

## Statistical & Measurement Terms

### Cohen's d (Effect Size)
**Definition:** A standardized measure of the difference between two group means, expressed in units of standard deviation.

**Formula:** d = (M₁ - M₂) / SD_pooled

**Interpretation:**
- d < 0.2: Negligible effect
- 0.2–0.5: Small effect
- 0.5–0.8: Medium effect
- d > 0.8: Large effect

**Example from this study:** Cohen's d = -1.24 (Solo vs. Structured) = **Large effect favoring Solo** (solo scores ~1.24 SD higher)

---

### Coefficient of Variation (CV)
**Definition:** A standardized measure of relative variability, expressed as a percentage. CV = (Standard Deviation / Mean) × 100

**Why it matters:** Allows comparison of consistency across different scales. A task where scores range 0–100 can be compared fairly with one where scores range 0–800.

**Example from this study:**
- Solo agents: CV = 3.9% (highly consistent; scores cluster tightly around the mean)
- Structured teams: CV = 7.2% (1.8× more variable; some teams perform well, others poorly)

**Interpretation:** Solo performance is more predictable; Structured performance is less reliable.

---

### Confidence Interval (CI)
**Definition:** A range of values that likely contains the true population parameter, calculated from sample data.

**Standard:** 95% CI means we're 95% confident the true value falls within this range.

**Formula:** CI = Mean ± (1.96 × Standard Error)

**Example:** If Session 5 Solo mean = 93.8% with 95% CI [88.2%, 99.4%], we're 95% confident the true Solo mean is between 88.2% and 99.4%.

**Note:** Overlapping confidence intervals between conditions suggest differences may not be statistically significant.

---

### Standard Deviation (SD) & Variance
**Definition:** Measures how spread out scores are around the mean.

- **Variance:** Average of squared deviations from the mean
- **Standard Deviation:** Square root of variance (more interpretable)

**Example:** 
- If Solo scores are 516, 518, 515, mean = 516.3, SD ≈ 1.3 (tightly clustered)
- If Structured scores are 442, 390, 510, mean = 447.3, SD ≈ 60 (widely spread)

**Implication:** Lower SD = more consistent performance; higher SD = less predictable.

---

### p-value (Statistical Significance)
**Definition:** The probability of observing a result as extreme as (or more extreme than) what we observed, assuming the null hypothesis is true.

**Standard threshold:** p < 0.05 (5% chance of false positive)

**Interpretation:**
- p < 0.05: Result is "statistically significant" (unlikely due to chance)
- p ≥ 0.05: Result may be due to chance; insufficient evidence to reject null hypothesis

**Example from this study:**
- Session 5 gap (93.8% vs 80.4%): Large observed difference, but p ≈ 0.30 (not statistically significant)
- **Why?** With only 2 conditions and limited replication, we lack the statistical power to reach p < 0.05 despite the large observed gap

**Important note:** Large effects can be non-significant; small sample sizes reduce power.

---

### Null Hypothesis (H₀)
**Definition:** The assumption that there is NO meaningful difference between groups (e.g., Solo = Structured).

**Alternative Hypothesis (H₁):** There IS a meaningful difference (e.g., Solo ≠ Structured).

**Hypothesis testing:** We try to *reject* the null hypothesis. If we can't reject it, we say the difference is "not statistically significant."

---

## Methodological Terms

### Blind / Blinded Scoring
**Definition:** Scorers evaluate submissions without knowing which condition produced them (Solo, Pair, Structured).

**Why it matters:** Prevents scorer bias. Scorers can't unconsciously favor one condition (e.g., assuming longer submissions = better).

**Implementation in this study:** Scorers received only the submission text and rubric; they never saw metadata like agent identity or collaboration mode.

---

### Contamination
**Definition:** When information about one experimental condition leaks to another, biasing the comparison.

**Examples:**
- Agent A learns about Agent B's solution strategy before working on their own task
- Agent C overhears the task details for Session 5 and uses that knowledge in Session 4
- Scorers know which condition produced a solution before scoring

**Risk:** Contamination can artificially inflate one condition's performance, invalidating the comparison.

**Prevention:** The five-barrier anti-contamination protocol (chat silence, task-ID checksums, Skeptic pre-briefs, pipeline timeouts, scorer spoiler avoidance).

---

### Ceiling Effect
**Definition:** When most or all participants achieve near-maximum scores, making it impossible to distinguish between conditions.

**Example:** Sessions 1-2 had easy tasks where all agents scored 525/550. Solo and Structured both hit the ceiling, so no meaningful comparison was possible.

**Solution:** Use harder tasks to create score variance and reveal differences between conditions.

---

### Handoff
**Definition:** The point where work transfers from one agent to another in a pipeline (e.g., Proposer → Skeptic → Synthesizer).

**Risk:** Information can be lost, garbled, or misunderstood during handoffs.

**This study's findings:** Two failure modes emerged at handoffs:
1. **Information loss** (Session 4): Synthesizer lost ~20% of upstream findings
2. **Error propagation** (Session 5): Proposer incorporated Skeptic errors uncritically

---

### Replication
**Definition:** Independently repeating a study using the same methods to verify whether findings are robust.

**Types:**
- **Direct replication:** Same task, same agents, same conditions
- **Conceptual replication:** Same research question, but different task domain or agent population

**Why it matters:** Single studies can be flukes. Replication builds confidence in findings.

**This study's status:** Exploratory pilot (5 sessions); future work should replicate and extend.

---

### Role (in structured collaboration)
**Definition:** An assigned position in a pipeline with specific responsibilities.

**Roles in this study:**
- **Proposer:** Develops initial solution
- **Skeptic (Critic):** Reviews solution, identifies issues, provides feedback
- **Synthesizer:** Integrates feedback into a revised solution
- **Verifier:** Quality checks final output (or is external scorer)

---

### Rubric
**Definition:** A scoring guide that specifies what correct and incorrect answers look like.

**Components:**
- List of items to evaluate (e.g., "correctly identified critical bug")
- Scoring scale for each item (e.g., 0-100 points)
- Exemplars (example answers showing different quality levels)

**Example from this study:**
- Full solution = 100 points
- 80% solution = 80 points
- 50% solution = 50 points
- Incorrect/irrelevant = 0 points

---

### Sample Size (N)
**Definition:** The number of observations or participants in a study.

**Impact on power:** Larger samples give more statistical power (better ability to detect real effects).

**This study's limitation:** 5 sessions with 2–4 conditions each gives N = 4–20 per condition, limiting statistical power. Future work should expand to 20+ sessions.

---

## Study-Specific Terms

### Synthesis Degradation (Session 4 Failure Mode)
**Definition:** Information loss when a third agent (Synthesizer) consolidates feedback from an upstream agent (Skeptic).

**What happened:** 
- Proposer identified 10 bugs correctly
- Skeptic confirmed 10/10 bugs correctly
- Synthesizer integrated findings but garbled 2/10 (80% retention)
- Final score: 87.5% instead of 100%

**Root cause:** Cognitive load during third-party consolidation under time pressure.

**Implication:** Pipeline handoffs introduce inherent failure points.

---

### Error Propagation (Session 5 Failure Mode)
**Definition:** When incorrect information from one agent is uncritically incorporated by another, embedding errors in the solution.

**What happened:**
- Skeptic provided 3 valid insights + 2 factual errors
- Proposer incorporated ALL feedback without re-verification
- Final score: 80.4% instead of 93.8%
- Gap: ~13%, comparable to Session 4 despite different cause

**Root cause:** Time pressure reduces verification capacity; errors and insights propagate equally.

**Implication:** Verification mechanisms needed at EACH handoff, not just downstream.

---

### H5b Hypothesis (Split Finding)
**Definition:** Originally Hypothesis 5 predicted "synthesis bottleneck is root cause of performance gap." But the finding split into two parts:

- **H5b-Retention:** ✅ SUPPORTED — Eliminating synthesis stage did improve retention (121.4% vs 80%), showing the bottleneck exists
- **H5b-Quality:** ❌ NOT SUPPORTED — But eliminating synthesis didn't close the performance gap (still -13.4%), revealing a different bottleneck (error propagation)

**Meta-insight:** Eliminating one bottleneck reveals another. Pipeline handoffs are inherent failure points regardless of design variation.

---

### Validator Effect
**Definition:** A strong historical finding that teams with **designated validators** (agents assigned to check quality) recovered from errors 100% of the time, vs. 17% without validators.

**Implication:** Oversight matters. Even if structure doesn't maximize quality, having someone explicitly responsible for catching mistakes is valuable.

---

### Solo Consistency
**Definition:** Solo agents showed remarkably low variability across sessions (CV = 3.9%), suggesting individual agents are more predictable than structured teams.

**Interpretation:** If you know a solo agent's baseline capability, you can predict performance fairly accurately. Structured teams are less predictable—configuration matters a lot.

---

## Historical Analysis Terms

### Coordination Mode
**Definition:** The level of formal structure in how a team organized itself across a historical goal.

**Categories:**
- Competitive/Individual (no collaboration)
- Parallel Individual (agents work separately on the same goal)
- Unstructured Collaboration (agents work together informally)
- Semi-Structured (some roles, some informality)
- Structured (explicit roles, formal process)

---

### Role Emergence Timing
**Definition:** When during a goal did agents naturally assume distinct roles?

**Examples:**
- **Day 1:** Roles were pre-assigned (structured from start)
- **Day 2-3:** Roles emerged naturally (agents discovered who was good at what)
- **Mid-goal:** Roles became more defined after initial chaos
- **Never:** Team remained unstructured throughout

---

## Experimental Conditions

### Solo
**Definition:** One agent working independently, with no collaboration.

**Timeline:** 15 minutes per task

**Typical result:** Highest quality, most consistent (CV = 3.9%)

---

### Unstructured Pair
**Definition:** Two agents collaborating freely without assigned roles.

**Timeline:** ~30 minutes total

**Typical result:** Tied with Solo on easy tasks; less consistent on hard tasks

---

### Structured Quartet / Structured Trio / Modified Pipeline
**Definition:** Multiple agents with explicit roles and sequential handoffs.

**Timeline:** 4 × 15 min = 60 min (pipelined, not sequential)

**Variations:**
- **Quartet:** Proposer → Skeptic → Synthesizer → Verifier
- **Trio (S4):** Proposer → Skeptic → Synthesizer (no separate verifier)
- **Modified Trio (S5):** Proposer → Skeptic → Proposer Revision (no synthesis agent; original proposer revises)

**Typical result:** Lower quality than Solo, high variability (CV = 7.2%)

---

## Citation & Reference Terms

### Canonical Source
**Definition:** The primary, most reliable version of a document.

**In this study:**
1. docs/blogpost.md (primary narrative)
2. docs/research_at_a_glance.md (quick reference)
3. docs/index.html (web version)
4. GitHub raw URLs (fresher than cached versions)

**Rule:** If a secondary document conflicts with the blogpost, treat blogpost as canonical.

---

### Commit Hash
**Definition:** A unique identifier for a specific version of the repository.

**Format:** 7-40 character alphanumeric string (e.g., `0d6a1b0`)

**Why it matters:** You can refer to the exact state of the repo at a given point in time.

**Example:** "As of commit 0d6a1b0, the research at a glance document was updated."

---

### Raw URL (GitHub Raw Content)
**Definition:** A direct link to the raw text file on GitHub, useful for citing specific versions.

**Format:** `https://raw.githubusercontent.com/ai-village-agents/research-day405-collaboration/main/docs/filename.md`

**Advantage:** Always shows the latest `main` branch version (freshest)

**Alternative:** Commit-pinned URL like `https://raw.githubusercontent.com/ai-village-agents/research-day405-collaboration/0d6a1b0/docs/filename.md` (shows state at that commit, never changes)

---

## Quick Reference Table

| Term | Definition | Example |
|------|-----------|---------|
| **Cohen's d** | Standardized effect size (units of SD) | d = -1.24 (Solo >> Structured) |
| **CV** | Relative variability (%) | Solo CV = 3.9% (consistent) |
| **p-value** | Probability of chance result | p = 0.30 (not statistically sig.) |
| **Blind scoring** | Scorers don't know condition | Prevents bias |
| **Contamination** | Info leakage between conditions | Five-barrier protocol prevents |
| **Ceiling effect** | Scores max out | Sessions 1-2 (easy tasks) |
| **Handoff** | Work transfer between agents | Proposer → Skeptic = handoff point |
| **Rubric** | Scoring guide with criteria | Defines what "correct" means |
| **Synthesis degradation** | Info loss during consolidation | Session 4: 20% loss |
| **Error propagation** | Errors embedded by uncritical acceptance | Session 5: 2 skeptic errors → final output |
| **H5b** | Split hypothesis: retention ✅, quality ❌ | Revealed different bottleneck |
| **Validator effect** | Teams with QA agents catch mistakes | 100% vs 17% error recovery |

---

**Last Updated:** May 13, 2026  
**Repository:** https://github.com/ai-village-agents/research-day405-collaboration  
**License:** CC BY 4.0

