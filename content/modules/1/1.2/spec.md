# 1.2 — Authority and protection

Pass A specification only. No lesson prose, exploits, or implementations.

## Identity

- **id:** 1.2
- **slug:** authority-and-protection
- **title:** Authority and protection
- **phase / track / difficulty:** 1 / core / foundation
- **estimatedMinutes:** 240
- **prerequisites:** 1.1 Pass A (invariant catalogue language). Entry profile. 0.1 vocabulary recommended, not blocking.
- **routeTags:** complete, accelerated, web-api, mobile
- **releaseMilestone:** none (feeds Gate 1; SecureCollab models precede M0)
- **masteryGate:** 1

## Objective hierarchy

1. Given SecureCollab (or an unfamiliar product), produce a **reviewable authority map and access matrix** that a second person can execute later as tests.
   - Name **subjects**, **objects**, **actions**, **delegation**, **capabilities** vs **ambient authority**, and where an access matrix (or equivalent) lives.
   - Apply **least privilege**, **complete mediation**, **fail-safe defaults**, **separation of privilege**, and **secure defaults** as design rules—not as product slogans.
2. Show that a missing check on an indirect path (cache, job, admin impersonation, bulk export) is a complete-mediation failure, not a “new vulnerability family.”
   - Distinguish deny-by-default failure states from fail-open “helpfulness.”
   - Separate **who is authenticated** from **what they may do** (authorization is not login).
3. Transfer: redraw the matrix after a **material change** (new admin role, support impersonation, or tenant). Explain which Saltzer principles were stressed.

## Prerequisite concepts

- 1.1: property vs mechanism; invariants name *who/what is trusted*.
- Informal idea of “logged-in user” — this module replaces it with subject, object, action, and delegation.
- Saltzer principles named in 1.1 open-design prompt; 1.2 operationalizes them for authority.

## Misconceptions

- Authentication *is* authorization.
- Roles in a UI are the access matrix.
- If the HTTP handler checks permission, every path is mediated (jobs, GraphQL, admin, files, search).
- “Admin” is one ambient superuser rather than separated privileges.
- Allow-by-default with a denylist of dangerous actions is fail-safe.
- Framework middleware “auth = True” is complete mediation.
- Capabilities and ACLs are the same mechanism; ambient authority is just “being logged in.”
- Secure by Design means shipping MFA as a paid add-on.

## Concept map

```text
Subject (principal, possibly a service or job)
  --delegates / presents--> Capability or authenticated context
       --requests--> Action on Object
            --mediated by--> Policy (matrix, ACL, relation, capability check)
                 --default on uncertainty--> Deny (fail-safe)
```

Ambient authority: leftover rights in the environment (process user, shared DB role, global “current_user”) that were not granted for this action.

Related: 1.1 properties; 1.3 trust boundaries (where mediation must occur); 4.4 executable authorization.

## Invariant prompts

- For this action, who is the subject, and was their authority **explicitly** granted for this object?
- What happens if the check is skipped on a retry, webhook, or worker?
- If the mechanism were public (open design), could a subject mint or copy authority they were not granted?
- Which two independent conditions must hold for the highest-impact action (separation of privilege)?
- What is the secure default for a new object or unknown subject?

## Threat-model prompts

- Where does ambient authority leak across tenants, roles, or background work?
- Who can delegate, and can they delegate more than they have?
- What attacker capability is “call any URL the user can see in DevTools” vs “compromise the worker identity”?
- Who is in the TCB for mediation: application policy, database role, or worker identity?

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 1.2-LO-01 | concept-model | Subjects, objects, actions, matrix vs capability vs ambient authority | 1 Property |
| 1.2-LO-02 | design-exercise | SecureCollab authority map and access matrix (org, member, note, file, admin) | 2 Model |
| 1.2-LO-03 | mechanism-lab | Local fixture: a handler that trusts ambient current_user without an object check | 3 Break (authorized local only) |
| 1.2-LO-04 | design-exercise | Restore complete mediation and least privilege on that path (structural, not a denylist) | 4 Build |
| 1.2-LO-05 | verification-lab | Turn matrix cells into forbidden-outcome tests (cross-role, cross-object) | 5 Verify |
| 1.2-LO-06 | operations-exercise | Revoke and expire: what logs prove who held which authority when | 6 Operate |
| 1.2-LO-07 | transfer-challenge | Add support impersonation or a worker: redraw matrix and name stressed principles | 7 Generalize |
| 1.2-LO-08 | code-review | Seeded diff that adds an admin JSON route without a policy check | 5 Verify |

