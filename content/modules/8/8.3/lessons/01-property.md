# 8.3 — Network, deep links, WebViews, IPC (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** MASVS 2.1 PLATFORM/NETWORK/AUTH (final); RFC 8252. Exported components are attack surface.

## Property (start here)

A deep link query as=admin must not switch the signed-in principal. The session is identity; the Intent is untrusted input.

## Attacker capabilities and trust assumptions

- **Attacker:** Malicious app sending an Intent; crafted https link.
- **Trust:** Local open_link / current_user.
**Mechanism (not the property):** exported=true defaults on old Android.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 8.3 |
|---|---|
| Root cause | Identity taken from the link. |
| Preconditions | open_link({as:admin}) sets admin. |
| Impact (1.1 cell) | Authenticity of the principal. — Local privilege / account switch. |
| Prevention | Do not take identity from links; validate App Link certs; WebView allow-list. |
| Detection | ignored_as_param metric. |
| Recovery | Force re-login. |

## Framework defaults vs application guarantees

exported=true defaults on old Android.

## Mechanism limits and bypasses

Verified App Links still pass query strings.

WebView javascript:; custom scheme hijack.

## Residual risk

User installs attacker app — OS model.

## Practice

List exported components.

Run `labs/8.3/8.3-lab` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

OAuth redirect to app (4.5).

Clinic: deep link as=doctor.

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Deep-link errors should not trap users in a broken WebView without a keyboard-accessible exit.
