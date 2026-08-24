import type { ReactElement } from "react";
import Link from "next/link";
import { PHASES } from "@/lib/catalog";
import { moduleHref } from "@/lib/loadCurriculum";
import type { ModuleMeta } from "@/lib/types";

export function ModuleCard({ mod }: { mod: ModuleMeta }): ReactElement {
  return (
    <Link
      href={moduleHref(mod.id)}
      className="flex h-full flex-col rounded-xl border border-stone-200 bg-white p-4 shadow-sm transition-colors hover:border-stone-400 hover:bg-stone-50"
    >
      <p className="font-mono text-xs font-medium text-stone-600">{mod.id}</p>
      <h3 className="mt-1 text-base font-semibold text-stone-900">{mod.title}</h3>
      {mod.outcomes[0] ? (
        <p className="mt-2 line-clamp-3 flex-1 text-sm leading-relaxed text-stone-700">
          {mod.outcomes[0]}
        </p>
      ) : null}
      <p className="mt-3 text-xs text-stone-600">
        {mod.track} · {mod.difficulty} · {mod.estimatedMinutes} min
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
    <section className="mb-12">
      <h2 className="text-2xl font-semibold tracking-tight text-stone-900">
        Phase {phase}
        {meta ? ` — ${meta.title}` : ""}
      </h2>
      {meta ? (
        <p className="mt-2 mb-5 max-w-prose leading-relaxed text-stone-700">{meta.blurb}</p>
      ) : null}
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
