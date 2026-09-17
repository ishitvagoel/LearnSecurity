# The same five rules, on a clinic deep link and a magic-link email

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

A clinic built on the SecureCollab pattern sends two kinds of links: an appointment reminder — `https://clinic.securecollab.test/visit?token=abc123` — that a patient taps from a text message, and a magic-link login email that exchanges a one-time code for a session, the subject of the workflow-and-exceptional-condition module's invite-token lesson. Both carry a token in a URL. Neither is this module's lab, and predicting what changes and what does not, before working through each in turn, is the actual exercise.

Do the prediction first: of this module's five claims, which ones are about the *URL as a channel* and therefore transfer unchanged to any link, clinic or otherwise; which ones are about what happens *after* the link is used and therefore depend on what the clinic's server does next; and which one is specific to a login event that a one-time link may or may not actually trigger?

## The appointment deep link

`?token=abc123` in a text message is [Lesson 01](01-property.md)'s claim wearing a different parameter name, and none of the four leak paths care what the parameter is called. The clinic's own access log will record it in plain text on the request that redeems it, exactly as SecureCollab's would. A `Referer` header fires if the visit page loads any third-party resource — a scheduling widget, a payment processor's iframe — and the full URL, token included, travels to that third party's server. Browser history on the patient's phone keeps the link indefinitely. The plausible-sounding defense that does not hold up any better here than it did in Lesson 01 is "it's SMS, not a browser, so `Referer` doesn't apply" — the moment the patient taps the link, it opens in a browser or an in-app browser view, and every one of Lesson 01's four leak paths is back in play; SMS delivery only changed how the URL arrived, not what happens once something renders it. One leak path is arguably worse here than in the notes app: a screenshot of a phone's messaging app, sent to a family member helping schedule the visit, is a completely ordinary, sympathetic action that leaks the token exactly as effectively as a malicious screenshot would.

What the clinic's server does with `token` after the tap is where the claims start to differ from a standing session. If `token` is genuinely one-time — valid for exactly one redemption, after which the server marks it used and refuses it again — then the query-string exposure is real but time-boxed: whoever else obtains a copy of an already-redeemed link gets a `410 Gone` or equivalent, not a working session. If the clinic instead treats `?token=abc123` as a standing credential that keeps working on every subsequent visit to that URL, the query-string exposure has become permanent, and the fix is not "move the token somewhere else" but "stop treating a URL parameter as anything other than a one-time redemption code, and exchange it for a proper session on first use." That exchange is exactly the authentication module's and this module's Lesson 02 territory: the moment of redemption is an authentication-adjacent event, and whatever session comes out of it needs a freshly minted identifier bound to that redemption, not a continuation of the token itself as though it were a session cookie.

## The magic-link email

A magic-link email token is the same one-time-redemption pattern with a different delivery channel, and the invite-token lesson owns the single-use property directly — a link that can be redeemed twice has failed that claim regardless of anything this module teaches. This module's claims pick up at the exchange: once the link is redeemed, the session the patient ends up with has to satisfy every claim from Lessons 01 through 06 exactly as if the patient had typed a password. It must not itself be carried forward in the URL as a standing session (C1) — the one-time code is spent, and a new cookie-based identifier replaces it. That new identifier must be freshly minted at the moment of redemption, not the same value the pre-redemption link carried (C2) — an attacker who somehow obtained the link before the patient clicked it, and who gets the server to treat the redeemed session as a continuation of the same value the link contained, has recreated fixation with a one-time code standing in for a password. The resulting session needs the same idle and absolute limits as any other (C3); "the patient proved who they are once, by clicking an emailed link" is not an argument for a longer-lived exception, because the link proved identity at one instant, and a stolen copy of the resulting cookie is exactly as dangerous an hour later as a stolen password-derived cookie would be. Logging out of that session has to actually revoke it server-side (C4), and the cookie it becomes needs the same `Secure`, `HttpOnly`, and `SameSite` attributes as any other session cookie (C5) — nothing about arriving via a one-time email link earns an exemption from any of the other four claims.

Trace one redemption concretely. A magic-link email carries `https://clinic.securecollab.test/login?code=one-time-9f21`. A correct exchange looks like:

```text
GET /login?code=one-time-9f21
  -> server marks code "one-time-9f21" as used -- the single-redemption claim
  -> server mints a NEW session identifier, e.g. sess_auth_c4e8 -- this module's C2
  -> server sets sc_session=sess_auth_c4e8 with Secure; HttpOnly; SameSite=Lax -- C5
  -> response redirects to /notes with the code no longer present in any URL -- C1
```

An incorrect exchange that still "works" for the patient looks almost identical, and the difference is exactly the line C2 governs: if the third step is skipped and the server instead sets `sc_session=one-time-9f21` — reusing the link's own code as the session value, rather than minting `sess_auth_c4e8` — the single-use property from the second step is still satisfied (the code cannot be redeemed a second time), while the fixation shape C2 forbids has been reintroduced anyway, because whoever saw the link before the patient clicked it now holds the exact value that became the standing session.

## Accessibility is part of this claim, not a separate checklist

If a human must read and tap the link — as opposed to an automated system consuming it — the flow has to meet the web accessibility baseline the rest of this curriculum treats as a security property, not a nice-to-have: link text that a screen reader can announce meaningfully, a redemption page that does not rely on color alone to show success or failure, and error states that are announced rather than only shown. A magic link that technically enforces every claim in this module but that a screen-reader user cannot successfully redeem has pushed that person toward whatever fallback exists — often a shared password, or a staff member reading the code aloud over the phone, both of which reopen risks this module spent six lessons closing. A security control that a meaningful fraction of real users cannot use is not fully deployed; it has a silent fallback path, and the fallback path is where the actual risk now lives.

## What is not good enough

| Reject | Why |
|---|---|
| "It's SMS, so `Referer` and access logs don't apply" | The link opens in a browser or in-app view; every Lesson 01 leak path re-applies the moment it renders |
| "The link proved identity, so the resulting session can be longer-lived" | C3 does not grant exceptions for how identity was proven; a stolen cookie is equally dangerous regardless |
| "One-time redemption means we don't need to mint a fresh session identifier" | 6.6's single-use property and this module's C2 are two separate claims; a one-time code that gets exchanged for a *continued* identifier still fixes that identifier |
| "The clinic uses HTTPS, so `?token=` is fine" | Restates Lesson 01's refuted belief with a clinic in front of it |
| A live clinic SMS or a real appointment link | Out of authorized scope for any exercise in this course |

## Practice

Write, for the appointment deep link and separately for the magic-link email: which of C1–C5 the scenario is still testing, which server-side behavior would satisfy each one, and which single claim is unique to the login-adjacent redemption moment rather than to the URL itself. Keep this write-up in your own notes; do not click a live appointment SMS or dump a mail server's logs to check your answer.

## What this page is not doing

Do not use live token replay, real session cookies, or a real clinic system. This page does not finish a check-in. Answer keys are not on this site.
