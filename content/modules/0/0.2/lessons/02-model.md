# 0.2 — Diagnostic and adaptive bridge (2 Model)

**Kind:** design-exercise  
**Loop step:** 2 Model  
**Standards:** NICE Secure Systems Development competencies (informative); this course’s Gate 1 evidence rules. A quiz vendor’s score report is not ASVS.

## Property (start here)

A placement quiz score of 100 does not skip 1.2 complete mediation, Gate 1 evidence, or the authority matrix. Adaptive paths may skip *orientation prose*, never *invariants*.

## Attacker capabilities and trust assumptions

- **Attacker:** A hurried learner optimizing for the shortest click-path; a future hiring manager who equates a badge with tenant isolation.
- **Trust:** The diagnostic repository is local and honest. Quiz items are not production secrets.
Name principals, objects, actions, channels, TCB vs untrusted, and time. Open design: the client, APK, model, or prompt is hostile.

| Piece | This system |
|---|---|
| Subjects | Learner, diagnostic scorer, Gate 1 reviewer |
| Objects | Quiz result, 1.2 matrix artifact, Gate 1 packet |
| Actions | Skip, remediate, attest |
| Channels | Course site, local git |
| TCB | diagnostic.py skip rule in labs/0.2/0.2-bridge |
| Untrusted | Self-attestation, LMS percentage, LinkedIn badge |
| State / time | Score is a moment; Gate 1 is evidence over time. |
| 1.1 cell | Integrity of the learning system: false competency is a safety defect for later labs. |

## Authority matrix (minimum)

| Subject | Object | Action | Decision |
|---|---|---|---|
| learner | 1.2 lab | skip | deny |
| learner | 0.1 prose | skip-if-known | allow |
| learner | Gate 1 packet | attest-by-quiz | deny |
| reviewer | evidence pack | sign | allow-if-artifacts |

A missing cell is how ambient authority appears. If a handler, cache, worker, or mobile cache is not in the matrix, write it as a hole.

## Practice

Draw this map so a second engineer could name pytest cases. Lab fixture: `labs/0.2/0.2-bridge` file `diagnostic.py`.

## Transfer

A vendor SANS/OSCP score used to skip your team’s threat-model review.

## Residual risk

Bridge units still needed for Git/SQL/HTTP gaps — those skips are OK when diagnostics show skill.

## Non-goals

Do not answer with a Top 10 item as the definition of security. Keys stay out of lessons.
