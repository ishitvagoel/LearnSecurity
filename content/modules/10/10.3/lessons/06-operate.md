# 10.3 — Cloud, containers, Kubernetes, and IaC (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST SP 800-190; Kubernetes security guidance; ASVS V13/V15. K8s is optional in prod, required as a *model* here.

## Property (start here)

A pod requesting cluster-admin must be denied. Workload identity is least privilege (3.3 at cluster grain), not “our namespace is private.”

## Attacker capabilities and trust assumptions

- **Attacker:** Compromised app container; malicious helm chart.
- **Trust:** Local pod_ok(role).
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | admission_denied. |
| Signal (no bodies) | cluster_admin_denied. |
| Revoke / recover | Rotate cluster creds. |
| Residual | Break-glass admin with E6. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/10.3/10.3-lab`.

## Transfer

Serverless IAM *.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
