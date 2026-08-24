"use client";

import { useEffect, useState, type ReactElement } from "react";
import type { TocHeading } from "@/lib/headings";

export function LessonToc({
  headings,
  variant,
}: {
  headings: TocHeading[];
  variant: "mobile" | "desktop";
}): ReactElement | null {
  const [active, setActive] = useState(headings[0]?.id ?? "");
  const ids = headings.map((h) => h.id).join(" ");

  useEffect(() => {
    const idList = ids.split(" ").filter(Boolean);
    if (idList.length === 0) {
      return;
    }
    const elements = idList
      .map((id) => document.getElementById(id))
      .filter((el): el is HTMLElement => el !== null);
    if (elements.length === 0) {
      return;
    }
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        const id = visible[0]?.target.id;
        if (id) {
          setActive(id);
        }
      },
      { rootMargin: "0px 0px -65% 0px", threshold: [0, 1] },
    );
    for (const el of elements) {
      observer.observe(el);
    }
    return () => observer.disconnect();
  }, [ids]);

  if (headings.length === 0) {
    return null;
  }

  const list = (
    <ol className="mt-2 space-y-1 text-sm">
      {headings.map((h) => (
        <li key={h.id} className={h.level === 3 ? "pl-3" : ""}>
          <a
            href={`#${h.id}`}
            aria-current={active === h.id ? "location" : undefined}
            className={`block leading-snug underline-offset-2 hover:underline ${
              active === h.id ? "font-medium text-stone-900" : "text-stone-700"
            }`}
          >
            {h.text}
          </a>
        </li>
      ))}
    </ol>
  );

  if (variant === "mobile") {
    return (
      <details className="mb-6 rounded-lg border border-stone-200 bg-white px-3 py-2 lg:hidden">
        <summary className="cursor-pointer font-medium text-stone-900">On this page</summary>
        {list}
      </details>
    );
  }

  return (
    <nav
      aria-label="On this page"
      className="sticky top-4 max-h-[calc(100vh-2rem)] overflow-y-auto pb-8"
    >
      <p className="text-xs font-semibold uppercase tracking-wide text-stone-600">
        On this page
      </p>
      {list}
    </nav>
  );
}

export function ReadingProgress(): ReactElement {
  const [percent, setPercent] = useState(0);

  useEffect(() => {
    const onScroll = (): void => {
      const el = document.getElementById("lesson-article");
      if (!el) {
        return;
      }
      const total = el.offsetHeight - window.innerHeight;
      const scrolled = window.scrollY - el.offsetTop;
      if (total <= 0) {
        setPercent(100);
        return;
      }
      setPercent(Math.min(100, Math.max(0, (scrolled / total) * 100)));
    };
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <div
      className="pointer-events-none fixed inset-x-0 top-0 z-40 h-1 bg-stone-200"
      role="progressbar"
      aria-label="Reading progress"
      aria-valuemin={0}
      aria-valuemax={100}
      aria-valuenow={Math.round(percent)}
    >
      <div className="h-full bg-blue-800" style={{ width: `${percent}%` }} />
    </div>
  );
}
