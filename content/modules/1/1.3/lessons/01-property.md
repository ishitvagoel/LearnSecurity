# 1.3-LO-01 — Boundaries are changes in assumptions, not lines around servers

**Kind:** concept-model  
**Loop step:** 1 Property  
**Standards:** OWASP Threat Modeling Project (maintained guidance, Four Questions and lifecycle refinement); Saltzer and Schroeder (1975, seminal), especially economy of mechanism, fail-safe defaults, complete mediation, and least common mechanism.

## Start with the claim

SecureCollab’s diagram is not the security property. Begin with one bounded claim:

> For a SecureCollab Phase 1 note export, a public requester cannot become a worker merely by choosing request metadata. The export effect occurs only after a trusted server-side adapter establishes worker provenance and a current grant narrows the worker to the intended tenant, action, and object set. Missing or unknown context denies.

This claim names an effect, attacker capability, trusted decision, scope, and failure default. It can be false even if every connection uses TLS and every box runs in a private subnet. Conversely, two functions in the same process can sit on opposite sides of the relevant trust boundary if one accepts hostile fields and the other accepts only context constructed by a trusted adapter.

A **trust boundary** is where a security-relevant assumption or capability changes. Ask what the receiving side may rely on after crossing. A line is useful only when its annotation answers that question.

## Keep six terms separate

| Term | Precise question | SecureCollab example |
|---|---|---|
| Actor | Who or what participates? | Member, tenant admin, batch operator, attacker |
| Principal | Which identity is used for a decision? | Current member ID or export-worker ID |
| Component | Where does code or data run? | Public adapter, policy function, note store |
| Channel | How are representations carried? | Function arguments now; HTTP or queue later |
| Entry point | Where can an actor or failure first influence in-scope behavior? | Public request adapter; worker adapter |
| Trust boundary | Where does a relevant assumption or capability change? | Untrusted request fields become a validated public context; worker identity becomes a server-constructed context |

These can coincide, but they are not synonyms. One component can expose several entry points with different assumptions. One channel can carry both trusted and untrusted data. One actor can act through several principals. A boundary can be crossed without a network.

### Network line without a new trust boundary

Suppose a public request passes through a transparent relay. Both sides still treat every field as attacker-controlled, and the relay adds no authenticated provenance or enforcement. There is a network hop, but for the export-authority property the relevant assumption did not change. Drawing a boundary there and labeling it “trusted edge” would invent trust.

### Trust boundary without a network line

Suppose `public_entry(...)` parses hostile fields and calls a policy function with a `PublicContext` that cannot represent a worker. The two functions execute in one Python process. The assumption changes from “the caller chooses these strings” to “this context was constructed through the public adapter and cannot carry worker authority.” That is a meaningful boundary for this property.

## The TCB is relative to a property

The **trusted computing base** is the set of components and assumptions that must be correct for a stated property. It is not a permanent inventory of everything called “backend.”

For the Phase 1 export-authority claim, a candidate TCB includes:

- the adapter that distinguishes public and worker call paths;
- the source of worker identity and scoped grant;
- the policy/enforcement code that consumes that context immediately before export;
- the store or fixture state used to resolve tenant and note scope;
- the language/runtime assumptions needed to preserve the context type and state.

The public browser should not be in that TCB. If a browser must honestly label itself as an internal worker, the design has already conceded the property.

Change the property and the TCB changes. For **note confidentiality**, output selection and any log/export sink handling note bodies matter. For **availability**, resource limits, work scheduling, and perhaps a dependency’s failure behavior matter; the content projection might not. For **accountability**, the evidence producer, transport, store, clock assumptions, and access to evidence become central. Saying “the API is trusted” hides those differences.

Use this test:

> If this component behaved maliciously or incorrectly, could the stated property fail despite every other listed control working as assumed?

If yes, it belongs in the TCB or the property must be narrowed. If no, it may be deployed and security-relevant without belonging to this property’s TCB. If you cannot decide, mark the dependency **unknown**, not trusted by optimism.

## Attack surface is reachable influence on a protected effect

An **attack surface** is the set of ways an attacker or modeled failure can influence a protected effect. Ports and routes can be members of the set, but they do not define it.

For a note export, relevant surface can include:

- the public request entry point and all fields it accepts;
- the worker entry point and the mechanism that establishes service provenance;
- stored tenant and note identifiers read later;
- a queued or retried message when workers are introduced;
- the policy and enforcement path;
- the shared database role or cache key that can widen reach;
- the evidence path if suppressing evidence changes whether the effect proceeds;
- administrative/configuration paths that can redefine worker identity or scope.

A CVE list answers a different question. An endpoint list misses stored inputs, alternate paths, shared credentials, configuration, evidence suppression, and state transitions. Derive the inventory from flows to protected effects, then ask what can influence each flow.

## Transitive trust and shared mechanisms

Trust is often transitive:

```text
export decision
  relies on worker context
    relies on adapter provenance
      may later rely on queue identity and deployment configuration
        may rely on build/control-plane operators
```

