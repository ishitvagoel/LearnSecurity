# 1.4 — Risk, people, economics, usable security, and resilience

Pass A specification only. No lesson prose, exploits, or implementations.

## Identity

- **id:** 1.4
- **slug:** risk-people-economics-usable-security-resilience
- **title:** Risk, people, economics, usable security, and resilience
- **phase / track / difficulty:** 1 / core / foundation
- **estimatedMinutes:** 270
- **prerequisites:** 1.1–1.3 Pass A. Entry profile. 0.1 recommended, not blocking.
- **routeTags:** complete, accelerated, web-api, mobile
- **releaseMilestone:** none (completes Gate 1 evidence set; precedes M0)
- **masteryGate:** 1

## Objective hierarchy

1. Produce a **risk register** for SecureCollab with assumptions, uncertainty, user-harm scenarios, residual risk, and owners—not a heat-map of CVE names.
   - Model threat actors by **capability and incentive**; include human error, coercion, and abuse economics (work factor).
   - Treat **security friction and inaccessibility** as security outcomes (bypass, lockout, unsafe workarounds), not UI polish.
2. Design **graceful degradation**, detection, and recovery as part of the risk decision when prevention is not absolute (ties 1.1 operate + Saltzer compromise recording).
3. Transfer: change actor capability or a WCAG-failing recovery flow and show which residuals and 1.1–1.3 artifacts must be rewritten.

## Prerequisite concepts

- 1.1 properties; 1.2 authority; 1.3 boundaries and blast radius.
- Psychological acceptability named in 1.2 as deferred here.

## Misconceptions

- Residual risk is “the scanner is yellow.”
- Usability is the opposite of security; accessibility is a later compliance add-on.
- Work factor is “our crypto is 256-bit.”
- Users who bypass a control are the problem, not the control.
- Detection without recovery is a complete resilience story.
- NIST 800-63 is a password-complexity checklist.
- SAMM scores prove the product is secure.
- CISA Secure by Design means the customer bought MFA.

## Concept map

```text
Actor capability + incentive + user harm
  -> Residual risk given 1.1 invariants, 1.2 matrix, 1.3 blast radius
       -> Work factor vs asset value
            -> Friction / accessibility (will people bypass?)
                 -> Degrade / detect / recover (when prevention fails)
```

## Invariant prompts

- If a legitimate user cannot complete recovery without sight, memory, or a mouse, which invariant fails?
- What attacker capability is in-scope, and what is explicitly out of scope?
- What residual do we accept, who owns it, and when do we revisit?
- If prevention fails, what still must be true (detection, containment, recovery)?

## Threat-model prompts

- Who is harmed (user, tenant, coerced user, bystander), not only “the system”?
- What is the cheapest abuse that still pays (notifications, invites, exports)?
- Which assumptions are untested (honest lab, trusted operator, honest IdP)?

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 1.4-LO-01 | concept-model | Actors, incentives, work factor, residual risk vs vanity metrics | 1 Property |
| 1.4-LO-02 | design-exercise | SecureCollab risk register with assumptions and user-harm scenarios | 2 Model |
| 1.4-LO-03 | mechanism-lab | Local fixture: a “secure” recovery flow that is unusable without a mouse/visual CAPTCHA | 3 Break (authorized local only) |
| 1.4-LO-04 | design-exercise | Reduce friction without weakening the 1.1 invariant; document the trade-off | 4 Build |
| 1.4-LO-05 | verification-lab | Test plan for lockout, bypass, and inaccessible recovery as forbidden outcomes | 5 Verify |
| 1.4-LO-06 | operations-exercise | Degrade, detect, recover: one scenario with CSF Detect/Respond/Recover labels | 6 Operate |
| 1.4-LO-07 | transfer-challenge | Raise attacker capability or add coercion: rewrite residuals and Gate 1 defense | 7 Generalize |
| 1.4-LO-08 | code-review | Seeded risk register that lists tools instead of harm and residual | 5 Verify |

## Lab briefs (not implementations)

**Lab `1.4-risk-register` (authorized scope: local/synthetic SecureCollab only).**

- **Invariant:** Every high-impact 1.1 invariant has a residual, an owner, and a revisit trigger; inaccessible security flows are recorded as security failures.
- **Forbidden outcome:** Heat-map-only register; live-target “user testing”; real PII in harm scenarios.
- **Evidence:** Versioned risk register; WCAG-oriented review notes for one recovery/auth journey (no claim of full conformance yet).
- **LO-03:** Local UI fixture only.

## Assessment blueprint

| Category | What is assessed | Artifact |
|---|---|---|
| Explain | Actor vs vulnerability; friction as security | Written actor/incentive note |
| Design | Register completeness vs 1.1–1.3 | Risk register |
| Build | Deferred to Pass B | Usable recovery change on local fixture |
| Break | Unusable control as security failure | LO-03 annotation |
| Verify | Lockout/bypass/a11y forbidden outcomes | Test plan |
| Operate | Degrade/detect/recover scenario | CSF-labeled operate note |
| Communicate | Residual risk without compliance theater | Residual + owner + trigger |

Mastery states: `not-attempted` \| `developing` \| `competent` \| `transfer-ready`. No compensating averages. Transfer-ready requires LO-07.

Gate 1 (with 1.1–1.3): given an unfamiliar product, define security without a tool name and justify which outcomes matter most—including people and residual risk.

## Standards references

| source | version | status | requirementIds | url |
|---|---|---|---|---|
| CISA Secure by Design | current public guidance | final | customer-outcomes; secure-defaults | https://www.cisa.gov/securebydesign |
| NIST CSF | 2.0 | final | DE, RS, RC (and GV for residual ownership) | https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20 |
| NIST SP 800-63-4 | 4 | final | risk-management; customer-experience (not full authenticator catalog) | https://pages.nist.gov/800-63-4/ |
| WCAG | 2.2 | final | security-sensitive journeys; no mouse-only / visual-only / memory-only | https://www.w3.org/TR/WCAG22/ |
| OWASP SAMM | 2.0 | final | Governance/metrics awareness; vanity vs outcome | https://owaspsamm.org/model/ |
| Saltzer & Schroeder | 1975 | seminal | psychological-acceptability; work-factor; compromise-recording | https://web.mit.edu/saltzer/www/publications/protection/ |

Pinned in `content/standards/pins.yaml` on 2026-08-23.

## Review triggers

- New high-impact user journey (recovery, invite, impersonation, billing).
- Actor model change (insider, coerced user, bulk automation).
- Accessibility complaint or lockout incident.
- Residual accepted without owner or expiry.

## Time budget and SecureCollab / milestone dependencies

- **Budget:** ~270 focused minutes.
- Completes Phase 1 models for Gate 1. Inputs to M1 usable auth and 4.2.
- Does not complete Gate 1 until learner evidence exists (Pass B/C).

## Operational considerations

- Detection and recovery are residual-risk controls, not optional add-ons.
- Support tools must not become impersonation-without-audit (ties 1.2).
- Logging harm scenarios must stay synthetic in the course.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
| 2026-08-23 | Pass A quality-gate: spec completeness competent |
