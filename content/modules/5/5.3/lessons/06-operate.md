# Notice default_secret_used; rotate without logging the secret

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

An old image or a worker can still present `sk-lab-hardcoded` after `auth` was repaired once. Do not log the secret. Leave the key out of the ticket.

## Picture: alert on the default string id, not the value

```mermaid
flowchart TD
  Presented[Presented key] --> Known{"matches retired default id?"}
  Known -->|yes| Metric["default_secret_used += 1"]
  Metric --> Alert["reason=default_secret_used secret_id=lab_default no value"]
  Alert --> Rotate[Rotate and rebuild]
```

| Outcome | This topic |
|---|---|
| Notice | `default_secret_used`; secret scanning |
| What the line holds | secret id, request id; never the value |
| Recover | Rotate; rebuild images; purge logs |
| Leftover | Copies already cloned |

A vendor name does not kill `DEFAULT`. Touch `auth` and `test_hardcoded_default_does_not_auth` has to stay red on `DEFAULT`. Enabling Vault does not stop the hardcoded default. Images and workers can still hold `DEFAULT`; the gist is not dead until those copies are named.

Recovery is incomplete if the next image still ships `DEFAULT = "sk-lab-hardcoded"` as an or-clause. Rebuild and prove `test_missing_current_denies` the same day you rotate, or the next allow-when-missing still authenticates the gist copy. A Vault dashboard is not that rebuild.

## What the framework does vs what you still have to check

A vault dashboard will show “rotation enabled” and stay silent when `DEFAULT` is still an or-clause. Notice must observe **presented equals the retired secret id**, not a product tile. If the alert includes `sk-lab-hardcoded` or a real key, you have opened a leak.

## Practice

```text
log_denied reason=default_secret_used secret_id=lab_default request_id=req_53sk
```

Reject any line that includes `sk-lab-hardcoded`, a real key, or “Vault handled.”

## Use it somewhere new

Notice gist-key use; do not paste the key into the ticket. Do not fetch a live gist.

## What this page is not doing

Do not use live gist searches. This site does not mark you as finished.
