# 6.2 — Browser injection and active content (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** ASVS 5.0.0 V3 (final); CWE-79 as name; CSP3 / Trusted Types are layered and some docs are still CR — do not claim they replace encoding.

## Property (start here)

Angle brackets in a note title must be encoded in HTML context (`&lt;`) so the browser does not parse an extra element. Encoding is context-specific; CSP is not this cell.

## Attacker capabilities and trust assumptions

- **Attacker:** Collaborator who can edit a title; stored XSS later in another tenant’s view.
- **Trust:** Local render(). Real DOM sinks in 2.3.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | renderer, browser HTML parser, peer user |
| Objects | title string, HTML output |
| Actions | render |
| Channels | HTML body |
| TCB | Context-aware encoder for HTML text. |
| Untrusted | Note title, display name |
| State / time | Stored now, viewed later by owner. |
| 1.1 cell | Integrity of the HTML interpreter; confidentiality of sessions if combined with 2.3 fail. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| peer | title | store | allow-data |
| browser | title | as-HTML | encoded |
| CSP | script | block | layer-not-property |
| admin | raw HTML | render | non-goal-or-tiny-exception |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/6.2/6.2-lab` file `html.py`.

## Transfer

Markdown-to-HTML sanitizer as a second parser (2.1).

## Residual risk

Trusted admin HTML — explicit tiny exception.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
