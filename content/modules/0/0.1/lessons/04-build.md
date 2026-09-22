# Allow only named local hosts, and deny everything the parser cannot read

**Kind:** design-exercise
**Loop step:** 4 Build

## The smallest repair, and why it has two parts, not one

The repair this lesson builds toward looks small enough to write in five lines, and the temptation with a fix this size is to stop as soon as the obvious case — a public host — is denied, without asking what the function should do when it cannot even determine what host it was given. `target_is_authorized` has to do two structurally different jobs: parse the URL into a hostname, and compare that hostname to a written set. Each job has its own failure mode, and a repair that fixes the comparison while leaving the parse unguarded has fixed exactly one of the two things this module's rule actually requires. `urlparse`, the standard-library function this course's fixture relies on, raises `ValueError` on a URL whose authority component is malformed — most commonly an unmatched IPv6 bracket, `"http://[::1/path"` being the concrete example this module's tests use — and raises `AttributeError` or `TypeError` if the argument is not a string at all. A function that lets either exception escape has not built a security check with a gap in it; it has built two different functions and only tested one of them, because "returns `False` for `example.com`" and "returns `False` for a string it cannot parse" are independent claims that the same five lines can satisfy or fail independently.

```python
from urllib.parse import urlparse

ALLOWED_HOSTS = {"127.0.0.1", "localhost", "lab.securecollab.test"}

def target_is_authorized(url: str) -> bool:
    try:
        host = (urlparse(url).hostname or "").lower()
    except (ValueError, AttributeError, TypeError):
        return False
    return host in ALLOWED_HOSTS
```

Every clause in this function earns its place by ruling out a specific way the earlier, broken versions failed. The `try`/`except` exists because a parse failure is not the same fact as "this host is not on the list" — it is "no host was determined at all," and the two facts must produce the same *action* (deny) without being confused for the same *reason*, which is why the except clause returns `False` explicitly rather than letting an unhandled exception crash whatever called this function and leave its caller to guess. The `.lower()` call exists because `ALLOWED_HOSTS` is written in lowercase and a URL's hostname is not guaranteed to arrive that way — `HTTP://LAB.SECURECOLLAB.TEST/` names the same host as the lowercase form, and a case-sensitive comparison would deny a legitimate local host for a reason that has nothing to do with authorization. The `or ""` guards against `urlparse` succeeding but finding no hostname at all — an empty string, correctly, is not a member of `ALLOWED_HOSTS`, so this path denies too, just through the normal comparison rather than through the exception handler.

## Denying is not the same as failing

A rejected alternative worth naming precisely: wrap the entire function body in a bare `except Exception: return False` instead of naming the three specific exception types. This looks safer at first glance — it catches everything, so nothing can possibly escape — and it fails here because "catches everything" is a description of an exception handler's blast radius, not of whether the code inside it is correct. A bare `except Exception` would silently swallow a genuine programming mistake introduced later in this same function — a typo'd variable name, a wrong attribute access, an accidentally-deleted import — and report it to every caller as an ordinary, expected denial, indistinguishable from a real out-of-scope host. Naming `ValueError`, `AttributeError`, and `TypeError` specifically means this function fails loudly on any exception it was not designed to expect, which is the correct behavior for a security check: a bug in the check itself should surface as a crash someone notices and fixes, not as a denial that looks exactly like the check working as intended. Denying because the input was genuinely unparseable, and failing because the code has a bug, are two different events, and a function that cannot tell them apart from the outside has made itself harder to debug in exactly the case — a scope check silently wrong — where debuggability matters most.

## The lookalike-host table

The comparison half of the fix is `host in ALLOWED_HOSTS`, and its correctness depends entirely on that being an exact-membership test against a Python `set`, never a substring, prefix, or suffix test. The previous lesson's model already introduced the shape of this mistake; here is what it costs concretely, worked through four inputs a reviewer might actually paste while testing a candidate fix by hand:

| Input hostname | `host in ALLOWED_HOSTS` (correct) | `host.endswith(a)` for some `a` in the set (rejected) |
|---|---|---|
| `lab.securecollab.test` | `True` | `True` |
| `127.0.0.1` | `True` | `True` |
| `evillab.securecollab.test` | `False` | `True` — wrongly authorized |
| `lab.securecollab.test.evil.com` | `False` | `False`, but only because this one is a *prefix* match failure the same reviewer's `startswith` variant would get equally wrong in the other direction |

The two correct rows and the two rejected-alternative rows agree with each other exactly often enough — on the inputs a reviewer is likely to type first — to make the rejected version look finished after a quick manual check. It is not finished; it is wrong on inputs nobody typed yet, which describes essentially every security defect that ships. The build step this lesson is named for is not "make the tests pass" — it is "make the comparison a claim you can state precisely enough that a specific, adversarial input either satisfies it or does not," and "is an exact member of this three-item set" is precise in that sense in a way that "resembles a member of this set" is not.

## Practice

Run this only inside `labs/0.1/0.1-orientation/`. `lab.securecollab.test` and its lookalikes are fixture labels; none of them resolves anywhere, and none should be typed into a browser.

```
python3 -m pytest labs/0.1/0.1-orientation/tests --impl fixed -v
```

All seven tests must pass. Before you run it, predict which of the seven would still fail if you deleted the `try`/`except` block from `fixed/scope.py` and left everything else unchanged — then delete it, run the tests, and check your prediction against the actual failure.

## Check yourself

- Can you state, separately, what the `try`/`except` block defends against and what the `in ALLOWED_HOSTS` comparison defends against, without collapsing the two into one sentence?
- Given `host.endswith(a)` and `host in ALLOWED_HOSTS`, can you construct one input where they disagree, and say which one is right for that input and why?
- If a redirect during a later module's lab work leaves the allowed host for a different one, does this function's `True` result from the first request still apply to the second? What would have to happen for the answer to be checked again?
