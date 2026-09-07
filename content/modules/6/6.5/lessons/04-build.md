# Parse, then allow-list host and scheme

**Kind:** design-exercise
**Loop step:** 4 Build

## The rule

“Starts with https” does not cover link-local metadata. A denylist of one IP misses the next address. Following redirects off the list still fetches.

Read it as the host is a named peer. `allowed` must parse the URL, require `https`, require the hostname in a small allow-list, and deny link-local and loopback.

Unfurl needs this: host deny unless listed. Unknown host **denies**. https as a scheme does not put the host on the list.

## Picture: host deny unless listed

```mermaid
flowchart TD
  Call[allowed] --> Parse[urlparse]
  Parse --> Https{"scheme https?"}
  Https -->|no| Deny[Deny]
  Https -->|yes| Host{"host in ALLOW?"}
  Host -->|no| Deny
  Host -->|yes| Allow[Allow]
```

The importer requires `https` and host in `{"lab.securecollab.test"}`, and denies named block hosts. Fetching customer sites still wants a dedicated egress proxy. DNS rebinding and IPv6 encodings remain leftover. Open-redirect UX is a sister check. Telling the person they are leaving the site is advanced work, not this check.

The allow-list has to run before calling another service — `allowed`. **Do not fetch.**

## What the repaired files must show

Do not treat `fixed/ssrf.py` as a production egress proxy.

| After the fix | Must be true |
|---|---|
| link-local metadata URL | false |
| loopback | false |
| `https://lab.securecollab.test/og` | true |

If the host is not on the list, the answer is no. Looking like https does not put it on the list.

## What this is not

HTTPS-only regex that still allows a metadata IP. Following redirects off the list. `file:` because the scheme is “local.” Pinning DNS as complete without a proxy. `requests.get` with a timeout as the policy.

## What the tool cannot do

- DNS rebinding can change the IP after the host check unless you pin or proxy.
- IPv6 and decimal encodings of the same destination remain leftover.
- Redirect following can leave the allow-list.
- Webhook signing waits for 7.3.
- `file:` and other schemes must deny, not “local is fine.”

## Practice

Name the check (https ∧ host in ALLOW ∧ not blocked). Run:

```text
python3 -m pytest labs/6.5/6.5-lab/tests --impl fixed
```

Do not fetch the URLs.

## Use it somewhere new

Stop fetching whatever URL the form posted; parse then allow-list.

## What can still go wrong

DNS rebinding; IPv6 encodings; telling the person they left the site (advanced); dedicated egress proxy for customer sites.

## What this page is not doing

Do not curl metadata. An HTTPS prefix is not a check-in.

