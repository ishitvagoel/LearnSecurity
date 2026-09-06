# 8.2 — Local data, keys, biometrics, offline state, and leakage surfaces

Pass A specification. Lesson prose lives in `lessons/`. No exploit walkthroughs. Lab AEAD prefix is a stand-in.

## Identity

- **id:** 8.2
- **slug:** local-data-keys-biometrics-offline-state-and-leakage-surfaces
- **title:** Local data, keys, biometrics, offline state, and leakage surfaces
- **phase / track / difficulty:** 8 / mobile / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 5.2 AEAD; 8.1 hostile client; 4.2 biometrics ≠ server MFA.
- **routeTags:** complete, mobile
- **releaseMilestone:** M3
- **masteryGate:** 8

## Objective hierarchy

1. Produce a **device store inventory** plus deny tests so a cached note is not plaintext on disk.
2. Name attacker capabilities (USB backup, lost device, cloud backup of app files) and trust assumptions (local `save_note` / `plaintext_on_disk`).
3. Transfer: clinic offline chart cache; iOS Keychain as a later mirror; Electron — without treating EncryptedSharedPreferences as covering every file.

## Prerequisite concepts

5.2 encoding ≠ encryption; 5.1 extra copies; 4.2 local authenticator is not phishing-resistant server auth; 8.1 APK is hostile.

## Misconceptions

- Private app dir is encryption.
- Fingerprint is MFA to the server.
- Offline means no policy.
- EncryptedSharedPreferences covers every file you write.

## Concept map

Hostile client (8.1) → at-rest on device (this module) → IPC leaks (8.3) → 5.1 deletion graph includes the phone.

## Invariant prompts

- What must remain true after `save_note("secret")`?
- What fails if biometrics lock the UI but the file is still plaintext?

## Threat-model prompts

- What can go wrong when Room writes bodies as text?
- What residual remains after a remote-wipe that the OS does not honor?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/8.2/8.2-lab`. Forbidden: note body cached as plaintext. Synthetic `'secret'` only.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- OWASP MASVS 2.1.0 (final): `MASVS-STORAGE-1` (store sensitive data securely); `MASVS-STORAGE-2` (prevent leakage); `MASVS-CRYPTO-2` (key management / Keystore); `MASVS-AUTH-2` (local authentication — not 4.2 server MFA). No MASVS L1/L2/R.
- OWASP MASTG 2.0.0 (final, June 2026): tests for STORAGE group; website/repos authoritative.
- OWASP ASVS 5.0.0 (final): `v5.0.0-11.3.3` AEAD property named; the lab prefix is **not** that algorithm.

## Review triggers

New cache/DB file; backup/screenshot/notification; biometric-as-MFA claim.

## Time budget and SecureCollab

Evidence: inventory + plaintext-on-disk tests. Feeds Gate 8 / M3 (not-attempted).

## Operational considerations

`logout_wipes_cache`; `backup_flag`. Physical + extracted keys is an honest residual.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: private-dir vs encryption; MASVS-STORAGE-1/2; AUTH-2 vs 4.2 |
