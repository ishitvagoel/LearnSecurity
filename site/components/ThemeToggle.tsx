"use client";

import { useSyncExternalStore, type ReactElement } from "react";

type Theme = "light" | "dark";

const listeners = new Set<() => void>();

function emit(): void {
  for (const listener of listeners) {
    listener();
  }
}

function subscribe(onStoreChange: () => void): () => void {
  const media = window.matchMedia("(prefers-color-scheme: dark)");
  media.addEventListener("change", onStoreChange);
  listeners.add(onStoreChange);
  return () => {
    media.removeEventListener("change", onStoreChange);
    listeners.delete(onStoreChange);
  };
}

function getStoredTheme(): Theme | null {
  try {
    const value = localStorage.getItem("ls-theme");
    return value === "light" || value === "dark" ? value : null;
  } catch {
    return null;
  }
}

function getSnapshot(): Theme {
  return getStoredTheme() ?? (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
}

function getServerSnapshot(): Theme {
  return "light";
}

export function ThemeToggle(): ReactElement {
  const theme = useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot);

  const toggle = (): void => {
    const next: Theme = theme === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try {
      localStorage.setItem("ls-theme", next);
    } catch {
      // Storage may be unavailable (private mode); the attribute above still
      // themes this page load.
    }
    emit();
  };

  const isDark = theme === "dark";

  return (
    <button
      type="button"
      onClick={toggle}
      aria-label={isDark ? "Switch to light mode" : "Switch to dark mode"}
      className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border border-line bg-surface text-muted hover:border-forest-accent hover:text-ink"
    >
      {isDark ? (
        <svg viewBox="0 0 20 20" className="h-4 w-4" aria-hidden="true" fill="none">
          <circle cx="10" cy="10" r="4.2" stroke="currentColor" strokeWidth="1.6" />
          <path
            d="M10 2.2v1.8M10 16v1.8M17.8 10H16M4 10H2.2M15.4 4.6l-1.27 1.27M5.86 14.14L4.6 15.4M15.4 15.4l-1.27-1.27M5.86 5.86L4.6 4.6"
            stroke="currentColor"
            strokeWidth="1.6"
            strokeLinecap="round"
          />
        </svg>
      ) : (
        <svg viewBox="0 0 20 20" className="h-4 w-4" aria-hidden="true" fill="none">
          <path
            d="M17 12.5A7 7 0 018 3a6.5 6.5 0 108.99 9.5z"
            stroke="currentColor"
            strokeWidth="1.6"
            strokeLinejoin="round"
          />
        </svg>
      )}
    </button>
  );
}
