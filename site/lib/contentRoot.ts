import path from "node:path";

/** Repo `content/` tree. Never include `assessment/keys`. */
export function contentRoot(): string {
  return path.join(process.cwd(), "..", "content");
}
