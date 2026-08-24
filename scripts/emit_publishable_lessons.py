#!/usr/bin/env python3
"""Emit 1.2-density unique lessons, assessments, and module.yaml stamps.

Skips module 1.1 (reference) and 1.2 (already unique). Rewrites every other unit.
Does not mark gates or milestones complete.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path("/workspace")
CONTENT = ROOT / "content"
SKIP_LESSONS = {"1.1", "1.2"}
TODAY = "2026-08-24"
REVIEWER = "quality-reviewer (publishable rewrite vs 1.1/1.2 bar)"

# lab slug overrides where the structural fixture is not `{id}-lab`
LAB_SLUG = {
    "0.1": "0.1-orientation",
    "0.2": "0.2-bridge",
    "1.1": "1.1-invariant-catalogue",
    "1.2": "1.2-authority-matrix",
    "1.3": "1.3-trust-boundaries",
    "1.4": "1.4-risk-register",
    "2.1": "2.1-parser-boundaries",
    "2.2": "2.2-request-path",
    "2.3": "2.3-browser-policy",
    "2.4": "2.4-state-time",
    "E1": "e1-lab",
    "E2": "e2-lab",
    "E3": "e3-lab",
    "E4": "e4-lab",
    "E5": "e5-lab",
    "E6": "e6-lab",
}


def lab_slug(mid: str) -> str:
    return LAB_SLUG.get(mid, f"{mid}-lab")


def module_dir(mid: str) -> Path:
    if mid == "11":
        return CONTENT / "modules" / "11" / "11"
    if mid.startswith("E"):
        return CONTENT / "modules" / "e" / mid
    phase = mid.split(".")[0]
    return CONTENT / "modules" / phase / mid


def lab_dir(mid: str) -> Path:
    parent = "11" if mid == "11" else mid
    return ROOT / "labs" / parent / lab_slug(mid)


# Each spec is unique. Fields drive eight differently structured lessons.
SPECS: dict[str, dict] = {}


def add(mid: str, **kw) -> None:
    spec = {"id": mid, **kw}
    # Aliases so the renderer can use a single field set.
    spec.setdefault("framework_not", spec.get("framework_not", ""))
    spec.setdefault("root_cause", spec.get("root_cause", ""))
    spec.setdefault("state_time", spec.get("state_time", ""))
    SPECS[mid] = spec


add(
    "0.1",
    title="Security engineering orientation",
    system="SecureCollab course lab",
    standards="NIST CSF 2.0 (final) GV/ID; OWASP WSTG v4.2 (final) as *lab method*, not a licence to scan the internet; NICE Framework as role language only.",
    property="A URL is in scope only if it is a named local lab host (127.0.0.1, localhost, lab.securecollab.test). example.com, a employer production API, and a classmate’s deployed preview are out of scope even if they are “easy to hit.”",
    attacker="A motivated learner who can type any URL into a proxy; a future self who is tired and copies a blog “try this host” snippet.",
    trust="You trust this repository’s lab trees and official OWASP training apps when the README names them. You do not trust “the internet,” robots.txt, or a recruiter’s staging site without written scope.",
    cell="Safety + accountability (1.1): unauthorized testing is both a legal and an engineering failure.",
    subjects="Learner, course maintainer, unnamed internet operator",
    objects="Local lab process, public website, production API",
    actions="Send HTTP, replay a capture, run pytest",
    channels="Browser, proxy, pytest against labs/",
    tcb="The allow-list in labs/0.1/0.1-orientation/fixed/scope.py",
    untrusted="Any host header, any “open bug bounty” rumour, any AI-suggested target",
    state_time="Scope is per engagement; yesterday’s lab VM IP is not forever-authorized.",
    root_cause="Authorization collapsed into reachability: if TCP connects, it was treated as in-scope.",
    preconditions="Learner has a proxy; a public URL is one paste away.",
    impact="Unlawful access; course expulsion; harm to uninvolved operators; poisoned evidence.",
    prevention="Allow-list local names; fail closed; written scope template.",
    detection="Log denied hosts without fetching them; supervisor review of proxy history in class only.",
    recovery="Stop, document, do not exfiltrate; notify instructor. Do not “just this once” continue.",
    framework_not="Burp, ZAP, or curl existing is not authorization. CSF GV is governance language, not a pentest permit.",
    mechanism_limit="An allow-list of three names still fails if you SSH to a stolen hostname that resolves locally via /etc/hosts tricks — check what you actually connected to.",
    bypass="DNS rebinding, hosts-file aliases, or “it’s just a redirect to localhost.” Still out of scope unless the README says so.",
    residual="Official Juice Shop on your machine is OK; a random cloud Juice Shop you do not own is not.",
    practice="Write a three-line scope: in, out, stop condition. Run the lab pair.",
    transfer="Your company staging URL: what written artifact would make it in-scope? (Not a Slack thumbs-up.)",
    transfer_product="A contractor asked to “quickly test our customer’s WordPress.”",
    hitl=True,
    wcag="Scope templates and stop-buttons in course UI must be keyboard-operable (WCAG 2.2). A mouse-only “I agree” is not informed consent.",
    review_findings=(
        "SECURITY.md says “any URL the proxy can open.”",
        "No stop condition when a redirect leaves 127.0.0.1.",
        "Live-target language in a learner note.",
        "Quiz score treated as permission to scan.",
    ),
    misconceptions=(
        "If it has a login page it is a lab",
        "WSTG chapter titles are the syllabus",
        "Defensive learning requires attacking strangers",
    ),
    operate_signals="Denied-host log line {url, reason=out_of_scope}; never store response bodies from out-of-scope hosts.",
    build_structure="Parse hostname; compare to ALLOWED_HOSTS; default False.",
    break_observe="vulnerable/scope.py returns True for https://example.com/.",
    verify_cases="localhost allowed; example.com denied; missing host denied.",
    matrix=(
        ("learner", "http://127.0.0.1:8000/notes", "GET", "allow"),
        ("learner", "https://example.com/", "GET", "deny"),
        ("learner", "https://lab.securecollab.test/", "GET", "allow"),
        ("learner", "https://customer.example/", "GET", "deny"),
    ),
    forbidden="HTTP to a non-allowlisted host treated as authorized",
    py_module="scope.py",
    evidence="Personal lab rules, scope template, vocabulary map",
)

add(
    "0.2",
    title="Diagnostic and adaptive bridge",
    system="SecureCollab placement path",
    standards="NICE Secure Systems Development competencies (informative); this course’s Gate 1 evidence rules. A quiz vendor’s score report is not ASVS.",
    property="A placement quiz score of 100 does not skip 1.2 complete mediation, Gate 1 evidence, or the authority matrix. Adaptive paths may skip *orientation prose*, never *invariants*.",
    attacker="A hurried learner optimizing for the shortest click-path; a future hiring manager who equates a badge with tenant isolation.",
    trust="The diagnostic repository is local and honest. Quiz items are not production secrets.",
    cell="Integrity of the learning system: false competency is a safety defect for later labs.",
    subjects="Learner, diagnostic scorer, Gate 1 reviewer",
    objects="Quiz result, 1.2 matrix artifact, Gate 1 packet",
    actions="Skip, remediate, attest",
    channels="Course site, local git",
    tcb="diagnostic.py skip rule in labs/0.2/0.2-bridge",
    untrusted="Self-attestation, LMS percentage, LinkedIn badge",
    state_time="Score is a moment; Gate 1 is evidence over time.",
    root_cause="A number was treated as a capability (ambient “you’re advanced”).",
    preconditions="Quiz exists; skip() consulted the number.",
    impact="Learner reaches 4.4/6.x without a matrix; false assurance in reviews.",
    prevention="Skip only missing *tooling* units; never skip mediation labs.",
    detection="Path log: skipped ids vs required 1.2/1.3/1.4.",
    recovery="Re-open 1.2; do not back-date Gate 1.",
    framework_not="The LMS mastery percentage is not a security property of SecureCollab.",
    mechanism_limit="A better quiz still cannot observe whether you can write a deny cell.",
    bypass="Memorizing 1.2 answers without running the lab.",
    residual="Bridge units still needed for Git/SQL/HTTP gaps — those skips are OK when diagnostics show skill.",
    practice="Name one thing a 100% quiz cannot prove about tenant isolation.",
    transfer="A vendor SANS/OSCP score used to skip your team’s threat-model review.",
    transfer_product="Onboarding at a clinic-booking SaaS.",
    hitl=True,
    wcag="Diagnostic UI must not be color-only “green = skip Phase 1” (WCAG 2.2 1.4.1).",
    review_findings=(
        "if score >= 80: skip_phase(1)",
        "No link from diagnostic to 1.2 evidence",
        "Badge screenshot as Gate 1",
        "Adaptive path hides 1.4 accessibility residual",
    ),
    misconceptions=(
        "Placement is a security clearance",
        "Fast learners skip invariants",
        "Tool fluency is threat modeling",
    ),
    operate_signals="Audit skipped-module list on each cohort export.",
    build_structure="quiz_score_grants_phase1_skip always False.",
    break_observe="vulnerable diagnostic returns True at score 100.",
    verify_cases="100 does not skip; missing Git still recommends a bridge unit.",
    matrix=(
        ("learner", "1.2 lab", "skip", "deny"),
        ("learner", "0.1 prose", "skip-if-known", "allow"),
        ("learner", "Gate 1 packet", "attest-by-quiz", "deny"),
        ("reviewer", "evidence pack", "sign", "allow-if-artifacts"),
    ),
    forbidden="Quiz score used as authorization to skip 1.2/Gate 1",
    py_module="diagnostic.py",
    evidence="Diagnostic repository and individualized path",
)

add(
    "1.3",
    title="Trust boundaries and attack surface",
    system="SecureCollab",
    standards="OWASP Threat Modeling (project guidance, living); ASVS 5.0.0 V15 (final) architecture; Saltzer economy of mechanism (1975, seminal).",
    property="A browser-supplied header such as X-SecureCollab-Internal is on the untrusted side of the API boundary. It must not dump all tenants’ notes. Only a worker bound in-process (or a real service identity later) may export.",
    attacker="Anyone who can set headers on HTTPS to the public API, including a modified Next.js client and a stolen browser extension.",
    trust="FastAPI process + PostgreSQL roles you will define; the HTTP client is hostile. CDN/WAF are not yet in the TCB.",
    cell="Confidentiality (1.1) via a boundary failure, not a new CWE slogan.",
    subjects="Anonymous client, logged-in member, bound worker",
    objects="All notes export, single note, worker credential",
    actions="export_notes, set header, bind worker",
    channels="HTTP headers, internal mesh (future), queue (7.4)",
    tcb="Server-side worker_bound flag / mTLS later — never the client header.",
    untrusted="Every header, cookie, JWT kid, IP, geo",
    state_time="A header that was “internal” on yesterday’s VPC is still untrusted from the browser today.",
    root_cause="Transitive trust: the handler believed a string that crossed the boundary.",
    preconditions="Public listener; header check instead of identity.",
    impact="Cross-tenant dump; blast radius = all notes.",
    prevention="Ignore client internal headers; bind worker identity in the process/mesh.",
    detection="Alert on that header appearing on the public listener (it is a probe).",
    recovery="Rotate worker credentials; audit export logs; notify tenants if bodies left.",
    framework_not="FastAPI dependency injection does not know your TCB. Next.js rewrite headers are client-controlled after the browser.",
    mechanism_limit="A WAF dropping the header is defense in depth, not the property. Attackers will use another field.",
    bypass="Body field is_internal=true; GraphQL; gRPC metadata; websocket first message.",
    residual="A real compromised worker still exports. Detect and revoke (7.4, 10.5).",
    practice="Draw the line: browser | TLS | app | DB. Star every input that currently influences export_notes.",
    transfer="CDN “authenticated origin pull” — is the CDN in the TCB? What header does it add?",
    transfer_product="Clinic booking: X-Internal-Admin on the public API.",
    hitl=False,
    wcag="",
    review_findings=(
        "if request.headers.get('X-SecureCollab-Internal'): return all_notes()",
        "SECURITY.md claims “API is private because we use HTTPS”",
        "No test for header present + worker_bound false",
        "Trusting X-Forwarded-For as client identity",
    ),
    misconceptions=(
        "TLS is a trust boundary for headers",
        "Security by an internal-sounding header name",
        "Defense in depth means any layer can be skipped",
    ),
    operate_signals="Public-edge log: internal-header-seen without worker identity.",
    build_structure="export_notes ignores client headers; requires worker_bound=True.",
    break_observe="vulnerable/surface.py treats X-SecureCollab-Internal as worker identity.",
    verify_cases="{} -> []; header-only -> []; worker_bound -> two notes.",
    matrix=(
        ("browser", "all notes", "export", "deny"),
        ("browser+header", "all notes", "export", "deny"),
        ("bound worker", "all notes", "export", "allow"),
        ("member tA", "tA notes", "list", "allow-via-1.2"),
    ),
    forbidden="Client internal header dumps all tenants' notes",
    py_module="surface.py",
    evidence="Trust-boundary diagram and attack-surface inventory",
)

add(
    "1.4",
    title="Risk, people, economics, usable security, and resilience",
    system="SecureCollab",
    standards="WCAG 2.2 (final, W3C Rec); NIST SP 800-63-4 (final) as identity *risk* language; CISA Secure by Design (public guidance, final); NIST CSF 2.0 GV.OC.",
    property="A high-impact recovery control that is color-only or mouse-only is a security failure: people will be locked out or will route around it (shared passwords, screenshot of the “red” button). Usability is in the TCB for human-mediated controls.",
    attacker="A tired legitimate user; an abuser who controls the mouse; a support attacker who prefers friction that pushes users to email secrets.",
    trust="Lab recovery UI fixture only. Real users would include keyboard-only and low-vision operators.",
    cell="Safety + availability + confidentiality: inaccessible recovery causes lockout *or* unsafe workarounds that leak notes.",
    subjects="Account owner, support agent, abuser in shared housing",
    objects="Recovery confirm control, backup codes, session",
    actions="confirm_recovery, cancel, request_support",
    channels="Browser UI, email (later 4.1), phone support",
    tcb="The control’s accessible name, keyboard path, and non-color cue.",
    untrusted="Color, hover-only hit targets, “users will figure it out”",
    state_time="Recovery happens under stress and time pressure.",
    root_cause="Psychological acceptability ignored; control designed for a demo mouse.",
    preconditions="High-impact action gated by a widget is_usable_accessible() fails.",
    impact="Lockout; or user pastes recovery codes into a chat; residual 1.1 confidentiality loss.",
    prevention="Keyboard operable, name in accessible tree, not color-only (WCAG 2.2).",
    detection="Support-ticket spike for “can’t click recover”; telemetry on cancel vs confirm without pointer.",
    recovery="Offer an alternative accessible path; do not lower assurance by emailing the note body.",
    framework_not="A React component library “accessible by default” is not your journey. You still test the recovery path.",
    mechanism_limit="CAPTCHA or “confirm in the app” can recreate the same exclusion.",
    bypass="Users share an always-on admin session to avoid the broken recovery UX.",
    residual="Coercion: a physically present attacker can still force a confirmation. Record as residual (do not pretend UX fixes coercion).",
    practice="Describe the control in words a screen-reader user would hear. If you cannot, it fails.",
    transfer="Step-up auth on a clinic portal: if the second factor UI is mouse-only, what property fails?",
    transfer_product="Banking re-auth dialog.",
    hitl=True,
    wcag="WCAG 2.2 Success Criteria 2.1.1 Keyboard, 1.4.1 Use of Color, 2.5.8 Target Size (Minimum) apply to this control. They are not a privacy policy.",
    review_findings=(
        "Confirm button has no accessible name",
        "Destructive action distinguished only by red vs green",
        "Mouse-only drag-to-confirm",
        "Risk register lists residual as “users should be careful”",
    ),
    misconceptions=(
        "Accessibility is a separate compliance track from security",
        "Friction always increases security",
        "Work factor applies only to attackers, not to legitimate users stuck in a flow",
    ),
    operate_signals="Recovery success/fail by input modality; never log recovery codes.",
    build_structure="recovery_confirm_control exposes role=button, name, keyboard=True, color_only=False.",
    break_observe="vulnerable control is color- and mouse-only.",
    verify_cases="is_usable_accessible True only when name+keyboard+non-color cue exist.",
    matrix=(
        ("owner", "recovery", "keyboard-confirm", "allow"),
        ("owner", "recovery", "color-only", "deny-as-control"),
        ("abuser", "recovery", "coerce", "residual"),
        ("support", "codes", "read-aloud-over-phone", "deny"),
    ),
    forbidden="High-impact recovery control is color- or mouse-only",
    py_module="recovery.py",
    evidence="Risk register with assumptions, user-harm, residual, accessibility",
)

add(
    "2.1",
    title="Bytes, encodings, parsers, and interpreter boundaries",
    system="SecureCollab",
    standards="ASVS 5.0.0 V5 (final) input; RFC 8259 JSON (STD 90); Unicode UAX #15 as *normalization*, not a security control by itself.",
    property="If a note JSON object repeats the tenant key, ingest must reject (or both the ACL decision and the stored row must see the same tenant). A parser that keeps the first key for ACL and the last key for storage is a confidentiality failure.",
    attacker="A member who can POST JSON; a proxy that re-encodes Unicode; a second parser in a worker.",
    trust="One agreed parser in the app. The client encoder is hostile. PostgreSQL jsonb is another parser — do not assume it matches Python json.",
    cell="Confidentiality (cross-tenant) caused by *disagreement*, not by missing login.",
    subjects="Poster (tB), ACL checker, storage writer, later reader",
    objects="JSON bytes, ACL tenant, stored tenant, note body",
    actions="ingest_note, parse, persist",
    channels="HTTP body, worker re-parse, DB jsonb",
    tcb="A single parse result object used for both ACL and persist.",
    untrusted="Duplicate keys, overlong UTF-8, NFC vs NFD names",
    state_time="The same bytes parsed tomorrow by a new library version.",
    root_cause="Two interpreters, two meanings of the same bytes.",
    preconditions="Duplicate tenant keys in one object; split parse.",
    impact="tB body stored as tA or ACL sees tA while disk sees tB.",
    prevention="Reject duplicate keys; pass one parse tree everywhere.",
    detection="Parse-error metric; differential test corpus in CI.",
    recovery="Quarantine ambiguous rows; do not “repair” by guessing.",
    framework_not="Pydantic v2 defaults are not “duplicate keys impossible.” stdlib json keeps the last key.",
    mechanism_limit="A WAF string filter for “tenant twice” fails on whitespace and Unicode escapes.",
    bypass="UTF-16 body, YAML, multipart, GraphQL variables.",
    residual="Honest unique-key JSON still needs 1.2 mediation.",
    practice="Write the two-parser diagram for ACL vs storage on the lab’s AMBIGUOUS blob.",
    transfer="GraphQL and REST both ingest the same note — two grammars.",
    transfer_product="Clinic booking: duplicate patient_id keys.",
    hitl=False, wcag="",
    review_findings=(
        "json.loads used twice; ACL on first, store on second",
        "Comment “JSON can’t have duplicate keys” (RFC 8259 recommends but parsers differ)",
        "No corpus test for duplicate keys",
        "Normalizing display names as a substitute for tenant ids",
    ),
    misconceptions=("Encoding is a crypto problem", "One parser is as good as another", "Validation equals canonicalization"),
    operate_signals="ingest_reject_duplicate_key count; never log raw ambiguous bodies.",
    build_structure="Reject duplicate keys or compare acl_tenant == stored_tenant.",
    break_observe="vulnerable parse_note.py splits ACL vs storage on duplicate tenant.",
    verify_cases="CLEAN accepted with tA; AMBIGUOUS rejected or consistent.",
    matrix=(
        ("poster tA", "CLEAN json", "ingest", "allow"),
        ("poster tB", "duplicate tenant keys", "ingest", "deny"),
        ("worker", "re-parse stored bytes", "must-match", "allow-only-if-same"),
        ("reader tA", "stored body", "read", "1.2 cell"),
    ),
    forbidden="Parser differential: ACL tenant disagrees with stored tenant",
    py_module="parse_note.py",
    evidence="Parser-boundary map and ambiguity tests",
)

add(
    "2.2",
    title="HTTP, TLS, proxies, CDNs, and cache keys",
    system="SecureCollab",
    standards="RFC 9110 HTTP Semantics (final); RFC 9846 TLS 1.3 (final); ASVS 5.0.0 V12 (final). TLS is transport authenticity, not a cache-key.",
    property="A cache entry for GET /notes/n1 must include the bound tenant in the key. Tenant B must not receive tenant A’s body. HTTPS does not imply this.",
    attacker="Tenant B on a shared CDN/proxy; a neighbor on a corporate TLS-inspecting proxy.",
    trust="Origin app can set cache keys. The CDN is honest but greedy. Clients are hostile.",
    cell="Confidentiality via shared mechanism (Saltzer least common mechanism).",
    subjects="tA member, tB member, cache node",
    objects="Note body, cache key, Authorization, Host",
    actions="cache_put, cache_get",
    channels="TLS, HTTP, CDN POP",
    tcb="Origin cache-key policy (tenant + path + auth).",
    untrusted="URL path alone, “Vary: Accept-Encoding” only, client-supplied X-Tenant",
    state_time="Cached 60s after tA’s GET — tB’s GET in that window.",
    root_cause="Key omitted the subject’s tenant; shared store.",
    preconditions="Shared cache; path-only key; tA populated the entry.",
    impact="Cross-tenant read without guessing ids.",
    prevention="Key = (tenant_id, route, representation). Default private for notes.",
    detection="Cache-hit with mismatched tenant id in logs (no body).",
    recovery="Purge the prefix; treat as 1.1 incident if bodies escaped.",
    framework_not="Next.js fetch cache and FastAPI HTTPException defaults do not encode tenant.",
    mechanism_limit="Cache-Control: private still fails if your CDN is configured to cache anyway.",
    bypass="Normalized URLs, HTTP/2 push, stale-while-revalidate serving tA to tB.",
    residual="Operational error at the CDN remains; monitor.",
    practice="Write the key tuple for /notes/n1. Run the lab.",
    transfer="Authenticated RSS or export CSV via CDN.",
    transfer_product="Clinic: cached /patients/me.",
    hitl=False, wcag="",
    review_findings=(
        "Cache-Control: public on /notes/{id}",
        "Key is path only",
        "Comment “TLS so cache is safe”",
        "Purge API not in the incident runbook",
    ),
    misconceptions=("HTTPS means no cache bugs", "CDNs are only a performance layer", "Vary: Cookie is enough forever"),
    operate_signals="cdn_hit_tenant_mismatch; purge playbook.",
    build_structure="cache_get requires same tenant as cache_put.",
    break_observe="vulnerable cache.py keys only on path.",
    verify_cases="tA hit works; tB get is None.",
    matrix=(
        ("tA", "/notes/n1", "GET-hit", "own-body"),
        ("tB", "/notes/n1", "GET", "miss-or-own"),
        ("anon", "/notes/n1", "GET", "deny"),
        ("ops", "cache", "purge-prefix", "allow"),
    ),
    forbidden="Shared cache returns tenant A's body to tenant B",
    py_module="cache.py",
    evidence="Request-path diagram and cache-key tests",
)

add(
    "2.3",
    title="Browser security model",
    system="SecureCollab",
    standards="HTML Living Standard cookies (living); RFC 6265bis drafts remain **draft** if cited; ASVS 5.0.0 V3 (final); CSP3 is **not** this lab’s property.",
    property="A session cookie marked HttpOnly must not be readable by script in the lab DOM. That is a *browser* cell. It does not mean XSS is impossible (6.2) and does not make CSP3 (Candidate Recommendation / draft-ish depending on pin) a substitute for encoding.",
    attacker="Injected script in origin (later 6.2); a malicious extension (residual).",
    trust="Browser honors HttpOnly. The app must actually set the flag. Extensions are outside this TCB.",
    cell="Session confidentiality against script (not against the network — that’s TLS).",
    subjects="Page script, browser cookie jar, attacker XSS",
    objects="sc_session cookie",
    actions="js_read_session, document.cookie",
    channels="DOM, Cookie header",
    tcb="Browser cookie jar + server Set-Cookie flags.",
    untrusted="Any JavaScript bundle, including yours after XSS.",
    state_time="Cookie lifetime vs XSS window.",
    root_cause="Session presented to the script interpreter.",
    preconditions="Cookie without HttpOnly; script runs.",
    impact="Session theft then 1.2 as the thief.",
    prevention="HttpOnly; Secure; careful SameSite — still not XSS-proof.",
    detection="Token-binding / anomaly (later); XSS reports.",
    recovery="Revoke session (4.3); rotate.",
    framework_not="Next.js “cookies() are httpOnly by default” is not true for every cookie you set manually.",
    mechanism_limit="HttpOnly does not stop network theft, CSRF (6.3), or native apps reading the store.",
    bypass="XSS in a sibling cookie that is not HttpOnly; MITM without Secure.",
    residual="Browser extensions; physical access.",
    practice="Name three things HttpOnly does *not* prove. Run the lab.",
    transfer="React Native WebView cookie bridge.",
    transfer_product="Clinic patient portal session cookie.",
    hitl=False, wcag="",
    review_findings=(
        "document.cookie used to persist session",
        "SECURITY.md equates HttpOnly with “no XSS”",
        "CSP Report-Only treated as enforcement (see E2)",
        "Missing Secure on the same cookie",
    ),
    misconceptions=("HttpOnly is XSS defense", "SameSite is CSRF complete", "localStorage is safer than cookies"),
    operate_signals="Set-Cookie without HttpOnly in staging scans.",
    build_structure="js_read_session returns None when httponly True.",
    break_observe="vulnerable cookies.py exposes session to script.",
    verify_cases="HttpOnly session not script-readable.",
    matrix=(
        ("page script", "HttpOnly cookie", "read", "deny"),
        ("browser", "Cookie header", "send-to-origin", "allow"),
        ("XSS", "session", "steal-via-js", "deny-if-HttpOnly"),
        ("network attacker", "cookie", "read-on-wire", "TLS-not-this-lab"),
    ),
    forbidden="Script reads the HttpOnly session cookie",
    py_module="cookies.py",
    evidence="Browser policy matrix and cookie tests",
)

add(
    "2.4",
    title="State, time, concurrency, and distributed failure",
    system="SecureCollab",
    standards="ASVS 5.0.0 V2/V8 (final); OWASP Top 10:2025 A10 as *awareness*, not the definition; RFC 9110 safety/idempotency language.",
    property="A retried share with the same idempotency key must not create a second share. Timeouts are a security property (integrity of the share graph), not only UX.",
    attacker="A client retrying after 504; a double-click; a worker at-least-once delivery (7.4).",
    trust="Local share store. Clocks may skew; do not rely on “user won’t retry.”",
    cell="Integrity of authorization state over time.",
    subjects="Sharer, retrying client, share table",
    objects="Share row, idempotency key, note n1",
    actions="share_note, retry",
    channels="HTTP POST, queue redelivery",
    tcb="Idempotency store keyed by (actor, key) with the first outcome.",
    untrusted="Client “I only clicked once”; load balancer retries",
    state_time="Two POSTs 200ms apart; worker redelivery tomorrow.",
    root_cause="Non-idempotent side effect + retry = extra grant.",
    preconditions="Timeout; client retries same key; handler inserts again.",
    impact="Extra principal on the note (1.2 cell changes).",
    prevention="Persist key → share id; second POST returns the first.",
    detection="Duplicate-key metric; share_count anomaly.",
    recovery="Revoke extra shares; notify owner.",
    framework_not="FastAPI does not dedupe POSTs. HTTP 201 twice is still two rows.",
    mechanism_limit="Keys that expire too fast replay as new shares.",
    bypass="New key each retry (client bug); GET-with-side-effect.",
    residual="Lost first response still needs a read-your-write path.",
    practice="Draw the state machine: pending → shared; retry edges labeled.",
    transfer="Payment capture (E3) and invite tokens (6.6) are the same shape.",
    transfer_product="Clinic: double-book the last slot.",
    hitl=True,
    wcag="Disable-on-submit is not the property (users retry). Accessible “still working” status (WCAG 4.1.3) must not encourage extra POSTs with new keys.",
    review_findings=(
        "INSERT share on every POST",
        "Idempotency key in a log comment only",
        "Test only happy-path single click",
        "Fail-open on idempotency store timeout",
    ),
    misconceptions=("Retries are a client bug not ours", "200 means once", "Databases are automatically idempotent"),
    operate_signals="share_count vs unique keys; never fail-open if the key store is down.",
    build_structure="share_note keyed by idempotency_key; share_count stays 1.",
    break_observe="vulnerable share.py increments on every call.",
    verify_cases="two calls with k1 => count 1.",
    matrix=(
        ("owner", "n1", "share-once", "allow"),
        ("owner", "n1", "share-retry-same-key", "no-second-row"),
        ("owner", "n1", "share-new-key", "policy-cap-3.4"),
        ("worker", "n1", "redeliver", "same-as-retry"),
    ),
    forbidden="Retry creates a second share grant",
    py_module="share.py",
    evidence="State machine plus replay tests",
)

# --- Phase 3 ---
add(
    "3.1",
    title="Assets, classification, and security requirements",
    system="SecureCollab",
    standards="NIST CSF 2.0 Identify (final); ASVS 5.0.0 V14 (final); NIST Privacy Framework 1.0 (final). Classification is a property of a *field*, not a spreadsheet sticker.",
    property="Note bodies are Confidential. An application log line for note_read must not contain the body. Labels in Confluence do not enforce this.",
    attacker="Operator with log access; SIEM vendor; another tenant’s admin who can read shared observability.",
    trust="Local log sink. Real ELK is another TCB later (10.5).",
    cell="Confidentiality + privacy of the body.",
    subjects="App logger, operator, SIEM",
    objects="note body, log line, classification tag",
    actions="log_event, read_logs",
    channels="stdout, log drain",
    tcb="Redaction in the logging API used by handlers.",
    untrusted="print(), f-strings, APM capture, exception repr",
    state_time="Logs retained 30 days after the note is deleted (5.1).",
    root_cause="Body treated as debug context.",
    preconditions="Handler logs the event payload with the body.",
    impact="Confidential field in a lower-trust store.",
    prevention="Structured logs with allow-listed fields; redact bodies.",
    detection="Secret scanning on log streams; DLP on the sink.",
    recovery="Purge matching logs; rotate if tokens present.",
    framework_not="uvicorn access logs will happily store query strings (4.3). FastAPI does not know Confidential.",
    mechanism_limit="Regex redaction misses encodings (2.1).",
    bypass="Error traces, slow-query logs, full-packet APM.",
    residual="Operators still see metadata (ids). That’s a different cell — document it.",
    practice="List every sink that might see a body (app, DB logs, CDN, mobile crash — 8.5).",
    transfer="Clinic notes vs appointment time: two classes, two sinks.",
    transfer_product="EHR-lite booking card.",
    hitl=False, wcag="",
    review_findings=(
        "logger.info('read %s', note.body)",
        "Classification spreadsheet with no test",
        "Debug=True in a “staging” that shares prod data",
        "Exception middleware dumps request body",
    ),
    misconceptions=("If we classified it, it is protected", "Logs are internal so safe", "Privacy policy equals redaction"),
    operate_signals="log_redaction_miss alerts; purge runbook.",
    build_structure="log_event redacts body to 'redacted'/'confidential'.",
    break_observe="vulnerable classify.py interpolates the body.",
    verify_cases="body not in line; marker present.",
    matrix=(
        ("handler", "body", "log", "deny"),
        ("handler", "note_id", "log", "allow"),
        ("operator", "logs", "read", "meta-only"),
        ("SIEM vendor", "body", "index", "deny"),
    ),
    forbidden="Confidential note body appears in a log line",
    py_module="classify.py",
    evidence="Data inventory, classification, requirements backlog",
)

add(
    "3.2",
    title="Threat modeling",
    system="SecureCollab",
    standards="OWASP Threat Modeling (project); NIST SP 800-154 remains **draft/withdrawn-track** — treat as informative only; ASVS 5.0.0 as later requirements, not a model.",
    property="A green scanner does not yield an empty threat list. SecureCollab’s model must still include a cross-tenant reader and a hostile Next.js client.",
    attacker="Cross-tenant member; hostile browser; future worker identity (named now as a trigger).",
    trust="Local threats_from_scan fixture. Real scanners are coverage tools (9.4), not oracles.",
    cell="Integrity of the *assurance story* — missing threats are untested 1.1 cells.",
    subjects="Modeler, scanner, reviewer",
    objects="Threat list, scan status, DFD",
    actions="threats_from_scan, review",
    channels="CI, threat-model markdown in git",
    tcb="Versioned model with owners and triggers.",
    untrusted="Scanner empty-result, “no High findings”",
    state_time="Model stale after a new share path (spiral).",
    root_cause="Tool output substituted for thinking.",
    preconditions="scan_green=True; model copies it.",
    impact="No test for 1.2; residual unowned.",
    prevention="Seed mandatory threats; scanner findings are extra, not the set.",
    detection="CI fails if required threat ids missing.",
    recovery="Add the threat, tests, owner; do not back-date.",
    framework_not="STRIDE stickers on a DFD are not a model without invalidation conditions.",
    mechanism_limit="LINDDUN is valuable for 5.1; it still won’t list IDOR for you automatically.",
    bypass="Moving threats to “accepted” without residual.",
    residual="Unknown unknowns — review triggers exist for that.",
    practice="List three threats that remain if every CVE is patched.",
    transfer="Add webhooks (7.3): which new threats?",
    transfer_product="Clinic SMS reminders.",
    hitl=False, wcag="",
    review_findings=(
        "threats = [] if scan_green",
        "No cross-tenant-read item",
        "Model not in git",
        "STRIDE letters without assets",
    ),
    misconceptions=("Green scan means no threats", "Threat models are pre-code only", "Awareness lists are the threat list"),
    operate_signals="model_age_days; missing-mandatory-threat CI.",
    build_structure="threats_from_scan always includes cross-tenant-read.",
    break_observe="vulnerable model.py returns [] when scan is green.",
    verify_cases="green scan still lists cross-tenant-read.",
    matrix=(
        ("modeler", "cross-tenant-read", "must-list", "allow-item"),
        ("scanner", "empty", "replace-model", "deny"),
        ("reviewer", "stale model", "merge", "deny"),
        ("CI", "mandatory ids", "gate", "allow"),
    ),
    forbidden="Green scanner produces an empty SecureCollab threat model",
    py_module="model.py",
    evidence="Versioned threat model with owners and triggers",
)

add(
    "3.3",
    title="Secure architecture patterns",
    system="SecureCollab",
    standards="ASVS 5.0.0 V4/V13 (final); CISA Secure by Design (final guidance); Saltzer least privilege (1975, seminal).",
    property="The application DB role used by FastAPI must not SELECT another tenant’s rows even if a handler forgets a WHERE. Architecture is a second mediation, not a substitute for 1.2.",
    attacker="Buggy handler; SQLi later (5.5/6.1); stolen app credentials.",
    trust="PostgreSQL RLS/role in the lab stand-in. The app still must mediate.",
    cell="Confidentiality defense-in-depth.",
    subjects="app role, migrator role, superuser",
    objects="notes table rows by tenant",
    actions="can_select",
    channels="SQL session",
    tcb="Role grants + optional RLS; migrator not used at runtime.",
    untrusted="ORM default connection user",
    state_time="Migration-time SUPERUSER leftover in DATABASE_URL.",
    root_cause="One omnipotent DB user shared by app and migrate.",
    preconditions="app role can_select other tenant.",
    impact="Forgot WHERE becomes a breach.",
    prevention="Least-privilege role; RLS as extra layer (5.5).",
    detection="pg_audit on cross-tenant seqscans.",
    recovery="Rotate DB password; review grants.",
    framework_not="SQLAlchemy session is not a tenant scope.",
    mechanism_limit="RLS bypassed by table owners and SECURITY DEFINER (E5).",
    bypass="Connection pooler user; analytics replica without RLS.",
    residual="Stolen migrator role — separate credential, shorter life.",
    practice="Draw app vs migrator vs analyst roles.",
    transfer="Serverless function with a shared “admin” connection string.",
    transfer_product="Clinic: billing replica.",
    hitl=False, wcag="",
    review_findings=(
        "DATABASE_URL uses superuser",
        "Comment “RLS later” in production path",
        "Analytics role SELECT *",
        "No test can_select(app, tB, tA) is False",
    ),
    misconceptions=("Microservices are automatically isolated", "RLS replaces application authz", "Network VPC is tenant isolation"),
    operate_signals="grant_drift check in CI; connection-user metric.",
    build_structure="can_select('app', 'tB', 'tA') is False.",
    break_observe="vulnerable roles.py allows app to read tA as tB.",
    verify_cases="app cannot select other tenant.",
    matrix=(
        ("app", "own tenant rows", "SELECT", "allow"),
        ("app", "other tenant rows", "SELECT", "deny"),
        ("migrator", "ddl", "ALTER", "allow-offline"),
        ("analyst", "bodies", "SELECT", "deny-or-tokenize"),
    ),
    forbidden="App DB role can SELECT another tenant's rows",
    py_module="roles.py",
    evidence="ADRs with rejected alternatives",
)

add(
    "3.4",
    title="Business logic and abuse-resistant design",
    system="SecureCollab",
    standards="ASVS 5.0.0 V2 (final); OWASP API Security Top 10:2023 API4/API6 as *awareness*; this lab is a product rule, not a CWE name.",
    property="A note share grant cannot be applied enough times to exceed the product cap (5 members). Abuse is a logic invariant.",
    attacker="A scripted member; a confused deputy UI that retries (2.4).",
    trust="Local counter. Real rate limits are 6.7.",
    cell="Integrity of the share policy; availability of the owner’s threat model (too many readers).",
    subjects="Owner, automated client",
    objects="share count, cap=5",
    actions="add_share",
    channels="API loop",
    tcb="Server-side cap in the same transaction as insert.",
    untrusted="Client disabling the “max 5” UI",
    state_time="Eight rapid POSTs.",
    root_cause="Policy only in the UI.",
    preconditions="add_share without cap.",
    impact="Unbounded readers; 1.2 matrix explodes.",
    prevention="Check count in the write path; reject 6th.",
    detection="share_cap_denied metric; anomaly on one note.",
    recovery="Trim extra grants; notify owner.",
    framework_not="HTML max=5 is not enforcement.",
    mechanism_limit="Cap on /share but not on /import or GraphQL.",
    bypass="Parallel requests before commit (needs transaction/lock — 2.4).",
    residual="Legitimate teams >5 need an owned exception (E6).",
    practice="State machine: shares=0..5; 6th denied.",
    transfer="Invite tokens (6.6) and export quotas (6.7).",
    transfer_product="Clinic: max 3 guardians per child.",
    hitl=True,
    wcag="Error “share limit reached” must be programmatically announced (WCAG 4.1.3), not only a red border.",
    review_findings=(
        "Cap in React only",
        "No transaction around count+insert",
        "Test loops 8 times and expects success",
        "Support tool bypasses cap without audit",
    ),
    misconceptions=("Business logic is not security", "Rate limits replace product caps", "CWE-799 is the requirement"),
    operate_signals="denied 6th share; lock contention on hot notes.",
    build_structure="add_share stops at 5.",
    break_observe="vulnerable share_limit.py has no cap.",
    verify_cases="eighth add leaves last <= 5.",
    matrix=(
        ("owner", "share 1-5", "add", "allow"),
        ("owner", "share 6", "add", "deny"),
        ("script", "parallel 6", "add", "deny-with-lock"),
        ("support", "override", "add", "audited-exception"),
    ),
    forbidden="Share grants exceed the product cap of 5",
    py_module="share_limit.py",
    evidence="Misuse cases, workflow state machine, abuse plan",
)

# --- Phase 4 ---
add(
    "4.1",
    title="Identity lifecycle",
    system="SecureCollab",
    standards="NIST SP 800-63-4 (final) identity lifecycle; ASVS 5.0.0 V6 (final). Deprovision is part of 1.2 over time.",
    property="After an account is deleted, that subject’s leftover session must not read notes. Lifecycle is complete mediation across account states, not a login screen.",
    attacker="Stolen session cookie after the user left the org; a delayed worker using the old user id.",
    trust="Local user+session maps. Real IdP SLO is extra (4.5).",
    cell="Authorization over time (1.2 + 2.4).",
    subjects="deleted user, leftover session, admin",
    objects="session token, notes",
    actions="delete_user, session_valid, read",
    channels="cookie, worker job",
    tcb="Session store checks user state on every use.",
    untrusted="JWT still-signed after deletion (4.3/4.5)",
    state_time="T+0 delete; T+1h replay cookie.",
    root_cause="Authentication artifact outlived the subject.",
    preconditions="delete_user removes profile only.",
    impact="Ex-employee or attacker with the cookie still reads tenant notes.",
    prevention="Invalidate sessions (and tokens, workers) in the same use-case.",
    detection="Use of session after user_state=deleted.",
    recovery="Mass revoke; rotate signing keys if tokens self-verify.",
    framework_not="Starlette SessionMiddleware does not know HR offboarding.",
    mechanism_limit="Email “you’re deleted” is not revocation.",
    bypass="Refresh tokens, mobile offline cache (8.2), shared device.",
    residual="Backups still contain the user row — 5.1.",
    practice="List every artifact that must die with the user.",
    transfer="Contractor access end-date; support impersonation tickets.",
    transfer_product="Clinic: departing clinician.",
    hitl=True,
    wcag="Offboarding confirmation must be accessible (1.4). A mouse-only “delete user” is a missed revoke.",
    review_findings=(
        "DELETE FROM users without session purge",
        "JWT exp 30d ignored on delete",
        "Worker still has user_id",
        "No test session_valid after delete",
    ),
    misconceptions=("Disable login is enough", "SSO magically revokes", "Deleted means gone from backups"),
    operate_signals="session_after_delete; offboarding checklist in 10.1.",
    build_structure="delete_user sets session_valid False.",
    break_observe="vulnerable lifecycle.py leaves session live.",
    verify_cases="after delete_user('alice') session_valid is False.",
    matrix=(
        ("alice live", "n1", "read", "allow"),
        ("alice deleted+cookie", "n1", "read", "deny"),
        ("admin", "alice", "delete", "allow-audited"),
        ("worker", "alice jobs", "run", "deny-after-delete"),
    ),
    forbidden="Deleted user's leftover session still authenticates",
    py_module="lifecycle.py",
    evidence="Account state machine and support-workflow controls",
)

add(
    "4.2",
    title="Authentication and phishing-resistant authenticators",
    system="SecureCollab",
    standards="NIST SP 800-63B-4 (final); WebAuthn Level 3 is a **W3C Candidate Recommendation** — label CR, not Rec; WCAG 2.2 for the journey; ASVS 5.0.0 V6.",
    property="A password check that ignores origin is not phishing-resistant. WebAuthn to evil.example must fail even if the secret/credential exists. Passwords to the real origin are still phishable — do not advertise them as resistant.",
    attacker="Lookalike origin; intercepted password; fatigued user.",
    trust="Lab origin binding. Real authenticators later; this fixture models origin check.",
    cell="Authenticity of the principal to *this* origin.",
    subjects="User, phishing site, real origin",
    objects="password, webauthn assertion, origin",
    actions="phishing_resistant",
    channels="browser, authenticator",
    tcb="Origin-bound authenticator ceremony.",
    untrusted="User’s ability to distinguish URLs; password reuse",
    state_time="Ceremony at login; later step-up (transfer).",
    root_cause="Shared secret replayable at the wrong origin.",
    preconditions="password method returns True for evil origin.",
    impact="Attacker obtains session at the real app (then 1.2).",
    prevention="WebAuthn origin/RP ID binding; do not call passwords resistant.",
    detection="Impossible-travel / new-device (weak); user reports.",
    recovery="Revoke sessions; force re-bind authenticators.",
    framework_not="HTML autocomplete=webauthn is not a ceremony.",
    mechanism_limit="WebAuthn does not authorize (1.2). Recovery paths can re-introduce phishable secrets (1.4, 4.1).",
    bypass="Prompt bombing; compromised authenticator; recovery email.",
    residual="Users with only passwords — honest residual, not a slogan.",
    practice="Table: method × origin × expected.",
    transfer="Step-up for export: still origin-bound?",
    transfer_product="Clinic staff SSO portal.",
    hitl=True,
    wcag="WebAuthn and password fallback must work with keyboard, labels, and no color-only errors (WCAG 2.2). A broken accessible path pushes people to shared passwords.",
    review_findings=(
        "phishing_resistant('password', evil, real) True",
        "Marketing copy “MFA = phishing resistant”",
        "Recovery SMS as default",
        "No wrong-origin WebAuthn test",
    ),
    misconceptions=("Any 2FA is phishing-resistant", "WebAuthn replaces authorization", "Usable login is a nice-to-have"),
    operate_signals="webauthn_fail_origin; recovery_used (higher risk).",
    build_structure="Only webauthn + matching origin returns True.",
    break_observe="vulnerable authn.py treats password as resistant.",
    verify_cases="password+evil False; webauthn+evil False.",
    matrix=(
        ("user", "password", "real origin", "phishable"),
        ("user", "password", "evil origin", "deny-and-not-resistant"),
        ("user", "webauthn", "evil origin", "deny"),
        ("user", "webauthn", "real origin", "resistant-authn-only"),
    ),
    forbidden="Password (or wrong-origin WebAuthn) counted as phishing-resistant",
    py_module="authn.py",
    evidence="Authenticator decision record and accessible-flow review",
)

add(
    "4.3",
    title="Sessions, cookies, and tokens",
    system="SecureCollab",
    standards="ASVS 5.0.0 V3/V7 (final); OWASP Session Management. JWT is a token format, not an architecture.",
    property="A session token in the query string is not an acceptable session. Access tokens belong in Cookie (HttpOnly, 2.3) or Authorization, never in logs and Referer.",
    attacker="Referer leak to a CDN; access-log operator; shared screenshot of a URL.",
    trust="Local request dict. Real TLS still leaks query to files and analytics.",
    cell="Authenticity/confidentiality of the session artifact.",
    subjects="Browser, logger, third-party referrer",
    objects="access_token query param, session",
    actions="session_from_request",
    channels="query, header, cookie, logs",
    tcb="Parser that ignores query tokens.",
    untrusted="URL, Referer, reverse-proxy logs",
    state_time="Link forwarded in chat months later.",
    root_cause="Token placed in a logged, shared channel.",
    preconditions="session_from_request reads access_token query.",
    impact="Session theft without XSS.",
    prevention="Reject query tokens; use cookie/header.",
    detection="Access logs containing token-shaped query keys.",
    recovery="Revoke those tokens; rotate.",
    framework_not="OAuth “implicit in URL” is obsolete; copying it is not ASVS.",
    mechanism_limit="Authorization header still logs at some gateways — redact.",
    bypass="Fragment tokens, POST body in debug dumps, 4.1 leftover sessions.",
    residual="Referer on first-party navigations — strip on outbound.",
    practice="Name three sinks of a query token.",
    transfer="Magic-link email (still a URL token — time-bound, one-time, 6.6).",
    transfer_product="Clinic appointment deep link.",
    hitl=False, wcag="",
    review_findings=(
        "session_from_request uses query",
        "JWT in localStorage as “SPA best practice” 2016 blog",
        "No Referer policy",
        "Tokens printed in uvicorn logs",
    ),
    misconceptions=("JWT is more secure than sessions", "Query strings are private over HTTPS", "Logout clears stolen tokens automatically"),
    operate_signals="query_token_rejected; log-redact gateway.",
    build_structure="query access_token => None.",
    break_observe="vulnerable token.py accepts query sessions.",
    verify_cases="query-only request yields no session.",
    matrix=(
        ("browser", "query token", "authn", "deny"),
        ("browser", "HttpOnly cookie", "authn", "allow-if-valid"),
        ("logger", "url", "store", "no-token"),
        ("cdn", "Referer", "receive", "no-token"),
    ),
    forbidden="Session established from a query-string token",
    py_module="token.py",
    evidence="Session state diagram and theft/replay tests",
)

add(
    "4.4",
    title="Authorization and tenant isolation",
    system="SecureCollab",
    standards="ASVS 5.0.0 V4 (final); Saltzer complete mediation; API1/API3/API5 as awareness after the matrix.",
    property="A share grant for note n1 is not a grant for n2. Object-level authorization (1.2) on the grant table. Login + “shared something” is ambient.",
    attacker="Member with a grant on n1 who swaps note_id; IDOR enumerator.",
    trust="Local grants dict. SQL still needs 5.5.",
    cell="Authorization (1.1/1.2).",
    subjects="bob with n1 grant, alice owner",
    objects="n1, n2, grant row",
    actions="can_read",
    channels="GET /notes/{id}",
    tcb="Lookup (subject, object) not (subject, any object).",
    untrusted="Client-supplied note_id, “I’m a collaborator” boolean",
    state_time="Grant revoked on n1 (11, 2.4) must not linger on n1 either.",
    root_cause="Collection-level “has any grant” flag.",
    preconditions="can_read(bob, n2) true because bob has n1.",
    impact="Unauthorized read of n2 body.",
    prevention="Grant keyed by note id; deny default.",
    detection="Deny logs (1.2 operate).",
    recovery="Revoke; audit bob’s reads.",
    framework_not="Depends(get_user) is not Depends(can_read_note).",
    mechanism_limit="UUID obscurity is not a grant.",
    bypass="GraphQL node(id); export zip; search index (2.2).",
    residual="Honest grant on n1 still reveals n1 — that’s the product.",
    practice="Four cells: bob×{n1,n2} × read.",
    transfer="Property-level: bob can read title but not body (7.2).",
    transfer_product="Clinic: grant on appointment A ≠ chart B.",
    hitl=False, wcag="",
    review_findings=(
        "if user.has_any_share: return note",
        "Missing n2 deny test",
        "Admin boolean bypass without tenant",
        "Search endpoint without mediation",
    ),
    misconceptions=("IDOR is a scanner finding not a missing cell", "RBAC role replaces object grants", "Signed ids are capabilities"),
    operate_signals="authz_deny{object}; grant_table_drift.",
    build_structure="can_read('bob','n2') False.",
    break_observe="vulnerable grant.py treats any grant as global.",
    verify_cases="n1 maybe true; n2 false.",
    matrix=(
        ("bob", "n1", "read", "allow-if-granted"),
        ("bob", "n2", "read", "deny"),
        ("alice", "n2", "read", "allow-owner"),
        ("anon", "n1", "read", "deny"),
    ),
    forbidden="Grant on n1 authorizes n2",
    py_module="grant.py",
    evidence="Executable authorization matrix and cross-tenant tests",
)

add(
    "4.5",
    title="OAuth, OIDC, and delegated authorization",
    system="SecureCollab",
    standards="RFC 9700 OAuth 2.0 Security BCP (final); RFC 8252 native apps (final); OIDC Core 1.0 (final); ASVS 5.0.0 V10. JWT *aud* is this lab’s cell, not “we use OAuth.”",
    property="A bearer JWT with the wrong audience must be rejected. Tokens for other-api are not sessions for securecollab-api. Delegation is not authentication theater.",
    attacker="Stolen token minted for another API; confused deputy client.",
    trust="Local aud check. Real JWKS, iss, nonce, PKCE in the full protocol — named as residual here.",
    cell="Authenticity of the audience binding.",
    subjects="client, resource server, other-api",
    objects="JWT aud, expected audience",
    actions="accept_token",
    channels="Authorization header",
    tcb="RS checks aud (and later iss, exp, signature).",
    untrusted="Client-supplied token blob",
    state_time="Long-lived tokens after client deprovision (4.1).",
    root_cause="Signature verified without audience.",
    preconditions="accept_token ignores aud.",
    impact="Other-api token spends SecureCollab API.",
    prevention="Exact aud match (or constrained list).",
    detection="Reject metric by aud.",
    recovery="Revoke client; rotate keys.",
    framework_not="Authlib defaults may verify signature only if you configure poorly.",
    mechanism_limit="Correct aud still needs 1.2 on the note.",
    bypass="Empty aud; array aud tricks; alg=none (do not teach as a payload — reject unknown alg).",
    residual="Full OAuth (PKCE, state, nonce, sender-constraining) not in this micro-fixture.",
    practice="Sequence: authz-code + PKCE vs this lab’s single aud check — name what is missing.",
    transfer="Mobile redirect (8.3, RFC 8252) and BFF vs SPA token storage.",
    transfer_product="Clinic: wrong-aud FHIR token.",
    hitl=False, wcag="",
    review_findings=(
        "verify signature, skip aud",
        "ID token used as API access token",
        "Implicit flow in SPA README",
        "No test other-api aud",
    ),
    misconceptions=("OIDC login replaces your matrix", "JWT means OAuth is done", "Mobile custom scheme is a safe redirect"),
    operate_signals="jwt_aud_mismatch; client_revoked.",
    build_structure="aud must equal expected.",
    break_observe="vulnerable jwt_aud.py accepts any aud.",
    verify_cases="wrong aud false; expected aud true.",
    matrix=(
        ("client", "aud=securecollab-api", "call API", "allow-if-valid"),
        ("client", "aud=other-api", "call API", "deny"),
        ("browser", "id_token", "call API", "deny"),
        ("mobile", "custom-scheme token", "store", "8.3 residual"),
    ),
    forbidden="JWT with wrong audience accepted as a SecureCollab session",
    py_module="jwt_aud.py",
    evidence="Protocol sequence diagrams and malicious-redirect tests",
)

add(
    "5.1",
    title="Data lifecycle and privacy engineering",
    system="SecureCollab",
    standards="NIST Privacy Framework 1.0 (final); NIST PF 1.1 IPD stays **draft** if cited; ASVS 5.0.0 V14; MASVS-PRIVACY for later mobile caches.",
    property="After account deletion, SecureCollab must not retain note bodies in an analytics copy. Retention is a 1.1 privacy/confidentiality property, not a checkbox in a DPA.",
    attacker="Insider with analytics DB; buyer of a “de-identified” export that still has bodies.",
    trust="Local NOTES vs ANALYTICS maps. Real warehouses are 7.4 workers.",
    cell="Privacy + confidentiality of bodies after the legal/product relationship ends.",
    subjects="deleted user, analytics role, remaining notes table",
    objects="body in NOTES, body in ANALYTICS",
    actions="delete_account, body_retained",
    channels="product DB, analytics copy, backups (residual)",
    tcb="Delete use-case that enumerates copies.",
    untrusted="“We don’t use analytics for authz” as a reason to skip delete",
    state_time="Delete T+0; warehouse load T+6h still has yesterday’s extract.",
    root_cause="Secondary copy not in the deletion graph.",
    preconditions="delete_account pops NOTES only.",
    impact="Bodies persist after the person left.",
    prevention="Inventory copies; delete or unlink bodies in each.",
    detection="Job that searches analytics for deleted user ids (careful with logs).",
    recovery="Purge warehouse partitions; notify if required by policy (not fake GDPR theater).",
    framework_not="Postgres DELETE is not warehouse DELETE. Next.js does not erase S3 analytics.",
    mechanism_limit="Anonymize ids but keep bodies — still a body retention fail.",
    bypass="Backups, search indexes, mobile cache (8.2), support tickets with paste.",
    residual="Legal hold copies — named exception with owner (E6).",
    practice="Draw collection → use → share → retain → delete for the body.",
    transfer="CSV export to a partner; clinic-booking card PHI.",
    transfer_product="Appointment card with notes.",
    hitl=True,
    wcag="Delete-account journey must be completable with keyboard and clear status (WCAG 3.3.x). An unreachable delete is a privacy incident (1.4).",
    review_findings=(
        "delete_account only NOTES.pop",
        "Analytics “immutable for ML” without exception record",
        "No test body_retained after delete",
        "Privacy policy PDF as the control",
    ),
    misconceptions=("Encryption makes retention OK", "Privacy equals confidentiality", "GDPR text in footer is the invariant"),
    operate_signals="deleted_user_body_hits; warehouse SLA for purge.",
    build_structure="delete_account also ANALYTICS.pop.",
    break_observe="vulnerable lifecycle.py leaves analytics body.",
    verify_cases="after delete body_retained is None.",
    matrix=(
        ("user", "NOTES body", "delete", "gone"),
        ("analyst", "ANALYTICS body", "after-delete", "gone"),
        ("backup", "body", "restore", "residual-named"),
        ("user", "delete UI", "complete", "accessible"),
    ),
    forbidden="Analytics copy still holds note body after account deletion",
    py_module="lifecycle.py",
    evidence="Data-flow inventory, retention/deletion matrix, privacy review",
)

add(
    "5.2",
    title="Cryptographic properties and safe use",
    system="SecureCollab",
    standards="ASVS 5.0.0 V11 (final); RFC 9106 Argon2 (final) for *passwords* not this field; never roll a cipher. This lab’s cell is confidentiality of a stored secret at rest — encoding is not encryption.",
    property="protect(secret) must not be reversible as Base64 of the plaintext. Encoding, hex, and “obfuscation” are not confidentiality mechanisms.",
    attacker="Operator who can read the stored field; stolen disk of the lab dict.",
    trust="Local protect()/looks_encrypted(). Real AEAD keys are 5.3.",
    cell="Confidentiality of the stored secret vs honest storage observers.",
    subjects="app, disk observer",
    objects="plaintext, stored blob",
    actions="protect",
    channels="file/db column",
    tcb="A real AEAD or KDF appropriate to the threat — lab may stub as non-b64.",
    untrusted="Base64, rot13, homegrown XOR with a constant",
    state_time="Stolen backup years later (crypto agility 5.3).",
    root_cause="Mechanism name “encrypted” applied to encoding.",
    preconditions="protect returns b64(secret).",
    impact="Any reader of the column gets the secret.",
    prevention="Use a standard AEAD with a managed key; tests forbid b64 identity.",
    detection="Scanner for b64-looking “ciphertext” of known plaintext in tests.",
    recovery="Rotate keys; re-encrypt; treat as leak.",
    framework_not="passlib/bcrypt is for passwords, not note bodies. Fernet still needs 5.3 key storage.",
    mechanism_limit="AES-GCM with a nonce reuse is not this property. Do not paste attack scripts — name the misuse.",
    bypass="Key in the same row; client-side only “encryption” with key in the bundle (8.1).",
    residual="Memory dumps; authorized operators.",
    practice="Table: property vs algorithm vs what it is *not* for.",
    transfer="Password hashing vs field encryption vs backup encryption.",
    transfer_product="Clinic: SSN column labeled “encrypted” that is b64.",
    hitl=False, wcag="",
    review_findings=(
        "protect = base64",
        "AES-ECB “because we need it deterministic”",
        "JWT as encryption",
        "No looks_encrypted test",
    ),
    misconceptions=("HTTPS means data at rest is encrypted", "Base64 is hashing", "Stronger algorithm fixes a bad key story"),
    operate_signals="known-plaintext-b64 test in CI.",
    build_structure="protect output is not b64(plaintext); looks_encrypted True.",
    break_observe="vulnerable crypto.py encodes rather than encrypts.",
    verify_cases="decode(protect(secret)) != secret.",
    matrix=(
        ("disk observer", "b64 field", "read", "must-not-be-plaintext"),
        ("app", "AEAD", "decrypt-with-key", "allow"),
        ("app", "password KDF", "note body", "wrong-tool"),
        ("backup", "blob", "steal", "5.3 key residual"),
    ),
    forbidden="Stored secret is mere encoding of plaintext",
    py_module="crypto.py",
    evidence="Crypto decision table and misuse tests",
)

add(
    "5.3",
    title="Key and secret lifecycle",
    system="SecureCollab",
    standards="ASVS 5.0.0 V11/V13 (final); OWASP secrets guidance; NIST PQC standards are for *agility planning*, not a lab quantum attack.",
    property="A disposable lab API key that is a hardcoded default must not authenticate after rotation. The old value fails. Inventory + rotation is the property, not “we have a secrets manager” as a sticker.",
    attacker="Anyone who cloned the repo or an old container image with sk-lab-hardcoded.",
    trust="Local auth(current). Real KMS later.",
    cell="Authenticity of the service credential over time.",
    subjects="old image, rotated app, attacker with git history",
    objects="sk-lab-hardcoded, rotated-now",
    actions="auth",
    channels="env, repo, image layers",
    tcb="Current secret store; deny list of retired versions.",
    untrusted="Source tree, Docker history, CI logs",
    state_time="Rotate T+0; attacker uses git from T-1.",
    root_cause="Default credential never invalidated.",
    preconditions="auth(hardcoded) True while current is rotated-now.",
    impact="Silent backdoor equal to production admin if copied.",
    prevention="Generate unique secrets; rotate; refuse known defaults; never commit.",
    detection="Secret scanning; auth failures on default strings.",
    recovery="Rotate again; rebuild images; purge logs.",
    framework_not="pydantic Settings reading .env does not rotate anything.",
    mechanism_limit="Vault without rotation policy is a new hard-to-scan dump.",
    bypass="Secondary default in a worker (7.4); mobile embedded key (8.4).",
    residual="PQC migration is a plan, not this test.",
    practice="Inventory: name, location, owner, last rotated, blast radius.",
    transfer="Envelope encryption DEK vs KEK; compromise runbook.",
    transfer_product="Clinic lab API key in a GitHub gist.",
    hitl=False, wcag="",
    review_findings=(
        "DEFAULT = 'sk-lab-hardcoded' still accepted",
        "Secret in README “for convenience”",
        "No rotation test",
        "Same key for all tenants",
    ),
    misconceptions=("gitignore means it was never leaked", "KMS equals rotated", "Passwords and API keys are the same lifecycle"),
    operate_signals="auth_default_denied; image_rebuild after rotate.",
    build_structure="auth(hardcoded, current=rotated) False.",
    break_observe="vulnerable secrets.py still honors the default.",
    verify_cases="hardcoded fails; current succeeds if you add that test.",
    matrix=(
        ("old default", "API", "auth", "deny"),
        ("rotated current", "API", "auth", "allow"),
        ("git history", "default", "checkout", "must-still-deny"),
        ("worker", "own secret", "auth", "separate"),
    ),
    forbidden="Hardcoded default API key still authenticates after rotation",
    py_module="secrets.py",
    evidence="Key hierarchy, inventory, rotation exercise, compromise runbook",
)

add(
    "5.4",
    title="Secure communication and channel binding",
    system="SecureCollab",
    standards="RFC 8446/9846 TLS 1.3 (final); ASVS 5.0.0 V12; MASVS-NETWORK for 8.x. Pinning is a trade-off, not a universal rule.",
    property="A client-supplied X-Forwarded-Proto: https does not make the channel HTTPS. Channel authenticity is what the server socket actually negotiated (or a trusted proxy you *bound*), not a header from the browser.",
    attacker="Client on cleartext who wants the app to think TLS is on (cookie Secure flags, redirects).",
    trust="Direct socket proto in the lab. Real deployments may trust a *locked* load balancer hop only.",
    cell="Authenticity of the transport.",
    subjects="client, app, maybe LB",
    objects="X-Forwarded-Proto, socket proto",
    actions="channel_is_https",
    channels="HTTP headers vs TLS",
    tcb="Socket or a *configured* trusted proxy hop.",
    untrusted="Any client header about TLS",
    state_time="Mixed content, stray http:// bookmark.",
    root_cause="Confused deputy: app believes client about the channel.",
    preconditions="Header https + socket http => True.",
    impact="Session cookies marked as if Secure; users stay on cleartext; HSTS skipped.",
    prevention="Ignore client proto unless the immediate peer is a trusted proxy with a bound identity.",
    detection="Requests where header https and socket http.",
    recovery="HSTS once you really have TLS; revoke cookies issued over cleartext.",
    framework_not="uvicorn --proxy-headers without a trusted proxy IP is this bug.",
    mechanism_limit="Correct TLS to the LB is not e2e if you needed e2e (messaging).",
    bypass="SSLStrip on networks without HSTS; spoofed Forwarded.",
    residual="Pinning mobile apps (8.x) vs operational breakage — document, don’t mandate.",
    practice="Draw hops: device — ? — LB — app. Who is allowed to assert proto?",
    transfer="mTLS service identity vs this header.",
    transfer_product="Clinic: “we’re on TLS” because the SPA uses https:// in axios baseURL while API is http internally logged as https.",
    hitl=False, wcag="",
    review_findings=(
        "channel_is_https trusts X-Forwarded-Proto from anyone",
        "--proxy-headers with *",
        "No test header vs socket mismatch",
        "HSTS on an app that still accepts http",
    ),
    misconceptions=("HTTPS URL in the client proves TLS", "Forwarded headers are for security", "Pinning is always required"),
    operate_signals="proto_mismatch; cert expiry drill (ops 10.4).",
    build_structure="header https + socket http => False.",
    break_observe="vulnerable channel.py trusts the header.",
    verify_cases="mismatch is not TLS.",
    matrix=(
        ("client", "X-Forwarded-Proto", "assert TLS", "deny"),
        ("socket TLS", "channel", "https", "allow"),
        ("trusted LB", "proto header", "assert", "allow-if-bound-peer"),
        ("mobile", "pin", "fail-closed", "trade-off"),
    ),
    forbidden="Client X-Forwarded-Proto treated as TLS",
    py_module="channel.py",
    evidence="Trust-chain diagram, TLS tests, certificate failure drill",
)

add(
    "5.5",
    title="Database and persistence security",
    system="SecureCollab",
    standards="ASVS 5.0.0 V13 (final); PostgreSQL role/RLS docs as *platform*; parameterization is complete mediation of the SQL interpreter (also 6.1).",
    property="fetch_sql must bind the tenant (and note id) as parameters, not concatenate a string the SQL interpreter will parse as code. Application 1.2 is necessary; it is not a substitute for interpreter isolation.",
    attacker="Member who types a note id with SQL metacharacters; stolen app role (3.3).",
    trust="Local query object. Real DB roles in 3.3.",
    cell="Confidentiality/integrity of rows via interpreter confusion.",
    subjects="app, postgres parser, attacker input",
    objects="SQL text vs bound params",
    actions="fetch_sql, is_bound",
    channels="SQL session",
    tcb="Bound API (psycopg parameters).",
    untrusted="note_id, sort columns, search q",
    state_time="One request; also migrations (residual).",
    root_cause="Data and program mixed in one string.",
    preconditions="fetch_sql returns a concatenated str.",
    impact="Interpreter reads other tenants / mutates rows.",
    prevention="Parameters; identifier allow-lists for ORDER BY.",
    detection="SQL error anomalies; WAF is not the property.",
    recovery="Rotate DB creds; restore if mutated.",
    framework_not="SQLAlchemy text() with f-strings is still concat. ORM defaults can still interpolate.",
    mechanism_limit="Bound ids plus missing 1.2 still leak via legitimate queries.",
    bypass="Identifier injection in ORDER BY; COPY; search DSL.",
    residual="DB superuser tools; replicas.",
    practice="Show bound vs concat for the lab payload *as data*, not as a weaponized cookbook.",
    transfer="NoSQL operators, GraphQL args (7.1).",
    transfer_product="Clinic search box.",
    hitl=False, wcag="",
    review_findings=(
        "f\"SELECT ... '{note_id}'\"",
        "ORM .filter with raw strings",
        "RLS disabled in tests “for speed” and forgotten",
        "No is_bound assertion",
    ),
    misconceptions=("ORM means no injection", "RLS replaces parameterization", "Blacklist of quotes is mediation"),
    operate_signals="sql_error_spike; grant_drift (3.3).",
    build_structure="fetch_sql returns bound structure not a concat string.",
    break_observe="vulnerable query.py concatenates.",
    verify_cases="is_bound true; concat fails the test.",
    matrix=(
        ("app", "tenant param", "query", "bound"),
        ("attacker", "id field", "as-SQL", "deny"),
        ("migrator", "ddl", "run", "offline-role"),
        ("analyst", "bodies", "SELECT", "3.3"),
    ),
    forbidden="Query built by concatenating untrusted strings into SQL",
    py_module="query.py",
    evidence="Schema threat model, role matrix, constraint tests, backup/restore",
)

# --- Phase 6 ---
add(
    "6.1",
    title="Interpreter confusion and injection",
    system="SecureCollab",
    standards="ASVS 5.0.0 V5 (final); CWE-77/78/89 as *names after* the cause; OWASP Top 10:2025 A05 as regression awareness.",
    property="A filename or list target is data, not a shell program. argv_for_list must not invoke a shell. Structural APIs (argv list, parameterized SQL in 5.5) are the mechanism; denylists of metacharacters are incomplete.",
    attacker="User who chooses a note/export name; a compromised client.",
    trust="Local argv.py. No live OS attack — the test only checks argv shape.",
    cell="Integrity of the OS interpreter boundary.",
    subjects="app, /bin/sh, user input",
    objects="argv vector, name",
    actions="argv_for_list, uses_shell",
    channels="subprocess",
    tcb="argv list without shell=True.",
    untrusted="name string",
    state_time="One export click.",
    root_cause="Concatenating untrusted data into a shell grammar.",
    preconditions="returns ['sh','-c','ls '+name].",
    impact="OS interpreter runs attacker grammar (lab asserts structure only).",
    prevention="argv list; no shell; validate allow-listed names.",
    detection="Unexpected child processes.",
    recovery="Kill; rotate host if it left the lab (it must not).",
    framework_not="subprocess defaults are easy to misuse; FastAPI has no opinion.",
    mechanism_limit="Rejecting ; | still fails on IFS and encoding (2.1).",
    bypass="Another interpreter: SQL, template, LDAP — same *shape*.",
    residual="Needed shell for a plugin — isolate that binary.",
    practice="Map data flow into each interpreter on the export path.",
    transfer="Jinja, SQL, mail headers.",
    transfer_product="Clinic export-to-CSV filename.",
    hitl=False, wcag="",
    review_findings=(
        "shell=True or sh -c concatenation",
        "Blacklist of ; as the fix",
        "No uses_shell test",
        "Comment “user is trusted internally”",
    ),
    misconceptions=("Injection is one CWE", "ORM/subprocess wrappers auto-escape shells", "Scanner finding is the invariant"),
    operate_signals="child_process_anomaly.",
    build_structure="argv is ['ls', name] or reject; uses_shell False.",
    break_observe="vulnerable argv.py uses sh -c concat.",
    verify_cases="not sh -c; uses_shell false.",
    matrix=(
        ("user", "name", "as-argv", "data"),
        ("user", "name", "as-shell", "deny"),
        ("app", "ls", "exec", "fixed-binary"),
        ("worker", "same name", "7.4", "same-cell"),
    ),
    forbidden="User-controlled name executed via a shell string",
    py_module="argv.py",
    evidence="Multi-interpreter data-flow review and exploit/fix regressions",
)

add(
    "6.2",
    title="Browser injection and active content",
    system="SecureCollab",
    standards="ASVS 5.0.0 V3 (final); CWE-79 as name; CSP3 / Trusted Types are layered and some docs are still CR — do not claim they replace encoding.",
    property="Angle brackets in a note title must be encoded in HTML context (`&lt;`) so the browser does not parse an extra element. Encoding is context-specific; CSP is not this cell.",
    attacker="Collaborator who can edit a title; stored XSS later in another tenant’s view.",
    trust="Local render(). Real DOM sinks in 2.3.",
    cell="Integrity of the HTML interpreter; confidentiality of sessions if combined with 2.3 fail.",
    subjects="renderer, browser HTML parser, peer user",
    objects="title string, HTML output",
    actions="render",
    channels="HTML body",
    tcb="Context-aware encoder for HTML text.",
    untrusted="Note title, display name",
    state_time="Stored now, viewed later by owner.",
    root_cause="HTML grammar mixed with data.",
    preconditions="render echoes <img without encoding.",
    impact="Active content in the victim origin.",
    prevention="Encode for HTML text; framework safe constructors; CSP extra.",
    detection="CSP reports (not enforcement by themselves — E2).",
    recovery="Patch content; rotate sessions if cookie not HttpOnly.",
    framework_not="React defaults help in JSX, not in dangerouslySetInnerHTML or a FastAPI HTML template.",
    mechanism_limit="HTML encoding is wrong in a JS string context.",
    bypass="DOM clobbering, prototype pollution, markdown pipeline.",
    residual="Trusted admin HTML — explicit tiny exception.",
    practice="Name the context (HTML text vs attr vs JS vs URL).",
    transfer="Markdown-to-HTML sanitizer as a second parser (2.1).",
    transfer_product="Clinic patient nickname field.",
    hitl=False, wcag="",
    review_findings=(
        "Template concatenates title",
        "CSP Report-Only as the fix",
        "No &lt; test",
        "Sanitizer after innerHTML assignment",
    ),
    misconceptions=("CSP replaces encoding", "HttpOnly makes XSS harmless", "Markdown is inert"),
    operate_signals="csp_report; stored_field_review.",
    build_structure="render encodes < to &lt; and no raw <img.",
    break_observe="vulnerable html.py echoes markup.",
    verify_cases="angle brackets encoded.",
    matrix=(
        ("peer", "title", "store", "allow-data"),
        ("browser", "title", "as-HTML", "encoded"),
        ("CSP", "script", "block", "layer-not-property"),
        ("admin", "raw HTML", "render", "non-goal-or-tiny-exception"),
    ),
    forbidden="Unencoded markup reaches the HTML interpreter",
    py_module="html.py",
    evidence="Browser exploit/fix lab plus CSP/TT rollout notes",
)

add(
    "6.3",
    title="Cross-site and cross-context attacks",
    system="SecureCollab",
    standards="ASVS 5.0.0 V3/V4 (final); Fetch Metadata / SameSite as *helpers*; cookie session (2.3) is not the CSRF property.",
    property="A state-changing share POST from a foreign origin without a matching CSRF token/origin check is denied. Ambient cookies are not consent.",
    attacker="Evil origin with the victim’s browser session cookie.",
    trust="Local allow_share(origin, expected, token).",
    cell="Integrity of share grants (3.4/1.2) against the browser’s confused-deputy.",
    subjects="victim browser, evil.example, app",
    objects="share POST, Origin, CSRF token",
    actions="allow_share",
    channels="cookie + cross-site POST",
    tcb="Server check of Origin/Fetch Metadata and/or anti-CSRF token bound to session.",
    untrusted="Cookie presence, Referer alone",
    state_time="User still logged in while visiting evil.",
    root_cause="Cookie authority used without site-bound intent.",
    preconditions="allow_share(evil, app, token=None) True.",
    impact="Unwanted share grant.",
    prevention="Reject foreign Origin; require token for cookie sessions.",
    detection="csrf_rejected metric.",
    recovery="Revoke surprise shares; notify.",
    framework_not="SameSite=Lax is not complete (GET side effects, chrome exceptions).",
    mechanism_limit="Bearer tokens in Authorization are a different deputy model.",
    bypass="subdomain XSS, open redirect (6.5), old browsers.",
    residual="User clicking “share” on a lookalike UI — 4.2 phishing.",
    practice="Matrix: origin × token × method.",
    transfer="postMessage, clickjacking, CORS * with credentials.",
    transfer_product="Clinic “share record with partner” POST.",
    hitl=True,
    wcag="CSRF errors must be readable (not color-only). Do not make the secure path harder than a cross-site GET that still mutates.",
    review_findings=(
        "Cookie auth + no Origin check",
        "GET /share?to= ",
        "CORS * with credentials",
        "Token in cookie not bound to session",
    ),
    misconceptions=("SameSite is CSRF done", "JSON APIs cannot CSRF", "CORS is CSRF defense"),
    operate_signals="foreign_origin_post_denied.",
    build_structure="evil origin + no token => False.",
    break_observe="vulnerable csrf.py allows foreign origin.",
    verify_cases="foreign POST denied.",
    matrix=(
        ("app origin", "POST share", "with token", "allow"),
        ("evil origin", "POST share", "cookie only", "deny"),
        ("evil origin", "GET share", "mutate", "deny"),
        ("bearer API", "POST", "no cookie", "different-model"),
    ),
    forbidden="Cross-origin state-changing POST authorized by cookie alone",
    py_module="csrf.py",
    evidence="Cross-origin policy matrix and attack/defense tests",
)

add(
    "6.4",
    title="Files, paths, uploads, archives, XML, deserialization",
    system="SecureCollab",
    standards="ASVS 5.0.0 V12 (final); CWE-22/434/502 as names after the path/interpreter cause.",
    property="A user-supplied path must not resolve outside the lab root. `../etc/passwd` is data that tried to become a different object. This is not a weaponized exploit lesson — we assert prefix.",
    attacker="Uploader or filename field attacker.",
    trust="Local resolve() under /tmp/sc-lab.",
    cell="Authorization of *which file object* plus integrity of the host.",
    subjects="app, filesystem, user filename",
    objects="resolved path, root",
    actions="resolve",
    channels="upload name, archive member (transfer)",
    tcb="realpath + prefix check after normalization (2.1).",
    untrusted="filename, symlink, zip slip members",
    state_time="Extract then later process.",
    root_cause="Path grammar mixed with data; no canonicalization.",
    preconditions="resolve('../etc/passwd') escapes root.",
    impact="Read/write outside the note store.",
    prevention="Join + canonicalize + prefix; random stored names; never execute uploads.",
    detection="denied_escape metric.",
    recovery="Audit filesystem; restore.",
    framework_not="Starlette UploadFile.filename is hostile.",
    mechanism_limit="Allow-list of .png still fails if the processor parses XML (XXE) — name it.",
    bypass="Absolute paths, UNC, zip slip, content-type vs magic.",
    residual="Image codecs (memory) — E4.",
    practice="Corpus: ../, encoded dots, zip members — as *test names*, not payloads to fire at strangers.",
    transfer="XML entity expansion; pickle; YAML load.",
    transfer_product="Clinic scan upload.",
    hitl=False, wcag="",
    review_findings=(
        "open(user_path)",
        "Blacklist of '..' only",
        "Trust Content-Type",
        "No prefix test",
    ),
    misconceptions=("UUID filenames replace path checks", "Antivirus is the upload control", "JSON is always safe deserialize"),
    operate_signals="path_escape_denied; malware-scan is extra.",
    build_structure="resolve either raises or stays under /tmp/sc-lab.",
    break_observe="vulnerable path.py concatenates.",
    verify_cases=".. does not escape.",
    matrix=(
        ("user", "safe name", "store", "under-root"),
        ("user", ".. path", "resolve", "deny"),
        ("zip member", "..", "extract", "deny"),
        ("processor", "upload", "exec", "deny"),
    ),
    forbidden="Resolved path escapes the lab root",
    py_module="path.py",
    evidence="Hostile-file corpus and isolated processing design",
)

add(
    "6.5",
    title="Server-side requests and protocol parsing",
    system="SecureCollab",
    standards="ASVS 5.0.0 V10 (final); API7 awareness; URL is untrusted *structure* (2.1).",
    property="The lab fetcher must not allow http://169.254.169.254/ (link-local metadata). SSRF is a trust-boundary fail: the server’s network is not the user’s to steer. HTTPS to a named lab host may be allowed.",
    attacker="User who supplies an unfurl/preview URL.",
    trust="Local allowed(url). No real cloud metadata in this VM lesson — we assert the deny.",
    cell="Confidentiality of the cloud TCB; integrity of egress.",
    subjects="app egress, user URL, metadata service",
    objects="URL, scheme, host",
    actions="allowed",
    channels="server-side HTTP",
    tcb="Allow-list of hosts/schemes after parse; no redirect to IP.",
    untrusted="URL string, redirects, DNS",
    state_time="Redirect hop after first allow.",
    root_cause="Server fetches attacker-chosen authority.",
    preconditions="allowed(link-local) True.",
    impact="In real clouds, credential theft; here, the test fails closed conceptually.",
    prevention="Allow-list; parse then pin; block link-local, loopback, metadata; no open redirects.",
    detection="egress deny logs.",
    recovery="Rotate instance role if a real system was hit — never in this course.",
    framework_not="requests.get is not an allow-list.",
    mechanism_limit="DNS rebinding after allow — pin IP or block.",
    bypass="IPv6, decimal IPs, redirect, file: scheme.",
    residual="Legitimate preview of customer URLs — dedicated egress proxy.",
    practice="Parse scheme/host; do not regex the string only.",
    transfer="Webhook delivery (7.3) is egress too.",
    transfer_product="Clinic “fetch lab result PDF from URL.”",
    hitl=False, wcag="",
    review_findings=(
        "requests.get(user_url)",
        "https-only regex still allows metadata IP",
        "Follows redirects off allow-list",
        "No 169.254 test",
    ),
    misconceptions=("HTTPS URLs cannot SSRF", "Private IP blocklists are complete", "Open redirect is just UX"),
    operate_signals="egress_denied{host}.",
    build_structure="link-local False; lab https host True.",
    break_observe="vulnerable ssrf.py allows any URL.",
    verify_cases="169.254 denied; lab host ok.",
    matrix=(
        ("user", "lab host https", "fetch", "allow"),
        ("user", "link-local", "fetch", "deny"),
        ("redirect", "to link-local", "follow", "deny"),
        ("webhook", "customer URL", "7.3", "signed+allow-list"),
    ),
    forbidden="Server-side fetch to link-local metadata is allowed",
    py_module="ssrf.py",
    evidence="Egress policy, URL validation, origin-consistency tests",
)

add(
    "6.6",
    title="Workflow, race, and exceptional-condition failures",
    system="SecureCollab",
    standards="ASVS 5.0.0 V2 (final); Top 10:2025 A10 awareness. State machines fail open or double-fire.",
    property="An invite token must be single-use. The second accept('t1') is denied. TOCTOU and retries (2.4) are the same family.",
    attacker="Two tabs; an attacker who copied the token from email logs.",
    trust="Local accept().",
    cell="Integrity of membership workflow.",
    subjects="invitee, attacker with token copy",
    objects="token t1, membership",
    actions="accept",
    channels="email link, API",
    tcb="Atomic consume of token.",
    untrusted="Email channel, retries",
    state_time="Two accepts 1ms apart.",
    root_cause="Non-atomic check-then-set; token not marked used.",
    preconditions="second accept True.",
    impact="Extra member or replay after revoke.",
    prevention="Single-use in a transaction; expire; bind to recipient.",
    detection="token_replay metric.",
    recovery="Remove extra membership; rotate token scheme.",
    framework_not="DB unique constraint helps but must be the actual consume.",
    mechanism_limit="Used flag without locking still races.",
    bypass="New token via fail-open email error.",
    residual="Email is a phishable channel (4.2).",
    practice="State: issued → consumed → dead.",
    transfer="Password reset; 2.4 share retry; 7.4 jobs.",
    transfer_product="Clinic invite-guardian token.",
    hitl=True,
    wcag="Invite errors (“link already used”) must be announced accessibly so people do not retry into a support backdoor.",
    review_findings=(
        "accept always True",
        "No unique constraint",
        "Fail-open on DB error",
        "Token in query logs (4.3)",
    ),
    misconceptions=("400 errors are fail-safe", "Email links are authenticators of the recipient", "Races are only performance"),
    operate_signals="invite_replay_denied.",
    build_structure="second accept False.",
    break_observe="vulnerable invite.py allows replay.",
    verify_cases="t1 then t1 => False.",
    matrix=(
        ("invitee", "fresh t1", "accept", "allow"),
        ("anyone", "used t1", "accept", "deny"),
        ("attacker", "stolen t1 unused", "accept", "residual-email"),
        ("system", "expired t1", "accept", "deny"),
    ),
    forbidden="Invite token accepted twice",
    py_module="invite.py",
    evidence="Concurrency tests and repaired state machine",
)

add(
    "6.7",
    title="Resource abuse, automation, and availability",
    system="SecureCollab",
    standards="ASVS 5.0.0 V1/V11 (final); API4/API6 awareness. Fairness is a security cell (availability + cost).",
    property="The fourth export in the lab window is denied. Unbounded exports exhaust budget and leak extra copies (5.1).",
    attacker="Scripted member; compromised session.",
    trust="Local allow(n).",
    cell="Availability and cost; secondary confidentiality via extra copies.",
    subjects="member, billing account",
    objects="export slot 1..4",
    actions="allow",
    channels="API loop",
    tcb="Server-side quota.",
    untrusted="UI disabled button",
    state_time="Burst of 4.",
    root_cause="No resource account.",
    preconditions="allow(4) True.",
    impact="Cost/DoS; extra CSV copies of bodies.",
    prevention="Quota + authz + maybe queue.",
    detection="export_denied_quota.",
    recovery="Disable token; bill anomaly.",
    framework_not="nginx rate limit without identity is shared-fate.",
    mechanism_limit="Per-IP limits punish NAT; need per-subject.",
    bypass="New accounts; GraphQL aliases (7.1).",
    residual="Legitimate burst — owned exception.",
    practice="Budget: CPU, bytes, paid API calls.",
    transfer="Notification fan-out; search complexity.",
    transfer_product="Clinic bulk-export patients.",
    hitl=True,
    wcag="Quota errors must be readable; do not trap keyboard users in a spinner that retries (amplifying load).",
    review_findings=(
        "No cap",
        "Limit only in frontend",
        "Global IP limit",
        "No test fourth denied",
    ),
    misconceptions=("Availability is ops not appsec", "Captcha replaces quotas", "Autoscaling is the control"),
    operate_signals="quota_denied; cost_alert.",
    build_structure="allow(4) False.",
    break_observe="vulnerable limit.py unbounded.",
    verify_cases="fourth export denied.",
    matrix=(
        ("member", "export 1-3", "run", "allow"),
        ("member", "export 4", "run", "deny"),
        ("anon", "export", "run", "deny"),
        ("worker", "export", "7.4", "service-quota"),
    ),
    forbidden="Unbounded exports (4th allowed in the lab window)",
    py_module="limit.py",
    evidence="Resource budget, rate policy, cost-abuse tests",
)

add(
    "7.1",
    title="API contracts, protocols, and inventory",
    system="SecureCollab",
    standards="ASVS 5.0.0 V13 (final); OpenAPI as inventory, not security; API8/API9 awareness.",
    property="Mass assignment: a PATCH must not set is_admin from the client document. The contract’s writable field set is an authorization property (1.2 at field grain, 7.2).",
    attacker="Authenticated member sending extra JSON keys.",
    trust="Local apply(user, patch).",
    cell="Authorization of properties.",
    subjects="member, admin flag",
    objects="display_name, is_admin",
    actions="apply",
    channels="JSON PATCH/PUT",
    tcb="Allow-listed writable fields server-side.",
    untrusted="JSON keys, GraphQL mutations, protobuf unexpected fields",
    state_time="One PATCH; also undocumented /v0 leftover (inventory).",
    root_cause="Binder maps any key onto the entity.",
    preconditions="apply(..., {is_admin: True}) succeeds.",
    impact="Privilege lift.",
    prevention="Explicit writable set; ignore/reject unknown privileged fields.",
    detection="rejected_field metric.",
    recovery="Demote; audit.",
    framework_not="Pydantic extra=allow is this bug. FastAPI will happily take extra if your model does.",
    mechanism_limit="Allow-list must track every protocol (REST, GraphQL, gRPC).",
    bypass="CSV import; admin BFF; 7.4 job payload.",
    residual="Honest display_name XSS (6.2) is another cell.",
    practice="Inventory endpoints; mark each field writable by which role.",
    transfer="GraphQL mutation arguments; gRPC unknown fields.",
    transfer_product="Clinic: PATCH patient {is_staff:true}.",
    hitl=False, wcag="",
    review_findings=(
        "user.__dict__.update(body)",
        "Undocumented route not in inventory",
        "No is_admin test",
        "OpenAPI not generated from code",
    ),
    misconceptions=("If it’s not in Swagger it cannot be called", "GraphQL is self-documenting therefore safe", "Versioning is a security control"),
    operate_signals="unknown_field_rejected; shadow_endpoint_scan.",
    build_structure="is_admin stays False.",
    break_observe="vulnerable patch.py copies is_admin.",
    verify_cases="PATCH is_admin does not stick.",
    matrix=(
        ("member", "display_name", "PATCH", "allow"),
        ("member", "is_admin", "PATCH", "deny"),
        ("admin", "is_admin", "PATCH", "allow-audited"),
        ("ghost /v0", "any", "call", "deny-or-inventory"),
    ),
    forbidden="Client PATCH sets is_admin",
    py_module="patch.py",
    evidence="Machine-readable contract, endpoint inventory, retirement plan",
)

add(
    "7.2",
    title="Object, property, and function security",
    system="SecureCollab",
    standards="ASVS 5.0.0 V4 (final); API1/3/5 awareness after 1.2/4.4.",
    property="A member must not resolve secret_internal. Function/property authorization is not “they can call GET /notes.” Identifiers locate; they do not authorize.",
    attacker="Member using GraphQL __typename or REST ?fields=.",
    trust="Local resolve(role, field).",
    cell="Authorization at property grain.",
    subjects="member vs admin",
    objects="secret_internal, title",
    actions="resolve",
    channels="field picker, GraphQL",
    tcb="Per-field policy.",
    untrusted="requested field names",
    state_time="One query.",
    root_cause="Serializer dumps the ORM object.",
    preconditions="resolve('member','secret_internal') True.",
    impact="Internal secret or PII extra.",
    prevention="Allow-list fields by role; never bind authz to the id format.",
    detection="field_denied.",
    recovery="Rotate the secret; audit.",
    framework_not="SQLAlchemy to_dict() is not a policy.",
    mechanism_limit="Hiding fields in UI only.",
    bypass="CSV export; 7.4; debug toolbar.",
    residual="Admin sees secret_internal — audited.",
    practice="Table: role × field.",
    transfer="Bulk update; search highlighting leaking snippets.",
    transfer_product="Clinic: member cannot resolve ssn.",
    hitl=False, wcag="",
    review_findings=(
        "return orm.__dict__",
        "GraphQL expose all columns",
        "IDOR test only on object not field",
        "UUID as “capability”",
    ),
    misconceptions=("Object-level authz implies field-level", "Private JSON keys are hidden", "GraphQL resolvers inherit REST policy magically"),
    operate_signals="field_denied{field}.",
    build_structure="member × secret_internal False.",
    break_observe="vulnerable field.py allows member internal.",
    verify_cases="member cannot resolve secret_internal.",
    matrix=(
        ("member", "title", "resolve", "allow"),
        ("member", "secret_internal", "resolve", "deny"),
        ("admin", "secret_internal", "resolve", "allow-audit"),
        ("anon", "title", "resolve", "deny"),
    ),
    forbidden="Member resolves secret_internal",
    py_module="field.py",
    evidence="Policy-aware serializers and mutation tests",
)

add(
    "7.3",
    title="Webhooks, callbacks, and third-party APIs",
    system="SecureCollab",
    standards="ASVS 5.0.0 V10 (final); API10 awareness. HMAC is a teaching stand-in, not “we are Stripe.”",
    property="A webhook with a missing signature is rejected. Authenticity of the *provider message* is distinct from TLS and from 1.2 on the resulting action.",
    attacker="Anyone who can POST your callback URL.",
    trust="Local accept(sig, body, secret).",
    cell="Authenticity + integrity of inbound integration.",
    subjects="forged client, real provider, app",
    objects="body, HMAC, secret",
    actions="accept",
    channels="HTTPS callback",
    tcb="Verify signature over raw body + freshness + idempotency (2.4).",
    untrusted="IP allow-lists as the only control; JSON fields",
    state_time="Replay yesterday’s valid signed body (residual if no nonce).",
    root_cause="Callback trusted because it hit the path.",
    preconditions="accept('', body, secret) True.",
    impact="Forged “share” or billing events.",
    prevention="Verify MAC; bind to secret per provider; timestamp.",
    detection="sig_fail metric.",
    recovery="Rotate webhook secret; review accepted events.",
    framework_not="Stripe SDK verify is not your custom HMAC if you reimplement poorly.",
    mechanism_limit="Correct signature still needs 1.2 on side effects.",
    bypass="Timing leak compare; parsed JSON vs raw body mismatch (2.1).",
    residual="Provider compromise — egress + least privilege on what a webhook may do.",
    practice="List: signature, raw body, time, replay, dest URL ownership.",
    transfer="Signed redirects; outbound webhook SSRF (6.5).",
    transfer_product="Clinic lab-result webhook.",
    hitl=False, wcag="",
    review_findings=(
        "if path==/webhook: process",
        "JSON parsed before MAC",
        "No missing-sig test",
        "Secret in query (4.3)",
    ),
    misconceptions=("TLS to us proves the sender", "IP allowlist is authenticity", "Webhooks are just APIs in reverse so JWT login applies"),
    operate_signals="webhook_sig_fail; replay_window.",
    build_structure="empty signature False.",
    break_observe="vulnerable hook.py accepts missing sig.",
    verify_cases="missing signature rejected.",
    matrix=(
        ("forger", "empty sig", "POST", "deny"),
        ("provider", "valid sig", "POST", "allow-verify"),
        ("replay", "old valid", "POST", "deny-if-freshness"),
        ("handler", "event", "side-effect", "still-1.2"),
    ),
    forbidden="Unsigned webhook body accepted",
    py_module="hook.py",
    evidence="Signed webhook protocol, replay tests, provider-failure runbook",
)

add(
    "7.4",
    title="Queues, workers, events, and service identity",
    system="SecureCollab",
    standards="ASVS 5.0.0 V4/V10 (final); NIST zero trust as architecture *guidance*.",
    property="A leftover user session is not worker identity. Exports must run as a service principal. Confused deputy: the queue message’s user_session must not become the worker’s ambient authority.",
    attacker="Stolen cookie posted into a job; a job that forgets to drop the user context.",
    trust="Local exporter(ctx).",
    cell="Authorization of the worker plane.",
    subjects="alice session, export-service",
    objects="export job",
    actions="exporter",
    channels="queue payload",
    tcb="Service credential distinct from user sessions.",
    untrusted="Job JSON, user ids inside jobs",
    state_time="Job delayed 6h after user deletion (4.1).",
    root_cause="Ambient user context in a system worker.",
    preconditions="exporter({user_session: alice}) succeeds.",
    impact="User cookie drives a privileged export; or stale user still exports.",
    prevention="Jobs carry (actor type=service, tenant, resource); workers authenticate as service.",
    detection="worker_used_user_session metric.",
    recovery="Revoke service creds; drain queue.",
    framework_not="Celery inherit request context is a trap.",
    mechanism_limit="Service role that is still god-mode (3.3).",
    bypass="Poison message loops; cross-tenant job fields.",
    residual="Broker ACLs — 10.3.",
    practice="Trace one export: who is the subject at HTTP vs worker.",
    transfer="Outbox pattern; event schemas.",
    transfer_product="Clinic batch-export worker.",
    hitl=False, wcag="",
    review_findings=(
        "job['session']=request.cookies",
        "Worker uses DATABASE_URL superuser",
        "No test user_session rejected",
        "Retry duplicates (2.4)",
    ),
    misconceptions=("Internal queue is trusted input", "Async means no authz", "Service account should be superuser “just for jobs”"),
    operate_signals="worker_identity_wrong; poison_queue.",
    build_structure="user_session only => None exporter.",
    break_observe="vulnerable worker.py treats user session as worker.",
    verify_cases="user_session is not worker identity.",
    matrix=(
        ("user session", "export job", "run", "deny-as-identity"),
        ("service", "export job", "run", "allow-least-priv"),
        ("deleted user", "old job", "run", "deny-4.1"),
        ("tB job", "tA worker ctx", "run", "deny"),
    ),
    forbidden="User session accepted as worker identity",
    py_module="worker.py",
    evidence="End-to-end authority trace and adversarial job tests",
)

add(
    "8.1",
    title="Hostile-client and mobile platform model",
    system="SecureCollab Android client",
    standards="MASVS 2.1 (final) PLATFORM/CODE; Android security model. APK is not in the TCB.",
    property="A client JSON field integrity=ok must not authorize a sensitive export. The server attestation result is the TCB; the APK is hostile (root, patched, emulator).",
    attacker="Modified APK; Frida; stolen “integrity ok” boolean.",
    trust="Local allow_export(client_claim, server_attest).",
    cell="Authorization — server decides.",
    subjects="hostile APK, server",
    objects="export, integrity claim",
    actions="allow_export",
    channels="JSON body",
    tcb="Server-side attestation/token — lab uses server_attest string.",
    untrusted="Any client field, local ifs.",
    state_time="Runtime after Play integrity check cached on device.",
    root_cause="Policy evaluated on the attacker’s CPU.",
    preconditions="allow_export({integrity:ok}, 'fail') True.",
    impact="Export without server authority.",
    prevention="Ignore client integrity for authorization; server attest/session 1.2.",
    detection="client_claim_ignored; attest_fail.",
    recovery="Revoke app tokens.",
    framework_not="Play Integrity is a signal, not 1.2.",
    mechanism_limit="Attestation raises cost, does not establish trust of the client binary.",
    bypass="Old app version; emulator farms.",
    residual="Honest users on rooted devices — product policy.",
    practice="Responsibility matrix: client vs server for each 1.1 cell.",
    transfer="Feature flags in the APK; premium=true.",
    transfer_product="Clinic Android: client says hipaaMode=true.",
    hitl=False, wcag="",
    review_findings=(
        "if body.integrity==ok: export",
        "No server attest test",
        "Secrets in the APK (8.4)",
        "MASVS as a sticker",
    ),
    misconceptions=("Obfuscation is authorization", "If we use Kotlin we are safe", "Store listing = device trust"),
    operate_signals="attest_fail_export_denied.",
    build_structure="client ok + server fail => False.",
    break_observe="vulnerable client.py trusts JSON integrity.",
    verify_cases="client integrity is not authorization.",
    matrix=(
        ("APK", "integrity field", "authorize", "deny"),
        ("server", "attest fail", "export", "deny"),
        ("server", "attest+user 1.2", "export", "allow"),
        ("rooted honest", "export", "policy", "residual"),
    ),
    forbidden="Client integrity claim authorizes export",
    py_module="client.py",
    evidence="Mobile threat model and client/server responsibility matrix",
)

add(
    "8.2",
    title="Local data, keys, biometrics, offline, leakage",
    system="SecureCollab Android client",
    standards="MASVS 2.1 STORAGE/CRYPTO/AUTH/PRIVACY (final); MASTG 2.0 tests.",
    property="A cached note must not be plaintext on disk. Biometric lock is not server authentication (4.2). Backups and screenshots are extra channels.",
    attacker="USB backup; lost unlocked-cache device; cloud backup of app files.",
    trust="Local save_note / plaintext_on_disk.",
    cell="Confidentiality of bodies at rest on a hostile device.",
    subjects="thief, backup service, app",
    objects="cache file",
    actions="save_note, plaintext_on_disk",
    channels="disk, backup, notifications (8.5 related)",
    tcb="Keystore-backed encryption; server remains source of truth.",
    untrusted="App private dir on a rooted device as “enough”",
    state_time="Offline cache after revoke (4.1).",
    root_cause="Bodies written as text files.",
    preconditions="plaintext_on_disk True after save.",
    impact="Stolen device yields notes.",
    prevention="Encrypt cache; expire; wipe on logout/revoke; no body in notifications.",
    detection="Device lost flow; remote wipe where the OS allows.",
    recovery="Revoke sessions; rotate.",
    framework_not="EncryptedSharedPreferences defaults are not automatic for every file you write.",
    mechanism_limit="Biometrics gate UI, not key extraction on a compromised OS.",
    bypass="Screenshots, logs, clipboard, auto backup.",
    residual="Physical + extracted keys — honest.",
    practice="Inventory every local store.",
    transfer="iOS Keychain vs Android Keystore; desktop Electron.",
    transfer_product="Clinic offline chart cache.",
    hitl=True,
    wcag="Unlock-with-biometrics fallback must remain accessible (device credential) without dumping plaintext to a debug overlay.",
    review_findings=(
        "write body to cache.txt",
        "Backup allowed for the app",
        "No wipe on logout",
        "Note in notification text",
    ),
    misconceptions=("Private app dir is encryption", "Fingerprint is MFA to the server", "Offline means no policy"),
    operate_signals="logout_wipes_cache; backup_flag.",
    build_structure="plaintext_on_disk False.",
    break_observe="vulnerable disk.py stores plaintext.",
    verify_cases="cached note not plaintext.",
    matrix=(
        ("thief", "cache file", "read", "deny-plaintext"),
        ("user", "offline read", "own notes", "allow-until-revoke"),
        ("backup", "app data", "cloud", "no-bodies-or-encrypted"),
        ("server", "revoke", "cache", "wipe"),
    ),
    forbidden="Note body cached as plaintext on disk",
    py_module="disk.py",
    evidence="Device data inventory and leakage tests",
)

add(
    "8.3",
    title="Network, deep links, WebViews, IPC",
    system="SecureCollab Android client",
    standards="MASVS 2.1 PLATFORM/NETWORK/AUTH (final); RFC 8252. Exported components are attack surface.",
    property="A deep link query as=admin must not switch the signed-in principal. The session is identity; the Intent is untrusted input.",
    attacker="Malicious app sending an Intent; crafted https link.",
    trust="Local open_link / current_user.",
    cell="Authenticity of the principal.",
    subjects="alice session, attacker app",
    objects="as query, current_user",
    actions="open_link",
    channels="Intent, App Link, custom scheme",
    tcb="Ignore identity params; use session.",
    untrusted="All extras, URLs, WebView JS bridges",
    state_time="Cold start via link.",
    root_cause="Identity taken from the link.",
    preconditions="open_link({as:admin}) sets admin.",
    impact="Local privilege / account switch.",
    prevention="Do not take identity from links; validate App Link certs; WebView allow-list.",
    detection="ignored_as_param metric.",
    recovery="Force re-login.",
    framework_not="exported=true defaults on old Android.",
    mechanism_limit="Verified App Links still pass query strings.",
    bypass="WebView javascript:; custom scheme hijack.",
    residual="User installs attacker app — OS model.",
    practice="List exported components.",
    transfer="OAuth redirect to app (4.5).",
    transfer_product="Clinic: deep link as=doctor.",
    hitl=True,
    wcag="Deep-link errors should not trap users in a broken WebView without a keyboard-accessible exit.",
    review_findings=(
        "current_user = extras['as']",
        "exported Activity without permission",
        "WebView addJavascriptInterface too wide",
        "No as= test",
    ),
    misconceptions=("https App Links are trusted input", "WebView is just Chrome so 2.3 applies unchanged", "IPC is private to our app"),
    operate_signals="deeplink_identity_ignored.",
    build_structure="as=admin leaves current_user alice.",
    break_observe="vulnerable link.py switches user.",
    verify_cases="deeplink does not switch user.",
    matrix=(
        ("attacker app", "as=admin", "identity", "deny"),
        ("alice session", "open note link", "nav", "allow-if-1.2"),
        ("WebView", "js bridge", "call", "allow-list"),
        ("custom scheme", "token", "4.5", "deny-leak"),
    ),
    forbidden="Deep link as= switches the signed-in user",
    py_module="link.py",
    evidence="Malicious-link harness and IPC review",
)

add(
    "8.4",
    title="Build, distribution, attestation, resilience",
    system="SecureCollab Android client",
    standards="MASVS 2.1 CODE/RESILIENCE (final). Resilience raises cost; it is not trust.",
    property="A debug-signed lab build must not call the production export API even if a client attest string is present. Channel + build type are part of the TCB decision on the server.",
    attacker="Leaked debug APK; student build pointed at prod.",
    trust="Local api_allowed(build, attest).",
    cell="Integrity of the release channel.",
    subjects="debug build, prod API",
    objects="export endpoint",
    actions="api_allowed",
    channels="TLS to prod",
    tcb="Server rejects debug client ids / non-prod signatures.",
    untrusted="Client attest string, obfuscation",
    state_time="CI artifact mis-tagged.",
    root_cause="Prod API trusts a client claim of attest=ok from any build.",
    preconditions="api_allowed('debug','ok') True.",
    impact="Debug keys, loggers, extra exports against prod data.",
    prevention="Separate client ids; server checks; signing keys in HSM; no prod in debug manifests.",
    detection="debug_client_to_prod.",
    recovery="Revoke debug client id; rotate.",
    framework_not="minifyEnabled is not this property.",
    mechanism_limit="R8/obfuscation does not authorize. Root detection is bypassable.",
    bypass="Repackaged release signature if keys leak (5.3).",
    residual="Attestation farms.",
    practice="Where are signing keys; who can push to the store.",
    transfer="SBOM of the APK (10.2).",
    transfer_product="Clinic: debug build against prod FHIR.",
    hitl=False, wcag="",
    review_findings=(
        "api_allowed debug+ok True",
        "Signing key in the repo",
        "Same API key in debug and release (5.3)",
        "Resilience checklist as Gate 8 evidence",
    ),
    misconceptions=("Obfuscation = security", "Play App Signing means we don’t care", "Anti-debug proves the server can trust the client"),
    operate_signals="debug_to_prod_denied.",
    build_structure="debug + attest ok => False.",
    break_observe="vulnerable build.py allows debug to prod.",
    verify_cases="debug cannot call prod export.",
    matrix=(
        ("debug APK", "prod export", "call", "deny"),
        ("release APK", "prod export", "call", "allow-if-1.2-attest"),
        ("stolen sign key", "store", "publish", "5.3 incident"),
        ("R8", "strings", "hide", "not-authz"),
    ),
    forbidden="Debug build allowed to call production export",
    py_module="build.py",
    evidence="Signed release evidence and resilience-limitations report",
)

add(
    "8.5",
    title="Mobile verification and privacy",
    system="SecureCollab Android client",
    standards="MASVS 2.1 + MASTG 2.0 (final); MASWE mapping; Mobile Top 10:2024 awareness only.",
    property="A crash report must not include the note body. Mobile privacy is a 1.1 privacy cell, not a Play Data safety form as the control.",
    attacker="Crash-platform operator; another process reading logcat.",
    trust="Local crash_report(body).",
    cell="Privacy/confidentiality of bodies in telemetry.",
    subjects="crash SDK, developer",
    objects="stack trace, note body",
    actions="crash_report",
    channels="HTTPS to vendor, logcat",
    tcb="Redaction before send.",
    untrusted="Third-party SDK, verbose logging",
    state_time="Crash at view-note.",
    root_cause="Exception message includes the body.",
    preconditions="secret in str(report).",
    impact="Bodies at a vendor; maybe public if misbucketed.",
    prevention="Do not put bodies in exceptions; SDK filters; permission minimization.",
    detection="CI grep crash fixtures; vendor DLP.",
    recovery="Purge vendor; notify if needed.",
    framework_not="Firebase Crashlytics “automatic” will ship whatever you log.",
    mechanism_limit="Play Data safety form is disclosure, not redaction.",
    bypass="Screenshots in bug reports; ANR traces.",
    residual="Vendor as processor — contract + 5.1.",
    practice="MASVS-PRIVACY traceability for this one cell.",
    transfer="Web Sentry (10.5) same cell.",
    transfer_product="Clinic crash with patient name.",
    hitl=True,
    wcag="In-app “send feedback” must not require attaching a screenshot of PHI to proceed.",
    review_findings=(
        "crash_report includes body",
        "READ_LOGS leftover",
        "Tracker SDK without review",
        "MASVS spreadsheet row without test",
    ),
    misconceptions=("Store privacy labels are controls", "Debug logs stay on device", "MASTG is a scanner"),
    operate_signals="crash_body_redacted test.",
    build_structure="secret not in report.",
    break_observe="vulnerable crash.py includes body.",
    verify_cases="crash omits note body.",
    matrix=(
        ("SDK", "body", "send", "deny"),
        ("SDK", "stack", "send", "allow"),
        ("logcat", "body", "print", "deny"),
        ("vendor", "retention", "5.1", "contract"),
    ),
    forbidden="Crash report contains the note body",
    py_module="crash.py",
    evidence="Mobile verification report and MASVS traceability",
)

add(
    "9.1",
    title="Verification requirements and traceability",
    system="SecureCollab",
    standards="ASVS 5.0.0 (final) as the web/API backbone; MASVS 2.1 for mobile; a spreadsheet row is not coverage.",
    property="A requirements row that only stores status=done without a test asserting isolation does not cover AUTHZ-1. Traceability is threat → requirement → test → result.",
    attacker="Optimistic PM; empty CI.",
    trust="Local covered(req, tests).",
    cell="Integrity of the assurance case.",
    subjects="reviewer, CI, requirement AUTHZ-1",
    objects="status cell, test that asserts isolation",
    actions="covered",
    channels="assurance matrix",
    tcb="Link to a failing-on-vulnerable test.",
    untrusted="Colour in Jira",
    state_time="Release day.",
    root_cause="Status without evidence.",
    preconditions="covered True when asserts_isolation False.",
    impact="Ship 1.2 holes with a green gate.",
    prevention="Coverage predicate requires the isolation assert.",
    detection="CI: every L2 req maps a test id.",
    recovery="Add tests; do not backfill “done.”",
    framework_not="ASVS PDF is not your matrix.",
    mechanism_limit="Level 2 tailored — say what you dropped (E6).",
    bypass="Test named test_authz that asserts 200.",
    residual="Unmapped Level 3 risks.",
    practice="One chain for AUTHZ-1.",
    transfer="MASVS STORAGE for 8.2.",
    transfer_product="Clinic: HIPAA “done” column.",
    hitl=False, wcag="",
    review_findings=(
        "status-only coverage",
        "ASVS copied wholesale",
        "No isolation assert",
        "Exceptions without expiry",
    ),
    misconceptions=("ASVS certification exists as a sticker", "Number of tests is coverage", "Green build is Gate 9"),
    operate_signals="unmapped_req_blocks_release.",
    build_structure="status-only row is not coverage.",
    break_observe="vulnerable trace.py treats status as coverage.",
    verify_cases="asserts_isolation False => not covered.",
    matrix=(
        ("AUTHZ-1", "isolation test", "cover", "allow"),
        ("AUTHZ-1", "status done", "cover", "deny"),
        ("AUTHZ-1", "HTTP 200 test", "cover", "deny"),
        ("exception", "unmapped", "ship", "E6"),
    ),
    forbidden="Status-only row counted as AUTHZ-1 coverage",
    py_module="trace.py",
    evidence="Living assurance case and traceability matrix",
)

add(
    "9.2",
    title="Secure code review",
    system="SecureCollab",
    standards="OWASP Code Review (guidance); NIST SSDF PW/RV (final). Review is complete mediation of the diff.",
    property="A diff that uses eval on user input must not be approved. LGTM without looking at interpreters/authority is not review.",
    attacker="Rushed colleague; supply-chain PR (10.2).",
    trust="Local review_ok(src).",
    cell="Integrity of the change.",
    subjects="reviewer, author",
    objects="eval(user)",
    actions="review_ok",
    channels="PR",
    tcb="Human + checklist tied to 1.1 cells.",
    untrusted="Green CI, pretty formatting",
    state_time="One PR.",
    root_cause="Visual plausibility.",
    preconditions="review_ok('x=eval(user)') True.",
    impact="Interpreter confusion shipped (6.1).",
    prevention="Reject eval-on-user; look at data flow, authz, state, config.",
    detection="review_bot as aid not oracle (9.4).",
    recovery="Revert.",
    framework_not="GitHub “rulesets” do not read eval.",
    mechanism_limit="Review misses generated code (E1).",
    bypass="eval hidden in helper; framework magic.",
    residual="Unknown unknowns — 9.3 tests.",
    practice="Review the lab vulnerable file as a PR.",
    transfer="Terraform, GitHub Actions yaml.",
    transfer_product="Clinic: eval in a report template.",
    hitl=True,
    wcag="Review UI must be keyboard accessible; otherwise people rubber-stamp from a phone.",
    review_findings=(
        "LGTM on eval(user)",
        "Reviewer only read README",
        "Framework-generated SQL ignored",
        "No authority question",
    ),
    misconceptions=("Tests mean review is optional", "Formatters catch security", "AI review replaces 9.2"),
    operate_signals="review_block_eval.",
    build_structure="eval(user) => review_ok False.",
    break_observe="vulnerable review.py approves eval.",
    verify_cases="eval on user rejected.",
    matrix=(
        ("reviewer", "eval(user)", "approve", "deny"),
        ("reviewer", "bound SQL", "approve", "maybe"),
        ("bot", "comment", "approve", "never-alone"),
        ("author", "self-merge", "prod", "deny"),
    ),
    forbidden="eval on user input approved in review",
    py_module="review.py",
    evidence="Structured review of a seeded diff",
)

add(
    "9.3",
    title="Security-focused tests",
    system="SecureCollab",
    standards="ASVS/WSTG/MASTG as catalogs of *what* to test; this lab’s cell is the shape of a security test.",
    property="A test that only asserts HTTP 200 is not a security test. Security tests name a forbidden outcome (1.1 / 4.4).",
    attacker="False confidence.",
    trust="Local is_security_test(spec).",
    cell="Integrity of evidence.",
    subjects="CI, author",
    objects="status_asserted-only test",
    actions="is_security_test",
    channels="pytest",
    tcb="Assert on deny/isolation/encoding…",
    untrusted="Coverage %",
    state_time="PR build.",
    root_cause="Happy path as assurance.",
    preconditions="is_security_test({status_asserted: True}) True.",
    impact="4.4 holes with green CI.",
    prevention="Require forbidden-outcome asserts.",
    detection="lint tests for security suite membership.",
    recovery="Add negative tests.",
    framework_not="pytest-cov 90% is not 1.2.",
    mechanism_limit="Property tests still need oracles.",
    bypass="Renaming test_security_*.",
    residual="Exploratory testing (9.5).",
    practice="Write one forbidden-outcome test name for this module’s neighbors.",
    transfer="Fuzzing without an oracle.",
    transfer_product="Clinic: test_get_patient_200.",
    hitl=False, wcag="",
    review_findings=(
        "assert r.status_code==200 only",
        "No cross-tenant test",
        "Security suite empty",
        "Chaos without authz",
    ),
    misconceptions=("Coverage is security", "Fuzzing finds all authz bugs", "Snapshot tests are isolation tests"),
    operate_signals="security_suite_missing_isolation.",
    build_structure="status-only is not a security test.",
    break_observe="vulnerable stest.py treats 200 as security.",
    verify_cases="status_asserted only => False.",
    matrix=(
        ("test", "HTTP 200", "security?", "no"),
        ("test", "bob cannot read n1", "security?", "yes"),
        ("test", "fuzz 5xx", "security?", "maybe-availability"),
        ("test", "mutation of grant", "security?", "yes"),
    ),
    forbidden="HTTP 200-only test counted as a security test",
    py_module="stest.py",
    evidence="Layered security test portfolio",
)

add(
    "9.4",
    title="Automated analysis and tool orchestration",
    system="SecureCollab",
    standards="NIST SSDF (final); OWASP SAMM; OpenSSF. Tools are signals.",
    property="A HIGH finding without a mapped SecureCollab requirement cannot pass the ship gate. Unmapped means unowned, not “probably fine.”",
    attacker="Alert fatigue; vendor dashboard theater.",
    trust="Local ship_ok(findings, map).",
    cell="Integrity of release decision.",
    subjects="CI, security champion",
    objects="HIGH F1, map {}",
    actions="ship_ok",
    channels="SAST/DAST/SCA",
    tcb="Gate: HIGH needs req id + decision.",
    untrusted="Tool default severity",
    state_time="Release candidate.",
    root_cause="Scanner output not joined to 9.1.",
    preconditions="ship_ok([HIGH], {}) True.",
    impact="Unknown HIGH in prod.",
    prevention="Block unmapped HIGH; allow mapped+accepted with E6.",
    detection="unmapped_high count.",
    recovery="Map or fix; do not suppress silently.",
    framework_not="GitHub code scanning default is not your policy.",
    mechanism_limit="False positives exist — mapping is how you record that.",
    bypass="Severity downgrade without evidence.",
    residual="Blind spots (authz logic) — 9.2/9.3.",
    practice="Triage one HIGH: reachability, map, or exception.",
    transfer="SCA CVE vs actually called function.",
    transfer_product="Clinic: 50 unmapped HIGHs.",
    hitl=True,
    wcag="Triage UI must be usable; otherwise people mass-suppress.",
    review_findings=(
        "ship_ok True on unmapped HIGH",
        "Suppressions without owner",
        "SAST as Gate 9",
        "No blind-spot note for IDOR",
    ),
    misconceptions=("Zero findings means secure", "Tool X replaces ASVS", "Reachability is optional theater"),
    operate_signals="unmapped_high_blocks.",
    build_structure="unmapped HIGH => ship_ok False.",
    break_observe="vulnerable sast.py ships anyway.",
    verify_cases="unmapped HIGH blocks.",
    matrix=(
        ("HIGH mapped+fixed", "ship", "allow"),
        ("HIGH unmapped", "ship", "deny"),
        ("HIGH accepted E6", "ship", "allow-audited"),
        ("info finding", "ship", "policy"),
    ),
    forbidden="Unmapped HIGH finding allows ship",
    py_module="sast.py",
    evidence="CI signal design, triage record, blind-spot analysis",
)

add(
    "9.5",
    title="Authorized assessment, reporting, and remediation",
    system="SecureCollab",
    standards="OWASP WSTG (final); CVSS 4.0 (final spec) as *input* not the decision; CISA KEV as exploitation context.",
    property="A finding cannot be closed without a passing retest of the same forbidden outcome. A PDF report is not remediation. Scope stays the local lab.",
    attacker="Paper-compliance; ignored variant classes.",
    trust="Local close_finding({retest}).",
    cell="Integrity of the fix loop.",
    subjects="assessor, developer, retester",
    objects="finding, retest field",
    actions="close_finding",
    channels="tracker",
    tcb="Retest artifact linked.",
    untrusted="“we deployed Friday”",
    state_time="After supposed fix.",
    root_cause="Closure on intent.",
    preconditions="close_finding({retest: None}) True.",
    impact="Vulnerable still there; false residual.",
    prevention="Require retest of the same cell.",
    detection="closed_without_retest metric.",
    recovery="Reopen.",
    framework_not="Jira Done is not retest.",
    mechanism_limit="CVSS 9.8 vs business priority — you still judge.",
    bypass="Retest different endpoint.",
    residual="Unknown variants — hunt (same root cause).",
    practice="Write a three-line report: cause, impact, retest cmd.",
    transfer="KEV vs internal-only.",
    transfer_product="Clinic pentest PDF shelf.",
    hitl=True,
    wcag="Reports used by engineers must be readable (structure, not color-only severity).",
    review_findings=(
        "close without retest",
        "CVSS as the only priority",
        "Live-target language",
        "No variant search",
    ),
    misconceptions=("Pentest replaces SSDLC", "Critical CVSS must be first always", "Retest is the same as the original exploit blog"),
    operate_signals="finding_closed_without_retest denied.",
    build_structure="retest None => cannot close.",
    break_observe="vulnerable pentest.py closes anyway.",
    verify_cases="no retest => False.",
    matrix=(
        ("finding", "retest pass", "close", "allow"),
        ("finding", "retest missing", "close", "deny"),
        ("finding", "PDF attached", "close", "deny"),
        ("variant", "same cause", "open", "allow"),
    ),
    forbidden="Finding closed without retest",
    py_module="pentest.py",
    evidence="Assessment report, remediation/variant plan, retest record",
)

add(
    "10.1",
    title="Secure software lifecycle and security culture",
    system="SecureCollab team",
    standards="NIST SSDF 1.1 SP 800-218 (final); OWASP SAMM; CISA Secure by Design.",
    property="A SecureCollab PR cannot merge without a threat-model identifier for the changed surface. Culture is the merge gate, not a poster.",
    attacker="Schedule pressure.",
    trust="Local merge_ok({}).",
    cell="Integrity of process evidence.",
    subjects="author, reviewer",
    objects="PR, tm-id",
    actions="merge_ok",
    channels="GitHub",
    tcb="Required field + human 9.2.",
    untrusted="“tiny change” label",
    state_time="Every merge.",
    root_cause="Security as a later phase.",
    preconditions="merge_ok({}) True.",
    impact="Surfaces without 3.2.",
    prevention="Require tm id; triggers on identity, data, mobile…",
    detection="merge_blocked_no_tm.",
    recovery="Open TM, then merge.",
    framework_not="CODEOWNERS is not a threat model.",
    mechanism_limit="A stale tm-id rubber stamp — 3.2 age.",
    bypass="Hotfix path without after-the-fact TM (must still record).",
    residual="Metrics vanity — count TMs with tests, not posters.",
    practice="Write the merge checklist line.",
    transfer="Exception path (E6).",
    transfer_product="Clinic: “HIPAA training complete” as merge.",
    hitl=True,
    wcag="Merge and checklist UIs must be accessible to the actual reviewers you have.",
    review_findings=(
        "merge_ok True without tm",
        "Security champion optional forever",
        "Vanity vuln-count KPI",
        "No change-trigger matrix",
    ),
    misconceptions=("SAMM score is product security", "Culture cannot be tested", "SSDLC is a waterfall gate at the end"),
    operate_signals="merge_without_tm denied.",
    build_structure="{} => merge_ok False.",
    break_observe="vulnerable sdl.py merges without TM.",
    verify_cases="missing tm-id cannot merge.",
    matrix=(
        ("PR", "tm-id+tests", "merge", "allow"),
        ("PR", "no tm", "merge", "deny"),
        ("hotfix", "no tm", "merge", "deny-or-timeboxed-E6"),
        ("poster", "wall", "merge", "irrelevant"),
    ),
    forbidden="Merge without a threat-model identifier",
    py_module="sdl.py",
    evidence="Lightweight SSDLC, change-trigger matrix, improvement plan",
)

add(
    "10.2",
    title="Source control, CI/CD, and software supply chain",
    system="SecureCollab",
    standards="SLSA 1.2; OpenSSF OSPS; CISA 2026 SBOM minimum elements; NIST 800-161r1. Pin versions.",
    property="A dependency whose digest does not match the lockfile must not install. Integrity of build inputs is the cell — not “we have Dependabot.”",
    attacker="Typosquat; compromised maintainer; poisoned PR from a fork.",
    trust="Local install_ok(got, expected).",
    cell="Integrity of the artifact you will run.",
    subjects="CI, package registry",
    objects="wheel hash, lockfile",
    actions="install_ok",
    channels="pip/npm/gradle",
    tcb="Lockfile + verify digest; isolated runners; signed provenance later.",
    untrusted="Postinstall scripts, mutable latest tags",
    state_time="Install at 03:00.",
    root_cause="Name-only install.",
    preconditions="install_ok('aaa','bbb') True.",
    impact="Malicious code in the TCB.",
    prevention="Hash pin; deny scripts; provenance.",
    detection="mismatch fail the job.",
    recovery="Pin known-good; rotate secrets in CI (5.3).",
    framework_not="npm audit is 9.4 signal, not this cell.",
    mechanism_limit="Pinning a malicious 1.2.3 still installs malware — review + provenance.",
    bypass="Git dependency to a moving branch; compromised runner.",
    residual="Build cache poisoning.",
    practice="Name lockfiles and who can change them.",
    transfer="GitHub Actions third-party action@v1.",
    transfer_product="Clinic: npm install in prod pod.",
    hitl=False, wcag="",
    review_findings=(
        "install_ok True on hash mismatch",
        "Unpinned action",
        "Secrets in PR from forks",
        "SBOM generated but never used",
    ),
    misconceptions=("Lockfile without verify is integrity", "Private npm is safe", "SLSA badge is the app’s 1.2"),
    operate_signals="hash_mismatch_denied.",
    build_structure="aaa vs bbb => False.",
    break_observe="vulnerable lock.py ignores digest.",
    verify_cases="mismatch refuses install.",
    matrix=(
        ("CI", "matching digest", "install", "allow"),
        ("CI", "mismatch", "install", "deny"),
        ("fork PR", "secrets", "read", "deny"),
        ("release", "provenance", "sign", "allow"),
    ),
    forbidden="Dependency installed when digest mismatches lockfile",
    py_module="lock.py",
    evidence="Hardened pipeline, SBOM, provenance, simulated compromise exercise",
)

add(
    "10.3",
    title="Cloud, containers, Kubernetes, and IaC",
    system="SecureCollab lab cluster",
    standards="NIST SP 800-190; Kubernetes security guidance; ASVS V13/V15. K8s is optional in prod, required as a *model* here.",
    property="A pod requesting cluster-admin must be denied. Workload identity is least privilege (3.3 at cluster grain), not “our namespace is private.”",
    attacker="Compromised app container; malicious helm chart.",
    trust="Local pod_ok(role).",
    cell="Authorization of the control plane.",
    subjects="app pod, cluster-admin",
    objects="API server",
    actions="pod_ok",
    channels="RBAC, IRSA, metadata (6.5)",
    tcb="Admission policy.",
    untrusted="Dockerfile USER root; hostNetwork",
    state_time="Deploy.",
    root_cause="God-mode for convenience.",
    preconditions="pod_ok('cluster-admin') True.",
    impact="Cluster takeover from one app bug.",
    prevention="Deny cluster-admin to app; PSP/PSS; no instance metadata from app net (6.5).",
    detection="admission_denied.",
    recovery="Rotate cluster creds.",
    framework_not="EKS default service account often too wide.",
    mechanism_limit="NetworkPolicy is not RBAC.",
    bypass="node IAM via metadata.",
    residual="Break-glass admin with E6.",
    practice="Shared-responsibility sketch: you vs cloud vs K8s.",
    transfer="Serverless IAM *.",
    transfer_product="Clinic: app SA is cluster-admin.",
    hitl=False, wcag="",
    review_findings=(
        "cluster-admin on app SA",
        "Privileged: true",
        "No admission test",
        "IaC with 0.0.0.0/0",
    ),
    misconceptions=("Namespace equals tenant", "Managed K8s is secure by default", "Containers are VMs"),
    operate_signals="cluster_admin_denied.",
    build_structure="cluster-admin pod_ok False.",
    break_observe="vulnerable iam.py allows cluster-admin.",
    verify_cases="cluster-admin denied.",
    matrix=(
        ("app SA", "namespace role", "run", "allow-least"),
        ("app SA", "cluster-admin", "run", "deny"),
        ("node", "metadata", "from-pod", "deny-or-hop"),
        ("break-glass", "admin", "use", "E6"),
    ),
    forbidden="App pod granted cluster-admin",
    py_module="iam.py",
    evidence="Threat-modeled deploy and IaC/container policy tests",
)

add(
    "10.4",
    title="Deployment and configuration hardening",
    system="SecureCollab",
    standards="ASVS 5.0.0 V14 (final); CISA Secure by Default. Debug in prod is a config property.",
    property="A production boot with debug=True must fail. Debug endpoints, extra headers, and verbose errors are forbidden outcomes in prod, not “just for five minutes.”",
    attacker="Anyone who finds /debug; error pages with traces.",
    trust="Local boot_ok('prod', True).",
    cell="Least privilege of the running config + confidentiality of traces.",
    subjects="prod process, attacker",
    objects="debug flag",
    actions="boot_ok",
    channels="env, feature flags",
    tcb="Fail closed on prod+debug.",
    untrusted="Default FastAPI debug, leftover env from staging",
    state_time="Boot; hot flag.",
    root_cause="Fail-open defaults.",
    preconditions="boot_ok('prod', True) True.",
    impact="Stack traces, interactive debugger, secret leak.",
    prevention="Refuse boot; config review; no debug routes registered.",
    detection="prod_debug_boot denied metric; drift.",
    recovery="Kill; rotate secrets that appeared in traces.",
    framework_not="Next.js NODE_ENV=development in prod compose files.",
    mechanism_limit="debug=False still has other flags (feature, migration).",
    bypass="Sidecar debug container.",
    residual="Emergency debug with E6 timebox.",
    practice="Production-readiness list: flags, admin, migrations, rollback.",
    transfer="Feature flag that disables authz.",
    transfer_product="Clinic: Django DEBUG=True.",
    hitl=False, wcag="",
    review_findings=(
        "boot_ok prod debug True",
        "Admin on 0.0.0.0",
        "Migration fail-open",
        "No rollback drill",
    ),
    misconceptions=("IaC means hardened", "Canary equals secure config", "Feature flags are not TCB"),
    operate_signals="prod_debug_forbidden.",
    build_structure="prod+debug => False.",
    break_observe="vulnerable cfg.py boots anyway.",
    verify_cases="prod debug must not boot.",
    matrix=(
        ("prod", "debug True", "boot", "deny"),
        ("prod", "debug False", "boot", "allow-if-else-ok"),
        ("dev", "debug True", "boot", "allow-local"),
        ("flag", "skip_authz", "on", "deny"),
    ),
    forbidden="Production process boots with debug enabled",
    py_module="cfg.py",
    evidence="Production-readiness review, hardened baseline, rollback drill",
)

add(
    "10.5",
    title="Logging, detection, incident response, recovery, maintenance",
    system="SecureCollab",
    standards="ASVS 5.0.0 V7 (final); NIST CSF 2.0 DE/RS/RC (final); CISA KEV as input.",
    property="An incident cannot be closed with recovery=todo. Detect without recover is theater. Logs must not become a second body store (3.1/5.1).",
    attacker="Real incident; optimistic closer.",
    trust="Local close_incident({recovery, logs}).",
    cell="Resilience — recover is part of the 1.1 cell when prevention failed.",
    subjects="IR lead, engineer",
    objects="incident ticket",
    actions="close_incident",
    channels="tracker, backups",
    tcb="Checklist: contain, revoke, retest, recover, learn.",
    untrusted="“logs=ok” as enough",
    state_time="After contain.",
    root_cause="Close on detection quality.",
    preconditions="close_incident({recovery:'todo', logs:'ok'}) True.",
    impact="System still broken or attacker still in.",
    prevention="Require recovery evidence (restore test, revoke list).",
    detection="closed_without_recovery.",
    recovery="This *is* the step — restore drill.",
    framework_not="PagerDuty is not recovery.",
    mechanism_limit="Observability pipeline as exfil (3.1).",
    bypass="Mark recovery N/A without E6.",
    residual="Some incidents never get perfect forensic certainty — say so.",
    practice="Tabletop: stolen session (4.3) — detect, revoke, recover.",
    transfer="Ransomware restore vs note-level integrity.",
    transfer_product="Clinic: close ticket when SIEM is green.",
    hitl=True,
    wcag="IR runbooks and status pages must be usable under stress (keyboard, language, not color-only severity).",
    review_findings=(
        "close with recovery todo",
        "Note bodies in logs",
        "No restore evidence",
        "Support tool is god-mode (3.3)",
    ),
    misconceptions=("MTTD is the goal", "Backups untested are recovery", "Disclosure is legal-only"),
    operate_signals="incident_closed_without_recovery denied.",
    build_structure="recovery todo => False.",
    break_observe="vulnerable ir.py closes anyway.",
    verify_cases="cannot close without recovery.",
    matrix=(
        ("incident", "restore+revoke", "close", "allow"),
        ("incident", "recovery todo", "close", "deny"),
        ("logs", "bodies", "store", "deny-3.1"),
        ("EOL", "unpatched", "run", "deny-or-E6"),
    ),
    forbidden="Incident closed without recovery evidence",
    py_module="ir.py",
    evidence="Detection rules, playbook, tabletop, restore evidence, maintenance policy",
)

add(
    "11",
    title="Capstone: SecureCollab integration",
    system="SecureCollab",
    standards="All prior pinned standards as applicable; no new “capstone-only” standard. Gates 0–10 stay not-attempted without learner evidence.",
    property="After a share is revoked, tenant B must not read tenant A’s note. The capstone stitches 1.2 mediation over time (2.4, 4.1, 4.4) — not a new slogan YAML.",
    attacker="Former collaborator with a cached id; delayed worker (7.4).",
    trust="Local share map.",
    cell="Authorization over time — the course thesis in one fixture.",
    subjects="A owner, B member after revoke",
    objects="n1 share",
    actions="revoke, read",
    channels="API, cache (2.2), mobile (8.2)",
    tcb="Grant table as source of truth on every read.",
    untrusted="CDN cache of n1, offline cache, email copy",
    state_time="Revoke then read.",
    root_cause="Grant not consulted after revoke.",
    preconditions="read after revoke still body.",
    impact="Ex-collaborator confidentiality fail.",
    prevention="Complete mediation on read; invalidate caches; wipe mobile.",
    detection="read_after_revoke.",
    recovery="Notify A; rotate links.",
    framework_not="A green capstone scanner is not the 13 artifacts.",
    mechanism_limit="Email already received the body — residual 5.1.",
    bypass="Export from B before revoke still on B’s disk.",
    residual="Honest copies already made — policy + detect.",
    practice="Map this cell to 1.2, 2.2, 2.4, 4.4, 7.4, 8.2.",
    transfer="Clinic: revoke a guardian.",
    transfer_product="Full SecureCollab slice.",
    hitl=True,
    wcag="Revoke UX must be completable (1.4) or people will not revoke.",
    review_findings=(
        "read after revoke succeeds",
        "Capstone README: scanner green = done",
        "No cache invalidation",
        "Gate 11 claimed without artifacts",
    ),
    misconceptions=("Capstone is a new product", "Milestones M0–M5 complete because lessons exist", "Integration tests replace the 13 artifacts"),
    operate_signals="revoked_share_read_denied.",
    build_structure="revoke then read is None.",
    break_observe="vulnerable capstone.py still reads.",
    verify_cases="revoked share cannot read.",
    matrix=(
        ("B", "n1 before revoke", "read", "allow-if-granted"),
        ("B", "n1 after revoke", "read", "deny"),
        ("cache", "n1", "serve B", "deny"),
        ("worker", "old job", "export B", "deny"),
    ),
    forbidden="Revoked share still reads the note",
    py_module="capstone.py",
    evidence="Capstone artifact set in blueprint §11 — not produced by this rewrite",
)

add(
    "E1",
    title="AI, LLM, and agentic application security",
    system="SecureCollab optional summarizer agent",
    standards="OWASP GenAI LLM Top 10 2026 (awareness, not syllabus); NIST AI RMF GenAI Profile (guidance); this lab’s cell is tool authority.",
    property="The lab agent may only invoke allowlisted tools. A model-proposed exec_sql is not authorization. The model is an untrusted client (8.1) that speaks English.",
    attacker="Prompt injection in a note body; malicious retrieved doc.",
    trust="Local run_tool(name).",
    cell="Authorization of tools — complete mediation for the agent.",
    subjects="model, user, tool exec_sql",
    objects="tool name",
    actions="run_tool",
    channels="prompt, tool router",
    tcb="Allow-list in code, not in the prompt text.",
    untrusted="System prompt, retrieved notes, model output",
    state_time="One agent turn.",
    root_cause="Model output treated as policy.",
    preconditions="run_tool('exec_sql') executes.",
    impact="Interpreter 6.1 via English.",
    prevention="Allow-list; no exec_sql; human approval for high impact.",
    detection="denied_tool.",
    recovery="Revoke agent creds (7.4).",
    framework_not="LangChain default tools are not your matrix.",
    mechanism_limit="Prompt “never call exec_sql” is not mediation.",
    bypass="Indirect injection via 5.1 analytics copy.",
    residual="Hallucinated packages (10.2) in copilot use.",
    practice="List tools and who may call them.",
    transfer="Copilot in CI.",
    transfer_product="Clinic summarizer over charts.",
    hitl=True,
    wcag="Human approval UI for tools must be accessible; otherwise operators auto-approve.",
    review_findings=(
        "exec_sql available",
        "Policy only in the system prompt",
        "No denied-tool test",
        "Retrieved docs trusted",
    ),
    misconceptions=("LLM Top 10 is ASVS for AI", "RAG is safe because it is “our data”", "The model is in the TCB"),
    operate_signals="tool_denied{exec_sql}.",
    build_structure="exec_sql => None.",
    break_observe="vulnerable tools.py allows exec_sql.",
    verify_cases="exec_sql denied.",
    matrix=(
        ("agent", "summarize", "run", "allow"),
        ("agent", "exec_sql", "run", "deny"),
        ("note body", "prompt", "steer", "untrusted"),
        ("human", "high-impact tool", "approve", "HITL"),
    ),
    forbidden="Agent executes exec_sql because the model asked",
    py_module="tools.py",
    evidence="AI-feature threat model and adversarial evaluation notes",
)

add(
    "E2",
    title="Advanced browser and edge security",
    system="SecureCollab edge/browser",
    standards="W3C CSP3 (CR — label draft/CR); Fetch Metadata; this lab’s cell is enforcement vs report-only.",
    property="Content-Security-Policy-Report-Only is not enforcement. Isolation is not “we set a header.”",
    attacker="XSS that would be blocked only if CSP were enforcing.",
    trust="Local isolation_enforced(headers).",
    cell="Integrity of the browser policy mechanism (2.3 layered with 6.2).",
    subjects="browser, app",
    objects="CSP header",
    actions="isolation_enforced",
    channels="HTTP headers",
    tcb="Enforcing CSP (and others) actually parsed as enforcing.",
    untrusted="Report-Only, comments in HTML",
    state_time="Rollout.",
    root_cause="Report-Only mistaken for on.",
    preconditions="Report-Only header => enforced True.",
    impact="XSS still runs; dashboard looks green.",
    prevention="Detect enforcing header; don’t claim isolation otherwise.",
    detection="csp_mode metric.",
    recovery="Flip to enforcing after fix 6.2.",
    framework_not="Helmet defaults may be report-only in some templates.",
    mechanism_limit="CSP does not replace encoding (6.2) or CSRF (6.3).",
    bypass="JSONP, trusted-types not deployed, edge cache stripping headers (2.2).",
    residual="XS-Leaks — named as elective depth.",
    practice="Classify each header as enforce vs signal.",
    transfer="Trusted Types, COOP/COEP.",
    transfer_product="Clinic: Report-Only as “HIPAA header.”",
    hitl=False, wcag="",
    review_findings=(
        "Report-Only counted as enforced",
        "CSP with unsafe-inline claimed strict",
        "Edge cache serves old headers",
        "No isolation_enforced test",
    ),
    misconceptions=("More headers is more security", "Report-Only is a safer enforcing mode", "CDN WAF is CSP"),
    operate_signals="csp_reportonly_not_enforced.",
    build_structure="Report-Only => False.",
    break_observe="vulnerable csp.py treats Report-Only as enforcement.",
    verify_cases="report-only is not enforcement.",
    matrix=(
        ("CSP enforce", "script", "block", "maybe"),
        ("CSP Report-Only", "script", "block", "no"),
        ("encoding 6.2", "title", "safe", "still-required"),
        ("cache 2.2", "header", "strip", "deny"),
    ),
    forbidden="Report-Only CSP counted as isolation enforcement",
    py_module="csp.py",
    evidence="Advanced edge/browser assessment notes",
)

add(
    "E3",
    title="Payments and other high-assurance systems",
    system="SecureCollab simulated ledger (no real money or PAN)",
    standards="ASVS L3 as *selection*; PCI DSS 4.0.1 as sector awareness — this lab does not claim PCI scope. Idempotency is 2.4 at money grain.",
    property="A capture with the same idempotency key must not double-charge the lab ledger. High-assurance is a 2.4/7.x property, not PCI theater. No real PAN/PII.",
    attacker="Retry after 504; client double-click.",
    trust="Local capture(key); synthetic amounts.",
    cell="Integrity of money-like state.",
    subjects="payer, ledger",
    objects="capture key k1",
    actions="capture, charge_count",
    channels="payment API stand-in",
    tcb="Idempotent capture store.",
    untrusted="Client retries, webhook duplicates (7.3)",
    state_time="Two captures.",
    root_cause="Non-idempotent side effect (2.4).",
    preconditions="two capture(k1) => count 2.",
    impact="Double charge (simulated).",
    prevention="Idempotency key as primary key of capture.",
    detection="charge_count vs unique keys.",
    recovery="Credit the extra (runbook); still fail the test first.",
    framework_not="Stripe idempotency is not your local ledger unless you use it.",
    mechanism_limit="PCI SAQ is not this cell.",
    bypass="New key each retry (client).",
    residual="Webhook vs capture race (7.3+2.4).",
    practice="Map 2.4, 7.3, 5.1 (no PAN stored).",
    transfer="Health record append-only audit.",
    transfer_product="Simulated copay.",
    hitl=True,
    wcag="Payment confirmations must be accessible; trapped users retry (this bug).",
    review_findings=(
        "double capture increments twice",
        "PAN in logs",
        "PCI checkbox as the test",
        "No idempotency key",
    ),
    misconceptions=("PCI means the app is safe", "We don’t store cards so no money bugs", "Webhooks are eventually consistent so double charge is OK"),
    operate_signals="duplicate_capture_denied.",
    build_structure="two capture(k1) => count 1.",
    break_observe="vulnerable pay.py double-charges.",
    verify_cases="duplicate capture does not double charge.",
    matrix=(
        ("payer", "k1 first", "capture", "allow"),
        ("payer", "k1 retry", "capture", "no-second-charge"),
        ("webhook", "k1", "capture", "same"),
        ("logs", "PAN", "store", "deny"),
    ),
    forbidden="Duplicate capture double-charges the lab ledger",
    py_module="pay.py",
    evidence="Scoped high-assurance profile (synthetic)",
)

add(
    "E4",
    title="Memory safety and native-code boundaries",
    system="SecureCollab native helper (lab buffer)",
    standards="CISA memory-safe roadmap (guidance); CWE Top 25 awareness. This models a length mismatch — it is not a weaponized native exploit.",
    property="A copy into a 4-byte lab buffer must not return more than 4 bytes. Length is complete mediation of the buffer object.",
    attacker="Hostile filename/size field; FFI caller.",
    trust="Local copy_into(dst_len, src, n).",
    cell="Integrity of memory object bounds.",
    subjects="Python stand-in for a C helper",
    objects="4-byte buffer",
    actions="copy_into",
    channels="FFI",
    tcb="min(n, dst_len) copy.",
    untrusted="n, src length",
    state_time="One copy.",
    root_cause="Trusting n over dst.",
    preconditions="copy 8 bytes into 4-byte dest returns 8.",
    impact="In real C, memory corruption; here, the test catches length.",
    prevention="Bound the copy; prefer memory-safe languages for new code.",
    detection="ASAN in real native (named, not run as a weapon).",
    recovery="Patch; do not ship the overflowed binary.",
    framework_not="Python slice is the *fixed* model; C will not do this for you.",
    mechanism_limit="Safe language still has FFI (this module).",
    bypass="Integer wrap on n (name it).",
    residual="Existing C codecs for images (6.4).",
    practice="Where does SecureCollab still need native code?",
    transfer="Image parser; protobuf C.",
    transfer_product="Clinic DICOM parser.",
    hitl=False, wcag="",
    review_findings=(
        "copy returns full src",
        "No dest length check",
        "unsafe FFI in Kotlin",
        "“Python so we are memory safe” with a C wheel",
    ),
    misconceptions=("Memory safety is only C", "Fuzzing without ASAN is enough", "This lab is an exploit tutorial"),
    operate_signals="overlong_copy_denied.",
    build_structure="len(out) <= 4.",
    break_observe="vulnerable copy.py returns too many bytes.",
    verify_cases="copy does not exceed buffer.",
    matrix=(
        ("caller", "n=4 dst=4", "copy", "allow"),
        ("caller", "n=8 dst=4", "copy", "clamp-or-deny"),
        ("ASAN", "real C", "ci", "named-tool"),
        ("lesson", "PoC", "weaponize", "forbid"),
    ),
    forbidden="Copy returns more bytes than the destination length",
    py_module="copy.py",
    evidence="Memory-safety roadmap or hardened native component notes",
)

add(
    "E5",
    title="Large-scale authorization and multi-tenant SaaS",
    system="SecureCollab at SaaS scale",
    standards="ASVS V4 plus row security as *extra*; ReBAC/Zanzibar as patterns. RLS is not a substitute for 1.2.",
    property="A request body tenant:B must not switch the bound tenant A. Tenant is taken from the session/binding, not from the JSON body (1.3 confused deputy).",
    attacker="Member of A sending tenant B in GraphQL/JSON.",
    trust="Local tenant_for(session, body).",
    cell="Authorization of the tenant context.",
    subjects="session A, body B",
    objects="tenant id",
    actions="tenant_for",
    channels="JSON, header, subdomain",
    tcb="Bound tenant from session/host.",
    untrusted="body.tenant, X-Tenant",
    state_time="One request; also analytics warehouse (5.1, 3.3).",
    root_cause="Client-chosen tenant.",
    preconditions="tenant_for({A},{B}) == B.",
    impact="Cross-tenant read/write at scale.",
    prevention="Ignore body tenant; bind from session; RLS extra.",
    detection="body_tenant_ignored mismatch logs.",
    recovery="Audit B’s data for A’s actions.",
    framework_not="Postgres RLS with a SET tenant from the body is this bug.",
    mechanism_limit="Search indexes, caches (2.2), data lakes — every copy.",
    bypass="Support impersonation without audit (E6).",
    residual="Honest super-admin — E6 + 3.3.",
    practice="List every place tenant is read from.",
    transfer="Zanzibar tuple vs this binding.",
    transfer_product="Clinic group practice switching org_id in JSON.",
    hitl=False, wcag="",
    review_findings=(
        "tenant from body",
        "RLS session var from JSON",
        "Cache key without tenant (2.2)",
        "Support impersonation silent",
    ),
    misconceptions=("RLS replaces app mediation", "Subdomain is unforgeable tenant", "Scale means we switch to IAM instead of 1.2"),
    operate_signals="body_tenant_mismatch.",
    build_structure="session A + body B => A.",
    break_observe="vulnerable rls.py trusts body.",
    verify_cases="body cannot switch tenant.",
    matrix=(
        ("session A", "body B", "tenant", "A"),
        ("session A", "no body", "tenant", "A"),
        ("RLS", "SET from body", "run", "deny"),
        ("lake", "export", "tenant", "bind"),
    ),
    forbidden="JSON body switches the bound tenant",
    py_module="rls.py",
    evidence="Formal authorization model notes and scale tests",
)

add(
    "E6",
    title="Product security leadership",
    system="SecureCollab product org",
    standards="OWASP SAMM; NIST CSF 2.0; SSDF; CISA Secure by Design. Leadership is accountable residual, not a slide.",
    property="A risk exception cannot be accepted without an owner, a review date, and an accessibility check flag. “We’ll accept it” is not a record.",
    attacker="Calendar; silent exceptions.",
    trust="Local accept_exception({owner, review_by}).",
    cell="Accountability of residual risk (1.1 + 1.4).",
    subjects="VP eng, security, users who need a11y",
    objects="exception record",
    actions="accept_exception",
    channels="risk register",
    tcb="Required fields + expiry.",
    untrusted="Slide deck, chat thumbs-up",
    state_time="Until review_by.",
    root_cause="Oral acceptance.",
    preconditions="accept_exception({owner:'', review_by:None}) True.",
    impact="Unowned holes; inaccessible recovery (1.4) forever.",
    prevention="Schema of an exception; refuse incomplete.",
    detection="exception_missing_owner.",
    recovery="Expire; fix or re-accept with fields.",
    framework_not="Jira “risk” issue type without dates.",
    mechanism_limit="A perfect register that nobody reads.",
    bypass="Rename to “tech debt.”",
    residual="Some risk always remains — that’s the point of an honest register.",
    practice="Write one exception that would pass the lab.",
    transfer="Procurement questionnaire vs this record.",
    transfer_product="Clinic: “HIPAA exception.”",
    hitl=True,
    wcag="The exception must record whether the residual includes an inaccessible control (1.4). Leadership owns that users cannot complete recovery.",
    review_findings=(
        "accept with empty owner",
        "No review_by",
        "a11y not in the schema",
        "SAMM slide as the exception",
    ),
    misconceptions=("Leadership is soft skills not invariants", "Exceptions are failure", "Users can always call support instead of accessible recovery"),
    operate_signals="exception_incomplete_denied.",
    build_structure="empty owner/date => False.",
    break_observe="vulnerable risk.py accepts empty exception.",
    verify_cases="exception needs owner, review date, a11y flag.",
    matrix=(
        ("VP", "complete record", "accept", "allow"),
        ("VP", "empty owner", "accept", "deny"),
        ("expired", "past review_by", "still-open", "deny-or-revisit"),
        ("a11y residual", "flag", "record", "required"),
    ),
    forbidden="Risk exception accepted without owner and review date",
    py_module="risk.py",
    evidence="One-year product security roadmap notes",
)

KINDS = [
    ("01-property.md", "concept-model", "1 Property", "property"),
    ("02-model.md", "design-exercise", "2 Model", "model"),
    ("03-break.md", "mechanism-lab", "3 Break", "break"),
    ("04-build.md", "design-exercise", "4 Build", "build"),
    ("05-verify.md", "verification-lab", "5 Verify", "verify"),
    ("06-operate.md", "operations-exercise", "6 Operate", "operate"),
    ("07-transfer.md", "transfer-challenge", "7 Transfer", "transfer"),
    ("08-review.md", "code-review", "Review", "review"),
]


def md_table(headers: list[str], rows: list[tuple]) -> str:
    line = "| " + " | ".join(headers) + " |"
    sep = "|" + "|".join("---" for _ in headers) + "|"
    body = "\n".join("| " + " | ".join(str(c) for c in r) + " |" for r in rows)
    return f"{line}\n{sep}\n{body}"


def discover_lab(mid: str, spec: dict) -> dict:
    d = lab_dir(mid)
    info = {
        "path": str(d.relative_to(ROOT)),
        "exists": d.is_dir(),
        "impl": "--impl",
        "vuln_files": [],
        "fixed_files": [],
        "tests": [],
        "readme": "",
    }
    if not d.is_dir():
        return info
    vuln = d / "vulnerable"
    fixed = d / "fixed"
    tests = d / "tests"
    if vuln.is_dir():
        info["vuln_files"] = [p.name for p in sorted(vuln.glob("*.py"))]
    if fixed.is_dir():
        info["fixed_files"] = [p.name for p in sorted(fixed.glob("*.py"))]
    if tests.is_dir():
        info["tests"] = [p.name for p in sorted(tests.glob("test_*.py"))]
    readme = d / "README.md"
    if readme.exists():
        info["readme"] = readme.read_text()[:400]
    conf = d / "conftest.py"
    if conf.exists() and "--impl" not in conf.read_text():
        info["impl"] = "fixtures"
    # snippet of vulnerable vs fixed
    py = spec.get("py_module")
    for name in info["vuln_files"]:
        if py and name != py:
            continue
        vp, fp = vuln / name, fixed / name
        if vp.exists():
            info["vuln_src"] = vp.read_text()[:1200]
        if fp.exists():
            info["fixed_src"] = fp.read_text()[:1200]
        info["code_file"] = name
        break
    if "code_file" not in info and info["vuln_files"]:
        name = info["vuln_files"][0]
        info["code_file"] = name
        info["vuln_src"] = (vuln / name).read_text()[:1200]
        if (fixed / name).exists():
            info["fixed_src"] = (fixed / name).read_text()[:1200]
    return info


def header(spec: dict, lo: str, kind: str, step: str) -> str:
    return "\n".join(
        [
            f"# {spec['id']} — {spec['title']} ({step})",
            "",
            f"**Kind:** {kind}  ",
            f"**Loop step:** {step}  ",
            f"**Standards:** {spec['standards']}",
            "",
            "## Property (start here)",
            "",
            spec["property"],
            "",
            "## Attacker capabilities and trust assumptions",
            "",
            f"- **Attacker:** {spec['attacker']}",
            f"- **Trust:** {spec['trust']}",
            "",
        ]
    )


def lesson_property(spec: dict, lab: dict) -> str:
    rows = [
        ("Root cause", spec["root_cause"]),
        ("Preconditions", spec["preconditions"]),
        ("Impact (1.1 cell)", spec["cell"] + " — " + spec["impact"]),
        ("Prevention", spec["prevention"]),
        ("Detection", spec["detection"]),
        ("Recovery", spec["recovery"]),
    ]
    mech = f"**Mechanism (not the property):** {spec['framework_not']}"
    return (
        header(spec, "01", "concept-model", "1 Property")
        + mech
        + "\n\n"
        + "Saltzer/Schroeder still apply: economy of mechanism, fail-safe defaults, complete mediation, open design. A named product (JWT, TLS, scanner, CSP) is not this sentence.\n\n"
        + "## Root cause vs impact vs prevention vs detection vs recovery\n\n"
        + md_table(["Slice", f"For {spec['id']}"], rows)
        + "\n\n## Framework defaults vs application guarantees\n\n"
        + spec["framework_not"]
        + "\n\n## Mechanism limits and bypasses\n\n"
        + spec["mechanism_limit"]
        + "\n\n"
        + spec["bypass"]
        + "\n\n## Residual risk\n\n"
        + spec["residual"]
        + "\n\n## Practice\n\n"
        + spec["practice"]
        + f"\n\nRun `{lab['path']}` (`pytest` with `{lab['impl']} vulnerable` then `{lab['impl']} fixed` if the lab uses `--impl`). Map the failing test to this property.\n\n"
        + "## Transfer\n\n"
        + spec["transfer"]
        + "\n\n"
        + spec["transfer_product"]
        + "\n\n## Non-goals\n\nLive targets, real PII, weaponized copy-paste exploits. Gates 0–10 and milestones M0–M5 stay **not-attempted** without learner/product evidence. Answer keys are not in this file.\n"
        + (f"\n## Usability and accessibility\n\n{spec['wcag']}\n" if spec.get("hitl") and spec.get("wcag") else "")
    )


def lesson_model(spec: dict, lab: dict) -> str:
    return (
        header(spec, "02", "design-exercise", "2 Model")
        + "Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.\n\n"
        + md_table(
            ["Piece", "This system"],
            [
                ("Subjects", spec["subjects"]),
                ("Objects", spec["objects"]),
                ("Actions", spec["actions"]),
                ("Channels", spec["channels"]),
                ("TCB", spec["tcb"]),
                ("Untrusted", spec["untrusted"]),
                ("State / time", spec["state_time"]),
                ("1.1 cell", spec["cell"]),
            ],
        )
        + "\n\n## Authority matrix (minimum)\n\n"
        + md_table(["Subject", "Object", "Action", "Decision"], spec["matrix"])
        + "\n\nA missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.\n\n"
        + "## Practice\n\n"
        + f"Draw this map so a second engineer could name pytest cases. Lab fixture: `{lab['path']}` file `{lab.get('code_file','?')}`.\n\n"
        + "## Transfer\n\n"
        + spec["transfer"]
        + "\n\n## Residual risk\n\n"
        + spec["residual"]
        + "\n\n## Non-goals\n\nDo not answer with a Top 10 item as the definition of security. Keys stay out of lessons.\n"
    )


def lesson_break(spec: dict, lab: dict) -> str:
    vuln = spec.get("break_observe", "")
    src = lab.get("vuln_src", "").strip()
    snippet = f"\n```python\n{src}\n```\n" if src else "\n"
    return (
        header(spec, "03", "mechanism-lab", "3 Break")
        + f"**Forbidden outcome:** {spec['forbidden']}\n\n"
        + f"**Authorized scope:** `{lab['path']}` only. Do not target other hosts. Do not paste weaponized payloads into notes.\n\n"
        + "## What to observe\n\n"
        + vuln
        + "\n\nThe vulnerable tree demonstrates **cause** (wrong mediation/interpreter/trust), not a trophy exploit. Preconditions: "
        + spec["preconditions"]
        + "\n\n## Vulnerable fixture (local)\n"
        + snippet
        + "\n## Root cause vs impact\n\n"
        + md_table(
            ["Slice", "Lab"],
            [
                ("Root cause", spec["root_cause"]),
                ("Impact", spec["impact"]),
                ("Not the lesson", "A scanner name or Top 10 mnemonic as the definition"),
            ],
        )
        + "\n\n## Practice\n\n"
        + f"Run tests against `vulnerable/` (they **must fail** on the forbidden outcome). Record the test name. Command shape: `pytest {lab['path']}/tests -q --impl vulnerable` (or the README if fixtures differ).\n\n"
        + "## Transfer\n\n"
        + spec["transfer"]
        + "\n\n## Non-goals\n\nNo live-target instructions. Synthetic data only.\n"
    )


def lesson_build(spec: dict, lab: dict) -> str:
    src = lab.get("fixed_src", "").strip()
    snippet = f"\n```python\n{src}\n```\n" if src else "\n"
    return (
        header(spec, "04", "design-exercise", "4 Build")
        + spec["build_structure"]
        + "\n\nStructural means the object/interpreter/identity is actually mediated — not a denylist of yesterday’s string, not a scanner suppression, not “trust the framework.”\n\n"
        + "## Fixed fixture (local)\n"
        + snippet
        + "\n## Why this restores the cell\n\n"
        + spec["prevention"]
        + "\n\nFail-safe: on uncertainty, **deny** (or refuse boot / refuse merge / refuse close — whatever the lab’s action is).\n\n"
        + "## What this is not\n\n"
        + spec["framework_not"]
        + "\n\n"
        + spec["mechanism_limit"]
        + "\n\n## Practice\n\n"
        + "Name subject, object, action, and the predicate that must be true after the fix. Run `--impl fixed` (must pass).\n\n"
        + "## Transfer\n\n"
        + spec["transfer"]
        + "\n\n## Residual risk\n\n"
        + spec["residual"]
        + "\n"
    )


def lesson_verify(spec: dict, lab: dict) -> str:
    tests = ", ".join(lab.get("tests") or ["test_property.py"])
    return (
        header(spec, "05", "verification-lab", "5 Verify")
        + "An invariant that cannot fail a test is still a slogan. Happy path is not evidence.\n\n"
        + md_table(
            ["Case", "Must show"],
            [
                ("Normal", "Honest allowed action still works where the product says so"),
                ("Negative / abuse", spec["forbidden"]),
                ("Failure", "Fail closed: " + spec["prevention"].split(".")[0]),
            ],
        )
        + f"\n\nLab tests: `{tests}` under `{lab['path']}`.\n\n"
        + f"- `--impl vulnerable` (or vulnerable fixtures): **fail** on `{spec['forbidden']}`\n"
        + "- `--impl fixed`: **pass**\n\n"
        + spec["verify_cases"]
        + "\n\n## Practice\n\n"
        + "Execute both implementations this session. Paste nothing from keys. Map each test to a matrix cell from LO-02.\n\n"
        + "## Transfer\n\n"
        + spec["transfer"]
        + "\n\nA test that only asserts HTTP 200 is not this module’s evidence (see 9.3).\n"
    )


def lesson_operate(spec: dict, lab: dict) -> str:
    return (
        header(spec, "06", "operations-exercise", "6 Operate")
        + "Prevention is not absolute. Pair detect and recover. Do not log secrets or note bodies (3.1 / 5.1).\n\n"
        + md_table(
            ["Outcome", "This module"],
            [
                ("Detect", spec["detection"]),
                ("Signal (no bodies)", spec["operate_signals"]),
                ("Revoke / recover", spec["recovery"]),
                ("Residual", spec["residual"]),
            ],
        )
        + "\n\nCSF 2.0 Detect / Respond / Recover name *outcomes*. They do not prove ASVS.\n\n"
        + "## Practice\n\n"
        + "Write one log line you would accept in review (ids, reason, no body, no real email). Tie it to `"
        + lab["path"]
        + "`.\n\n"
        + "## Transfer\n\n"
        + spec["transfer"]
        + "\n"
        + (f"\n## Usability\n\n{spec['wcag']}\n" if spec.get("hitl") and spec.get("wcag") else "")
        + "\n## Non-goals\n\nSIEM product names are not the property. Keys stay out of lessons.\n"
    )


def lesson_transfer(spec: dict, lab: dict) -> str:
    return (
        header(spec, "07", "transfer-challenge", "7 Transfer")
        + "Change one channel, principal, or object class. Rewrite the invariant. Do not answer with a Top 10 / CWE Top 25 / scanner as the definition of security.\n\n"
        + f"**Prompt:** {spec['transfer']}\n\n"
        + f"**Product sketch:** {spec['transfer_product']}\n\n"
        + "Your answer must include: attacker capabilities, trust assumptions, a forbidden outcome, a test idea that would fail if the cell were false, residual risk, and whether a human path must meet WCAG 2.2.\n\n"
        + "## What graders reject\n\n"
        + md_table(
            ["Reject", "Why"],
            [
                ("Tool or awareness-list name as the property", "1.1"),
                ("Framework default as the guarantee", spec["framework_not"][:80] + "…"),
                ("Live-target plan", "Lab policy"),
            ],
        )
        + "\n\n## Practice\n\n"
        + "One page. No keys. The lab `"
        + lab["path"]
        + "` stays the only running system you may break.\n"
    )


def lesson_review(spec: dict, lab: dict) -> str:
    findings = spec["review_findings"]
    bullets = "\n".join(f"- Seeded smell (label it yourself): {f}" for f in findings)
    return (
        header(spec, "08", "code-review", "Review")
        + f"Review `{lab['path']}/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/{spec['id']}.md` — not here.\n\n"
        + "## What to label\n\n"
        + "For each claim and each branch: **property**, **mechanism**, or **false assurance**.\n\n"
        + bullets
        + "\n\nAlso reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.\n\n"
        + "## Misconceptions\n\n"
        + "\n".join(f"- {m}" for m in spec["misconceptions"])
        + "\n\n## Practice\n\n"
        + "Write three review notes. Do not open the keys file.\n\n"
        + "## Transfer\n\n"
        + spec["transfer"]
        + "\n"
        + (f"\n## HITL / WCAG 2.2\n\n{spec['wcag']}\n" if spec.get("hitl") and spec.get("wcag") else "")
    )


RENDER = {
    "property": lesson_property,
    "model": lesson_model,
    "break": lesson_break,
    "build": lesson_build,
    "verify": lesson_verify,
    "operate": lesson_operate,
    "transfer": lesson_transfer,
    "review": lesson_review,
}


def write_lessons(mid: str, spec: dict) -> None:
    lab = discover_lab(mid, spec)
    d = module_dir(mid) / "lessons"
    d.mkdir(parents=True, exist_ok=True)
    for filename, kind, step, key in KINDS:
        text = RENDER[key](spec, lab)
        (d / filename).write_text(text)


def write_assessment(mid: str, spec: dict) -> None:
    lab = lab_dir(mid)
    rel = str(lab.relative_to(ROOT)) if lab.exists() else f"labs/{mid}/{lab_slug(mid)}"
    rubric = f"""# {mid} assessment (learner-facing — no answers)

