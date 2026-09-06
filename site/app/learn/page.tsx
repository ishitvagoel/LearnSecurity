import { PhaseJump, PhaseSection } from "@/components/PhaseSection";
import { PageHeader, PageShell } from "@/components/ui";
import { phaseList } from "@/lib/catalog";
import { loadAllModules } from "@/lib/loadCurriculum";

export default function LearnIndexPage() {
  const modules = loadAllModules();
  const phases = phaseList(modules);

  return (
    <PageShell>
      <PageHeader kicker="All topics" title="Lessons">
        <p>
          Work through the stages in order. Each topic is one idea you can check,
          not a vendor feature list. Open a topic, then read its pages left to
          right.
        </p>
        <p>
          Answer keys are not on this site. When a topic includes practice, you
          run it on your computer from the course repository.
        </p>
      </PageHeader>
      <PhaseJump phases={phases} />
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
