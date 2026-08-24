# 3.3 — Secure architecture patterns (Review)

**Kind:** code-review  
**Loop step:** Review  
**Standards:** ASVS 5.0.0 V4/V13 (final); CISA Secure by Design (final guidance); Saltzer least privilege (1975, seminal).

## Property (start here)

The application DB role used by FastAPI must not SELECT another tenant’s rows even if a handler forgets a WHERE. Architecture is a second mediation, not a substitute for 1.2.

## Attacker capabilities and trust assumptions

- **Attacker:** Buggy handler; SQLi later (5.5/6.1); stolen app credentials.
- **Trust:** PostgreSQL RLS/role in the lab stand-in. The app still must mediate.
Review `labs/3.3/3.3-lab/vulnerable/` as a SecureCollab PR. Intended findings live only in `content/assessment/keys/3.3.md` — not here.

## What to label

For each claim and each branch: **property**, **mechanism**, or **false assurance**.

- Seeded smell (label it yourself): DATABASE_URL uses superuser
- Seeded smell (label it yourself): Comment “RLS later” in production path
- Seeded smell (label it yourself): Analytics role SELECT *
- Seeded smell (label it yourself): No test can_select(app, tB, tA) is False

Also reject: client trust, interpreter concatenation, Report-Only as enforcement, closing findings without retest, keys in lessons.

## Misconceptions

- Microservices are automatically isolated
- RLS replaces application authz
- Network VPC is tenant isolation

## Practice

Write three review notes. Do not open the keys file.

## Transfer

Serverless function with a shared “admin” connection string.
