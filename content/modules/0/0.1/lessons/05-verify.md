# 0.1 — Security engineering orientation (5 Verify)

**Kind:** verification-lab  
**Loop step:** 5 Verify  
**Standards:** NIST CSF 2.0 (final) GV/ID; OWASP WSTG v4.2 (final) as *lab method*, not a licence to scan the internet; NICE Framework as role language only.

## Property (start here)

A URL is in scope only if it is a named local lab host (127.0.0.1, localhost, lab.securecollab.test). example.com, a employer production API, and a classmate’s deployed preview are out of scope even if they are “easy to hit.”

## Attacker capabilities and trust assumptions

- **Attacker:** A motivated learner who can type any URL into a proxy; a future self who is tired and copies a blog “try this host” snippet.
- **Trust:** You trust this repository’s lab trees and official OWASP training apps when the README names them. You do not trust “the internet,” robots.txt, or a recruiter’s staging site without written scope.
An invariant that cannot fail a test is still a slogan. Happy path is not evidence.

| Case | Must show |
|---|---|
| Normal | Honest allowed action still works where the product says so |
| Negative / abuse | HTTP to a non-allowlisted host treated as authorized |
| Failure | Fail closed: Allow-list local names; fail closed; written scope template |

Lab tests: `test_scope.py` under `labs/0.1/0.1-orientation`.

- `--impl vulnerable` (or vulnerable fixtures): **fail** on `HTTP to a non-allowlisted host treated as authorized`
- `--impl fixed`: **pass**

localhost allowed; example.com denied; missing host denied.

## Practice

Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.

## Transfer

Your company staging URL: what written artifact would make it in-scope? (Not a Slack thumbs-up.)

A test that only asserts HTTP 200 is not this module’s evidence (see 9.3).
