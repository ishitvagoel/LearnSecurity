"""Fixed: duplicate tenant keys are rejected so every reader shares one meaning.

The first attempt at this fix collected every occurrence of the tenant key
with a second regex (`re.findall`), the same technology the ACL-side reader
already used, just applied more thoroughly. That was itself a real bug, not
a hypothetical one: a regex matching `"tenant"\\s*:\\s*"([^"]*)"` only
recognizes a *string-typed* value in quotes, so `{"tenant":1,"tenant":"tA"}`
has one occurrence the regex cannot see at all -- the integer `1` -- and the
"collect every occurrence" logic silently believed there was only one
occurrence to check.

The second attempt used `json.loads`'s own `object_pairs_hook` to collect
every occurrence, which correctly fixed the non-string-value gap -- but it
introduced a different one, caught by independent review: `object_pairs_hook`
fires for *every* object literal in the document, at every nesting depth, not
only the top-level object. Collecting "every pair named tenant, anywhere in
the document" means a `tenant` key buried inside an unrelated nested object
(an attachment, a metadata blob -- anything the submitter controls) is
treated as though it were the top-level claim. A note with *no* top-level
tenant field at all was being accepted, using a company id scraped from
whatever nested structure happened to contain a `tenant` key -- the exact
forbidden outcome this module exists to prevent, reintroduced by the fix
meant to close a different gap.

`object_pairs_hook` is called innermost-first: by the time `json.loads`
returns, the *last* invocation the hook has seen is necessarily the root
object's own pairs, because every object nested inside it was already
resolved (and folded into a plain `dict` value) before the root's own call.
Collecting occurrences only from that last invocation restricts "every
occurrence of tenant" to what it was always supposed to mean: every
occurrence at the top level of the note object itself, not anywhere in the
document.
"""

from __future__ import annotations

import json


def _root_tenant_occurrences(text: str) -> list[object]:
    """Every value assigned to a "tenant" key at the TOP LEVEL of the note
    object only -- not inside any nested object -- exactly as the real JSON
    parser sees them, including non-string values and escaped keys that a
    regex over the raw text cannot reliably recognize.

    object_pairs_hook fires once per object literal, innermost first, so
    the last invocation it makes is always the root object: every nested
    object was already resolved into a plain dict by the time the root's
    own pairs are handed to the hook.
    """
    invocations: list[list[tuple[str, object]]] = []

    def collect(pairs: list[tuple[str, object]]) -> dict:
        invocations.append(pairs)
        return dict(pairs)

    json.loads(text, object_pairs_hook=collect)
    root_pairs = invocations[-1] if invocations else []
    return [value for key, value in root_pairs if key == "tenant"]


def ingest_note(text: str) -> dict:
    try:
        occurrences = _root_tenant_occurrences(text)
    except json.JSONDecodeError:
        # Malformed JSON syntax is not a duplicate-key disagreement, but it
        # is exactly as much "no single meaning was established" as a
        # disagreement is, and it must fail closed for the same reason.
        return {"accepted": False, "acl_tenant": "", "stored_tenant": "", "body": None}

    # Compare the actual values, not a stringified form -- 1 and "1" are
    # different JSON values, and treating them as the same after both get
    # converted to the string "1" would be a new, quieter version of the
    # exact mistake this fix exists to close.
    one_meaning = bool(occurrences) and all(v == occurrences[0] for v in occurrences[1:])
    reported = str(occurrences[0]) if occurrences else ""
    if not one_meaning:
        return {"accepted": False, "acl_tenant": reported, "stored_tenant": reported, "body": None}

    data = json.loads(text)
    return {"accepted": True, "acl_tenant": reported, "stored_tenant": reported, "body": data.get("body")}
