Vulnerable 3.2 fixture. Local only.

`evaluate_gate` reads one field of the CI request — `scanner_green` — and,
when it is `True`, returns `pass` without ever opening the stored
threat-model document. The three always-name threats, the required-flow
list, review triggers, and priority/mitigation fields all sit in the
stored model unread. A model missing `cross-tenant-read` entirely, a model
whose diagram never traces the worker-redelivery path, and a model whose
`new-share-path` trigger fired eleven sprints ago with no row ever
revisited all gate green, identically, as long as the scanner is green.
