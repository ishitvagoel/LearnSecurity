# 2.2 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/2.2.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — rule, tool, or false assurance

Four statements a reviewer might find in a pull request touching SecureCollab's notes cache:

**A.** "We added `Cache-Control: private` to every `/notes/{id}` response."
**B.** "The cache key for `/notes/{id}` is `(note_id, company)`, where `company` is the value the caller's own API key resolved to — never a header, and never the path alone."
**C.** "Our CDN only accepts HTTPS connections, so cross-company cache leakage can't happen."
**D.** "We added a job that clears the whole cache every 60 seconds, so any leaked entry is short-lived."

Sort each statement into **rule**, **tool**, or **false assurance**, and for each one that is not the rule, name specifically what it would need to add or change to become one.

**Claim assessed:** C1 · **Outcome:** Identify every point where a shared cache or a forwarded-identity header could substitute a wrong company for the caller's own bound identity

## 2. Discrimination — property vs. mechanism for company resolution

Four statements about how SecureCollab's origin decides which company a request belongs to:

**A.** "The API key is looked up in a table only the origin controls, and the key itself is never transmitted anywhere in plaintext."
**B.** "The company an authorization decision uses must come only from the caller's own credential-derived resolution; a client-supplied `X-Company`, `X-Tenant`, or `Host` value is never treated as authoritative for that decision, whether or not it happens to agree with the credential."
**C.** "Our access logs have never shown a request where `X-Company` disagreed with the API key's own company."
**D.** "Every request to this endpoint is served over a TLS 1.3 connection."

Identify which statement states the property this module calls C2, and which three are mechanism or proxy claims. Rank the three mechanism claims by how close each comes to being real evidence for the property.

**Claim assessed:** C2 · **Outcome:** Identify every point where a shared cache or a forwarded-identity header could substitute a wrong company for the caller's own bound identity

## 3. Diagnosis — a different hop check's gap

```python
def hop_is_trustworthy(expected_hostname, presented_hostname, cert_trusted_ca, tls_version):
    if cert_trusted_ca is None:
        return False
    if tls_version not in {"1.2", "1.3"}:
        return False
    return presented_hostname == expected_hostname
```

This function is not `vulnerable/app.py`'s `hop_is_trustworthy`, and it is not `fixed/app.py`'s either — it is a third implementation that fails closed on an *unknown* trust state but has not been checked against an *explicitly resolved untrusted* one. Give it `expected_hostname="notes-origin.securecollab.internal"`, `presented_hostname="notes-origin.securecollab.internal"`, `cert_trusted_ca=False`, `tls_version="1.3"`. Name the root cause of why this function reports the hop trustworthy, the precondition under which the gap matters in practice, and the impact if it ships this way — as three distinct answers, not one answer restated three times.

**Claim assessed:** C3 · **Outcome:** State precisely what a TLS 1.3 handshake does and does not prove about a hop's peer, and name the additional checks a deployment must add

## 4. Diagnosis — a cache key that still trusts the header

A teammate proposes this fix, reasoning that it adds the missing company dimension to the cache key:

```python
def get_note(note_id, api_key, x_company, authorization):
    company = _resolve_company(api_key, None)   # hardened: never reads x_company
    cache_key = (note_id, x_company or company)
    cached = _CACHE.get(cache_key)
    if cached is not None:
        return {"body": cached, "source": "cache"}
    text = _ORIGIN_STORE.get((note_id, company))
    if text is None:
        raise HTTPException(status_code=404, detail="not found")
    _CACHE[cache_key] = text
    return {"body": text, "source": "origin"}
```

Determine, without running any code, whether this fix still lets a caller holding only `key-A` (bound to `companyA`) read `companyB`'s already-cached note `n2` by sending `X-Company: companyB` — given that `companyB` legitimately read `n2` once already, with no header, before the attacker's request. Trace both requests' `cache_key` values through this exact function and explain your conclusion.

**Claim assessed:** C1, C2 · **Outcome:** Identify every point where a shared cache or a forwarded-identity header could substitute a wrong company for the caller's own bound identity

## 5. Diagnosis — reading a one-hop-covers-all description

