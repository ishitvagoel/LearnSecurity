# 8.5-LO-07 — Transfer: clinic crash with a synthetic patient name

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP MASVS 2.1.0 (final) `MASVS-PRIVACY-1`–`PRIVACY-4`. ASVS `v5.0.0-16.2.5`. Play Data safety is disclosure.

## Change the workplace; keep bodies out of telemetry

Do not answer with a Top 10 / CWE / scanner as the definition of security.

**Prompt:** Clinic crash with a synthetic patient name. Also name web Sentry (10.5).

**Product sketch:** EHR-lite “debug crash includes the last chart so support can reproduce,” plus a completed Play Data safety form.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (crash-platform operator, logcat reader — not a live clinic);
2. trust assumptions (redact-before-send is TCB; Play Data safety and Crashlytics automatic are not);
3. forbidden outcome (`'name' in str(crash_report(name))`, not “HIPAA”);
4. a test idea on a **local** fixture only (no live Sentry);
5. residual (vendor processor, screenshots, ANR, leftover `READ_LOGS`);
6. WCAG if a human feedback path exists (must not require a screenshot of the chart).

## Mental model: same sink, clinical object

```mermaid
flowchart LR
  Chart[synthetic chart text] --> Belief[support wants the last screen]
  Crash[crash SDK] --> Reality[vendor copy of the chart]
```

## What graders reject

| Reject | Why |
|---|---|
| “Play Data safety is filled in” | Disclosure, not redaction |
| Live Crashlytics / real names | Lab policy |
| “MASVS L1 privacy” | Obsolete MASVS levels; profiles live in MASTG |

## Practice

One page. No keys. `labs/8.5/8.5-lab` is the only running system you may break.
