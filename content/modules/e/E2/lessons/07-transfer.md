# Same idea when a clinic treats Report-Only as a HIPAA header

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

You get a **clinic** that ships Report-Only and calls it a “HIPAA header.” Also name Trusted Types and COOP/COEP.

Report-Only must not make `isolation_enforced` true.

An EHR-lite “we ship Content-Security-Policy-Report-Only so scripts are blocked,” plus “the reporting dashboard is green.”

## Picture: green report vs blocked script

```mermaid
flowchart LR
  Dash[dashboard green] --> Belief[blocked]
  Ro[Report-Only] --> Reality[script ran]
```

Here, “charts” is still “notes” for this rule. If the dashboard is green while `isolation_enforced` treats Report-Only as on, the rule is gone. Helmet, a HIPAA sticker, and the current content-security spec do not put the enforcing name on the response. Trusted Types and COOP/COEP are sibling isolation leftovers — name them, do not load a live clinic here. The current content-security spec is still a **draft**; encoding (6.2) remains the first rule. Reporting from that policy is extra, later, and advanced: reporting, not enforcement.

| Notes app | Clinic sketch |
|---|---|
| Next.js response headers | EHR-lite response headers |
| Report-Only counted as isolation | Report-Only called a “HIPAA header” |
| Enforcing header name is what you trust | Same; a dashboard is not |
| Encoding leftover (6.2) | Encoding still first; Trusted Types still draft |

## Write this for a clinic Report-Only as a HIPAA header

1. who might try (a script that would only be logged — not a live clinic script hunt);
2. what you trust (the enforcing header name is what you trust; Report-Only, Helmet, and a dashboard are not);
3. what must not happen (`isolation_enforced` true on Report-Only, not “HIPAA”);
4. a check idea on a **local** practice only (no live page);
5. leftover risk (encoding skipped, CDN strip, XS-Leaks, Trusted Types **draft**, content-security reporting as extra, later, and advanced);
6. the web accessibility baseline if a blocked-script message is shown (readable text, not color-only meaning).

Report-Only still has to be denied. Enforcing CSP may still count. Adding Report-Only without the enforcing name leaves `isolation_enforced` true. The local check is `test_report_only_is_not_enforcement` — on practice files, not a live page.

## What is not good enough

| Reject | Why |
|---|---|
| “we have CSP” | Name may be Report-Only |
| Live script hunt | Course rules |
| “The current spec so encoding is done” | Draft layer, not encoding |
| “Helmet defaults” | Library, not the name gate |
| “Check-in 7 complete” | Forbidden stamp |

## Practice

Write one page. Leave the keys closed. `labs/E2/e2-lab` is the only running system you may break. Do not load a live page.

## What this page is not doing

Do not run live-page walkthroughs. Do not do public-host scanning. This page does not finish check-in 7 or milestone M2.
