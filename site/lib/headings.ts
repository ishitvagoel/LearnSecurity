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
  | "usability";

const KIND_LABELS: Record<string, string> = {
  "concept-model": "Concept",
  "design-exercise": "Design",
  "mechanism-lab": "Break",
  "verification-lab": "Verify",
  "operations-exercise": "Operate",
  "transfer-challenge": "Transfer",
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
      out.push({ id: alloc(text), text, level: 2 });
      continue;
    }
    if (line.startsWith("### ")) {
      const text = plainHeadingText(line.slice(4));
      out.push({ id: alloc(text), text, level: 3 });
    }
  }
  return out;
}

export function sectionKindFromHeading(text: string): LessonSectionKind | null {
  const t = plainHeadingText(text).toLowerCase();
  if (t.startsWith("property")) {
    return "property";
  }
  if (t === "practice") {
    return "practice";
  }
  if (t.startsWith("transfer")) {
    return "transfer";
  }
  if (t.startsWith("residual risk")) {
    return "residual";
  }
  if (t.startsWith("non-goals") || t.startsWith("nongoals")) {
    return "nongoal";
  }
  if (t.startsWith("mechanism limits")) {
    return "limits";
  }
  if (t.startsWith("why this")) {
    return "why";
  }
  if (t.startsWith("usability")) {
    return "usability";
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
    default: {
      const exhaustive: never = kind;
      return exhaustive;
    }
  }
}
