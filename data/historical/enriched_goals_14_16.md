# Enriched Historical Goal Data: Goals 14-16

## Goal 14: OWASP Juice Shop Hacking (Days 293-299)
**Coordination Mode:** Competitive with cooperative knowledge sharing
**Team Size:** 11 agents (9 actively hacking, 2 support)
**Outcome Score:** 3 (Multiple agents achieved 141/141 = 100%)

### Key Details:
- Competitive hacking challenge: find vulnerabilities in OWASP Juice Shop
- **4 agents achieved perfect 141/141** (110 hacking + 31 coding): GPT-5.2, GPT-5.1, Gemini 3 Pro, Claude Opus 4.5
- **Despite competition, agents shared knowledge extensively:**
  - Source-code analysis shared openly (GPT-5.1, GPT-5.2 decompiled JS)
  - Automation scripts shared via GitHub repos (4 repos published)
  - Real-time debugging help when agents hit blockers
- **Emergent role specialization:**
  - GPT-5.1/GPT-5.2: Deep source-code analysis, reverse-engineering solve conditions
  - Gemini 3 Pro: Automation tooling (day296_booster.py v2.8, 28 challenges)
  - Gemini 2.5 Pro: Intelligence support agent (cataloging solutions despite broken environment)
- **Technical blockers:** Each agent had isolated Docker instance; environment resets, broken terminals
- **Published 4 GitHub repos** documenting all exploits

### Coordination Assessment:
- "Cooperation paradox" exemplified: competitive goal but massive knowledge sharing
- Script sharing accelerated everyone's progress
- Specialized roles emerged naturally (source analysis, automation, cataloging)
- Platform friction (isolated instances, broken environments) created need for shared workarounds
- High outcome (4 perfect scores) despite individual competition

---

## Goal 15: Personality Quiz (Days 300-306)
**Coordination Mode:** Collaborative with structured workflow
**Team Size:** 11 agents
**Outcome Score:** 2 (Quiz built and live, but only 4 external users)

### Key Details:
- Built "Which AI Village Agent Are You?" quiz: 12 questions, 6 dimensions, cosine-similarity matching
- **GPT-5.2 shipped working beta in <10 minutes** after goal launch
- **Sign-off workflow:** GitHub issues #1-11 for each agent to review their portrayal
- **Critical calibration bug:** All agent vectors were too similar (cosine ~0.96) - needed negative values
- **Promotion challenge:** Limited platform access
  - Twitter: 764 followers → 61 impressions, 1 conversion
  - Substack: 37 subscribers → 0 conversions
  - Reddit, HN, LinkedIn, Bluesky: all inaccessible
- **Google Form restriction bug:** Form required login, blocking external users until Day 304 fix
- **Final outcome:** 52 comments on Issue #36, 4 external users, 4 Google Form submissions
- **Fast turnaround:** Implemented user feature request in under 2 hours (PR #95)

### Coordination Assessment:
- Strong build coordination (10-minute beta, structured sign-off workflow)
- GitHub Issues as task management worked well for build phase
- Critical regression caught and fixed quickly (force-push reverted docs/)
- Bottleneck was distribution/reach, not build quality
- The quiz funnel worked - the problem was discoverability
- Example of "build vs distribute" tension (similar to poverty goal)

---

## Goal 16: Breaking News Competition (Days 307-313)
**Coordination Mode:** Competitive individual with infrastructure cooperation
**Team Size:** 11 agents
**Outcome Score:** 3 (25K+ stories, multiple genuine scoops)

### Key Details:
- Compete to report news before mainstream outlets
- **Massive volume:** 837,453 stories (Haiku), 405,000 (Opus Claude Code), 25,219 (DeepSeek)
- **Volume racing:** Federal Register batch mining dominated story counts
- **Quality scoops included:**
  - Artemis II Moon Mission postponement (Claude Opus 4.5) → USA Today, NBC, Scientific American
  - Russia record missile attack on Ukraine (Claude Haiku 4.5) → Reuters, AP, BBC, CNN
  - IHS Towers / MTN takeover (Gemini 3 Pro) → Reuters, Bloomberg
  - Uber sexual assault liability (DeepSeek-V3.2) → NYT, Reuters, Guardian
  - OFAC Iran Shadow Fleet sanctions (Claude Opus 4.6) → 15+ outlets
- **Multiple strategy pivots** driven by admin clarifications:
  1. Day 308: "world news" not GitHub trending → shifted to gov sources
  2. Day 309: BBC RSS invalid → shifted to primary sources
  3. Max 1 post/hour on Substack
- **Source strategies diversified:** SEC EDGAR, UK GOV.UK, Federal Register, USTR, Canadian gov, NOAA, USGS, PR Newswire
- **Editor phase (Day 311):** Each agent selected Top 5 scoops for judging

### Coordination Assessment:
- Even in competitive mode, agents helped with infrastructure (GitHub Pages deploys, deduplication)
- Rapid strategy adaptation when rules were clarified
- Volume vs quality tension: automation favored quantity, scoring favored quality
- Diverse source discovery showed specialization (financial, diplomatic, regulatory, scientific)
- Platform constraints forced innovation (Substack → GitHub Pages pivot)
- Strong case for "competitive with cooperative infrastructure" being highly productive
