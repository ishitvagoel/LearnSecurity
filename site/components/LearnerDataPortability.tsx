"use client";

import { useRef, useState, type ChangeEvent, type ReactElement } from "react";

const PROGRESS_KEY = "learnsecurity-progress-v1";
const ASSESSMENT_PREFIX = "learnsecurity-assessment-v1:";
const FORMAT = "learnsecurity-learner-state";
const VERSION = 1;
const MAX_IMPORT_BYTES = 1_000_000;

type AssessmentState = {
  status: string;
  answers: Record<string, string>;
  evidence: string[];
};

type LearnerExport = {
  format: typeof FORMAT;
  version: typeof VERSION;
  exportedAt: string;
  progress: string[];
  assessments: Record<string, AssessmentState>;
};

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null;
}

function safeStringList(value: unknown): string[] {
  return Array.isArray(value)
    ? value.filter((item): item is string => typeof item === "string").slice(0, 500)
    : [];
}

function safeAssessment(value: unknown): AssessmentState {
  if (!isRecord(value)) {
    return { status: "not-started", answers: {}, evidence: [] };
  }
  const answers: Record<string, string> = {};
  if (isRecord(value.answers)) {
    for (const [key, answer] of Object.entries(value.answers).slice(0, 50)) {
      if (typeof answer === "string") {
        answers[key.slice(0, 120)] = answer.slice(0, 50_000);
      }
    }
  }
  return {
    status: typeof value.status === "string" ? value.status.slice(0, 40) : "not-started",
    answers,
    evidence: safeStringList(value.evidence),
  };
}

function readExport(value: unknown): LearnerExport | null {
  if (!isRecord(value) || value.format !== FORMAT || value.version !== VERSION) {
    return null;
  }
  const assessments: Record<string, AssessmentState> = {};
  if (isRecord(value.assessments)) {
    for (const [key, state] of Object.entries(value.assessments).slice(0, 500)) {
      if (key.startsWith(ASSESSMENT_PREFIX)) {
        assessments[key] = safeAssessment(state);
      }
    }
  }
  return {
    format: FORMAT,
    version: VERSION,
    exportedAt: typeof value.exportedAt === "string" ? value.exportedAt : new Date().toISOString(),
    progress: safeStringList(value.progress),
    assessments,
  };
}

function collectState(): LearnerExport {
  let progress: string[] = [];
  try {
    progress = safeStringList(JSON.parse(window.localStorage.getItem(PROGRESS_KEY) || "[]"));
  } catch {
    // A malformed progress entry should not prevent exporting valid worksheets.
  }
  const assessments: Record<string, AssessmentState> = {};
  for (let index = 0; index < window.localStorage.length; index += 1) {
    const key = window.localStorage.key(index);
    if (!key?.startsWith(ASSESSMENT_PREFIX)) {
      continue;
    }
    try {
      assessments[key] = safeAssessment(JSON.parse(window.localStorage.getItem(key) || "{}"));
    } catch {
      // Ignore malformed local entries while exporting the rest of the work.
    }
  }
  return { format: FORMAT, version: VERSION, exportedAt: new Date().toISOString(), progress, assessments };
}

export function LearnerDataPortability(): ReactElement {
  const inputRef = useRef<HTMLInputElement>(null);
  const [message, setMessage] = useState("");

  const exportState = (): void => {
    const payload = JSON.stringify(collectState(), null, 2);
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
          setMessage("This is not a LearnSecurity work file (version 1).");
          return;
        }
        window.localStorage.setItem(PROGRESS_KEY, JSON.stringify(payload.progress));
        for (const [key, state] of Object.entries(payload.assessments)) {
          window.localStorage.setItem(key, JSON.stringify(state));
        }
        setMessage("Imported. Reloading this page to show the restored work.");
        window.setTimeout(() => window.location.reload(), 350);
      } catch {
        setMessage("The file could not be read as JSON.");
      }
    };
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
      <p className="mt-3 text-xs text-muted" aria-live="polite">
        {message || "The file contains only your local progress and worksheet answers."}
      </p>
    </section>
  );
}
