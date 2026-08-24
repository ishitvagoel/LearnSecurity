import Link from "next/link";
import { PHASES, phaseList } from "@/lib/catalog";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";

export default function RoadmapPage() {
  const modules = loadAllModules();
  const phases = phaseList(modules);

  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Roadmap</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        Hard order (blueprint §7): 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 9 → 10 → 11.
        Phase 8 (mobile) waits on identity, data, and API foundations. Electives
        open after Phase 7. Mastery gates are evidence checkpoints, not a Top 10
        playlist.
      </p>
      <p className="mb-8 max-w-prose leading-relaxed">
        You do not need a production SecureCollab to study. You do need local
        labs for modules that include a fixture. Product milestones M0–M5 stay
        unmarked until a real product tree exists.
      </p>
      {phases.map((phase) => {
        const meta = PHASES[phase];
        return (
          <section key={phase} className="mb-8">
            <h2 className="mb-2 text-2xl font-semibold">
              Phase {phase}
              {meta ? ` — ${meta.title}` : phase === 11 ? " (capstone)" : ""}
            </h2>
            {meta ? (
              <p className="mb-3 max-w-prose text-stone-800">{meta.blurb}</p>
            ) : null}
            <ul className="list-disc pl-6">
              {modules
                .filter((m) => m.phase === phase)
                .map((m) => (
                  <li key={m.id} className="mb-1">
                    <Link href={moduleHref(m.id)} className="text-blue-900 underline">
                      {m.id} — {m.title}
                    </Link>{" "}
                    <span className="text-stone-700">
                      ({m.track}; {m.difficulty})
                    </span>
                  </li>
                ))}
            </ul>
          </section>
        );
      })}
    </article>
  );
}
