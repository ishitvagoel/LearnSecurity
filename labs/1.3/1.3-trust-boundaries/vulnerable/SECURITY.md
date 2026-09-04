# Vulnerable variant — boundary claims and intentional defects

## Deliberately false claim

This variant claims that an illustrative edge check and an application check independently protect a worker-only export. Both checks read `X-SecureCollab-Internal` from the same public mapping, and the public caller also chooses the service label. They are correlated uses of one untrusted assertion, not independent worker provenance.

The worker path then treats any registered worker plus any known grant as broad ability. It does not bind the grant to worker, tenant, action, exact object set, expiry, or successful-use state. It proceeds when required evidence is unavailable.

## Intended observable failures

- public metadata creates a worker-only export;
- Worker B uses Worker A’s grant;
- tenant, action, and same-tenant object scope widen;
- expired and consumed grants remain usable;
- a high-impact effect proceeds without required evidence;
- the dependency report calls correlated controls independent.

Valid exact export, ordinary public denial, unknown worker/grant denial, malformed duplicate denial, summary projection, privacy-safe server-held capability/correlation references, and the no-network/file/process safety constraint remain as regression cases.

## Scope warning

This file documents intentionally vulnerable local course code. It is not a production pattern and is never authorization to test a live system. The metadata names are synthetic triggers, not an evasion recipe. The root cause is requester-derived provenance plus ambient authority, not one spelling of a header.
