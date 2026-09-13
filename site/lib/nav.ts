export type NavLink = {
  href: string;
  label: string;
};

export const PRIMARY_NAV: NavLink[] = [
  { href: "/learn/", label: "Lessons" },
  { href: "/roadmap/", label: "Study order" },
  { href: "/labs/", label: "Practice" },
  { href: "/assess/", label: "Assessments" },
  { href: "/checkpoints/", label: "Check-ins" },
];

export const RESOURCE_NAV: NavLink[] = [
  { href: "/reference/", label: "The notes app" },
  { href: "/project/", label: "Project milestones" },
  { href: "/glossary/", label: "Word list" },
  { href: "/references/", label: "References" },
];

export const COURSE_NAV: NavLink[] = [
  { href: "/progress/", label: "Your progress" },
  { href: "/capstone/", label: "Final project" },
  { href: "/policy/", label: "Rules" },
];

export const MORE_NAV: NavLink[] = [...RESOURCE_NAV, ...COURSE_NAV];

export function isCurrentPath(href: string, pathname: string): boolean {
  if (href === "/") {
    return pathname === "/";
  }
  return pathname === href || pathname.startsWith(href);
}
