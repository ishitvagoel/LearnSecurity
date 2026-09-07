import type { Metadata } from "next";
import { PhaseJump, PhaseSection } from "@/components/PhaseSection";
import { PageHeader, PageShell } from "@/components/ui";
import { phaseList } from "@/lib/catalog";
import { loadAllModules } from "@/lib/loadCurriculum";

export const metadata: Metadata = { title: "Lessons" };

export default function LearnIndexPage() {
  const modules = loadAllModules();
  const phases = phaseList(modules);

  return (
    <PageShell>
      <PageHeader kicker="All topics" title="Lessons">
        <p>
          Work through the parts in order. Open a topic, then read its pages
          left to right. Later topics assume you did the earlier ones.
        </p>
        <p>
          Answer keys are not on this site. When a topic includes practice, you
          run it on your computer from the course files on GitHub.
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
