"use client";

import type { ReactElement } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";

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

function isCurrent(href: string, pathname: string): boolean {
  if (href === "/") {
    return pathname === "/";
  }
  return pathname === href || pathname.startsWith(href);
}

export function SiteNav(): ReactElement {
  const pathname = usePathname() || "/";

  return (
    <header className="border-b border-stone-300 bg-white">
      <div className="mx-auto flex max-w-[90rem] flex-wrap items-baseline gap-x-5 gap-y-2 px-4 py-4">
        <Link
          href="/"
          className="font-semibold tracking-tight text-stone-900 underline-offset-4 hover:underline"
        >
          LearnSecurity
        </Link>
        <nav aria-label="Primary" className="flex flex-wrap gap-x-3 gap-y-2 text-sm">
          {LINKS.filter((l) => l.href !== "/").map((l) => {
            const current = isCurrent(l.href, pathname);
            return (
              <Link
                key={l.href}
                href={l.href}
                aria-current={current ? "page" : undefined}
                className={`underline-offset-4 hover:underline ${
                  current ? "font-semibold text-stone-900" : "text-blue-900"
                }`}
              >
                {l.label}
              </Link>
            );
          })}
        </nav>
      </div>
    </header>
  );
}
