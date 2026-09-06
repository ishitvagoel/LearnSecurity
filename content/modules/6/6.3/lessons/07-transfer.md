# 6.3-LO-07 — Transfer: clinic share-with-partner POST

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-3.5.1`. SameSite is a helper.

## Change the workplace; keep cookie-without-intent

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `allow_share` from a foreign origin without a matching CSRF token is false. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic “share record with partner” POST. Also name postMessage, clickjacking, and CORS `*` with credentials as residuals — do not run them against a live clinic.

**Product sketch:** EHR-lite share button that relies on the login cookie.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (foreign origin using the victim browser as deputy — not a live clinic);
2. trust assumptions (origin + token are TCB; SameSite is not);
3. forbidden outcome (`allow_share` true for foreign origin without token, not “HIPAA”);
4. a test idea on a **local** fixture only (foreign origin + no token is false);
5. residual (GET mutate; clickjacking; postMessage; CORS credentials; Level 3 embeds; 4.2 phishing);
6. WCAG if a human deny page is in the claim (readable “share blocked,” not a silent no-op).

## Mental model: partner share is still a grant POST

```mermaid
flowchart LR
  Partner[share with partner] --> Belief[UI believes the user clicked]
  Cookie3[ambient cookie] --> Reality[foreign origin can POST]
```

If the partner-share POST keys only the login cookie, the cell is gone. FastAPI, SameSite=Lax, and a CORS allow-list do not bind origin and token. CORS `*` with credentials is false assurance. postMessage and clickjacking are named residuals: they can still confuse the deputy after this pytest is green.

The clinic rewrite still has to keep the SecureCollab fork: foreign origin without token is false, and same origin without token is also false. Setting SameSite=Lax without an origin×token test leaves ambient cookies as consent. The local pytest analogue is `test_foreign_origin_post_is_denied` plus `test_same_origin_without_token_is_denied` — on a fixture, not a live EHR.

## What graders reject

| Reject | Why |
|---|---|
| “SameSite is Lax” | Helper, not complete |
| Live clinic probe | Lab policy |
| CORS as the CSRF property | Different cell |
| HTTP 200 as intent evidence | Wrong observation |
| Cookie-only “logged in” as consent | This cell’s failure |

## Practice

One page. No keys. `labs/6.3/6.3-lab` is the only running system you may break. Do not visit a live foreign origin.

## Non-goals

Live-target CSRF. Real session cookies. Claiming Gate 6 from this page.
