# 7.2-LO-07 — Transfer: clinic member cannot resolve SSN

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-8.2.3`. API1/API3/API5 awareness after. WCAG 2.2 for the deny message.

## Change the workplace; keep a role × field matrix

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `resolve("member", "secret_internal")` must be false. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic member cannot resolve SSN. Also name bulk update and search highlighting leaking snippets.

**Product sketch:** EHR-lite patient page that omits the SSN column in the table, plus GraphQL `Patient { ssn }`.

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (clinician session selecting extra fields — not a live clinic);
2. trust assumptions (server role×field is TCB; UI omit and UUID are not);
3. forbidden outcome (`resolve("member", "ssn")` true, not “HIPAA”);
4. a test idea on a **local** fixture only (no public EHR);
5. residual (search snippets, CSV, 7.4 workers, Level 3 serializer cache);
6. WCAG if a human path is in the claim (do not announce the SSN in an error).

Use synthetic labels (`ssn` as a field name in a local fixture). Do not use real patient identifiers.

## Mental model: hidden column is not field authorization

```mermaid
flowchart LR
  Table["SPA omits SSN column"] --> Belief[UI believes hidden]
  GQL["selection set still asks"] --> Reality[dump if matrix is missing]
```

If the table omits the SSN column while `resolve` is always true, the cell is gone. FastAPI `response_model`, GraphQL “typed schema,” and UUID length do not check role × field. Search highlighting and CSV export are the same dump family — name them, do not run those systems here. A passing 4.4 object GET is a coarser grain: the member may read the *row* and still must not read the *field*.

The clinic rewrite still has to keep the SecureCollab fork: member × SSN false, member × display name true. Hiding SSN in the table without a member×field deny test leaves the serializer open. The local pytest analogue is `test_member_cannot_resolve_internal_field` — on a fixture, not a live EHR GraphQL query.

## What graders reject

| Reject | Why |
|---|---|
| “UUID is secret” | Locator, not a grant |
| Live clinic / public GraphQL | Lab policy |
| “We already have object authz” | 4.4 is a coarser grain |
| SPA omits column as field authz | Client is not TCB |
| HTTP 200 on object GET as this cell | Wrong observation (4.4) |

## Practice

One page. No keys. `labs/7.2/7.2-lab` is the only running system you may break. Do not query a public host.

## Non-goals

Live-target GraphQL. Real SSNs. Claiming Gate 7 from this page.
