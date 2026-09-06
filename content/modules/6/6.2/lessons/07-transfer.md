# 6.2-LO-07 — Transfer: clinic patient nickname field

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-1.2.1`. CSP3 **draft**.

## Change the workplace; keep context encoding

Do not answer with a Top 10 / CWE / scanner as the definition of security.

**Prompt:** Clinic patient nickname field rendered on a shared board. Also name markdown-to-HTML as a second parser (2.1).

**Product sketch:** EHR-lite “preferred name” that concatenates into an HTML badge.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (patient or clerk supplying a nickname — not a live clinic);
2. trust assumptions (HTML-text encoder is TCB; CSP header is not);
3. forbidden outcome (`render` leaves `<` as markup, not “HIPAA”);
4. a test idea on a **local** fixture only (tame `<` marker);
5. residual (JS/attr/URL contexts; markdown pipeline; Trusted Types draft; CSP reporting Level 3);
6. WCAG if a human “name could not be shown” path is in the claim (readable fallback, not a blank badge that hides the person).

## Mental model: nickname is still HTML input

```mermaid
flowchart LR
  Nick[nickname] --> Belief[UI believes it is a label]
  HTML[HTML badge] --> Reality[grammar mixed with data]
```

## What graders reject

| Reject | Why |
|---|---|
| “CSP is on” | Layer, draft, not this cell |
| Live clinic probe | Lab policy |
| Exploit-kit payload as the test | Lab policy; tame `<` is enough |

## Practice

One page. No keys. `labs/6.2/6.2-lab` is the only running system you may break.
