# 1.1-LO-07 — Transfer the method to a changed system

**Kind:** transfer-challenge  
**Loop step:** 7 Generalize  
**Gate 1 contribution:** define and justify security outcomes without using a tool, scanner, or vulnerability list as the definition.

## Why this is transfer, not repetition

Changing “notes” to “appointments” is not enough. A valid transfer case changes assets, actors, authority, trust, state, time, or harm. You must determine which SecureCollab reasoning survives and which must be rebuilt.

Do not target or research a real clinic or municipal system. Use only the synthetic product card below.

## Product card: CivicClinic appointments

A municipal service lets residents request clinic appointment slots.

- A resident can request, reschedule, or cancel their own appointment.
- Clinic staff confirm slots and record a short accessibility accommodation code.
- A guardian may act for a dependent after a relationship is established.
- SMS reminders are delivered by an external provider.
- A vendor calendar is embedded for staff scheduling.
- Some residents share phones or change phone numbers.
- During a regional emergency, capacity is scarce and the service may degrade.
- The design must avoid exposing whether a named person has an appointment.
- Real medical records are out of scope; all exercise data is synthetic.

## Changed assumptions to notice

Compared with SecureCollab Phase 1:

- guardians introduce delegated authority rather than simple tenant membership;
- shared phones weaken assumptions about possession and message confidentiality;
- SMS and the calendar vendor create third-party boundaries;
- appointment existence may itself be sensitive;
- accessibility accommodations create purpose and retention constraints;
- scarce capacity introduces fairness, automation, and availability harms;
- cancellation and rescheduling are time-dependent state transitions.

Do not treat this list as the answer. Use it to build the model.

## Deliverable

Produce at least six catalogue rows covering:

1. disclosure of appointment existence or accommodation data;
2. integrity of booking, cancellation, or rescheduling;
3. authenticity or authorization of guardian actions;
4. availability and abuse under scarce capacity;
5. accountability that does not over-collect resident information;
6. privacy or safety of reminders and recovery.

Each row must include the full claim envelope: attacker, trust, state/time, forbidden outcome, candidate mechanisms and limits, four evidence modes, detection/recovery, residual risk, non-goals, and review triggers.

## Comparison memo

Add a one-page comparison with three headings:

### Claims that transfer structurally

Identify SecureCollab reasoning patterns that still apply, such as hostile clients or the difference between control presence and outcome evidence. Explain the common structure.

### Claims that fail

Choose at least three SecureCollab assumptions or rows that cannot be copied. Name the changed asset, actor, authority relation, boundary, state transition, time horizon, or harm that breaks them.

### Claims that need stronger human factors

Explain how accessibility, shared devices, delegated action, stress, and recovery affect whether a technically enforced path is actually safe and usable.

## Constraints

- Do not organize the answer around OWASP Top 10, CWE, or named products.
- Do not use “encrypt,” “authenticate,” “rate-limit,” or “log” as a complete property.
- Do not assume SMS proves a person’s identity or private device possession.
- Do not declare universal thresholds or risk acceptance without context.
- Do not browse or probe a real service.
- Do not include answer keys in learner-facing material.

## Success criteria

A competent submission is system-specific and testable. A transfer-ready submission also:

- explains why at least three original SecureCollab claims fail to transfer;
- discovers a non-obvious conflict between properties;
- narrows a universal claim after modeling state or time;
- identifies a mechanism that supports one property but harms another;
- names evidence and residual risk without pretending the synthetic design is implemented.

The evaluator uses the isolated examiner notes and the learner-facing rubric. Completion of this prompt alone does not mark Gate 1 transfer-ready; satisfactory evidence is required.
