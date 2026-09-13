"use client";

import { useRef, useState, type ChangeEvent, type ReactElement } from "react";
import { TOPIC_TITLE } from "@/lib/catalog";

const PROGRESS_KEY = "learnsecurity-progress-v1";
const LAST_ACTIVITY_KEY = "learnsecurity-last-activity-v1";
const ASSESSMENT_PREFIX = "learnsecurity-assessment-v1:";
const PRE_IMPORT_BACKUP_KEY = "learnsecurity-pre-import-backup-v1";
const FORMAT = "learnsecurity-learner-state";
const VERSION = 1;
const CONTENT_VERSION = "2026-09-13";
const MAX_IMPORT_BYTES = 1_000_000;
const MAX_ANSWER_CHARS = 50_000;

type AssessmentState = {
  status: string;
  answers: Record<string, string>;
  evidence: string[];
};

type LastActivity = { href: string; title: string };

type LearnerExport = {
  format: typeof FORMAT;
  version: typeof VERSION;
  contentVersion: string;
  exportedAt: string;
  progress: string[];
  assessments: Record<string, AssessmentState>;
  lastActivity?: LastActivity;
};

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function safeStringList(value: unknown): string[] {
  return Array.isArray(value)
    ? value.filter((item): item is string => typeof item === "string")
    : [];
}

function safeProgress(value: unknown): string[] {
  return safeStringList(value).filter((moduleId) => Boolean(TOPIC_TITLE[moduleId]));
}

function safeAssessment(value: unknown): AssessmentState | null {
  if (!isRecord(value)) {
    return null;
  }
  const answers: Record<string, string> = {};
  if (isRecord(value.answers)) {
    for (const [key, answer] of Object.entries(value.answers)) {
      if (typeof answer !== "string" || answer.length > MAX_ANSWER_CHARS) {
        return null;
      }
      answers[key] = answer;
    }
  }
  return {
    status: typeof value.status === "string" ? value.status : "not-started",
    answers,
    evidence: safeStringList(value.evidence),
  };
}

function safeLastActivity(value: unknown): LastActivity | undefined {
  if (!isRecord(value) || typeof value.href !== "string" || typeof value.title !== "string") {
    return undefined;
  }
  const href = value.href.slice(0, 240);
  if (!["/learn/", "/labs/", "/assess/", "/bridges/"].some((prefix) => href.startsWith(prefix))) {
    return undefined;
  }
  return { href, title: value.title.slice(0, 200) };
}

function readExport(value: unknown): LearnerExport | null {
  if (!isRecord(value) || value.format !== FORMAT || value.version !== VERSION) {
    return null;
  }
  const assessments: Record<string, AssessmentState> = {};
  if (isRecord(value.assessments)) {
    for (const [key, state] of Object.entries(value.assessments)) {
      if (key.startsWith(ASSESSMENT_PREFIX)) {
        const moduleId = key.slice(ASSESSMENT_PREFIX.length);
        if (!TOPIC_TITLE[moduleId]) return null;
        const parsed = safeAssessment(state);
        if (!parsed) {
          return null;
        }
        assessments[key] = parsed;
      }
    }
  }
  return {
    format: FORMAT,
    version: VERSION,
    contentVersion: typeof value.contentVersion === "string" ? value.contentVersion : "unknown",
    exportedAt: typeof value.exportedAt === "string" ? value.exportedAt : new Date().toISOString(),
    progress: safeProgress(value.progress),
    assessments,
    lastActivity: safeLastActivity(value.lastActivity),
  };
}

