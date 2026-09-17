# 4.3 — Sessions, cookies, and tokens

Pass A specification, deepened. Lesson prose lives in `lessons/`. No exploit walkthroughs.

## Identity

- **id:** 4.3
- **slug:** sessions-cookies-and-tokens
- **title:** Sessions, cookies, and tokens
- **phase / track / difficulty:** 4 / core / intermediate
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 1.1–4.2 authored.
- **routeTags:** complete, web-api
- **releaseMilestone:** M1
- **masteryGate:** 4

## Objective hierarchy

1. Produce a **session protocol/state diagram and theft/replay tests** for SecureCollab Phase 1 (no query-string tokens; bound to the authentication event; idle and absolute limits; revocable).
2. Name attacker capabilities (Referer, access logs, screenshots, a stolen pre-authentication identifier, an unbounded lifetime, an un-invalidated server record) and trust assumptions (TLS does not hide the query from logs; a client deleting its own cookie does not touch the server's record of that session).
3. Transfer: clinic appointment deep link; magic-link email (module 6.6's single-use invite-token lesson).

## Prerequisite concepts

Module 2.3's cookie jar vs script distinction; module 3.1's treatment of query-string logs as a sink; module 4.2's authentication event, which this module's sessions are bound to.

## Misconceptions

- Query strings are fine over TLS.
- JWT means secure.
- HttpOnly is the same as "not in the URL."
- Deleting the cookie client-side is the same as revoking the session at the server.
- A session that keeps getting used does not need an absolute expiry.

## Concept map

Authn (module 4.2) → this module's channel, binding, lifetime, and revocation → module 4.4's authorization using the session → module 4.5's OAuth tokens.

## Teaching claims

Five falsifiable claims, ordered by dependency. The module previously taught only the first of these across all eight lessons — a query-string boolean repeated eight times under different headings. Naming the other four here makes the coverage contract checkable, and stops "session" from meaning only "not in the URL."

1. **C1 — A session secret placed in a URL is no longer a secret.** The URL a browser sends is copied into the server's own access logs, into the `Referer` header of any request the page makes to a third party, into browser history, and into any screenshot or pasted link a person makes of that page. TLS protects the bytes in transit between browser and server; it does nothing to any of those four copies, because each one is made *after* the request has already been decrypted and read by something the sender trusted with the connection, not by an attacker on the wire. A query-string `access_token` is therefore not a weaker version of a session token — it is a token that has already been disclosed to everyone who can read any one of those four copies, whether or not anyone attacks the TLS connection at all.
2. **C2 — A session identifier must be unguessable and bound to the authentication event that minted it.** Unguessable alone is not enough: if the identifier a browser holds *before* logging in survives the login unchanged, an attacker who can plant that pre-authentication identifier in the victim's browser — by sending a link that sets it, or by reading it from a shared or unauthenticated response — gets a session that becomes authenticated as the victim the moment the victim logs in, without ever needing to see the victim's password. This is session fixation, and the fix is not a stronger random number generator; a sufficiently random identifier that is *kept* across login is fixed exactly as effectively as a predictable one. The fix is a state transition: authentication must mint a new identifier and retire whatever identifier existed before it, so that no identifier chosen or observed before login can be the identifier that carries authority after it.
3. **C3 — A session needs both an idle lifetime and an absolute lifetime.** An idle timeout alone protects only against a session nobody is using; an attacker who has a valid session token and replays it periodically — often automatically, by simply keeping a browser tab open, or a background refresh call running — keeps the session's "last used" clock moving forward forever, so an idle-only policy never expires it. An absolute timeout alone protects only against a session that has existed a long time; a session that is actively idle-refreshed by a legitimate user for eleven hours and fifty-nine minutes of a twelve-hour absolute cap is still perfectly valid at 11:59, and the caller has no way to distinguish "the legitimate owner is still using this" from "an attacker who stole this an hour ago is still using it" without either limit forcing a re-authentication. The two checks answer different questions — "has this been touched recently enough" and "how long ago was this actually proven to belong to someone" — and a system that implements only one has silently promised the other for free.
4. **C4 — Logout and revocation must invalidate server-side state, because a token the server still honours is not revoked.** A browser deleting its own cookie changes what that one browser will send on its next request; it changes nothing about what the server will accept if the same token value arrives by some other path — a saved copy, a proxy log, a second device that never received the delete. "Log out" that only clears client-side storage is a UI action wearing a security claim it has not earned. The server has to hold (or be able to reconstruct) a fact of the form "this identifier is no longer good," and every request has to be checked against that fact, or the deletion on one browser is theater for every other place that same token value is sitting.
5. **C5 — `HttpOnly`, `Secure`, and `SameSite` each defend a different attacker capability, and naming one does not cover the others.** `HttpOnly` stops a script running on the page — an injected or third-party script exploiting an XSS bug — from reading the cookie's value; it does nothing about the cookie being sent to the wrong place. `Secure` stops the cookie from ever being sent over a plaintext HTTP connection, where a network-position attacker could read it off the wire; it does nothing about which site's pages can trigger that connection. `SameSite` stops the cookie from being attached to requests that a *different* site's page causes the browser to make, which is the cross-site request forgery and cross-site leak surface; it does nothing about a script that is already running on the cookie's own origin. A cookie with all three still relies on the application never leaking the value into a URL — the subject of C1 — so "we set the security flags" answers a narrower question than "is this cookie safe," and a reviewer who accepts one flag as proof of the other two has been shown a slogan, not a control.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break, 5 Verify | `test_query_string_token_is_rejected`, `test_cookie_session_still_works`, `test_authorization_header_still_works` (module's forbidden outcome plus the two channels it must not break) | items.md #1 |
| C2 | 1 Property, 2 Model, 4 Build | Not directly code-testable — minting a new identifier at login is owned by module 4.2's authentication lab, and this Tier-1 fixture has no login event for an identifier to be bound to. Modeled in `lessons/02-model.md`'s state diagram and `lessons/04-build.md`. | items.md #2 |
| C3 | 3 Break, 4 Build, 5 Verify | `test_active_session_within_both_windows_is_active`, `test_forbidden_outcome_activity_alone_does_not_extend_the_absolute_limit`, `test_idle_timeout_boundary_*`, `test_missing_timestamp_fails_closed_not_open`, plus the anti-fake pair added in this pass (see `upgrade-lab`) | items.md #3, #4, #7 |
| C4 | 6 Operate | Not directly code-testable — this stateless request-parsing fixture has no persisted session store for a revocation fact to live in. Modeled in `lessons/06-operate.md`. | items.md #6, #9 |
| C5 | 4 Build, 7 Transfer | Not directly code-testable — cookie-attribute emission is a response-building decision this request-parsing fixture does not make. Modeled in `lessons/04-build.md` and `lessons/07-transfer.md`. | items.md #5 |

C1 and C3 carry genuine lab assertions, satisfying the ≥2-claims bar, and C3's forbidden-outcome test is new in this pass — the lab previously exercised only C1. C2, C4, and C5 are honestly declared non-code-testable rather than mapped to a fabricated test: C2 needs an actual login event this fixture does not have, C4 needs a persisted session store this fixture does not have, and C5 is a response-header decision this request-side fixture does not make.

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| Identify which channel(s) a candidate session value arrived on and justify rejecting the query string | C1 | `lessons/01-property.md` §The URL is a postcard | `lessons/01-property.md` `?access_token=secret` walkthrough | `lessons/03-break.md` | items.md #1 | `lessons/07-transfer.md` clinic deep link |
| Explain why a pre-authentication identifier must not survive login | C2 | `lessons/01-property.md` §An old identifier does not become trustworthy | `lessons/02-model.md` fixation walkthrough | `lessons/02-model.md` state-diagram exercise | items.md #2 | `lessons/07-transfer.md` |
| Decide whether a session is still active under a stated idle/absolute policy | C3 | `lessons/04-build.md` §Two clocks, not one | `lessons/03-break.md` counterexample; `lessons/05-verify.md` | `labs/4.3/4.3-lab` `session_is_active` tests | items.md #3, #4, #7 | `lessons/07-transfer.md` |
| Distinguish server-side revocation from client-side cookie deletion | C4 | `lessons/06-operate.md` §Deleting is not revoking | `lessons/06-operate.md` worked incident | `lessons/06-operate.md` runbook exercise | items.md #6, #9 | `lessons/07-transfer.md` |
| Choose `Secure`/`HttpOnly`/`SameSite` and name the capability each removes | C5 | `lessons/04-build.md` §Three attributes, three attackers | `lessons/04-build.md` attribute table | `lessons/08-review.md` review checklist | items.md #5 | `lessons/07-transfer.md` |
| Transfer channel/binding/lifetime/revocation rules to a deep link and a magic link | C1–C5 | `lessons/07-transfer.md` | `lessons/07-transfer.md` clinic table | `lessons/07-transfer.md` write-up prompts | items.md #8 | (is the transfer task) |

## Known residuals

- Session fixation's mint-a-new-identifier fix (C2) is module 4.2's lab, not this one — named explicitly rather than silently assumed solved here.
- Concurrent-session limits and behavior at the limit (ASVS `v5.0.0-7.1.2`) are out of scope for this module's grain; named as a later design decision, not tested.
- Federated session termination between an identity provider and this app (ASVS `v5.0.0-7.1.3`, `v5.0.0-7.6.1`) is deferred to module 4.5's OAuth/OIDC treatment.
- Revocation (C4) is modeled, not lab-tested, because this fixture keeps no state across calls; a future Tier-2 upgrade with a real session store would let a revoke-then-check sequence be asserted directly.
- History and screenshots that already captured a leaked URL (C1) cannot be purged by any server-side control; named as a leftover in `lessons/06-operate.md`, not solved.

## Invariant prompts

- What must remain true if a URL is pasted into chat?
- What fails if uvicorn logs the query?
- What must be true of a session identifier the instant after login that was not true the instant before it?
- What must be true of a session record at 11:59 of a 12-hour absolute cap that is not true at 12:01?

## Threat-model prompts

- What can go wrong with `?access_token=`?
- What residual remains for one-time magic links?
- Who can plant a pre-authentication identifier in a victim's browser before the victim logs in?
- Who can hold a copy of a token after the browser that received it deletes its cookie?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/4.3/4.3-lab`. Forbidden: session from query-string token; a session whose activity alone extends it past its absolute lifetime. No live CDNs.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

OWASP ASVS 5.0.0 (final). Live-checked against the canonical `v5.0.0` tag on 2026-09-17; exact requirement text recorded in `content/standards/pins.yaml` and in the `**Standards:**` lines of `lessons/01-property.md` and `lessons/05-verify.md`.

- `v5.0.0-14.2.1` — sensitive data (including session tokens) only in HTTP bodies or headers, never URLs or query strings. C1.
- `v5.0.0-3.4.5` — a referrer policy to stop technically sensitive data leaking via `Referer`. C1.
- `v5.0.0-7.2.4` — a new session token is generated on authentication (including re-authentication), and the prior token is terminated. C2.
- `v5.0.0-7.3.1` — an inactivity (idle) timeout enforced per documented risk decisions. C3.
- `v5.0.0-7.3.2` — an absolute maximum session lifetime enforced per documented risk decisions. C3.
- `v5.0.0-7.4.1` — session termination (logout or expiration) disallows further use of the session; for reference tokens or stateful sessions this means invalidating the data at the backend. C4.
- `v5.0.0-3.3.1` — cookies carry the `Secure` attribute, and either the cookie name uses the `__Host-` prefix or, failing that, the `__Secure-` prefix. C5. (This module's worked cookie name, `sc_session`, carries neither prefix — a known simplification, not a claim that the example itself satisfies the requirement's literal text.)
- `v5.0.0-3.3.2` — a cookie's `SameSite` attribute is set according to its purpose. C5.
- `v5.0.0-3.3.4` — a cookie not meant to be read by client-side scripts (a session token) carries `HttpOnly`. C5.

The prior version of this spec cited only the last three of these nine identifiers, under a heading that implied full coverage of "sessions, cookies, and tokens" while the lessons taught only C1. The six `V7` (Session Management) identifiers are new in this pass and are what actually anchor C2–C4; V7 did not appear in this module at all before this revision.

## Review triggers

New OAuth flow; magic-link; log drain; superseding ASVS V7 or V14 (formerly V3 in this file, corrected — see Standards references).

## Time budget and SecureCollab

Evidence: session protocol/state diagram, theft/replay tests, idle/absolute-lifetime tests. Feeds M1.

## Operational considerations

`query_token_rejected`; log-redact; revoke leaked tokens; `session_expired reason=idle|absolute`; revoke-on-logout must be a server-side write, not only a client-side delete.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: URL-as-postcard models; ASVS 14.2.1 |
| 2026-09-17 | Deepen (B0 pilot, third of three): named five teaching claims (C1–C5) and a coverage contract; C1 and C3 carry lab assertions, C2/C4/C5 declared honestly non-code-testable with a stated reason each. Corrected the Standards references section — the prior three ASVS citations (`v5.0.0-14.2.1`, `3.4.5`, `3.3.4`) were re-verified against the live `v5.0.0` tag and are accurate, but they anchor only C1 and one clause of C5; added six further identifiers (`7.2.4`, `7.3.1`, `7.3.2`, `7.4.1`, `3.3.1`, `3.3.2`) that this module needed and never cited. Also corrected a bug shared with 1.4 and 2.1 before their independent review: `module.yaml` carried `reviewer: pending` with `lastReviewedAt`/`nextReviewAt` set to real dates and no artifact under `content/progress/reviews/` — reverted both to `null` per `metadata-honesty.mdc`. |
