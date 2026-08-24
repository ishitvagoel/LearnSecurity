# 10.3 — Cloud, containers, Kubernetes, and IaC (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** NIST SP 800-190; Kubernetes security guidance; ASVS V13/V15. K8s is optional in prod, required as a *model* here.

## Property (start here)

A pod requesting cluster-admin must be denied. Workload identity is least privilege (3.3 at cluster grain), not “our namespace is private.”

## Attacker capabilities and trust assumptions

- **Attacker:** Compromised app container; malicious helm chart.
- **Trust:** Local pod_ok(role).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Serverless IAM *.

**Product sketch:** Clinic: app SA is cluster-admin.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | EKS default service account often too wide.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/10.3/10.3-lab` stays the only running system you may break.
