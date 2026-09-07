# Session binding vs body vs copies

**Kind:** design-exercise
**Loop step:** 2 Model

## Could someone else name the company check from your scale map?

“We have row-level rules” is not this page. A map someone else can test names **session binding, body fields, where the database session variable comes from, cache/search/lake keys, and impersonation**.

This week’s freeze: local `tenant_for(session, body)`. No public company. The notes app binds company from the session. The JSON body is not the tenant.

## Picture: one binding, many copies

```mermaid
flowchart TD
  Bind[session tenant] --> Api[API query]
  Bind --> Cache[cache key]
  Bind --> Search[search index]
  Bind --> Lake[analytics copy]
  Body[JSON tenant] --> Untrusted[input only]
```

## Picture: Host header is not the company

```mermaid
flowchart LR
  Host[subdomain] --> Claim[looks like org]
  Bind[session] --> TCB[tenant_for]
  Host --> NotBind["not who is allowed"]
```

## Step 1: freeze pieces

| Piece | This system |
|---|---|
| People | member of A; support impersonator |
| Objects | notes; search docs; cache entries |
| Actions | `tenant_for`; query; index |
| Paths | JSON or GraphQL body; Host; JWT |
| What you trust | session binding |
| What you do not trust | body tenant; Host; client JWT org |
| Time | binding at request; copies after write |
| The rule | who is allowed for company context |

## Step 2: write cells

| Person | Object | Action | Decision |
|---|---|---|---|
| member A | tenant B | set from body | deny |
| session A | notes A | query | allow |
| row-level session var | tenant | SET from body | deny |
| cache | key | omit tenant | deny |

## Practice

Look in `labs/E5/e5-lab`, starting with `rls.py`.

## Use it somewhere new

Clinic `org_id` in a bulk GraphQL mutation. Same grain: body tenant overrides session must stay false.

## What can still go wrong

Silent impersonation; lake jobs that re-key on a body field.

## What this page is not doing

Do not treat a famous-bugs list as the definition of security. Answer keys are not on this site.
