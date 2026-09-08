"use client";

import { useCallback, useSyncExternalStore, type ReactElement } from "react";
import type { AssessmentEvidence, AssessmentPrompt } from "@/lib/types";

type WorkbookState = {
  status: string;
  answers: Record<string, string>;
  evidence: string[];
};

const EMPTY_STATE: WorkbookState = { status: "not-started", answers: {}, evidence: [] };
const STATUS_OPTIONS = [
  ["not-started", "Not started"],
  ["developing", "Developing"],
  ["competent", "Competent"],
  ["transfer-ready", "Transfer-ready"],
] as const;
const listeners = new Map<string, Set<() => void>>();
const snapshots = new Map<string, { raw: string | null; state: WorkbookState }>();
const memoryFallbacks = new Map<string, WorkbookState>();

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function readState(raw: string | null): WorkbookState {
  if (!raw) {
    return EMPTY_STATE;
  }
  try {
    const parsed: unknown = JSON.parse(raw);
    if (!isRecord(parsed)) {
      return EMPTY_STATE;
    }
    const rawAnswers = isRecord(parsed.answers) ? parsed.answers : {};
    const answers: Record<string, string> = {};
    for (const [key, value] of Object.entries(rawAnswers)) {
      if (typeof value === "string") {
        answers[key] = value;
      }
    }
    const evidence = Array.isArray(parsed.evidence)
      ? parsed.evidence.filter((value): value is string => typeof value === "string")
      : [];
    const status = typeof parsed.status === "string" ? parsed.status : EMPTY_STATE.status;
    return { status, answers, evidence };
  } catch {
    return EMPTY_STATE;
  }
}

function readSnapshot(storageKey: string): WorkbookState {
  if (typeof window === "undefined") {
    return EMPTY_STATE;
  }
  try {
    const raw = window.localStorage.getItem(storageKey);
    const cached = snapshots.get(storageKey);
    if (cached?.raw === raw) {
      return cached.state;
    }
    const state = raw ? readState(raw) : memoryFallbacks.get(storageKey) || EMPTY_STATE;
    snapshots.set(storageKey, { raw, state });
    return state;
  } catch {
    return memoryFallbacks.get(storageKey) || EMPTY_STATE;
  }
}

function emit(storageKey: string): void {
  for (const listener of listeners.get(storageKey) || []) {
    listener();
  }
}

function subscribe(storageKey: string, listener: () => void): () => void {
  const current = listeners.get(storageKey) || new Set<() => void>();
  current.add(listener);
  listeners.set(storageKey, current);
  const onStorage = (event: StorageEvent): void => {
    if (event.key === storageKey) {
      snapshots.delete(storageKey);
      emit(storageKey);
    }
  };
  window.addEventListener("storage", onStorage);
  return () => {
    current.delete(listener);
    window.removeEventListener("storage", onStorage);
    if (current.size === 0) {
      listeners.delete(storageKey);
    }
  };
}

function saveSnapshot(storageKey: string, state: WorkbookState): void {
  memoryFallbacks.set(storageKey, state);
  try {
    window.localStorage.setItem(storageKey, JSON.stringify(state));
  } catch {
    // The in-memory copy keeps the worksheet usable when storage is unavailable.
  }
  snapshots.delete(storageKey);
  emit(storageKey);
}

export function AssessmentWorkbook({
  moduleId,
  sections,
  evidence,
}: {
  moduleId: string;
  sections: AssessmentPrompt[];
  evidence: AssessmentEvidence[];
}): ReactElement {
  const storageKey = "learnsecurity-assessment-v1:" + moduleId;
  const subscribeForKey = useCallback(
    (listener: () => void) => subscribe(storageKey, listener),
    [storageKey],
  );
  const readForKey = useCallback(() => readSnapshot(storageKey), [storageKey]);
  const state = useSyncExternalStore(subscribeForKey, readForKey, () => EMPTY_STATE);
  const setState = useCallback(
    (update: WorkbookState | ((current: WorkbookState) => WorkbookState)): void => {
      const next = typeof update === "function" ? update(readSnapshot(storageKey)) : update;
      saveSnapshot(storageKey, next);
    },
    [storageKey],
  );

  const setAnswer = (id: string, value: string): void => {
    setState((current) => ({
      ...current,
      answers: { ...current.answers, [id]: value },
    }));
  };

  const toggleEvidence = (id: string): void => {
    setState((current) => ({
      ...current,
      evidence: current.evidence.includes(id)
        ? current.evidence.filter((item) => item !== id)
        : [...current.evidence, id],
    }));
  };

  return (
    <div className="space-y-4">
      <div className="rounded-2xl border border-line bg-paper p-4">
        <label className="block text-sm font-medium text-stone-900" htmlFor={`${moduleId}-status`}>
          How does this topic feel right now?
        </label>
        <select
          id={`${moduleId}-status`}
          value={state.status}
          onChange={(event) => setState((current) => ({ ...current, status: event.target.value }))}
          className="mt-2 w-full rounded-lg border border-stone-400 bg-white px-3 py-2 text-sm text-stone-900 sm:w-auto"
        >
          {STATUS_OPTIONS.map(([value, label]) => (
            <option key={value} value={value}>
              {label}
            </option>
          ))}
        </select>
      </div>

      {sections.map((section, index) => (
        <section key={section.id} className="rounded-2xl border border-line bg-paper p-4">
          <label className="block" htmlFor={`${moduleId}-${section.id}`}>
            <span className="block text-sm font-semibold text-stone-900">
              {index + 1}. {section.title}
            </span>
            <span className="mt-2 block leading-relaxed text-stone-800">{section.prompt}</span>
          </label>
          {section.hint ? (
            <p className="mt-2 text-sm leading-relaxed text-stone-600">Helpful reminder: {section.hint}</p>
          ) : null}
          <textarea
            id={`${moduleId}-${section.id}`}
            value={state.answers[section.id] || ""}
            onChange={(event) => setAnswer(section.id, event.target.value)}
            rows={5}
            className="mt-3 block w-full rounded-lg border border-stone-400 bg-white px-3 py-2 text-sm leading-relaxed text-stone-900"
          />
        </section>
      ))}

      {evidence.length > 0 ? (
        <fieldset className="rounded-2xl border border-line bg-paper p-4">
          <legend className="px-1 text-sm font-semibold text-stone-900">Evidence to collect</legend>
          <div className="mt-2 space-y-3">
            {evidence.map((item) => (
              <label key={item.id} className="flex items-start gap-3 text-sm leading-relaxed text-stone-800">
                <input
                  type="checkbox"
                  checked={state.evidence.includes(item.id)}
                  onChange={() => toggleEvidence(item.id)}
                  className="mt-1 h-4 w-4 shrink-0"
                />
                <span>{item.label}</span>
              </label>
            ))}
          </div>
        </fieldset>
      ) : null}

      <p className="text-sm text-stone-600" aria-live="polite">
        Saved in this browser only. This worksheet does not submit answers or grade you.
      </p>
    </div>
  );
}
