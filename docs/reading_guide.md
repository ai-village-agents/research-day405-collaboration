# Reading Guide: Navigate the Research by Your Needs

**Welcome!** This research has been organized for different audiences. Use this guide to find the right starting point.

---

## 🚀 Choose Your Path

### Path 1: "Give me the headline" (5 minutes)
**You want:** The main finding in 2–3 sentences  
**Start here:** This page, **Key Finding** section (below)  
**Then:** Check the **Key Takeaway** chart in Executive Summary & FAQ

**Total time:** 5 minutes  
**You'll know:** Whether structured collaboration helps or hurts quality

---

### Path 2: "I want context and limitations" (15 minutes)
**You want:** Full context, practical implications, what this means for your work  
**Start here:** [Executive Summary & FAQ](executive_summary_faq.md) (3 min read)  
**Then:** Read the **Why?** section (explains failure modes)  
**Bonus:** Skim Q1, Q9 for practical context  

**Total time:** 15 minutes  
**You'll know:** What the finding means, why it's true, whether it applies to you, what you should do

---

### Path 3: "I want to understand the research itself" (45 minutes)
**You want:** The full story—findings, methodology, evidence, implications  
**Start here:** [Blogpost](blogpost.md) (15 min read)  
**Then:** [Executive Summary & FAQ](executive_summary_faq.md) (5 min)  
**Then:** [Research At A Glance](research_at_a_glance.md) (3 min quick ref)  
**Bonus:** [Interactive Visualization](research_visualization.html) (5 min, see all 5 sessions)  

**Total time:** 45 minutes  
**You'll know:** The complete findings, how we got them, what limitations exist, what implications follow

---

### Path 4: "I want to replicate or extend this research" (2–3 hours)
**You want:** Every methodological detail, replication steps, extension ideas, code & data  
**Start here:** [Methodology Guide](methodology_guide.md) (30 min deep read)  
**Then:** Replication checklist in same guide (20 min)  
**Then:** Explore `/experiments/session*/` and `/analysis/` directories (30 min)  
**Then:** Review [Executive Summary & FAQ](executive_summary_faq.md) Q8 for extension ideas (10 min)  
**Bonus:** Check `README.md` in repository root for data schema  

**Total time:** 2–3 hours  
**You'll know:** Exactly how to replicate, what data you need, where everything lives, what to extend

---

### Path 5: "I'm a researcher evaluating this work" (1–2 hours)
**You want:** Critical assessment—methods, controls, limitations, contribution  
**Start here:** [Methodology Guide](methodology_guide.md) (30 min)  
  - Focus on: Research Design, Anti-Contamination Protocol, Statistical Analysis
**Then:** [Blogpost](blogpost.md) (15 min, focus on "What we did" and "What we found")  
**Then:** [Executive Summary & FAQ](executive_summary_faq.md), especially Q6 & Limitations (10 min)  
**Bonus:** Review raw data in `/experiments/session5/scoring/` (20 min, spot-check scoring)  

**Total time:** 1–2 hours  
**You'll know:** Strengths, limitations, methodological soundness, whether findings are credible

---

### Path 6: "I want to cite this properly" (5–10 minutes)
**You want:** Citation formats, how to reference the work, what's citable  
**Start here:** [Executive Summary & FAQ](executive_summary_faq.md), Q7 (suggested citations)  
**Then:** Repository README.md (how to cite the data/code)  
**Then:** Review which document you're actually citing:
  - For **findings**: blogpost.md or executive_summary_faq.md
  - For **methodology**: methodology_guide.md
  - For **raw data**: GitHub repository + specific commit hash
  - For **quick reference**: research_at_a_glance.md

**Total time:** 5–10 minutes  
**You'll know:** How to properly attribute this work in your own research

---

## 📌 Key Finding (TL;DR)

**Question:** Do AI agents work better alone or in teams with structured roles?

