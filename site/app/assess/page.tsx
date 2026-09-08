import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";
import { maturityLabel, phaseHeading, phaseList, topicBlurb, topicTitle } from "@/lib/catalog";
import { assessmentHref } from "@/lib/loadCurriculum";
import { loadAllModules } from "@/lib/loadCurriculum";

export default function ReflectionsPage() {
  const modules = loadAllModules();
  return (
    <PageShell>
      <PageHeader kicker="Show your work" title="Reflection workbooks">
        <p>
          Use a reflection workbook after each topic to state the rule, explain
          the break, plan the fix, and collect evidence. Your notes stay in this
          browser; this site does not submit or grade them.
        </p>
      </PageHeader>
      {phaseList(modules).map((phase) => (
        <section key={phase} className="mb-10">
          <h2 className="mb-3 text-xl font-semibold">
            Part {phase} — {phaseHeading(phase)}
          </h2>
          <ul className="grid gap-3 sm:grid-cols-2">
            {modules
              .filter((mod) => mod.phase === phase)
              .map((mod) => (
                <li key={mod.id}>
                  <Link
                    href={assessmentHref(mod.id)}
                    className="block h-full rounded-2xl border border-line bg-paper p-4 shadow-sm transition hover:-translate-y-0.5 hover:border-forest/40 hover:shadow-md"
                  >
                    <div className="flex flex-wrap items-center gap-2">
                      <span className="font-mono text-xs text-stone-600">{mod.id}</span>
                      <span className="rounded-full border border-line px-2 py-0.5 text-xs text-stone-700">
                        {maturityLabel(mod.status)}
                      </span>
                    </div>
                    <p className="mt-2 font-semibold text-blue-900">{topicTitle(mod)}</p>
                    <p className="mt-2 line-clamp-3 text-sm leading-relaxed text-stone-700">
                      {topicBlurb(mod)}
                    </p>
                  </Link>
                </li>
              ))}
          </ul>
        </section>
      ))}
    </PageShell>
  );
}
