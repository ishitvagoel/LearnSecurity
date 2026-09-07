# Notice stored-field review; CSP reports are extra

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

A markdown path can bring raw HTML back after `render` was repaired once. Do not log title bodies if they are patient data (3.1). Leave nicknames out of the ticket.

## Picture: stored field is a signal

```mermaid
flowchart TD
  Store[Stored title] --> Review{"contains raw angle bracket?"}
  Review -->|yes| Metric["stored_field_review += 1"]
  Metric --> Alert["reason=stored_field_review no body"]
  Alert --> Patch[Patch renderer; rotate sessions if needed]
```

A checklist name does not encode HTML.

## Signals that do not become a second leak

| Outcome | This topic |
|---|---|
| Notice | `stored_field_review`; `csp_report` is extra, not enforcement |
| What the line holds | request id, field name; never the title body if it is patient data |
| Recover | Patch encoding; draw again; rotate cookies if they were readable by script |
| Leftover | Report-only content-security policy; trusted admin HTML |

Raw `<` in the title still has to fail `test_angle_brackets_are_encoded`. Turning a content-security policy on does not encode `<`. Markdown and nickname fields still emit raw `<` if you only encoded the title.

## What the framework does vs what you still have to check

A content-security report-only dashboard will page on blocked scripts and stay silent when the stored title still contains raw `<`. Notice must observe **raw angle brackets at the encode sink**, not report-only counts. If the alert includes the title text, you have opened a logging leak (3.1).

A stored-field review fires without the title body, and a content-security report is extra, not this enforcement.

## Practice

```text
log_denied reason=stored_field_review field=title request_id=req_62h
```

Reject any line that includes the title text, a note body, or an attack cookbook.

## Use it somewhere new

Notice nickname fields with raw `<`; do not paste nicknames into the ticket. Do not load a live board.

## What this page is not doing

Content-security policy in report-only mode is not this rule’s enforcement. Do not use live attack hunts. Opening this page does not finish a check-in.
