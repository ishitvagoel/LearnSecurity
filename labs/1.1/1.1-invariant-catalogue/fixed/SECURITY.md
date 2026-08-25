# Security claim structure

SecureCollab security is represented as a versioned catalogue of bounded invariants, not a universal conclusion.

The fixed catalogue identifies five Phase 1 properties: cross-tenant note confidentiality, authorized state-transition integrity, attributable membership changes, bounded shared-resource availability, and privacy-aware deletion/retention. Every row records attacker capabilities, trusted and untrusted components, time, forbidden outcomes, candidate mechanisms and their limits, four evidence modes, detection/recovery, residual risk, non-goals, and review triggers.

The catalogue does not claim that an implementation exists or that the listed mechanisms prove the properties. It is a reviewable model that later modules must implement and test. Cloud administrative access, distributed workers, production capacity, real personal data, and future assets remain explicit non-goals or review triggers.

See security_claim.yaml for the structured fixture and the lesson for the reasoning process.