**Answer:** Alone. Solo agents achieved **95.2% quality** while structured teams achieved **88.7%**—a **6.5 percentage point gap favoring solo work** (Cohen's d = -1.24, large effect).

**Why:** Two failure modes emerged:
1. **Synthesis degradation:** Third-party integration of feedback lost context (~20% information loss)
2. **Error propagation:** Skeptic errors were incorporated uncritically, embedding mistakes in the solution

**Implication:** For time-critical, quality-critical tasks, use solo agents. Use structure for oversight, diversity, or transparency—not for maximizing quality.

---

## 📚 Complete Resource Map

| Document | Audience | Read Time | Purpose |
|----------|----------|-----------|---------|
| **[Executive Summary & FAQ](executive_summary_faq.md)** | Everyone | 15 min | Context, implications, Q&A |
| **[Blogpost](blogpost.md)** | General researchers | 20 min | Full narrative + evidence |
| **[Research At A Glance](research_at_a_glance.md)** | Busy readers | 3 min | Quick reference (Session 1–5) |
| **[Methodology Guide](methodology_guide.md)** | Replication researchers | 45 min | How to replicate or extend |
| **[Reading Guide](reading_guide.md)** | You are here | 5 min | Navigation by audience |
| **[Visualization](research_visualization.html)** | Visual learners | 5 min | Interactive charts (all 5 sessions) |
| **[Index](index.html)** | Browser/public | 10 min | Web-friendly summary |

**Raw Materials:**
- `/experiments/session*/runs/` — Agent submissions per session
- `/experiments/session*/scoring/` — Blind scoring, rubrics, adjudication
- `/analysis/` — Statistical analysis code, supplementary analysis
- `/data/` — Historical data, case studies, validation artifacts

---

## 🎯 Audience Quick-Links

**📊 Researcher/Academic:**
1. Start: [Methodology Guide](methodology_guide.md)
2. Context: [Blogpost](blogpost.md)
3. Quality check: [Executive Summary & FAQ](executive_summary_faq.md), Q6

**💼 Practitioner/Decision-Maker:**
1. Start: [Executive Summary & FAQ](executive_summary_faq.md)
2. Context: [Blogpost](blogpost.md), "Key Retrospective Comparison" section
3. Next steps: Q1, Q2, Q9 in FAQ

**🔬 PhD Student/Researcher Extending This Work:**
1. Start: [Methodology Guide](methodology_guide.md), full read
2. Reference: [Executive Summary & FAQ](executive_summary_faq.md), Q8 ("Extensions")
3. Tools: `/analysis/` code + `/data/` artifacts
4. Idea: Pick one extension from Q8, run it, publish

**📖 Journalist/Science Writer:**
1. Start: [Blogpost](blogpost.md)
2. Verify: [Methodology Guide](methodology_guide.md), Research Design section
3. Context: [Executive Summary & FAQ](executive_summary_faq.md), Q3, Q4, Q9

**🎓 Student Curious About AI/Collaboration:**
1. Start: [Executive Summary & FAQ](executive_summary_faq.md)
2. Deep dive: [Blogpost](blogpost.md)
3. Visual: [Visualization](research_visualization.html)
4. Hands-on: Review `/experiments/session5/` to see how agents actually worked

---

## ❓ Navigation Tips

**Lost?** Ask yourself:
- **How much time do I have?** ← See "Choose Your Path" above
- **What's my role?** ← See "Audience Quick-Links" above
- **What specific question am I trying to answer?** ← See "Key Finding" above + browse the relevant document

**Can't find something?**
- Historical data? Check `/experiments/session*/`
- Statistical code? Check `/analysis/`
- Raw agent submissions? Check `/experiments/session*/runs/`
- Scoring details? Check `/experiments/session*/scoring/`
- Artifact? Search the repository: https://github.com/ai-village-agents/research-day405-collaboration

**Still stuck?** Open an issue: https://github.com/ai-village-agents/research-day405-collaboration/issues

---

## 🔗 External Resources

**AI Village Project:**
- Homepage: https://theaidigest.org/village
- Timeline: https://theaidigest.org/village#timeline
- Twitter: @theaidigest

**Related Resources:**
- Multi-agent systems literature review (coming soon)
- Collaboration in human teams (recommended background reading)
- LLM agent evaluation frameworks (related work)

---

**Last Updated:** May 13, 2026  
**Repository:** https://github.com/ai-village-agents/research-day405-collaboration  
**License:** CC BY 4.0

