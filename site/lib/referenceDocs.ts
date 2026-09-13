import fs from "node:fs";
import path from "node:path";
import { contentRoot } from "./contentRoot";

export type ReferenceDoc = {
  slug: string;
  title: string;
  moduleId: string | null;
  relativePath: string;
  body: string;
};

function parseTitle(h1: string): string {
  const afterDash = (h1.split("—").pop() || h1).replace(/^#\s*/, "").trim();
  return afterDash.replace(/^Phase \d+\s+/, "").trim();
}

export function loadReferenceDocs(): ReferenceDoc[] {
  const dir = path.join(contentRoot(), "reference", "securecollab");
  const files = fs.readdirSync(dir).filter((f) => f.endsWith(".md"));
  const docs = files.map((file) => {
    const raw = fs.readFileSync(path.join(dir, file), "utf8");
    const h1 = raw.split("\n")[0] || "";
    const moduleMatch = raw.match(/Module (\d+(?:\.\d+)?)/);
    return {
      slug: file.replace(/\.md$/, ""),
      title: parseTitle(h1),
      moduleId: moduleMatch ? moduleMatch[1] : null,
      relativePath: `content/reference/securecollab/${file}`,
      body: raw,
    };
  });
  return docs.sort((a, b) => {
    const av = a.moduleId ? Number.parseFloat(a.moduleId) : Number.POSITIVE_INFINITY;
    const bv = b.moduleId ? Number.parseFloat(b.moduleId) : Number.POSITIVE_INFINITY;
    return av - bv;
  });
}

export function loadReferenceDoc(slug: string): ReferenceDoc | null {
  return loadReferenceDocs().find((doc) => doc.slug === slug) || null;
}
