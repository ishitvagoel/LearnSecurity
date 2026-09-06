# 10.3 — Cloud, serverless, containers, Kubernetes, and IaC

Pass A specification. Lesson prose lives in `lessons/`. Workload identity is least privilege at cluster grain — not “our namespace is private.” Do not mark M4 or Gate 10 complete.

## Identity

- **id:** 10.3
- **slug:** cloud-serverless-containers-kubernetes-and-iac
- **title:** Cloud, serverless, containers, Kubernetes, and IaC
- **phase / track / difficulty:** 10 / core / advanced
- **estimatedMinutes:** 240
- **prerequisites:** Blueprint §7; 3.3 least privilege; 6.5 metadata/SSRF; 7.4 worker identity.
- **routeTags:** complete, web-api
- **releaseMilestone:** M4
- **masteryGate:** 10

## Objective hierarchy

1. Produce a **pod admission predicate** so `pod_ok("cluster-admin")` is false.
2. Name attacker capabilities (compromised app container; malicious Helm chart; instance-metadata hop) and trust assumptions (local `pod_ok(role)`; K8s is a *model* even if production is serverless).
3. Transfer: clinic app SA is `cluster-admin`; serverless IAM `*` — without treating a namespace, NetworkPolicy, or managed Kubernetes as 1.2.

## Prerequisite concepts

3.3 least privilege; 6.5 link-local metadata; 7.4 leftover sessions as worker identity. NIST SP 800-190 (final, 2017) as container-stack vocabulary. Kubernetes Pod Security Standards / Pod Security Admission as policy vocabulary, not RBAC. ASVS `v5.0.0-13.2.1` / `v5.0.0-13.2.2` / `v5.0.0-13.2.4`.

## Misconceptions

- Namespace equals tenant isolation.
- Managed Kubernetes is secure by default.
- Containers are VMs.
- NetworkPolicy is RBAC.
- PSS/PSA replaces RBAC (they are different planes).

## Concept map

Always-true admission (break) → namespaced allowlist (this module) → PSS restricted + RBAC RoleBinding → IMDS hop denied (6.5) → worker principal (7.4). Residual: break-glass ClusterRole with E6.

## Invariant prompts

- What must remain true for `pod_ok("cluster-admin")`?
- What fails if the namespace is “private” but the ServiceAccount is ClusterRole `cluster-admin`?

## Threat-model prompts

- What can a compromised app container do with cluster-admin?
- What residual remains if PSS is restricted but RBAC is still cluster-admin?

## Lesson inventory (titles only)

See `module.yaml` learningObjects (LO-01–08).

## Lab briefs

Authorized local `labs/10.3/10.3-lab`. Forbidden: app pod granted cluster-admin. No live clusters.

## Assessment blueprint

See `module.yaml` assessmentBlueprint.

## Standards references

- NIST SP 800-190 (final, 2017-09-25): image / registry / orchestrator / container / host vocabulary — not an RBAC catalogue.
- Kubernetes Pod Security Standards and Pod Security Admission (stable): privileged / baseline / restricted profiles; namespace labels. Not RBAC. PodSecurityPolicy is obsolete.
- OWASP ASVS 5.0.0 (final): `v5.0.0-13.2.1` backend service accounts (Level 2); `v5.0.0-13.2.2` least privilege between components; `v5.0.0-13.2.4` outbound allowlist (IMDS hop). `v5.0.0-13.2.6` documented connection/retry for cluster API is **Level 3, labeled advanced**.

## Review triggers

App SA bound to cluster-admin; `privileged: true`; unlabeled namespaces; IaC `0.0.0.0/0`; IMDS reachable from app net.

## Time budget and SecureCollab

Evidence: threat-modeled deploy + local `pod_ok` tests. Feeds Gate 10 / M4 (not-attempted). Kubernetes is required as a *model*; production may be Cloud Run / ECS.

## Operational considerations

`cluster_admin_denied`. Rotate cluster credentials after a god-mode binding. Break-glass with E6.

## Changelog

| date | note |
|---|---|
| 2026-08-23 | Pass A specification (curriculum map complete) |
| 2026-09-06 | Depth pass: namespace-is-not-tenant; PSS ≠ RBAC; allowlist stand-in |
