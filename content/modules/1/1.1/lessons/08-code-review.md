# 1.1-LO-08 — Review a security document as an engineering claim

**Kind:** code-review  
**Loop step:** 5 Verify
**Fixture:** labs/1.1/1.1-invariant-catalogue/vulnerable/SECURITY.md

## Review objective

Security documentation can create false assurance before a line of vulnerable application code exists. Treat the seeded SECURITY.md as a proposed engineering claim in a pull request.

Your review should determine whether each sentence is:

- a property;
- a mechanism;
- evidence;
- an assumption or non-goal;
- false assurance;
- or too ambiguous to classify.

Do not open content/assessment/keys/1.1.md until your work has been evaluated.

## Review method

### 1. Reconstruct the implied claim

For every mechanism named by the document, ask:

- which asset and forbidden outcome is this supposed to address?
- against which attacker capability?
- which trusted component must enforce it?
- over which channel and time horizon?
- what evidence would falsify the claim?
- what unrelated properties remain uncovered?

If the document does not answer, do not invent certainty on the author’s behalf. Record the gap.

### 2. Trace control to outcome

Create a table:

| Source sentence | Classification | Implied property | Missing assumptions | Counterexample | Minimum rewrite |
|---|---|---|---|---|---|

A counterexample should be safe and conceptual. For example, a transport mechanism may protect one network hop while a log or authorization error discloses the same asset. Do not demonstrate attacks against a running or public system.

### 3. Look for universal language

Flag terms such as secure, protected, encrypted, validated, compliant, impossible, always, and only when they lack a bounded subject, object, action, attacker, trust, channel, or time horizon.

Universal language is not automatically wrong. It carries a large proof obligation that the seeded document does not meet.

### 4. Look for missing operations

Ask what happens when the stated mechanism fails, is bypassed, is misconfigured, or produces no evidence. A security claim with no detection, response, recovery, or review trigger may be incomplete even if its prevention mechanism is reasonable.

### 5. Check editorial integrity

A reviewer line, green badge, generated timestamp, or passing schema is not independent evidence of semantic quality. Verify who reviewed what, against which criteria, and with which test result.

## Write actionable review comments

Each comment should contain:

1. the unsupported conclusion;
2. the concrete missing model element;
3. why the gap matters;
4. the minimum requested change;
5. how the revised claim could be evaluated.

Avoid “needs more detail.” Prefer: “This sentence names a credential-storage mechanism but concludes that the whole application is secure. Please state the credential property, snapshot attacker, trusted capture paths, time horizon, and evidence; move note confidentiality and authorization to separate catalogue rows.”

## Required output

Submit:

- the classification table;
- at least four actionable comments;
- one proposed bounded rewrite;
- one residual risk the document should acknowledge;
- one review trigger for a future asset or actor;
- a short note explaining why a green scanner result cannot close the review.

## Transfer

Review this new sentence without naming a vendor-specific fix:

> We use signed tokens, so only authorized workers can process jobs.

Identify the property, subject, object, action, attacker capability, trust assumptions, state/time issue, mechanism limit, evidence, and residual risk that the sentence omits.
