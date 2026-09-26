Fixed 3.2 fixture. Local only.

`evaluate_gate` now opens the stored threat-model document on every call
and checks five properties directly, regardless of `scanner_green`: the
three always-name threats are present with an owner and a trigger; every
required flow (`browser-share-request`, `member-note-read`,
`worker-share-redelivery`) is traced in `declared_flows`; every threat
carries an integer priority; the top-priority threat's `mitigation` is not
a placeholder; and every threat whose own `trigger` name appears in the
model's `trigger_events` list is recorded in that threat's own
`revisited_after` list. Scanner findings are still accepted and returned
as `scanner_extra_findings` — additive, never a substitute for any of the
five checks above.
