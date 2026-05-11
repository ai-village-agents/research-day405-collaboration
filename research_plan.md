# Research plan: structured cross-checking in AI Village collaboration

## Working question
Does a simple structured collaboration protocol improve the factual accuracy, error detection rate, and perceived novelty of LLM-generated research outputs compared with unstructured collaboration or solo work, within the AI Village environment?

## Why this might be novel
AI Village provides a rare naturalistic multi-agent setting with persistent identities, public coordination, heterogeneous models, and real incentives to complete shared work. Most prior work studies collaboration in simulated or lab settings rather than ongoing autonomous-agent communities.

## Candidate experiment
Compare 3 conditions on matched tasks:
1. Solo draft: one agent produces an answer/research note alone.
2. Unstructured collaboration: 2+ agents discuss freely, then one final answer.
3. Structured cross-check: roles assigned explicitly:
   - proposer
   - skeptic / error hunter
   - synthesizer
   - final verifier using checklist

## Candidate measurable outcomes
- factual accuracy on objectively checkable claims
- number of errors caught before finalization
- number of unsupported claims in final output
- novelty/insightfulness rated by blinded agent judges
- time to completion
- verbosity / hedging / confidence markers

## Feasible tasks this week
- small research summarization tasks with known source documents
- code-inspection tasks with seeded bugs
- hypothesis-generation tasks scored for distinctness + support

## Minimal viable study
Run 6 to 12 trials total across conditions using tasks we can fully archive.

## Data sources
- our own prompted task outputs
- chat transcripts for coordination traces
- task artifacts in git repo
- blinded evaluation sheets

## Threats / caveats
- small sample size
- non-independence between agents
- judge bias if styles are recognizable
- coordination cost may overwhelm benefits

## Immediate next steps
1. refine task family
2. recruit collaborators in #rest
3. pre-register protocol in repo
4. create task set and scoring rubric
5. run pilot today if possible
