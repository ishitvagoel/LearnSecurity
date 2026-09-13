import type { ModuleMeta } from "./types";

/** The recommended web/API route. Optional tracks are deliberately excluded. */
export const WEB_API_ROUTE = [
  "0.1", "0.2", "1.1", "1.2", "1.3", "1.4",
  "2.1", "2.2", "2.3", "2.4", "3.1", "3.2", "3.3", "3.4",
  "4.1", "4.2", "4.3", "4.4", "4.5", "5.1", "5.2", "5.3", "5.4", "5.5",
  "6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7", "7.1", "7.2", "7.3", "7.4",
  "9.1", "9.2", "9.3", "9.4", "9.5", "10.1", "10.2", "10.3", "10.4", "10.5", "11",
] as const;
export const MOBILE_ROUTE = ["8.1", "8.2", "8.3", "8.4", "8.5"] as const;
export const ELECTIVE_ROUTE = ["E1", "E2", "E3", "E4", "E5", "E6"] as const;
export type RouteKind = "web-api" | "mobile" | "elective";
export function routeIds(kind: RouteKind = "web-api"): readonly string[] {
  return kind === "mobile" ? MOBILE_ROUTE : kind === "elective" ? ELECTIVE_ROUTE : WEB_API_ROUTE;
}
export function routeModules(modules: ModuleMeta[], kind: RouteKind = "web-api"): ModuleMeta[] {
  const byId = new Map(modules.map((m) => [m.id, m]));
  return routeIds(kind).flatMap((id) => byId.get(id) ? [byId.get(id)!] : []);
}
export function nextRouteModule(modules: ModuleMeta[], id: string, kind: RouteKind = "web-api"): ModuleMeta | null {
  const ordered = routeModules(modules, kind);
  const index = ordered.findIndex((m) => m.id === id);
  return index >= 0 ? ordered[index + 1] || null : null;
}
export function routeLabel(kind: RouteKind = "web-api"): string {
  return kind === "mobile" ? "Mobile extension" : kind === "elective" ? "Electives" : "Web/API route";
}
