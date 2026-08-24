# 0.1 — Security engineering orientation (6 Operate)

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST CSF 2.0 (final) GV/ID; OWASP WSTG v4.2 (final) as *lab method*, not a licence to scan the internet; NICE Framework as role language only.

## Property (start here)

A URL is in scope only if it is a named local lab host (127.0.0.1, localhost, lab.securecollab.test). example.com, a employer production API, and a classmate’s deployed preview are out of scope even if they are “easy to hit.”

## Attacker capabilities and trust assumptions

- **Attacker:** A motivated learner who can type any URL into a proxy; a future self who is tired and copies a blog “try this host” snippet.
- **Trust:** You trust this repository’s lab trees and official OWASP training apps when the README names them. You do not trust “the internet,” robots.txt, or a recruiter’s staging site without written scope.
Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).

| Outcome | This module |
|---|---|
| Detect | Log denied hosts without fetching them; supervisor review of proxy history in class only. |
| Signal (no bodies) | Denied-host log line {url, reason=out_of_scope}; never store response bodies from out-of-scope hosts. |
| Revoke / recover | Stop, document, do not exfiltrate; notify instructor. Do not “just this once” continue. |
| Residual | Official Juice Shop on your machine is OK; a random cloud Juice Shop you do not own is not. |

CSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.

## Practice

Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `labs/0.1/0.1-orientation`.

## Transfer

Your company staging URL: what written artifact would make it in-scope? (Not a Slack thumbs-up.)

## Usability

Scope templates and stop-buttons in course UI must be keyboard-operable (WCAG 2.2). A mouse-only “I agree” is not informed consent.

## Non-goals

SIEM product names are not the property. Keys stay out of lessons.
