function speakPromptTopic(rest: string): string {
  if (rest.startsWith("clinic, ")) {
    return `a clinic with ${rest.slice("clinic, ".length)}`;
  }
  if (rest.startsWith("clinic ")) {
    return `a clinic ${rest.slice("clinic ".length)}`;
  }
  if (rest === "clinic") {
    return "a clinic";
  }
  if (rest.startsWith("departing ") || rest.startsWith("React Native")) {
    return `a ${rest}`;
  }
  return rest;
}

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
  "What to look at — cause, not a trophy": "What to look at: the cause, not a hunt",
  "What to look at — cause, not a dump": "What to look at: the cause, not a hunt",
  "Signals that do not become a second leak": "Signals that should not become a second leak",
  "Step 2: write cells": "Step 2: write the rules",
  "Step 2: write cells the lab can fail": "Step 2: write the rules the check can fail",
  "Step 1: freeze pieces": "Step 1: name the pieces",
  "Step 1: freeze the pieces": "Step 1: name the pieces",
  "Step 1: freeze who, what, and time": "Step 1: name who, what, and when",
  "Step 1: freeze who, what, and the copy": "Step 1: name who, what, and the copy",
  "Step 1: freeze who, what, and the path": "Step 1: name who, what, and the path",
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
  if (text.startsWith("Step 1: freeze ")) {
    const rest = text.slice("Step 1: freeze ".length);
    if (rest === "pieces" || rest === "the pieces") {
      return "Step 1: name the pieces";
    }
    return `Step 1: name ${rest}`;
  }
  const promptHeading = text.match(/^Prompt(?: [AB])? — (.+)$/);
  if (promptHeading) {
    return `Write this for ${speakPromptTopic(promptHeading[1])}`;
  }
  if (text.startsWith("What to look at — cause, not a ")) {
    const rest = text.slice("What to look at — cause, not a ".length);
    if (rest === "dump" || rest === "trophy") {
      return "What to look at: the cause, not a hunt";
    }
    return `What to look at: the cause, not a ${rest}`;
  }
  if (text.startsWith("Mental model:")) {
    return `Picture:${text.slice("Mental model:".length)}`;
  }
  if (text.startsWith("Mental model")) {
    return `Picture${text.slice("Mental model".length)}`;
  }
  if (text.startsWith("Picture: fail closed on ")) {
    return `Picture: deny ${text.slice("Picture: fail closed on ".length)}`;
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
  t = t.replace(/\bpytest\b(?!-cov)/g, "the check");
  t = t.replace(
    /bound the export blast radius/gi,
    "limit how far an export break can spread",
  );
  t = t.replace(/attack-surface model/gi, "ways-in model");
  t = t.replace(/attack-surface/gi, "ways in");
  t = t.replace(/^the notes app risk register/i, "The notes app risk register");
  t = t.replace(/ is a browser cell/gi, " is a browser setting");
  t = t.replace(/ is not a 1\.2 cell/g, " does not pass who-is-allowed");
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
  let rest = text.slice(prefix.length).trim();
  if (!rest) {
    return null;
  }
  rest = rest.charAt(0).toUpperCase() + rest.slice(1);
  if (!/[.!?]$/.test(rest) && !/[.!?][”"]$/.test(rest)) {
    rest += ".";
  }
  return rest;
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
  [/The app['’]s promise is:\s*\*\*this\*\* practice,\s*/g, ""],
  [/The app['’]s promise is:\s*\*\*this\*\* helper,\s*/g, ""],
  [/The app['’]s promise is:\s*\*\*this\*\* check,\s*/g, ""],
  [/The app['’]s promise is:\s*\*\*these\*\* /g, ""],
  [/The app['’]s promise is:/g, ""],
  [/What this practice is supposed to show: \*\*this\*\* (?=`)/g, ""],
  [
    /, and Naming a product is not this week's rule\.?/g,
    ".",
  ],
  [
    /Broken must fail that question\. Repaired must pass it/g,
    "The broken files must fail that check",
  ],
  [
    /A (?:check|test) that only (.+?) can pass while (.+?)\. Ask whether .+?\. (?:The )?[Bb]roken files must fail that(?: question)?\. (?:The )?[Rr]epaired files must pass it/g,
    "A check that only $1 can still hide that $2",
  ],
  [/ The broken files have to fail that case\. The repaired files have to pass it\.?/g, ""],
  [/ is a \*\*what must not happen\*\* (?:check|test|pair): /g, " is there so "],
  [/ is not allowed to count as a pass/g, " still fails"],
  [/ cannot count as a pass/g, " still fails"],
  [/ cannot sneak through as /g, " does not pass as "],
  [/ cannot sneak through/g, " still fails"],
  [/Ask whether .+? still counts as a pass\. /g, ""],
  [/Ask whether .+? is allowed to count as a pass(?: for [^.]+)?\. /g, ""],
  [/You are here to see that the check treats/g, "Watch the check treat"],
  [/The point is to see that the check treats/g, "Watch the check treat"],
  [/You are here to see that/g, ""],
  [/The point is to see that/g, ""],
  [/still counts as a passing control/g, "still counts as a pass"],
  [/count as a passing control/g, "count as a pass"],
  [/\bwhat-must-not-happen\b/g, "what must not happen"],
  [/Practice checks live in /g, "The checks are in "],
  [/The checks live in /g, "The checks are in "],
  [/map-page row/g, "notes for this topic"],
  [/Attacker capability in this lab: /g, "Picture "],
  [/Who can act in this story: /g, "Picture "],
  [/Who can act here: /g, "Picture "],
  [/Who can act, in this story: /g, "Picture "],
  [/Who can act: /g, "Picture "],
  [/Who could do this: /g, "Picture "],
  [/Who you are standing in for: /g, "Picture "],
  [/What the attacker can do here: /g, "Picture "],
  [/What the attacker can do: /g, "Picture "],
  [/What an attacker can do here: /g, "Picture "],
  [/\. That stands in for /g, " — "],
  [/ That stands in for /g, " — "],
  [/What is supposed to stop this: /g, ""],
  [/What you are supposed to trust:/g, "What you trust:"],
  [/What you trust for this check:/g, "What you trust:"],
  [/Picture Anyone /g, "Picture anyone "],
  [/Picture Another /g, "Picture another "],
  [/Picture An /g, "Picture an "],
  [/Picture A /g, "Picture a "],
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
  [/This week's check is the one that covers /g, ""],
  [/If that call never includes /g, "If the change never checks "],
  [/If that loop never includes /g, "If the loop never checks "],
  [/Naming a product is not the rule\./g, ""],
  [/A ([A-Za-z0-9.+-]+) product name is not the rule\./g, ""],
  [/An ([A-Za-z0-9.+-]+) product name is not the rule\./g, ""],
  [/Do not add a live-([a-z-]+) trophy\./g, "Do not use a live $1 as the check."],
  [/Do not add a live ([A-Za-z]+) trophy\./g, "Do not use a live $1 as the check."],
  [/Do not add a native-overflow trophy\./g, "Do not treat a native overflow as a prize."],
  [
    /An environment error is not security evidence\./g,
    "A setup error is not proof the rule holds.",
  ],
  [
    /An environment error is not evidence\./g,
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
  [/a larger blast radius/gi, "more places a break can reach"],
  [/larger blast radius/gi, "more places a break can reach"],
  [/\battack surfaces?\b/gi, "ways in"],
  [/\bTop 10\b/g, "a famous-bugs list"],
  [/\bawareness lists?\b/gi, "famous-bugs lists"],
  [/\bthis origin\b/gi, "this website"],
  [/\bthe TCB\b/g, "what you trust"],
  [/\bTCB\b/g, "what you trust"],
  [/The local pytest analogue is /g, "The local check is "],
  [/ is that sentence for /g, " looks at "],
  [/This pytest is /g, "This check is "],
  [/This week's pytest is that sentence for /g, " — "],
  [/name the pytest cases/g, "name the checks"],
  [/name pytest cases/g, "name the checks"],
  [/The check below is that sentence for /g, " — "],
  [/\. This week's check covers /g, " — "],
  [/\. This week's check is about /g, " — "],
  [/\. This week's check looks at /g, " — "],
  [/The notes-app sentence was: /g, ""],
  [/On the notes app, /g, ""],
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
    /The answers are not on this page\. Do not open the keys file until someone has looked at your review\.\n?/g,
    "",
  ],
  [/Wait until someone has looked at your review before opening the keys\.\n?/g, ""],
  [/Rewrite the notes-app sentence\. Include:\n?/g, ""],
  [
    /Rewrite the notes-app sentence for this product\. Your answer must include:\n?/g,
    "",
  ],
  [/Rewrite the course sentence\. Include:\n?/g, ""],
  [/Write the same rule here\. Include:\n?/g, ""],
  [
    /Write three notes a (?:maintainer|peer) could act on, and tie at least one to (`[^`]+`)\. For each: what you saw, whether it is a rule or false assurance, a structural change, leftover(?: risk)? you will \*\*not\*\* delete\./g,
    "",
  ],
  [
    /Do not open the repaired files yet\. Diagnose the cause first\. Do not paste the public host into a browser or proxy\./g,
    "Do not paste the public host into a browser or proxy.",
  ],
  [/Do not open the repaired files yet\. (?:Diagnose|Name) the cause first\.\n?/g, ""],
  [
    /Write the review that blocks this change\. Mention (`[^`]+`)\./g,
    "",
  ],
  [
    /Your blocking review has to cite (`[^`]+`)\./g,
    "",
  ],
  [/Write the review that would block this change\. Name (`[^`]+`)\./g, ""],
  [/Run both this session from the lab directory if needed:\n?/g, ""],
  [/Run both this session from the lab directory if needed\. /g, ""],
  [/Run both this session from the practice folder if needed\. /g, ""],
  [/Run both this session:/g, ""],
  [/Run both this session\. /g, ""],
  [/Run both implementations this session from the lab directory if needed\. /g, ""],
  [/Run both implementations this session\. /g, ""],
  [/Execute both implementations this session from the lab directory if needed\. /g, ""],
  [/Run both versions this session\. /g, ""],
  [/ If both fail, the fix is not structural or the check is wrong\./g, ""],
  [/If both fail, the fix is not structural or the check is wrong\. /g, ""],
  [/Paste nothing from answer keys\. row\./g, ""],
  [/Paste nothing from answer keys\. /g, ""],
  [/Paste nothing from answer keys\./g, ""],
  [/ The failure \*is\* the evidence that the rule is currently false\./g, ""],
  [/ Neither reprints the body\./g, ""],
  [/Neither reprints the body\./g, ""],
  [/ Neither reprints [^.]+\./g, ""],
  [/not the check\. page\./g, "not the check."],
  [/This week['’]s freeze for the notes app: /g, ""],
  [/This week['’]s freeze: the notes app['’]s /g, ""],
  [/This week['’]s freeze: /g, ""],
  [/This week on the notes app: /g, ""],
  [/^This week: /g, ""],
  [/The notes app this week: /g, ""],
  [/The notes app this week /g, "The notes app "],
  [/This week['’]s rule is /g, "The rule is "],
  [/this week['’]s rule is /g, "the rule here is "],
  [/This week['’]s grain is /g, "The grain is "],
  [/This week['’]s check is /g, "The check is "],
  [/This week['’]s practice is /g, "The practice is "],
  [/\| Notes app this week \|/g, "| Notes app |"],
  [
    / is a notice-and-recover problem, not a licence to /g,
    " still has to be noticed. Do not ",
  ],
  [
    / is something you still have to notice and recover from, not an excuse to /g,
    " still has to be noticed. Do not ",
  ],
  [
    / still has to be noticed and recovered from — not an excuse to /g,
    " still has to be noticed. Do not ",
  ],
  [/in this week['’]s freeze/g, "in this week's practice"],
  [/Notes-app freeze: /g, ""],
  [/not a licence to scan /g, "not permission to scan "],
  [/as a licence to scan /g, "as permission to scan "],
  [/, not a legal label and not /g, ", not "],
  [/, not a legal label/g, ""],
  [/A legal label as the check/g, "A famous-bugs name as the check"],
  [/\. Practice files are in (`[^`]+`)\./g, " — files in $1."],
  [/The folder is (`[^`]+`)\./g, " — files in $1."],
  [/The practice folder is (`[^`]+`)\./g, " — files in $1."],
  [/The local check is (`labs\/[^`]+`)\./g, " — files in $1."],
  [/The local folder is (`labs\/[^`]+`)\./g, " — files in $1."],
  [/This week's check covers /g, ""],
  [/not a trophy against /g, "not an attack on "],
  [/not a trophy /g, "not a hunt "],
  [/, not a trophy/g, ", not a hunt"],
  [/not an eval trophy/g, "not an eval hunt"],
  [/Do not add a ([A-Za-z-]+) trophy\./g, "Do not use a $1 screenshot as the check."],
  [/The app['’]s promise this week is:\s*\*\*these\*\* local files, /g, ""],
  [/The (?:notes )?app['’]s promise this week is:\s*\*\*this\*\* practice, /g, ""],
  [/The app['’]s promise this week is:\s*\*\*this\*\* local check, /g, ""],
  [/The app['’]s promise this week is:\s*\*\*this\*\* /g, ""],
  [/The app['’]s promise in this practice: /g, ""],
  [/The app['’]s promise: /g, ""],
  [/sister cells/g, "related leftover"],
  [
    /Write one log line you would accept(?: in review)?(?: \(([^)]+)\))?\. Tie it to (`[^`]+`)\./g,
    "Sketch a deny line you would keep.",
  ],
  [/ Example shape \(fake (?:ids|routes) only\):/g, ""],
  [/ is not this (?:lesson|page)\. A [^.]+? names /g, " still has to name "],
  [/In (\u0000C\d+\u0000|`labs\/[^`]+`), mark (\u0000C\d+\u0000|`[^`]+`)\./g, "Start at $2 under $1."],
  [/Point at (`[^`]+`) file (`[^`]+`)\./g, "Start at $2 in $1."],
  [/Look in (`[^`]+`), starting with (`[^`]+`)\./g, "Start at $2 in $1."],
  [/Open (`[^`]+`) in (`labs\/[^`]+`)\./g, "Start at $1 in $2."],
  [/Label (`[^`]+`) in (`labs\/[^`]+`)\./g, "Start at $1 in $2."],
  [
    /Write down (.+?), allow or deny, and what would show the deny is false\./g,
    "Name $1 and the case that would prove the deny false.",
  ],
  [/\*\*Prompt:\*\* /g, ""],
  [/\*\*Product sketch:\*\* /g, ""],
  [/Product sketch: /g, ""],
  [/You do not need a ([^.]+) this week\./g, "You do not need a $1."],
  [/into the paging channel/g, "into the pager"],
  [/What has to be true first: /g, ""],
  [/\|\s*What has to be true first\s*\|/g, "| What's already wrong |"],
  [/ still has to be noticed\./g, " still has to page someone."],
  [/The notice should name /g, "Name "],
  [/The alert should name /g, "Name "],
  [/Recovery should /g, "Then "],
  [/You do not need a new [^.]+\.\n/g, "\n"],
  [/ \*is\* the leak/g, " is already the leak"],
  [/The leftover still returning /g, "The leftover "],
  [/ is already a broken rule, not /g, " is the break, not "],
  [/ is already a broken rule; /g, " is the break; "],
  [/Your artifact is a versioned list \(even a table in your notes\) with /g, "Write down "],
  [/\. The practice is an in-process (`[^`]+`)\./g, "."],
  [/Stay inside (`labs\/[^`]+`) — in-process `[^`]+`\. /g, "Stay inside $1. "],
  [/Stay inside (`labs\/[^`]+`) — in-process `[^`]+` with /g, "Stay inside $1. "],
  [/ is a tiny Python helper that /g, " "],
  [/ is a tiny Python helper\. The failure is already in the function: it /g, " "],
  [/ is a tiny Python helper\. The failure is already in the function: /g, ": "],
  [/ is a tiny Python helper\. /g, ". "],
  [/It is a tiny Python helper named (`[^`]+`)\. The failure is already in the function: /g, "$1: "],
  [/\. The failure is already in the functions?: it /g, ". It "],
  [/\. The failure is already in the functions?: /g, ": "],
  [/\. The failure is already in the (?:reader|dict|string): /g, ". "],
  [/(`[^`]+`) is local\. No /g, "$1 — no "],
  [/(`[^`]+`) is local\. /g, "$1 — "],
  [/The helper is an in-process /g, "The helper is "],
  [/The helper is in-process: /g, "The helper is "],
  [/The check is an in-process /g, "The check is "],
  [/The check is in-process /g, "The check is "],
  [/The maps are in-process: /g, "The files are "],
  [/The practice is in-process /g, "The practice is "],
  [/It is a tiny in-process /g, ""],
  [/For (?:\u0000C\d+\u0000|`[^`]+`), write a log line you would accept\./g, ""],
  [/For (?:\u0000C\d+\u0000|`[^`]+`), write a log line( \([^)]+\))/g, "Draft a deny line$1"],
  [/Write a log line( \([^)]+\))/g, "Draft a deny line$1"],
  [/Draw [^.]+ so someone else could name the checks\. ?/g, ""],
  [/Do not invent a new catalogue\./g, ""],
  [/Do not start a new list from scratch\. /g, ""],
  [/A vendor name is not this week's rule\. /g, ""],
  [/A vendor name is not this week's rule\./g, ""],
  [/Do not (use|follow|run) (.+?) (is|are) out of scope\./g, "Do not $1 $2."],
  [
    /A check that only counts passing (?:tests|cases|checks) can still look green while /g,
    "Passing tests can still miss that ",
  ],
  [
    /A (?:check|test) that only greps (.+?) can still look green while /g,
    "A grep for $1 can still hide that ",
  ],
  [/ can still look green while /g, " can still hide that "],
  [/If both pass, the (?:test|check) is not looking at /g, "Green on both sides does not prove you checked "],
  [/If both pass, you are not looking at /g, "Green on both sides does not prove you checked "],
  [
    /The test (\u0000C\d+\u0000) is there so always-(?:true|yes) (\u0000C\d+\u0000) still fails\./g,
    "$1 exists because $2 cannot always return true.",
  ],
  [
    /HTTP 200 on ([^.]+?) is the status, not ([^.]+)\./g,
    "A 200 from $1 does not prove $2.",
  ],
  [/This review is about notes-app /g, "This page reviews "],
  [
    /Review (\u0000C\d+\u0000) as a (?:change to|pull request for) [^.]+?\. Check whether /g,
    "Open $1. Does ",
  ],
  [
    /Review (\u0000C\d+\u0000) as a (?:change to|pull request for) [^.]+?\. Reconstruct whether /g,
    "Open $1. Reconstruct whether ",
  ],
  [
    /You are reviewing (?!a change that)([^.]+)\. Check whether /g,
    "This is a $1 review. Does ",
  ],
  [
    /Your job is to label each claim \*\*rule\*\*, \*\*tool\*\*, or \*\*false assurance\*\*, and to say whether /g,
    "Label each claim **rule**, **tool**, or **false assurance**. Say whether ",
  ],
  [/The smallest restore for the notes app[’']s /g, "For the notes app's "],
  [/The smallest restore for the notes-app /g, "For the notes-app "],
  [/The smallest restore for notes-app /g, "For "],
  [/The smallest restore for a notes-app /g, "For a "],
  [/The smallest restore for the notes app is:/g, "For the notes app:"],
  [/The smallest fix for /g, "For "],
  [/Do not fail open because /g, "Do not allow just because "],
  [/even in the repaired (?:tree|files) — the fix is /g, ". After repair, keep "],
  [/not pretending (.+) became (.+)\./g, "$1 is not $2."],
  [/The structural change is: /g, "The restore: "],
  [/Structural means /g, "In short, "],
  [
    /On the broken files it returns true\. On the repaired files it does not\./g,
    "Leftover still returns true; repair returns false.",
  ],
  [/Muting a scanner finding does not /g, "Hiding a scan result does not "],
  [/ is not the repair\./g, " does not close the leftover."],
  [
    /On \u0000C\d+\u0000 the helper returns true\. On \u0000C\d+\u0000 it returns false\./g,
    "Leftover still says yes; repair says no.",
  ],
  [
    /On the broken files the helper still returns true\. On the repaired files it does not\./g,
    "Leftover still says yes; repair says no.",
  ],
  [
    /On the broken files the helper returns true\. On the repaired files it returns false\./g,
    "Leftover still returns true; repair returns false.",
  ],
  [/On the repaired files it does not\./g, "Repair clears that leftover."],
  [
    /That is the cause\. (.+?) is a \*\*result\*\*, not the cause\./g,
    "That's why it broke. $1 is what showed up later.",
  ],
  [/Evidence that the deny is false: /g, "You can see the hole: "],
  [/The true return is already the leak of /g, "That true return already leaks "],
  [/^Last week['’]s /g, "Leftover "],
  [/The \*\*cause\*\* is (.+?); the \*\*cost\*\* is (.+?); \*\*how you stop it\*\* is (.+?); \*\*how you notice\*\* is (.+?); \*\*how you recover\*\* is (.+?)\./g,
    "Why it broke: $1. The damage is $2. Put $3 in the path. Watch $4. Recover by $5.",
  ],
  [/What the tool cannot do: this alert /g, "This alert "],
  [/What this alert cannot do: it /g, "It "],
  [/may pass on both sides\. You still have to /g, "can still look fine. Still need to "],
  [/Do not claim a course gate from ([^.]+)\./g, "That is not a check-in — $1."],
  [/Do not claim a course gate\./g, "This page does not finish a check-in."],
  [/Do not claim a course gate without /g, "A check-in still needs "],
  [/claiming a course gate;/g, "claiming this page as a check-in;"],
  [/A course gate\./g, "A check-in sticker."],
  [/\*\*The tool \(not the rule\):\*\* /g, "**Tools, not the rule:** "],
  [/Reject any line that includes /g, "Throw out a line that has "],
  [/Fail closed: if /g, "If "],
  [/Fail closed: on /g, "On "],
  [
    /Uncertainty is a \*\*deny\*\*, not a yes because /g,
    "A maybe is still no — not because ",
  ],
  [
    /Uncertainty is a \*\*no\*\*, not a yes because /g,
    "Don't treat that as a yes just because ",
  ],
  [
    /Uncertainty is a \*\*refuse\*\*, not a yes because /g,
    "Still a no, even when ",
  ],
  [
    /Uncertainty is a \*\*miss\*\*, not a yes because /g,
    "That is still deny, even if ",
  ],
  [
    /Uncertainty is a \*\*no\*\* on (.+?), not a yes because (.+)\./g,
    "Don't treat $1 as a yes just because $2.",
  ],
  [/Fail-safe: if /g, "If "],
  [/Do not skip the deny because /g, "Don't waive the deny just because "],
  [/Do not open the door because /g, "Don't open it just because "],
  [/Do not count it as a pass because /g, "Don't count a pass just because "],
  [/Do not allow just because /g, "Don't allow it just because "],
  [/4\. a check on /g, "4. run it on "],
  [/4\. a check idea on /g, "4. try this on "],
  [/6\. the web accessibility baseline if /g, "6. if "],
  [/By default: /g, "By default, "],
  [/Do not hide the gap behind /g, "Don't paper over the gap with "],
  [/In doubt, if /g, "If "],
  [/Unless you know otherwise, if /g, "If "],
  [/Do not accept a line that includes /g, "Don't keep a line with "],
  [/, dumping lab Python into notes/g, ""],
  [/ dumping lab Python into notes/g, ""],
  [/\. without product evidence\./g, "."],
  [/ without product evidence\./g, "."],
  [/Naming an ([^.]+?) product is not the rule\./g, "An $1 name does not finish this."],
  [/Naming a ([^.]+?) product is not the rule\./g, "A $1 name does not finish this."],
  [/The folder (`[^`]+`) is the change\./g, ""],
  [/Treat the files in (`[^`]+`) as the pull request\./g, ""],
  [
    /You already ran (\u0000C\d+\u0000)\. A (comment|banner) ([“"][^“”"]+[”"]) is not\./g,
    "$3 does not make $1 pass.",
  ],
  [
    /The check you already ran \((\u0000C\d+\u0000|`[^`]+`)\) is the rule (?:test|check)\./g,
    "$1 still has to fail.",
  ],
  [/You already ran (\u0000C\d+\u0000|`[^`]+`) — that is the rule\./g, "$1 still has to fail."],
  [
    /(\u0000C\d+\u0000) is the check\. [“"](?:Will |We should )[^“”"]+[”"] is a postponement\./g,
    "$1 still has to fail. A later ticket is not that fail.",
  ],
  [
    /(\u0000C\d+\u0000) is the check; [“"]will [^“”"]+[”"] is a postponement\./g,
    "$1 still has to fail. A later ticket is not that fail.",
  ],
  [/Notice names ([^.]+)\./g, "Name $1."],
  [/Name the event when you notice it\./g, "Name the event."],
  [/The ship gate stays not finished\./g, "This page does not finish the ship check-in."],
  [
    /Claiming you finished ([^.]+) from this page\./g,
    "This page does not finish $1.",
  ],
  [/The failure of (`[^`]+`) \*is\* the evidence\./g, ""],
  [/When (`[^`]+`) fails, that is the evidence\./g, ""],
  [/Here is the rule:/g, ""],
  [/The file is (`[^`]+`)\. /g, ""],
  [/The broken files take that path on purpose\. /g, ""],
  [/Name those places before you claim recover\./g, ""],
  [/Write fail\/pass into your notes next to[^.]*\. /g, ""],
  [/Write the fail\/pass pair next to[^.]*\. /g, ""],
  [/Write fail or pass next to [^.]+. /g, ""],
  [
    /Renaming “([^”]+)” to “([^”]+)” is not transfer\./g,
    "$2 here is the same kind of thing as $1.",
  ],
  [
    /Renaming "([^"]+)" to "([^"]+)" is not transfer\./g,
    "$2 here is the same kind of thing as $1.",
  ],
  [
    /Renaming (\u0000C\d+\u0000) to (\u0000C\d+\u0000) is not transfer\./g,
    "$2 here is the same kind of thing as $1.",
  ],
  [
    /Calling it “([^”]+)” instead of “([^”]+)” does not move the work\./g,
    "$1 here is the same kind of thing as $2.",
  ],
  [
    /Here, “([^”]+)” is still “([^”]+)” for this rule\./g,
    "$1 here is the same kind of thing as $2.",
  ],
  [
    /Here, "([^"]+)" is still "([^"]+)" for this rule\./g,
    "$1 here is the same kind of thing as $2.",
  ],
  [
    /Here, (\u0000C\d+\u0000) is still (\u0000C\d+\u0000) for this rule\./g,
    "$1 here is the same kind of thing as $2.",
  ],
  [/ Object, bad case, and leftover change\./g, ""],
  [/ Finding, map, and leftover change\./g, ""],
  [/ Field, place, and leftover change\./g, ""],
  [/ Threat, requirement, test, and leftover change\./g, ""],
  [/ Surfaces, threat-model id, and leftover change\./g, ""],
  [/ Expected digest, got digest, and leftover change\./g, ""],
  [/ Recovery evidence, log inventory, and leftover change\./g, ""],
  [/ Owner, grant, and leftover change\./g, ""],
  [/ Rule, allow-list, and leftover change\./g, ""],
  [/ Rule, retest, and leftover change\./g, ""],
  [/ Env, debug, and leftover change\./g, ""],
  [/ Person, object, reader, and leftover change\./g, ""],
  [
    /Honest (.+?) may pass on both implementations\. That does not excuse the (.+?)\./g,
    "$1 may pass on both sides. You still need the $2.",
  ],
  [
    /may pass on both implementations; that does not excuse the /g,
    "may pass on both sides; you still have to deny the ",
  ],
  [/One page\. No answer keys\. /g, "Keep the answer keys closed. "],
  [/One page\. No keys\. /g, "Keep the answer keys closed. "],
  [/Write one page\. Leave the answer keys closed\. /g, "Keep the answer keys closed. "],
  [/Write one page\. Leave the keys closed\. /g, "Keep the answer keys closed. "],
  [/Why it happens vs what it costs stays split here too: the /g, "The "],
  [
    /Why it happens, what it costs, how you stop it, how you notice, how you recover stays split here too: the /g,
    "The ",
  ],
  [/Cause vs cost stays split here too: the /g, "The "],
  [
    /[“"]([^“”"]+)[”"] is not evidence\. [“"]([^“”"]+)[”"] is a tool observation\. The check is:/g,
    "$1 does not finish this. $2 is only what a tool showed. Ask:",
  ],
  [
    /[“"]([^“”"]+)[”"] is not this topic['’]s evidence\. [“"]([^“”"]+)[”"] is a tool observation\. The check is:/g,
    "$1 does not finish this. $2 is only what a tool showed. Ask:",
  ],
  [
    /Searching for (.+) is not evidence\./g,
    "Looking up $1 does not finish this.",
  ],
  [
    /A denylist of yesterday['’]s (.+) is not the fix\./g,
    "A list of old $1 does not restore the rule.",
  ],
  [/Hiding a scanner warning is not the fix\./g, "Hiding a scan result does not restore the rule."],
  [
    /Do not weaken it to [“"]([^“”"]+)[”"]\./g,
    "Do not swap the failing test for “$1.”",
  ],
  [/- An assurance gate complete/g, "- This page does not finish a check-in"],
  [
    /A test that only greps (`[^`]+`) without calling (`[^`]+`) is not this topic['’]s evidence\./g,
    "Looking up $1 without calling $2 does not finish this.",
  ],
  [
    /A test that only greps (`[^`]+`) without (decoding|asserting|comparing) (`[^`]+`) is not this topic['’]s evidence\./g,
    "Looking up $1 without $2 $3 does not finish this.",
  ],
  [
    /Reject a [“"](?:test|check)[”"] that only greps (`[^`]+`) without calling (`[^`]+`)\./g,
    "Call $2. $1 is the string, not the call.",
  ],
  [
    /Reject a [“"](?:test|check)[”"] that only greps (`[^`]+`) without (decoding|asserting|comparing) (`[^`]+`)\./g,
    "Call $2 $3. $1 is the string, not the call.",
  ],
  [
    /Do not treat a grep for (.+) as the check\. Call (.+)\./g,
    "Call $2. $1 is the string, not the call.",
  ],
  [
    /Do not treat a live (.+) screenshot as proof\./g,
    "Do not use a live $1 screenshot as the check.",
  ],
  [
    /Do not attach (.+) to the ticket\./g,
    "Keep $1 out of the ticket.",
  ],
  [
    /Do not log ([^.]+)\. Leave ([^.]+) (?:off|out of) the ticket\./g,
    "Keep $1 and $2 out of the ticket.",
  ],
  [
    /Do not log ([^.]+)\. Do not paste ([^.]+) into the ticket\./g,
    "Keep $1 and $2 out of the ticket.",
  ],
  [/ after (\u0000C\d+\u0000) was repaired once(?=\.)/g, ""],
  [/ after (.+?) was repaired once(?=\.)/g, ""],
  [/ after (\u0000C\d+\u0000) was [“"]fixed once[.”"]+/g, "."],
  [/ after (.+?) was [“"]fixed once[.”"]+/g, "."],
  [/ after (\u0000C\d+\u0000) was [“"]set once[.”"]+/g, "."],
  [/ after (.+?) was [“"]set once[.”"]+/g, "."],
  [/ after (\u0000C\d+\u0000) was [“"]capped once[.”"]+/g, "."],
  [/ after (.+?) was [“"]capped once[.”"]+/g, "."],
  [
    /Buying a (.+?) does not ([^.]+)\. A badge that says ([^.]+) is not that check\./g,
    "A $1 does not $2.",
  ],
  [
    /Buying a (.+?) does not ([^.]+)\. A tile that says ([^.]+) is not that check\./g,
    "A $1 does not $2.",
  ],
  [
    /Buying a (.+?) does not ([^.]+)\. A clean-looking (?:line|report) is not that check\./g,
    "A $1 does not $2.",
  ],
  [
    /Buying a (.+?) does not ([^.]+)\. A schema screenshot is not that check\./g,
    "A $1 does not $2.",
  ],
  [
    /Buying a (.+?) does not ([^.]+)\. Ticking a checklist does not ([^.]+)\./g,
    "A $1 does not $2.",
  ],
  [/ A badge that says ([^.]+) is not that check\./g, ""],
  [/ A tile that says ([^.]+) is not that check\./g, ""],
  [/ Calling it an allow-list is not that check\./g, ""],
  [/A (.+) as the syllabus\./g, "Do not treat a $1 as the syllabus."],
  [/An (.+) as the syllabus\./g, "Do not treat an $1 as the syllabus."],
  [/Running it for real is the rest of the loop: /g, "Then "],
  [/ is not this sentence\./g, " is not the rule here."],
  [/ is not the fix\./g, " does not restore the rule."],
  [/as the check\. decoding /g, "as the check. Decode "],
  [/as the check\. asserting /g, "as the check. Assert "],
  [/as the check\. comparing /g, "as the check. Compare "],
  [
    /A clinic example: a (?:test|check|review) that only asserts /g,
    "Asserting ",
  ],
  [
    /A test that only asserts ([^.]+?) is not this topic['’]s evidence\. (?=Searching )/g,
    "",
  ],
  [
    /A test that only asserts HTTP 200 is not this topic['’]s evidence\./g,
    "HTTP 200 does not finish this.",
  ],
  [/\bA (?:test|check|review) that only asserts /g, "Asserting "],
  [
    /Asserting ([^\n]+?) is not this (?:topic|rule|check)((?: \([^)]+\))?)\./g,
    "$1 does not finish this$2.",
  ],
  [/ is 4\.4, not this rule\./g, " is 4.4, not this check."],
  [
    /A test that ([a-z][^.]*?) is out of scope\./g,
    "Do not run a test that $1.",
  ],
  [
    /A check that ([a-z][^.]*?) is out of scope\./g,
    "Do not run a check that $1.",
  ],
  [
    /A check against ([^.]*?) is out of scope\./g,
    "Do not run a check against $1.",
  ],
  [/A live vendor POST is out of scope\./g, "Do not send a live vendor POST."],
  [/A live broker attach is out of scope\./g, "Do not attach to a live broker."],
  [
    /A live Play Console call is out of scope\./g,
    "Do not make a live Play Console call.",
  ],
  [
    /A live web-crash call is out of scope\./g,
    "Do not make a live web-crash call.",
  ],
  [/A live fuzz call is out of scope\./g, "Do not make a live fuzz call."],
  [
    /A live governance scrape is out of scope\./g,
    "Do not run a live governance scrape.",
  ],
  [/A live pentest is out of scope\./g, "Do not run a live pentest."],
  [/A live ([^.]*?) is out of scope\./g, "Do not use a live $1."],
  [/A public ([^.]*?) is out of scope\./g, "Do not use a public $1."],
  [
    /A third-party binary is out of scope\./g,
    "Do not use a third-party binary.",
  ],
  [
    /A sideloaded malware APK is out of scope\./g,
    "Do not use a sideloaded malware APK.",
  ],
  [/Store APK unpacking is out of scope\./g, "Do not unpack a store APK."],
  [
    /Personal-phone imaging is out of scope\./g,
    "Do not image a personal phone.",
  ],
  [
    /Live GitHub and weaponized eval are out of scope\./g,
    "Do not use live GitHub or weaponized eval.",
  ],
  [
    /A (.+?) still has to show up as an alert\. Keep (.+?) out of the (pager|ticket)\. The alert should name (.+?)\. Then /g,
    "Name $4 for a $1. Leave $2 off the $3. Then ",
  ],
  [
    /An (.+?) still has to show up as an alert\. Keep (.+?) out of the (pager|ticket)\. The alert should name (.+?)\. Then /g,
    "Name $4 for an $1. Leave $2 off the $3. Then ",
  ],
  [
    /A (.+?) still has to show up as an alert\. Keep (.+?) out of the (pager|ticket)\. Then /g,
    "On a $1, leave $2 off the $3. Then ",
  ],
  [
    /An (.+?) still has to show up as an alert\. Keep (.+?) out of the (pager|ticket)\. Then /g,
    "On an $1, leave $2 off the $3. Then ",
  ],
  [
    /A (.+?) still has to show up as an alert\. Do not paste (.+?)\. The alert should name (.+?)\. Then /g,
    "Name $3 for a $1. Do not paste $2. Then ",
  ],
  [
    /A (.+?) still has to show up as an alert\. Do not paste (.+?)\. Then /g,
    "On a $1, do not paste $2. Then ",
  ],
  [/A (.+?) still has to show up as an alert\. /g, "On a $1, "],
  [/An (.+?) still has to show up as an alert\. /g, "On an $1, "],
  [
    /When you see a (.+?), name (.+?)\. Leave (.+?) off the (pager|ticket)\. Then /g,
    "Name $2 for a $1. Leave $3 off the $4. Then ",
  ],
  [
    /When you see an (.+?), name (.+?)\. Leave (.+?) off the (pager|ticket)\. Then /g,
    "Name $2 for an $1. Leave $3 off the $4. Then ",
  ],
  [
    /When you see a (.+?), leave (.+?) off the (pager|ticket)\. Then /g,
    "On a $1, leave $2 off the $3. Then ",
  ],
  [
    /When you see an (.+?), leave (.+?) off the (pager|ticket)\. Then /g,
    "On an $1, leave $2 off the $3. Then ",
  ],
  [/When you see a (.+?), /g, "On a $1, "],
  [/When you see an (.+?), /g, "On an $1, "],
  [/\*\*A tool is not the rule\.\*\* /g, ""],
  [/\*\*A tool is not the rule:\*\* /g, ""],
  [/\*\*A tool is not this sentence\.\*\* /g, ""],
  [/A tool is not the rule: /g, ""],
  [/A tool is not the rule\. /g, ""],
  [/The alert should name /g, "Name "],
  [/ — inventory them before you claim recover\./g, "."],
  [/ — inventory it before you claim recover\./g, "."],
  [/ — inventory them before claiming recover\./g, "."],
  [/ — inventory it before claiming recover\./g, "."],
  [/ — list them before you claim Recover\./g, "."],
  [
    /If your alert includes (.+?), the pager now has (.+?)\./g,
    "Putting $1 in the alert means the pager now has $2.",
  ],
  [
    /If your alert includes (.+?), the pager now holds (.+?)\./g,
    "Putting $1 in the alert leaves $2 in the pager.",
  ],
  [
    /If your alert includes (.+?), you have copied the leak into the ticket\./g,
    "Putting $1 in the alert copies the leak into the ticket.",
  ],
  [
    /If your alert includes (.+?), you have opened (.+?)\./g,
    "Putting $1 in the alert opens $2.",
  ],
  [/puts (.+) too in the pager\./g, "puts $1 in the pager too."],
  [/leaves (.+) too in the pager\./g, "leaves $1 in the pager too."],
  [/Read (`[^`]+`) against this checklist\./g, "Check $1 against the list above."],
  [/Claiming a course gate from this page\./g, "This page does not finish a check-in."],
  [/Do not treat a famous-bugs list as the definition of security\. /g, ""],
  [/Treating an awareness list as the definition of security\. ?/g, ""],
  [/A famous-bugs list as the definition of security\. /g, ""],
  [/An awareness list as the definition of security\. /g, ""],
  [/A [“"]top ten bugs[”"] list as the definition of security\. /g, ""],
  [
    /This page does not mark you as finished\. from this page\./g,
    "This page does not mark you as finished.",
  ],
  [
    /This page does not mark you as finished\. from a ([^.]+)\./g,
    "This page does not mark you as finished. A $1 is not a check-in.",
  ],
  [/on a \*\*local\*\* practice files/g, "on **local** practice files"],
  [/on a local practice files/g, "on local practice files"],
  [/a local practice files/g, "local practice files"],
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
  [/this week’s pytest/g, "this check"],
  [/\bthat pytest\b/gi, "that check"],
  [/\bthis pytest\b/gi, "this check"],
  [/\bthe pytest\b/gi, "the check"],
  [/\bpytest cases\b/gi, "checks"],
  [/\bpytest\b(?!-cov)/g, "the check"],
  [/\bthis cell is not\b/gi, "this rule is not"],
  [/This cell is/g, "This rule is"],
  [/\bthis cell\b/gi, "this rule"],
  [/\bthe cell\b/gi, "the rule"],
  [/of the same cell/g, "of the same rule"],
  [/\ba different cell\b/g, "a different rule"],
  [/A [A-Za-z0-9-]+-product name is not the rule/g, ""],
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
  [/\bthe lab oracle\b/gi, "what this local check looks at"],
  [/\bthe lab's oracle\b/gi, "what this check looks at"],
  [/\bthis lab's oracle\b/gi, "what this check looks at"],
  [/\boracle\b/gi, "check"],
  [/\bHITL\b/g, "a person in the loop"],
  [/\bElectives do not stamp them\.?/g, ""],
  [/\bAnswer keys are not in this file\.?/g, "Answer keys are not on this site."],
  [/\bAnswer keys stay out of (?:this file|lessons)\.?/g, "Answer keys are not on this site."],
  [/A comment ([“"][^“”"]+[”"]) is not a pass on /g, "$1 does not close "],
  [/A banner ([“"][^“”"]+[”"]) is not a pass on /g, "$1 does not close "],
  [
    /Do not merge by adding a comment ([“"][^“”"]+[”"])\. That comment is leftover(?: risk)? without an owner\./g,
    "Do not ship $1 as the merge. Name who owns that leftover.",
  ],
  [
    /Do not merge by adding a comment ([“"][^“”"]+[”"])\. That comment is a leftover without an owner\./g,
    "Do not ship $1 as the merge. Name who owns that leftover.",
  ],
  [/Do not merge by adding a comment ([“"][^“”"]+[”"])\./g, "Do not ship $1 as the merge."],
  [/Here, (.+?) is still this topic['’]s (.+?)\./g, "$1 here is the same job as $2."],
  [/that leftover path is still open\./g, "the old path still works."],
  [
    /A passing collection count is not this (?:check|rule)\./g,
    "A green suite count does not finish this.",
  ],
  [/, not at a scanner color or an? ([^.]+)\./g, ". A $1 can wait."],
  [/, not at a scanner color\./g, "."],
  [
    /Name the independent falsehood that would still keep /g,
    "What would still keep ",
  ],
  [
    /Name the independent falsehood that would still stop /g,
    "What would still stop ",
  ],
  [/Here, (.+?) is this topic['’]s (.+?)\./g, "$1 here is the same job as $2."],
  [/Here, (.+?) are this topic['’]s (.+?)\./g, "$1 here are the same job as $2."],
  [/ is an incomplete review of ([^.]+)\./g, " still misses $1."],
  [/ is an incomplete [a-z-]+ review\./g, " still misses that review."],
  [/ is an incomplete review\./g, " still misses the rule."],
  [/ is a skipped-check review\./g, " still skips the check."],
  [/ — list those before you [^.]+./g, "."],
  [/ — list it before you [^.]+./g, "."],
  [
    /An? (.+) product name is not the check\./g,
    "A $1 sticker does not finish this.",
  ],
  [
    / that bypass this practice will also bypass a [“"]scan our ([^”"]+)[”"] detector\./g,
    " still slip past a green $1.",
  ],
  [
    /This page does not finish an assurance gate(?: from this page)?\./g,
    "This page does not finish a check-in.",
  ],
  [
    /This page does not finish the verification gate\./g,
    "This page does not finish a check-in.",
  ],
  [
    /This page does not finish the ship gate\./g,
    "This page does not finish the ship check-in.",
  ],
  [/claiming an assurance gate/g, "claiming a check-in"],
  [/claiming the verification gate(?: is done)?/g, "claiming a check-in"],
  [/claiming the ship gate/g, "claiming a check-in"],
  [/[“"]assurance gate complete[”"]/g, "“check-in complete”"],
  [/[“"]verification gate complete[”"]/g, "“check-in complete”"],
  [/[“"]ship gate complete[”"]/g, "“check-in complete”"],
  [/\ban assurance gate\b/g, "a check-in"],
  [/\bthe verification gate\b/g, "the verification check-in"],
  [/\bthe ship gate\b/g, "the ship check-in"],
  [
    /The repaired files require ([^.]+)\. Production still needs /g,
    "Those files need $1. You still need ",
  ],
  [
    /The lab[’']s repaired files ([^.]+)\. Production still needs /g,
    "Those files $1. You still need ",
  ],
  [
    /The repaired files ([^.]+)\. Production still needs /g,
    "Those files $1. You still need ",
  ],
  [
    /Even after (\u0000C\d+\u0000) was repaired once, /g,
    "After $1 is green, ",
  ],
  [/Even after (.+?) was repaired once, /g, "After $1 is green, "],
  [
    /Even after (\u0000C\d+\u0000) was [“"]fixed once[,”"]+\s*/g,
    "After $1 is green, ",
  ],
  [/Even after (.+?) was [“"]fixed once[,”"]+\s*/g, "After $1 is green, "],
  [/Then page the /g, "Page the "],
  [/Then notice the /g, "Notice the "],
  [/ and refuse to [“"]help[”"] by /g, ", and do not "],
  [
    /Re-run (\u0000C\d+\u0000) after any ([^.]+) change\./g,
    "Keep $1 when $2 changes.",
  ],
  [
    /Re-run (\u0000C\d+\u0000) after any ([^.;]+) change;/g,
    "Keep $1 when $2 changes;",
  ],
  [/Also re-run (\u0000C\d+\u0000)/g, "Also keep $1"],
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
  // Leftover sketch labels ("Clinic SMS…") — do not match gold
  // "Clinic second factor that is mouse-only".
  if (/^Clinic (?=[A-Z`“"])/.test(line)) {
    line = line.replace(/^Clinic /, "");
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
  next = next.replace(/^local /, "Local ");
  next = next.replace(/^a local /, "A local ");
  next = next.replace(/Fail-safe: ([a-z])/g, (_, ch: string) => ch.toUpperCase());
  next = next.replace(/Fail-safe: /g, "");
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
  next = next.replace(/^A clinic example: ([a-z])(.*)$/g, (_, ch: string, rest: string) => `${ch.toUpperCase()}${rest}`);
  next = next.replace(/^A clinic example: /g, "");
  next = next.replace(/^Clinic: ([a-z])(.*)$/g, (_, ch: string, rest: string) => `${ch.toUpperCase()}${rest}`);
  next = next.replace(/^Clinic: /g, "");
  next = next.replace(/ Clinic: /g, " ");
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
