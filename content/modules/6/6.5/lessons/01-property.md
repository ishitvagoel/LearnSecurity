# 6.5 — Server-side requests and protocol parsing (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** ASVS 5.0.0 V10 (final); API7 awareness; URL is untrusted *structure* (2.1).

## Property (start here)

The lab fetcher must not allow http://169.254.169.254/ (link-local metadata). SSRF is a trust-boundary fail: the server’s network is not the user’s to steer. HTTPS to a named lab host may be allowed.

## Attacker capabilities and trust assumptions

- **Attacker:** User who supplies an unfurl/preview URL.
- **Trust:** Local allowed(url). No real cloud metadata in this VM lesson — we assert the deny.
**Mechanism (not the property):** requests.get is not an allow-list.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 6.5 |
|---|---|
| Root cause | Server fetches attacker-chosen authority. |
| Preconditions | allowed(link-local) True. |
| Impact (1.1 cell) | Confidentiality of the cloud TCB; integrity of egress. — In real clouds, credential theft; here, the test fails closed conceptually. |
| Prevention | Allow-list; parse then pin; block link-local, loopback, metadata; no open redirects. |
| Detection | egress deny logs. |
| Recovery | Rotate instance role if a real system was hit — never in this course. |

## Framework defaults vs application guarantees

requests.get is not an allow-list.

## Mechanism limits and bypasses

DNS rebinding after allow — pin IP or block.

IPv6, decimal IPs, redirect, file: scheme.

## Residual risk

Legitimate preview of customer URLs — dedicated egress proxy.

## Practice

Parse scheme/host; do not regex the string only.

Run `labs/6.5/6.5-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Webhook delivery (7.3) is egress too.

Clinic “fetch lab result PDF from URL.”

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.
