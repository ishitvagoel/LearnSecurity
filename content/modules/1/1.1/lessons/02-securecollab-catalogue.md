# 1.1-LO-02 — First invariant catalogue for SecureCollab

**Kind:** design-exercise  
**Loop step:** 2 Model

## Property

For the **Phase 1 product sketch** (organizations/tenants, users, notes, later files/sharing—not a running product yet), which outcomes are forbidden?

## Attacker / trust (minimum set)

- Public internet client, fully modified (hostile Next.js/browser).
- Honest-but-curious tenant member.
- Operator who can read logs and backups.
- Non-goal unless you say otherwise: nation-state against the cloud provider’s hypervisor.

Trust: application + database you will build; not the client; not “the scanner.”

## Task

Write `invariants-v1.md` (learner artifact) with:

1. Assets (notes, membership, later files—flag as future).
2. For at least five of the eight properties: invariant, attacker, trust, time horizon (session vs backup).
3. Explicit **non-goals**.
4. One line each: prevention, detection, recovery if prevention is not absolute.

Forbidden: a tool list; a copied textbook CIA definition; targeting a live site.

## Evidence

A reviewer can mark each line **testable** or **mechanism-claim**. Mechanism-claims must be rewritten.

## Transfer

If billing simulation is added (high-impact, still fake money), which new invariant appears?
