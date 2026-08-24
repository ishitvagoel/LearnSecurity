import { PageHeader, PageShell } from "@/components/ui";
import { PhaseSection } from "@/components/PhaseSection";
import { phaseList } from "@/lib/catalog";
import { loadAllModules } from "@/lib/loadCurriculum";

export default function LearnIndexPage() {
  const modules = loadAllModules();
  const phases = phaseList(modules);

  return (
    <PageShell>
      <PageHeader kicker="Catalog" title="Learn">
        <p>
          Work phases in order. Each module is a property of{" "}
          <strong>SecureCollab</strong> (or an elective system), not a vendor
          feature list.
        </p>
        <p>
          Open a module, then read its lessons left-to-right. Answer keys are not
          on this site. Labs run only in your clone of the repository.
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
