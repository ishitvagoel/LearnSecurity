# 10.2 — Source control, CI/CD, and software supply chain (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** SLSA 1.2; OpenSSF OSPS; CISA 2026 SBOM minimum elements; NIST 800-161r1. Pin versions.

## Property (start here)

A dependency whose digest does not match the lockfile must not install. Integrity of build inputs is the cell — not “we have Dependabot.”

## Attacker capabilities and trust assumptions

- **Attacker:** Typosquat; compromised maintainer; poisoned PR from a fork.
- **Trust:** Local install_ok(got, expected).
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | CI, package registry |
| Objects | wheel hash, lockfile |
| Actions | install_ok |
| Channels | pip/npm/gradle |
| TCB | Lockfile + verify digest; isolated runners; signed provenance later. |
| Untrusted | Postinstall scripts, mutable latest tags |
| State / time | Install at 03:00. |
| 1.1 cell | Integrity of the artifact you will run. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| CI | matching digest | install | allow |
| CI | mismatch | install | deny |
| fork PR | secrets | read | deny |
| release | provenance | sign | allow |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/10.2/10.2-lab` file `lock.py`.

## Transfer

GitHub Actions third-party action@v1.

## Residual risk

Build cache poisoning.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
