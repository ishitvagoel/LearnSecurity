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

## Teaching claims

Five falsifiable claims, ordered by dependency. The module previously taught all five implicitly across the lessons without naming them; naming them here makes the coverage contract checkable and stops any one claim from being silently dropped in a future edit.

1. **C1 — Residual risk is a decision, not a color.** For SecureCollab's account-recovery confirm step, "residual risk" means a specific named harm that survives after the control is applied, with an owner and a revisit trigger. A heat-map cell or a scanner color is not evidence that a residual was named; it is evidence that a table was filled in.
2. **C2 — An unusable security control is a failed security control, not a UI defect.** If a legitimate account owner cannot complete the recovery-confirm step with a keyboard, a name a screen reader can speak, and a cue that is not color alone, the control has failed as a security control: the owner is locked out, or they take a shortcut (shared admin session, codes pasted into chat) that reintroduces the exposure the control existed to prevent. This is WCAG 2.2's success criteria (2.1.1 Keyboard, 4.1.2 Name/Role/Value, 1.4.1 Use of Color) applied to a security-sensitive journey, not a general accessibility audit of the product.
3. **C3 — Attacker effort and legitimate-user effort are two different costs that trade against each other.** Raising attacker work while ignoring user work produces "friction theater" — a control that demos well and fails a real user under stress, a missing pointer, or a screen reader. Lowering user work without preserving the who-is-allowed check produces a "convenience hole" — emailing a password, reading a code aloud, sharing an admin session. A change that only measures one side of this trade cannot be evaluated.
4. **C4 — Threat actors are named by capability and motive, not by a villain archetype.** "Hacker" and "insider" do not predict what recovery actually breaks against. The account owner with reduced ability, the person physically present who can force a confirmation, the caller impersonating support, and the bulk automator each have a different capability and a different motive, and each breaks a different part of the recovery path.
5. **C5 — A degrade/detect/recover path inherits the same accessibility and authority rules as the path it replaces, and must not create a new leak.** An alternate recovery route is still subject to C2 (it must itself be usable) and to the who-is-allowed check from C1/C4 (support reading a code aloud is a new, unreviewed grant, not a fallback). The operational signal that detects a failed recovery must never carry the secret the control exists to protect.

