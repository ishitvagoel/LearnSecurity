import { PageHeader, PageShell } from "@/components/ui";
import { PhaseSection } from "@/components/PhaseSection";
import { phaseList } from "@/lib/catalog";
import { loadAllModules } from "@/lib/loadCurriculum";

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
      {phases.map((phase) => (
        <PhaseSection
          key={phase}
          phase={phase}
          modules={modules.filter((m) => m.phase === phase)}
        />
      ))}
    </PageShell>
  );
}
