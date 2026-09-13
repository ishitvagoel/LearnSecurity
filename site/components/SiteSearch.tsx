"use client";

import type { ReactElement } from "react";
import { useRouter } from "next/navigation";
import { useEffect, useId, useMemo, useRef, useState } from "react";
import type { SearchEntry, SearchEntryType } from "@/lib/searchIndex";

let cachedIndex: SearchEntry[] | null = null;
let inFlight: Promise<SearchEntry[]> | null = null;

function loadIndex(): Promise<SearchEntry[]> {
  if (cachedIndex) {
    return Promise.resolve(cachedIndex);
  }
  if (!inFlight) {
    inFlight = fetch("/search-index.json")
      .then((res) => res.json())
      .then((data: SearchEntry[]) => {
        cachedIndex = data;
        return data;
      })
      .catch(() => {
        inFlight = null;
        return [];
      });
  }
  return inFlight;
}

const TYPE_LABEL: Record<SearchEntryType, string> = {
  page: "Site page",
  module: "Topic",
  lesson: "Lesson",
  glossary: "Word list",
};

function score(entry: SearchEntry, queryLower: string, words: string[]): number {
  const titleLower = entry.title.toLowerCase();
  let s = 0;
  if (titleLower === queryLower) {
    s += 100;
  } else if (titleLower.startsWith(queryLower)) {
    s += 60;
  } else if (titleLower.includes(queryLower)) {
    s += 40;
  }
  const textLower = entry.text.toLowerCase();
  for (const w of words) {
    if (!w) {
      continue;
    }
    if (titleLower.includes(w)) {
      s += 8;
    }
    if (entry.subtitle?.toLowerCase().includes(w)) {
      s += 4;
    }
    if (textLower.includes(w)) {
      s += 2;
    }
  }
  return s;
}

function search(entries: SearchEntry[], query: string): SearchEntry[] {
  const trimmed = query.trim().toLowerCase();
  if (!trimmed) {
    return [];
  }
  const words = trimmed.split(/\s+/).filter(Boolean);
  return entries
    .map((entry) => ({ entry, s: score(entry, trimmed, words) }))
    .filter((x) => x.s > 0)
    .sort((a, b) => b.s - a.s)
    .slice(0, 20)
    .map((x) => x.entry);
}

function isTypingTarget(el: EventTarget | null): boolean {
  if (!(el instanceof HTMLElement)) {
    return false;
  }
  const tag = el.tagName;
  return tag === "INPUT" || tag === "TEXTAREA" || el.isContentEditable;
}

