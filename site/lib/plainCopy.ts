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
    "If you cannot test it, it is still a slogan",
  "What this is not": "What this is not",
  "The claim this module owns": "The rule",
  "Start with the claim": "Start with the rule",
  "What graders reject": "What is not good enough",
  "What the tests do not prove": "What the checks do not prove",
  "Why this restores the cell": "Why this fix works",
  "Prevention is not absolute": "Stopping it is not enough",
  "Authorized scope": "Where you may practice",
  "What to read in the fixture": "What to read in the practice files",
  "Misconceptions this module refuses": "Common mix-ups",
  Misconceptions: "Common mix-ups",
  "Seeded smells (label them yourself)": "Problems to find (name them yourself)",
  "Step 2: write cells": "Step 2: write the rules",
  "Step 2: write cells the lab can fail": "Step 2: write the rules the check can fail",
  "Step 1: freeze pieces": "Step 1: name the pieces",
  "Invariant prompts": "Questions to ask",
  "Threat-model prompts": "Who might attack, and how",
  "Lab briefs": "Practice notes",
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
  if (text.startsWith("Transfer:")) {
    return `Use it somewhere new:${text.slice("Transfer:".length)}`;
  }
  if (text.startsWith("Transfer ")) {
    return `Use it somewhere new: ${text.slice("Transfer ".length)}`;
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
  if (text.startsWith("HITL")) {
    return "Can people still use it";
  }
  return text;
}

export function plainLessonTitle(title: string): string {
  let t = title.trim();
  t = t.replace(/^Local fixture:\s*/i, "Practice: ");
  t = t.replace(/^Transfer:\s*/i, "Somewhere new: ");
  t = t.replace(/ as a PR$/i, " like a pull request");
  t = t.replace(
    /Fail-on-vulnerable then pass-on-fixed/gi,
    "Fail on the broken files, then pass on the repaired ones",
  );
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
  [/\bGate (\d+)\b/g, "check-in $1"],
  [/\bPhase (\d+)\b/g, "part $1"],
  [/\bnot-attempted\b/g, "not finished"],
  [/\bambient authority\b/gi, "leftover permission"],
  [/\bblast radius\b/gi, "how far a break can spread"],
  [/\battack surfaces?\b/gi, "ways in"],
  [/\bTop 10\b/g, "a famous-bugs list"],
  [/\bawareness lists?\b/gi, "famous-bugs lists"],
  [/\bthis origin\b/gi, "this website"],
  [/\bthe TCB\b/g, "what you trust"],
  [/\bTCB\b/g, "what you trust"],
  [/\bthis pytest\b/gi, "this check"],
  [/\bthe pytest\b/gi, "the check"],
  [/\bpytest cases\b/gi, "checks"],
  [/\bpytest\b/g, "the check"],
  [/\bthis cell is not\b/gi, "this rule is not"],
  [/\bthis cell\b/gi, "this rule"],
  [/\bthe cell\b/gi, "the rule"],
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
  next = next.replace(/\bthe the notes app\b/g, "the notes app");
  next = next.replace(/\ban empty the notes app\b/g, "an empty notes-app");
  next = next.replace(/\ban rule\b/g, "a rule");
  next = next.replace(/\ban leftover\b/g, "a leftover");
  next = next.replace(/\bthe what you trust\b/g, "what you trust");
  next = next.replace(/\bThe practice files is\b/g, "The practice is");
  next = next.replace(/\bThis practice files is\b/g, "This practice is");
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
