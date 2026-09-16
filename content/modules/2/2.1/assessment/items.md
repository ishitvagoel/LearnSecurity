# 2.1 assessment items

**Learner-facing. No answers.** Answers, distractor rationales, and banding live in `content/assessment/keys/2.1.md` — do not open the key before attempting an item.

Write enough that another engineer could check your reasoning. Practical gates require evidence for every critical invariant; a strong answer in one area never compensates for a missing one elsewhere.

---

## 1. Discrimination — rule, tool, or false assurance

Four statements a reviewer might find in a pull request touching note ingest:

**A.** "We use Pydantic v2 to model the tenant field, so duplicate keys can't reach storage."
**B.** "The same request bytes must yield one tenant identifier, used identically by the who-is-allowed check and by storage; if two readers of those bytes would disagree, ingest refuses."
**C.** "JSON object names should be unique per RFC 8259, so this isn't a real concern."
**D.** "We added a regex filter that rejects any body containing the string `tenant` twice."

Sort each statement into **rule**, **tool**, or **false assurance**, and for each one that is not the rule, name specifically what it would need to add or change to become one.

**Claim assessed:** C1 · **Outcome:** Demonstrate a local parser differential as a property failure

## 2. Discrimination — property vs. mechanism for parser agreement

Four statements about a note-ingest system:

**A.** "We validate the request body against a JSON Schema before processing it."
**B.** "Our staging environment has never shown a duplicate-key error in six months of logs."
**C.** "`ingest_note` collects every occurrence of the tenant key and refuses unless the full set has exactly one distinct value."
**D.** "Every occurrence of a repeated key in the same object must resolve to one value before that value is used by any consumer; otherwise, the object is refused."

Identify which statement states the property and which state mechanisms or proxies for it, and rank the three mechanism claims by how close each comes to being real evidence for the property.

**Claim assessed:** C1, C2 · **Outcome:** Demonstrate a local parser differential as a property failure

## 3. Diagnosis — a different checker's gap

```python
def ingest_note(text: str) -> dict:
    values = re.findall(r'"tenant"\s*:\s*"([^"]*)"', text)
    first = values[0] if values else ""
    last = values[-1] if values else ""
    if first != last:
        return {"accepted": False, "acl_tenant": first, "stored_tenant": last, "body": None}
    data = json.loads(text)
    return {"accepted": True, "acl_tenant": first, "stored_tenant": last, "body": data.get("body")}
```

This checker is not `vulnerable/parse_note.py`, and it is not `fixed/parse_note.py` — it is a third implementation that compares the first and last regex matches directly rather than using two independently-implemented readers. Give it the object `{"tenant":"tA","body":"x","tenant":"tC","tenant":"tA"}`. Name the root cause of why this function accepts that object, the precondition under which the gap matters in practice, and the impact if it ships this way — as three distinct answers, not one answer restated three times.

**Claim assessed:** C1, C4 · **Outcome:** Demonstrate a local parser differential as a property failure

## 4. Diagnosis — reading a candidate fix

A teammate proposes this fix, reasoning that it directly addresses the module's own two-key example:

```python
def ingest_note(text: str) -> dict:
    acl = _first_tenant(text)
    stored = _last_tenant(text)
    if acl != stored:
        return {"accepted": False, "acl_tenant": acl, "stored_tenant": stored, "body": None}
    return {"accepted": True, "acl_tenant": acl, "stored_tenant": stored, "body": json.loads(text).get("body")}
```

Determine, without running any code, whether this fix passes `test_middle_duplicate_is_not_silently_dropped`, and explain your reasoning by tracing the specific input `{"tenant":"tA","body":"x","tenant":"tC","tenant":"tA"}` through this exact function.

**Claim assessed:** C4 · **Outcome:** Separate validation, canonicalization, sanitization, and encoding by context

## 5. Diagnosis — which operation is missing

A team's note-ingest pipeline does the following, in order: (1) checks that the `tenant` field is a string matching a known-company allow-list; (2) escapes the note body for safe HTML rendering in a future preview feature; (3) strips control characters from the body before storage. The pipeline still exhibits the parser differential this module teaches. Name which of the four operations — validation, canonicalization, sanitization, encoding — is missing from this list entirely, and explain why the three present operations, even performed correctly, cannot substitute for it.

**Claim assessed:** C2, C3 · **Outcome:** Explain bytes vs characters, Unicode, canonicalization, encodings, grammars, serialization, interpreter boundaries

## 6. Design — two candidate fixes under a constraint

Given the vulnerable fixture, two engineers propose fixes: Engineer A compares only the first and last occurrence of the tenant key (item 4's fix); Engineer B collects every occurrence and requires the full set to have exactly one value. Under the constraint that the fix must correctly handle an object with an arbitrary number of duplicate keys, not merely two, choose between the two proposals and defend your choice, including the specific case where your chosen fix still falls short of a complete guarantee.

**Claim assessed:** C4 · **Outcome:** Separate validation, canonicalization, sanitization, and encoding by context

## 7. Design — the worker re-parse gap

Lesson 02's design table names a row for "a worker re-parses stored bytes" as a gap this fixture's tests do not cover, since no queue or worker exists in the practice. A colleague argues the ingest-time check is sufficient because "the data was already validated once." Under the constraint that any proposal must name a specific, concrete failure mode a re-parse could introduce that ingest-time validation cannot catch, propose what a worker-safe design would need to guarantee, and state what residual risk your proposal still leaves open.

**Claim assessed:** C5 · **Outcome:** Transfer the map when a new format is added

## 8. Transfer — clinic REST and GraphQL

Using the clinic scenario from `lessons/07-transfer.md`, state which of this module's five claims (C1–C5) transfer unchanged when the format changes from a single JSON object to two grammars (REST and GraphQL) carrying the same logical field, which claims need a materially different treatment, and why a GraphQL alias mechanism specifically requires more than a first-versus-last comparison.

**Success criteria:** Your answer must explain the GraphQL alias mechanism in your own words (not by repeating this module's phrasing), and must connect it explicitly to the same "check every occurrence, not only two of them" principle Lesson 03's middle-duplicate counterexample established for JSON.

**Claim assessed:** C1–C5 · **Outcome:** Transfer the map when a new format is added

## 9. Operate — the deny-line signal

Write the log line your system would emit when a note is refused because two readers disagreed about the tenant. State which fields it must carry, which field it must never carry, and why a metric alone — without a quarantine procedure for rows a bypassing code path might already have written — is not sufficient operational coverage.

**Claim assessed:** C5 · **Outcome:** Transfer the map when a new format is added

---

## Evidence checklist

- [ ] Parser-boundary map for the SecureCollab request path (Lesson 02), naming every reader
- [ ] Local differential annotation: which two readers disagree, and on what input (Lesson 03)
- [ ] Lab `labs/2.1/2.1-parser-boundaries`: forbidden outcome named as **a parser differential where the ACL tenant disagrees with the stored tenant**
- [ ] `vulnerable/` tests show 4 of 6 failing for the stated security reason; `fixed/` tests show 6 of 6 passing
- [ ] Transfer answer (item 8) naming which claims change and which do not, with the GraphQL alias mechanism explained
- [ ] Operate signal (item 9) that carries no note body or raw JSON blob
