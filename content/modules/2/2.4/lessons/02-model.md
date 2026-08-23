# 2.4-LO-02 — Share/invite state machine

**Kind:** design-exercise  
**Loop step:** 2 Model  

States: requested, done, timed-out-unknown. Transitions: retry with same key, retry with new key. Mark TOCTOU between “check if shared” and “insert share.”

## Practice

Where would a lock or idempotency store live (1.3)?
