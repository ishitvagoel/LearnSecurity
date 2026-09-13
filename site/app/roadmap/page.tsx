import Link from "next/link";
import { ModuleDoneBadge, PhaseProgress } from "@/components/ModuleProgress";
import { PageHeader, PageShell } from "@/components/ui";
import { PHASES, phaseHeading, phaseList, topicTitle } from "@/lib/catalog";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";
import { routeLabel, routeModules } from "@/lib/route";

const PROJECT_THREAD: Record<number, { artifact: string; moduleId: string }> = {
  0: { artifact: "Scope and learning contract", moduleId: "0.1" },
  1: { artifact: "SecureCollab invariant and authority catalogue", moduleId: "1.1" },
  2: { artifact: "Executable policy and access matrix", moduleId: "1.2" },
  3: { artifact: "Trust-boundary and attack-surface model", moduleId: "1.3" },
  4: { artifact: "Risk register and residual-risk decisions", moduleId: "1.4" },
  5: { artifact: "Data and secret handling decisions", moduleId: "5.1" },
  6: { artifact: "Input and parser safety checks", moduleId: "6.1" },
  7: { artifact: "API, worker, and evidence flows", moduleId: "7.1" },
  9: { artifact: "Independent retest and evidence record", moduleId: "9.1" },
  10: { artifact: "Release and recovery controls", moduleId: "10.1" },
  11: { artifact: "Capstone SecureCollab implementation", moduleId: "11" },
};

export const metadata = {
  title: "Study order",
  description:
    "What to study next and in what order, from ground rules through the final project.",
};

export default function RoadmapPage() {
  const route = routeModules(loadAllModules());
  const phases = phaseList(route);

  return (
    <PageShell>
      <PageHeader kicker="What to study next" title="Study order">
        <p>
          Follow the {routeLabel()}: parts 0 through 7, then 9 through 11. Phone
          apps are an extension after the web/API foundations, and extra topics
          open after part 7.
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
          const items = route.filter((m) => m.phase === phase);
          return (
            <li
              key={phase}
              id={`phase-${phase}`}
              className="scroll-mt-24 rounded-2xl border border-line bg-paper p-5 shadow-sm"
            >
              <div className="flex flex-wrap items-baseline justify-between gap-2">
                <h2 className="text-xl font-semibold tracking-tight text-ink">
                  <span className="mr-2 font-mono text-sm font-medium text-muted">
                    {phase}
                  </span>
                  {phaseHeading(phase)}
                </h2>
                <div className="flex flex-col items-end gap-1.5">
                  <p className="text-sm text-muted">
                    {items.length} topic{items.length === 1 ? "" : "s"}
                  </p>
                  <PhaseProgress moduleIds={items.map((m) => m.id)} />
                </div>
              </div>
              {meta ? (
                <p className="mt-2 max-w-prose leading-relaxed text-muted">{meta.blurb}</p>
              ) : null}
              {PROJECT_THREAD[phase] ? (
                <p className="mt-3 rounded-xl border border-forest-accent/20 bg-surface px-3 py-2 text-sm text-ink">
                  <span className="font-medium">Project thread:</span>{" "}
                  {PROJECT_THREAD[phase].artifact}. Start with{" "}
                  <Link href={moduleHref(PROJECT_THREAD[phase].moduleId)} className="text-link underline underline-offset-2">
                    {PROJECT_THREAD[phase].moduleId}
                  </Link>
                  , then add the phase&apos;s evidence to the same record.
                </p>
              ) : null}
              <ul className="mt-4 flex flex-wrap gap-2">
                {items.map((mod) => (
                  <li key={mod.id}>
                    <Link
                      href={moduleHref(mod.id)}
                      className="inline-flex items-center gap-1.5 rounded-full border border-line bg-background px-2.5 py-1 font-mono text-xs text-ink hover:border-forest-accent hover:bg-surface"
                    >
                      {mod.id}
                      <span className="max-w-[14rem] truncate font-sans text-muted">
                        {topicTitle(mod)}
                      </span>
                      <ModuleDoneBadge moduleId={mod.id} />
                    </Link>
                  </li>
                ))}
              </ul>
            </li>
          );
        })}
      </ol>
      <section className="mt-10 rounded-2xl border border-line bg-surface p-5">
        <h2 className="text-xl font-semibold text-ink">Optional after the route</h2>
        <p className="mt-2 leading-relaxed text-muted">Part 8 covers mobile apps. E1–E6 are electives. They remain available from the lesson list without counting against completion of the recommended web/API route.</p>
      </section>
      <p className="mt-8 text-sm text-muted">
        Want a card for each topic instead of this list? Use the{" "}
        <Link href="/learn/" className="text-link underline underline-offset-2">
          lesson list
        </Link>
        .
      </p>
    </PageShell>
  );
}
