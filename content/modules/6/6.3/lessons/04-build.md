# Require origin match and a CSRF token

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

A leftover cookie does not decide a cross-site share. SameSite as the only check still allows a foreign origin with `token=None`. CORS is an origin header, not the share. “The user clicked something somewhere” is a story.

The repair: `allow_share` must require a session cookie **and** `origin == expected` **and** a matching CSRF token. In short, site-bound intent — not leftover cookie authority from the surroundings.

Repair share: all three, or deny. A missing origin or token **denies**. SameSite Lax does not replace origin and token.

## Picture: all three, or deny

```mermaid
flowchart TD
  Call[allow_share] --> Cookie{"cookie?"}
  Cookie -->|no| Deny[Deny]
  Cookie -->|yes| Origin{"origin expected?"}
  Origin -->|no| Deny
  Origin -->|yes| Token{"token ok?"}
  Token -->|no| Deny
  Token -->|yes| Allow[Allow]
```

Share requires `session_cookie`, then `origin == expected and token == "lab-csrf"`. Bind that token to the session, not a cookie a foreign origin can cause to be sent. GET `/share?to=` is a mutate-on-GET leftover. Clickjacking, postMessage, and a later open-redirect lesson stay named leftovers. CORS `*` with credentials is false assurance.

Use anti-forgery tokens or extra headers a simple form cannot set — `allow_share`. Extra rows about authenticated embeds and CORP are **advanced** — not this check.

## What the repaired files must show

| After the fix | Must be true |
|---|---|
| foreign origin, no token | false |
| same origin, matching token, cookie | true |
| cookie missing | false |
| same origin, no token | false |

## What this is not

SameSite=Lax as complete. CORS `*` with credentials. Token stored in a cookie that the foreign origin can cause to be sent (double-submit without binding). GET `/share?to=`. Fetch metadata as the only check.

## What the tool cannot do

- Clickjacking / who may frame the page is a different rule.
- postMessage origin checks are a different rule.
- A later open-redirect lesson can still send the person somewhere else after a real click.
- Authenticated embeds / CORP are advanced extras.
- Lookalike UI from the phishing lesson: the person intended the *lookalike*, not this origin.

## Practice

Name the check (cookie and origin == expected and token). Run:

```text
python3 -m pytest labs/6.3/6.3-lab/tests --impl fixed
```

## Use it somewhere new

Stop treating “logged-in cookie” as consent to share with a partner.

## What can still go wrong

Clickjacking; postMessage; later open redirect; advanced embeds; lookalike UI; GET that still mutates.

## What this page is not doing

Do not visit a live foreign origin. SameSite=Lax does not finish a check-in.
