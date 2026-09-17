# 4.3 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/4.3.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — rule, tool, or false assurance

Four statements a reviewer might find in a pull request touching SecureCollab's session parsing:

**A.** "`session_from_request` has no code path that returns a value read from the query string, under any parameter name."
**B.** "We added a `Referrer-Policy: no-referrer` header to every response."
**C.** "We use HTTPS everywhere, so a token in the query string can't be intercepted."
**D.** "We added a check that rejects the request if `access_token` specifically appears in the query dict."

Sort each statement into **rule**, **tool**, or **false assurance**, and for each one that is not the rule, name specifically what it would need to add or change to become one.

**Claim assessed:** C1 · **Outcome:** Identify which channel(s) a candidate session value arrived on and justify rejecting the query string

## 2. Discrimination — property vs. mechanism for session binding

Four statements about a login flow:

**A.** "Session identifiers are generated with a cryptographically secure random-number generator, 256 bits of entropy."
**B.** "An identifier that exists in the browser before a successful login must not be the identifier that carries authority after it; login mints a new one and retires the old one."
**C.** "Our load balancer has never logged two requests with the same session ID from different IP addresses."
**D.** "The login form uses HTTPS and a CSRF token."

Identify which statement states the property this module calls C2, and which three are mechanism or proxy claims. Rank the three mechanism claims by how close each comes to being real evidence for the property.

**Claim assessed:** C2 · **Outcome:** Explain why an identifier that existed before a login event must not be the identifier that carries authority after it

## 3. Diagnosis — a lifetime checker's gap

```python
def session_is_active(session: dict, now: float) -> bool:
    issued_at = session.get("issued_at")
    last_seen_at = session.get("last_seen_at")
    if issued_at is None or last_seen_at is None:
        return False
    return now - last_seen_at < 900
```

This checker is not `vulnerable/token.py`, and it is not `fixed/token.py` — it is a third implementation. Give it a session record with `issued_at` fourteen days before `now` and `last_seen_at` five seconds before `now`. Name the root cause of why this function reports the session active, the precondition under which the gap matters in practice, and the impact if it ships this way — as three distinct answers, not one answer restated three times.

**Claim assessed:** C3 · **Outcome:** Decide whether a session is still active under a stated idle/absolute policy

## 4. Diagnosis — reading a candidate fix

A teammate proposes this fix, reasoning that it correctly adds the missing absolute-lifetime check:

```python
def session_is_active(session: dict, now: float) -> bool:
    issued_at = session.get("issued_at", now)
    last_seen_at = session.get("last_seen_at", now)
    if now - last_seen_at >= 900:
        return False
    if now - issued_at >= 43_200:
        return False
    return True
```

Determine, without running any code, whether this fix passes a test that supplies a session record with **no `issued_at` key at all** and a `last_seen_at` five seconds before `now`, and explain your reasoning by tracing that exact input through this exact function.

**Claim assessed:** C3 · **Outcome:** Decide whether a session is still active under a stated idle/absolute policy

## 5. Diagnosis — a cookie-setting call

```python
response.set_cookie(
    "sc_session", value,
    secure=True,
    httponly=True,
)
```

Name the one attacker capability this call leaves open that the module's cookie-attribute claim (C5) would otherwise close, state the specific class of request that capability enables against this cookie, and name the one-line change that would close it.

**Claim assessed:** C5 · **Outcome:** Choose Secure/HttpOnly/SameSite and name the capability each removes

## 6. Design — logout under a constraint

Two engineers propose a fix for a bug report that a user's "logged out" session still works from a second browser. Engineer A proposes shortening the client-side cookie's `Max-Age` so it expires sooner on its own. Engineer B proposes adding a server-side revoked-session set that every request's session check consults, populated by the logout handler. Under the constraint that the fix must make the second browser's copy of the same token stop working **immediately**, not merely sooner, choose between the two proposals and defend your choice, including the specific residual risk your chosen fix still leaves open.

**Claim assessed:** C4 · **Outcome:** Distinguish server-side revocation from client-side cookie deletion

## 7. Design — two clocks under a constraint

SecureCollab's product team wants "a session that doesn't log people out while they're actively working, but that still limits how long a stolen token stays useful." Propose specific idle and absolute timeout values that satisfy both halves of that request, and state which of the two numbers is doing the actual work of limiting a stolen token's useful life, and why the other number alone would not.

**Claim assessed:** C3 · **Outcome:** Decide whether a session is still active under a stated idle/absolute policy

## 8. Transfer — clinic deep link and magic-link email

Using the clinic and magic-link scenarios from `lessons/07-transfer.md`, state which of this module's five claims (C1–C5) transfer unchanged to a one-time link delivered by SMS or email, which one is specific to the redemption moment rather than to the link itself, and why "the link is one-time" does not, by itself, satisfy that one claim.

**Success criteria:** Your answer must name C2 specifically as the claim tied to the redemption moment, must explain that a one-time link's single-use property (owned by module 6.6) is a different guarantee from whether the *session that results from redeeming it* was freshly minted rather than a continuation of the link's own token, and must state that all five claims still apply to whatever session comes out the other side of redemption.

**Claim assessed:** C1–C5 · **Outcome:** Transfer the channel, binding, lifetime, and revocation rules to a clinic appointment deep link and a one-time magic-link email

## 9. Operate — the expiry and revocation signal

Write the two distinct log lines your system would emit when a session ends: once for hitting an idle or absolute lifetime limit, and once for an explicit logout. State which field distinguishes the two cases, which field must never appear in either line, and why a single `session_ended` event with no reason code would be operationally worse than two distinct ones, even though both indicate the same session is no longer usable.

**Claim assessed:** C3, C4 · **Outcome:** Distinguish an idle/absolute lifetime expiry from an explicit logout in the operational signal each one emits, without letting either collapse into the other or leak the session value

---

## Evidence checklist

- [ ] Session protocol/state diagram naming every transition (Lesson 02), including the login-mints-fresh-identifier transition
- [ ] Local reproduction of both forbidden outcomes: a query-string token, and an idle-refreshed session outliving its absolute lifetime (Lesson 03)
- [ ] Lab `labs/4.3/4.3-lab`: forbidden outcomes named as **a session established from a query-string token** and **a session's activity alone extending it past its absolute lifetime**
- [ ] `vulnerable/` tests show 3 of 9 failing for the stated security reasons; `fixed/` tests show 9 of 9 passing
- [ ] Transfer answer (item 8) naming which claim is redemption-specific, distinguishing it accurately from module 6.6's single-use property
- [ ] Operate signal (item 9) that carries no session identifier or token value
