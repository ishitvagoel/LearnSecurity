# SecureCollab Phase 1 — HTML text encoding

Design stub for Module 6.2. Not a production browser.

## Freeze

- Local `render(body)` wrapping a text node.
- Tame marker `<` must become `&lt;`. No exploit kit.

## Data, not grammar

HTML text encoding is the cell. CSP3 and Trusted Types are draft layers, not substitutes. Markdown is a second parser (2.1).

## Tests

`&lt;` present and extra tags absent is the evidence. A CSP header is not.
