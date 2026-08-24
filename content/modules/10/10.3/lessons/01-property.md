# 10.3 — Cloud, containers, Kubernetes, and IaC (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NIST SP 800-190; Kubernetes security guidance; ASVS V13/V15. K8s is optional in prod, required as a *model* here.

## Property (start here)

A pod requesting cluster-admin must be denied. Workload identity is least privilege (3.3 at cluster grain), not “our namespace is private.”

## Attacker capabilities and trust assumptions

- **Attacker:** Compromised app container; malicious helm chart.
- **Trust:** Local pod_ok(role).
**Mechanism (not the property):** EKS default service account often too wide.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 10.3 |
|---|---|
| Root cause | God-mode for convenience. |
| Preconditions | pod_ok('cluster-admin') True. |
| Impact (1.1 cell) | Authorization of the control plane. — Cluster takeover from one app bug. |
| Prevention | Deny cluster-admin to app; PSP/PSS; no instance metadata from app net (6.5). |
| Detection | admission_denied. |
| Recovery | Rotate cluster creds. |

## Framework defaults vs application guarantees

EKS default service account often too wide.

## Mechanism limits and bypasses

NetworkPolicy is not RBAC.

node IAM via metadata.

## Residual risk

Break-glass admin with E6.

## Practice

Shared-responsibility sketch: you vs cloud vs K8s.

Run `labs/10.3/10.3-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Serverless IAM *.

Clinic: app SA is cluster-admin.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
