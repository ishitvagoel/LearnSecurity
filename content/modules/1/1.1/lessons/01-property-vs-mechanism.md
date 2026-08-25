# 1.1-LO-01 — Security is a claim about outcomes

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** Saltzer and Schroeder (1975, seminal) for named protection principles; NIST CSF 2.0 (final) for outcome functions, not a control catalogue.

## The question that comes before controls

Suppose a design review begins with: “We use TLS, bcrypt, JWTs, a web application firewall, and a weekly scanner.” You still do not know what security means for the product.

Those statements name mechanisms. A security property names an outcome that must remain true while a stated adversary acts, a component fails, or the system moves through time. An invariant is a property phrased precisely enough that a reviewer can imagine a forbidden counterexample.

For SecureCollab, compare these claims:

| Claim | Type | Why |
|---|---|---|
| We use TLS. | Mechanism | It says nothing about note bodies in logs, backups, browser storage, or a misrouted tenant response. |
| A member of Tenant B cannot read a Tenant A note through any public API operation. | Property, but incomplete | It names an actor, object, action, and forbidden result. It still needs assumptions, time horizon, and evidence. |
| Tenant A note bodies remain unreadable to Tenant B members through the public API, application logs they can reach, and retained exports; the browser is hostile and the API policy layer is trusted. | Property-shaped invariant | It bounds channels, attacker capability, trusted enforcement, and retained state. |

A mechanism is valuable only after you can say which property it supports, under which assumptions, and how you will know when it stops working.

## The claim envelope

A useful invariant has more than a sentence. Treat the invariant as the center of a claim envelope:

| Element | Question it answers | Weak version | Stronger SecureCollab version |
|---|---|---|---|
| Asset | What is valued? | data | note body, membership record, audit event |
| Subject and action | Who may do what? | users can access notes | a current Tenant A member may read a Tenant A note |
| Attacker capability | What can the adversary control? | malicious user | an authenticated Tenant B member can modify every browser request and guess identifiers |
| Trusted base | What must behave correctly? | the server | the FastAPI authorization path and PostgreSQL role are trusted; the browser is not |
| State and time | When must it hold? | always | during a request and across retained logs, exports, and backup restore |
| Forbidden outcome | What observable result disproves it? | breach | a Tenant B response contains any Tenant A note-body bytes |
| Evidence | How could a reviewer challenge it? | scanner passes | cross-tenant negative tests, log-capture tests, and restore-path review |
| Residual risk | What remains outside the claim? | none | a cloud administrator with database snapshot access is out of scope for Phase 1 and triggers a later encryption/key-management review |

The envelope prevents universal claims. “No unauthorized person can ever read a note” sounds strong but is not testable until unauthorized, read, note, channels, time, and trusted components are defined.

## Eight useful property names, not eight checkboxes

The names below are prompts. They overlap, trade off, and depend on the product.

| Property | SecureCollab invariant shape | A counterexample |
|---|---|---|
| Confidentiality | A note body is disclosed only to principals authorized for that note and tenant over the channels in scope. | A support log contains the full body. |
| Integrity | Note content and membership change only through authorized transitions; corruption is detectable. | A retry applies the same membership removal twice and leaves an invalid state. |
| Availability | One tenant’s expensive request cannot exhaust every tenant’s ability to read existing notes beyond the stated recovery objective. | An unbounded export starves normal reads. |
| Authenticity | Security-relevant actions attributed to a principal have evidence tied to the authenticator and service path used. | An internal header supplied by a browser is recorded as a worker identity. |
| Authorization | Authentication alone never grants an action; the current subject-object-action relationship is evaluated at the enforcement point. | A logged-in Tenant B member reads Tenant A by changing a note identifier. |
| Accountability | High-impact changes produce privacy-safe evidence sufficient to reconstruct who requested what and which policy decision occurred. | A tenant-admin role grant is stored with no actor or correlation identifier. |
| Privacy | Collection, retention, inference, and disclosure stay within the stated purpose, even if storage is confidential. | Deleted note titles remain in analytics indefinitely. |
| Safety | Failure and recovery do not create unacceptable harm to people or surrounding systems. | Account recovery exposes a coerced user or permanently locks out an accessible user. |

Do not force all eight into every row. If a property is not claimed, record a non-goal and the review trigger that would make it relevant. Omitting a considered non-goal is different from forgetting it.

## A worked causal trace: “passwords are hashed”

Start with the mechanism claim: “SecureCollab is secure because passwords are hashed.”

1. **Possible property supported:** a database snapshot alone should not reveal reusable plaintext passwords within an assumed work factor.
2. **Attacker and preconditions:** the attacker obtains stored credential verifiers but not the application’s live memory, password-entry logs, or reset channel.
3. **Mechanism:** a slow, salted password-hashing construction and safe parameter management.
4. **Mechanism limits:** weak user passwords can still be guessed; an application log may capture plaintext before hashing; a reset flow can bypass the password; hashing says nothing about note authorization.
5. **Impact if the original slogan is trusted:** reviewers may incorrectly mark note confidentiality, session security, and recovery as covered.
6. **Prevention:** narrow the claim and design each unrelated property separately.
7. **Detection:** review logs and telemetry schemas for credential fields; monitor unusual authentication attempts without recording passwords.
8. **Recovery:** invalidate exposed credentials or sessions, remove captured sensitive data, notify affected users when required, and repair the capture path.

The root cause is not “bcrypt is bad.” It is collapsing a bounded mechanism into a universal property.

## Protection principles shape mechanism choice

Saltzer and Schroeder’s principles help test a proposed mechanism after the property is clear:

- **Economy of mechanism:** can the enforcement path be smaller and easier to review?
- **Fail-safe defaults:** is a missing or ambiguous decision a denial?
- **Complete mediation:** is authority checked on every relevant access, including retries and alternate routes?
- **Open design:** would disclosure of the design break the property? If so, secrecy has become an unrecorded assumption.
- **Least privilege and least common mechanism:** can the trusted base and shared blast radius shrink?
- **Psychological acceptability:** can legitimate users complete the secure path, including recovery?
- **Compromise recording:** when prevention is incomplete, is useful evidence likely to survive?

The principles do not prove a design. They are reasoning tools for finding hidden assumptions and unnecessarily large trust.

## Outcome functions are not proof

NIST CSF 2.0 groups outcomes under Govern, Identify, Protect, Detect, Respond, and Recover. The sequence reminds you that prevention alone is incomplete. A Protect mechanism does not satisfy a property merely because it maps to a framework label. Evidence must still show that the system-specific forbidden outcome is prevented or bounded.

## Practice: turn a slogan into a bounded claim

Choose one slogan:

- “We encrypt everything.”
- “Only admins can do that.”
- “The framework validates input.”
- “We keep audit logs.”

Write six lines:

1. the asset, subject, action, and forbidden outcome;
2. attacker capabilities;
3. trusted components and explicitly untrusted components;
4. state and time horizon;
5. one piece of negative evidence;
6. one residual risk or non-goal.

A peer should be able to invent a concrete counterexample. If they cannot, your claim is probably too vague. If their counterexample is outside your recorded scope, your claim may be precise—but the scope must be defensible.

## Check your model

Before continuing, you should be able to explain:

- why confidentiality and privacy are not synonyms;
- why a mechanism can support one property while failing another;
- why “always” usually hides channels or time;
- why detection and recovery belong in the claim when prevention is not absolute;
- why a secure framework default is not an application guarantee.

LO-02 turns this vocabulary into a versioned catalogue for SecureCollab.
