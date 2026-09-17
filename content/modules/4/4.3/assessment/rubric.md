# 4.3 assessment (learner-facing — no answers)

**Practical evidence, not a compensating average.** States: not attempted | developing | competent | transfer-ready. Every critical invariant below needs satisfactory evidence on its own; a strong answer on one claim never substitutes for a missing one on another.

## Module

Sessions, cookies, and tokens — five teaching claims (C1–C5), named in `spec.md` §Teaching claims: the URL as a channel, binding a session to the authentication event, dual idle/absolute lifetime, server-side revocation, and the three distinct cookie attributes.

## Evidence checklist

- [ ] Session protocol/state diagram (Lesson 02) showing at minimum: anonymous → authenticated (with a fresh identifier minted, the old one retired), and the three ways an authenticated session ends — idle expiry, absolute expiry, revocation
- [ ] Local reproduction of both this module's forbidden outcomes (Lesson 03): a session established from a query-string token, and a session kept "active" past its absolute lifetime by activity alone
- [ ] Lab `labs/4.3/4.3-lab`: `vulnerable/` tests show 3 of 9 failing for the stated security reasons — the query-string channel and the missing absolute-lifetime check; `fixed/` tests show 9 of 9 passing
- [ ] Assessment items (`content/modules/4/4.3/assessment/items.md`) attempted with written reasoning, not single-word answers
- [ ] Seeded review (Lesson 08) completed via the four-question checklist — do not open the key first
- [ ] Operate signals for both this module's failure classes: `query_token_rejected` and `session_expired reason=idle|absolute`, plus a distinct `session_revoked` signal for explicit logout — none of them carrying the token or session identifier value
- [ ] Transfer task (Lesson 07) naming which of C1–C5 is specific to a redemption moment, for a clinic deep link and a magic-link email

## Rubric

| Result | Meaning |
|---|---|
| Developing | Names one claim (usually C1, "don't put it in the URL") without the other four; JWT-format or HTTPS-transport slogans offered as evidence for a channel, binding, lifetime, or revocation claim; missing forbidden-outcome lab evidence for either C1 or C3 |
| Competent | All five claims stated as system-specific properties of SecureCollab, not tool names; both lab forbidden outcomes reproduced and mapped to the claim each one tests; the cookie-jar-vs-URL distinction from the browser-security-model module applied correctly |
| Transfer-ready | Lesson 07's transfer task completed, correctly separating module 6.6's single-use link property from this module's C2 redemption-binding claim, without Top 10/scanner language standing in for either |

Knowledge check (retryable, 80% threshold): the nine module-specific items in `content/modules/4/4.3/assessment/items.md`.

## Seeded review

Use the local `vulnerable/` artifact via Lesson 08's four-question checklist. Intended findings and banding live only in `content/assessment/keys/4.3.md`.
