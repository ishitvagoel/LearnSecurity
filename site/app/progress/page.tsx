import { ProgressDashboard, type ProgressPhase } from "@/components/ProgressDashboard";
import { PageHeader, PageShell } from "@/components/ui";
import { PHASES, phaseHeading, phaseList, topicTitle } from "@/lib/catalog";
import { loadAllModules } from "@/lib/loadCurriculum";
import { routeModules } from "@/lib/route";

export const metadata = {
  title: "Your progress",
  description:
    "How far you've read through the course, tracked in this browser only.",
};

export default function ProgressPage() {
  const modules = routeModules(loadAllModules());
  const phases: ProgressPhase[] = phaseList(modules).map((phase) => ({
    phase,
    title: phaseHeading(phase),
    blurb: PHASES[phase]?.blurb ?? "",
    modules: modules
      .filter((m) => m.phase === phase)
      .map((m) => ({ id: m.id, title: topicTitle(m), minutes: m.estimatedMinutes })),
  }));

  return (
    <PageShell>
      <PageHeader kicker="Tracked in this browser" title="Your progress">
        <p>
          This page reads the “I’ve read this” marks you have set on topic
          pages. Nothing is sent anywhere — clearing your browser data clears
          this too, and it will read as zero on a different computer.
        </p>
      </PageHeader>
      <ProgressDashboard phases={phases} />
    </PageShell>
  );
}
