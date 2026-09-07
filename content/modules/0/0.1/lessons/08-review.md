# Would you merge this “any URL is in scope”?

**Kind:** code-review
**Loop step:** Review
**Standards:** CSF 2.0 GV. WSTG 4.2 as a list, not a licence.

## Review the practice files as if they were the course helper

Review `labs/0.1/0.1-orientation/vulnerable/` as a pull request for a course tool. Check whether `target_is_authorized` still returns true for a public host.

## Picture: any URL the proxy can open

**Any URL the proxy can open**.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would falsify it?"}
  Q -->|"example.com authorized"| Property["A rule - good if tested"]
  Q -->|a proxy is installed| Mechanism[A tool]
  Q -->|a guide mapped| False[False assurance]
```

A public host still has to be denied. Without a hostname allow-list, example.com stays authorized.

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

## Use it somewhere new

A contractor change that “added the guide and a proxy” without a host allow-list is a skipped-check review. What would still keep `example.com` out of scope after someone adds a proxy?

## What this page is not doing

A comment that says “do not scan production” does not own the allow-list. Keep the finding open until someone does. Do not fetch a public host to prove the finding.
