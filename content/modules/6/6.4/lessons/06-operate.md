# Notice path_escape_denied

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

An export path can join a user filename again and walk out of the folder. Skip patient filenames and host paths in the ticket.

## Picture: an escape attempt is a signal

```mermaid
flowchart TD
  Name[filename] --> Esc{"canonical leaves folder?"}
  Esc -->|yes| Metric["path_escape_denied += 1"]
  Metric --> Alert["reason=path_escape_denied no name"]
  Alert --> Audit[Audit store; restore]
```

On a broken resolve, skip the patient filename on the log line.

| Outcome | This topic |
|---|---|
| Notice | `path_escape_denied` |
| What the line holds | request id, stored key; never the raw filename if it is a patient id |
| Recover | Deny; audit; restore if a file landed outside |
| Leftover | Malware scan extra; zip/XML still open |

A log product and an antivirus name do not prove this path rule. `..` still has to fail `test_dotdot_does_not_escape_root`. UUID stored filenames do not bind the resolved prefix. Export and unzip paths still walk `..` if you only bound the upload helper.

Recovery is incomplete if the next route still joins `UploadFile.filename` without canonicalize. Grep export and unzip helpers the same day you restore a stray file, or the next scan re-issues the escape.

## What the framework does vs what you still have to check

A WAF will page on `../` in the URL and stay silent when `UploadFile.filename` still joins without canonicalize. Notice must observe **canonical path left the folder**, not a denylist hit. If the alert includes a patient filename or a host path cookbook, you have opened a leak.

## Practice

```text
log_denied reason=path_escape_denied request_id=req_64p
```

A patient filename, a note body, or a host path cookbook has no place on the path line.

## Use it somewhere new

Notice scan names that leave the imaging root; do not paste filenames into the ticket. Do not open a live imaging folder.

## What this page is not doing

An antivirus sticker does not keep the path under the folder. Do not use live host reads. This page does not finish a check-in. Answer keys are not on this site.
