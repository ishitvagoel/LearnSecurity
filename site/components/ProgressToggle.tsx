"use client";

import { useCallback, useSyncExternalStore, type ReactElement } from "react";

const KEY = "learnsecurity-progress-v1";
const listeners = new Set<() => void>();

function emit(): void {
  for (const listener of listeners) {
    listener();
  }
}

function subscribe(onStoreChange: () => void): () => void {
  listeners.add(onStoreChange);
  return () => {
    listeners.delete(onStoreChange);
  };
}

function snapshot(moduleId: string): boolean {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) {
      return false;
    }
    const parsed: unknown = JSON.parse(raw);
    if (!Array.isArray(parsed)) {
      return false;
    }
    return parsed.some((x) => x === moduleId);
  } catch {
    return false;
  }
}

export function ProgressToggle({ moduleId }: { moduleId: string }): ReactElement {
  const getSnapshot = useCallback(() => snapshot(moduleId), [moduleId]);
  const done = useSyncExternalStore(subscribe, getSnapshot, () => false);

  const onChange = (): void => {
    const current = snapshot(moduleId);
    let next: string[] = [];
    try {
      const raw = localStorage.getItem(KEY);
      const parsed: unknown = raw ? JSON.parse(raw) : [];
      next = Array.isArray(parsed)
        ? parsed.filter((x): x is string => typeof x === "string")
        : [];
    } catch {
      next = [];
    }
    if (current) {
      next = next.filter((x) => x !== moduleId);
    } else {
      next = [...next, moduleId];
    }
    localStorage.setItem(KEY, JSON.stringify(next));
    emit();
  };

  return (
    <label className="mt-4 flex items-start gap-2 text-sm">
      <input
        type="checkbox"
        checked={done}
        onChange={onChange}
        className="mt-1 h-4 w-4"
      />
      <span>
        Mark this module visited on this device (local-first progress; no account).
      </span>
    </label>
  );
}
