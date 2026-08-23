# 1.3 — Trust boundaries and attack surface

Pass A specification only. No lesson prose, exploits, or implementations.

## Identity

- **id:** 1.3
- **slug:** trust-boundaries-and-attack-surface
- **title:** Trust boundaries and attack surface
- **phase / track / difficulty:** 1 / core / foundation
- **estimatedMinutes:** 240
- **prerequisites:** 1.1 (invariants) and 1.2 (authority map) Pass A. Entry profile. 0.1 recommended, not blocking.
- **routeTags:** complete, accelerated, web-api, mobile
- **releaseMilestone:** none (feeds Gate 1; diagrams precede M0 request-path evidence)
- **masteryGate:** 1

## Objective hierarchy

1. Given SecureCollab (or an unfamiliar product), produce an **annotated trust-boundary diagram** and an **attack-surface inventory** a reviewer can challenge.
   - Identify the **trusted computing base**, **entry points**, **transitive trust**, **shared mechanisms**, **isolation boundaries**, and **blast radius**.
   - Place 1.2 mediation checks *on* boundaries, not only inside a named service.
2. Explain **defense in depth** without assuming layers are independent (a second layer that shares the first layer’s identity or parser is not independent).
   - Distinguish browser/client, edge, application, worker, data store, and third-party as different trust (not just different boxes).
3. Transfer: add a CDN, queue, or mobile client and show which boundaries, surfaces, and blast radius change—and which prior invariants/matrix cells must be revisited.

## Prerequisite concepts

- 1.1: properties and attacker capabilities.
- 1.2: subjects, objects, complete mediation, ambient authority.
- Informal “frontend / backend / database” boxes — this module replaces them with trust and surface language.

## Misconceptions

- Drawing boxes labeled “secure zone” is a threat model.
- The TCB is “the server” or “the cloud provider.”
- Defense in depth means stacking products whose failures are correlated.
- The attack surface is the list of open ports or the OWASP Top 10.
- Clients are trusted if they use HTTPS.
- Shared caches, log pipelines, and CI runners are outside the product.
- Transitive trust (IdP, email, object storage) does not count as an entry point.
- Isolating tenants in the app makes blast radius independent of the database role.

## Concept map

```text
Asset + invariant (1.1)
  -> Subject/object/action (1.2)
       -> Trust boundary (where those checks must hold)
            -> Entry points + shared mechanisms = attack surface
                 -> Blast radius if this component is wrong
                      -> TCB = what must be right for the invariant
```

Shostack four questions (methodology-neutral): What are we working on? What can go wrong? What will we do? Did we do a good job? Full elicitation methods (STRIDE, LINDDUN) wait for 3.2.

## Invariant prompts

- What must remain true *across* this boundary if the component on the untrusted side is fully hostile?
- Which components must we trust for this invariant (TCB), and what happens if one is wrong?
- If two layers share a parser, identity, or key, are they one control or two?
- What shared mechanism (cache key, tenant ID, log sink) becomes a cross-user channel (least common mechanism)?

## Threat-model prompts

- What are we working on (scope, users, dependencies, trust boundaries)?
- What can go wrong at each entry point and shared mechanism?
- Who can we no longer trust if the IdP, email provider, or object store is compromised?
- How far does a worker or admin identity blast if stolen?

## Lesson inventory (titles only)

| Object id | Kind | Title | Loop step |
|---|---|---|---|
| 1.3-LO-01 | concept-model | TCB, entry points, transitive trust, shared mechanisms, blast radius | 1 Property |
| 1.3-LO-02 | design-exercise | Annotated SecureCollab trust-boundary diagram (browser, API, DB, later workers) | 2 Model |
| 1.3-LO-03 | mechanism-lab | Local fixture: a “second layer” that trusts the same unsanitized identifier as the first | 3 Break (authorized local only) |
| 1.3-LO-04 | design-exercise | Shrink TCB or split a shared mechanism; redraw blast radius | 4 Build |
| 1.3-LO-05 | verification-lab | Attack-surface inventory with “what evidence the surface is closed” | 5 Verify |
| 1.3-LO-06 | operations-exercise | Detect crossing a boundary (unexpected caller, unexpected egress) | 6 Operate |
| 1.3-LO-07 | transfer-challenge | Add CDN or mobile client: new boundaries, surfaces, and invalidated 1.1/1.2 artifacts | 7 Generalize |
| 1.3-LO-08 | code-review | Seeded diagram that puts the database inside the same trust box as the API | 5 Verify |

