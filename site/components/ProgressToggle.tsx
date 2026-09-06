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

const EMPTY_VISITED: string[] = [];
let cachedRaw: string | null | undefined = undefined;
let cachedIds: string[] = EMPTY_VISITED;

function readVisited(): string[] {
  try {
    const raw = localStorage.getItem(KEY);
    if (raw === cachedRaw) {
      return cachedIds;
    }
    cachedRaw = raw;
    if (!raw) {
      cachedIds = EMPTY_VISITED;
      return cachedIds;
    }
    const parsed: unknown = JSON.parse(raw);
    if (!Array.isArray(parsed)) {
      cachedIds = EMPTY_VISITED;
      return cachedIds;
    }
    cachedIds = parsed.filter((x): x is string => typeof x === "string");
    return cachedIds;
  } catch {
    cachedRaw = undefined;
    cachedIds = EMPTY_VISITED;
    return cachedIds;
  }
}

function snapshot(moduleId: string): boolean {
  return readVisited().includes(moduleId);
}

export function useVisitedModuleIds(): string[] {
  return useSyncExternalStore(subscribe, readVisited, () => EMPTY_VISITED);
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
    <label className="mt-2 flex cursor-pointer items-start gap-3 rounded-2xl border border-line bg-paper px-3 py-3 text-sm">
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
