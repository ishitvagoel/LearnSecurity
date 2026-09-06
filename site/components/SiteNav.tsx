"use client";

import type { ReactElement } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useId, useRef, useState } from "react";
import { COURSE_NAV, MORE_NAV, PRIMARY_NAV, RESOURCE_NAV, isCurrentPath } from "@/lib/nav";

function NavItem({
  href,
  label,
  pathname,
}: {
  href: string;
  label: string;
  pathname: string;
}): ReactElement {
  const current = isCurrentPath(href, pathname);
  return (
    <Link
      href={href}
      aria-current={current ? "page" : undefined}
      className={`rounded-md px-2 py-1 text-sm underline-offset-4 hover:underline ${
        current ? "font-semibold text-stone-900" : "text-stone-700 hover:text-stone-900"
      }`}
    >
      {label}
    </Link>
  );
}

export function SiteNav(): ReactElement {
  const pathname = usePathname() || "/";
  const [menuOpen, setMenuOpen] = useState(false);
  const [moreOpen, setMoreOpen] = useState(false);
  const [navPath, setNavPath] = useState(pathname);
  const moreRef = useRef<HTMLDivElement>(null);
  const moreId = useId();
  const menuId = useId();
  const moreCurrent = MORE_NAV.some((link) => isCurrentPath(link.href, pathname));

  if (navPath !== pathname) {
    setNavPath(pathname);
    setMenuOpen(false);
    setMoreOpen(false);
  }
  useEffect(() => {
    const onKey = (event: KeyboardEvent): void => {
      if (event.key === "Escape") {
        setMenuOpen(false);
        setMoreOpen(false);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  useEffect(() => {
    if (!moreOpen) {
      return;
    }
    const onPointer = (event: MouseEvent): void => {
      if (moreRef.current && !moreRef.current.contains(event.target as Node)) {
        setMoreOpen(false);
      }
    };
    window.addEventListener("mousedown", onPointer);
    return () => window.removeEventListener("mousedown", onPointer);
  }, [moreOpen]);

  useEffect(() => {
    document.body.style.overflow = menuOpen ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [menuOpen]);

  return (
    <header className="sticky top-0 z-50 border-b border-stone-300/90 bg-[color-mix(in_srgb,var(--background)_86%,white)] backdrop-blur-md">
      <div className="mx-auto flex h-16 max-w-[90rem] items-center justify-between gap-4 px-4">
        <Link href="/" className="min-w-0 shrink-0 no-underline">
          <span className="block text-base font-semibold tracking-tight text-stone-900">
            LearnSecurity
          </span>
          <span className="hidden text-xs text-stone-600 sm:block">
            Secure application engineering
          </span>
        </Link>
        <nav aria-label="Primary" className="hidden items-center gap-1 md:flex">
          {PRIMARY_NAV.map((link) => (
            <NavItem key={link.href} href={link.href} label={link.label} pathname={pathname} />
          ))}
          <div className="relative" ref={moreRef}>
            <button
              type="button"
              className={`rounded-md px-2 py-1 text-sm ${
                moreCurrent || moreOpen
                  ? "font-semibold text-stone-900"
                  : "text-stone-700 hover:text-stone-900"
              }`}
              aria-expanded={moreOpen}
              aria-controls={moreId}
              aria-haspopup="true"
              aria-label="More pages"
              onClick={() => setMoreOpen((open) => !open)}
            >
              More
            </button>
            {moreOpen ? (
              <div
                id={moreId}
                className="absolute right-0 z-50 mt-2 w-56 rounded-xl border border-stone-200 bg-white p-2 shadow-lg"
              >
                <p className="px-2 pb-1 text-xs font-semibold uppercase tracking-wide text-stone-500">
                  Reference
                </p>
                {RESOURCE_NAV.map((link) => (
                  <Link
                    key={link.href}
                    href={link.href}
                    aria-current={isCurrentPath(link.href, pathname) ? "page" : undefined}
                    className="block rounded-md px-2 py-1.5 text-sm text-stone-800 hover:bg-stone-100"
                  >
                    {link.label}
                  </Link>
                ))}
                <p className="mt-2 px-2 pb-1 text-xs font-semibold uppercase tracking-wide text-stone-500">
                  Course
                </p>
                {COURSE_NAV.map((link) => (
                  <Link
                    key={link.href}
                    href={link.href}
                    aria-current={isCurrentPath(link.href, pathname) ? "page" : undefined}
                    className="block rounded-md px-2 py-1.5 text-sm text-stone-800 hover:bg-stone-100"
                  >
                    {link.label}
                  </Link>
                ))}
              </div>
            ) : null}
          </div>
        </nav>
        <button
          type="button"
          className="rounded-md border border-stone-300 bg-white px-3 py-1.5 text-sm font-medium text-stone-900 md:hidden"
          aria-expanded={menuOpen}
          aria-controls={menuId}
          aria-label={menuOpen ? "Close menu" : "Open menu"}
          onClick={() => setMenuOpen((open) => !open)}
        >
          {menuOpen ? "Close" : "Menu"}
        </button>
      </div>
      {menuOpen ? (
        <nav
          id={menuId}
          aria-label="Site"
          className="max-h-[calc(100vh-4rem)] overflow-y-auto border-t border-stone-200 bg-white px-4 py-4 md:hidden"
        >
          <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-stone-500">
            Start
          </p>
          <div className="flex flex-col gap-1">
            {PRIMARY_NAV.map((link) => (
              <NavItem key={link.href} href={link.href} label={link.label} pathname={pathname} />
            ))}
          </div>
          <p className="mt-4 mb-2 text-xs font-semibold uppercase tracking-wide text-stone-500">
            Reference
          </p>
          <div className="flex flex-col gap-1">
            {RESOURCE_NAV.map((link) => (
              <NavItem key={link.href} href={link.href} label={link.label} pathname={pathname} />
            ))}
          </div>
          <p className="mt-4 mb-2 text-xs font-semibold uppercase tracking-wide text-stone-500">
            Course
          </p>
          <div className="flex flex-col gap-1">
            {COURSE_NAV.map((link) => (
              <NavItem key={link.href} href={link.href} label={link.label} pathname={pathname} />
            ))}
          </div>
        </nav>
      ) : null}
    </header>
  );
}
