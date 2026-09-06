# Role times field is a table, not a dump

**Kind:** design-exercise
**Loop step:** 2 Model

## Could someone else name pytest cases from your field table?

“Object authz is on” is not this page. A table someone else can test names **role, field, and every serializer**.

This week’s freeze: the notes app’s local `resolve(role, field)`. No live GraphQL.

## Picture: three grains

```mermaid
flowchart TD
  Fn["function permission"] --> Obj["object x company"]
  Obj --> Field["field read"]
```

Passing GET `/notes/{id}` (4.4) does not decide `secret_internal`. Passing last week’s extra-key write check (cannot *write* `is_admin`) does not decide who may *read* a field.

## Picture: a UUID is not a grant

```mermaid
flowchart LR
  Id["note UUID"] --> Locate[locator]
  Locate --> Grant{"object grant?"}
  Grant --> Fields["field table"]
```

Identifiers find a row. They do not authorize fields. Obscure identifiers are not capabilities. Famous “broken object / property / function” lists are awareness after this sentence.

## Step 1: freeze the pieces

| Piece | This system |
|---|---|
| Who | member; service role |
| What | `display_name`; `secret_internal` |
| Actions | `resolve` |
| Paths | REST JSON; GraphQL; CSV; search |
| What you trust | server-side role × field |
| What you do not trust | `?fields=`; GraphQL selection sets; UI hide |
| Time | current role; cached dump after a role change is advanced leftover |
| The cell | who-is-allowed at field grain |

## Step 2: write cells the practice can fail

| Who | What | Action | Decision |
|---|---|---|---|
| member | `display_name` | resolve | allow |
| member | `secret_internal` | resolve | deny |
| service | `secret_internal` | resolve | allow-audited |
| SPA hide | `secret_internal` | omit | not what you trust |

## Practice

Draw the table so someone else could name pytest cases. Point at `labs/7.2/7.2-lab` file `field.py`.

## Use it somewhere new

Clinic SSN; search snippets; bulk update of hidden fields (write grain is 7.1, read grain is this map).

## What can still go wrong

Later worker dumps (7.4). Stale serializers after a role change (advanced). Debug toolbar.

## What this page is not doing

A famous-bugs list as the definition of security. Answer keys are not on this site.
