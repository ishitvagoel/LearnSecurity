# 0.1 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/0.1.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer on one claim never compensates for a missing one on another.

---

## 1. Discrimination — rule, tool, or false assurance

Four statements a reviewer might find in a PR touching this course's lab tooling:

**A.** "`target_is_authorized` returns `True` only when the parsed hostname is exactly one of `127.0.0.1`, `localhost`, or `lab.securecollab.test`."
**B.** "I have a Burp Suite Community license and the proxy is configured against the target."
**C.** "The host answered on port 443 with a valid TLS certificate and rendered a login page in under 200ms."
**D.** "The recruiter's email said this is an official assessment, so the URL they sent must be in scope."

Sort each statement into **rule**, **tool**, or **false assurance**, and for each one that is not the rule, name specifically what it would need to add or change to become one.

**Claim assessed:** C1 · **Outcome:** Decide whether a URL is in scope by checking the parsed hostname against the written allow-list, not whether it answers

## 2. Discrimination — a vocabulary term vs. a target list

Four statements proposing to add a new host to a lab's allow-list:

**A.** "The OWASP WSTG has a chapter on authentication testing, so any login page qualifies."
**B.** "The NICE Framework lists 'Vulnerability Assessment Analyst' as a real job, and that's my job title."
**C.** "The CSF's Identify function calls for asset inventories, and this host showed up when I inventoried our assets."
**D.** "The client emailed a signed statement naming `staging.client-example.com` as in scope for testing between these two dates, for these two testers."

Identify which statement would actually add a host to a written allow-list, and for the three that would not, name the real thing each one is (a testing method, a job title, a governance activity) and why none of the three is a substitute for the fourth.

**Claim assessed:** C2 · **Outcome:** Identify that a testing-method catalogue, a work-role title, or a governance outcome label cannot add a host to the allow-list

## 3. Diagnosis — a scope checker that crashes instead of denying

```python
from urllib.parse import urlparse

ALLOWED_HOSTS = {"127.0.0.1", "localhost", "lab.securecollab.test"}

def target_is_authorized(url: str) -> bool:
    host = urlparse(url).hostname.lower()
    return host in ALLOWED_HOSTS
```

This checker is not `vulnerable/scope.py`, and it is not `fixed/scope.py` — it is a third implementation. Call it with `url = "http://[::1/path"` (an unmatched IPv6 bracket). Name the root cause of what happens, the precondition under which it matters in practice, and the impact if this checker ships this way — as three distinct answers, not one answer restated three times.

**Claim assessed:** C3 · **Outcome:** State that a URL the checker cannot parse, or a non-string argument, must deny rather than raise or default to allowed

## 4. Diagnosis — a host comparison that is not exact

A teammate proposes this fix, reasoning that it is more permissive of legitimate variation in how a lab host might be written:

```python
def target_is_authorized(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return any(host.endswith(allowed) for allowed in ALLOWED_HOSTS)
```

Call this function with `url = "https://evillab.securecollab.test/"`. Name the root cause of why this returns what it returns, the precondition under which the gap is exploitable in practice (who controls a hostname string, and how), and the impact if this shipped as the course's actual scope check — as three distinct answers.

**Claim assessed:** C5 · **Outcome:** Determine that a hostname containing, prefixed by, or suffixed with an allowed name is not a member of the allow-list

## 5. Design — silent deny vs. deny-and-alert under a constraint

Two engineers propose how `target_is_authorized` should behave on a URL it cannot parse. Engineer A proposes catching every exception inside the function and returning `False`, with nothing else. Engineer B proposes the same `False` return, plus writing a distinct `scope_check_parse_error` signal (host string, exception type, no other content) that a human reviews on a regular cadence. Under the constraint that a scope checker with a latent bug — one that makes it deny far more often than it should, for example — must be **noticed by a person**, not just fail safely forever, choose between the two proposals and defend your choice, including the one thing Engineer A's version can never surface on its own.

**Claim assessed:** C3 · **Outcome:** State that a URL the checker cannot parse, or a non-string argument, must deny rather than raise or default to allowed

## 6. Operate — the denied-host signal, after a response was already fetched

A script's older code path fetched a host before `target_is_authorized` was consulted, and the response body is now sitting in a variable in memory. The check now runs, and the host is denied. Write the two things that must happen next: the log line your system emits for the denial, and the specific handling of the already-fetched body. State which field the log line must never contain, and why "we'll just log the body too, for the ticket" turns a single violation into two.

**Claim assessed:** C4 · **Outcome:** Write the deny signal for an out-of-scope host without capturing anything that host returned

## 7. Transfer — the contractor and the staging URL

Using the scenario in `lessons/07-transfer.md`: a contractor is asked to "quickly test our customer's WordPress," and separately, a company staging URL is proposed as a target. For each of the two hosts, state (a) what specific written artifact — not a feeling, not a job title, not a testing guide — would have to exist before `target_is_authorized` could honestly return `True` for it, (b) which of this module's five claims (C1–C5) is doing the actual work of the refusal in each case, and (c) one plausible-sounding justification a colleague might offer for testing anyway, and which claim it violates.

**Success criteria:** Your answer must name a concrete artifact (a signed scope letter, a written engagement agreement with named hosts and dates — not "permission," unqualified) for both hosts, must identify C1 as the reason "it has a login page and it resolves" fails for the WordPress site, must identify C2 as the reason "the recruiter said it's an official assessment" or "WSTG covers WordPress" fails to license either host, and must not propose fetching, scanning, or otherwise contacting either host to settle the question.

**Claim assessed:** C1–C5 · **Outcome:** Transfer the reachability/vocabulary/fail-closed/exact-match rules to a contractor's customer-WordPress request and a company staging URL

---

## Evidence checklist

- [ ] Scope map naming the three allowed hosts and the stop condition (Lesson 02); WSTG/NICE/CSF explicitly labeled as vocabulary, not authorization
- [ ] Local reproduction of all three of this module's forbidden outcomes: a public host, a lookalike host, and a malformed URL, each treated as authorized (Lesson 03)
- [ ] Lab `labs/0.1/0.1-orientation`: `vulnerable/` tests show 4 of 7 failing for the stated security reasons; `fixed/` tests show 7 of 7 passing
- [ ] Seeded review notes (Lesson 08) — do not look at the key
- [ ] Operate signal without response bodies: `out_of_scope` (Lesson 06), and item 6's two-part answer
- [ ] Transfer answer (item 7) naming a concrete written artifact for both the contractor WordPress and the staging URL, and the specific claim each bad justification violates
