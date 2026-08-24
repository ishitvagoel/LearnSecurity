# 10.2 — Source control, CI/CD, and software supply chain (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** SLSA 1.2; OpenSSF OSPS; CISA 2026 SBOM minimum elements; NIST 800-161r1. Pin versions.

## Property (start here)

A dependency whose digest does not match the lockfile must not install. Integrity of build inputs is the cell — not “we have Dependabot.”

## Attacker capabilities and trust assumptions

- **Attacker:** Typosquat; compromised maintainer; poisoned PR from a fork.
- **Trust:** Local install_ok(got, expected).
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** GitHub Actions third-party action@v1.

**Product sketch:** Clinic: npm install in prod pod.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | npm audit is 9.4 signal, not this cell.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/10.2/10.2-lab` stays the only running system you may break.