SecureCollab's origin adds a new outbound call to a downstream audit service. A colleague writes this as the request-path model update: "The origin's connection to the audit service is authenticated, because the whole path already uses TLS 1.3 — we verified that for the browser-to-edge hop when we built `hop_is_trustworthy`." Name specifically what this description gets wrong, state what a correct model of the new origin-to-audit-service hop would have to add that the description omits, and name the one module claim (by its letter) this description violates.

**Claim assessed:** C4 · **Outcome:** Produce a request-path diagram naming, per hop, what was authenticated and the cache-key policy that must hold

## 6. Design — a new CDN under a constraint

Ops adds a new CDN in front of the existing edge. Its default configuration caches `GET /notes/{note_id}` for 30 seconds, keyed by its own default (method + path + query string only), before the request ever reaches the origin. Under the constraint that `fixed/app.py`'s own code has not changed at all, state which of this module's claims (C1, C2) the CDN's default configuration silently reverts and which it leaves untouched, name one CDN-level configuration change that would restore the reverted invariant without touching origin code, and design one detection signal — using the vocabulary of `lessons/06-operate.md` — that would catch a recurrence of exactly this misconfiguration even if nobody remembers to re-check the CDN's settings.

**Claim assessed:** C1, C5 · **Outcome:** Given a new CDN or reverse proxy, predict which cache-key and forwarded-identity assumptions change and design the detection and recovery response

## 7. Transfer — clinic `/patients/me` and `Vary: Cookie`

Using the clinic scenario from `lessons/07-transfer.md`, a teammate proposes closing the cross-patient cache leak by adding `Vary: Cookie` to the cached `/patients/me` response, reasoning that the CDN will then vary its stored representation per session cookie. State which of this module's claims (C1–C5) this proposal actually satisfies, if any; explain precisely what `Vary: Cookie` instructs a cache to do differently from binding the cache key to the resolved patient; and name one attacker capability this proposal leaves completely open even for a cache that honors `Vary: Cookie` perfectly.

**Success criteria:** Your answer must state that `Vary: Cookie` selects among representations a cache already has by matching a request header's raw value, and does not itself resolve or verify any identity — it is not a substitute for C1's `(path, patient)` key derived from the origin's own session lookup. It must name at least one capability the proposal leaves open: a patient who authenticates by bearer token rather than a cookie gets no protection from this header at all, and an intermediary that rewrites or shares a cookie value across two patients' requests can still collide two representations `Vary: Cookie` would treat as identical.

**Claim assessed:** C1–C5 · **Outcome:** Given a new CDN or reverse proxy, predict which cache-key and forwarded-identity assumptions change and design the detection and recovery response

## 8. Operate — two signals, one boolean

Write the two distinct log lines SecureCollab's origin would emit for: (a) a cache hit whose served company does not match the caller's bound company, and (b) a relay rejected because `hop_is_trustworthy` returned `False`. Name the field that lets an operator distinguish, within case (b) alone, a hostname mismatch from an untrusted-CA rejection from an unsupported TLS version, and explain why collapsing all three into a single `hop_rejected` event with no reason field would be operationally worse — even though all three cases share the same boolean outcome.

**Claim assessed:** C1, C3, C5 · **Outcome:** Given a new CDN or reverse proxy, predict which cache-key and forwarded-identity assumptions change and design the detection and recovery response

---

## Evidence checklist

- [ ] Request-path diagram (Lesson 02) naming, per hop, what was authenticated and what was not, including the cache-key policy at the shared store
- [ ] Local reproduction of all three forbidden outcomes: a shared-cache cross-company hit, a forwarded-header company override, and a hostname-mismatched hop accepted as trustworthy (Lesson 03)
- [ ] Lab `labs/2.2/2.2-request-path`: `vulnerable/` tests show 9 of 15 failing for the stated security reasons; `fixed/` tests show 15 of 15 passing
- [ ] Transfer answer (item 7) correctly explaining why `Vary: Cookie` does not implement C1, and naming at least one capability it leaves open
- [ ] Operate signals (item 8) for both a cache-mismatch and a hop-rejection, neither carrying a note body, a session token, or key material
