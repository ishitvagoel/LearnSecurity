# 10.3 — Cloud, containers, Kubernetes, and IaC (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** NIST SP 800-190; Kubernetes security guidance; ASVS V13/V15. K8s is optional in prod, required as a *model* here.

## Property (start here)

A pod requesting cluster-admin must be denied. Workload identity is least privilege (3.3 at cluster grain), not “our namespace is private.”

## Attacker capabilities and trust assumptions

- **Attacker:** Compromised app container; malicious helm chart.
- **Trust:** Local pod_ok(role).
Review `labs/10.3/10.3-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/10.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): cluster-admin on app SA
- Seeded smell (label it yourself): Privileged: true
- Seeded smell (label it yourself): No admission test
- Seeded smell (label it yourself): IaC with 0.0.0.0/0

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Namespace equals tenant
- Managed K8s is secure by default
- Containers are VMs

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Serverless IAM *.
