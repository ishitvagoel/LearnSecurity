# Same idea: clinic Android hipaaMode=true

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

The notes-app scaffolding goes away. You get a clinic Android client that sends `hipaaMode=true`. Also name feature flags in the app file and `premium=true`.

Do not answer with a famous-bugs list, a CWE, or a scanner as the definition of security. The notes-app sentence was: `allow_export({"integrity": "ok"}, "fail")` must be false. Rewrite it for a clinic without changing the fork.

**Product sketch:** an EHR-lite Compose switch “HIPAA mode” that the API trusts as a boolean.

## Picture: a client switch is still a client claim

```mermaid
flowchart LR
  Switch["Compose hipaaMode"] --> Belief[UI believes compliant]
  Json["JSON hipaaMode true"] --> Reality[server grant if unchecked]
```

Renaming `integrity` to `hipaaMode` is not transfer. Person, object, path, and leftover change. If the Compose switch is “HIPAA mode” while the server binds `hipaaMode=true` as a grant, the rule is gone. Play Integrity in the app, shrinking the app, and the store listing do not ignore the client boolean. Feature flags and `premium=true` are the same claim family — name them, do not run those app files here. The phone sandbox still does not put this process in what you trust (the first page).

| Notes app this week | Clinic sketch |
|---|---|
| Patched notes-app file sending `integrity=ok` | Patched clinic app file sending `hipaaMode=true` — not a live hospital device |
| `allow_export({"integrity": "ok"}, "fail")` | Clinic export on client `hipaaMode` with failing attest |
| Server attest is what you trust | Same; Compose switch and store listing are not |
| Feature flags / `premium=true` leftover | Same claim family — name them, do not run them here |

## Prompt — clinic Android hipaaMode=true

Rewrite the notes-app sentence for this product. Your answer must include:

1. who can act (patched clinic app file — not a live hospital device);
2. what you trust (server attest plus 1.2 is what you trust; client boolean and store listing are not);
3. what must not happen (`allow_export` true on a client claim with failing attest, not “HIPAA”);
4. a check idea on **local** practice files only (no live Play);
5. leftover risk (attestation farms, rooted honest clinicians, 8.4 debug builds);
6. the accessibility baseline if a human deny path is in the claim (readable “export unavailable,” not a silent crash).

The clinic rewrite still has to keep the notes-app fork: client claim plus failing attest false, server-pass may allow. Enabling Play Integrity without a failing-attest deny check leaves `allow_export({integrity: ok}, fail)` true. The local pytest analogue is `test_client_integrity_claim_is_not_authorization` — on the practice files, not a live hospital device.

## What is not good enough

| Reject | Why |
|---|---|
| “Play Integrity is on” | Signal, not 1.2 |
| Live clinic device | Course rules |
| Old numbered mobile levels as current | Not current levels |
| Compose disabled as the grant | Client is not what you trust |
| Store listing as device trust | Package id, not next JSON |

## Practice

One page. No keys. `labs/8.1/8.1-lab` is the only running system you may break. Do not instrument a public device.

## What this page is not doing

Live-target mobile attacks. Real BAA flags. This page does not finish a check-in.
