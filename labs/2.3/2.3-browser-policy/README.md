# Lab: 2.3-browser-policy

**Module:** `2.3`  
**Authorized scope:** this directory (model of document.cookie). No real browser exploit pages.  
**Invariant:** A SecureCollab session cookie marked HttpOnly is not readable to script in the origin. That is **browser-enforced**, not an application output-encoding guarantee.  
**Root cause class:** trust (confusing cookie flags with XSS completeness)  
**Non-goals:** live sites, XSS payloads, copy-paste gadget chains.

## Reset

Reset only this lab (destructive for uncommitted edits in this path): first inspect `git diff -- labs/2.3/2.3-browser-policy`, then run `git restore --source=HEAD -- labs/2.3/2.3-browser-policy` only if you intend to discard those edits. Never use a repository-wide reset or restore.

## Vulnerable behavior (local only)

`js_read_session` ignores `httponly` and returns the value. HTTPS/`Secure` does not imply unreadability to JS.

## Structural fix

Honor HttpOnly. Label **CSP3** and **Trusted Types** as **Working Drafts** (2026-08-23 snapshot) — they are not this cell and not “XSS finished.”

## Verify

```bash
python3 -m pytest tests/test_httponly.py --impl vulnerable
python3 -m pytest tests/test_httponly.py --impl fixed
```

## Operate

Set-Cookie in logs should not include the session value. Report-only CSP is detection, not this property.

## Transfer

Third-party iframe: origin vs site (schemeful same-site) — new matrix rows; this lab does not prove CORS.
