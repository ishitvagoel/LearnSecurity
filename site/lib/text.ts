export function stripMarkdown(md: string): string {
  return md
    .replace(/```[\s\S]*?```/g, " ")
    .replace(/!\[[^\]]*\]\([^)]*\)/g, " ")
    .replace(/\[([^\]]+)\]\([^)]*\)/g, "$1")
    .replace(/[`*_>#|]/g, " ")
    .replace(/^\s*---\s*$/gm, " ")
    .replace(/\s+/g, " ")
    .trim();
}

const WORDS_PER_MINUTE = 200;

export function estimateReadingMinutes(markdown: string): number {
  const words = stripMarkdown(markdown).split(" ").filter(Boolean).length;
  return Math.max(1, Math.round(words / WORDS_PER_MINUTE));
}