## Lab briefs (not implementations)

**Lab `1.2-authority-matrix` (authorized scope: local course fixture / synthetic SecureCollab only).**

- **Invariant:** Every security-relevant action in the scoped matrix has an explicit subject–object–action rule; unknown pairs deny.
- **Forbidden outcome:** Cross-role or cross-object success on the local fixture; or any instruction to test a third-party/public app.
- **Evidence:** Versioned authority map + access matrix; later Pass B tests that encode forbidden cells.
- **LO-03:** Local toy only—demonstrate missing object-level check. No weaponized payloads; no live targets.

## Assessment blueprint

| Category | What is assessed | Artifact |
|---|---|---|
| Explain | Subject/object/action; ambient vs granted authority; authn ≠ authz | Short definitions tied to the map |
| Design | Completeness of matrix including one indirect path | Authority map and access matrix |
| Build | Deferred to Pass B | Policy check on a local fixture |
| Break | Identify a complete-mediation miss | Annotation of LO-03 / seeded route |
| Verify | Forbidden cells named as tests | Negative-test list |
| Operate | Revocation/expiry and audit of authority | Operate notes |
| Communicate | Why “admin can do everything” was rejected or bounded | ADR-style paragraph |

Mastery states: `not-attempted` \| `developing` \| `competent` \| `transfer-ready`. No compensating averages. Transfer-ready requires LO-07, not only the happy-path matrix.

Gate 1 (with 1.1, 1.3, 1.4): define security of an unfamiliar product without a tool name—including who may do what.

## Standards references

| source | version | status | requirementIds | url |
|---|---|---|---|---|
| Saltzer & Schroeder | 1975 | seminal | least-privilege, complete-mediation, fail-safe-defaults, separation-of-privilege, economy-of-mechanism, open-design | https://web.mit.edu/saltzer/www/publications/protection/ |
| CISA Secure by Design | current public guidance | final | secure-defaults, manufacturer-ownership | https://www.cisa.gov/securebydesign |
| OWASP ASVS | 5.0.0 | final | V8 (Authorization), V15 (Secure Coding and Architecture) — chapter-level until requirement IDs are pinned as `v5.0.0-…` | https://owasp.org/www-project-application-security-verification-standard/ |

Do not mix ASVS 4.x IDs. Do not treat CISA pledge language as ASVS Level 2 evidence.

## Review triggers

- New principal (support impersonation, CI bot, webhook signer, mobile client).
- New object class (files, GraphQL field, search index).
- Any path that runs without the HTTP middleware (workers, scripts, admin CLI).
- Multi-tenant cells added to the matrix.

## Time budget and SecureCollab / milestone dependencies

- **Budget:** ~240 focused minutes.
- **SecureCollab Phase 1:** this module owns the authority map; 1.1 owns invariants; 1.3 owns boundaries; 1.4 owns risk/usability.
- **Later:** 4.4 turns the matrix into executable tests; 7.2/7.4 extend to APIs and workers.
- **Milestones:** input to M1 (identity vertical slice), not M0 by itself.

## Operational considerations

- Complete mediation includes cached authorization, impersonation sessions, and break-glass admin—log grants, impersonation, and revocations.
- Fail-safe defaults: new tenants, new objects, and failed policy evaluation deny.
- Psychological acceptability (Saltzer) is flagged here and designed in 1.4/4.2: a matrix that users bypass is not complete mediation.
- Least privilege for **database roles** is noted as a later 5.5 concern; this module stays at application-authority language.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
| 2026-08-23 | Pass A quality-gate: spec completeness competent |
