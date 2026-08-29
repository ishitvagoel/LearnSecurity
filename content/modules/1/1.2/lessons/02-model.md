# 1.2-LO-02 — Build SecureCollab’s authority map and executable matrix

**Kind:** design-exercise
**Loop step:** 2 Model
**Standards:** Saltzer and Schroeder (1975, seminal); OWASP ASVS 5.0.0 (final) `v5.0.0-8.1.1`, `v5.0.0-8.1.2`, `v5.0.0-8.2.1`, `v5.0.0-8.2.2`, `v5.0.0-8.2.3`, `v5.0.0-8.3.1`, and `v5.0.0-8.4.1`.

## Can a second engineer turn your model into tests?

An authority diagram is useful only if it predicts allowed and forbidden effects. “Member → API → note” is a data-flow sketch. “An active member may read a note body only when the server-resolved membership tenant equals the note’s stored tenant” is an executable policy cell.

Your artifact for this lesson has three connected parts:

1. an authority map showing where grants originate and where decisions are enforced;
2. an access matrix describing the policy relation;
3. an enforcement inventory listing every in-scope path that can cause the effect.

The matrix says **what** should be allowed. The map and inventory say **where the claim can fail**.

## Freeze the product version first

SecureCollab Phase 1 is still a design model. It includes tenants, active memberships, tenant administrators, text notes, and privacy-safe authority events. It does not yet include files, public sharing, support impersonation, workers, webhooks, caches, mobile offline state, real PII, or production deployment.

Name deferred features as review triggers. Do not add them to the current allow matrix by accident, and do not pretend they are already protected.

## Step 1: enumerate subjects without hiding scope

Start with concrete subject types and attributes.

| Subject | Trusted authority attributes | What the subject controls |
|---|---|---|
| Unauthenticated requester | none | request path, identifiers, order, volume, client labels |
| Active Tenant A member | authenticated principal ID; current A membership resolved server-side | browser, request fields, known or guessed object IDs |
| Active Tenant B member | authenticated principal ID; current B membership resolved server-side | same capabilities, used adversarially across tenants |
| Tenant A administrator | active A membership plus scoped admin role | legitimate A administration requests; not B authority |
| Revoked former member | authenticated identity may remain; current membership is inactive | old session and previously observed identifiers |
| API policy path | policy version and server-resolved subject/object context | security decision; therefore in the trusted computing base |

“Backend” is too broad. The browser is not trusted merely because your code rendered it. The API is not wholly trusted merely because it is server-side. Name the smallest behavior the property depends on: for example, “the policy path resolves current membership and note tenant before release.”

Keep **originating subject** and **effective subject** separate when one actor operates for another. Phase 1 has no support impersonation or worker feature, so record those as absent. LO-07 introduces a machine principal specifically to test whether you can preserve that distinction.

## Step 2: split objects at security boundaries

“Note” may be too coarse. A note has at least:

- identifier;
- title or summary metadata;
- body;
- tenant binding;
- lifecycle state;
- authority decision evidence.

Different actions or fields may have different rules. A list view might expose identifiers and titles without exposing bodies. An API that serializes the whole database object can therefore violate field-level authority even if its route-level decision is correct. ASVS `v5.0.0-8.1.2` and `v5.0.0-8.2.3` make this distinction explicit; `v5.0.0-15.3.1` separately asks an application to return only required fields.

Other current objects are the tenant record and membership record. Exports and emergency sessions are modeled high-impact cases, not shipped features.

## Step 3: name actions as effects, not URLs

Use verbs that describe the protected effect:

- `note:list-summary`
- `note:read-body`
- `note:create`
- `note:update`
- `note:delete`
- `membership:view`
- `membership:grant`
- `membership:revoke`
- `tenant:bulk-export`

`GET /notes/{id}` is a route. The same read effect may happen through REST, GraphQL, search, export, cache, notification, restore preview, or an administrative tool. Complete mediation follows the effect across paths.

## Step 4: write cells with positive authority

Use `allow`, `deny`, or `out-of-scope`. Never leave a blank cell if the action is in scope; blank silently becomes whatever the implementation happens to do.

The following is a worked subset, not the full deliverable:

| Subject | Object | Action | State / grant | Decision | Why |
|---|---|---|---|---|---|
| Active member A | Note A-17 body | read | current A membership; note stored in A | allow | positive same-tenant rule |
| Active member B | Note A-17 body | read | no A membership or delegation | deny | cross-tenant forbidden outcome |
| Revoked former A member | Note A-17 body | read | identity valid; membership inactive | deny | authentication is not current authority |
| Active member A | Note A-17 summary | list | current A membership | allow | summary is explicitly in member view |
| Active member A | Note B-4 summary | list | no B authority | deny | aggregation is still access |
| Admin A | Membership A-9 | revoke | active scoped A admin | allow | narrow administrative grant |
| Admin A | Membership B-4 | revoke | admin role not bound to B | deny | no ambient global admin |
| Member A | Tenant A bulk export | execute | no export grant | deny | ordinary membership is insufficient |
| Admin A plus Admin A2 | Tenant A bulk export | approve | two current distinct approvals; policy-specific time window | allow for the lab’s design case | illustrative separation of privilege |
| Any subject | unknown object/action | any | no positive rule | deny | fail-safe default |

