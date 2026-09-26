Vulnerable 3.1 fixture. Local only.

Two independent sinks -- an application log (`log_event`) and an
error/diagnostic dump (`write_error_dump`, reached when a note lookup fails)
-- both accept every field of the context dictionary they are given,
verbatim, regardless of the `CLASSIFICATION` table sitting unused at the top
of the file. The note body (Confidential) and the session token (an
authority artifact, also Confidential) both reach both sinks. A field this
fixture has never named at all (`X-Debug-Hint`) leaks exactly as readily,
because nothing here treats an unrecognized field as anything other than
"print it."
