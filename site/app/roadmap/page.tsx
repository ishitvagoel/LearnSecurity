import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";
import { PHASES, phaseList } from "@/lib/catalog";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";

export default function RoadmapPage() {
  const modules = loadAllModules();
  const phases = phaseList(modules);

  return (
    <PageShell>
      <PageHeader kicker="Order of study" title="Roadmap">
        <p>
          Hard order (blueprint §7): 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 9 → 10 → 11.
          Phase 8 (mobile) waits on identity, data, and API foundations. Electives
          open after Phase 7. Mastery gates are evidence checkpoints, not a Top 10
          playlist.
        </p>
        <p>
          You do not need a production SecureCollab to study. You do need local
          labs for modules that include a fixture. Product milestones M0–M5 stay
          unmarked until a real product tree exists.
        </p>
      </PageHeader>
      <ol className="space-y-4">
        {phases.map((phase) => {
          const meta = PHASES[phase];
          const items = modules.filter((m) => m.phase === phase);
          return (
            <li
              key={phase}
              id={`phase-${phase}`}
              className="scroll-mt-24 rounded-xl border border-stone-200 bg-white p-5 shadow-sm"
            >
              <div className="flex flex-wrap items-baseline justify-between gap-2">
                <h2 className="text-xl font-semibold tracking-tight text-stone-900">
                  <span className="mr-2 font-mono text-sm font-medium text-stone-500">
                    {phase}
                  </span>
                  {meta?.title ?? `Phase ${phase}`}
                </h2>
                <p className="text-sm text-stone-600">
                  {items.length} module{items.length === 1 ? "" : "s"}
                </p>
              </div>
              {meta ? (
                <p className="mt-2 max-w-prose leading-relaxed text-stone-700">{meta.blurb}</p>
              ) : null}
              <ul className="mt-4 flex flex-wrap gap-2">
                {items.map((mod) => (
                  <li key={mod.id}>
                    <Link
                      href={moduleHref(mod.id)}
                      className="inline-flex items-center rounded-full border border-stone-300 bg-stone-50 px-2.5 py-1 font-mono text-xs text-stone-800 hover:border-stone-500 hover:bg-white"
                    >
                      {mod.id}
                      <span className="ml-1.5 max-w-[14rem] truncate font-sans text-stone-600">
                        {mod.title}
                      </span>
                    </Link>
                  </li>
                ))}
              </ul>
            </li>
          );
        })}
      </ol>
      <p className="mt-8 text-sm text-stone-600">
        Prefer cards with outcomes? Use the{" "}
        <Link href="/learn/" className="text-blue-900 underline underline-offset-2">
          catalog
        </Link>
        .
      </p>
    </PageShell>
  );
}