**Pass C.** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Module

{spec['title']}

## Evidence checklist

- [ ] {spec['evidence']}
- [ ] Transfer task ({spec['transfer_product']})
- [ ] Lab `{rel}`: forbidden outcome **{spec['forbidden']}**
- [ ] `vulnerable/` tests fail, `fixed/` tests pass (authorized local fixture only)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Operate signal without note bodies / secrets: {spec['operate_signals']}

## Rubric

| Result | Meaning |
|---|---|
| Developing | Tools listed; missing attacker/trust; mechanism slogans |
| Competent | System-specific invariant; lab mapped; operate present |
| Transfer-ready | LO-07 done without Top 10/scanner language as the definition of security |

Knowledge check (retryable): distinguish property vs mechanism for **{mid}**. Items live in the session worksheet, not here.

## Seeded review

Use the local `vulnerable/` artifact. Intended findings live only in `content/assessment/keys/{mid}.md`.
"""
    ad = module_dir(mid) / "assessment"
    ad.mkdir(parents=True, exist_ok=True)
    (ad / "rubric.md").write_text(rubric)

    findings = "\n".join(f"- {f}" for f in spec["review_findings"])
    keys = f"""# Examiner notes — {mid} (not learner-facing)

## Property

{spec['property']}

## Lab

- `{rel}/vulnerable/` must fail: {spec['forbidden']}
- `{rel}/fixed/` must pass.
- Root cause: {spec['root_cause']}

