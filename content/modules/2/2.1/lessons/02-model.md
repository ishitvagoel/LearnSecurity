# 2.1-LO-02 — Parser-boundary map (browser → API → DB)

**Kind:** design-exercise  
**Loop step:** 2 Model  

## Property (start here)

Where do bytes become a **tenant id** on the SecureCollab path?

Map: TLS bytes → HTTP body → FastAPI JSON → Pydantic → SQL parameter. Star every hop that can decode differently. Unicode normalization (NFC vs NFD) on display names is a later integrity issue.

## Practice

One diagram. Mark the lab’s two parsers on the same hop.

## Transfer

Add GraphQL: another grammar on the same objects (7.2).
