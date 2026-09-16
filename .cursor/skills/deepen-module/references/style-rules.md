# Style rules

Mechanical restatement of `lesson-prose.mdc`. When drafting, check against this list before running the linter.

1. **Every paragraph is ≥3 connected sentences.** No standalone noun phrases as paragraphs.
2. **Derive before you assert.** A rule sentence is preceded by the mechanism that makes it necessary. Ban `X is not Y.` standing alone.
3. **Define on first use in dual form, then use the real term.** `cross-site scripting (XSS)` → `XSS`. Never invent a circumlocution to avoid a term the industry uses.
4. **One scope statement per lesson**, immediately before the first command.
5. **At most three rejected alternatives**, each one full sentence with a reason.
6. **Every cross-reference is a titled link.** No bare `(2.3)`. No `(later)` without a destination.
7. **Tables carry data, not prose.** Causal chains belong in sentences.
8. **No undefined repository jargon** — `cell`, `grain`, `sticker`, `oracle`.
9. **Headings describe this lesson.** Only `## Practice` and `## Check yourself` may repeat verbatim across modules.
10. **Diagrams meet the minimums** in `lesson-prose.mdc` or become prose.

## Before and after

The defect, from `4.3/lessons/04-build.md`:

> localStorage JWT. Implicit grant. Magic-link standing session. TLS as the log control. HttpOnly as "not in the URL." A referrer policy as the parser.

Six noun phrases, no verbs, no reason given for any. A reader who did not already know why each is wrong learns nothing; a reader who did needed none of it.

The repair keeps at most three, and each earns a sentence:

> Two of these look like the same fix and are not. Storing the token in `localStorage` keeps it out of the URL, so it survives the access-log and `Referer` problem — but it hands the token to any script that runs on the page, which is a wider capability than the one we just closed. A `Referrer-Policy` header is narrower still: it stops the URL leaking *outward* to third parties, and does nothing about your own access logs, browser history, or a screenshot pasted into chat. Neither one changes what `session_from_request` accepts, which is where the rule actually lives.

Longer, and it teaches. The extra words are the derivation, not padding.

## Failure mode to avoid

Do not reach the word floor by restating the claim in new words. If a paragraph does not add a mechanism, a constraint, a consequence, or a worked case, cut it and write a different one. `L001` measures length; the reviewer measures whether the length carried reasoning, and the reviewer is the one that counts.
