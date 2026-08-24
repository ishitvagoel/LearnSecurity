# 0.1 — Security engineering orientation (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** NIST CSF 2.0 (final) GV/ID; OWASP WSTG v4.2 (final) as *lab method*, not a licence to scan the internet; NICE Framework as role language only.

## Property (start here)

A URL is in scope only if it is a named local lab host (127.0.0.1, localhost, lab.securecollab.test). example.com, a employer production API, and a classmate’s deployed preview are out of scope even if they are “easy to hit.”

## Attacker capabilities and trust assumptions

- **Attacker:** A motivated learner who can type any URL into a proxy; a future self who is tired and copies a blog “try this host” snippet.
- **Trust:** You trust this repository’s lab trees and official OWASP training apps when the README names them. You do not trust “the internet,” robots.txt, or a recruiter’s staging site without written scope.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Learner, course maintainer, unnamed internet operator |
| Objects | Local lab process, public website, production API |
| Actions | Send HTTP, replay a capture, run pytest |
| Channels | Browser, proxy, pytest against labs/ |
| TCB | The allow-list in labs/0.1/0.1-orientation/fixed/scope.py |
| Untrusted | Any host header, any “open bug bounty” rumour, any AI-suggested target |
| State / time | Scope is per engagement; yesterday’s lab VM IP is not forever-authorized. |
| 1.1 cell | Safety + accountability (1.1): unauthorized testing is both a legal and an engineering failure. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| learner | http://127.0.0.1:8000/notes | GET | allow |
| learner | https://example.com/ | GET | deny |
| learner | https://lab.securecollab.test/ | GET | allow |
| learner | https://customer.example/ | GET | deny |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/0.1/0.1-orientation` file `scope.py`.

## Transfer

Your company staging URL: what written artifact would make it in-scope? (Not a Slack thumbs-up.)

## Residual risk

Official Juice Shop on your machine is OK; a random cloud Juice Shop you do not own is not.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
