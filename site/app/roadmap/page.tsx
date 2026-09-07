import type { Metadata } from "next";
import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";
import { PHASES, phaseHeading, phaseList, topicTitle } from "@/lib/catalog";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";

export const metadata: Metadata = { title: "Study order" };

export default function RoadmapPage() {
  const modules = loadAllModules();
  const phases = phaseList(modules);

  return (
    <PageShell>
      <PageHeader kicker="What to study next" title="Study order">
        <p>
          Go in this order: parts 0 through 7, then 9 through 11. Part 8 (phone
          apps) can wait until the website and API path is in place. Extra
          topics open after part 7.
        </p>
        <p>
          You do not need a live product to study. You do need the practice
          files on your computer when a topic includes them. This site does not
          mark you as finished.
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
              className="scroll-mt-24 rounded-2xl border border-line bg-paper p-5 shadow-sm"
            >
              <div className="flex flex-wrap items-baseline justify-between gap-2">
                <h2 className="text-xl font-semibold tracking-tight text-stone-900">
                  <span className="mr-2 font-mono text-sm font-medium text-stone-500">
                    {phase}
                  </span>
                  {phaseHeading(phase)}
                </h2>
                <p className="text-sm text-stone-600">
                  {items.length} topic{items.length === 1 ? "" : "s"}
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
                      className="inline-flex items-center rounded-full border border-line bg-background px-2.5 py-1 font-mono text-xs text-ink hover:border-forest hover:bg-white"
                    >
                      {mod.id}
                      <span className="ml-1.5 max-w-[14rem] truncate font-sans text-stone-600">
                        {topicTitle(mod)}
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
        Want a card for each topic instead of this list? Use the{" "}
        <Link href="/learn/" className="text-link underline underline-offset-2">
          lesson list
        </Link>
        .
      </p>
    </PageShell>
  );
}
