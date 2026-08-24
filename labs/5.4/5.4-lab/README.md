# Lab 5.4

Authorized: this directory only.

Client-supplied X-Forwarded-Proto=https is not proof of TLS. Channel binding uses the server's view of the connection.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: trusting X-Forwarded-Proto from the client.
