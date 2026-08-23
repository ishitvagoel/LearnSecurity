import Link from "next/link";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";

export default function RoadmapPage() {
  const modules = loadAllModules();
  const phases = [...new Set(modules.map((m) => m.phase))].sort((a, b) => a - b);

  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Roadmap</h1>
      <p className="mb-6 max-w-prose leading-relaxed">
        Hard phase order follows blueprint §7 (0→1→2→3→4→5→6→7→9→10→11). Phase 8
        (mobile) depends on identity/data/API foundations. Electives open after
        Phase 7. Mastery gates are checkpoints, not a Top 10 rotation.
      </p>
      {phases.map((phase) => (
        <section key={phase} className="mb-8">
          <h2 className="mb-3 text-2xl font-semibold">
            Phase {phase}
            {phase === 11 ? " (capstone)" : ""}
          </h2>
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
      ))}
    </article>
  );
}
