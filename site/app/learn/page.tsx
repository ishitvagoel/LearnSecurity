import Link from "next/link";
import { OverallProgress } from "@/components/ModuleProgress";
import { PhaseJump, PhaseSection } from "@/components/PhaseSection";
import { PageHeader, PageShell } from "@/components/ui";
import { phaseList } from "@/lib/catalog";
import { loadAllModules } from "@/lib/loadCurriculum";

export const metadata = {
  title: "Lessons",
  description:
    "All topics in this free security engineering course, in study order — from ground rules through logins, data, bad input, APIs, and shipping.",
};

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
            assessment worksheets
          </Link>{" "}
          to keep your own evidence as you study.
        </p>
      </PageHeader>
      <div className="mb-8">
        <OverallProgress moduleIds={modules.map((m) => m.id)} />
      </div>
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