| Claim | Loop step(s) | Lab assertion | Assessment item |
|---|---|---|---|
| C1 | 1 Property, 2 Model, 6 Operate | Not code-testable — the lab is a pure predicate over `{name, keyboard, mouse_only, color}` and has no notion of an owner or a revisit trigger. Modeled instead in `lessons/02-model.md`'s register-row exercise (see the Coverage contract below). | items.md #1, #8 |
| C2 | 1 Property, 3 Break, 4 Build, 5 Verify | `test_recovery_control_is_usable_and_accessible`, `test_color_only_without_name_is_rejected`, `test_missing_keyboard_flag_is_not_silently_accepted` (all in `labs/1.4/1.4-risk-register/tests/test_recovery_a11y.py`) | items.md #2, #3, #4, #6 |
| C3 | 1 Property, 4 Build, 7 Transfer | Not directly code-testable — this claim is about a trade-off judgment between two costs, not a single object's shape. `test_whitespace_only_name_is_rejected` exercises C2's boundary (a name that satisfies bare presence but not screen-reader legibility), not C3 itself; modeled instead in `lessons/01-property.md`'s two-effort picture and `items.md`'s item 5 (the 24-hour-timeout scenario). | items.md #2, #5 |
| C4 | 1 Property, 2 Model | Not code-testable — coercion is a residual, not a unit test, and this is the correct call rather than a gap. | items.md #1, #7 |
| C5 | 6 Operate, 7 Transfer | `test_checker_rejects_a_bad_control_regardless_of_variant`, `test_checker_accepts_a_good_control_regardless_of_variant` (the anti-fake pair: an oracle that can be faked cannot be trusted to enforce a degrade path's rules either) | items.md #7, #9 |

C2 and C5 carry genuine lab assertions, satisfying the ≥2-claims-with-lab-assertions bar. C1, C3, and C4 are honestly declared non-code-testable rather than mapped to a test that does not actually assert them — pretending a unit test can check "an owner and a trigger were named" or "attacker effort was weighed against user effort" would be a worse defect than naming the limit plainly.

## Coverage contract

One row per outcome in `module.yaml`. Any empty cell is a blocker (`quality-gate` step 2).

| Outcome | Claim | Explanation | Worked example | Practice | Assessment item | Transfer |
|---|---|---|---|---|---|---|
| Produce a SecureCollab risk register with assumptions, uncertainty, user-harm, residual risk, and owners | C1 | `lessons/01-property.md` §Leftover risk is a decision | `lessons/02-model.md` §Step 3 harm scenarios (Kai, Remy, support-pressure) | `lessons/02-model.md` register-row exercise | items.md #1 | `lessons/07-transfer.md` clinic/bank register |
| Model threat actors by capability and incentive, including human error, coercion, and abuse economics | C4 | `lessons/01-property.md` §People are capability plus motive | `lessons/01-property.md` actor table (owner, person present, fake support, bulk automator) | `lessons/02-model.md` who-is-allowed rows | items.md #7 | `lessons/07-transfer.md` clinician/bank actor table |
| Treat security friction and inaccessibility as security outcomes | C2, C3 | `lessons/01-property.md` §Two kinds of effort | `lessons/03-break.md` broken `recovery.py` fixture | `labs/1.4/1.4-risk-register` vulnerable/fixed pair | items.md #2, #3, #4, #5, #6 | `lessons/07-transfer.md` mouse-only second factor |
| Include graceful degradation, detection, and recovery when prevention is not absolute | C5 | `lessons/06-operate.md` §Degrade without leftover permission | `lessons/06-operate.md` deny-line log example | `lessons/06-operate.md` practice (draft a deny line) | items.md #9 | `lessons/07-transfer.md` clinician degrade path |
| Transfer the register after changed actor capability or a failing accessible recovery flow | C1–C5 | `lessons/07-transfer.md` | `lessons/07-transfer.md` clinic/bank table | `lessons/07-transfer.md` write-up prompts | items.md #8 | (is the transfer task) |

## Known residuals

Genuinely out of scope for this module:

- Coercion by a physically present attacker → owned by C4/C1 as permanent residual; no module removes it. Recorded, not deferred to another module.
- A real accessibility audit of the full product → out of scope; this module's claim is scoped to one security-sensitive journey (recovery confirm), per WCAG 2.2's own security-sensitive-journey framing, not full conformance.
- A live user study → out of scope for a synthetic course lab; explicitly named as a limit in `lessons/02-model.md`.
- Support-impersonation as a shipped feature → residual named in the design table; a checked, audited support-assist flow is future work, not this module's forbidden-outcome fixture.

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
| CISA Secure by Design | current public guidance | **unverified** — canonical and independent fetches both returned 403 on the 2026-08-25 check recorded in `content/standards/pins.yaml`; do not present pledge language as an assurance baseline | customer-outcomes; secure-defaults | https://www.cisa.gov/securebydesign |
| NIST CSF | 2.0 | final | GV, **GV.RM** (Risk Management Strategy — the category this module actually uses for residual-risk ownership), DE, RS, RC | https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20 |
| NIST SP 800-63-4 | 4 | final | risk-management; customer-experience (not full authenticator catalog) | https://pages.nist.gov/800-63-4/ |
| WCAG | 2.2 | final | security-sensitive journeys; **2.1.1 Keyboard (Level A)**, **4.1.2 Name, Role, Value (Level A)**, **1.4.1 Use of Color (Level A)** — the exact success criteria the lab predicate checks; no mouse-only / visual-only / memory-only | https://www.w3.org/TR/WCAG22/ |
| OWASP SAMM | 2.0 | final | Governance/metrics awareness; vanity vs outcome | https://owaspsamm.org/model/ |
| Saltzer & Schroeder | 1975 | seminal | psychological-acceptability; work-factor; compromise-recording | https://web.mit.edu/saltzer/www/publications/protection/ |

CISA Secure by Design, OWASP SAMM 2.0, and NIST SP 800-63-4 are pinned because the misconception list above names them by name, and each is grounded by an explicit prose mention (not merely gestured at) in `lessons/01-property.md`: the maturity-score refutation names OWASP SAMM 2.0 directly rather than "industry lists"; the "buying a second factor is not the rule" clause names CISA Secure by Design's own "customer-outcomes, secure-defaults" framing directly; and the two-effort model's user-cost framing names NIST SP 800-63-4's risk-management and customer-experience emphasis directly, as the alternative to reading 800-63 as a password-complexity checklist.

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
| 2026-09-06 | Named Mental model H2s on remaining lessons; mermaid already present; independent review still required |
