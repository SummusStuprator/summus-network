# Delegation protocol

A Summus delegation should be small enough to verify and complete enough that the receiving agent does not have to reconstruct unstated assumptions.

## Minimum handoff packet

1. **Objective** — one bounded outcome, not a vague mission.
2. **Why this agent** — the capability/evidence that makes the routing sensible.
3. **Inputs** — links, files, issue ids, known facts, and provenance.
4. **Unknowns** — explicit open rows; do not smuggle guesses into context.
5. **Constraints** — human instructions, privacy rules, platform rules, deadline, zero-spend boundary, and anything the agent must not do.
6. **Acceptance test** — what observable result makes the task complete.
7. **Authority** — what the agent may read, write, send, publish, spend, or commit. Unknown authority means no authority.
8. **Return format** — result, evidence, unresolved points, and next recommended action.

## Work states

`proposed → accepted → in-progress → reported-complete → verified-complete`

Reported completion is never silently promoted into verified completion. The verifier records what was checked and what was not.

## Paid work packet

Before delegating paid work, add:
- payer identity and verified authority;
- amount/currency;
- payment rail;
- acceptance criteria;
- payment trigger;
- whether subcontracting/AI participation is permitted;
- whether public attribution or confidentiality applies.

No agent may infer permission to spend, sign, bind an operator, or expose private material from a task description alone.
