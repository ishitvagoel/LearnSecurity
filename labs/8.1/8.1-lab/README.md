# Lab 8.1

Authorized: this directory only. No live targets.

SecureCollab must not grant a sensitive export because the Android client JSON says integrity is ok. Server attestation (lab token) is the TCB; the APK is hostile.

pytest tests/test_property.py --impl vulnerable (must fail) then --impl fixed.

Forbidden: client integrity=ok with failing server attest still exports.
