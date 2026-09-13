# Model the host check and stop condition

**Kind:** design-exercise
**Loop step:** 2 Model

For this local course, `target_is_authorized(url)` may allow `127.0.0.1`, `localhost`, and `lab.securecollab.test`. It must deny unknown or unparseable hosts. A redirect that leaves the list is a stop condition.

| Question | Answer to record |
|---|---|
| What do you trust? | The written host list and the parsed hostname |
| What can the learner control? | The URL, redirects, and request fields |
| What must not happen? | A public or unknown host is treated as in scope |
| What evidence matters? | Local allow and public deny tests |

A WSTG chapter is a method catalogue for an already-authorized application. NICE role language and a job title do not add a host to the list.

## Practice

Open `labs/0.1/0.1-orientation` and predict the result for a localhost URL and `https://example.com/` before running the tests. Do not open the public URL.
