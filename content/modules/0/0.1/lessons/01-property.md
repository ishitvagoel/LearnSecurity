# 0.1 — Security engineering orientation (1 Property)

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** NIST CSF 2.0 (final) GV/ID; OWASP WSTG v4.2 (final) as *lab method*, not a licence to scan the internet; NICE Framework as role language only.

## Property (start here)

A URL is in scope only if it is a named local lab host (127.0.0.1, localhost, lab.securecollab.test). example.com, a employer production API, and a classmate’s deployed preview are out of scope even if they are “easy to hit.”

## Attacker capabilities and trust assumptions

- **Attacker:** A motivated learner who can type any URL into a proxy; a future self who is tired and copies a blog “try this host” snippet.
- **Trust:** You trust this repository’s lab trees and official OWASP training apps when the README names them. You do not trust “the internet,” robots.txt, or a recruiter’s staging site without written scope.
**Mechanism (not the property):** Burp, ZAP, or curl existing is not authorization. CSF GV is governance language, not a pentest permit.

Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.

## Root cause vs impact vs prevention vs detection vs recovery

| Slice | For 0.1 |
|---|---|
| Root cause | Authorization collapsed into reachability: if TCP connects, it was treated as in-scope. |
| Preconditions | Learner has a proxy; a public URL is one paste away. |
| Impact (1.1 cell) | Safety + accountability (1.1): unauthorized testing is both a legal and an engineering failure. — Unlawful access; course expulsion; harm to uninvolved operators; poisoned evidence. |
| Prevention | Allow-list local names; fail closed; written scope template. |
| Detection | Log denied hosts without fetching them; supervisor review of proxy history in class only. |
| Recovery | Stop, document, do not exfiltrate; notify instructor. Do not “just this once” continue. |

## Framework defaults vs application guarantees

Burp, ZAP, or curl existing is not authorization. CSF GV is governance language, not a pentest permit.

## Mechanism limits and bypasses

An allow-list of three names still fails if you SSH to a stolen hostname that resolves locally via /etc/hosts tricks — check what you actually connected to.

DNS rebinding, hosts-file aliases, or “it’s just a redirect to localhost.” Still out of scope unless the README says so.

## Residual risk

Official Juice Shop on your machine is OK; a random cloud Juice Shop you do not own is not.

## Practice

Write a three-line scope: in, out, stop condition. Run the lab pair.

Run `labs/0.1/0.1-orientation` (`pytest` with `--impl vulnerable` then `--impl fixed` if the lab uses `--impl`). Map the failing test to this property.

## Transfer

Your company staging URL: what written artifact would make it in-scope? (Not a Slack thumbs-up.)

A contractor asked to “quickly test our customer’s WordPress.”

## Non-goals

Live targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.

## Usability and accessibility

Scope templates and stop-buttons in course UI must be keyboard-operable (WCAG 2.2). A mouse-only “I agree” is not informed consent.
