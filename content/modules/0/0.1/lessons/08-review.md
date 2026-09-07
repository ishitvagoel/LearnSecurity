# Would you merge this “any URL is in scope”?

**Kind:** code-review
**Loop step:** Review
**Standards:** CSF 2.0 GV. WSTG 4.2 as catalogue, not a licence.

## Review the practice files as if they were the course helper

Review `labs/0.1/0.1-orientation/vulnerable/` as a pull request for a course tool. Don't just tally suspicious lines. Check whether `target_is_authorized` still returns true for a public host, compare that with the rule, and write changes a developer can check.

The answers are not on this page. Do not open the keys until your review has been evaluated.

## Picture: any URL the proxy can open

Look at this first: **Any URL the proxy can open**. Label it a rule, a tool, or false assurance before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"example.com authorized"| Property["A rule - good if tested"]
  Q -->|a proxy is installed| Mechanism[A tool]
  Q -->|a guide mapped| False[False assurance]
```

Keep this: public host denied. If that call never includes a hostname allow-list, that leftover path is still open.

## Problems to find (name them yourself)

- Any URL the proxy can open
- No stop when a redirect leaves 127.0.0.1
- Live-target language in a learner note
- A quiz score treated as permission to scan

Also reject: fetching example.com; keys in lessons; claiming the first check-in; “it has a login page”; robots.txt as permission; a job title as a permit.

## Common mix-ups

- If it has a login page it is a lab
- Testing-guide chapter titles are the course
- Defensive learning requires attacking strangers
- The computer answering is permission
- A cloud Juice Shop you found is in-scope because the project is “official training”

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, whether it is a rule or false assurance, a suggested structural change, leftover risk you will **not** delete. Tie at least one to `test_public_host_is_out_of_scope`.

## Use it somewhere new

A contractor change that “added the guide and a proxy” without a host allow-list is a skipped-check review. Name the independent falsehood that would still keep `example.com` false.

## What this page is not doing

Do not merge by adding a comment “do not scan production.” That comment is leftover risk without an owner. Do not fetch a public host to prove the finding.
