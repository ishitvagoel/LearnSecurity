# 8.1-LO-07 — Transfer: clinic Android hipaaMode=true

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP MASVS 2.1.0 (final) `MASVS-PLATFORM`. ASVS 5.0.0 (final) `v5.0.0-8.3.1`. Mobile Top 10:2024 awareness after. Do not use MASVS L1/L2/R.

## Change the workplace; keep the server as TCB

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `allow_export({"integrity": "ok"}, "fail")` must be false. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic Android client sends `hipaaMode=true`. Also name APK feature flags and `premium=true`.

**Product sketch:** EHR-lite Compose switch “HIPAA mode” that the API trusts as a boolean.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (patched clinic APK — not a live hospital device);
2. trust assumptions (server attest + 1.2 is TCB; client boolean and store listing are not);
3. forbidden outcome (`allow_export` true on client claim with failing attest, not “HIPAA”);
4. a test idea on a **local** fixture only (no live Play);
5. residual (attestation farms, rooted honest clinicians, 8.4 debug builds);
6. WCAG if a human deny path exists (readable “export unavailable,” not a silent crash).

## Mental model: a client switch is still a client claim

```mermaid
flowchart LR
  Switch["Compose hipaaMode"] --> Belief[UI believes compliant]
  Json["JSON hipaaMode true"] --> Reality[server grant if unchecked]
```

If the Compose switch is “HIPAA mode” while the server binds `hipaaMode=true` as a grant, the cell is gone. Play Integrity in the app, R8, and the store listing do not ignore the client boolean. Feature flags and `premium=true` are the same claim family — name them, do not run those APKs here. Sandboxing still does not put this process in the TCB (LO-01).

The clinic rewrite still has to keep the SecureCollab fork: client claim plus failing attest false, server-pass may allow. Enabling Play Integrity without a failing-attest deny test leaves `allow_export({integrity: ok}, fail)` true. The local pytest analogue is `test_client_integrity_claim_is_not_authorization` — on a fixture, not a live hospital device or Frida session.

## What graders reject

| Reject | Why |
|---|---|
| “Play Integrity is on” | Signal, not 1.2 |
| Live clinic device / Frida | Lab policy |
| “MASVS L2” | Obsolete MASVS levels |
| Compose disabled as the grant | Client is not TCB |
| Store listing as device trust | Package id, not next JSON |

## Practice

One page. No keys. `labs/8.1/8.1-lab` is the only running system you may break. Do not instrument a public device.

## Non-goals

Live-target mobile attacks. Real BAA flags. Claiming Gate 8 from this page.
