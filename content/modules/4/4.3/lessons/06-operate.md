# Deleting the cookie is not revoking the session

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

Lessons 03 through 05 fixed a channel and a lifetime policy in code that runs on every request. This lesson is about an action that happens once, outside that steady flow — a user clicks "log out," or an administrator decides an account is compromised and wants every session for it gone right now — and asks what has to be true afterward for that action to have actually meant something. The uncomfortable answer is that the most common implementation of "log out" is a client-side action: the browser deletes its own cookie, or the application tells it to via `Set-Cookie` with an already-expired date. That deletion is real and it does change what the browser will send on its next request. It changes nothing about what the server will accept if the exact same token value arrives some other way — from a saved copy in a password manager's session-restore feature, from a proxy's access log an operator can replay, from a second device that logged in with the same session and never received any instruction to log out at all.

"Log out" that only clears client-side storage is a UI action wearing a security claim it never earned, and the gap between the two is not hypothetical: a session token is, by design, a bearer credential — whoever presents it is treated as the session's owner, with no further proof required — and a bearer credential's validity lives entirely in whatever the server checks it against. If that check is "does this look like a token," deleting one copy of the token changes nothing, because the server never looked at ownership in the first place. C4's claim is a state transition the server has to perform and remember: mark this specific identifier as no longer good, in state every future request will actually be checked against, not merely in the one browser that happened to click the button.

> Logout for session `sess_auth_7c1` must set a server-side fact — call it membership in a revoked set, or a `revoked_at` timestamp on the session record, or a signing-key rotation if the session is a self-contained token rather than a reference — such that a request presenting `sess_auth_7c1` after that point is rejected, from any browser, on any device, regardless of whether that particular browser ever received the logout instruction. A client-side cookie delete on browser A does not make browser B's copy of `sess_auth_7c1` reject; only a server-side check does.

## Picture: three requests, one after logout, only one server fact decides all three

```mermaid
sequenceDiagram
  participant Browser as Browser A
  participant Second as Browser B (second device)
  participant Server as SecureCollab server
  Browser->>Server: request with sess_auth_7c1
  Server-->>Browser: 200 OK (session valid)
  Browser->>Server: POST /logout
  Server-->>Browser: Set-Cookie: sc_session=; Max-Age=0 (client copy cleared)
  Second->>Server: request with sess_auth_7c1 (never told to log out)
  Server-->>Second: must be rejected -- only if the server marked sess_auth_7c1 revoked
```

The fourth message is where the claim either holds or does not. Browser A's copy is gone after the third message regardless of what the server does, because the browser deleted its own cookie on instruction. Browser B never received any instruction and still holds a live copy of the exact same identifier; whether that copy is honored on the fourth message depends entirely on whether the server, at the third message, wrote down a fact that the fourth message's check actually reads. A server that implements logout as "tell the browser to forget it" and nothing else will answer the fourth message with 200 OK, because nothing about that implementation ever touches server-side state.

## Notice, log, and recover without creating a second copy of the secret

Every operational signal in this module shares one constraint: naming the failure must not recreate it. A log line that records `query_token_rejected path=/notes request_id=req_43qs` is useful and safe; a log line that records the actual token value alongside the word "rejected" has turned a detection control into a second, permanent copy of the exact secret [Lesson 01](01-property.md) spent its whole argument trying to keep out of logs in the first place. The same discipline applies to session expiry and revocation: `session_expired reason=idle path=/notes` and `session_expired reason=absolute path=/notes` are two distinct, useful signals — distinguishing them tells an operator whether a policy boundary was hit by design or whether something (a stuck client, a misconfigured retry loop) is generating traffic against sessions that should have gone idle long ago. Neither line needs the session identifier itself, and if an incident investigation genuinely needs to correlate a specific session's history, that correlation belongs in a system built for that purpose, with its own access controls, not in the same general-purpose log every operator and log-shipping vendor can read.

Contrast the safe signal with the unsafe one directly:

```text
# safe:   session_expired reason=absolute path=/notes request_id=req_9f21
# unsafe: session_expired reason=absolute session=sess_auth_7c1 path=/notes
```

The second line differs from the first by exactly one field, and that one field is the entire session identifier — the same value [Lesson 01](01-property.md) spent its whole argument keeping out of a URL, now sitting in a log line that a log operator, a SIEM, or a log-shipping vendor's storage can read just as easily as an access log's query string. Writing the unsafe line does not make the expiry check itself wrong; the session still correctly stops working. It creates a second, independent way for the exact secret this module exists to protect to end up somewhere a leak-analysis of the URL alone would never think to look.

Recovery after a suspected leak has two parts that are easy to do only one of. Revoking the specific token that leaked closes that one door. Purging the log lines that already captured a query-string token (the failure mode [Lesson 01](01-property.md) covers) closes a door that revocation alone does not touch, because a log entry that has already been written and shipped to a retention system is not affected by anything that happens to the session record afterward — the token in that log line is exactly as usable to whoever can read the log after revocation as before it, until the log entry itself is found and removed, which for `access_token` a purge target and Referer collector may be a different system with a different retention policy than the one holding the session record.

## Why it happens, what it costs, how you stop it, how you notice, how you recover

| Slice | For this rule |
|---|---|
| Why it happens | "Log out" is built as a client-side convenience, and it looks complete from the browser that clicked it |
| What's already wrong | The server never wrote down a fact any other request's check will read |
| Trigger | A second device, a saved token, or a log replay presenting the "logged out" identifier |
| What it costs | A revocation the user believes happened has not happened anywhere the attacker's copy can see |
| How you stop it | A server-side revoked-set write on logout, checked on every request alongside the idle/absolute checks |
| How you notice | `session_expired reason=idle\|absolute\|revoked`, never the token value |
| How you recover | Revoke the specific token; separately, purge any log system that already captured a leaked value — revocation does not retroactively redact a log |

## What the framework does vs. what you still have to check

A framework's `logout()` helper will reliably clear whatever it was told to clear on the client — that part of the job is usually correct by default, because it is simple and stateless. Whether that same call also writes a server-side revocation fact depends entirely on whether the session is a *reference* (an opaque identifier the server looks up in its own store, where revocation is a straightforward delete or flag) or a *self-contained* token such as a signed JWT that carries its own claims and validates itself without a server-side lookup. A self-contained token's whole design point is not needing a server round trip to validate, which is also exactly why revoking one before its own expiry needs a separate mechanism — a deny-list of revoked token IDs, or rotating the signing key and accepting that every other token signed with it dies too — that the token format itself does not provide for free. Choosing self-contained tokens without choosing a revocation mechanism to go with them is choosing "logout does nothing server-side" without meaning to.

## Practice

Write the log line SecureCollab's logout handler should emit, and separately, write the server-side write that same handler must perform before that log line is written. If your answer to the second part is "nothing, the client clears its cookie," that answer is this lesson's claim failing, not a legitimate implementation choice.

## Use it somewhere new

A clinic staff member who logs out at a shared workstation, and a patient's magic-link session that should stop working the moment it has been used once, are both this lesson's claim wearing a different name. [Lesson 07 Transfer](07-transfer.md) asks which server-side fact each scenario needs written, and by which action.

## What this page is not doing

No live log dumps, no real session identifiers, no production incident replayed here. This page does not mark you as finished; it names what "log out" has to mean.
