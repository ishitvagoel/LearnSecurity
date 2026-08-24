# 1.2 assessment (learner-facing — no answers)

**Pass C (deepened).** Practical evidence, not a compensating average. States: not-attempted | developing | competent | transfer-ready.

## Evidence checklist

- [ ] Authority map and access matrix for SecureCollab Phase 1 (LO-02), including at least one indirect path marked
- [ ] Lab: `--impl vulnerable` fails `test_cross_tenant_read_is_denied`; `--impl fixed` passes the suite
- [ ] Forbidden-outcome table mapping matrix cells to tests (LO-05)
- [ ] Operate note: deny-log without note bodies (LO-06)
- [ ] Seeded review notes (LO-08) — do not look at keys
- [ ] Transfer matrix for impersonation or worker (LO-07) for transfer-ready

## Rubric (Gate 1 contribution)

| Result | Meaning |
|---|---|
| Developing | “Use JWT”; UI roles as the matrix; login = authorization |
| Competent | Testable matrix; lab understood; operate present; authentication ≠ authorization |
| Transfer-ready | LO-07 redraws principals without Top 10-as-definition |

Knowledge check (80% retryable): four short claims—property vs mechanism vs ambient authority. Items live in the session worksheet, not here.

## Seeded review

Use `vulnerable/notes.py` and `vulnerable/SECURITY.md`. Intended findings live only in `content/assessment/keys/1.2.md`.
