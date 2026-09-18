# Connecting is not permission

**Kind:** concept-model
**Loop step:** 1 Property
**Standards:** NIST CSF 2.0 (final) GV/ID as outcome vocabulary. OWASP WSTG 4.2 (final) as a lab method catalogue, not a licence. NIST SP 800-181r1 NICE (final) as workforce role language. WCAG 2.2 (final) for the scope/stop UI.

## Connecting is not permission

Every module in this course rests on one fact that is easy to state and surprisingly easy to forget under pressure: a computer answering you is not the same fact as a person authorizing you. When a browser or a proxy opens a connection to a host, the three-way TCP handshake that follows is a property of the network, not a property of consent. A server that is reachable, responsive, and even friendly is reachable, responsive, and friendly to anyone who can route a packet to it — which, for most of the public internet, means it is reachable, responsive, and friendly to strangers it has never met and never agreed to be tested by. This course calls the fact that decides whether a test may proceed **authorization of the tester**, and it is deliberately narrow: authorization is a written record, made by someone with the standing to make it, naming a specific host and a specific tester. Everything else — a fast response, a valid certificate, a recognizable login form, a job title, a testing methodology, a quiz score — is evidence about the target or the tester's competence, and none of it is evidence about permission.

The course encodes that distinction as a single predicate, `target_is_authorized(url)`, which every lab in `labs/0.1/0.1-orientation` calls before anything resembling an attack step. The rule the function has to satisfy is one sentence you can prove false: for a URL evaluated by this course's tooling, `target_is_authorized("https://example.com/")` must return `False`, and `target_is_authorized("http://127.0.0.1:8000/notes")` may return `True`, because the second URL names a host this course's own lab tree runs on and the first names a host nobody involved in this course has any standing to grant testing permission over. Notice what the sentence does and does not claim. It does not claim that `example.com` is dangerous, poorly secured, or an attractive target — it might be none of those things. It claims only that no fact available to this function establishes permission, and in the absence of that fact the answer has to be no. A tired learner with a proxy already open, three browser tabs deep into a tutorial, is one paste away from typing a real company's URL into that proxy instead of a lab one; the function's entire job is to make that mistake produce a denial instead of a request.

```python
from urllib.parse import urlparse

ALLOWED_HOSTS = {"127.0.0.1", "localhost", "lab.securecollab.test"}

def target_is_authorized(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return host in ALLOWED_HOSTS

target_is_authorized("https://example.com/")            # False
target_is_authorized("http://127.0.0.1:8000/notes")      # True
```

Walk through why the first call has to return `False` before you walk through how it does. The URL parses cleanly, the scheme is valid, and the hostname is a real, currently-registered domain that has answered HTTP requests for decades — every syntactic fact about this URL is exactly as well-formed as the second one. The only fact that differs is that nobody who has anything to do with this course, this repository, or this learner's employer wrote `example.com` into a list of hosts a tester may act against. That is the entire basis for the denial, and it is also the entire basis this function is designed to ever use. A function that denied `example.com` because it "looked suspicious," or allowed a different public host because it "looked like a training app," would be answering a different, unreliable question — this one answers only "is this hostname a member of a written set," which is the one question that does not depend on anyone's judgment about how a target looks.

## A guide is not a permission slip

The vocabulary this module introduces — vulnerability, threat, risk, control, assurance, compliance, privacy, safety, resilience — describes the shape of security work throughout this course. None of it, by itself, describes who may test what. This matters because three respected, current, and genuinely useful documents sit close enough to "permission" in a learner's mental map that citing one can feel like citing an authorization, when it is not. The OWASP Web Security Testing Guide (WSTG), version 4.2, is a stable catalogue of testing methods — cross-site scripting checks, authentication checks, session-management checks — organized by application area. It is an excellent answer to "how would I test this login form," for a login form that is already in scope. It has never been, and does not claim to be, an answer to "may I test this login form." A chapter title naming an attack class is a description of technique, not a grant of permission, in exactly the way a cookbook chapter on knife skills is not permission to use someone else's kitchen.

The NIST NICE Framework (SP 800-181 Revision 1) sits in the same trap from a different angle. It defines work roles — "Vulnerability Assessment Analyst," "Penetration Tester" — along with the task, knowledge, and skill statements each role is built from. Holding a job title the NICE Framework recognizes says something true and useful about a person's competencies; it says nothing at all about which specific systems that person is currently authorized to test, because the framework was built to describe *work*, not to grant *access*. A live fetch of NIST's own overview of the framework, current as of this module's most recent revision, states plainly that it exists to give "a common, consistent lexicon that categorizes and describes cybersecurity work" for education, training, and workforce development — not to authorize anyone to act against a specific host. The NIST Cybersecurity Framework (CSF) 2.0 is the third document worth naming here, and it fails to be a permission slip for a related but distinct reason: it describes organizational outcomes — Govern, Identify, Protect, Detect, Respond, Recover — that an organization pursues over its *own* systems and its *own* risk posture. A company can be doing excellent CSF-aligned governance work and that says nothing about whether it, or anyone working for it, has been granted the right to run tests against a *different* company's infrastructure.

## What this predicate cannot see

A rejected alternative worth naming precisely, because it is the one a competent engineer is most likely to reach for: "check whether the host resolves to a private IP address, and allow it if so." This looks like it solves the problem functionally — private ranges are, in practice, usually inside an organization's own network — but it fails here for a structural reason rather than a coverage reason. `/etc/hosts` lets any user on a machine map any public-looking hostname to `127.0.0.1`, so "resolves to private" is a fact about local configuration a learner controls, not a fact about who granted testing permission; a learner could alias `example.com` to `127.0.0.1` and this alternative would authorize it, precisely the outcome the rule exists to prevent. This module's check compares the hostname string a caller supplies, before any resolution happens, against a small set a person actually wrote down — which is a narrower guarantee than "is this address private," but a narrower guarantee that is actually true, is worth more than a broader one that a single configuration change defeats.

## Check yourself

- Can you state, for any URL, which single fact `target_is_authorized` is allowed to depend on, and name two facts about a host (speed, certificate validity, product recognizability) that it must not depend on?
- Can you explain why an official, unmodified copy of OWASP Juice Shop running on your own machine is a legitimate practice target, while the same Juice Shop image running on a cloud instance someone else administers is not — even though the software is identical?
- Can you explain, without using the word "should," why citing WSTG's authentication-testing chapter answers a different question from "is this application in scope"?

## Practice

Run this only inside `labs/0.1/0.1-orientation/`. The data is synthetic; every hostname above is a fixture label, not a real credential or a live target.

```
python3 -m pytest labs/0.1/0.1-orientation/tests --impl vulnerable
python3 -m pytest labs/0.1/0.1-orientation/tests --impl fixed
```

The first command must show failures for the security reasons named above — a public host, a lookalike host, and a malformed URL, each wrongly treated as authorized. The second must pass every test. Do not fetch `example.com` at any point; the string itself is the test fixture, and the test asserts on the string, never on a network response.

## Where this goes next

This course's module titled "Security as invariants under attack" gives vulnerability, threat, risk, and control their full formal definitions; this lesson only needs you to hold them loosely enough to recognize that none of them means "permitted." The module titled "Penetration testing, reporting, and remediation" is where WSTG's method catalogue is finally paired with a real, written, dated engagement scope — the missing half this lesson deliberately withholds.
