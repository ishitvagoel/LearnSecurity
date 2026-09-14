# Build the first invariant catalogue

**Kind:** design-exercise
**Loop step:** 2 Model

## Start with the system you are actually studying

SecureCollab is a small notes app used by more than one company. At this stage it is a model, not a deployed service. Name what matters before naming a control.

A useful catalogue row says:

| Field | Example |
|---|---|
| Asset | Note body and company membership |
| Subject and action | Current member reads a note body |
| Attacker capability | A signed-in member changes identifiers and request fields |
| Trust | Server-side policy and stored company relation; not the browser |
| State and time | Membership and grant are current at each read |
| Forbidden outcome | Company B receives any Company A note-body bytes |
| Evidence | Cross-company negative test and privacy-safe decision record |
| Leftover risk | Database administrator with a snapshot; reviewed later |

## Your task

Create five rows for confidentiality, integrity, availability, authorization, and accountability. Do not fill a row with a tool name. A reviewer should be able to invent a counterexample from your wording.

Use the local catalogue lab only. The lab checks the meaning and relationships between fields; passing YAML shape alone is not implementation evidence.

## Check yourself

Before moving on, underline the actor, action, object, trust assumption, time horizon, and forbidden outcome in each row. If any row says only “use TLS,” “use JWT,” or “log it,” rewrite it as an outcome.
