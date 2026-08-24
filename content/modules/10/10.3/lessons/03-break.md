# 10.3 — Cloud, containers, Kubernetes, and IaC (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** NIST SP 800-190; Kubernetes security guidance; ASVS V13/V15. K8s is optional in prod, required as a *model* here.

## Property (start here)

A pod requesting cluster-admin must be denied. Workload identity is least privilege (3.3 at cluster grain), not “our namespace is private.”

## Attacker capabilities and trust assumptions

- **Attacker:** Compromised app container; malicious helm chart.
- **Trust:** Local pod_ok(role).
**Forbidden outcome:** App pod granted cluster-admin

**Authorized scope:** `labs/10.3/10.3-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable iam.py allows cluster-admin.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: pod_ok('cluster-admin') True.

## Vulnerable fixture (local)

```python
def pod_ok(role):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | God-mode for convenience. |
| Impact | Cluster takeover from one app bug. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/10.3/10.3-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

Serverless IAM *.

## Non-goals

No live-target instructions. Synthetic data only.
