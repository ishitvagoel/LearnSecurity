# Review always-true pod_ok like a pull request

**Kind:** code-review
**Loop step:** Review

Intended findings live only in the answer-key folder — not here. Do not open that file until your review has been evaluated.

## What you are reviewing

A colleague ships the notes app's cluster admission. Review `labs/10.3/10.3-lab/vulnerable/` as that change. Your job is not to count suspicious lines. Reconstruct whether `pod_ok("cluster-admin")` still returns true, compare that with the rule, and write changes a developer can verify.

Start at `pod_ok` and the cluster-admin row, not at a scanner color or a CIS screenshot. The check you already ran (`test_cluster_admin_pod_is_denied`) is the rule test. A comment "will tighten RBAC later" is not.

## Picture: cluster-admin on app SA

Start with this seeded smell: **cluster-admin on app SA**. Label it rule, tool, or false comfort before you accept the change.

```mermaid
flowchart TD
  Claim[PR claim] --> Q{"What would show it is false?"}
  Q -->|cluster-admin runs| Property["Rule - good if tested"]
  Q -->|namespace private| Mechanism[Tool - naming]
  Q -->|CIS scan green| False[False comfort]
```

Classification starts at the protected effect (cluster-admin denied). Everything that is not allow-list membership at that call is a candidate always-run path. A CIS screenshot without that pytest is the same smell, not a different finding class.

A restricted pod profile is pod spec. A network policy is egress. Instance metadata is a sibling leftover. Name them, do not skip `test_cluster_admin_pod_is_denied`. Do not claim you finished an assurance gate. Do not apply manifests to a live cluster to prove the finding.

## Seeded smells (label them yourself)

- cluster-admin on app SA
- `privileged: true`
- No admission test
- IaC with `0.0.0.0/0`

Also reject: live cluster attacks; admitting without re-running `test_cluster_admin_pod_is_denied`; keys in learner notes; claiming an assurance gate.

## Common mix-ups

- Namespace equals tenant
- Managed Kubernetes is secure by default
- A network policy is who-is-allowed on the API
- A restricted pod profile is `pod_ok`
- A CIS score is an assurance gate

## Practice

Write three review notes a maintainer could act on. Each note: what you saw, rule or false comfort, suggested structural change, leftover you will **not** delete. Tie at least one note to `test_cluster_admin_pod_is_denied`. Do not open the keys file.

## Use it somewhere new

Clinic change that "added a namespace and a CIS scan" without a ClusterRole deny is an incomplete admission review. Name the independent falsehood that would still keep cluster-admin from running.

## Can people still use it

A denied admission must say why the pod stayed out (cluster-admin refused), not only "will tighten RBAC later."

## What this page is not doing

Do not merge by adding a comment "will tighten RBAC later." That comment is leftover without an owner. Do not attack a live cluster to prove the finding.