## Lab briefs (not implementations)

**Lab `1.3-trust-boundaries` (authorized scope: local course materials / synthetic SecureCollab only).**

- **Invariant:** Every data flow that can change a 1.1 invariant crosses a named boundary with a named check (or an explicit accepted residual).
- **Forbidden outcome:** Treating the client as trusted; omitting a shared cache/log/IdP; instructing tests against a public site.
- **Evidence:** Annotated diagram + attack-surface inventory; list of independent vs correlated layers.
- **LO-03:** Local toy showing correlated layers, not a network attack playbook.

## Assessment blueprint

| Category | What is assessed | Artifact |
|---|---|---|
| Explain | TCB vs attack surface vs blast radius; correlated vs independent layers | Short written legend on the diagram |
| Design | Completeness of boundaries vs 1.2 matrix paths | Annotated diagram + inventory |
| Build | Deferred to Pass B | Isolation or check placement on a local fixture |
| Break | Correlated “depth” or missing transitive trust | Annotation of LO-03 / seeded diagram |
| Verify | Surfaces listed with how closure would be tested | Inventory with evidence column |
| Operate | Unexpected caller/egress as a detection signal | Operate notes |
| Communicate | Residual trust in third parties without hiding it | Transitive-trust paragraph |

Mastery states: `not-attempted` \| `developing` \| `competent` \| `transfer-ready`. No compensating averages. Transfer-ready requires LO-07.

Gate 1 (with 1.1, 1.2, 1.4): describe an unfamiliar product’s security by properties, authority, and boundaries—not tools.

## Standards references

| source | version | status | requirementIds | url |
|---|---|---|---|---|
| OWASP Threat Modeling Project | maintained project guidance | final | four-questions; trust-boundaries (not a single methodology) | https://owasp.org/www-project-threat-modeling/ |
| OWASP ASVS | 5.0.0 | final | V15 Secure Coding and Architecture (chapter-level) | https://owasp.org/www-project-application-security-verification-standard/ |
| Saltzer & Schroeder | 1975 | seminal | least-common-mechanism; economy-of-mechanism; open-design | https://web.mit.edu/saltzer/www/publications/protection/ |

Pinned in `content/standards/pins.yaml` on 2026-08-23. Do not present STRIDE as mandatory here (3.2). Do not mix ASVS 4.x IDs.

## Review triggers

- New component: CDN, queue, mobile client, AI summarizer, webhook receiver.
- New third party: IdP, email, object storage, analytics.
- Shared cache, search index, or log pipeline added.
- Isolation claim (container, tenant schema) without independence analysis.

## Time budget and SecureCollab / milestone dependencies

- **Budget:** ~240 focused minutes.
- **SecureCollab Phase 1:** this module owns boundary diagram and surface inventory; spiral input when Phase 2 adds a real request path (M0).
- **Later:** 3.2 version-controlled threat model; 2.2 edge/CDN; 7.4 workers; 8.1 hostile client.

## Operational considerations

- Detection: unexpected identity at a boundary, unexpected egress, shared-mechanism collisions.
- Transitive trust failures need revocation/runbook hooks (later 10.5), noted here as residual.
- Logging pipelines are both evidence and a data-exfiltration surface (privacy vs accountability).
- WAF, CDN, or framework edge defaults are not the application TCB or an independent layer.
- Detection UX and accessibility of human response are designed in 1.4.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A initial specification |
| 2026-08-23 | Pass A quality-gate: spec completeness competent |
