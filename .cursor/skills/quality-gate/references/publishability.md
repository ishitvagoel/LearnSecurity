# Semantic publishability rubric

Score each dimension 0–3 and cite evidence.

| Dimension | 0 — absent or false | 1 — present by label | 2 — teachable and specific | 3 — transferable and diagnostic | Critical |
|---|---|---|---|---|---|
| Property and question | Topic or tool name | Generic property slogan | This-system invariant with forbidden outcome | Learner can revise it after assumptions change | yes |
| Attacker, authority, trust, state, and time | No model | Actors named without capabilities or boundaries | Capabilities, trusted components, state, and horizon constrain the claim | Model predicts a non-obvious failure and review trigger | yes |
| Causal explanation | Lists controls or symptoms | Mentions cause and fix | Separates root cause, preconditions, impact, prevention, detection, and recovery | Compares plausible alternatives and explains mechanism limits | yes |
| Worked reasoning | None | One unexplained example | At least one traced example and one counterexample | Multiple representations expose a misconception | no |
| Practice and feedback | Read-only prose | Reflection prompt with no success criteria | Guided practice plus rubric or feedback path | Fading scaffold prepares independent performance | no |
| Safe executable lab | Missing or decorative | Runs but tests syntax/keywords only | Vulnerable fails and fixed passes on a module-specific forbidden outcome | Failure cases show why the structural fix works and where it stops | yes |
| Assessment alignment | Presence checklist | Recall dominates | Outcomes map to practical evidence; critical gaps cannot compensate | Transfer case distinguishes memorization from model use | yes |
| Standards accuracy | Unversioned name drop | Version/status present but mapping vague | Exact identifiers or exact named principles support the claim | Limits, drafts, migrations, and non-applicability are explicit | yes |
| Operations and human factors | Prevention only | Logs or recovery named | Useful signals, privacy-safe evidence, response, recovery, and usable journey | Failure of operators or recovery paths is modeled as residual risk | no |
| Transfer and review triggers | Same scenario repeated | New nouns, same assumptions | Materially changed assets, actors, boundary, or time horizon | Learner explains which original claims break and why | yes |
| Safety and scope | Ambiguous target/data | Local-only statement | Authorized scope, synthetic data, isolation, reset, and no live-target path | Safety constraints are tested or structurally enforced | yes |
| Editorial integrity | Generator or author self-approval | Reviewer field with no evidence | Dated independent record cites files and test results | Review finds and closes a substantive issue with traceability | yes |

## Decision rules

- 0–1 means developing for that dimension.
- 2 is the minimum publishable score.
- 3 is not required for publication and should be uncommon.
- Any critical dimension below 2 blocks depth publishable.
- N/A is allowed only when the artifact is deliberately out of scope for the current pass. It is not allowed to claim publishable depth.
- Generated prose, file presence, schema validity, word count, and successful happy-path tests never substitute for the semantic evidence above.
- A mechanism-slogan YAML file is not a lab unless its educational property is specifically the quality of a security claim and its tests check meaning beyond field presence.
