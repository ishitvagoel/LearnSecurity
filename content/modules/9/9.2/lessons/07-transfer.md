# 9.2-LO-07 — Transfer: clinic eval in a report template

**Kind:** transfer-challenge
**Loop step:** 7 Transfer
**Standards:** OWASP ASVS 5.0.0 (final) `v5.0.0-1.3.2`. Code Review Guide v2 as guidance. SSDF 1.2 IPD remains **draft**.

## Change the workplace; keep eval off user input

Do not answer with a Top 10 / CWE / scanner as the definition of security. The SecureCollab sentence was: `review_ok("x = eval(user)")` must be false. Rewrite it for a clinic without changing the fork.

**Prompt:** Clinic eval in a report template. Also name Terraform `local-exec` and GitHub Actions yaml.

**Product sketch:** EHR-lite “designers can put expressions in the discharge template,” plus “CI formatted the file so we LGTM’d.”

Rewrite the SecureCollab sentence. Include:

1. attacker capabilities (template author / compromised designer — not a live clinic);
2. trust assumptions (review of interpreters is TCB; formatter LGTM is not);
3. forbidden outcome (`review_ok` true for eval-on-user, not “HIPAA”);
4. a test idea on a **local** fixture only (no weaponized eval);
5. residual (substring stand-in, `exec(`, generated templates, E1);
6. WCAG if a human block path exists (say “eval on user input,” not only a code).

## Mental model: same interpreter, clinical object

```mermaid
flowchart LR
  Tmpl[report template] --> Belief[designers need expressions]
  Eval[eval of field] --> Reality[patient field becomes code]
```

If designers “need expressions” while `review_ok` is always true, the cell is gone. Formatter CI, ruff, and “AI reviewed it” (9.4) do not ask the interpreter question. Terraform `local-exec` and Actions `run:` are the same interpreter family — name them, do not run those systems here. The lab substring is a stand-in, not a complete oracle.

The clinic rewrite still has to keep the SecureCollab fork: eval-on-user rejected, honest `int(user)` may pass. CI formatted the template without an interpreter question leaves `review_ok` true. The local pytest analogue is `test_eval_on_user_input_is_rejected` — on a fixture, not a live GitHub org.

## What graders reject

| Reject | Why |
|---|---|
| “Formatter passed” | Not an interpreter review |
| Weaponized eval / live GitHub | Lab policy |
| “AI reviewed it” | 9.4 is an aid, not 9.2 |
| Documented as dangerous, still merged | Level 3 `v5.0.0-15.1.5` is not reject |
| SSDF 1.2 certified | IPD draft; not Gate 9 |

## Practice

One page. No keys. `labs/9.2/9.2-lab` is the only running system you may break. Do not run eval on untrusted input.

## Non-goals

Weaponized eval. Live orgs. Claiming Gate 9 from this page.