The diagram should stop only at an explicit assumption, residual, or later-module boundary. “Managed service” is not an endpoint in the reasoning chain.

Saltzer and Schroeder’s **least common mechanism** warns that mechanisms shared by users or scopes create communication and failure channels. A process-wide database credential, a tenantless cache key, one parser used by edge and API, or a logging pipeline shared with sensitive content can expand both attack surface and blast radius.

Shared does not always mean unacceptable. It means the claim must account for common-mode failure. If two layers both rely on the same `X-Internal` value, the second check is not independent evidence of worker provenance. If a configuration mistake causes both to accept the value, both fail together.

## Isolation and blast radius are claims about effects

An **isolation boundary** is a mechanism intended to prevent one scope from influencing another. A container, schema, process, credential, sandbox, or network policy may contribute. Its name does not prove the property.

**Blast radius** describes what a compromised or mistaken capability can affect. Bound it across dimensions:

- which tenants and objects;
- which actions: read, mutate, delete, execute, administer, or suppress evidence;
- which data fields and sensitivity;
- which egress destinations;
- which time, expiry, replay, and retry window;
- which control-plane or policy changes;
- which evidence can be hidden or forged.

“Worker access is limited” is not reviewable. “The capability can export note summaries for Tenant A’s object set once before 12:05, cannot read bodies, cannot choose egress, cannot alter policy, and emits an independent decision record” is a bounded claim. Later modules will supply production mechanisms; this module requires the reasoning shape.

## Defense in depth requires a failure argument

Multiple controls can be useful for different reasons:

- **prevention** blocks the effect;
- **detection** makes misuse or drift observable;
- **recovery** limits duration or restores state.

Calling them “layers” is not enough. Compare their failure assumptions.

| Pair | Independence question | Honest conclusion |
|---|---|---|
| Edge strips `X-Internal`; API trusts `X-Internal` | Do both rely on the same field and routing/configuration? | Correlated for header-forgery failure |
| Adapter constructs typed worker context; policy enforces scoped capability | Can a requester bypass the adapter or mint the capability? | Potentially complementary; prove enforcement coverage |
| Policy denies; evidence sink records decision | Can failure of the policy also suppress evidence? Does evidence failure block? | Detection may be partially independent, not preventive |
| Two products use the same identity assertion and administrator | Can one false assertion or operator mistake defeat both? | Correlated for that failure |

Independence is always “independent with respect to which failure?” A control may be independent of parser compromise but correlated through the same cloud control plane. Unknown dependencies should be labeled unknown.

## Work the four questions

OWASP’s current Threat Modeling Project recommends a methodology-neutral Four Question starting point:

1. **What are we working on?** The property, Phase 1 scope, flows, assumptions, boundaries, TCB, and dependencies.
2. **What can go wrong?** Forged provenance, scope widening, alternate entry, replay, dependency failure, shared-mechanism collision, evidence suppression.
3. **What are we going to do?** Structural adapter separation, narrow authority, fail-safe enforcement, evidence, recovery, explicit residuals.
4. **Did we do a good enough job?** Trace every effect, use five evidence modes, challenge independence, and refresh on change or incident.

This is not a claim that OWASP mandates one threat-modeling method. STRIDE, LINDDUN, attack trees, and more formal elicitation come later. Here the four questions prevent the diagram from becoming decorative.

## Guided practice — classify before drawing

For each statement, label it **property**, **component**, **entry point**, **channel**, **trust boundary**, **TCB claim**, **attack-surface item**, **isolation claim**, **blast-radius claim**, or **unsupported**. More than one label may apply only if you explain why.

1. “The browser connects using TLS.”
2. “The public adapter treats every request field as attacker-controlled.”
3. “Only the worker adapter can construct `WorkerContext`.”
4. “The API and edge both reject requests whose `X-Internal` value is not `worker`.”
5. “One process-wide store credential can read all tenants.”
6. “A single-use grant names Tenant A, action `export_summary`, and notes A1/A2.”
7. “The audit sink is down, but exports continue and no alternate evidence exists.”
8. “The service is in a private subnet, so public callers cannot influence it.”

For every **unsupported** statement, rewrite it as a falsifiable claim. Include the protected property, attacker/failure capability, changed assumption, trusted source, forbidden effect, and oracle.

### Success criteria

Your answer is ready for peer review when:

- no box, protocol, product, address range, or internal name is trusted by label alone;
- the TCB is tied to one property and changes when the property changes;
- entry point and channel are not used as synonyms;
- attack-surface rows point to reachable protected effects;
- isolation and blast radius name dimensions and evidence;
- defensive layers include a common-mode failure analysis;
- unknowns and later work remain explicit.

## Transfer hook

PreviewForge will accept hostile document bytes, store them, trigger asynchronous conversion, and publish previews. Before LO-07, predict why “the upload API is the boundary” is insufficient. Consider stored-input entry, parser workers, object-store callbacks, queue replay, converter egress, shared libraries, preview caching, moderator tools, and evidence suppression. Do not solve the transfer yet; list which definitions from this lesson will need a new instance.
