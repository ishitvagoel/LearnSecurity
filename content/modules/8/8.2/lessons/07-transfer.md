# 8.2-LO-07 — Transfer: clinic offline chart cache

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP MASVS 2.1.0 (final) `MASVS-STORAGE-1`. AUTH-2 local vs 4.2 server.

## Change the workplace; keep ciphertext on disk

Do not answer with a Top 10 / CWE / scanner as the definition of security.

**Prompt:** Clinic offline chart cache. Also name iOS Keychain vs Android Keystore and desktop Electron.

**Product sketch:** EHR-lite “available offline” that writes the chart as `charts.json` in internal storage, plus a fingerprint prompt to open the app.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (lost clinic tablet / backup — not a live hospital);
2. trust assumptions (Keystore-wrapped cache is TCB; private dir and fingerprint UI are not);
3. forbidden outcome (`plaintext_on_disk` true, not “HIPAA”);
4. a test idea on a **local** fixture only (no personal-phone imaging);
5. residual (backups, screenshots, notifications, extracted keys, 8.3 clipboard);
6. WCAG if a human unlock path exists (device-credential fallback, no plaintext debug overlay).

Use synthetic labels. Do not use real patient charts.

## Mental model: fingerprint is not the file wrap

```mermaid
flowchart LR
  Fp["fingerprint to open app"] --> Belief[clinician believes encrypted]
  File["charts.json plaintext"] --> Reality[backup yields bodies]
```

## What graders reject

| Reject | Why |
|---|---|
| “Internal storage” | Not encryption |
| Live clinic tablet imaging | Lab policy |
| “Fingerprint is MFA” | AUTH-2 local, not 4.2 |

## Practice

One page. No keys. `labs/8.2/8.2-lab` is the only running system you may break.
