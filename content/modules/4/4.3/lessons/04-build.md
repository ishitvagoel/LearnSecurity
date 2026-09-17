# Two clocks, a fresh identifier, and three attributes that each answer a different question

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

Lesson 03 staged two breaks: a query-string token, and a session that outlives any sane policy because only its idle clock was ever checked. The build for the first is a deny rule already covered — if `access_token` is present in the query, return `None` before looking at anything else. The build for the second needs two clocks read together, not one clock read more carefully: a session is active only while it is within its idle window *and* within its absolute window, and either deadline alone is enough to end it.

```text
def session_is_active(session, now):
    issued_at = session.get("issued_at")
    last_seen_at = session.get("last_seen_at")
    if issued_at is None or last_seen_at is None:
        return False                              # fail closed, not "assume new"
    if now < issued_at or now < last_seen_at:
        return False                              # a timestamp in the future cannot be trusted
    if now - last_seen_at >= IDLE_TIMEOUT_SECONDS:
        return False
    if now - issued_at >= ABSOLUTE_TIMEOUT_SECONDS:
        return False
    return True
```

Walk this in the order it was written, because the order encodes a design decision, not just a style preference. The two `is None` checks come first and refuse to guess: a session record missing either timestamp has not proven anything about its age, and treating an unknown age as "brand new" — which is what a convenient `.get(key, now)` default would do — is the exact fail-open shape [Lesson 03](03-break.md)'s malformed-input test exists to catch. The clock-skew check that follows refuses a session whose `last_seen_at` is somehow in the future relative to `now`, because a negative duration is not a small idle time, it is evidence the record should not be trusted at all. Only after both guards pass do the two real policy checks run, and they are two separate `if` statements rather than one combined boolean specifically so that each can be tested, read, and reasoned about on its own — a single line computing `active = (idle_ok and absolute_ok)` would behave identically today and would silently invite someone to "simplify" it back down to one clock during a future edit, which is exactly the regression this lesson's forbidden-outcome test exists to catch if it ever happens.

## Mint fresh on the authentication event, retire what came before

Lesson 02's claim does not have a code block in this fixture, because minting the actual new identifier happens inside the authentication module's login route, not inside this module's request parser — but the shape of the fix is worth stating precisely so it can be recognized wherever it is implemented: on a successful authentication event, generate a new session identifier from a cryptographically secure source, store it as the active session for that user, and explicitly invalidate whatever identifier the request that triggered the login carried, if any. "Explicitly invalidate" is the clause that separates a real fix from one that merely looks like one; a login handler that mints a new identifier and returns it to the browser, while leaving the pre-authentication identifier's server-side record untouched, has added a working door without removing the old one, and an attacker who planted the old identifier can walk through it exactly as before.

## Three attributes, three attackers

A session cookie's job does not end once its value is chosen correctly and its channel is right. `Secure`, `HttpOnly`, and `SameSite` are three separate response-side attributes a server sets when writing the cookie, and each one closes off one specific way an attacker could get at the cookie — not three redundant ways of saying "this cookie is protected."

| Attribute | Attacker capability it removes | What it does nothing about |
|---|---|---|
| `Secure` | A network-position attacker (a hostile Wi-Fi hotspot, a compromised router) reading the cookie off an unencrypted connection | Which site's pages can trigger a request that carries the cookie in the first place |
| `HttpOnly` | A script already running on the cookie's own origin — most often through an XSS bug — reading the cookie's value out of `document.cookie` | The cookie being sent to the wrong destination, or over a plaintext connection |
| `SameSite` | A different site's page causing the victim's browser to send this cookie along with a request it did not intend — the cross-site request forgery and cross-site-leak surface | A script that is already running on the cookie's own origin, which `SameSite` never touches |

A session cookie set with `Secure; HttpOnly; SameSite=Lax` (or `Strict`, depending on whether the notes app needs the cookie present on a cross-site top-level navigation such as an email link) has closed three distinct doors. It has not closed a fourth: nothing about any of the three attributes stops the same value from being copied into a URL by application code that reads the cookie and echoes it into a query parameter for some unrelated reason — that fourth door is [Lesson 01](01-property.md)'s subject, and it is a mistake to treat "we set the three flags" as proof that door is closed too, because none of the three attributes has anything to say about it.

> `set_cookie("sc_session", value, secure=True, httponly=True, samesite="Lax")` removes the network-eavesdropper, script-reading, and cross-site-request capabilities in one call. It does not remove the capability of a developer three months later writing `return redirect(f"/notes?access_token={value}")` for a "convenience" deep link — that regression is caught only by the channel check in Lesson 01's `session_from_request`, and by a reviewer who has internalized that these are four separate claims, not one.

## What a competent engineer believes here, and why it is wrong

**"We set `HttpOnly`, so the cookie is secure."** `HttpOnly` answers exactly one question — can page JavaScript read this value — and says nothing about `Secure` (plaintext transport) or `SameSite` (cross-site request attachment). A cookie can be `HttpOnly` and still be sent in the clear over `http://`, and still ride along on a forged cross-site POST, if the other two attributes were never set.

**"An idle timeout is a session lifetime policy."** An idle timeout answers "was this recently touched." A system that implements only an idle timeout has an unstated absolute lifetime of infinity, which [Lesson 03](03-break.md)'s six-day session made concrete: infinite is not a value anyone would choose on purpose if asked, and yet it is the value a policy silently has if only one of the two clocks is ever checked.

**"Minting a new session ID at login is optional if the old one was random enough."** Randomness defends against an attacker guessing an identifier they were never given. It does nothing for an attacker who already has a copy of one, which is precisely [Lesson 02](02-model.md)'s fixation scenario — the identifier's strength was never the property in question.

## What the framework does vs. what you still have to check

A framework's session middleware will typically default `HttpOnly` to true and leave `Secure` and `SameSite` for the application to set explicitly, because the framework cannot know whether the deployment is HTTPS-only or what the intended cross-site behavior is — those are the notes app's decisions, not the library's. No framework default enforces an absolute session lifetime; idle timeouts are common defaults, absolute caps are not, because an absolute cap is a product and risk decision (how much friction is acceptable) that a general-purpose library correctly declines to guess on the application's behalf.

## Practice

Run this only inside `labs/4.3/4.3-lab/`.

```text
python3 -m pytest labs/4.3/4.3-lab/tests --impl fixed
```

Then write, for SecureCollab's actual cookie-setting call, which of `Secure`, `HttpOnly`, and `SameSite` is already set, and which attacker capability is still open if any one of them is missing.

## Use it somewhere new

A magic-link email exchanges a one-time URL token for a cookie session; [Lesson 07 Transfer](07-transfer.md) asks which of this lesson's four controls — deny-on-query, mint-fresh, dual-clock lifetime, and the three cookie attributes — apply unchanged to the cookie that link exchanges into, and which one (the one-time nature of the link itself) is a fifth control this lesson has not covered yet.

## What this page is not doing

No live cookie-setting against a real host; the `set_cookie` call above is illustrative syntax, not a runnable snippet in this repository. Answer keys are not on this site.