function collectState(): LearnerExport {
  let storage: Storage | null = null;
  try {
    storage = window.localStorage;
  } catch {
    // Continue with an empty snapshot; the caller can still preserve a draft
    // in memory or report that storage is unavailable.
  }
  let progress: string[] = [];
  try {
    progress = safeProgress(JSON.parse(storage?.getItem(PROGRESS_KEY) || "[]"));
  } catch {
    // A malformed progress entry should not prevent exporting valid worksheets.
  }
  const assessments: Record<string, AssessmentState> = {};
  for (let index = 0; storage && index < storage.length; index += 1) {
    const key = storage.key(index);
    if (!key?.startsWith(ASSESSMENT_PREFIX)) {
      continue;
    }
    try {
      const assessment = safeAssessment(JSON.parse(storage.getItem(key) || "{}"));
      if (assessment) assessments[key] = assessment;
    } catch {
      // Ignore malformed local entries while exporting the rest of the work.
    }
  }
  let lastActivity: LastActivity | undefined;
  try {
    lastActivity = safeLastActivity(JSON.parse(storage?.getItem(LAST_ACTIVITY_KEY) || "null"));
  } catch {
    // Ignore a malformed continuation pointer while exporting the rest of the work.
  }
  return {
    format: FORMAT,
    version: VERSION,
    contentVersion: CONTENT_VERSION,
    exportedAt: new Date().toISOString(),
    progress,
    assessments,
    lastActivity,
  };
}

