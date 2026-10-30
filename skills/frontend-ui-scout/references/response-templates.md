# Reporting templates

Adapt to task size. Stay concise for small tweaks; include enough evidence for nontrivial UI decisions.

## Recommendation only

**Task:** [goal and constraints]

**Inspected:** [existing UI or code; external pages actually opened]

| Candidate | Exact demo / code URL | Strength | Tradeoff | Status |
|---|---|---|---|---|
| [A] | [verified URL] | [fit] | [risk] | [inspected/docs only/unverified] |
| [B] | [verified URL] | [fit] | [risk] | [...] |

**Recommended:** [choice], because [task and design system rationale].

**Integration guidance:** [how to adapt if user chooses to implement].

**Unknowns:** [licenses, code access, browser limitations, etc.].

## Implementation completed

**Goal and outcome:** [one-sentence user benefit]

**Chosen design / implementation:** [specific source or local pattern and why]

**Changes:** [files, visual/behavior changes, new dependencies]

**References:** [exact URLs and what was taken from each: inspiration or reusable code]

**Verification performed:** [commands run; breakpoints and interactions tested]

**Remaining risks or unverified checks:** [honest disclosures]

## Blocked research

"I checked the existing project, but couldn't access live external pages. These are **directory leads, not verified components**: [URLs]. I can still [local work performed]. I did not verify current licenses, examples or compatibility."

Never replace `[verified URL]` with a guessed or non-existent slug. Use an actual homepage labeled as a directory if that is all you have.
