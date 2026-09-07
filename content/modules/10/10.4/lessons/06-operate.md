# Turn debug off without leaking logs

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

A flag can still flip after `boot_ok` was “fixed once.” Do not log stack traces that contain secrets, session tokens, or note bodies. Do not paste the traceback into the ticket.

## Picture: an illegal boot is a signal

An illegal boot is something you still have to notice and recover from, not an excuse to quote the stack trace in the paging channel. The notice should name env, debug, and deploy. Recover kills the process and rotates secrets that already leaked.

```mermaid
flowchart TD
  Boot[process start] --> Pair{"prod and debug?"}
  Pair -->|yes| Metric["prod_debug_forbidden plus 1"]
  Metric --> Kill[kill and rotate trace secrets]
```

A canary product is not the rule, and a boot-refused tile is not proof.

Re-run `test_prod_debug_must_not_boot` after any compose change. A green `NODE_ENV` tile is not that check. Emergency debug is E6 — inventory it before you claim recover.

## Signals that do not become a second leak

| Outcome | This topic |
|---|---|
| Notice | `prod_debug_forbidden` |
| What the line holds | env, debug, deploy id; **never** trace bodies |
| Respond | Stop the process that booted with debug; do not paste traces into chat |
| Recover | Kill; rotate secrets that appeared in traces |
| Leftover | Other flags; E6 emergency debug; sidecar debug |

A canary dashboard will show rollout percent and stay silent when CI’s `boot_ok` is always true. Detection must observe **prod plus debug is deny**, not “the container started.” If the alert includes a stack trace or a session token, you have opened the same leak as a log line.

```text
log_denied reason=prod_debug_forbidden env=prod debug=true deploy=sc-12
```

Not: a stack trace, a secret, or “assurance gate complete.”

If your alert includes the matching trace, you have copied the leak into the paging channel.

## What the framework does vs what you still have to check

The same feature flags, sidecar debug, and public admin bind that bypass this practice will also bypass a “scan our canary dashboard” detector.

Cause vs cost stays split here too: the **cause** is fail-open boot (debug ignored); the **cost** is traces and extra attack surface; **how you stop it** is the prod-and-debug check; **how you notice** is `prod_debug_forbidden`; **how you recover** is kill-and-rotate. What the tool cannot do: this alert does not catch a feature flag that turns off authorization (1.2), and it does not catch sidecar debug.

## Can people still use it

A refused boot must say *prod debug refused*, not only “assert False.” Do not encode that reason as color only.

## Practice

```text
log_denied reason=prod_debug_forbidden env=prod debug=true deploy=sc-12
```

Reject any line that includes a stack trace, a secret, or “assurance gate complete.”

## Use it somewhere new

A clinic example: deny Django `DEBUG=True`; do not paste the traceback into the ticket. Do not hit a live `/debug`.

## What this page is not doing

A canary-vendor name is not the rule. This page does not mark you as finished. A manufacturer-defaults program page stays unverified. Answer keys are not on this site.
