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

function readVisited(): string[] {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) {
      return [];
    }
    const parsed: unknown = JSON.parse(raw);
    if (!Array.isArray(parsed)) {
      return [];
    }
    return parsed.filter((x): x is string => typeof x === "string");
  } catch {
    return [];
  }
}

function snapshot(moduleId: string): boolean {
  return readVisited().includes(moduleId);
}

export function useVisitedModuleIds(): string[] {
  return useSyncExternalStore(subscribe, readVisited, () => []);
}

export function ProgressToggle({ moduleId }: { moduleId: string }): ReactElement {
  const getSnapshot = useCallback(() => snapshot(moduleId), [moduleId]);
  const done = useSyncExternalStore(subscribe, getSnapshot, () => false);

  const onChange = (): void => {
    const current = snapshot(moduleId);
    let next = readVisited();
    if (current) {
      next = next.filter((x) => x !== moduleId);
    } else {
      next = [...next, moduleId];
    }
    localStorage.setItem(KEY, JSON.stringify(next));
    emit();
  };

  return (
    <label className="mt-2 flex cursor-pointer items-start gap-3 rounded-lg border border-stone-200 bg-white px-3 py-3 text-sm">
      <input
        type="checkbox"
        checked={done}
        onChange={onChange}
        className="mt-0.5 h-4 w-4 shrink-0"
      />
      <span>
        <span className="font-medium text-stone-900">
          {done ? "Visited on this device" : "Mark visited on this device"}
        </span>
        <span className="mt-0.5 block text-stone-600">
          Stored in this browser only. No account.
        </span>
      </span>
    </label>
  );
}
