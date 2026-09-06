# Same idea on a clinic share-with-partner POST

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

The notes-app scaffolding goes away. You get a **clinic sketch** with a “share record with partner” POST that relies on the login cookie. Your job is to rewrite the loop, not to name a famous-bugs code.

The notes-app sentence was: `allow_share` from a foreign origin without a matching CSRF token is false. Rewrite it for a clinic without changing the fork: leftover cookies are not consent to share.

**Prompt:** Clinic “share record with partner” POST. Also name postMessage, clickjacking, and CORS `*` with credentials as leftovers — do not run them against a live clinic.

## Picture: partner share is still a grant POST

```mermaid
flowchart LR
  Partner[share with partner] --> Belief[UI believes the user clicked]
  Cookie3[leftover cookie] --> Reality[foreign origin can POST]
```

If the partner-share POST keys only the login cookie, the cell is gone. FastAPI, SameSite=Lax, and a CORS allow-list do not bind origin and token. CORS `*` with credentials is false comfort. postMessage and clickjacking are named leftovers: they can still confuse the helper after this pytest is green.

The clinic rewrite still has to keep the notes-app fork: foreign origin without token is false, and same origin without token is also false. Setting SameSite=Lax without an origin-and-token test leaves leftover cookies as consent. The local pytest analogue is `test_foreign_origin_post_is_denied` plus `test_same_origin_without_token_is_denied` — on a fixture, not a live clinic system.

## Prompt — clinic sketch

Rewrite the notes-app sentence. Include:

1. who can act (foreign origin using the victim browser as helper — **not** a live clinic);
2. what you trust (origin + token are trusted; SameSite is not);
3. what must not happen (`allow_share` true for foreign origin without token, not a legal label);
4. a test idea on a **local** fixture only (foreign origin + no token is false);
5. leftover (GET mutate; clickjacking; postMessage; CORS credentials; advanced embeds; lookalike UI from the phishing lesson);
6. whether a human-seen “share blocked” path must be announced in text, not a silent no-op that pushes people to retry from a lookalike.

## What is not good enough

| Reject | Why |
|---|---|
| “SameSite is Lax” | Helper, not complete |
| Live clinic probe | Course rules |
| CORS as the CSRF rule | Different cell |
| HTTP 200 as intent evidence | Wrong observation |
| Cookie-only “logged in” as consent | This cell’s failure |

## Practice

One page. No answer keys. `labs/6.3/6.3-lab` is the only running system you may break. Do not visit a live foreign origin.

## What this page is not doing

Live-target CSRF. Real session cookies. Claiming a course gate from this page.
