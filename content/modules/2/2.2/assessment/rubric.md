# 2.2 assessment (learner-facing — no answers)

**Practical evidence, not a compensating average.** States: not attempted | developing | competent | transfer-ready. Every critical invariant below needs satisfactory evidence on its own; a strong answer on one claim never substitutes for a missing one on another.

## Module

DNS, transport, HTTP, TLS, proxies, CDNs, and caches — five teaching claims (C1–C5), named in `spec.md` §Teaching claims: cache-key company binding, forwarded-identity trust, TLS hop authentication, TLS's one-hop-at-a-time scope, and a code fix's need for a paired detection/recovery signal.

## Evidence checklist

- [ ] Request-path diagram (Lesson 02) naming, per hop, which identity or name was authenticated and which was not, and stating the cache-key policy that must hold at the shared store
- [ ] Local reproduction of all three forbidden outcomes (Lesson 03): a shared-cache cross-company hit, a forwarded-header company override, and a hostname-mismatched hop accepted as trustworthy
- [ ] Lab `labs/2.2/2.2-request-path`: `vulnerable/` tests show 29 of 35 failing for the stated security reasons; `fixed/` tests show 35 of 35 passing
- [ ] Assessment items (`content/modules/2/2.2/assessment/items.md`) attempted with written reasoning, not single-word answers
- [ ] Operate signals for both failure classes: `cdn_hit_company_mismatch` and `hop_rejected reason=hostname_mismatch|version|untrusted`, neither carrying a note body, session token, or key material
- [ ] Transfer task (Lesson 07) applying the same cache-key and forwarded-identity rules to a clinic `/patients/me` endpoint on a shared CDN, correctly rejecting `Vary: Cookie` as a substitute for resolved-identity binding

## Rubric

| Result | Meaning |
|---|---|
| Developing | Names the cache-key claim (C1) alone as "the" property; TLS-transport slogans ("HTTPS everywhere") offered as evidence for identity resolution or hop authentication; missing forbidden-outcome lab evidence for any of C1, C2, or C3 |
| Competent | All five claims stated as system-specific properties of SecureCollab's request path, not tool names; every lab forbidden outcome reproduced and mapped to the claim it tests; the encryption-vs-authentication distinction from `01-property.md` applied correctly to a new hop |
| Transfer-ready | Lesson 07's transfer task completed, correctly separating `Vary: Cookie`'s selection-among-existing-representations behavior from C1's resolved-identity cache-key binding, without Top 10/scanner language standing in for either |

Knowledge check (retryable, 80% threshold): the eight module-specific items in `content/modules/2/2.2/assessment/items.md`.

## Seeded review

Use the local `vulnerable/` artifact via Lesson 08's checklist. Intended findings and banding live only in `content/assessment/keys/2.2.md`.
