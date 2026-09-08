# Lab E2 — Report-Only is not enforcement

**Module:** `E2`
**Authorized scope:** this directory only. Local course fixture. No live origins or public XSS targets.
**Invariant:** a Report-Only header does not make `isolation_enforced` true. An enforcing `Content-Security-Policy` header may.
**Root cause class:** Report-Only mistaken for on
**Non-goals:** CSP3 as encoding; claiming Gate 7.

Header-name presence is a **teaching stand-in** for browser policy mode. It does not parse CSP.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/E2/e2-lab`, then run `git restore --source=HEAD -- labs/E2/e2-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

Any CSP-looking header counts as enforced. Forbidden outcome: Report-Only treated as isolation.

## Structural fix

Require the enforcing `Content-Security-Policy` header name.

## Verify

```
python3 -m pytest labs/E2/e2-lab/tests --impl vulnerable
python3 -m pytest labs/E2/e2-lab/tests --impl fixed
```

The first command must fail Report-Only. The second must pass. Honest enforcing CSP may pass on both.

## Operate

Signal: `csp_report_only_not_enforced`. Do not log full document HTML. Do not claim Gate 7.

## Transfer

Clinic: Report-Only as “HIPAA header.” Trusted Types / COOP. Prompt only.
