# 1.1 — Security as invariants under attack

Pass A specification only. No lesson prose, exploits, or implementations.

## Identity

- **id:** 1.1
- **slug:** security-as-invariants-under-attack
- **title:** Security as invariants under attack
- **phase / track / difficulty:** 1 / core / foundation
- **estimatedMinutes:** 240
- **prerequisites:** Entry profile (can ship a small API, Git, tests, basic SQL). Module 0.1 vocabulary recommended, not blocking for the Phase 1 spec pilot.
- **routeTags:** complete, accelerated, web-api, mobile
- **releaseMilestone:** none (feeds Gate 1; SecureCollab models precede M0)
- **masteryGate:** 1

## Objective hierarchy

1. Given a product description (SecureCollab or an unfamiliar sibling), produce a **system-specific invariant catalogue** that a reviewer can test—not a list of tools or CVE names.
   - Separate **desired property** from **mechanism** (encryption, login, a header, a scanner finding).
   - Express at least: confidentiality, integrity, availability, authenticity, authorization, accountability, privacy, and safety as *invariants of this system* (or explicitly mark one as out of scope with a reason).
   - Name **attacker capabilities** and **trust assumptions** for each invariant (who is in the TCB, what they can read/modify, time horizon).
2. Show that a control can fail its property, and that detection/recovery are part of the claim when prevention is not absolute.
   - Distinguish root cause, preconditions, impact, prevention, detection, recovery without naming a vendor product as the property.
   - Identify when a framework default is not an application guarantee.
3. Transfer: apply the same catalogue method to a **materially changed** product description (different assets, tenants, or offline clients) and explain what must be rewritten.

## Prerequisite concepts

- Difference between a running program, stored data, and a network message (entry profile).
- “User,” “server,” and “database” as informal roles—this module replaces them with property language.
- 0.1 terms if completed: vulnerability, threat, risk, control, assurance (recommended).

## Misconceptions

- Security *is* a list of vulnerabilities, a Top 10, or a green scanner.
- Confidentiality, integrity, and availability are universal checkboxes independent of the product.
- “We use TLS / JWT / bcrypt” *is* the security property.
- If the happy path works, the invariant holds.
- Privacy is the same as confidentiality; safety is the same as availability.
- A control that usually works needs no detection or recovery story.
- Framework or cloud “secure defaults” are the application’s guarantees.

## Concept map

```text
Asset (what is valued)
  -> Property / invariant (what must remain true under misuse, failure, attack)
       -> Attacker capabilities + trust assumptions + time horizon
            -> Mechanism (control) — never confused with the property
                 -> Evidence (test, log, review) that the property still holds
                      -> Detection / recovery when prevention is incomplete
```

Related later nodes (not taught here): authority (1.2), trust boundaries (1.3), risk and usability (1.4).

## Invariant prompts

- What must still be true if the client is hostile and fully modified?
- What must still be true if an operator, backup, or log pipeline is compromised?
- Who is allowed to cause which state change, and how would we *notice* a forbidden change?
- If this mechanism were public knowledge (open design), would the property still hold?
- Which property are we *not* claiming, and why is that an explicit non-goal?

## Threat-model prompts

- If this invariant is false, who is harmed and how (user, tenant, operator, bystander)?
- What is the smallest change to assets or actors that invalidates the catalogue?
- Which claims depend on the browser, the OS, the cloud provider, or the learner’s honesty in the lab?

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 1.1-LO-01 | concept-model | Property vs mechanism: eight named properties as invariants | 1 Property |
| 1.1-LO-02 | design-exercise | Sketch SecureCollab assets and write a first invariant catalogue | 2 Model |
| 1.1-LO-03 | mechanism-lab | Observe a local app claim (“passwords are hashed”) and restate the actual property | 3 Break (authorized local only: failed property, not a public exploit) |
| 1.1-LO-04 | design-exercise | Replace a named tool with the smallest trustworthy mechanism that would restore one invariant | 4 Build |
| 1.1-LO-05 | verification-lab | List forbidden outcomes and what evidence would show they did not occur | 5 Verify |
| 1.1-LO-06 | operations-exercise | For one invariant, note log/alert/revoke/recover if prevention is not absolute | 6 Operate |
| 1.1-LO-07 | transfer-challenge | Unfamiliar product card: catalogue without naming a scanner or Top 10 item | 7 Generalize |
| 1.1-LO-08 | code-review | Seeded README/security.md that confuses controls with properties (find the confusion) | 5 Verify |

