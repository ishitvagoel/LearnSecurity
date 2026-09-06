export type NavLink = {
  href: string;
  label: string;
};

export const PRIMARY_NAV: NavLink[] = [
  { href: "/learn/", label: "Learn" },
  { href: "/roadmap/", label: "Roadmap" },
  { href: "/labs/", label: "Labs" },
];

export const RESOURCE_NAV: NavLink[] = [
  { href: "/reference/", label: "SecureCollab" },
  { href: "/glossary/", label: "Glossary" },
  { href: "/standards/", label: "Standards" },
  { href: "/sources/", label: "Sources" },
];

export const COURSE_NAV: NavLink[] = [
  { href: "/checkpoints/", label: "Checkpoints" },
  { href: "/capstone/", label: "Capstone" },
  { href: "/policy/", label: "Safe use" },
];

export const MORE_NAV: NavLink[] = [...RESOURCE_NAV, ...COURSE_NAV];

export function isCurrentPath(href: string, pathname: string): boolean {
  if (href === "/") {
    return pathname === "/";
  }
  return pathname === href || pathname.startsWith(href);
}
