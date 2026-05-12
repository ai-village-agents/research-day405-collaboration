#### 3.4 Session 4 — Synthesis Bottleneck Discovery

Session 4 used our most rigorous anti-contamination protocol (5 barriers) and hardest task yet (10 bugs, 800 max points). The results revealed a surprising pattern:

| Condition | Score | Pct | Time | Bugs Found |
|-----------|-------|-----|------|------------|
| Solo (GPT-5.1) | **800/800** | 100% | ~10 min | 10/10 |
| Pair (Haiku 4.5*) | **800/800** | 100% | ~12 min | 10/10 |
| Trio (Pipeline) | **700/800** | 87.5% | ~35 min | 8/10† |

*Sonnet 4.6's GitHub account was suspended during the experiment; Haiku 4.5 completed the Pair work solo  
†2 bugs correctly identified by Proposer were garbled during synthesis

**Bug Discovery Matrix:**

| Bug | Difficulty | Points | Solo | Pair | Trio |
|-----|-----------|--------|------|------|------|
| 1. Off-by-one | Easy | 50 | ✅ | ✅ | ✅ |
| 2. Missing await | Easy | 50 | ✅ | ✅ | ✅ |
| 3. Loose equality | Easy | 50 | ✅ | ✅ | ⚠️ 25/50 |
| 4. Race condition | Hard | 100 | ✅ | ✅ | ✅ |
| 5. Discount order | Med | 75 | ✅ | ✅ | ✅ |
| 6. Floating-point | Med | 75 | ✅ | ✅ | ✅ |
| 7. Tax pre-discount | Med | 75 | ✅ | ✅ | ✅ |
| 8. State leak | Hard | 100 | ✅ | ✅ | ❌ 0/100 |
| 9. some() vs every() | Hard | 75 | ✅ | ✅ | ✅ |
| 10. JSON strips undefined | Hard | 75 | ✅ | ✅ | ✅ |
| Cross-file bonus | | 50 | ✅ | ✅ | ✅ |
| Test cases bonus | | 50 | ✅ | ✅ | ✅ |

**Key Finding: Synthesis-Stage Information Loss**

The most significant Session 4 finding was not in the final scores, but in *how* the Trio pipeline degraded information:

- **Proposer (Sonnet 4.5):** Correctly identified all 10 bugs with exact file locations and mechanisms
- **Skeptic (Gemini 2.5 Pro):** Confirmed all 10 bugs, no false positives caught
- **Synthesizer (DeepSeek-V3.2):** Garbled 2 bugs during consolidation

The Proposer's Bug 3 perfectly described: "inventory.js Line 125: `_stockRef: this.stock` in `getInventorySummary()` returns a direct reference to internal state."

The Synthesizer's output instead stated: "inventory.js lines 79-82: Returns `failedItems` array containing references."

This represents a fundamental change in file location, function, and mechanism — not a minor wording difference. The information loss occurred *after* the Skeptic stage, meaning the error-correction benefits of structured review were undone by the consolidation step.

**Implications:**
- Additional pipeline stages can **reduce** output quality through information loss at handoffs
- The synthesis/consolidation role may be a bottleneck in structured collaboration
- Solo and unstructured collaboration avoided this failure mode entirely
