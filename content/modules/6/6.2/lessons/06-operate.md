# 6.2-LO-06 — Detect stored_field_review; CSP reports are extra

**Kind:** operations-exercise
**Loop step:** 6 Operate
**Standards:** NIST CSF 2.0 (final) DE/RS/RC as outcome labels; OWASP ASVS 5.0.0 (final) `v5.0.0-1.2.1`. `v5.0.0-3.4.7` Level 3 is **advanced**. CSP3 **draft**. CSF names outcomes; it does not encode HTML.

## Prevention is not absolute

A markdown path can reintroduce raw HTML after `render` was “fixed once.” Pair detect and recover. Do not log title bodies if they are PHI (3.1). Do not paste nicknames into the ticket.

## Mental model: stored field is a signal

```mermaid
flowchart TD
  Store[Stored title] --> Review{"contains raw angle bracket?"}
  Review -->|yes| Metric["stored_field_review += 1"]
  Metric --> Alert["reason=stored_field_review no body"]
  Alert --> Patch[Patch renderer; rotate sessions if needed]
```

| Outcome | This module |
|---|---|
| Detect | `stored_field_review`; `csp_report` is extra, not enforcement |
| Signal | request id, field name; never the title body if PHI |
| Recover | Patch encoding; re-render; rotate cookies if they were script-readable |
| Residual | Report-Only CSP; trusted admin HTML |

CSF 2.0 Detect / Respond / Recover name outcomes. They do not prove `v5.0.0-1.2.1`. A WAF product name is not the property. Re-run `test_angle_brackets_are_encoded` after any renderer change; a green “CSP enabled” tile is not that pytest. Markdown and nickname fields are other paths of the same cell — inventory them before claiming Recover.

## Framework defaults versus the operate guarantee

A CSP report-only dashboard will page on blocked scripts and stay silent when the stored title still contains raw `<`. Detection must observe **raw angle brackets at the encode sink**, not Report-Only counts. If the alert includes the title text, you have opened a 3.1 cell.

## Practice

Write one log line you would accept. Tie it to `labs/6.2/6.2-lab`.

```text
log_denied reason=stored_field_review field=title request_id=req_62h
```

Reject any line that includes the title text, a note body, or a payload cookbook.

## Transfer

Clinic: detect nickname fields with raw `<`; do not paste nicknames into the ticket. Do not load a live board.

## Non-goals

A WAF product name is not the property. CSP Report-Only is not this cell’s enforcement. Live XSS hunts are out of scope. Gates 0–10 stay not-attempted.
