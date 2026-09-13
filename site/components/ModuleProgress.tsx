"use client";

import type { ReactElement } from "react";
import { useVisitedModuleIds } from "@/components/ProgressToggle";

export function ModuleDoneBadge({ moduleId }: { moduleId: string }): ReactElement | null {
  const visited = useVisitedModuleIds();
  if (!visited.includes(moduleId)) {
    return null;
  }
  return (
    <span className="inline-flex items-center gap-1 rounded-full bg-forest px-2 py-0.5 text-[0.7rem] font-medium text-on-forest">
      <svg viewBox="0 0 16 16" className="h-3 w-3" aria-hidden="true" fill="none">
        <path
          d="M3.5 8.5l2.8 2.8L12.5 5"
          stroke="currentColor"
          strokeWidth="1.8"
          strokeLinecap="round"
          strokeLinejoin="round"
        />
      </svg>
      Read
    </span>
  );
}

export function OverallProgress({ moduleIds }: { moduleIds: string[] }): ReactElement | null {
  const visited = useVisitedModuleIds();
  const total = moduleIds.length;
  if (total === 0) {
    return null;
  }
  const done = moduleIds.filter((id) => visited.includes(id)).length;
  if (done === 0) {
    return null;
  }
  const pct = Math.round((done / total) * 100);
  return (
    <div className="flex items-center gap-3 rounded-2xl border border-line bg-paper px-4 py-3 text-sm">
      <div className="h-2 w-32 overflow-hidden rounded-full bg-line" aria-hidden="true">
        <div className="h-full bg-forest transition-[width]" style={{ width: `${pct}%` }} />
      </div>
      <span className="text-stone-700">
        You have marked <strong className="text-ink">{done}</strong> of {total} topics as read
        on this computer.
      </span>
    </div>
  );
}

export function PhaseProgress({ moduleIds }: { moduleIds: string[] }): ReactElement | null {
  const visited = useVisitedModuleIds();
  const total = moduleIds.length;
  if (total === 0) {
    return null;
  }
  const done = moduleIds.filter((id) => visited.includes(id)).length;
  const pct = Math.round((done / total) * 100);
  return (
    <div className="flex items-center gap-2">
      <div className="h-1.5 w-20 overflow-hidden rounded-full bg-line" aria-hidden="true">
        <div className="h-full bg-forest transition-[width]" style={{ width: `${pct}%` }} />
      </div>
      <span className="text-sm text-stone-600">
        {done} of {total} read
      </span>
    </div>
  );
}