export function SiteSearch(): ReactElement {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [entries, setEntries] = useState<SearchEntry[] | null>(null);
  const [activeIndex, setActiveIndex] = useState(0);
  const inputRef = useRef<HTMLInputElement>(null);
  const triggerRef = useRef<HTMLButtonElement>(null);
  const listId = useId();
  const router = useRouter();

  const results = useMemo(() => (entries ? search(entries, query) : []), [entries, query]);

  const close = (): void => {
    setOpen(false);
    triggerRef.current?.focus();
  };

  const openSearch = (): void => {
    setOpen(true);
    setQuery("");
    setActiveIndex(0);
    if (!entries) {
      loadIndex().then(setEntries);
    }
  };

  useEffect(() => {
    if (!open) {
      return;
    }
    inputRef.current?.focus();
  }, [open]);

  useEffect(() => {
    const onKey = (event: KeyboardEvent): void => {
      if (!open && event.key === "/" && !isTypingTarget(event.target)) {
        event.preventDefault();
        openSearch();
        return;
      }
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault();
        if (open) {
          close();
        } else {
          openSearch();
        }
        return;
      }
      if (!open) {
        return;
      }
      if (event.key === "Escape") {
        event.preventDefault();
        close();
      } else if (event.key === "ArrowDown") {
        event.preventDefault();
        setActiveIndex((i) => Math.min(i + 1, results.length - 1));
      } else if (event.key === "ArrowUp") {
        event.preventDefault();
        setActiveIndex((i) => Math.max(i - 1, 0));
      } else if (event.key === "Enter") {
        event.preventDefault();
        const target = results[activeIndex];
        if (target) {
          close();
          router.push(target.href);
        }
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [open, results, activeIndex]);

  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [open]);

  return (
    <>
      <button
        ref={triggerRef}
        type="button"
        onClick={openSearch}
        className="flex items-center gap-2 rounded-full border border-line bg-white px-3 py-1.5 text-sm text-stone-700 hover:border-forest-accent hover:text-stone-900"
        aria-haspopup="dialog"
      >
        <svg viewBox="0 0 20 20" className="h-4 w-4" aria-hidden="true" fill="none">
          <circle cx="9" cy="9" r="6" stroke="currentColor" strokeWidth="1.6" />
          <path d="M17 17L13.4 13.4" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
        </svg>
        <span className="hidden sm:inline">Search</span>
        <kbd className="hidden rounded border border-line bg-background px-1.5 py-0.5 font-mono text-[0.7rem] text-muted sm:inline-block">
          /
        </kbd>
      </button>
      {open ? (
        <div className="fixed inset-0 z-[60] flex items-start justify-center px-4 pt-[10vh]">
          <div
            className="absolute inset-0 bg-stone-900/40"
            onClick={close}
            aria-hidden="true"
          />
          <div
            role="dialog"
            aria-modal="true"
            aria-label="Search this course"
            className="relative w-full max-w-xl overflow-hidden rounded-2xl border border-line bg-paper shadow-xl"
          >
            <div className="flex items-center gap-2 border-b border-line px-4 py-3">
              <svg viewBox="0 0 20 20" className="h-4 w-4 shrink-0 text-muted" aria-hidden="true" fill="none">
                <circle cx="9" cy="9" r="6" stroke="currentColor" strokeWidth="1.6" />
                <path d="M17 17L13.4 13.4" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
              </svg>
              <input
                ref={inputRef}
                type="text"
                value={query}
                onChange={(e) => {
                  setQuery(e.target.value);
                  setActiveIndex(0);
                }}
                placeholder="Search topics, lessons, and pages…"
                className="w-full bg-transparent text-sm text-ink outline-none placeholder:text-muted"
                role="combobox"
                aria-expanded={results.length > 0}
                aria-controls={listId}
                autoComplete="off"
              />
              <button
                type="button"
                onClick={close}
                className="shrink-0 rounded-md px-2 py-1 text-xs text-muted hover:bg-white hover:text-ink"
              >
                Esc
              </button>
            </div>
            <div id={listId} className="max-h-[60vh] overflow-y-auto p-2">
              {!entries ? (
                <p className="px-3 py-6 text-center text-sm text-muted">Loading the index…</p>
              ) : query.trim() === "" ? (
                <p className="px-3 py-6 text-center text-sm text-muted">
                  Type to search {entries.length} pages, topics, and lessons.
                </p>
              ) : results.length === 0 ? (
                <p className="px-3 py-6 text-center text-sm text-muted">Nothing matched “{query}.”</p>
              ) : (
                <ul>
                  {results.map((entry, i) => (
                    <li key={entry.id}>
                      <button
                        type="button"
                        onMouseEnter={() => setActiveIndex(i)}
                        onClick={() => {
                          close();
                          router.push(entry.href);
                        }}
                        className={`flex w-full flex-col items-start gap-0.5 rounded-lg px-3 py-2 text-left ${
                          i === activeIndex ? "bg-forest text-on-forest" : "text-ink hover:bg-white"
                        }`}
                      >
                        <span className="flex w-full items-center justify-between gap-2">
                          <span className="truncate text-sm font-medium">{entry.title}</span>
                          <span
                            className={`shrink-0 rounded-full px-2 py-0.5 text-[0.7rem] ${
                              i === activeIndex
                                ? "bg-black/15 text-on-forest"
                                : "bg-background text-muted"
                            }`}
                          >
                            {TYPE_LABEL[entry.type]}
                          </span>
                        </span>
                        {entry.subtitle ? (
                          <span
                            className={`text-xs ${i === activeIndex ? "text-on-forest-muted" : "text-muted"}`}
                          >
                            {entry.subtitle}
                          </span>
                        ) : null}
                      </button>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        </div>
      ) : null}
    </>
  );
}
