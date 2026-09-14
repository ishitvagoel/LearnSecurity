import fs from "node:fs";
import path from "node:path";
import yaml from "js-yaml";
import { contentRoot } from "./contentRoot";

export type Bridge = {
  id: string;
  capability: string;
  title: string;
  objective: string;
  task: string;
  success: string;
  retry: string;
};

type BridgeManifest = { version?: number; bridges?: unknown };
let cached: Bridge[] | null = null;

function isBridge(value: unknown): value is Bridge {
  if (!value || typeof value !== "object") return false;
  const item = value as Record<string, unknown>;
  return ["id", "capability", "title", "objective", "task", "success", "retry"].every(
    (key) => typeof item[key] === "string" && item[key],
  );
}

export function loadBridges(): Bridge[] {
  if (cached) return cached;
  const file = path.join(contentRoot(), "bridges.yaml");
  const data = yaml.load(fs.readFileSync(file, "utf8")) as BridgeManifest;
  if (!Array.isArray(data.bridges) || !data.bridges.every(isBridge)) {
    throw new Error("content/bridges.yaml must contain complete bridge records");
  }
  const ids = new Set<string>();
  for (const bridge of data.bridges) {
    if (ids.has(bridge.id)) throw new Error(`duplicate bridge id: ${bridge.id}`);
    ids.add(bridge.id);
  }
  cached = data.bridges;
  return cached;
}

export function bridgeHref(id: string): string {
  return `/bridges/${encodeURIComponent(id)}/`;
}
