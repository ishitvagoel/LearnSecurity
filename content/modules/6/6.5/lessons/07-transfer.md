# Same idea when a clinic fetches a lab-result PDF

**Kind:** transfer-challenge
**Loop step:** 7 Transfer

## Use it somewhere new

You get a clinic form that **fetches a lab-result PDF from a URL**.

On the notes app, `allowed` must be false for a link-local metadata URL. Parse, then allow-list host and scheme. For a clinic, the importer must not treat the posted URL as permission to dial.

Also name webhook delivery (7.3) as the same egress deputy, without running those systems.

## Picture: the PDF URL is still a steering wheel

Calling it “PDF URL” instead of “preview URL” does not move the work.

| Notes app this week | Clinic sketch |
|---|---|
| Preview URL on a note | Lab-result PDF URL on a form |
| `allowed` | Importer allow-check |
| Parse, then host and scheme allow-list | Same check before any GET |
| Member supplying a preview URL | Clinician supplying a PDF URL — **not** a live clinic |

```mermaid
flowchart LR
  Pdf[PDF URL field] --> Belief[UI believes it is a document]
  Egress[server GET] --> Reality[whoever the URL names]
```

If the importer GETs whatever URL the form posted, the check is gone. FastAPI, an HTTPS prefix, and a private-IP denylist of one address do not name the peer. Webhook delivery (7.3) is the same deputy with a different verb. Open-redirect UX is a sister check; do not fetch to demonstrate it.

Link-local and loopback still have to be false; only the named lab (or clinic) host on https may be true. Switching the importer to HTTPS without a host allow-list leaves the server as deputy. The local check is `test_link_local_metadata_is_denied` — on a practice, not a live PDF or metadata endpoint.

## Prompt — clinic fetch of a lab-result PDF

1. who can act (URL field — not a live clinic or cloud metadata probe);
2. what you trust (parsed host allow-list; “https” prefix is not);
3. what must not happen (`allowed` true for link-local);
4. a test idea on **local** practice files only (predicate, no fetch — never on the real clinic);
5. leftover (redirects, DNS rebinding, IPv6, `file:`, telling the person they left the site);
6. whether a human-read “could not fetch PDF” status must not use color as the only cue (readable error, not a spinner that retries the bad URL).

## What is not good enough

| Reject | Why |
|---|---|
| “HTTPS only” | Scheme is not host identity |
| Live metadata / clinic probe | Course rules |
| Famous-bugs nickname as the rule | Awareness after the cause |
| HTTP 200 as egress evidence | Wrong observation |
| Fetching to confirm the deny | Course rules |

## Practice

One page. No answer keys. The only running system you may break is `labs/6.5/6.5-lab`. Do not fetch.

## What this page is not doing

Do not try live-target server-side requests. Do not use real PDFs or metadata. This page does not finish a check-in.
