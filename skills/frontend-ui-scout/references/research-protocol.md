# Research protocol

Use this protocol for standard and deep discovery. Do not require it for every small CSS change.

## Define the brief

Extract from the task and repository: target page/component, audience, expected action, stack/framework versions, style/tokens, current UX problems, mobile constraints, accessibility/performance expectations, permission to implement, and budget/license constraints. Infer known facts rather than asking the user to repeat them.

## Query strategy

1. Identify categories in `SKILL.md` and open only matching resource directories.
2. Start with a handful of promising sites and search for the *requested component type* (e.g. `calendar scheduling React accessible`, `sports statistics data table`, `hero scroll parallax`), not generic 'beautiful UI'.
3. Locate the exact component page or working demo, then find installation docs or source. For visual-only inspiration, label it **reference only**.
4. Cross-check source claims against official docs/code, GitHub issue history where relevant, and recent developer feedback. Prefer maintained libraries; don't confuse stars or hype with suitability.
5. Stop when a clear best fit is established. Expand search if no candidate meets the task's design and technical gates.

## Candidate evidence record

Capture one compact row per candidate:

| Field | Record |
|---|---|
| Name and exact component | Specific, not only library |
| Demo URL | URL verified to exist if browsing available |
| Code/docs URL | Source, instructions, and version info |
| Status | Inspected live / docs only / unverified |
| Implementation | Framework, language, styling, packages, runtime cost |
| Rights | License/terms and any attribution requirements, or unknown |
| UX | Keyboard, touch, semantics, screen reader, reduced motion, states |
| Design | Fit with existing typography, tokens and brand |
| Performance | Initial load, animation/render cost, responsiveness |
| Verdict | Adopt / adapt / inspiration-only / reject, with reason |

Mark observed findings as observed, documentation statements as claimed by docs, and visual judgments as opinions. **Never say a demo worked unless it was actually tested.**

## Source hierarchy

1. Existing repository code and project guidelines determine implementation constraints.
2. Official vendor documentation, source code and live demos establish technical behavior.
3. Real shipped product examples establish UX/design patterns, not reuse rights.
4. GitHub activity, issues and developer/social discussions help identify risks but may be anecdotal.
5. Catalog summaries are search leads and can be outdated.

## Research depth

- **Quick**: reuse local pattern; zero external candidates is acceptable.
- **Standard**: 2–4 specific candidates; seek two independent relevant sources when possible.
- **Deep**: 4–6 specific candidates, and a real app/flow example where appropriate.
- **Blocked browsing**: do not fabricate specificity; provide provisional leads and proceed from local materials if possible.

## Prompts for browser-capable agents

- "Find a component with accessible keyboard interaction and responsive layout for [job], preferably in [stack]. Return exact demos, docs, licenses and source links."
- "Compare the details of [candidate A] and [candidate B] against the existing [components/...] and [tokens]. Identify integration costs and blockers."
- "Find 2–3 examples of a real shipped [product flow] to improve information hierarchy; treat them as UX inspiration rather than copyable implementation."
