import { displayHeading, plainLessonTitle } from "./plainCopy";

export type TocHeading = {
  id: string;
  text: string;
  level: 2 | 3;
};

export type LessonLead = {
  title: string | null;
  kind: string | null;
  loopStep: string | null;
  standards: string | null;
  body: string;
};

export type LessonSectionKind =
  | "property"
  | "practice"
  | "transfer"
  | "residual"
  | "nongoal"
  | "limits"
  | "why"
  | "usability"
  | "mental";

const KIND_LABELS: Record<string, string> = {
  "concept-model": "Idea",
  "design-exercise": "Design",
  "mechanism-lab": "Try it",
  "break-fix-lab": "Try it",
  "verification-lab": "Check it",
  "operations-exercise": "Keep it running",
  "transfer-challenge": "Use it elsewhere",
  "code-review": "Review",
};

export function kindLabel(kind: string): string {
  return KIND_LABELS[kind] ?? kind.replace(/-/g, " ");
}

export function plainHeadingText(md: string): string {
  return md
    .replace(/\*\*/g, "")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\[([^\]]+)\]\([^)]+\)/g, "$1")
    .trim();
}

export function slugifyHeading(text: string): string {
  const slug = plainHeadingText(text)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);
  return slug || "section";
}

export function createIdAllocator(): (text: string) => string {
  const used = new Map<string, number>();
  return (text: string): string => {
    const base = slugifyHeading(text);
    const next = (used.get(base) ?? 0) + 1;
    used.set(base, next);
    return next === 1 ? base : `${base}-${next}`;
  };
}

export function parseLessonLead(source: string): LessonLead {
  const lines = source.replace(/\r\n/g, "\n").split("\n");
  let i = 0;
  while (i < lines.length && lines[i].trim() === "") {
    i += 1;
  }
  let title: string | null = null;
  if (lines[i] === "---") {
    i += 1;
    while (i < lines.length && lines[i] !== "---") {
      const field = /^title:\s*(.*)$/.exec(lines[i]);
      if (field) {
        title = field[1].trim().replace(/^['"]|['"]$/g, "");
      }
      i += 1;
    }
    if (lines[i] === "---") {
      i += 1;
    }
    while (i < lines.length && lines[i].trim() === "") {
      i += 1;
    }
  }
  if (lines[i]?.startsWith("# ")) {
    title = lines[i].slice(2).trim();
    i += 1;
  }
  while (i < lines.length && lines[i].trim() === "") {
    i += 1;
  }
  const meta: Record<string, string> = {};
  while (i < lines.length) {
    const match = /^\*\*(Kind|Loop step|Standards):\*\*\s*(.*)$/.exec(
      lines[i].trim(),
    );
    if (!match) {
      break;
    }
    meta[match[1]] = match[2].trim();
    i += 1;
  }
  while (i < lines.length && lines[i].trim() === "") {
    i += 1;
  }
  return {
    title,
    kind: meta.Kind ?? null,
    loopStep: meta["Loop step"] ?? null,
    standards: meta.Standards ?? null,
    body: lines.slice(i).join("\n"),
  };
}

export function spokenLessonTitle(yamlTitle: string, body: string): string {
  const lead = parseLessonLead(body);
  return plainLessonTitle(lead.title || yamlTitle);
}

export function extractHeadings(source: string): TocHeading[] {
  const alloc = createIdAllocator();
  const out: TocHeading[] = [];
  let inCode = false;
  for (const line of source.replace(/\r\n/g, "\n").split("\n")) {
    if (line.startsWith("```")) {
      inCode = !inCode;
      continue;
    }
    if (inCode) {
      continue;
    }
    if (line.startsWith("## ")) {
      const text = plainHeadingText(line.slice(3));
      out.push({ id: alloc(text), text: displayHeading(text), level: 2 });
      continue;
    }
    if (line.startsWith("### ")) {
      const text = plainHeadingText(line.slice(4));
      out.push({ id: alloc(text), text: displayHeading(text), level: 3 });
    }
  }
  return out;
}

export function sectionKindFromHeading(text: string): LessonSectionKind | null {
  const t = plainHeadingText(text).toLowerCase();
  if (t.startsWith("property") || t === "the rule" || t === "start with the rule") {
    return "property";
  }
  if (t === "practice") {
    return "practice";
  }
  if (t.startsWith("transfer") || t.startsWith("use it somewhere new")) {
    return "transfer";
  }
  if (t.startsWith("residual risk") || t.startsWith("what can still go wrong")) {
    return "residual";
  }
  if (
    t.startsWith("non-goals") ||
    t.startsWith("nongoals") ||
    t.startsWith("what this page is not doing")
  ) {
    return "nongoal";
  }
  if (t.startsWith("mechanism limits") || t.startsWith("what the tool cannot do")) {
    return "limits";
  }
  if (t.startsWith("why this") || t.startsWith("why it happens")) {
    return "why";
  }
  if (t.startsWith("usability") || t.startsWith("can people still use it")) {
    return "usability";
  }
  if (t.startsWith("mental model") || t.startsWith("picture")) {
    return "mental";
  }
  return null;
}

export function sectionClassName(kind: LessonSectionKind): string {
  switch (kind) {
    case "property":
      return "lesson-section lesson-section-property";
    case "practice":
      return "lesson-section lesson-section-practice";
    case "transfer":
      return "lesson-section lesson-section-transfer";
    case "residual":
      return "lesson-section lesson-section-residual";
    case "nongoal":
      return "lesson-section lesson-section-nongoal";
    case "limits":
      return "lesson-section lesson-section-limits";
    case "why":
      return "lesson-section lesson-section-why";
    case "usability":
      return "lesson-section lesson-section-usability";
    case "mental":
      return "lesson-section lesson-section-mental";
    default: {
      const exhaustive: never = kind;
      return exhaustive;
    }
  }
}
