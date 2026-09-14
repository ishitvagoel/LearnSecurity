# Break, repair, and verify the local host gate

**Kind:** mechanism-lab
**Loop step:** 3 Break · 4 Build · 5 Verify

Work only in `labs/0.1/0.1-orientation`. The vulnerable helper treats every URL as authorized. The fixed helper parses the hostname and compares it with the local allow-list.

```text
python3 -m pytest labs/0.1/0.1-orientation/tests --impl vulnerable
python3 -m pytest labs/0.1/0.1-orientation/tests --impl fixed
```

The broken run must fail the public-host deny assertion. The fixed run must allow the honest localhost case and deny `example.com`. A test string is enough; never send a request to the public host.

**Feedback:** if both implementations pass, the assertion is not exercising the property. If the fixed version allows every string, the mechanism is still a comment rather than a boundary check. If a setup error occurs, it is an environment problem rather than proof of the rule.

## Practice

Write the smallest repair in your own words: parse the host, allow only named local hosts, and fail closed when the host is missing or unknown. Then record one leftover risk, such as a redirect chain or hosts-file alias.
