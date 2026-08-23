# Security

## Property

Tenant A’s note bodies are not readable by Tenant B via the API, logs, or backups Tenant B can access.

## Mechanism (not the property)

User passwords are stored with a slow password hash. That supports a *password-at-rest* property. It does not imply note confidentiality.

## Attacker and trust

Hostile or merely logged-in client of another tenant; operator-readable logs. Client code is not in the TCB.
