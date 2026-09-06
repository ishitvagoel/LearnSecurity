"use client";

import type { ReactElement } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useId, useRef, useState } from "react";
import { BrandMark } from "@/components/BrandMark";
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
      className={`rounded-full px-3 py-1.5 text-sm transition-colors ${
        current
          ? "bg-forest text-paper"
          : "text-stone-700 hover:bg-white hover:text-stone-900"
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
  const home = pathname === "/";

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
    <header className="sticky top-0 z-50 border-b border-line bg-paper/90 backdrop-blur-md">
      <div className="mx-auto flex h-[4.25rem] max-w-6xl items-center justify-between gap-4 px-4">
        <Link href="/" className="flex min-w-0 items-center gap-2.5 no-underline">
          <BrandMark />
          <span>
            <span className="block text-[0.95rem] font-semibold tracking-tight text-ink">
              LearnSecurity
            </span>
            <span className="hidden text-xs text-muted sm:block">A course in building safer software</span>
          </span>
        </Link>
        <nav aria-label="Primary" className="hidden items-center gap-1 lg:flex">
          <Link
            href="/"
            aria-current={home ? "page" : undefined}
            className={`rounded-full px-3 py-1.5 text-sm transition-colors ${
              home ? "bg-forest text-paper" : "text-stone-700 hover:bg-white hover:text-stone-900"
            }`}
          >
            Home
          </Link>
          {PRIMARY_NAV.map((link) => (
            <NavItem key={link.href} href={link.href} label={link.label} pathname={pathname} />
          ))}
          <div className="relative" ref={moreRef}>
            <button
              type="button"
              className={`rounded-full px-3 py-1.5 text-sm ${
                moreCurrent || moreOpen
                  ? "bg-white text-ink ring-1 ring-line"
                  : "text-stone-700 hover:bg-white hover:text-stone-900"
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
                className="absolute right-0 z-50 mt-2 w-60 rounded-2xl border border-line bg-paper p-2 shadow-lg"
              >
                <p className="px-3 pt-1 pb-1 text-xs font-medium text-muted">Reference</p>
                {RESOURCE_NAV.map((link) => (
                  <Link
                    key={link.href}
                    href={link.href}
                    aria-current={isCurrentPath(link.href, pathname) ? "page" : undefined}
                    className="block rounded-xl px-3 py-2 text-sm text-ink hover:bg-white"
                  >
                    {link.label}
                  </Link>
                ))}
                <p className="mt-1 px-3 pt-2 pb-1 text-xs font-medium text-muted">Course</p>
                {COURSE_NAV.map((link) => (
                  <Link
                    key={link.href}
                    href={link.href}
                    aria-current={isCurrentPath(link.href, pathname) ? "page" : undefined}
                    className="block rounded-xl px-3 py-2 text-sm text-ink hover:bg-white"
                  >
                    {link.label}
                  </Link>
                ))}
              </div>
            ) : null}
          </div>
        </nav>
        <div className="flex items-center gap-2">
          <Link
            href="/learn/0.1/"
            className="hidden rounded-full bg-forest px-3.5 py-1.5 text-sm font-medium text-paper hover:bg-forest-hover sm:inline-flex"
          >
            Start here
          </Link>
          <button
            type="button"
            className="rounded-full border border-line bg-white px-3 py-1.5 text-sm font-medium text-ink lg:hidden"
            aria-expanded={menuOpen}
            aria-controls={menuId}
            aria-label={menuOpen ? "Close menu" : "Open menu"}
            onClick={() => setMenuOpen((open) => !open)}
          >
            {menuOpen ? "Close" : "Menu"}
          </button>
        </div>
      </div>
      {menuOpen ? (
        <nav
          id={menuId}
          aria-label="Site"
          className="max-h-[calc(100vh-4.25rem)] overflow-y-auto border-t border-line bg-paper px-4 py-4 lg:hidden"
        >
          <div className="flex flex-col gap-1">
            <NavItem href="/" label="Home" pathname={pathname} />
            {PRIMARY_NAV.map((link) => (
              <NavItem key={link.href} href={link.href} label={link.label} pathname={pathname} />
            ))}
          </div>
          <p className="mt-4 mb-2 text-xs font-medium text-muted">Reference</p>
          <div className="flex flex-col gap-1">
            {RESOURCE_NAV.map((link) => (
              <NavItem key={link.href} href={link.href} label={link.label} pathname={pathname} />
            ))}
          </div>
          <p className="mt-4 mb-2 text-xs font-medium text-muted">Course</p>
          <div className="flex flex-col gap-1">
            {COURSE_NAV.map((link) => (
              <NavItem key={link.href} href={link.href} label={link.label} pathname={pathname} />
            ))}
          </div>
          <Link
            href="/learn/0.1/"
            className="mt-4 inline-flex w-full justify-center rounded-full bg-forest px-3.5 py-2.5 text-sm font-medium text-paper hover:bg-forest-hover sm:hidden"
          >
            Start here
          </Link>
        </nav>
      ) : null}
    </header>
  );
}