## Seeded review intended findings

{findings}

## Transfer

Reject answers that name Top 10 / CWE Top 25 items as the definition of security.
Require a system-specific invariant, attacker, trust, residual risk.
Acceptable transfer direction: {spec['transfer']}

## Operate

Accept a detect/recover note that does not log bodies/secrets. Example signal: {spec['operate_signals']}
"""
    kdir = CONTENT / "assessment" / "keys"
    kdir.mkdir(parents=True, exist_ok=True)
    (kdir / f"{mid}.md").write_text(keys)


def stamp_yaml(mid: str, spec: dict) -> None:
    path = module_dir(mid) / "module.yaml"
    data = yaml.safe_load(path.read_text())
    data["reviewer"] = REVIEWER
    data["lastReviewedAt"] = TODAY
    data["nextReviewAt"] = "2027-02-24"
    lab = data.get("labSpec") or {}
    lab["slug"] = lab_slug(mid)
    lab["summary"] = spec["forbidden"]
    lab["authorizedScope"] = (
        "Local course fixture or official training lab only; no public or third-party targets"
    )
    lab["forbiddenOutcomes"] = [
        spec["forbidden"],
        "Live-target instructions",
        "Real PII or production secrets",
        "Awareness list used as the syllabus",
    ]
    data["labSpec"] = lab
    data["misconceptions"] = list(spec["misconceptions"])
    data["operationalConsiderations"] = [
        spec["operate_signals"],
        spec["residual"],
    ]
    los = data.get("learningObjects") or []
    titles = {
        0: f"{spec['title']}: property vs mechanism",
        1: f"Model {spec['system']} for {mid}",
        2: f"Local fixture: {spec['forbidden']}",
        3: f"Structural fix restoring the {mid} invariant",
        4: f"Forbidden-outcome tests for {mid}",
        5: f"Detect/recover notes for {mid}",
        6: f"Transfer: {spec['transfer_product']}",
        7: f"Seeded review for {mid}",
    }
    for i, lo in enumerate(los):
        if i in titles:
            lo["title"] = titles[i]
    data["learningObjects"] = los
    ch = list(data.get("changelog") or [])
    ch.append(
        {
            "date": TODAY,
            "note": "Publishable rewrite: unique 1.2-density lessons, structural lab mapping, Pass C keys isolated",
        }
    )
    data["changelog"] = ch
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))


def main() -> None:
    props = [SPECS[k]["property"] for k in SPECS]
    if len(props) != len(set(props)):
        raise SystemExit("duplicate properties")
    forbs = [SPECS[k]["forbidden"] for k in SPECS]
    if len(forbs) != len(set(forbs)):
        raise SystemExit("duplicate forbidden outcomes")
    written = []
    for mid, spec in SPECS.items():
        if mid in SKIP_LESSONS:
            write_assessment(mid, spec)
            stamp_yaml(mid, spec)
            continue
        write_lessons(mid, spec)
        write_assessment(mid, spec)
        stamp_yaml(mid, spec)
        written.append(mid)
    print("wrote lessons for", len(written), "modules")
    print("specs", len(SPECS))


if __name__ == "__main__":
    main()





