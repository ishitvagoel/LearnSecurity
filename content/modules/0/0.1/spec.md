# 0.1 — Security engineering orientation

Pass A specification, deepened. Lesson prose lives in `lessons/`. A public URL is out of scope even if TCP connects. WSTG is a method catalogue, not a scanning licence. Do not mark Gate 0 complete from this orientation alone without the rest of Phase 0–1 evidence.

## Identity

- **id:** 0.1
- **slug:** security-engineering-orientation
- **title:** Security engineering orientation
- **phase / track / difficulty:** 0 / core / foundation
- **estimatedMinutes:** 240 (recomputed per `metadata-honesty.mdc`: 8,262 lesson words / 200 ≈ 41 + 45 Tier-1 lab minutes + 7 items × 12 = 84 + 60 transfer task ≈ 230, rounded to the nearest 30)
- **prerequisites:** None; this module opens the course.
- **routeTags:** complete, web-api
- **releaseMilestone:** none
- **masteryGate:** 0

## Objective hierarchy

1. Produce a **scope predicate** so `target_is_authorized("https://example.com/")` is false, named local lab hosts may be true, and a malformed or unparseable URL is also false rather than a raised exception.
2. Name attacker capabilities (a tired learner with a proxy, a learner who pastes a lookalike hostname) and trust assumptions (this repo's lab trees; official training apps named in a README; nothing about DNS, redirects, or `/etc/hosts` beyond the literal string checked).
3. Transfer: contractor asked to "quickly test our customer's WordPress" — without hitting that host.

## Prerequisite concepts

None. This module teaches the vocabulary the rest of the course uses: vulnerability, threat, risk, control, assurance, compliance, privacy, safety, resilience — and **authorization of the tester**.

## Misconceptions

- If it has a login page it is a lab.
- WSTG chapter titles are the syllabus.
- Defensive learning requires attacking strangers.
- Burp existing is authorization.
- A hostname that contains an allowed name is itself allowed.

## Concept map

Reachability (break) → written host allow-list (this module) → official Juice Shop on your machine OK. Residual: hosts-file aliases; redirects off localhost.

## Teaching claims

Five falsifiable claims, ordered by dependency. The module previously taught only the first of these across all eight lessons — "reachability is not authorization" repeated under eight headings, with a two-test lab that exercised the allow-list's happy path and nothing else: no boundary case, no malformed-input case, no anti-fake test, and no assertion that the checker itself fails safely rather than crashing. Naming the other four here, and building lab evidence for three of the five, makes the coverage contract checkable rather than aspirational.

1. **C1 — Reachability is not authorization.** For any URL evaluated by this course's tooling, a tester's ability to open a TCP connection, receive an HTTP response, or see a rendered login page is not the fact `target_is_authorized` decides on. The function returns `True` only if the parsed hostname is exactly one of three names a person wrote into `ALLOWED_HOSTS` — `127.0.0.1`, `localhost`, `lab.securecollab.test` — and returns `False` for every other host, answered or not, because a server answering a socket says nothing about who is permitted to open that socket in the first place. A public host that responds instantly, over TLS, with a professional-looking login form, is exactly as unauthorized as one that refuses the connection outright; the response is evidence the network path exists, not evidence anyone granted testing permission over it.
2. **C2 — A vocabulary term is not a target list.** For a host that is not on the written allow-list, citing the OWASP Web Security Testing Guide's chapter titles, the NIST NICE Framework's work-role titles, or the NIST Cybersecurity Framework's Govern/Identify outcome labels cannot move that host onto the list, because each of those documents describes a testing *method*, a *job description*, or a *governance outcome* — none of them is a record of who granted a specific tester permission against a specific host. WSTG names how to test an application that is already in scope; it does not decide which applications are in scope, any more than a cookbook decides whose kitchen you may use. A learner, a pull request, or a teammate who cites a standard as the reason a host is now testable has misread that standard regardless of which one it is, because scope is a fact about written permission, and none of these three documents is in the business of granting it.
3. **C3 — A scope check must fail closed on the unknown, not only on the known-bad.** For a URL `target_is_authorized` cannot parse — a malformed authority such as an unmatched IPv6 bracket, or an argument that is not a string at all — the function must return `False` rather than raise an exception or silently default to `True`, because a caller that receives an exception instead of a verdict has no principled way to tell "this is denied" apart from "this checker broke," and code elsewhere in a real system that catches an unexpected exception and proceeds anyway turns "I don't know" into "allowed" by omission rather than by decision. The rule stated in this module's own lesson — "if the URL cannot be parsed, deny" — is a claim about behavior, and a claim about behavior that the code does not actually enforce is not a rule; it is a comment.
4. **C4 — Noticing a denial is a different control from capturing what was denied.** For a host `target_is_authorized` denies, a system may record that the denial happened — a host string and a reason code — but must never store, log, or screenshot anything that host actually returned, because every byte read back from an unauthorized target is itself an unauthorized read of that target: the deny check's entire purpose was to prevent the exchange, and a pipeline that denies the checker's verdict and then fetches and keeps the response "for the ticket" has performed the exact action the deny existed to prevent, one step later than expected. A denied-host log line with a body attached is not a stronger record; it is the violation, filed.
5. **C5 — Allow-list membership is an exact match, and it does not travel.** For a hostname string to satisfy `target_is_authorized`, it must be one of the three written names exactly — not a string that starts with one (`lab.securecollab.test.evil.com`), not a string that ends with one (`evillab.securecollab.test`), and not a connection that merely *began* at an allowed host before a redirect, a DNS answer, or an `/etc/hosts` alias sent it somewhere else. The check runs against the hostname string it was given; it has no way to know, and makes no claim about, where a connection eventually lands after that string is resolved or followed, so a tester who starts a request at `lab.securecollab.test` and follows a redirect elsewhere has left the one fact this function verified and must treat the new destination as unverified until it, too, is checked.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 3 Break, 5 Verify | `test_localhost_lab_is_in_scope`, `test_named_lab_domain_is_in_scope`, `test_public_host_is_out_of_scope`, `test_case_and_scheme_do_not_change_the_public_verdict` (normal case, forbidden outcome, and a case/scheme boundary) | items.md #1 |
| C2 | 1 Property, 7 Transfer, 8 Review | Not directly code-testable — no function in this Tier-1 fixture takes a standard's name as input, so there is nothing for a test to assert on; a vocabulary-as-scope confusion is a citation error, not a code path. Modeled in `lessons/01-property.md` and `lessons/08-review.md`. | items.md #2 |
| C3 | 3 Break, 4 Build, 5 Verify | `test_malformed_and_non_string_url_fails_closed` (the anti-fake test in this pass; a URL with an unmatched IPv6 bracket, and non-string arguments, must deny rather than raise) | items.md #3, #5 |
| C4 | 6 Operate | Not directly code-testable — this fixture performs no I/O and fetches nothing, so it has no response body to capture or withhold; the failure C4 names happens in a caller this fixture does not model. Modeled in `lessons/06-operate.md`. | items.md #6 |
| C5 | 2 Model, 4 Build, 5 Verify | `test_lookalike_hosts_are_not_authorized` (boundary case: prefix/suffix lookalikes), `test_anti_fake_generalizes_beyond_the_three_literal_example_urls` (anti-fake test) | items.md #4 |

C1, C3, and C5 carry genuine lab assertions — three of five, exceeding the two-claim minimum — and C3 and C5's tests are new in this pass; the lab previously exercised only C1's happy path and forbidden outcome, with no boundary case, no malformed-input case, and no anti-fake test. C2 and C4 are declared honestly non-code-testable rather than mapped to a fabricated assertion: C2 is a claim about how a person reads a standard, which this fixture has no input channel for, and C4 is a claim about a caller's handling of a fetched response, which this pure predicate never produces because it never fetches anything.

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| Decide whether a URL is in scope by checking the parsed hostname against the written allow-list, not whether it answers | C1 | `lessons/01-property.md` §Connecting is not permission | `lessons/01-property.md` `target_is_authorized("https://example.com/")` walkthrough | `lessons/03-break.md` | items.md #1 | `lessons/07-transfer.md` contractor WordPress |
| Identify that a testing-method catalogue, a work-role title, or a governance outcome label cannot add a host to the allow-list | C2 | `lessons/01-property.md` §A guide is not a permission slip | `lessons/01-property.md` WSTG/NICE/CSF walkthrough | `lessons/08-review.md` | items.md #2 | `lessons/07-transfer.md` |
| State that a URL the checker cannot parse, or a non-string argument, must deny rather than raise or default to allowed | C3 | `lessons/04-build.md` §Denying is not the same as failing | `lessons/03-break.md` counterexample; `lessons/05-verify.md` | `labs/0.1/0.1-orientation` `test_malformed_and_non_string_url_fails_closed` | items.md #3, #5 | `lessons/07-transfer.md` |
| Determine that a hostname containing, prefixed by, or suffixed with an allowed name is not a member of the allow-list | C5 | `lessons/02-model.md` §An allow-list entry is a whole word | `lessons/04-build.md` lookalike-host table | `labs/0.1/0.1-orientation` `test_lookalike_hosts_are_not_authorized` | items.md #4 | `lessons/07-transfer.md` |
| Write the deny signal for an out-of-scope host without capturing anything that host returned | C4 | `lessons/06-operate.md` §Noticing is not keeping | `lessons/06-operate.md` worked incident | `lessons/06-operate.md` runbook exercise | items.md #6 | `lessons/07-transfer.md` |
| Transfer the reachability/vocabulary/fail-closed/exact-match rules to a contractor's customer-WordPress request and a company staging URL | C1–C5 | `lessons/07-transfer.md` | `lessons/07-transfer.md` contractor table | `lessons/07-transfer.md` write-up prompts | items.md #7 | (is the transfer task) |

## Known residuals

- Redirect chains that leave an allowed host for an unallowed one are named as a stop condition (C5) but not lab-tested: this Tier-1 predicate takes a single URL string and performs no network follow, so there is no redirect for a test to assert on. A future component-tier fixture with a real HTTP client could assert the follow-and-recheck behavior directly.
- `/etc/hosts` aliasing a public name to `127.0.0.1` is named as a residual in every lesson that reaches it, and is intentionally not solved by this check: `target_is_authorized` compares the string it was given, not the address that string eventually resolves to, and resolving it here would require a real DNS lookup this course's safety rules do not permit against arbitrary input.
- C4 (denial-signal vs. response capture) is modeled, not lab-tested, because this fixture never fetches anything; a future Tier-2 fixture with a real request path could assert that a denied host's body is never written to a store the test can inspect.
- IPv6 loopback (`[::1]`) is not in `ALLOWED_HOSTS`; it fails closed (denied) rather than being falsely accepted, which is safe but is a named gap, not a claim that IPv6 local testing is unsupported by design.

## Invariant prompts

- What must remain true for `https://example.com/`?
- What fails if a redirect leaves 127.0.0.1?
- What must `target_is_authorized` return for a URL it cannot parse, and why is "it raised an exception" not an acceptable substitute for that answer?
- What must be false about `"evillab.securecollab.test"` that is true about `"lab.securecollab.test"`?

## Threat-model prompts

- What can a tired learner paste into a proxy?
- What written artifact would make a company staging URL in-scope?
- Who benefits if a scope checker's parse failure is silently treated as "allowed" by whatever code calls it next?
- What residual remains if `/etc/hosts` aliases a public name to `127.0.0.1`?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/0.1/0.1-orientation`. Forbidden: public host treated as authorized; a lookalike hostname treated as an allow-listed one; a parse failure treated as an allow-listed one. Do not fetch example.com.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

NIST CSF 2.0, OWASP WSTG 4.2, NIST SP 800-181r1 (NICE), and WCAG 2.2 — live-checked against their canonical pages on 2026-09-18; see `content/standards/pins.yaml` for the fetched confirmation on each. This module deliberately mints no ASVS identifiers: `pins.yaml`'s ASVS entry records that modules 0.1 and 0.2 do not mint ASVS ethics/bridge IDs, because ASVS is a web/API requirements catalogue and this module's subject — a tester's own authorization, not an application's security requirements — is not in its scope.

- NIST CSF 2.0 (final, CSWP 29) — Govern/Identify outcome language, used only as vocabulary for *why* scope governance exists, never as a testing permit. C2.
- OWASP WSTG 4.2 (final, stable; v5.0 in development and must be labeled draft if ever cited) — a catalogue of *how* to test an application already in scope, not a decision about *which* applications are in scope. C2.
- NIST SP 800-181 Rev. 1 / NICE Framework (final, structure dated 2020-11-16; Components v2.2.0, 2026-04-28, are living work-role data, not a replacement for the SP) — workforce role language, used only to show that a job title is not a scope grant. C2.
- W3C WCAG 2.2 (Recommendation, 2024-12-12) — the scope/stop UI described in `lessons/02-model.md` and `lessons/06-operate.md` must be keyboard-operable and not color-only; this module cites WCAG 2.2 for that one property, not as a claim of full conformance.

## Review triggers

Any URL in-scope; no stop on redirect; live-target language; quiz as scan permission; a lookalike hostname accepted as an allow-listed one; a parse failure treated as an allowed verdict.

## Time budget and SecureCollab

Orientation. Python host allow-list stand-in only; SecureCollab itself does not exist as a running system until Phase 2, so this module's fixture is deliberately a predicate, not a slice of the reference application.

## Operational considerations

`out_of_scope`. Never store denied-host bodies. Stop and notify instructor.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: reachability is not authorization |
| 2026-09-18 | Deepen (B0 pilot, fourth of four): named five teaching claims (C1–C5) and a six-row coverage contract; C1, C3, and C5 carry genuine lab assertions (three of five, exceeding the two-claim minimum), C2 and C4 declared honestly non-code-testable with a stated reason each. Live-fetched and re-verified NIST CSF 2.0, OWASP WSTG 4.2, NIST SP 800-181r1/NICE, and WCAG 2.2 against their canonical pages on 2026-09-18 (recorded in `content/standards/pins.yaml`); all four citations were already accurate, and no ASVS identifiers were added, since this module's subject is tester authorization, not an application security requirement ASVS catalogues. Also corrected a bug shared with 1.4, 2.1, and 4.3 before their independent review: `module.yaml` carried `reviewer: pending` with `lastReviewedAt`/`nextReviewAt` set to real dates and no artifact under `content/progress/reviews/` — reverted both to `null` per `metadata-honesty.mdc`. Found and fixed a genuine latent bug in the lab's own `fixed/scope.py`: `urlparse` raises `ValueError` on a malformed authority (an unmatched IPv6 bracket) and `AttributeError`/`TypeError` on non-string input, and the pre-existing "fixed" implementation let that exception propagate out of `target_is_authorized` instead of returning `False` — directly contradicting this module's own stated rule in `lessons/04-build.md`, "if the URL cannot be parsed, deny." Added a `try/except` that fails closed, and a boundary test (`test_lookalike_hosts_are_not_authorized`) plus an anti-fake test verified by hand against two distinct plausible fakes (a hard-coded URL-string table, and a suffix-match comparison), taking the lab from 2 tests covering one claim to 7 tests covering three. |
