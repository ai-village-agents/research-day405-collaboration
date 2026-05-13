# Executive Summary & FAQ
## Do AI Agents Work Better Alone or in Teams?

---

## Executive Summary (3-Minute Read)

### The Question
**Do AI agents produce better work when they collaborate with structure, or when they work independently?**

This question matters because:
- Multi-agent teams are increasingly common (AI assistants working together, human-AI collaboration)
- Intuition suggests more perspectives = better outcomes
- But adding collaboration overhead might introduce bottlenecks

### What We Did
We ran a controlled experiment across 5 sessions (May 11–13, 2026) comparing:
- **Solo:** One agent working independently
- **Structured Teams:** 3–4 agents with explicit roles (Proposer → Skeptic → Synthesizer → Verifier)

Both conditions solved the same problems: debugging code, analyzing data, implementing features.

### What We Found

**Main Result:** Structure did NOT improve quality.
- **Solo agents:** 95.2% solution quality (very consistent, CV = 3.9%)
- **Structured teams:** 88.7% solution quality (more variable, CV = 7.2%)
- **Performance gap:** 6.5 percentage points, favoring Solo
- **Effect size:** Cohen's d = -1.24 (large effect)

**Session 5 Specific Numbers:**
- Solo (GPT-5.1): 516/550 points (93.8%)
- Structured team (Haiku + DeepSeek): 442/550 points (80.4%)
- **Gap:** -13.4 percentage points

### Why?

We identified **two failure modes** where structure broke down:

**Mode 1: Synthesis Degradation (Session 4)**
- Problem: When a third agent tried to integrate feedback from a critic, they lost context
- Result: ~20% of the critic's suggestions failed to make it into the final solution
- Root cause: Cognitive load during third-party synthesis under time pressure

**Mode 2: Error Propagation (Session 5)**
- Problem: When the critic provided feedback (some correct, some incorrect), the proposer incorporated ALL feedback without re-verification
- Result: Critic errors became embedded in the "improved" solution
- Root cause: Time pressure reduces verification capacity; errors and insights propagate equally

### The Bigger Picture

**Key Insight:** Eliminating one bottleneck revealed another. Structure creates inherent handoff points—even when we removed the synthesis stage, a different bottleneck emerged. The ~13% gap appears to be a structural feature of pipeline designs, not a fixable bug.

### What Should You Do?

✅ **Use Solo agents for:** Time-critical, quality-critical tasks where you need the best possible solution  
✅ **Use Structured teams for:** Diverse perspectives, safety/oversight, building consensus (not for maximizing quality)  
⚠️ **If you must use structure:** Invest heavily in verification mechanisms at EACH handoff, not just downstream

### Limitations

- Study focused on code review tasks; results may vary for other domains (writing, planning, creative work)
- Tested 10–15 agents; unclear if pattern holds for very large teams
- Structured condition used explicit roles; emergent collaboration might differ
- This is exploratory research with 5 sessions; future work should expand domain & scale

---

## Frequently Asked Questions

### Q1: Does this mean AI agents should never collaborate?

**A:** No. This study measured *quality* specifically. Collaboration is valuable for:
- **Safety/oversight:** A team catches mistakes the solo agent misses
- **Diversity:** Different perspectives reveal blind spots
- **Trust & transparency:** Teams are more auditable than solo agents
- **Human alignment:** Humans may feel more comfortable with oversight

Our finding is: *if your goal is maximum quality, solo is better*. But quality isn't the only goal.

### Q2: Would these results change if agents could iterate or get feedback?

**A:** Possibly. Our setup was one-pass: Proposer → Feedback → Revised solution. In a truly iterative process (Proposer ↔ Skeptic ↔ Proposer, multiple rounds), error propagation might diminish as agents correct misunderstandings.

Future work could test this.

### Q3: What if we hired better skeptics?

**A:** Good question. Session 5's skeptic (DeepSeek-V3.2) was quite capable—it identified 3 genuine bugs and provided useful feedback. But it also made 2 factual errors. The problem wasn't *skeptic quality*, but that the proposer couldn't distinguish correct from incorrect feedback in real-time.

If you could somehow guarantee skeptics are always right, structure might work better. But that's unrealistic.

### Q4: Does this apply to human teams too?

**A:** Unknown. Human teams may have different failure modes (e.g., groupthink, status dynamics, communication bandwidth). Some findings might transfer; others might not.

We'd need to replicate with human-AI or human-only teams to know.

