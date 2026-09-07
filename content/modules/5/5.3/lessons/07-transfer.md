# A gist-leaked clinic API key

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

You get a **clinic lab API key in a gist**. `auth("sk-lab-hardcoded", current="rotated-now")` is false.

A lab API key in a gist is the same leak. Also sketch envelope wrapping (data key vs wrapping key) on compromise.

EHR-lite with a backend integration key.

1. who might try (gist reader; old container — **not** a live clinic);
2. what you trust (which current secret is trusted; the vault brand is not);
3. what must not happen (`auth` true for the leaked string after rotate — not a privacy-law name);
4. a check on a **local** practice only (leaked string false; missing current denies);
5. leftover (images; logs; worker default; hardware box as an advanced extra);
6. whether a human rotation acknowledgement must meet the web accessibility baseline — only if a human acknowledgement is in the claim.

## Picture: leak, rotate, prove dead

```mermaid
flowchart LR
  Gist[Gist copy] --> Old[Old string]
  Rotate[Set current] --> Old
  Old --> Test{"auth false?"}
```

If rotate only updates the wiki, the gist string still authenticates. A settings library, a vault brand, and `.gitignore` do not pop `DEFAULT`. Envelope wrapping is a later sketch: compromising the wrapping key still requires the old data key to be dead — same fork, different wrapping.

The leaked string still has to be false after rotate, and a missing current still has to deny. Moving the key to Vault while leaving `or presented == DEFAULT` in `auth` leaves the gist live. The local check is `test_hardcoded_default_does_not_auth` plus `test_missing_current_denies` — on a practice, not a live gist.

## What is not good enough

| Reject | Why |
|---|---|
| “We use Vault” without a test | Sticker |
| Live gist search | Course rules |
| gitignore as revocation | Artifact still live |
| HTTP 200 as rotation evidence | Wrong observation |
| Password rotation as this rule | Different authenticator |

## Practice

Kill the gist that still holds `DEFAULT`. Keep the answer keys closed. `labs/5.3/5.3-lab` is the only running system you may break. Do not fetch a live gist or paste a key into a ticket.

## Can people still use it

If a human rotation acknowledgement is in the claim, that step must be something keyboard and assistive tech can use, not only a mouse click. A usable acknowledgement is not the rotation check.

## What this page is not doing

Do not try live-target key hunts. Do not use real API keys. This page does not finish a check-in.
