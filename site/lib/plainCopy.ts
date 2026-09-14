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
  if (text.startsWith("HITL")) {
    return "Can people still use it";
  }
  return text;
}

export function plainLessonTitle(title: string): string {
  let t = title.trim();
  t = t.replace(/^Local fixture:\s*/i, "Practice: ");
  t = t.replace(/^Somewhere new:\s*/i, "Same idea on ");
  t = t.replace(/^Transfer:\s*/i, "Same idea on ");
  t = t.replace(/ as a PR$/i, " like a pull request");
  t = t.replace(/^Review (.+) like a pull request$/i, "Would you merge this $1?");
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

const HIDDEN_LAB_NOTES = [
  /^live-target/i,
  /^real pii/i,
  /^awareness list used as the syllabus/i,
  /^weaponized/i,
];

/**
 * Lesson prose is authored for learners and should reach them unchanged.
 * Presentation belongs in the Markdown renderer; semantic rewrites here made
 * the source and the displayed lesson disagree. Legacy title helpers remain
 * available while headings are migrated to explicit display copy.
 */
export function plainLessonProse(source: string): string {
  return source;
}

/** Lab "what must not happen" lines, without internal curriculum notes. */
export function learnerFacingOutcomes(outcomes: string[] | undefined): string[] {
  return (outcomes || [])
    .filter((outcome) => !HIDDEN_LAB_NOTES.some((pattern) => pattern.test(outcome.trim())))
    .map((outcome) => outcome.trim())
    .filter(Boolean);
}
