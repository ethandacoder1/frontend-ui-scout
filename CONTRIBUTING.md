# Contributing

Thanks for improving UI Scout. Favor a carefully selected, useful directory over a long, unverified collection.

## Updating a resource

1. Check the current official link, available demos and whether it still serves the category.
2. Edit the relevant file in `skills/frontend-ui-scout/references/`.
3. Keep entries concise and grounded in the resource's actual capabilities. Avoid time-sensitive numeric feature counts unless sourced and dated.
4. Don't claim that a license, pricing plan or component works without fresh evidence.
5. If adding a link, update the catalog counts in `README.md` and `scripts/validate_skill.py` (and the count described in the skill) in the same PR.
6. Run `python scripts/validate_skill.py`.

## Editing the agent procedure

- Keep `SKILL.md` small and actionable: task-first, research, evaluate, implement if authorized, verify.
- Use references for long catalogs and detailed procedures.
- Do not turn every frontend task into compulsory extensive browsing.
- Maintain the no-fabricated-research, rights, security and scope safeguards.

## Reporting issues

Include the resource URL, what changed, evidence when available, and the suggested replacement or correction. Do not include secrets or private project files.
