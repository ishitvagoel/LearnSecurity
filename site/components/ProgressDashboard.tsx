"use client";

import type { ReactElement } from "react";
import Link from "next/link";
import { useVisitedModuleIds } from "@/components/ProgressToggle";
import { formatMinutes } from "@/lib/catalog";
import { moduleHref } from "@/lib/hrefs";

export type ProgressModule = { id: string; title: string; minutes: number };
export type ProgressPhase = {
  phase: number;
  title: string;
  blurb: string;
  modules: ProgressModule[];
};

export function ProgressDashboard({
  phases,
  scopeLabel = "course",
}: {
  phases: ProgressPhase[];
  scopeLabel?: string;
}): ReactElement {
  const visited = useVisitedModuleIds();
  const allModules = phases.flatMap((p) => p.modules);
  const totalDone = allModules.filter((m) => visited.includes(m.id)).length;
  const totalCount = allModules.length;
  const overallPct = totalCount === 0 ? 0 : Math.round((totalDone / totalCount) * 100);
  const nextModule = allModules.find((module) => !visited.includes(module.id));
  const remainingMinutes = allModules
    .filter((m) => !visited.includes(m.id))
    .reduce((sum, m) => sum + m.minutes, 0);

  return (
    <div>
      <div className="mb-10 rounded-2xl border border-line bg-paper p-6">
        <div className="flex flex-wrap items-baseline justify-between gap-3">
          <p className="text-lg font-semibold text-ink">
            {totalDone} of {totalCount} topics read
          </p>
          <p className="text-sm text-muted">{overallPct}% through the {scopeLabel}</p>
        </div>
        <div className="mt-3 h-2.5 w-full overflow-hidden rounded-full bg-line" aria-hidden="true">
          <div
            className="h-full bg-forest transition-[width]"
            style={{ width: `${overallPct}%` }}
          />
        </div>
        <p className="mt-3 text-sm text-muted">
          {totalCount === 0
            ? "No topics yet."
            : totalDone === totalCount
              ? `You have marked every topic in the ${scopeLabel} as read.`
              : `${formatMinutes(remainingMinutes)} left across the topics you have not marked read.`}
        </p>
        {nextModule ? (
          <p className="mt-4 text-sm">
            <span className="font-medium text-ink">Next recommended:</span>{" "}
            <Link href={moduleHref(nextModule.id)} className="text-link underline underline-offset-2 hover:no-underline">
              {nextModule.id} — {nextModule.title}
            </Link>
          </p>
        ) : null}
      </div>
      <ol className="space-y-0 border-l border-line">
        {phases.map((group) => {
          const done = group.modules.filter((m) => visited.includes(m.id)).length;
          const total = group.modules.length;
          const pct = total === 0 ? 0 : Math.round((done / total) * 100);
          const complete = total > 0 && done === total;
          return (
            <li key={group.phase} className="relative py-5 pl-8">
              <span
                className={`absolute top-6 -left-3.5 flex h-7 w-7 items-center justify-center rounded-full text-xs font-semibold ${
                  complete
                    ? "bg-forest text-on-forest"
                    : "border border-line bg-surface text-muted"
                }`}
              >
                {group.phase}
              </span>
              <div className="flex flex-wrap items-baseline justify-between gap-2">
                <p className="font-semibold text-ink">{group.title}</p>
                <p className="text-sm text-muted">
                  {done} of {total} read
                </p>
              </div>
              {group.blurb ? (
                <p className="mt-1 max-w-prose text-sm text-muted">{group.blurb}</p>
              ) : null}
              <div
                className="mt-2 h-1.5 w-full max-w-xs overflow-hidden rounded-full bg-line"
                aria-hidden="true"
              >
                <div
                  className="h-full bg-forest transition-[width]"
                  style={{ width: `${pct}%` }}
                />
              </div>
              <ul className="mt-3 flex flex-wrap gap-2">
                {group.modules.map((m) => {
                  const isDone = visited.includes(m.id);
                  return (
                    <li key={m.id}>
                      <Link
                        href={moduleHref(m.id)}
                        className={`inline-flex items-center gap-1.5 rounded-full border px-2.5 py-1 text-xs ${
                          isDone
                            ? "border-forest bg-forest text-on-forest"
                            : "border-line bg-background text-ink hover:border-forest-accent hover:bg-surface"
                        }`}
                      >
                        {m.id}
                        <span className="max-w-[10rem] truncate">{m.title}</span>
                      </Link>
                    </li>
                  );
                })}
              </ul>
            </li>
          );
        })}
      </ol>
    </div>
  );
}