## Lab briefs (not implementations)

**Lab `1.1-invariant-catalogue` (authorized scope: local course materials / synthetic SecureCollab description only).**

- **Invariant:** The learner’s catalogue is specific enough that a second person can mark each line as testable or as an unjustified mechanism-claim.
- **Forbidden outcome:** Submitting a tool list, a copied CIA triad definition with no system names, or instructions that target a non-lab system.
- **Evidence:** Versioned markdown (or YAML) catalogue in the learner’s notes for SecureCollab Phase 1; instructor rubric against Gate 1.
- **Non-goals:** No injection, no credential theft, no live-target work. Mechanism-lab 1.1-LO-03 uses a **local** toy service or fixture created for the course.

## Assessment blueprint

| Category | What is assessed | Artifact |
|---|---|---|
| Explain | Property vs mechanism; eight properties as system-specific invariants | Short written rationale in the catalogue |
| Design | Catalogue completeness for stated assets and non-goals | Invariant catalogue v1 for SecureCollab |
| Build | N/A at spec time; later a one-file fixture that *states* a property in tests | Placeholder until Pass B |
| Break | Identify a stated control that does not imply the claimed property | Annotation on a seeded “we are secure because X” claim (local) |
| Verify | Forbidden-outcome list and how it would be tested | Negative-evidence notes |
| Operate | Detection/recovery note for at least one non-absolute prevention | Operate paragraph |
| Communicate | Residual risk / explicit non-goals without compliance theater | Non-goals and residual-risk lines |

Gate 1 (with 1.2–1.4): given an unfamiliar product, define security without naming a particular tool or vulnerability and justify which outcomes matter most. Transfer-ready requires the unfamiliar-product card (1.1-LO-07), not only SecureCollab.

Mastery states: `not-attempted` | `developing` | `competent` | `transfer-ready`. Security-critical gaps cannot be hidden by high scores elsewhere (no compensating averages).

## Standards references

| source | version | status | requirementIds | url |
|---|---|---|---|---|
| Saltzer & Schroeder | 1975 | seminal | protection-principles (economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism, psychological acceptability, work factor, compromise recording) | https://web.mit.edu/saltzer/www/publications/protection/ |
| NIST CSF | 2.0 | final | GV, ID, PR, DE, RS, RC (Functions as *outcome* categories, not a control menu) | https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20 |

Pinned in `content/standards/pins.yaml` on 2026-08-23. Do not present CSF as a vulnerability standard or as ASVS.

## Review triggers

- SecureCollab adds a new asset class (files, webhooks, AI summarizer, billing simulation).
- A new principal class (support impersonation, mobile offline cache, background worker).
- Time horizon changes (long-lived backup vs session).
- A lesson author starts organizing later modules as a Top 10 rotation (reject; keep causal order).

## Time budget and SecureCollab / milestone dependencies

- **Budget:** ~240 focused minutes (authoring mix later: heavy on models; light on break/fix).
- **SecureCollab (blueprint §9.1 Phase 1):** asset, invariant, authority, boundary, and risk models—**before features**. This module owns the invariant catalogue; 1.2–1.4 extend authority, boundaries, and risk.
- **Milestones:** no M0 evidence yet. Catalogue becomes an input to M0 once Phase 2 exists.
- **Does not depend on** FastAPI/Next.js implementation details; stack defaults still apply to later labs.

## Operational considerations

- Accountability invariants imply what must be logged (and what must not, for privacy).
- Availability and safety invariants imply graceful degradation, not “the site is up.”
- Human action as part of a control (approval, recovery) must later be usable and WCAG-aware (1.4 / 4.2); this module only flags that usability is part of the property, not a UI skin.
- Compromise recording (Saltzer) is an invariant about evidence existing under attack, not a SIEM product name.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
| 2026-08-23 | Pass A quality-gate: spec completeness competent |
