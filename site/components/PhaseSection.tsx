import type { ReactElement } from "react";
import Link from "next/link";
import { Chip } from "@/components/ui";
import { PHASES } from "@/lib/catalog";
import { moduleHref } from "@/lib/loadCurriculum";
import type { ModuleMeta } from "@/lib/types";

export function ModuleCard({ mod }: { mod: ModuleMeta }): ReactElement {
  return (
    <Link
      href={moduleHref(mod.id)}
      className="flex h-full flex-col rounded-xl border border-stone-200 bg-white p-4 shadow-sm transition-colors hover:border-stone-400 hover:bg-stone-50"
    >
      <div className="flex items-center justify-between gap-2">
        <p className="font-mono text-xs font-medium text-stone-600">{mod.id}</p>
        <Chip>{mod.track}</Chip>
      </div>
      <h3 className="mt-2 text-base font-semibold text-stone-900">{mod.title}</h3>
      {mod.outcomes[0] ? (
        <p className="mt-2 line-clamp-3 flex-1 text-sm leading-relaxed text-stone-700">
          {mod.outcomes[0]}
        </p>
      ) : null}
      <p className="mt-3 text-xs text-stone-600">
        {mod.difficulty} · {mod.estimatedMinutes} min
      </p>
    </Link>
  );
}

export function PhaseSection({
  phase,
  modules,
}: {
  phase: number;
  modules: ModuleMeta[];
}): ReactElement {
  const meta = PHASES[phase];
  return (
    <section id={`phase-${phase}`} className="mb-12 scroll-mt-24">
      <div className="mb-5 flex flex-wrap items-end justify-between gap-2">
        <div>
          <h2 className="text-2xl font-semibold tracking-tight text-stone-900">
            Phase {phase}
            {meta ? ` — ${meta.title}` : ""}
          </h2>
          {meta ? (
            <p className="mt-2 max-w-prose leading-relaxed text-stone-700">{meta.blurb}</p>
          ) : null}
        </div>
        <p className="text-sm text-stone-600">
          {modules.length} module{modules.length === 1 ? "" : "s"}
        </p>
      </div>
      <ul className="grid gap-3 sm:grid-cols-2">
        {modules.map((m) => (
          <li key={m.id}>
            <ModuleCard mod={m} />
          </li>
        ))}
      </ul>
    </section>
  );
}

export function PhaseJump({ phases }: { phases: number[] }): ReactElement {
  return (
    <nav aria-label="Jump to phase" className="mb-10">
      <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-stone-500">
        Jump to a phase
      </p>
      <ul className="flex flex-wrap gap-2">
        {phases.map((phase) => {
          const meta = PHASES[phase];
          return (
            <li key={phase}>
              <a
                href={`#phase-${phase}`}
                className="inline-flex items-center rounded-full border border-stone-300 bg-white px-3 py-1 text-sm text-stone-800 hover:border-stone-500"
              >
                {phase}
                {meta ? (
                  <span className="ml-1.5 hidden text-stone-500 sm:inline">{meta.title}</span>
                ) : null}
              </a>
            </li>
          );
        })}
      </ul>
    </nav>
  );
}
