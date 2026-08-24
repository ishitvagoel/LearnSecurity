# 7.3 — Webhooks, callbacks, and third-party APIs (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V10 (final); API10 awareness. HMAC is a teaching stand-in, not “we are Stripe.”

## Property (start here)

A webhook with a missing signature is rejected. Authenticity of the *provider message* is distinct from TLS and from 1.2 on the resulting action.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who can POST your callback URL.
- **Trust:** Local accept(sig, body, secret).
**Mechanism (not the property):** Stripe SDK verify is not your custom HMAC if you reimplement poorly.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 7.3 |
|---|---|
| Root cause | Callback trusted because it hit the path. |
| Preconditions | accept('', body, secret) True. |
| Impact (1.1 cell) | Authenticity + integrity of inbound integration. — Forged “share” or billing events. |
| Prevention | Verify MAC; bind to secret per provider; timestamp. |
| Detection | sig_fail metric. |
| Recovery | Rotate webhook secret; review accepted events. |

## Framework defaults vs application guarantees

Stripe SDK verify is not your custom HMAC if you reimplement poorly.

## Mechanism limits and bypasses

Correct signature still needs 1.2 on side effects.

Timing leak compare; parsed JSON vs raw body mismatch (2.1).

## Residual risk

Provider compromise — egress + least privilege on what a webhook may do.

## Practice

List: signature, raw body, time, replay, dest URL ownership.

Run `labs/7.3/7.3-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Signed redirects; outbound webhook SSRF (6.5).

Clinic lab-result webhook.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