export function LearnerDataPortability(): ReactElement {
  const inputRef = useRef<HTMLInputElement>(null);
  const [message, setMessage] = useState("");
  const [pendingImport, setPendingImport] = useState<LearnerExport | null>(null);

  const applyImport = (payload: LearnerExport): void => {
    let storage: Storage;
    try {
      storage = window.localStorage;
    } catch {
      setMessage("Your browser does not provide storage. Existing local work was preserved.");
      return;
    }
    const previous = new Map<string, string | null>();
    const existingAssessmentKeys: string[] = [];
    for (let index = 0; index < storage.length; index += 1) {
      const key = storage.key(index);
      if (key && (key === PROGRESS_KEY || key === LAST_ACTIVITY_KEY || key === PRE_IMPORT_BACKUP_KEY || key.startsWith(ASSESSMENT_PREFIX))) {
        previous.set(key, storage.getItem(key));
        if (key.startsWith(ASSESSMENT_PREFIX)) existingAssessmentKeys.push(key);
      }
    }
    try {
      // Keep one recoverable snapshot before replacing work. It is bounded by
      // the same limit as the downloaded file.
      const backup = JSON.stringify(collectState());
      if (new TextEncoder().encode(backup).byteLength <= MAX_IMPORT_BYTES) {
        storage.setItem(PRE_IMPORT_BACKUP_KEY, backup);
      }
      storage.setItem(PROGRESS_KEY, JSON.stringify(payload.progress));
      if (payload.lastActivity) {
        storage.setItem(LAST_ACTIVITY_KEY, JSON.stringify(payload.lastActivity));
      } else {
        storage.removeItem(LAST_ACTIVITY_KEY);
      }
      const importedKeys = new Set(Object.keys(payload.assessments));
      for (const key of existingAssessmentKeys) {
        if (!importedKeys.has(key)) storage.removeItem(key);
      }
      for (const [key, state] of Object.entries(payload.assessments)) {
        storage.setItem(key, JSON.stringify(state));
      }
    } catch {
      for (const [key, value] of previous) {
        try {
          if (value === null) storage.removeItem(key);
          else storage.setItem(key, value);
        } catch {
          // Best-effort rollback; the original values were captured above.
        }
      }
      setPendingImport(null);
      setMessage("Your browser storage rejected the import. Existing local work was preserved.");
      return;
    }
    setPendingImport(null);
    setMessage("Imported. Reloading this page to show the restored work.");
    window.setTimeout(() => window.location.reload(), 350);
  };

  const restoreBackup = (): void => {
    try {
      const raw = window.localStorage.getItem(PRE_IMPORT_BACKUP_KEY);
      const backup = raw ? readExport(JSON.parse(raw)) : null;
      if (!backup) {
        setMessage("The previous browser snapshot is no longer available.");
        return;
      }
      applyImport(backup);
    } catch {
      setMessage("The previous browser snapshot could not be read. Existing local work was preserved.");
    }
  };

  const exportState = (): void => {
    const payload = JSON.stringify(collectState(), null, 2);
    if (new TextEncoder().encode(payload).byteLength > MAX_IMPORT_BYTES) {
      setMessage("Your work is larger than the supported import size; shorten an unusually long answer before exporting.");
      return;
    }
    const blob = new Blob([payload], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = `learnsecurity-work-${new Date().toISOString().slice(0, 10)}.json`;
    anchor.click();
    URL.revokeObjectURL(url);
    setMessage("Downloaded your local reading marks and assessment work.");
  };

  const importState = (event: ChangeEvent<HTMLInputElement>): void => {
    const file = event.target.files?.[0];
    event.target.value = "";
    if (!file) {
      return;
    }
    if (file.size > MAX_IMPORT_BYTES) {
      setMessage("That file is too large to import.");
      return;
    }
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const parsed: unknown = JSON.parse(String(reader.result));
        const payload = readExport(parsed);
        if (!payload) {
          setMessage("This is not a valid LearnSecurity work file (version 1), or one of its records is invalid.");
          return;
        }
        setPendingImport(payload);
        setMessage("Review the replacement summary before importing.");
      } catch {
        setMessage("The selected file is not valid JSON. Your existing local work was preserved.");
      }
    };
    reader.onerror = () => setMessage("The file could not be read. Your existing local work was preserved.");
    reader.readAsText(file);
  };

  return (
    <section className="mb-10 rounded-2xl border border-line bg-surface p-5">
      <h2 className="text-xl font-semibold text-ink">Move your work</h2>
      <p className="mt-2 max-w-prose text-sm leading-relaxed text-muted">
        Progress and assessment notes stay in this browser by default. Export a versioned copy before changing devices; import it on the other device to continue.
      </p>
      <div className="mt-4 flex flex-wrap gap-3">
        <button
          type="button"
          onClick={exportState}
          className="rounded-full bg-forest px-4 py-2 text-sm font-medium text-on-forest hover:bg-forest-hover"
        >
          Download my work
        </button>
        <button
          type="button"
          onClick={() => inputRef.current?.click()}
          className="rounded-full border border-border bg-paper px-4 py-2 text-sm font-medium text-ink hover:border-forest-accent"
        >
          Import a work file
        </button>
        <input ref={inputRef} type="file" accept="application/json" onChange={importState} className="sr-only" />
      </div>
      {pendingImport ? (
        <div className="mt-4 rounded-xl border border-amber-300 bg-amber-50 p-4 text-sm text-ink">
          <p className="font-semibold">Replace the work in this browser?</p>
          <p className="mt-1 leading-relaxed">
            This file contains {pendingImport.progress.length} reading mark{pendingImport.progress.length === 1 ? "" : "s"} and {Object.keys(pendingImport.assessments).length} worksheet record{Object.keys(pendingImport.assessments).length === 1 ? "" : "s"}. Existing reading marks and worksheet records will be replaced. A one-step backup is kept in this browser when storage allows.
          </p>
          <div className="mt-3 flex flex-wrap gap-3">
            <button
              type="button"
              onClick={() => applyImport(pendingImport)}
              className="rounded-full bg-forest px-4 py-2 text-sm font-medium text-on-forest hover:bg-forest-hover"
            >
              Replace and reload
            </button>
            <button
              type="button"
              onClick={() => { setPendingImport(null); setMessage("Import cancelled. Existing local work is unchanged."); }}
              className="rounded-full border border-border bg-paper px-4 py-2 text-sm font-medium text-ink hover:border-forest-accent"
            >
              Cancel
            </button>
          </div>
        </div>
      ) : null}
      {!pendingImport ? (
        <p className="mt-4 text-sm">
          <button type="button" onClick={restoreBackup} className="text-link underline underline-offset-2 hover:no-underline">
            Restore the previous browser snapshot
          </button>
        </p>
      ) : null}
      <p className="mt-3 text-xs text-muted" aria-live="polite">
        {message || "The file contains only your local progress and worksheet answers."}
      </p>
    </section>
  );
}
