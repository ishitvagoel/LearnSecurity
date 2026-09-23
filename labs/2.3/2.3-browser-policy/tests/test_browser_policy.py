"""C1: the session cookie must be HttpOnly and Secure.
C2/C3: Access-Control-Allow-Origin must be validated against a fixed
allow-list of exact origins, and Access-Control-Allow-Credentials: true
must never accompany an origin that was not on that list.
C4: the app must send an enforcing Content-Security-Policy, not only
Content-Security-Policy-Report-Only.

These tests read response headers -- the exact signal a real browser
consults before deciding whether to expose a cross-origin response to
script, or to block a resource load. httpx's TestClient does not enforce
same-origin policy or CORS itself (it is not a browser), so a test that
reads the response *body* here would tell us nothing about what a browser
would do with it. Reading the header is the most this fixture can prove;
see lessons/05-verify.md for what it does not prove.
"""

from __future__ import annotations

from fastapi.testclient import TestClient

TRUSTED_ORIGIN = "https://app.securecollab.example"
ATTACKER_ORIGIN = "https://evil.example"


# ---------------------------------------------------------------------------
# C1 -- cookie: HttpOnly and Secure on the real Set-Cookie header.
# ---------------------------------------------------------------------------


def test_forbidden_outcome_session_cookie_missing_httponly(client: TestClient) -> None:
    resp = client.post("/login")
    set_cookie = resp.headers.get("set-cookie", "")
    assert "httponly" in set_cookie.lower(), (
        "the sc_session Set-Cookie header must carry HttpOnly -- without it, "
        "page script in the origin can read the session value through "
        "document.cookie"
    )


def test_secure_attribute_is_also_present(client: TestClient) -> None:
    resp = client.post("/login")
    set_cookie = resp.headers.get("set-cookie", "")
    assert "secure" in set_cookie.lower(), (
        "Secure is a sister rule to HttpOnly (ASVS v5.0.0-3.3.1); a "
        "session cookie should not be sent over a plaintext connection "
        "even when it is already unreadable to script"
    )


# ---------------------------------------------------------------------------
# C2/C3 -- CORS: exact-origin allow-list, credentials never follow a caller's
# own unchecked claim about who it is.
# ---------------------------------------------------------------------------


def test_trusted_origin_is_reflected_with_credentials(client: TestClient) -> None:
    resp = client.get("/notes", headers={"Origin": TRUSTED_ORIGIN, "Cookie": "sc_session=s"})
    assert resp.headers.get("access-control-allow-origin") == TRUSTED_ORIGIN
    assert resp.headers.get("access-control-allow-credentials") == "true"


def test_forbidden_outcome_attacker_origin_gets_no_credentialed_access(
    client: TestClient,
) -> None:
    resp = client.get("/notes", headers={"Origin": ATTACKER_ORIGIN, "Cookie": "sc_session=s"})
    allow_origin = resp.headers.get("access-control-allow-origin")
    assert allow_origin != ATTACKER_ORIGIN, (
        "an origin absent from the allow-list must never be reflected back "
        "as Access-Control-Allow-Origin -- reflecting it is what lets any "
        "page on the web read a signed-in member's /notes response"
    )
    assert resp.headers.get("access-control-allow-credentials") != "true" or allow_origin is None


def test_origin_vs_site_boundary_subdomain_scheme_and_port_are_each_denied(
    client: TestClient,
) -> None:
    """Origin is scheme + host + port. Each of these three callers shares
    the registrable domain a person would call "the site" with the trusted
    origin, but each is a distinct origin the allow-list must not grant:
    a different subdomain, a different scheme, and a different port."""
    for boundary_origin in (
        "https://evil.securecollab.example",  # different host (subdomain)
        "http://app.securecollab.example",  # different scheme
        "https://app.securecollab.example:8443",  # different port
    ):
        resp = client.get(
            "/notes", headers={"Origin": boundary_origin, "Cookie": "sc_session=s"}
        )
        assert resp.headers.get("access-control-allow-origin") != boundary_origin, (
            f"{boundary_origin} shares a hostname or domain with the trusted "
            "origin but is not the same origin; site and origin are not the "
            "same word"
        )


def test_missing_origin_header_does_not_crash_and_grants_nothing(client: TestClient) -> None:
    """A same-origin browser navigation, or a plain curl call, sends no
    Origin header at all. The app must not raise, and must not manufacture
    a CORS grant for a request that never claimed to be cross-origin."""
    resp = client.get("/notes", headers={"Cookie": "sc_session=s"})
    assert resp.status_code == 200
    assert "access-control-allow-origin" not in {k.lower() for k in resp.headers.keys()}


def test_anti_fake_lookalike_domain_is_not_treated_as_the_trusted_origin(
    client: TestClient,
) -> None:
    """Anti-fake test. A plausible fake fix checks membership with a
    substring or suffix test instead of exact set membership, for example
    `"securecollab.example" in origin` or
    `origin.endswith("securecollab.example")` (note: no leading dot). Both
    would wrongly treat this attacker-registered domain as trusted, because
    "evilsecurecollab.example" contains "securecollab.example" as a
    trailing substring even though it shares no dot-delimited label with
    it. Real fixed code, using exact set membership, must deny it."""
    lookalike = "https://evilsecurecollab.example"
    resp = client.get("/notes", headers={"Origin": lookalike, "Cookie": "sc_session=s"})
    assert resp.headers.get("access-control-allow-origin") != lookalike, (
        "a domain that merely contains the trusted origin as a substring "
        "is not the trusted origin; the allow-list check must be exact, "
        "not endswith/in"
    )


# ---------------------------------------------------------------------------
# C4 -- CSP: an enforcing header must exist, not only Report-Only.
# ---------------------------------------------------------------------------


def test_csp_is_enforced_not_only_reported(client: TestClient) -> None:
    resp = client.get("/notes", headers={"Cookie": "sc_session=s"})
    csp = resp.headers.get("content-security-policy")
    assert csp is not None, (
        "Content-Security-Policy-Report-Only only asks the browser to send "
        "a violation report; it does not block anything. A blocking "
        "Content-Security-Policy header must also be present."
    )
    assert "object-src 'none'" in csp and "base-uri 'none'" in csp, (
        "ASVS v5.0.0-3.4.3's floor for a global policy"
    )
