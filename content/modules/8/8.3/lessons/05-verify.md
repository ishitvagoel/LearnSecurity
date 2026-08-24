# 8.3 — Network, deep links, WebViews, IPC (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** MASVS 2.1 PLATFORM/NETWORK/AUTH (final); RFC 8252. Exported components are attack surface.

## Property (start here)

A deep link query as=admin must not switch the signed-in principal. The session is identity; the Intent is untrusted input.

## Attacker capabilities and trust assumptions

- **Attacker:** Malicious app sending an Intent; crafted https link.
- **Trust:** Local open_link / current_user.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | Deep link as= switches the signed-in user |
| Failure | Fail closed: Do not take identity from links; validate App Link certs; WebView allow-list |

Lab tests: `test_property.py` under `labs/8.3/8.3-lab`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `Deep link as= switches the signed-in user`
- `--impl fixed`: **pass**

deeplink does not switch user.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

OAuth redirect to app (4.5).

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
