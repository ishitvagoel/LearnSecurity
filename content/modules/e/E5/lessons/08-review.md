# Would you merge this body-chosen company?

**Kind:** code-review
**Loop step:** Review

The answers are not on this page. Do not open the keys file until someone has looked at your review.

## What you are reviewing

A colleague ships notes-app company binding. Don't just tally suspicious lines. Check whether `tenant_for({"tenant": "A"}, {"tenant": "B"})` still returns `"B"`, compare that with the module rule, and write changes a developer can verify.

The folder `labs/E5/e5-lab/vulnerable/` is the change. Review it as if it were the notes app’s note query. The check you already ran (`test_body_cannot_switch_tenant`) is the rule test. A comment “will bind later” is not. The JSON body is not the tenant. Body tenant overrides session is the smell. Bind tenant from the session is the structural change.

## Picture: company taken from the body

Look at this first: **company taken from the body**. Label it rule, tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|body B becomes tenant| Property["Rule - good if tested"]
  Q -->|RLS is on| Mechanism[Tool - session variable]
  Q -->|famous-bugs mapped| False[False assurance]
```

Keep this: session A plus body B is A. If that call never includes session binding, that body-wins path is still open. A row-level screenshot does not replace that check.

Cache keys without company are leftover. Silent impersonation is a later topic. Do not skip `test_body_cannot_switch_tenant`. Do not claim a course gate. Do not probe a live company to prove the finding.

## Problems to find (name them yourself)

- Company taken from the body
- Row-level session variable set from JSON
- Cache key without company
- Support impersonation silent

Also reject: live product probes; shipping without re-running `test_body_cannot_switch_tenant`; keys in lessons; claiming a course gate; treating a famous-bugs list as the syllabus.

## Common mix-ups

- Row-level rules replace the app check
- Subdomain is an unforgeable company
- Scale means identity products instead of who-is-allowed
- A relationship-graph product is `tenant_for`
- GraphQL `org_id` is a different rule

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false assurance, suggested structural change, leftover you will **not** delete. Tie at least one to `test_body_cannot_switch_tenant`. Do not open the keys file.

## Use it somewhere new

Clinic change that “enabled row-level rules and mapped a famous-bugs list” without session binding is an incomplete review of a body-chosen company. Name the independent falsehood that would still keep body B from becoming the company.

## What this page is not doing

Do not merge by adding a comment “will bind later.” That comment is leftover without an owner. Do not send `org_id` to a public product to prove the finding.
