import fs from "node:fs";
import path from "node:path";

/**
 * Repo `content/` tree. Never include `assessment/keys`.
 *
 * Vercel must use the **repository root** as the project root so `content/` is
 * present next to `site/`. Do not set the Vercel Root Directory to `site/`.
 */
export function contentRoot(): string {
  if (process.env.CONTENT_DIR) {
    return path.resolve(process.env.CONTENT_DIR);
  }
  const candidates = [
    path.join(process.cwd(), "..", "content"),
    path.join(process.cwd(), "content"),
  ];
  for (const dir of candidates) {
    if (fs.existsSync(path.join(dir, "modules"))) {
      return dir;
    }
  }
  throw new Error(
    `Cannot find content/modules (cwd=${process.cwd()}). Set CONTENT_DIR or build with the git root as the Vercel project root. Tried: ${candidates.join(", ")}`,
  );
}
