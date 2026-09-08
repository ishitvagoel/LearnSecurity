import Link from "next/link";
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
          Work through the parts in order. Open a topic, then read its pages
          left to right. Later topics assume you did the earlier ones.
        </p>
        <p>
          Answer keys are not on this site. When a topic includes practice, you
          run it on your computer from the course files on GitHub.
        </p>
        <p>
          Most topics are drafts awaiting independent review. Use the{" "}
          <Link href="/assess/" className="text-blue-900 underline underline-offset-2">
            reflection worksheets
          </Link>{" "}
          to keep your own evidence as you study.
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
