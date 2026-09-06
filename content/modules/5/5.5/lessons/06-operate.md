# 5.5-LO-06 — Detect sql_error_spike; restore if mutated

**Kind:** operations-exercise
**Loop step:** 6 Operate
**Standards:** NIST CSF 2.0 (final) DE/RS/RC as outcome labels; OWASP ASVS 5.0.0 (final) `v5.0.0-1.2.4`. `v5.0.0-16.3.2` Level 3 clause is **advanced**. CSF names outcomes; it does not bind parameters.

## Prevention is not absolute

A new report path can concatenate again after `fetch_sql` was “fixed once.” Pair detect and recover. Do not log note bodies or bound parameter values that are bodies (3.1 / 5.1). Do not paste patient names into the ticket.

## Mental model: error shape is a signal

```mermaid
flowchart TD
  Req[Request] --> Err{"SQL syntax error spike?"}
  Err -->|yes| Metric["sql_error_spike += 1"]
  Metric --> Alert["reason=sql_error_spike no body"]
  Alert --> Restore[Rotate creds; restore if mutated]
```

| Outcome | This module |
|---|---|
| Detect | `sql_error_spike`; `grant_drift` (3.3) |
| Signal | request id, tenant id, statement **name**; never the body |
| Recover | Stop the concatenating path; rotate DB creds; restore from backup if rows mutated |
| Residual | Superuser tools; replicas that were not restored |

CSF 2.0 Detect / Respond / Recover name outcomes. They do not prove `v5.0.0-1.2.4`. A SIEM product name is not the property. Re-run `test_query_is_bound_not_concatenated` after any query helper change; a green “WAF SQLi rule” tile is not that pytest. Report paths and ORDER BY builders are other paths of the same cell — inventory them before claiming Recover.

## Framework defaults versus the operate guarantee

A WAF will page on syntax errors and stay silent when the values were concatenated but happened to parse. Detection must observe **concatenated `str` from `fetch_sql`**, not HTTP 500 counts. If the alert includes a full SQL string with values, you have opened a 3.1 cell.

## Practice

Write one log line you would accept. Tie it to `labs/5.5/5.5-lab`.

```text
log_denied reason=sql_error_spike tenant=tA request_id=req_55q stmt=fetch_note
```

Reject any line that includes a note body, a full SQL string with values, or a real email.

## Transfer

Clinic: detect search-box syntax errors; do not paste patient names into the ticket. Do not hit a live EHR.

## Non-goals

SIEM product names are not the property. WAF is not this cell. Live SQL hunts are out of scope. Gates 0–10 stay not-attempted.
