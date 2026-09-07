# Same idea on fifty unmapped clinic findings

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

You get a **clinic dashboard**. Fifty HIGH findings sit unmapped.

On the notes app, `ship_ok([HIGH], {})` must be false. For a clinic, finding × map, allow or deny. A noisy dashboard is still noise, not a map.

**Product sketch:** an EHR-lite “code scanning is on and the dashboard is noisy so we ship Fridays,” plus a maturity score on a slide.

## Picture: same join, clinical object

Renaming “note finding” to “clinic finding” is not transfer. Finding, map, and leftover change. Enabling code scanning without a mapping check does not own the HIGH.

| Notes app this week | Clinic sketch |
|---|---|
| HIGH finding is unowned until mapped | Same — fifty unmapped HIGHs |
| Coverage-map requirement id | Same join, clinic requirement names |
| `ship_ok([HIGH], {})` | `ship_ok` on a local practice files |
| Alert-fatigued reviewer | Same reader — **not** a live clinic |
| Empty map ships the finding | Empty map ships the finding |

```mermaid
flowchart LR
  Fifty[50 HIGHs] --> Belief[probably false positives]
  Empty[empty map] --> Reality[unowned ships]
```

If the dashboard is noisy while `ship_ok` is always true, the rule is gone. A vendor default setup, a maturity score, and Dependabot do not join F1 to AUTHZ-1. SCA “we do not call that function” still records an owner — name it, do not scan a live org here. Who-is-allowed blind spots remain review and isolation tests.

An unmapped HIGH still has to be denied. A mapped HIGH may still ship. Enabling code scanning without a mapping check leaves `ship_ok([HIGH], {})` true. The local check is `test_unmapped_high_blocks_ship` — on a practice, not a live GitHub tenant.

Also name SCA: a CVE versus a function you actually call.

## Prompt — clinic, fifty unmapped HIGHs

1. who can act (alert fatigue — not a live clinic);
2. what you trust (the mapping check is the promise; the dashboard and a maturity score are not);
3. what must not happen (`ship_ok([HIGH], {})` true, not a legal label);
4. a test idea on a **local** practice files only (no live GitHub);
5. leftover (who-is-allowed blind spots, dependency confusion as an advanced leftover, mass suppressions);
6. whether a human triage path exists (must say *why* F1 is blocked, in words).

Use fake labels. Do not use real patient findings.

## What is not good enough

| Reject | Why |
|---|---|
| “The scanner is on” | Signal, not ownership |
| Live GitHub org / public SCA | Course rules |
| A maturity score as `ship_ok` | Measurement, not the check |
| Empty dashboard as isolation | Wrong observation |
| A draft supply-chain paper as a certificate | Draft; not the verification gate |

## Practice

One page. No answer keys. `labs/9.4/9.4-lab` is the only running system you may break. Do not scan a public host.

## What this page is not doing

Live-target scanning. Real patient findings. Claiming you finished the verification gate from this page.
