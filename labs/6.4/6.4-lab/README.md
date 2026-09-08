# Lab 6.4 — a filename is data, not a filesystem object

**Module:** `6.4`
**Authorized scope:** this directory only. Local course fixture. No host-file trophies.
**Invariant:** `resolve` stays under `/tmp/sc-lab` after canonicalize. `../` names deny.
**Root cause class:** path grammar mixed with data
**Non-goals:** reading host files, zip bombs, XML/pickle gadgets.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/6.4/6.4-lab`, then run `git restore --source=HEAD -- labs/6.4/6.4-lab` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`resolve` joins the name onto the lab root without canonicalize-and-prefix. Forbidden outcome: resolved path escapes the lab root.

## Structural fix

Join, canonicalize, deny unless the result is the root or a child. Tests assert prefix; they do not open host files.

## Verify

```
python3 -m pytest labs/6.4/6.4-lab/tests --impl vulnerable
python3 -m pytest labs/6.4/6.4-lab/tests --impl fixed
```

The first command must fail on the escape test. The second must pass. Honest relative names may pass on both.

## Operate

Signal: `path_escape_denied`. Do not log PHI filenames.

## Transfer

Clinic scan upload. Prompt only.
