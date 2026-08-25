# 1.1-LO-06 — Preserve useful outcomes when prevention fails

**Kind:** operations-exercise  
**Loop step:** 6 Operate  
**Standards:** NIST CSF 2.0 Detect, Respond, and Recover functions as outcome categories.

## Prevention is a dependency, not a promise

Assume one prevention mechanism fails. A stale authorization cache serves one cross-tenant response, an exception path logs a note body, or a restore reintroduces deleted metadata. The invariant has already been violated. Operations determines whether the violation is quickly bounded, understood, and repaired—or remains invisible.

For one catalogue row, extend the claim with detection, response, recovery, and evidence-retention properties.

## Design a privacy-safe event

An accountability event should contain enough context to reconstruct a decision without copying the protected asset.

A useful authorization event might contain:

- event type and schema version;
- opaque actor identifier and authenticator class;
- tenant and object identifiers, not note contents;
- requested action;
- policy decision and reason code;
- enforcement point;
- correlation identifier;
- trustworthy timestamp and service identity.

It should not contain note bodies, passwords, session tokens, raw authorization headers, recovery answers, or unnecessary personal attributes.

The event itself creates new properties: confidentiality of the log, integrity of evidence, availability during an incident, retention limits, and access accountability.

## From event to detection

A signal is not “log denied requests.” State the pattern and why it matters.

| Element | Example shape |
|---|---|
| Signal | One actor requests objects from many tenant identifiers and receives repeated tenant-mismatch denials |
| Threshold/window | A risk-based count over a short window, with a lower threshold after an impossible tenant transition |
| Suppression | Known test tenants and health paths are excluded by authenticated service identity, not a client header |
| Destination | On-call security/operations route with least-privilege access |
| Privacy limit | No note bodies, tokens, or raw query values |
| Failure behavior | If the event pipeline is unavailable, the policy decision still denies; evidence loss is separately alerted |

Thresholds are hypotheses. Record false-positive and false-negative risks rather than declaring them universally correct.

## Response and recovery sequence

Write an ordered runbook fragment:

1. **Triage:** verify the signal source and scope without opening protected content unnecessarily.
2. **Contain:** revoke the relevant session, share, role, key, or worker identity; avoid disabling every tenant unless impact justifies it.
3. **Preserve evidence:** protect logs and decision records with access and retention controls.
4. **Eradicate root cause:** repair the policy, state transition, configuration, or alternate path—not only the observed request.
5. **Recover:** restore known-good state, purge wrongly retained data, rebuild caches, and validate the forbidden-outcome tests.
6. **Communicate:** notify affected parties with facts, uncertainty, and actionable recovery steps.
7. **Learn:** update the invariant, assumptions, review triggers, tests, and runbook.

Recovery is complete only when the system-specific property is re-established and evidence supports that conclusion. “Service is back up” may be unrelated.

## When the operator is the attacker

An operator who can alter both the protected state and its evidence defeats a catalogue row that trusts the same administrative plane for prevention and recording. Possible design directions include separation of privilege, append-only or externally witnessed records, approval for high-impact actions, and independent restore verification.

Do not turn those mechanisms into guarantees. State the remaining trust: who controls the witness, keys, retention, and emergency override? If no independent evidence survives, record that as residual risk.

## Human factors are part of the property

Response and recovery paths are security controls used under stress. They fail when:

- the only approver is unavailable;
- a keyboard or screen-reader user cannot complete recovery;
- a warning communicates only by color;
- a revocation action gives no status and is repeated;
- a user must remember inaccessible historical details;
- an incident message drives people toward an unsafe workaround.

For a human-in-the-loop step, name an accessible alternative, a clear completion state, and a safe failure path. Usability is not cosmetic when it determines whether containment or recovery occurs.

## Practice: operate paragraph

Attach an operate section to one catalogue row with:

- event fields and prohibited fields;
- signal, threshold, and evidence-pipeline failure behavior;
- containment authority and blast radius;
- root-cause repair;
- recovery validation;
- communication owner and audience;
- one operator-compromise residual risk;
- one accessibility or usability constraint if a person must act.

Then ask a peer to remove the prevention mechanism mentally. Does your operate section still preserve any valuable outcome? If the answer is no, either improve it or state honestly that the current design has no independent detection or recovery.

## Transfer

Suppose SecureCollab adds a background worker that retries webhook delivery. The worker has different identity, timing, and evidence paths. Identify which event fields, containment actions, and trust assumptions from your current operate paragraph do not transfer.
