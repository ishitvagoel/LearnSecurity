# 5.3 — Key and secret lifecycle (7 Transfer)

**Kind:** transfer-challenge  
**Loop step:** 7 Transfer  
**Standards:** ASVS 5.0.0 V11/V13 (final); OWASP secrets guidance; NIST PQC standards are for *agility planning*, not a lab quantum attack.

## Property (start here)

A disposable lab API key that is a hardcoded default must not authenticate after rotation. The old value fails. Inventory + rotation is the property, not “we have a secrets manager” as a sticker.

## Attacker capabilities and trust assumptions

- **Attacker:** Anyone who cloned the repo or an old container image with sk-lab-hardcoded.
- **Trust:** Local auth(current). Real KMS later.
Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.

**Prompt:** Envelope encryption DEK vs KEK; compromise runbook.

**Product sketch:** Clinic lab API key in a GitHub gist.

Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.

## What graders reject

| Reject | Why |
|---|---|
| Tool or awareness-list name as the property | 1.1 |
| Framework default as the guarantee | pydantic Settings reading .env does not rotate anything.… |
| Live-target plan | Lab policy |

## Practice

One page. No keys. The lab `labs/5.3/5.3-lab` stays the only running system you may break.
