# 8.4-LO-07 — Transfer: clinic debug build against prod FHIR

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP MASVS 2.1.0 (final) `MASVS-CODE`. Resilience as cost. ASVS 5.0.0 (final) `v5.0.0-13.3.1`. MASTG profiles — not MASVS L1/L2/R.

## Change the workplace; keep debug off production

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `api_allowed("debug", "ok")` must be false. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic debug build against prod FHIR. Also name APK SBOM (10.2).

**Product sketch:** EHR-lite “debug flavor uses the same ApplicationId and API key so testers can hit real data,” plus R8 on release.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (leaked debug APK — not a live hospital);
2. trust assumptions (server build+attest is TCB; R8 and Play App Signing are not);
3. forbidden outcome (`api_allowed("debug","ok")` true, not “HIPAA”);
4. a test idea on a **local** fixture only (no store APK unpacking);
5. residual (stolen release keys, attestation farms, 8.1 hostile release APK);
6. WCAG if a human deny path exists (readable “use the lab environment”).

## Mental model: same key, two flavors

```mermaid
flowchart LR
  Flavor["debug flavor"] --> Belief[testers want real data]
  Key["prod API key"] --> Reality[debug loggers on prod FHIR]
```

If testers share the prod API key while `api_allowed` is always true, the cell is gone. R8, Play App Signing, and root detection do not check `build_type`. APK SBOM (10.2) is inventory of what shipped, not this channel check — name it, do not unpack store APKs here. Debug should still reach a **lab** FHIR sandbox.

The clinic rewrite still has to keep the SecureCollab fork: debug plus ok false, release plus ok may be true. Enabling R8 and Play App Signing without a debug-to-prod deny test leaves `api_allowed("debug","ok")` true. The local pytest analogue is `test_debug_build_cannot_call_prod_export` — on a fixture, not a store APK unpack.

## What graders reject

| Reject | Why |
|---|---|
| “R8 is on” | Cost, not channel |
| Live Play Console / unpacking | Lab policy |
| “MASVS R-level” | Obsolete MASVS levels; profiles live in MASTG |
| Play App Signing as this cell | Store signing, not debug deny |
| Debug APK builds as evidence | Wrong observation |

## Practice

One page. No keys. `labs/8.4/8.4-lab` is the only running system you may break. Do not unpack a public APK.

## Non-goals

Live-target reverse engineering. Real FHIR keys. Claiming Gate 8 from this page.
