# 10.3 — Cloud, containers, Kubernetes, and IaC (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** NIST SP 800-190; Kubernetes security guidance; ASVS V13/V15. K8s is optional in prod, required as a *model* here.

## Property (start here)

A pod requesting cluster-admin must be denied. Workload identity is least privilege (3.3 at cluster grain), not “our namespace is private.”

## Attacker capabilities and trust assumptions

- **Attacker:** Compromised app container; malicious helm chart.
- **Trust:** Local pod_ok(role).
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | App pod granted cluster-admin |
| Failure | Fail closed: Deny cluster-admin to app; PSP/PSS; no instance metadata from app net (6 |

Lab tests: `test_property.py` under `labs/10.3/10.3-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `App pod granted cluster-admin`
- `--impl fixed`: **pass**

cluster-admin denied.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Serverless IAM *.

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
