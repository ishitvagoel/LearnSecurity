# Derive a mechanism from the property

**Kind:** design-exercise
**Loop step:** 4 Build

## The property comes first

Choose one row from your catalogue. For example: a Company B member must not receive Company A note-body bytes through the public read path.

A smallest candidate mechanism is a server-side decision immediately before release of the body:

```text
allow = current_member.company == note.company
        and current_member is active
        and requested action == read_body
```

Unknown identity, object, relationship, or policy state denies. The browser-supplied company label is input to check, never the grant.

## State the limits

This mechanism does not prove that logs, exports, backups, workers, caches, or a compromised database are safe. Those are separate claim rows or later review triggers. Record the mechanism, its proof obligations, and one alternative you rejected.

## Check yourself

Can another engineer implement the mechanism without guessing what “admin,” “secure,” or “has access” means? If not, narrow the property before adding another tool.
