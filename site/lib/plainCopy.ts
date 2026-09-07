function stripMarks(raw: string): string {
  return raw
    .replace(/\*\*/g, "")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .trim();
}

const HEADING_EXACT: Record<string, string> = {
  Practice: "Practice",
  "Non-goals": "What this page is not doing",
  Transfer: "Use it somewhere new",
  "Transfer hook": "Use it somewhere new",
  "Residual risk": "What can still go wrong",
  "Mechanism limits": "What the tool cannot do",
  "Root cause vs impact vs prevention vs detection vs recovery":
    "Why it happens, what it costs, how you stop it, how you notice, how you recover",
  "Root cause vs impact": "Why it happens, and what it costs",
  Usability: "Can people still use it",
  "Usability and accessibility": "Can people still use it",
  "HITL / WCAG 2.2": "Can people still use it",
  "An invariant that cannot fail a test is still a slogan":
    "Check it",
  "If you cannot test it, it is still a slogan":
    "Check it",
  "If you cannot check it, it is still a slogan":
    "Check it",
  "Until you can fail it, it is still a slogan":
    "Check it",
  "What this is not": "What this is not",
  "The claim this module owns": "The rule",
  "Start with the claim": "Start with the rule",
  "What graders reject": "What is not good enough",
  "What the tests do not prove": "What the checks do not prove",
  "Why this restores the cell": "Why this fix works",
  "Prevention is not absolute": "Fixing it once is not enough",
  "Stopping it is not enough": "Fixing it once is not enough",
  "Authorized scope": "Where you may practice",
  "What to read in the fixture": "What to read in the practice files",
  "Misconceptions this module refuses": "Common mix-ups",
  Misconceptions: "Common mix-ups",
  "Seeded smells (label them yourself)": "Problems to find (name them yourself)",
  "What to look at — cause, not a trophy": "What to look at: the cause, not a trophy",
  "Signals that do not become a second leak": "Signals that should not become a second leak",
  "Step 2: write cells": "Step 2: write the rules",
  "Step 2: write cells the lab can fail": "Step 2: write the rules the check can fail",
  "Step 1: freeze pieces": "Step 1: name the pieces",
  "Invariant prompts": "Questions to ask",
  "Threat-model prompts": "Who might attack, and how",
  "Lab briefs": "Practice files",
  "Assessment blueprint": "How you will show this",
  "Review triggers": "When to look again",
  "Operational considerations": "Running this for real",
  "Standards references": "Industry lists this page mentions",
  Changelog: "What changed",
  Identity: "Who this is about",
  "Lesson inventory (titles only)": "Pages in this topic",
  "Objective hierarchy": "What this topic is for",
  "Concept map": "The picture",
  "Prerequisite concepts": "What you should already know",
  "Time budget and SecureCollab": "Time and the notes app",
};

export function displayHeading(raw: string): string {
  const text = stripMarks(raw);
  const exact = HEADING_EXACT[text];
  if (exact) {
    return exact;
  }
  if (text.startsWith("Mental model:")) {
    return `Picture:${text.slice("Mental model:".length)}`;
  }
  if (text.startsWith("Mental model")) {
    return `Picture${text.slice("Mental model".length)}`;
  }
  if (text.startsWith("Framework defaults versus")) {
    return "What the framework does vs what you still have to check";
  }
  if (text.includes("what you still have a to check")) {
    return "What the framework does vs what you still have to check";
  }
  if (text.startsWith("Transfer:")) {
    return `Use it somewhere new:${text.slice("Transfer:".length)}`;
  }
  if (text.startsWith("Transfer ")) {
    return `Use it somewhere new: ${text.slice("Transfer ".length)}`;
  }
  if (/^Could someone else name pytest cases from your /i.test(text)) {
    return `Could someone else name the checks from your ${text.slice(
      "Could someone else name pytest cases from your ".length,
    )}`;
  }
  if (/^Can a second engineer name pytest cases from your /i.test(text)) {
    return "Could someone else name the checks from your notes?";
  }
  if (/^Can a second engineer turn your model into tests/i.test(text)) {
    return "Could someone else turn your picture into checks?";
  }
  if (/^Can a second engineer /i.test(text)) {
    return "Could someone else check this from your notes?";
  }
  if (text.startsWith("Three observations")) {
    return "Three things to look at";
  }
  if (text.startsWith("Four modes, even for")) {
    return "What the check has to show";
  }
  return text;
}

