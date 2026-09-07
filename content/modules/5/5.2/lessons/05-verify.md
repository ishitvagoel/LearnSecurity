# A Base64 round-trip must fail the check

**Kind:** verification-lab
**Loop step:** 5 Verify

## Check it

“We use AES” is not evidence. “Column is bytea” is a tool observation. The check is: Base64 decode of `protect("secret")` is not `"secret"`, and `looks_encrypted` is true on the repaired stand-in. That observation must be **false** on the broken files (decode equals secret) and **true** on the repaired files.

## Picture: Base64 round-trip must fail the check

A passing collection count is not this rule. The failing observation on the broken files is **Base64 round-trip**.

```mermaid
flowchart LR
  V["broken files --impl vulnerable"] --> F[Must fail: Base64 round-trip]
  X["repaired files --impl fixed"] --> P[Must pass: not reversible]
```

If both pass, you are not looking at Base64 decode of `protect("secret")`.

## What the check has to show

| Mode | Must show for this topic |
|---|---|
| Normal | Output is not plaintext; teaching flag present on repaired files |
| Wrong input / abuse | Base64 of `secret` is rejected; broken files must fail |
| Failure | If the library is missing, refuse the write — do not store plaintext |
| Not claimed | Real AES-GCM; key storage; nonce uniqueness |

The test `test_protect_is_not_mere_encoding` is there so reversible encoding still fails.

A test that only greps `AES` in a comment without decoding `protect("secret")` is not this topic's evidence. This practice never opens a live column.

```text
python3 -m pytest labs/5.2/5.2-lab/tests --impl vulnerable
python3 -m pytest labs/5.2/5.2-lab/tests --impl fixed
```

`test_protect_does_not_return_plaintext` may pass on both if the broken files already Base64. That does not excuse the round-trip test. If the broken files do not fail Base64 decode, the lab is miswired — fix the wiring, not the assertion. A setup error is not proof the rule holds.

## What the tests do not prove

- Key lifecycle (later)
- TLS (later)
- A post-quantum plan (advanced; not this check)
- Nonce uniqueness (advanced; not this check)
- A production AES-GCM implementation

## Practice

```text
python3 -m pytest labs/5.2/5.2-lab/tests --impl vulnerable
python3 -m pytest labs/5.2/5.2-lab/tests --impl fixed
```

Reject a “test” that only greps `AES` in a comment without decoding `protect("secret")`.

## Use it somewhere new

Clinic SSN. A test that only asserts the column is non-null is not secrecy evidence. A test that decodes a live clinic column is out of scope.

## What this page is not doing

Do not add a live decoder. Do not log plaintext `secret`. Keys stay out of this file.