The two-approval export rule is an exercise assumption, not a universal industry requirement. The reasoning obligation is to justify why the impact warrants independent conditions, define what counts as independent, and describe failure and revocation.

## Step 5: add state and time

Static cells miss the hardest authority failures. Add transitions:

```text
invited -> active -> suspended -> revoked
                 \-> expired
```

For each transition, ask:

- who may cause it;
- whether old sessions, grants, caches, or jobs retain authority;
- when the change becomes effective;
- which decision version is recorded;
- what happens if the policy store is unavailable;
- how recovery or restore treats old authority state.

A revoked member may remain authenticated. A cached allow decision may outlive the membership version that justified it. Immediate invalidation can be technically difficult, but “eventually” is not a design. State the maximum window, affected actions, compensating detection, and information that cannot be recovered after disclosure.

ASVS `v5.0.0-8.3.2` is a Level 3 requirement about applying authorization changes immediately or using specified mitigation where that is impossible. This module uses it as an advanced review anchor, not as a hidden requirement for every learner system.

## Step 6: map authority sources and enforcement points

Draw arrows from authority source to decision to enforcement:

```text
identity evidence
      |
current membership + role ------> policy decision <------ stored note tenant/state
      |                                  |
grant / approval record -----------------+
                                         |
                   +---------------------+------------------+
                   |                     |                  |
              read-body path       list-summary path   admin mutation path
                   |                     |                  |
                   +---------- protected state / output ---+
```

For each enforcement point, record:

- operation/effect;
- decision input source;
- policy version;
- failure behavior;
- alternate paths;
- evidence;
- current test owner;
- review trigger.

Do not write “all routes use middleware” without enumerating routes and non-route effects. Middleware may authenticate the requester while object authorization still belongs at the service or persistence boundary.

## Worked reasoning: why list is not a harmless cousin of read

Suppose `read_note` correctly checks `note.tenant_id == subject.tenant_id`, but `list_notes` returns every note and the UI filters the result. The direct body-read cell is enforced; the list-summary cells are not.

The root cause is not that the UI filter is buggy. The server released objects before a trusted policy decision. The precondition is an authenticated requester who can call the list operation without the official UI. The impact depends on returned fields: identifiers may enable enumeration; titles may disclose content; whole objects may disclose bodies. The structural repair is to bind the server-side query or result construction to the current authority context and return only authorized fields. Hiding the list page, randomizing IDs, or adding a client filter does not change the release.

This example shows why the object and action vocabulary must be precise enough to predict the failure.

## Delegation worksheet

For one hypothetical “Alice asks Cara to review Note A-17 until 17:00 UTC” grant, record:

| Field | Required entry |
|---|---|
| Issuer | Alice, including the authority that permits delegation |
| Grantee | Cara’s stable subject identity |
| Action/object | `note:read-body` on A-17 only |
| Constraints | tenant, audience, purpose if enforced, and no further delegation unless justified |
| Issue/expiry | explicit trustworthy time basis |
| Revocation | current status/version and maximum effect delay |
| Use evidence | issuer, grantee, object, action, decision, policy/grant version, correlation ID |
| Limits | copyability, endpoint compromise, offline copies, or unavailable revocation check |

Do not assume a bearer link satisfies this record. Decide whether possession is intentionally the authority and, if so, how the capability properties are achieved.

## Required practice artifact

Produce `authority-phase1.md` or an equivalent one-page set containing:

1. product scope and explicit deferred principals/paths;
2. concrete subjects and trusted authority attributes;
3. objects split by field or state where rules differ;
4. actions as effects;
5. at least twelve allow/deny cells, including cross-tenant, revoked, list, admin, unknown, and high-impact cases;
6. at least five enforcement points or named future gaps;
7. one delegation record;
8. three authority-lifecycle transitions;
9. residual risks and review triggers.

## Peer feedback protocol

Give the artifact to a peer who did not help write it. They must be able to:

- turn at least six cells into test names without clarification;
- identify the trusted source of every policy attribute;
- find every blank or implicit default;
- name one path that bypasses each enforcement point;
- explain when a grant or membership stops authorizing;
- distinguish a policy decision from identity evidence and from a UI control.

Mark each challenged cell **executable**, **underspecified**, **ambient**, **stale**, or **out-of-scope but explicit**. Revise every underspecified, ambient, or stale cell.

## Transfer preview

Add a field-level rule: members may list note titles, but a restricted note’s body needs a separate grant. Which original cells split? Which query or serializer becomes an enforcement point? Which tests now need to distinguish summary from body? If your matrix cannot answer, it was too coarse.