export function plainLessonTitle(title: string): string {
  let t = title.trim();
  t = t.replace(/^Local fixture:\s*/i, "Practice: ");
  t = t.replace(/^Somewhere new:\s*/i, "Same idea on ");
  t = t.replace(/^Transfer:\s*/i, "Same idea on ");
  t = t.replace(/^Review (.+) like a pull request$/i, "Would you merge this $1?");
  t = t.replace(/ as a PR$/i, " like a pull request");
  t = t.replace(
    /^Fail on the broken files, then pass on the repaired ones$/i,
    "The broken files must fail this check",
  );
  t = t.replace(
    /Fail-on-vulnerable then pass-on-fixed/gi,
    "The broken files must fail this check",
  );
  t = t.replace(/^attest_fail_export_denied without logging the APK$/i, "Log the deny, not the app file");
  t = t.replace(/^deeplink_identity_ignored without logging the URL$/i, "Log the dropped link, not the URL");
  t = t.replace(/^logout_wipes_cache without logging the body$/i, "Wipe the cache without logging the note");
  t = t.replace(/^debug_to_prod_denied without logging the APK$/i, "Log the deny, not the APK");
  t = t.replace(/^csp_report_only_not_enforced without logging HTML$/i, "Log that Report-Only is not enforcement, not the HTML");
  t = t.replace(/^field_denied without logging the secret$/i, "Log the denied field, not the secret");
  t = t.replace(/^unmapped_high_blocks without logging payloads$/i, "Block the unmapped HIGH without logging payloads");
  t = t.replace(/^merge_blocked_no_tm without logging bodies$/i, "Block the merge without logging the threat-model body");
  t = t.replace(/^revoked_share_read_denied without logging bodies$/i, "Log the revoked-share deny, not the note");
  t = t.replace(/^crash_body_redacted without logging the body$/i, "Redact the crash report without logging the note");
  t = t.replace(/^duplicate_capture_denied without logging PAN$/i, "Log the duplicate capture, not the card number");
  t = t.replace(/^tool_denied without logging transcripts$/i, "Log the denied tool, not the transcript");
  t = t.replace(/^body_tenant_mismatch without logging note bodies$/i, "Log the company mismatch, not the note");
  t = t.replace(/^finding_closed_without_retest without logging bodies$/i, "Notice a close without a retest, without logging notes");
  t = t.replace(/^security_suite_missing_isolation without logging bodies$/i, "Notice a missing isolation check, without logging notes");
  t = t.replace(/^unmapped_req_blocks_release without logging bodies$/i, "Block the release without logging notes");
  t = t.replace(/^worker_identity_wrong without logging the cookie$/i, "Log the wrong worker identity, not the cookie");
  t = t.replace(/^webhook_sig_fail without logging the body$/i, "Log the bad signature, not the body");
  t = t.replace(/^cluster_admin_denied without logging kubeconfig$/i, "Log the cluster-admin deny, not the kubeconfig");
  t = t.replace(/^incident_closed_without_recovery without logging bodies$/i, "Notice a close without recovery, without logging notes");
  t = t.replace(/^exception_incomplete_denied without logging secrets$/i, "Log the incomplete exception, not the secrets");
  t = t.replace(/^copy_length_denied without logging file bytes$/i, "Log the oversize copy, not the file bytes");
  t = t.replace(/^review_block_eval without logging the payload$/i, "Block eval in review without logging the payload");
  t = t.replace(/^hash_mismatch_denied without logging secrets$/i, "Log the hash mismatch, not the secrets");
  t = t.replace(/SecureCollab's/g, "the notes app's");
  t = t.replace(/\bthe SecureCollab\b/g, "the notes app");
  t = t.replace(/\bSecureCollab\b/g, "the notes app");
  t = t.replace(/\ban empty the notes app\b/g, "an empty notes-app");
  t = t.replace(/\bthe the notes app\b/g, "the notes app");
  t = t.replace(/Build the the notes app /g, "Build the notes app ");
  t = t.replace(/invariant catalogue/gi, "list of rules");
  t = t.replace(/\ban invariant\b/gi, "a rule");
  t = t.replace(/\binvariants\b/gi, "rules");
  t = t.replace(/\binvariant\b/gi, "rule");
  t = t.replace(/\ban rule\b/g, "a rule");
  t = t.replace(/forbidden outcomes/gi, "what must not happen");
  t = t.replace(/forbidden outcome/gi, "what must not happen");
  t = t.replace(/mechanism-only/gi, "tools-only");
  t = t.replace(
    /Break a tools-only security claim/g,
    "Watch a tools-only claim fail",
  );
  t = t.replace(
    / the smallest mechanism that restores a rule/g,
    " the smallest fix that restores a rule",
  );
  t = t.replace(/control presence/gi, "having a tool installed");
  t = t.replace(/incomplete mediation/gi, "skipped checks");
  t = t.replace(/ambient authority/gi, "leftover permission");
  t = t.replace(/ambient grants/gi, "leftover permission");
  t = t.replace(/mediate every/gi, "check every");
  t = t.replace(/\bGate (\d+)\b/g, "check-in $1");
  t = t.replace(/\bPhase (\d+)\b/g, "part $1");
  t = t.replace(/^Transfer the method to /i, "Use the same idea on ");
  t = t.replace(/^Use the same idea to /i, "Use the same idea on ");
  t = t.replace(/\bfixtures\b/gi, "practice files");
  t = t.replace(/\bfixture\b/gi, "practice files");
  t = t.replace(/out_of_scope/g, "out of scope");
  t = t.replace(/phase1_skip_denied/g, "do not skip part 1");
  t = t.replace(/\bpytest\b/g, "the check");
  t = t.replace(
    /bound the export blast radius/gi,
    "limit how far an export break can spread",
  );
  t = t.replace(/attack-surface model/gi, "ways-in model");
  t = t.replace(/attack-surface/gi, "ways in");
  t = t.replace(/^the notes app risk register/i, "The notes app risk register");
  t = t.replace(/ is a browser cell/gi, " is a browser setting");
  t = t.replace(/ is not a 1\.2 cell/g, " is not a pass on who-is-allowed");
  t = t.replace(/ is not a 1\.1 rule/g, " is not the original rule");
  t = t.replace(/\bthe TCB\b/g, "what you trust");
  t = t.replace(/\bTCB\b/g, "what you trust");
  t = t.replace(/^Seeded review of /i, "Review of ");
  t = t.replace(/always-true /g, "always-yes ");
  t = t.replace(/Revoke is mediation, not an event/g, "Revoke has to be checked, not just recorded");
  t = t.replace(/Architecture is a second mediation/g, "Architecture is a second check");
  t = t.replace(/Length is complete mediation of the buffer/g, "The copy must fit the box");
  t = t.replace(/Same what must not happen, same cell/g, "Same bad result, same rule");
  t = t.replace(/\bthis cell\b/gi, "this rule");
  t = t.replace(/\bthe cell\b/gi, "the rule");
  t = t.replace(/Require a named what must not happen/g, "Name what must not happen");
  t = t.replace(/What must not happen vs happy path/g, "The bad case vs the happy path");
  t = t.replace(/without back-dating check-in/g, "without pretending you already passed check-in");
  t = t.replace(/Diagnostics never grant 1\.2 or check-in 1/g, "A quiz never skips who-is-allowed or check-in 1");
  t = t.replace(/Tooling skip vs rule skip/g, "Skipping a tool is not skipping a rule");
  t = t.replace(/prod_debug_forbidden without logging traces/g, "Turn debug off without leaking logs");
  t = t.replace(/Refuse encoding as the confidentiality mechanism/g, "Encoding is not secrecy");
  t = t.replace(/A three-gate map a second engineer can test/g, "A three-check map someone else can test");
  t = t.replace(/A token for other-api is not a the notes app session/g, "A token for another API is not a notes-app login");
  t = t.replace(/A token for other-api is not a notes app session/g, "A token for another API is not a notes-app login");
  t = t.replace(/\bthe what you trust\b/g, "what you trust");
  t = t.replace(/\ban leftover\b/g, "a leftover");
  return t;
}

export function plainMechanismLead(text: string): string | null {
  const prefix = "**Mechanism (not the property):**";
  if (!text.startsWith(prefix)) {
    return null;
  }
  const rest = text.slice(prefix.length).trim();
  return rest ? `A tool is not the rule: ${rest}` : "A tool is not the rule.";
}

const PROSE_PHRASES: [RegExp, string][] = [
  [/\btrusted computing base\b/gi, "what you trust"],
  [/\bincomplete mediation\b/gi, "a skipped check"],
  [/\bcomplete mediation\b/gi, "checking every path"],
  [/\bfail-safe defaults\b/gi, "failing closed"],
  [/\bleast privilege\b/gi, "only the permission that is needed"],
  [/\bseparation of privilege\b/gi, "two independent checks"],
  [/\bThe forbidden outcomes? are therefore\b/g, "So what must not happen is"],
  [/\bThe forbidden outcome is\b/g, "What must not happen is"],
  [/\bThe forbidden outcomes are\b/g, "What must not happen:"],
  [/\bforbidden[- ]outcomes?\b/gi, "what must not happen"],
  [/\bresidual risks?\b/gi, "leftover risk"],
  [/\bSecureCollab Phase \d+\b/g, "the notes app at this stage"],
  [/\bSecureCollab's\b/g, "the notes app's"],
  [/\bthe SecureCollab\b/g, "the notes app"],
  [/\bSecureCollab\b/g, "the notes app"],
  [/\binvariant catalogues?\b/gi, "lists of rules"],
  [/\ban invariant\b/gi, "a rule"],
  [/\binvariants\b/gi, "rules"],
  [/\binvariant\b/gi, "rule"],
  [/\bmechanism-only\b/gi, "tools-only"],
  [/\bthe vulnerable tree\b/gi, "the broken files"],
  [/\bthe fixed tree\b/gi, "the repaired files"],
  [/\bLocal fixture\b/g, "Practice files"],
  [/\bthe fixture\b/gi, "the practice files"],
  [/\bfixtures\b/gi, "practice files"],
  [/\bfixture\b/gi, "practice files"],
  [
    /Gates 0[–-]10 and milestones M0[–-]M5 stay \*\*not-attempted\*\*\.?/g,
    "Opening this page does not finish a check-in.",
  ],
  [/Gates 0[–-]10 stay not-attempted\.?/g, "Opening this page does not finish a check-in."],
  [/Course gates stay not-attempted\.?/g, "This page does not finish a check-in."],
  [
    /Course gates stay unclaimed without learner or product evidence\.?/g,
    "This page does not finish a check-in.",
  ],
  [/Course gates stay unclaimed\.?/g, "This site does not mark you as finished."],
  [/Gates stay \*\*not-attempted\*\*\.?/g, "This page does not finish a check-in."],
  [
    /The verification gate stays not-attempted\.?/g,
    "This page does not finish the verification check-in.",
  ],
  [/Check-in 7 stays not finished\.?/g, "This page does not finish check-in 7."],
  [/Do not claim you finished an assurance gate\.?/g, "This page does not mark you as finished."],
  [/Claiming Gate \d+ from this page\.?/g, "This page does not finish a check-in."],
  [/Course gates from this page\.?/g, "This page does not finish a check-in."],
  [/\bGate (\d+)\b/g, "check-in $1"],
  [/\bPhase (\d+)\b/g, "part $1"],
  [/\bnot-attempted\b/g, "not finished"],
  [/The app['’]s promise is:\s*\*\*this\*\* practice,\s*/g, "What this practice is supposed to show: "],
  [/The app['’]s promise is:\s*\*\*this\*\* helper,\s*/g, "What this practice is supposed to show: "],
  [/The app['’]s promise is:\s*\*\*this\*\* check,\s*/g, "What this practice is supposed to show: "],
  [/The app['’]s promise is:\s*\*\*these\*\* /g, "What these files are supposed to show: "],
  [/The app['’]s promise is:/g, "What this practice is supposed to show:"],
  [/What this practice is supposed to show: \*\*this\*\* (?=`)/g, "What this practice is supposed to show: "],
  [
    /, and Naming a product is not this week's rule\.?/g,
    ". A vendor name is not this week's rule.",
  ],
  [
    /Broken must fail that question\. Repaired must pass it/g,
    "The broken files must fail that check",
  ],
  [
    /A (?:check|test) that only (.+?) can pass while (.+?)\. Ask whether .+?\. (?:The )?[Bb]roken files must fail that(?: question)?\. (?:The )?[Rr]epaired files must pass it/g,
    "A check that only $1 can still look green while $2",
  ],
  [/ The broken files have to fail that case\. The repaired files have to pass it\.?/g, ""],
  [/ is a \*\*what must not happen\*\* (?:check|test|pair): /g, " is there so "],
  [/ is not allowed to count as a pass/g, " cannot sneak through"],
  [/ cannot count as a pass/g, " cannot sneak through"],
  [/Ask whether .+? still counts as a pass\. /g, ""],
  [/Ask whether .+? is allowed to count as a pass(?: for [^.]+)?\. /g, ""],
  [/You are here to see that the check treats/g, "Watch the check treat"],
  [/The point is to see that the check treats/g, "Watch the check treat"],
  [/You are here to see that/g, "Watch for this: "],
  [/The point is to see that/g, "Watch for this: "],
  [/still counts as a passing control/g, "still counts as a pass"],
  [/count as a passing control/g, "count as a pass"],
  [/\bwhat-must-not-happen\b/g, "what must not happen"],
  [/Practice checks live in /g, "The checks live in "],
  [/map-page row/g, "notes for this topic"],
  [/Attacker capability in this lab:/g, "Who could do this:"],
  [/Who can act in this story:/g, "Who could do this:"],
  [/Who can act here:/g, "Who could do this:"],
  [/Who can act:/g, "Who could do this:"],
  [/What you are supposed to trust:/g, "What is supposed to stop this:"],
  [/What you trust for this check:/g, "What is supposed to stop this:"],
  [/What you trust:/g, "What is supposed to stop this:"],
  [/are not in what you trust for this rule\.?/g, "are not enough."],
  [/are not what you trust for this cell\.?/g, "are not enough."],
  [/are not what you trust for this rule\.?/g, "are not enough."],
  [/are not what you trust for this check\.?/g, "are not enough."],
  [/are not what you trust\.?/g, "are not enough."],
  [/Classification starts at the protected effect/g, "Keep the rule"],
  [/The review starts at the protected effect/g, "Keep the rule"],
  [/Review starts at the protected effect/g, "Keep the rule"],
  [/Hold onto the rule/g, "Keep the rule"],
  [/Hold onto this:/g, ""],
  [/Start with this seeded smell:/g, ""],
  [/Start with this seeded problem: /g, ""],
  [/\bseeded smell\b/gi, "first example"],
  [/\bfalse comfort\b/gi, "false assurance"],
  [
    /the same smell, not a different finding class/g,
    "still the same problem",
  ],
  [
    /the same problem, not a different kind of finding/g,
    "still the same problem",
  ],
  [/, not a different finding class/g, ""],
  [/Industry checklists want /g, ""],
  [/Industry lists want /g, ""],
  [/Industry lists ask for you to /g, "You need to "],
  [/Industry lists ask for /g, ""],
  [
    /Industry lists name detect, respond, recover\./g,
    "",
  ],
  [
    /Industry lists talk about noticing, responding, and recovering\./g,
    "",
  ],
  [
    /Someone still has to notice, respond, and recover\. That work does not /g,
    "Logging does not ",
  ],
  [/Someone still has to notice, respond, and recover\. /g, ""],
  [/Pair notice and recover\. /g, ""],
  [/Look at this first: /g, ""],
  [/Keep this: /g, ""],
  [/Don't just tally suspicious lines\. /g, ""],
  [/This week's check is the one that covers /g, "This week's check covers "],
  [/If that call never includes /g, "If the change never checks "],
  [/If that loop never includes /g, "If the loop never checks "],
  [/Naming a product is not the rule\./g, "A vendor name is not this week's rule."],
  [/A ([A-Za-z0-9.+-]+) product name is not the rule\./g, "A $1 name is not this week's rule."],
  [/An ([A-Za-z0-9.+-]+) product name is not the rule\./g, "An $1 name is not this week's rule."],
  [/Do not add a live-([a-z-]+) trophy\./g, "Do not treat a live $1 screenshot as proof."],
  [/Do not add a live ([A-Za-z]+) trophy\./g, "Do not treat a live $1 screenshot as proof."],
  [/Do not add a native-overflow trophy\./g, "Do not treat a native overflow as a prize."],
  [
    /An environment error is not security evidence\./g,
    "A setup error is not proof the rule holds.",
  ],
  [/Last topic \((\d+\.\d+)\) already said/g, "Topic $1 already said"],
  [
    /Module (\d+\.\d+) \/ (\d+\.\d+) already said/g,
    "Topics $1 and $2 already said",
  ],
  [/server-side 1\.2 cell/g, "server-side who-is-allowed check"],
  [/authority is a cell/g, "who-is-allowed is a rule"],
  [/the cell is gone/g, "the rule is gone"],
  [/opened a (\d+\.\d+) cell/g, "opened a leftover hole from topic $1"],
  [/\ba (\d+\.\d+) cell\b/g, "a leftover hole from topic $1"],
  [/\bambient authority\b/gi, "leftover permission"],
  [/\bblast radius\b/gi, "how far a break can spread"],
  [/\battack surfaces?\b/gi, "ways in"],
  [/\bTop 10\b/g, "a famous-bugs list"],
  [/\bawareness lists?\b/gi, "famous-bugs lists"],
  [/\bthis origin\b/gi, "this website"],
  [/\bthe TCB\b/g, "what you trust"],
  [/\bTCB\b/g, "what you trust"],
  [/The local pytest analogue is /g, "The local check is "],
  [/ is that sentence for /g, " covers "],
  [/This pytest is /g, "This week's check is "],
  [/This week's pytest is that sentence for /g, "This week's check covers "],
  [/name the pytest cases/g, "name the checks"],
  [/name pytest cases/g, "name the checks"],
  [/The check below is that sentence for /g, "This week's check covers "],
  [/The notes-app sentence was: /g, "On the notes app, "],
  [/The course sentence was: /g, "In this course, "],
  [/Do not answer with [^.]+ as the definition of security\. ?/g, ""],
  [
    / Label it (?:a )?(?:\*\*)?rule(?:\*\*)?, (?:a )?(?:\*\*)?tool(?:\*\*)?, or (?:\*\*)?false assurance(?:\*\*)? before you accept the change\./g,
    "",
  ],
  [/Person, object, path, and leftover change\. /g, ""],
  [/The untrusted \w+ changes\. The fork does not\. /g, ""],
  [/Rewrite it for a clinic: /g, "For a clinic, "],
  [/Rewrite it for a clinic\. /g, ""],
  [
    /The answers are not on this page\. Do not open the keys file until someone has looked at your review\./g,
    "Wait until someone has looked at your review before opening the keys.",
  ],
  [/Rewrite the notes-app sentence\. Include:\n?/g, ""],
  [
    /Rewrite the notes-app sentence for this product\. Your answer must include:\n?/g,
    "",
  ],
  [/Rewrite the course sentence\. Include:\n?/g, ""],
  [/Write the same rule here\. Include:\n?/g, ""],
  [
    /Write three notes a (?:maintainer|peer) could act on, and tie at least one to (`[^`]+`)\. For each: what you saw, whether it is a rule or false assurance, a structural change, leftover(?: risk)? you will \*\*not\*\* delete\./g,
    "Write the review that blocks this change. Mention $1.",
  ],
  [
    /Do not open the repaired files yet\. Diagnose the cause first\. Do not paste the public host into a browser or proxy\./g,
    "Do not paste the public host into a browser or proxy.",
  ],
  [/Do not open the repaired files yet\. (?:Diagnose|Name) the cause first\.\n?/g, ""],
  [/A log line a reviewer can accept looks like:\n?/g, ""],
  [
    /It must pass\. Run from the lab directory if (?:a )?collection at (?:the )?repo root is polluted\. ?/g,
    "",
  ],
  [
    /Then write one sentence: which rule is restored, and which leftover you refused to delete\.\n?/g,
    "",
  ],
  [/Do not define security as a famous-bugs list(?: item)?\. /g, ""],
  [/Record those as leftover or later topics, not as silent passes\. ?/g, ""],
  [
    /Write those down as leftover risk or later topics, not as silent passes\. ?/g,
    "",
  ],
  [/Watch for this: /g, ""],
  [/this week’s pytest/g, "this week's check"],
  [/\bthat pytest\b/gi, "that check"],
  [/\bthis pytest\b/gi, "this check"],
  [/\bthe pytest\b/gi, "the check"],
  [/\bpytest cases\b/gi, "checks"],
  [/\bpytest\b/g, "the check"],
  [/\bthis cell is not\b/gi, "this rule is not"],
  [/This cell is/g, "This rule is"],
  [/\bthis cell\b/gi, "this rule"],
  [/\bthe cell\b/gi, "the rule"],
  [/of the same cell/g, "of the same rule"],
  [/\ba different cell\b/g, "a different rule"],
  [/A [A-Za-z0-9-]+-product name is not the rule/g, "A vendor name is not this week's rule"],
  [/Naming a ([AaEeIiOoUu])/g, "Naming an $1"],
  [/Naming a (R8|API|MDM)\b/g, "Naming an $1"],
  [/\*\*different cell\*\*/g, "**different rule**"],
  [/the same cell/g, "the same rule"],
  [/deny cell/g, "deny rule"],
  [/Map each check to a cell/g, "Map each check to a rule"],
  [/\bpolicy cell\b/gi, "policy rule"],
  [/\bexecutable (?:policy )?cells?\b/gi, "rules you can test"],
  [/\bOWASP ASVS 5\.0\.0 \(final\)/g, "the published web-security checklist"],
  [/\bASVS 5\.0\.0\b/g, "the published web-security checklist"],
  [/\bASVS\b/g, "the published checklist"],
  [/\bMASVS\b/g, "the phone-app checklist"],
  [/\bWSTG\b/g, "the testing guide"],
  [/\bLO-\d+\b/g, "a later page"],
  [/\bWhat graders reject\b/g, "What is not good enough"],
  [/\bthe lab's oracle\b/gi, "what this check looks at"],
  [/\bthis lab's oracle\b/gi, "what this check looks at"],
  [/\boracle\b/gi, "check"],
  [/\bHITL\b/g, "a person in the loop"],
  [/\bElectives do not stamp them\.?/g, ""],
  [/\bAnswer keys are not in this file\.?/g, "Answer keys are not on this site."],
  [/\bAnswer keys stay out of (?:this file|lessons)\.?/g, "Answer keys are not on this site."],
];

const HIDDEN_LAB_NOTES = [
  /^live-target/i,
  /^real pii/i,
  /^awareness list used as the syllabus/i,
  /^weaponized/i,
];

function keepInlineCode(inner: string): boolean {
  if (/^v\d+\.\d+\.\d+-/.test(inner)) {
    return false;
  }
  if (/^LO-\d+$/i.test(inner)) {
    return false;
  }
  return true;
}

function transformProseLine(line: string): string {
  if (line.startsWith("#")) {
    return line;
  }
  const codes: string[] = [];
  const withPlaceholders = line.replace(/`([^`]+)`/g, (match, inner: string) => {
    if (!keepInlineCode(inner)) {
      return "";
    }
    codes.push(match);
    return `\u0000C${codes.length - 1}\u0000`;
  });
  let next = withPlaceholders;
  for (const [pattern, replacement] of PROSE_PHRASES) {
    next = next.replace(pattern, replacement);
  }
  next = next.replace(/you still have a to /g, "you still have to ");
  next = next.replace(/\bthe the notes app\b/g, "the notes app");
  next = next.replace(/\ban empty the notes app\b/g, "an empty notes-app");
  next = next.replace(/\ban rule\b/g, "a rule");
  next = next.replace(/\ban leftover\b/g, "a leftover");
  next = next.replace(/\bthe what you trust\b/g, "what you trust");
  next = next.replace(/\bThe practice files is\b/g, "The practice is");
  next = next.replace(/\bThis practice files is\b/g, "This practice is");
  next = next.replace(/\bthat the check\b/g, "that check");
  next = next.replace(/\bthis the check\b/g, "this check");
  next = next.replace(/^Clinic: /g, "A clinic example: ");
  next = next.replace(/\s{2,}/g, " ");
  next = next.replace(/ \(Level \d+\)/g, "");
  return next.replace(/\u0000C(\d+)\u0000/g, (_, index) => codes[Number(index)] ?? "");
}

/** Reword template jargon in lesson prose. Leaves headings and fenced code alone. */
export function plainLessonProse(source: string): string {
  const chunks = source.split(/(```[\s\S]*?```)/);
  return chunks
    .map((chunk) => {
      if (chunk.startsWith("```")) {
        return chunk;
      }
      return chunk
        .split("\n")
        .map((line) => transformProseLine(line))
        .join("\n");
    })
    .join("");
}

/** Lab "what must not happen" lines, without internal curriculum notes. */
export function learnerFacingOutcomes(outcomes: string[] | undefined): string[] {
  return (outcomes || [])
    .filter((outcome) => !HIDDEN_LAB_NOTES.some((pattern) => pattern.test(outcome.trim())))
    .map((outcome) => transformProseLine(outcome).trim())
    .filter(Boolean);
}