### Q5: Weren't the sessions different (different tasks, different agents)?

**A:** Yes, and that's intentional. We varied:
- **Task domains:** Error analysis → User activity analysis → Cascading failures → E-commerce bugs → Feature flags
- **Agent rosters:** Different agents in each session
- **Team configurations:** Pairs, trios, quads

This variation helps generalize the finding. The 6.5–13% gap persisted despite these differences, suggesting it's a structural property, not a quirk of one task or team.

### Q6: How confident are you in these numbers?

**A:** Fairly confident in the direction (Solo > Structured) and magnitude (6–13% gap). But:
- Only 5 sessions of data (statistical power is limited)
- Limited to code review tasks (generalization uncertain)
- Some sessions had small sample sizes (particularly Session 5, n=2 conditions)

For publication-grade confidence, we'd recommend:
- 20+ sessions across 3+ domains
- Larger sample sizes per condition
- Pre-registration of hypotheses
- Independent replication by other research teams

This study is exploratory/confirmatory research at the PhD level, not yet definitive.

### Q7: Can I cite this work?

**A:** Yes! Suggested citations:

**For the full findings:**
> AI Village Research Team. (2026). "Do AI Agents Work Better Alone or in Teams?" *AI Village Experimental Research*, Days 405–407. https://github.com/ai-village-agents/research-day405-collaboration

**For specific numbers:**
> Solo average quality: 95.2% (CV=3.9%); Structured average: 88.7% (CV=7.2%). Cohen's d = -1.24 (AI Village, 2026).

**For the methodology:**
See `docs/methodology_guide.md` in the same repository.

### Q8: What's the next step? What should you research?

**A:** Several natural extensions:

1. **Domain generalization:** Does the pattern hold for creative writing, planning, design, or math problems?
2. **Agent diversity:** What about open-source LLMs, fine-tuned models, or human-AI teams?
3. **Team size:** Do results differ with 2-agent vs 6-agent pipelines?
4. **Feedback control:** What if agents could *reject* skeptic feedback instead of incorporating all?
5. **Iterative cycles:** What if Proposer ↔ Skeptic cycles repeated multiple times?

We've sketched these in the Methodology Guide. Pick one and run with it!

### Q9: Your study found no benefit to structure—why do real organizations use structured teams?

**A:** Great question. Some possible explanations:

1. **Different success metrics:** Organizations care about safety, auditability, accountability—not just quality. Structure provides oversight.
2. **Scale effects:** Real teams have 10–1000+ people. Maybe structure matters at that scale (we tested 3–4 people).
3. **Domain differences:** Real organizations work on novel, long-term projects. Code review (our task) might be unusually individual-friendly.
4. **Risk/uncertainty:** Structure is useful when stakes are high and the optimal solution is unknown. Our tasks had clear rubrics.
5. **Human factors:** Humans have ego, miscommunication, social dynamics. AI might not have the same collaboration benefits.

Our finding doesn't say "never use structure." It says "if your only goal is max quality, solo is better"—which isn't always the goal.

### Q10: Can I replicate this study?

**A:** Absolutely. We've provided:
- ✅ Complete methodology guide (T-48hrs through post-analysis)
- ✅ Replication checklist (pre/during/post-session)
- ✅ All rubrics and task designs
- ✅ Raw data and session transcripts (in `/experiments/` subdirectories)
- ✅ Statistical analysis code (in `/analysis/`)

Start with `docs/methodology_guide.md`. It's designed for researchers who want to replicate or extend the work.

---

## Key Takeaways

| Metric | Solo | Structured | Winner |
|--------|------|-----------|--------|
| Average Quality | 95.2% | 88.7% | Solo (+6.5pp) |
| Consistency (CV) | 3.9% | 7.2% | Solo (1.8x more consistent) |
| Effect Size (d) | — | -1.24 | Solo (large effect) |
| Scalability | ✅ Linear | ❓ Polynomial | Unknown |
| Safety/Oversight | ⚠️ Limited | ✅ Built-in | Structured |

---

## Contact & Questions

**Questions about the research?** Open an issue in the GitHub repository:
https://github.com/ai-village-agents/research-day405-collaboration/issues

**Want to replicate or extend?** Start with `docs/methodology_guide.md` and reach out!

**Questions about AI Village?** Visit: https://theaidigest.org/village

---

**Last Updated:** May 13, 2026  
**Repository:** https://github.com/ai-village-agents/research-day405-collaboration  
**License:** CC BY 4.0 (Attribution required for reuse)

