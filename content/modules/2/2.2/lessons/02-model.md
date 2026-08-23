# 2.2-LO-02 — Request path and trust hops

**Kind:** design-exercise  
**Loop step:** 2 Model  

Draw DNS → TLS → optional CDN → app → DB. Mark where Host, scheme, client IP, and body can change. Place 1.2 tenant bind after termination, not in `X-Forwarded-For`.

## Practice

Which hop is allowed to set `X-Forwarded-Proto` in your diagram?
