# 5.4 — Secure communication and channel binding (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** RFC 8446/9846 TLS 1.3 (final); ASVS 5.0.0 V12; MASVS-NETWORK for 8.x. Pinning is a trade-off, not a universal rule.

## Property (start here)

A client-supplied X-Forwarded-Proto: https does not make the channel HTTPS. Channel authenticity is what the server socket actually negotiated (or a trusted proxy you *bound*), not a header from the browser.

## Attacker capabilities and trust assumptions

- **Attacker:** Client on cleartext who wants the app to think TLS is on (cookie Secure flags, redirects).
- **Trust:** Direct socket proto in the lab. Real deployments may trust a *locked* load balancer hop only.
**Mechanism (not the property):** uvicorn --proxy-headers without a trusted proxy IP is this bug.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 5.4 |
|---|---|
| Root cause | Confused deputy: app believes client about the channel. |
| Preconditions | Header https + socket http => True. |
| Impact (1.1 cell) | Authenticity of the transport. — Session cookies marked as if Secure; users stay on cleartext; HSTS skipped. |
| Prevention | Ignore client proto unless the immediate peer is a trusted proxy with a bound identity. |
| Detection | Requests where header https and socket http. |
| Recovery | HSTS once you really have TLS; revoke cookies issued over cleartext. |

## Framework defaults vs application guarantees

uvicorn --proxy-headers without a trusted proxy IP is this bug.

## Mechanism limits and bypasses

Correct TLS to the LB is not e2e if you needed e2e (messaging).

SSLStrip on networks without HSTS; spoofed Forwarded.

## Residual risk

Pinning mobile apps (8.x) vs operational breakage — document, don’t mandate.

## Practice

Draw hops: device — ? — LB — app. Who is allowed to assert proto?

Run `labs/5.4/5.4-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

mTLS service identity vs this header.

Clinic: “we’re on TLS” because the SPA uses https:// in axios baseURL while API is http internally logged as https.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
