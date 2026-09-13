import fs from "node:fs";
import path from "node:path";
import yaml from "js-yaml";
import type { ModuleMeta } from "./types";
import { contentRoot } from "./contentRoot";

export type RouteKind = "web-api" | "mobile" | "elective";
type RouteManifest = { version?: number; routes?: Partial<Record<RouteKind, unknown>> };
let cachedRoutes: Partial<Record<RouteKind, readonly string[]>> | null = null;

function loadRoutes(): Partial<Record<RouteKind, readonly string[]>> {
  if (cachedRoutes) {
    return cachedRoutes;
  }
  const file = path.join(contentRoot(), "route.yaml");
  const data = yaml.load(fs.readFileSync(file, "utf8")) as RouteManifest;
  const routes: Partial<Record<RouteKind, readonly string[]>> = {};
  for (const kind of ["web-api", "mobile", "elective"] as const) {
    const values = data.routes?.[kind];
    if (Array.isArray(values) && values.every((value): value is string => typeof value === "string")) {
      routes[kind] = values;
    }
  }
  if (!routes["web-api"]?.length) {
    throw new Error("content/route.yaml must define a non-empty web-api route");
  }
  cachedRoutes = routes;
  return routes;
}

export function routeIds(kind: RouteKind = "web-api"): readonly string[] {
  return loadRoutes()[kind] || [];
}

export function routeModules(modules: ModuleMeta[], kind: RouteKind = "web-api"): ModuleMeta[] {
  const byId = new Map(modules.map((module) => [module.id, module]));
  return routeIds(kind).flatMap((id) => {
    const item = byId.get(id);
    return item ? [item] : [];
  });
}

export function nextRouteModule(modules: ModuleMeta[], id: string, kind: RouteKind = "web-api"): ModuleMeta | null {
  const ordered = routeModules(modules, kind);
  const index = ordered.findIndex((module) => module.id === id);
  return index >= 0 ? ordered[index + 1] || null : null;
}

export function routeLabel(kind: RouteKind = "web-api"): string {
  return kind === "mobile" ? "Mobile extension" : kind === "elective" ? "Electives" : "Web/API route";
}
