import fs from "node:fs";
import path from "node:path";
import yaml from "js-yaml";
import { contentRoot } from "./contentRoot";
import type { LessonFile, ModuleMeta } from "./types";

function assertModule(data: unknown, file: string): ModuleMeta {
  if (!data || typeof data !== "object") {
    throw new Error(`Invalid module.yaml: ${file}`);
  }
  const m = data as ModuleMeta;
  if (!m.id || !m.title) {
    throw new Error(`module.yaml missing id/title: ${file}`);
  }
  return m;
}

export function listModuleFiles(): string[] {
  const root = path.join(contentRoot(), "modules");
  const out: string[] = [];
  const walk = (dir: string): void => {
    for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        walk(p);
      } else if (entry.name === "module.yaml") {
        out.push(p);
      }
    }
  };
  walk(root);
  return out.sort();
}

export function loadAllModules(): ModuleMeta[] {
  return listModuleFiles().map((file) => {
    const raw = yaml.load(fs.readFileSync(file, "utf8"));
    const meta = assertModule(raw, file);
    meta.contentDir = path.dirname(file);
    return meta;
  });
}

export function loadModule(id: string): ModuleMeta {
  const found = loadAllModules().find((m) => m.id === id);
  if (!found) {
    throw new Error(`Unknown module ${id}`);
  }
  return found;
}

export function loadLessons(mod: ModuleMeta): LessonFile[] {
  return (mod.learningObjects || []).map((lo) => {
    const rel = lo.path || "";
    const filename = rel.replace(/^lessons\//, "");
    const full = path.join(mod.contentDir, rel);
    let body = "";
    if (rel && fs.existsSync(full) && !full.includes(`${path.sep}assessment${path.sep}keys${path.sep}`) && !full.endsWith(`${path.sep}assessment${path.sep}keys`)) {
      body = fs.readFileSync(full, "utf8");
    }
    return {
      id: lo.id,
      title: lo.title,
      kind: lo.kind,
      filename,
      body,
    };
  });
}

export function loadPins(): unknown {
  const file = path.join(contentRoot(), "standards", "pins.yaml");
  return yaml.load(fs.readFileSync(file, "utf8"));
}

export function moduleHref(id: string): string {
  return `/learn/${encodeURIComponent(id)}/`;
}

export function lessonHref(moduleId: string, filename: string): string {
  const slug = filename.replace(/\.md$/, "");
  return `/learn/${encodeURIComponent(moduleId)}/${encodeURIComponent(slug)}/`;
}
