# E2 — Advanced browser and edge security (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** W3C CSP3 (CR — label draft/CR); Fetch Metadata; this lab’s cell is enforcement vs report-only.

## Property (start here)

Content-Security-Policy-Report-Only is not enforcement. Isolation is not “we set a header.”

## Attacker capabilities and trust assumptions

- **Attacker:** XSS that would be blocked only if CSP were enforcing.
- **Trust:** Local isolation_enforced(headers).
Review `labs/E2/e2-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/E2.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): Report-Only counted as enforced
- Seeded smell (label it yourself): CSP with unsafe-inline claimed strict
- Seeded smell (label it yourself): Edge cache serves old headers
- Seeded smell (label it yourself): No isolation_enforced test

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- More headers is more security
- Report-Only is a safer enforcing mode
- CDN WAF is CSP

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Trusted Types, COOP/COEP.
