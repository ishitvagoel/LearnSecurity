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
  Usability: "Can people still use it",
  "Usability and accessibility": "Can people still use it",
  "An invariant that cannot fail a test is still a slogan":
    "If you cannot test it, it is still a slogan",
  "What this is not": "What this is not",
  "The claim this module owns": "The rule",
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
