# Same idea on npm install in a clinic prod pod

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

You get a **clinic that runs npm install in a prod pod**. A fake “always get latest” install sits next to an SBOM.

The notes-app sentence was: `install_ok("aaa", "bbb")` must be false. Rewrite it for a clinic: mismatch is deny; a matching pair may install. An SBOM is still inventory, not verify.

**Product sketch:** an EHR-lite “prod pod runs npm install so we always get latest,” plus “we attach a CycloneDX SBOM and a provenance badge.”

## Picture: latest vs lockfile

Renaming “note” to “chart” is not transfer. Expected digest, got digest, and leftover change. Marking “npm install ran” does not compare hashes.

| Notes app this week | Clinic sketch |
|---|---|
| `install_ok("aaa", "bbb")` must be false | Same check on a local practice files |
| Lockfile digest is the pin | Prod pod still needs a pin |
| Name-only install | “Always get latest” |
| Lookalike publisher | Same actor — **not** a live clinic registry |
| Equality in the function | Equality in the function |

```mermaid
flowchart LR
  Latest[npm install latest] --> Belief[patched]
  Name[name only] --> Reality[wrong bytes]
```

If the pod installs “latest” while `install_ok` is always true, the rule is gone. CycloneDX, provenance badges, and Dependabot do not compare `aaa` to `bbb`. Pinning Actions by SHA is the same equality idea on a different object — name it, do not typosquat a live registry here. A lookalike package wins when you install by name. An SBOM is inventory, not verify.

A digest mismatch still has to be denied. A match may still install. Generating an SBOM without a digest check leaves `install_ok("aaa","bbb")` true. The local check is `test_hash_mismatch_refuses_install` — on a practice, not a live npm.

## Prompt — clinic npm install in a prod pod

Rewrite the notes-app sentence. Include:

1. who can act (lookalike / compromised maintainer — not a live clinic registry attack);
2. what you trust (digest equality is the promise; SBOM / provenance / Dependabot are not);
3. what must not happen (`install_ok("aaa","bbb")` true, not a legal label);
4. a test idea on a **local** practice files only (no live npm);
5. leftover (malicious pin, cache poisoning, unpinned actions, lookalike packages);
6. whether a human-read CI path exists (must say digest mismatch in words).

Use fake labels. Do not use real clinic secrets. Also name GitHub Actions `action@v1`.

## What is not good enough

| Reject | Why |
|---|---|
| “We have an SBOM” | Inventory, not verify |
| Live npm / typosquat tutorial | Course rules |
| “A provenance badge so the hash check is done” | Provenance is not the install check |
| “Dependabot is on” | Signal, not digest equality |
| “Ship gate complete” | Forbidden stamp |

## Practice

One page. No answer keys. `labs/10.2/10.2-lab` is the only running system you may break. Do not fetch a live package.

## What this page is not doing

Live-registry attacks. Real org poison-PRs. Claiming you finished the ship gate from this page.
