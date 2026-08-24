# 10.2 — Source control, CI/CD, and software supply chain (3 Break)

**Kind:** mechanism-lab  
**Loop step:** 3 Break  
**Standards:** SLSA 1.2; OpenSSF OSPS; CISA 2026 SBOM minimum elements; NIST 800-161r1. Pin versions.

## Property (start here)

A dependency whose digest does not match the lockfile must not install. Integrity of build inputs is the cell — not “we have Dependabot.”

## Attacker capabilities and trust assumptions

- **Attacker:** Typosquat; compromised maintainer; poisoned PR from a fork.
- **Trust:** Local install_ok(got, expected).
**Forbidden outcome:** Dependency installed when digest mismatches lockfile

**Authorized scope:** `labs/10.2/10.2-lab` only. Do not target other hosts. Do not paste weaponized payloads into notes.

## What to observe

vulnerable lock.py ignores digest.

The vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: install_ok('aaa','bbb') True.

## Vulnerable fixture (local)

```python
def install_ok(expected_hash, got_hash):
    return True
```

## Root cause vs impact

| Slice | Lab |
|---|---|
| Root cause | Name-only install. |
| Impact | Malicious code in the TCB. |
| Not the lesson | A scanner name or Top 10 mnemonic as the definition |

## Practice

Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest labs/10.2/10.2-lab/tests -q --impl vulnerable` (or the README if fixtures differ).

## Transfer

GitHub Actions third-party action@v1.

## Non-goals

No live-target instructions. Synthetic data only.
