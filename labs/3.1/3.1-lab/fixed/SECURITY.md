Fixed 3.1 fixture. Local only.

Both sinks now route every field through `_redact(context, sink)`, which
looks up each field's level in `CLASSIFICATION` and checks it against that
sink's own `SINK_POLICY` before allowing the value through. A field the
table has never named defaults to `confidential` -- the most restrictive
level, not the least -- so a future schema addition nobody has classified
yet is denied until someone positively assigns it a level. Denied fields
are replaced with a `[redacted-<level>]` marker, not silently dropped, so
`event`, `note_id`, and `company_id` (all Internal) still reach both sinks
and an operator can see that a field existed and was withheld.
