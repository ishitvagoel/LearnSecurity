# Module 1.1 lab — invariant catalogue under review

This lab teaches one narrow failure: a mechanism slogan is accepted as a security property. It uses local YAML and Markdown fixtures because SecureCollab product code does not exist in Phase 1.

## Authorized scope

Only files under this lab directory are in scope. Data is synthetic. Do not send requests to public, employer, classmate, or third-party systems. The vulnerable fixture contains a deliberately forbidden public URL as text so the validator can reject it; do not visit it.

## Security invariant

A submitted catalogue must contain bounded, system-specific claims that a reviewer can challenge. Each claim names assets, adversary capabilities, trust, state/time, forbidden outcomes, mechanisms and limits, four evidence modes, detection/recovery, residual risk, non-goals, and review triggers.

A valid catalogue is evidence of reviewable reasoning. It is not evidence that a SecureCollab implementation satisfies the claims.

## Root cause

The vulnerable document treats control names and a scanner result as proof that the whole product is secure. It omits the product model and proof obligations. Field presence alone would not repair the error, so the validator checks relationships and minimum semantic constraints as well as shape.

## Impact

False assurance can close design and review work while note confidentiality, membership integrity, accountability, availability, privacy, failure behavior, and recovery remain unspecified and untested.

## Structural fix

The fixed fixture:

- scopes the synthetic product and authorized lab;
- records at least five stable invariant claims;
- distinguishes property, mechanism, and mechanism limits;
- ties each claim to observable forbidden outcomes;
- requires normal, negative, abuse, and failure evidence;
- pairs prevention with privacy-safe detection and recovery;
- records residual risk, non-goals, and assumption-change triggers.

The validator is intentionally incomplete. It catches selected reasoning defects but cannot prove an application secure or replace independent review.

## Setup

Use Python 3.11 or newer in a disposable virtual environment:

```text
python -m venv .venv
. .venv/bin/activate
python -m pip install -r labs/1.1/1.1-invariant-catalogue/requirements.txt
```

On Windows PowerShell, activate the environment using its Scripts directory.

## Run the vulnerable and fixed pair

From the repository root:

```text
python -m pytest labs/1.1/1.1-invariant-catalogue/tests   --claim labs/1.1/1.1-invariant-catalogue/vulnerable/security_claim.yaml

python -m pytest labs/1.1/1.1-invariant-catalogue/tests   --claim labs/1.1/1.1-invariant-catalogue/fixed/security_claim.yaml
```

Expected result:

- vulnerable: the selected-catalogue test fails for the intended semantic and scope defects;
- fixed: all tests pass.

A missing package, bad path, or syntax error is an environment failure, not successful observation of the forbidden outcome.

## Learner workflow

1. Run the vulnerable fixture and group errors by property, model, evidence, operation, and safety.
2. Review vulnerable/SECURITY.md without reading the examiner key.
3. Draft a corrected claim before opening the fixed fixture.
4. Compare your draft with fixed/security_claim.yaml. Explain differences rather than copying.
5. Copy the fixed fixture to a temporary working file and remove one assumption, evidence mode, mechanism limit, or recovery step. Confirm the validator rejects what it can detect.
6. Record any semantic defect the validator misses as residual assurance risk.

## Detection and recovery

In the modeled product, detection plans must avoid note bodies, passwords, and tokens. If a false security claim has already influenced design, recovery means reopening affected requirements, identifying decisions that relied on the claim, revising tests and review triggers, and re-running independent review.

## Reset

The vulnerable and fixed directories are course fixtures. Do not edit them in place. Delete your temporary copy and virtual environment when finished. If a fixture was accidentally changed, restore only this lab directory from version control or re-download the repository; do not use a destructive repository-wide reset.

## Safety notes

- No exploit payloads or credentials are required.
- No network service is started.
- No real PII appears in fixtures.
- Examiner notes remain under content/assessment/keys and are not linked from the learner site.
- The --claim option can read a caller-selected local YAML path. That parser performs no network action, but the course authorization remains limited to this lab directory.
