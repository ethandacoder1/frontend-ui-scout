# Evaluation rubric and release quality gates

Do not let a numerical score override blockers or user constraints. Start with hard gates, then compare remaining choices qualitatively or with task-adjusted weights.

## Hard gates

Reject or hold a candidate if:

- Reuse is not permitted by the applicable license/terms, or rights are unknown and permission is required before integration.
- It would break required behavior, backend wiring, navigation, form handling, or critical accessibility interactions.
- It is incompatible with the project's environment without unjustifiable migration or risk.
- It imposes unacceptable performance, privacy, security, or ongoing cost.

An unknown license is **not** automatically permission to use code; seek a permissive alternative or keep it inspiration-only.

## Suggested weighting (adapt to task)

| Dimension | Default | Questions |
|---|---:|---|
| UX and visual fit | 25% | Clear hierarchy? Suits brand? Interesting without distraction? |
| Technical fit | 20% | Compatible stack and versions? Existing patterns reused? |
| Accessibility and usability | 20% | Keyboard/focus? Semantics? Touch? Contrast? Motion controls? |
| Performance and responsive behavior | 15% | Works on narrow screens? Efficient rendering? No disruptive layout shifts? |
| Source quality and maintenance | 10% | Inspectable and understandable code? Docs and recent issues? |
| Licensing and reusability | 10% | Rights documented? Attribution/cost acceptable? |

If scoring, label 0–5 values as subjective assessment and cite supporting evidence. Strong visual excitement alone never waives a hard gate.

## Visual craft review

A good result balances **personality, product utility, and quality of execution**:

- Clear typography scale, rhythm and intentional whitespace, not merely generic defaults.
- Polished layout and alignment at all relevant breakpoints.
- Coherent component design, with deliberate color, radius and elevation decisions.
- Useful feedback for hover, focus, active, loading, empty, disabled and error states.
- Microinteractions that make the interface feel alive but do not obstruct common tasks.
- Realistic data, realistic device shapes and real/appropriately licensed imagery if design examples require them.
- Avoid defaulting to AI-looking gradient blobs, neon glows, faux 3D objects, or obviously mismatched component styles.
- Also avoid over-correcting into a plain, personality-free interface when the goal calls for compelling design.

## Verification checklist

- [ ] Scope and existing behaviors preserved
- [ ] Desktop and mobile layout checked
- [ ] Keyboard flow and visible focus checked
- [ ] Semantics, labels and contrast reviewed
- [ ] Reduced-motion or motion-off handling considered
- [ ] Loading/empty/error/disabled states considered
- [ ] License/rights and dependency implications checked
- [ ] Relevant tests, lint and build run or limitations stated
- [ ] Exact source links and changes reported

Check only what you actually verified. Different tasks may require additional tests.
