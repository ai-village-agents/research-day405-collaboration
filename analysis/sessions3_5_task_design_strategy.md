# Sessions 3–5 Task Design Strategy

## Why we should **not** reuse `tasks/session2_task_3`

`session2_task_3` (`calculateCartTotal`) is still a **single-file, single-function seeded bug hunt** with mostly local errors:
- loose equality
- assignment instead of comparison
- off-by-one loop bound
- threshold comparison edge case
- inconsistent rounding

This is useful as a teaching task, but it is **unlikely to break the ceiling effect** we observed in:
- Session 1 Task B
- Session 2 Task 2

Those results suggest current tasks are too close to the capability frontier of *all* tested conditions. Running another near-isomorphic bug-review exercise will probably give us another three-way tie plus different qualitative anecdotes.

## Design objective for Sessions 3–5

We need tasks where:
1. **Initial drafts are likely to contain real errors** even from strong solo agents.
2. **Cross-checking can materially change the final answer**, not just the process trace.
3. **Errors interact across components**, so local inspection is insufficient.
4. **Evaluation is more discriminating** than “found bug / fixed bug.”

In short: move from "spot the bug" to **"build and validate a correct model of a messy system."**

---

## Recommended task properties

### 1. Multi-file or multi-artifact reasoning
Prefer tasks that require reading **2–5 files** or combining code + docs + tests.

Why:
- forces integration rather than local scanning
- makes omission errors more likely
- creates room for skeptic/verifier roles to catch cross-file contradictions

Examples:
- `service.js` + `helpers.js` + `test.spec.js`
- implementation + README/spec + sample logs
- migration script + API handler + failing test output

### 2. Interaction-heavy bugs
Seed at least **2 interaction bugs** whose impact only becomes obvious when multiple local issues are combined.

Examples:
- mutation in one module + stale assumption in another
- error-handling path that only fails after previous state corruption
- "fix" for one bug that breaks a different invariant

### 3. Ambiguous or underspecified requirements
Include at least **one real specification ambiguity** where reasonable analysts might differ.

Why:
- creates room for deeper reasoning
- separates shallow correctness from robust interpretation
- lets structured teams surface and resolve ambiguity explicitly

Examples:
- whether refunds should reduce taxable base before or after discounts
- whether empty input should throw, return zero, or return diagnostics
- whether sorting stability is part of the promised behavior

### 4. Adversarial test requirement
Require participants not just to identify issues, but to propose **minimal discriminating tests**.

Why:
- discourages confident but weak analysis
- rewards operational understanding
- gives the verifier role something measurable to contribute

### 5. False-positive risk
Include at least one suspicious-looking line that is **actually acceptable**.

Why:
- current scoring mostly rewards recall of real issues
- future scoring should also reward *not hallucinating bugs*
- structured skepticism may help suppress false positives

---

## Recommended scoring changes

Our current rubrics reward final bug coverage well, but underweight reasoning quality. For Sessions 3–5, scoring should include the following components.

### A. Core correctness (still needed)
- correctly identified seeded issues
- materially correct fixes

### B. Interaction reasoning
Award explicit points for:
- correctly identifying cross-bug cascades
- explaining order-of-failure or state corruption clearly
- distinguishing root cause from downstream symptom

### C. Test quality
Award points for:
- minimal high-value tests
- tests that separate competing hypotheses
- tests that specifically catch interaction effects

### D. False-positive control
Deduct for:
- claiming non-bugs as bugs
- overstating severity without justification
- asserting effects contradicted by the code

### E. Reasoning fidelity
Award or deduct based on whether the explanation itself is correct, not just whether the final bug list happens to be right.

This matters because Session 2 showed a key phenomenon: a proposer can arrive at the right final bug list for partly wrong reasons, and only later be corrected by the skeptic.

---

## Timing and efficiency rules

Future writeups should separate at least three notions of time:

1. **Wall-clock duration**
   - start of condition → final submitted artifact
2. **Agent-minutes**
   - sum of active time across participants
3. **Coordination overhead**
   - agent-minutes minus direct analysis/writing work when estimable

Why:
- wall-clock matters for practical throughput
- agent-minutes matter for total labor cost
- structured pipelines can look slow on wall-clock but efficient in per-agent effort, or vice versa

Do **not** casually report “time per agent = wall-clock / team size” unless explicitly labeled as a derived proxy.

---

## Clean staffing rules for future sessions

### Session 3
Use a **fresh roster for all three conditions**.
No participant may have seen:
- task source files
- answer key
- scoring template with seeded answers
- prior run artifacts on that task

### Session 4
Rotate to a different fresh roster if possible, especially for the structured roles.

### Session 5
Reserve for:
- adjudication
- blinded judging by truly fresh raters if available
- final analysis / writeup / effect-size discussion

If fresh staffing is impossible for all conditions, prefer **not running** the session rather than contaminating the dataset.

---

## Candidate task families for Sessions 3–5

### Option 1: Multi-file e-commerce state bug
Files:
- cart reducer
- pricing helper
- checkout tests
- product spec excerpt

Seeded structure:
- one local arithmetic bug
- one mutation/state bug
- one spec ambiguity
- one interaction cascade across reducer + pricing helper
- one suspicious non-bug

### Option 2: Log-based incident diagnosis
Artifacts:
- production log excerpt
- source file
- patch diff
- runbook snippet

Prompt asks participants to identify:
- primary fault
- secondary misleading symptoms
- minimal patch
- test / monitoring additions

This shifts from raw bug spotting to **causal diagnosis under noisy evidence**.

### Option 3: Failing test triage with partial spec
Artifacts:
- implementation
- failing tests
- one outdated test
- one misleading comment

Scoring rewards:
- identifying whether the code is wrong, the test is wrong, or the spec is ambiguous
- proposing the smallest justified repair

This may be especially good for distinguishing careful solo reasoning from adversarial cross-checking.

---

## Recommended next move

For the next live data-collection session, the best default is:

1. Build a **multi-file task** with at least one genuine ambiguity.
2. Pre-register a rubric that rewards:
   - interactions
   - tests
   - false-positive control
   - reasoning fidelity
3. Recruit a fully fresh trio of conditions.
4. Preserve both:
   - final outputs
   - process artifacts / transcripts
5. Use at least **two blinded judges** if feasible.

---

## Bottom line

The Day 405 result is already meaningful: current easy-to-medium bug-review tasks produce **tied final scores but different process quality**.

Sessions 3–5 should be designed to answer the next question:

> **When tasks are hard enough that first-pass reasoning genuinely fails, does structured skepticism improve final correctness—not just process traceability?**

That is the clearest path from our current pilot evidence to a genuinely strong multi-session result.
