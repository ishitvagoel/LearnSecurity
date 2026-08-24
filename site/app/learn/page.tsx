import Link from "next/link";
import { PHASES, phaseList } from "@/lib/catalog";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";

export default function LearnIndexPage() {
  const modules = loadAllModules();
  const phases = phaseList(modules);

  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Learn</h1>
      <p className="mb-8 max-w-prose leading-relaxed">
        Work phases in order. Each module is a property of{" "}
        <strong>SecureCollab</strong> (or an elective system), not a vendor
        feature list. Lessons are on this site; answer keys are not. Labs run
        only in your clone of the repository.
      </p>
      {phases.map((phase) => {
        const meta = PHASES[phase];
        const items = modules.filter((m) => m.phase === phase);
        return (
          <section key={phase} className="mb-10">
            <h2 className="mb-2 text-2xl font-semibold">
              Phase {phase}
              {meta ? ` — ${meta.title}` : ""}
            </h2>
            {meta ? (
              <p className="mb-4 max-w-prose text-stone-800">{meta.blurb}</p>
            ) : null}
            <ul className="divide-y divide-stone-200 border-y border-stone-200">
              {items.map((m) => (
                <li key={m.id} className="py-3">
                  <Link
                    href={moduleHref(m.id)}
                    className="font-medium text-blue-900 underline"
                  >
                    {m.id} — {m.title}
                  </Link>
                  <p className="mt-1 max-w-prose text-sm text-stone-700">
                    {m.track} · {m.difficulty} · {m.estimatedMinutes} min
                    {m.outcomes[0] ? ` · ${m.outcomes[0]}` : ""}
                  </p>
                </li>
              ))}
            </ul>
          </section>
        );
      })}
    </article>
  );
}
