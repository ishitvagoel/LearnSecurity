# 10.3 — Cloud, containers, Kubernetes, and IaC (4 Build)

**Kind:** design-exercise  
**Loop step:** 4 Build  
**Standards:** NIST SP 800-190; Kubernetes security guidance; ASVS V13/V15. K8s is optional in prod, required as a *model* here.

## Property (start here)

A pod requesting cluster-admin must be denied. Workload identity is least privilege (3.3 at cluster grain), not “our namespace is private.”

## Attacker capabilities and trust assumptions

- **Attacker:** Compromised app container; malicious helm chart.
- **Trust:** Local pod_ok(role).
cluster-admin pod_ok False.

Structural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”

## Fixed fixture (local)

```python
def pod_ok(role):
    return role != 'cluster-admin'
```

## Why this restores the cell

Deny cluster-admin to app; PSP/PSS; no instance metadata from app net (6.5).

Fail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).

## What this is not

EKS default service account often too wide.

NetworkPolicy is not RBAC.

## Practice

Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).

## Transfer

Serverless IAM *.

## Residual risk

Break-glass admin with E6.
