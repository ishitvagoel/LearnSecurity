# 10.3 assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not finished | developing | competent | transfer-ready. Check-in 10 and M4 stay **not finished**.

## Module

Cloud, serverless, containers, Kubernetes, and IaC

## Evidence checklist

- [ ] Namespace vs ClusterRole map; PSS/NetworkPolicy labeled as not RBAC
- [ ] Transfer task (clinic app SA is cluster-admin; serverless IAM `*` named)
- [ ] Lab `labs/10.3/10.3-lab`: what must not happen: **app pod granted cluster-admin**
- [ ] `vulnerable/` deny tests fail, `fixed/` tests pass (authorized local practice files only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without secrets: `cluster_admin_denied`

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; “namespace / CIS / NetworkPolicy” slogans |
| Competent | System-specific rule; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/live-cluster/Gate-10 language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **10.3**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/10.3.md`.
