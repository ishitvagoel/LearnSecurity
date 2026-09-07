# An origin-and-token map someone else can test

**Kind:** design-exercise
**Loop step:** 2 Model

## Could someone else name the checks from your origin map?

Keep **who may POST share, with which cookie, origin, and token**; “SameSite is on” is not that list.

`allow_share(origin, expected, token, session_cookie)` — no live browsers.

## Picture: three inputs, one decision

```mermaid
flowchart TD
  C[session_cookie] --> D{allow_share}
  O[origin == expected] --> D
  T[token matches] --> D
```

Missing cookie denies. Matching origin without token denies. Foreign origin denies.

## Picture: a hand-attached token is a different helper

```mermaid
flowchart LR
  Cookie2[cookie] --> Ambient[rides on form POST]
  Bearer[Authorization] --> Manual[caller must attach]
```

This lab is the leftover-cookie helper. Do not treat a Bearer-only API as “CSRF solved” if a cookie fallback still exists.

## Step 1: name the pieces

| Piece | This system |
|---|---|
| People | victim browser; foreign origin |
| Objects | share grant |
| Actions | `allow_share` |
| Paths | cookie; Origin; CSRF token |
| What you trust | origin match **and** token when cookie present |
| What you do not trust | Origin header from the request; missing token |
| Time | one POST |
| The rule | Integrity of share grants |

## Step 2: write cells

| Subject | Object | Action | Decision |
|---|---|---|---|
| same origin + token + cookie | share | POST | allow |
| foreign origin + cookie | share | POST | deny |
| same origin, no token | share | POST | deny |
| no cookie | share | POST | deny |
| GET | share | mutate | deny (named, not this practice) |

## Practice

Start at `csrf.py` under `labs/6.3/6.3-lab`.

## Use it somewhere new

A partner-share POST still needs the origin check; postMessage is the sibling leftover.

## What can still go wrong

Clickjacking; CORS credentials; advanced authenticated embeds; lookalike UI from the phishing lesson.

## What this page is not doing

Naming CSRF does not require Origin on the share POST. Answer keys are not on this site.
