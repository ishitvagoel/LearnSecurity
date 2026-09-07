# A context map someone else can test

**Kind:** design-exercise
**Loop step:** 2 Model

## Could someone else name the checks from your map?

“We turned on a content-security policy” is not this lesson. A map someone else can test names **the sink, the context, and what encoding applies**.

`render(body)` wrapping a `<p>` text node — no live page. No real browser.

## Picture: one sink, one context in this practice

```mermaid
flowchart TD
  Body[title string] --> P["p text context"]
  P --> Enc{"< encoded?"}
```

Attribute, JavaScript, and URL contexts are named holes, not this practice.

## Picture: React is not what you trust

```mermaid
flowchart TD
  JSX[React JSX text] --> Help[Usually encodes]
  DHTML[dangerouslySetInnerHTML] --> Raw[Untrusted HTML]
  FastAPI[FastAPI template] --> Raw
```

Framework defaults help only at the constructors you actually use.

## Step 1: name the pieces

| Piece | This system |
|---|---|
| Who | Collaborator editing a title |
| What | HTML text vs markup |
| Actions | `render` |
| Paths | HTML document |
| What you trust | The HTML-text encoder |
| What you do not trust | The title / body string |
| Time | Stored title, later drawn |
| Integrity rule | Integrity of the HTML interpreter |

## Step 2: write cells the practice can fail

| Who | What | Action | Decision |
|---|---|---|---|
| app | title | HTML text | encode `<` |
| attacker | title | as HTML grammar | deny |
| markdown | HTML | second parse | 2.1 leftover |
| content-security policy | script loads | extra layer | draft, not this check |

## Practice

Draw text vs attribute vs JavaScript vs URL. In `labs/6.2/6.2-lab`, mark `html.py`. Label the sink as HTML text even in the repaired tree — the fix is encoding at that sink, not pretending a header became encoding.

## Use it somewhere new

Clinic nickname. Markdown pipeline.

## What can still go wrong

Trusted admin HTML. Content-security policy in report-only mode. Encoding for a JavaScript string (a different rule).

## What this page is not doing

Answer keys are not on this site.
