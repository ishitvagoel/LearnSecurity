# 4.2-LO-07 — Transfer: clinic SSO and step-up export

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** NIST SP 800-63B-4 (final); WebAuthn Level 3 (**CR**); WCAG 2.2 (final).

## Change the portal; keep origin binding

Do not answer with a Top 10 / CWE / scanner as the definition of security.

**Prompt:** Clinic staff SSO portal. Optionally: step-up for export — still origin-bound?

**Product sketch:** EHR-lite login plus a second ceremony before chart export.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (lookalike IdP; intercepted OTP; fatigued clinician — not a live clinic);
2. trust assumptions (which origin check is TCB; “we use Okta” is not);
3. forbidden outcome (`phishing_resistant("otp", evil, real)` is true, or step-up password counted as resistant);
4. a test idea on a **local** fixture only;
5. residual (password fallback; recovery SMS; WebAuthn ≠ authorization);
6. WCAG 2.2 on the ceremony (keyboard, labels, not color-only).

## Mental model: MFA to the wrong IdP is still phishing

```mermaid
flowchart LR
  Staff[Clinician] --> Fake["https://evil-sso.example"]
  Fake --> Otp[OTP typed]
  Otp --> Real["Real EHR session"]
```

Step-up for export must bind origin too, or the second factor is theater.

## What graders reject

| Reject | Why |
|---|---|
| “Any 2FA is phishing-resistant” | OTP walks |
| Live clinic IdP | Lab policy |
| Passkey vendor as the property | Mechanism |

## Practice

One page. No keys. `labs/4.2/4.2-lab` is the only running system you may break.
