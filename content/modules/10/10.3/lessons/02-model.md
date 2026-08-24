# 10.3 — Cloud, containers, Kubernetes, and IaC (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** NIST SP 800-190; Kubernetes security guidance; ASVS V13/V15. K8s is optional in prod, required as a *model* here.

## Property (start here)

A pod requesting cluster-admin must be denied. Workload identity is least privilege (3.3 at cluster grain), not “our namespace is private.”

## Attacker capabilities and trust assumptions

- **Attacker:** Compromised app container; malicious helm chart.
- **Trust:** Local pod_ok(role).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | app pod, cluster-admin |
| Objects | API server |
| Actions | pod_ok |
| Channels | RBAC, IRSA, metadata (6.5) |
| TCB | Admission policy. |
| Untrusted | Dockerfile USER root; hostNetwork |
| State / time | Deploy. |
| 1.1 cell | Authorization of the control plane. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| app SA | namespace role | run | allow-least |
| app SA | cluster-admin | run | deny |
| node | metadata | from-pod | deny-or-hop |
| break-glass | admin | use | E6 |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/10.3/10.3-lab` file `iam.py`.

## Transfer

Serverless IAM *.

## Residual risk

Break-glass admin with E6.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
