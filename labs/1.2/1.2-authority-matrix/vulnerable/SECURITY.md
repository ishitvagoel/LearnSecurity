# Intentionally vulnerable authority policy

This local course fixture treats identity and broad role labels as ambient authority. Some operations release or mutate objects without a current subject–object–action rule, current membership state, tenant-scoped administration, or a fail-safe unknown-action default. Its illustrative export decision also accepts approval without proving two distinct current scoped approvers.

The code is deliberately wrong. Do not reuse it in an application. Diagnose each decision against the Module 1.2 authority matrix before comparing the fixed tree.

The fixture contains only synthetic users, tenants, notes, and decision metadata. It performs no network, filesystem, process, credential, or production operation.
