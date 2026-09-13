import Link from "next/link";
import { Chip, PageHeader, PageShell } from "@/components/ui";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";
import { loadProjectMilestones } from "@/lib/project";

export const metadata = {
  title: "Project milestones",
  description: "Follow the SecureCollab learner project from its first request trace to the defended capstone.",
};

const STATUS_LABEL: Record<string, string> = {
  planned: "Planned",
  optional: "Optional extension",
  "teaching-stand-in": "Teaching stand-in",
};

export default function ProjectPage() {
  const project = loadProjectMilestones();
  const moduleIds = new Set(loadAllModules().map((module) => module.id));
  return (
    <PageShell width="narrow">
      <PageHeader kicker="One evolving artifact" title={`${project.product} milestones`}>
        <p>
          Each milestone changes the same notes-app design. The learner records the new request or state flow, the earlier rule it threatens, the check that now matters, and the decision that resolves the change.
        </p>
        <p>
          “Planned” is an honest status: it names the intended evidence without pretending that the current teaching fixture is a running product.
        </p>
      </PageHeader>
      <ol className="relative space-y-4 border-l border-line pl-6">
        {project.milestones.map((milestone) => (
          <li key={milestone.id} className="relative rounded-2xl border border-line bg-paper p-5 shadow-sm">
            <span className="absolute -left-[2.05rem] top-5 flex h-7 w-7 items-center justify-center rounded-full bg-forest text-xs font-semibold text-on-forest">
              {milestone.id.replace("M", "")}
            </span>
            <div className="flex flex-wrap items-center justify-between gap-2">
              <h2 className="text-xl font-semibold text-ink">{milestone.title}</h2>
              <Chip>{STATUS_LABEL[milestone.status] || milestone.status}</Chip>
            </div>
            <p className="mt-3 leading-relaxed text-muted">{milestone.summary}</p>
            <h3 className="mt-4 text-sm font-semibold text-ink">Evidence to produce</h3>
            <ul className="mt-2 list-disc space-y-1 pl-5 text-sm leading-relaxed text-muted">
              {milestone.learnerArtifacts.map((artifact) => <li key={artifact}>{artifact}</li>)}
            </ul>
            <p className="mt-4 rounded-xl border border-forest-accent/20 bg-surface px-3 py-2 text-sm leading-relaxed text-ink">
              <span className="font-medium">Revisit:</span> {milestone.revisit}
            </p>
            <div className="mt-4 flex flex-wrap items-center gap-4">
              {moduleIds.has(milestone.moduleId) ? (
                <Link href={moduleHref(milestone.moduleId)} className="text-sm font-medium text-link underline-offset-2 hover:underline">
                  Start with module {milestone.moduleId} →
                </Link>
              ) : null}
              {milestone.labPath ? (
                <code className="rounded bg-surface px-2 py-1 text-xs text-muted">{milestone.labPath}</code>
              ) : null}
            </div>
          </li>
        ))}
      </ol>
      <p className="mt-8 text-sm text-muted">
        Read the related design notes in the <Link href="/reference/" className="text-link underline underline-offset-2">notes-app reference</Link> and use the <Link href="/capstone/" className="text-link underline underline-offset-2">capstone brief</Link> only after the route work is complete.
      </p>
    </PageShell>
  );
}
