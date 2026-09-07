# Log the hash mismatch, not the secrets

**Kind:** operations-exercise
**Loop step:** 6 Operate

## Fixing it once is not enough

A cache can serve old bytes after `install_ok` was “fixed once.” Do not log registry tokens or signing keys (5.3). Do not paste `.npmrc` into the ticket.

## Picture: digest mismatch is a signal

If a digest does not match, page the package name and both digest ids — not the registry token. Then pin the known-good digest.

```mermaid
flowchart TD
  Inst[install] --> Eq{digest match?}
  Eq -->|no| Metric["hash_mismatch_denied plus 1"]
  Metric --> Pin[repin known-good]
```

An SBOM vendor name does not prove the lockfile was checked.

Re-run `test_hash_mismatch_refuses_install` after any installer change. Attaching an SBOM does not compare digests. Cache poisoning and `@v1` Actions are sibling leftovers — list those before you call the pin done.

## Signals that do not become a second leak

| Outcome | This topic |
|---|---|
| Notice | `hash_mismatch_denied` |
| What the line holds | Package name, expected vs got *ids*; **never** tokens |
| Respond | Stop the install that would take wrong bytes; do not paste registry tokens into chat |
| Recover | Pin known-good; rotate CI secrets |
| Leftover | Malicious pin; cache poisoning; unpinned actions |

An npm audit dashboard will show advisory counts and stay silent when CI’s `install_ok` is always true. Detection must observe **aaa vs bbb is deny**, not CVE volume. If the alert includes a registry token, you have opened the same leak as a log line (5.3).

```text
log_denied reason=hash_mismatch_denied pkg=demo expected=aaa got=bbb
```

Not: a token, a private key, or “ship gate complete.”

Putting the registry token in the alert puts a secret in the pager too.

## What the framework does vs what you still have to check

The same always-true installer, poisoned cache, and unpinned `@v1` Actions that bypass this practice will also bypass a “scan our advisory count” detector. An SBOM-vendor name is not the rule.

The **cause** is install without comparing digests; the **cost** is wrong bytes in the trusted computing base; **how you stop it** is `expected_hash == got_hash`; **how you notice** is `hash_mismatch_denied`; **how you recover** is pin known-good and rotate CI secrets (5.3). What the tool cannot do: this alert does not prove the pin is benign, does not authenticate provenance, and does not stop cache poisoning or `@v1` Actions. Equality is the local stand-in, not index policy.

## Can people still use it

A denied install must say *digest mismatch* in words, not only “assert False.” If operators see a mismatch badge, do not encode it as color only.

## Practice

```text
log_denied reason=hash_mismatch_denied pkg=demo expected=aaa got=bbb
```

Reject any line that includes a token, a private key, or “ship gate complete.”

## Use it somewhere new

Deny npm in the prod pod; do not paste `.npmrc` into the ticket. Do not fetch a live package.

## What this page is not doing

An SBOM-vendor name is not the rule. Do not use live registry traces. This page does not finish the ship check-in. A provenance badge is not this alert. Answer keys are not on this site.
