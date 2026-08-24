# 0.1 — Security engineering orientation (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** NIST CSF 2.0 (final) GV/ID; OWASP WSTG v4.2 (final) as *lab method*, not a licence to scan the internet; NICE Framework as role language only.

## Property (start here)

A URL is in scope only if it is a named local lab host (127.0.0.1, localhost, lab.securecollab.test). example.com, a employer production API, and a classmate’s deployed preview are out of scope even if they are “easy to hit.”

## Attacker capabilities and trust assumptions

- **Attacker:** A motivated learner who can type any URL into a proxy; a future self who is tired and copies a blog “try this host” snippet.
- **Trust:** You trust this repository’s lab trees and official OWASP training apps when the README names them. You do not trust “the internet,” robots.txt, or a recruiter’s staging site without written scope.
Review `labs/0.1/0.1-orientation/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/0.1.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): SECURITY.md says “any URL the proxy can open.”
- Seeded smell (label it yourself): No stop condition when a redirect leaves 127.0.0.1.
- Seeded smell (label it yourself): Live-target language in a learner note.
- Seeded smell (label it yourself): Quiz score treated as permission to scan.

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- If it has a login page it is a lab
- WSTG chapter titles are the syllabus
- Defensive learning requires attacking strangers

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Your company staging URL: what written artifact would make it in-scope? (Not a Slack thumbs-up.)

## HITL / WCAG 2.2

Scope templates and stop-buttons in course UI must be keyboard-operable (WCAG 2.2). A mouse-only “I agree” is not informed consent.
