import type { ReactElement } from "react";
import Link from "next/link";

const LINKS = [
  { href: "/", label: "Home" },
  { href: "/roadmap/", label: "Roadmap" },
  { href: "/learn/", label: "Learn" },
  { href: "/labs/", label: "Labs" },
  { href: "/reference/", label: "Reference" },
  { href: "/standards/", label: "Standards" },
  { href: "/checkpoints/", label: "Checkpoints" },
  { href: "/capstone/", label: "Capstone" },
  { href: "/glossary/", label: "Glossary" },
  { href: "/sources/", label: "Sources" },
  { href: "/policy/", label: "Safe use" },
] as const;

export function SiteNav(): ReactElement {
  return (
    <header className="border-b border-stone-300 bg-white">
      <div className="mx-auto flex max-w-6xl flex-wrap items-baseline gap-x-4 gap-y-2 px-4 py-4">
        <Link href="/" className="font-semibold text-stone-900 underline-offset-4 hover:underline">
          LearnSecurity
        </Link>
        <nav aria-label="Primary" className="flex flex-wrap gap-x-3 gap-y-2 text-sm">
          {LINKS.filter((l) => l.href !== "/").map((l) => (
            <Link
              key={l.href}
              href={l.href}
              className="text-blue-900 underline-offset-4 hover:underline"
            >
              {l.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  );
}
