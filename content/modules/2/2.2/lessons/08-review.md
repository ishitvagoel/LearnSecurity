# Review of path-only cache keys

**Kind:** code-review
**Loop step:** Review

## What you are reviewing

You are reviewing a notes-app edge cache. Label each claim **rule**, **tool**, or **false assurance**. Say whether company B can read company A’s body if they ship. Start at the store key. An HTTPS checkbox is the wrong starting place.

Reconstruct whether the store still keys only on path. Compare that with the rule. Write changes a developer can verify. `test_other_tenant_does_not_receive_cached_body` is the check. “Will add Vary later” is a postponement.

## Picture: problems to find (name them yourself)

**`Cache-Control: public` on `/notes/{id}`**.

```mermaid
flowchart TD
  Claim[Change claim] --> Q{What would falsify it?}
  Q -->|company B get returns company A body| Property["Rule - good if checked"]
  Q -->|"we use TLS 1.3"| Mechanism[Tool - ask which hop]
  Q -->|HTTPS so cache is safe| False[False assurance]
```

For each claim and each branch: label **rule**, **tool**, or **false assurance**.

Problems to find (name them yourself; do not open the keys file):

- `Cache-Control: public` on `/notes/{id}`
- Key is path only
- Comment “TLS so cache is safe”
- Purge API not in the incident runbook

Also reject: client `X-Tenant` as key input; `Vary: Cookie` as forever; Report-Only as enforcement; closing findings without re-running `test_other_tenant_does_not_receive_cached_body`; keys in learner notes; live-target CDN work.

## Common mix-ups

- HTTPS means no cache bugs
- CDNs are only a performance layer
- `Vary: Cookie` is enough forever
- TLS 1.3 is the cache key
- Next.js `fetch` cache defaults encode company

## Use it somewhere new

Authenticated RSS or export CSV via CDN. A change that “turns on HTTPS” on only the browser hop is an incomplete check-every-path review. Name the independent falsehood that would still stop company B from receiving company A’s body.

## What this page is not doing

Shipping a path-only cache key plus “will add Vary later” leaves the cached body unowned.
