import Link from "next/link";
import { notFound } from "next/navigation";
import { AssessmentWorkbook } from "@/components/AssessmentWorkbook";
import { ButtonLink, Chip, PageHeader, PageShell } from "@/components/ui";
import { assessmentEvidence, assessmentPrompts } from "@/lib/assessment";
import {
  difficultyLabel,
  formatMinutes,
  maturityLabel,
  phaseHeading,
  topicBlurb,
  topicTitle,
} from "@/lib/catalog";
import { loadAllModules, loadAssessmentRubric, loadModule, moduleHref } from "@/lib/loadCurriculum";
import { Markdown } from "@/lib/markdown";

type Props = { params: Promise<{ id: string }> };

export const dynamicParams = false;

export function generateStaticParams() {
  return loadAllModules().map((mod) => ({ id: mod.id }));
}

export async function generateMetadata({ params }: Props) {
  const { id } = await params;
  const mod = loadAllModules().find((item) => item.id === id);
  return { title: mod ? `${mod.id} reflection` : "Reflection" };
}

export default async function AssessmentPage({ params }: Props) {
  const { id } = await params;
  const exists = loadAllModules().some((mod) => mod.id === id);
  if (!exists) {
    notFound();
  }
  const mod = loadModule(id);
  const rubric = loadAssessmentRubric(mod);

  return (
    <PageShell width="narrow">
      <p className="mb-3 text-sm text-stone-600">
        <Link href="/assess/" className="text-blue-900 underline-offset-2 hover:underline">
          Reflections
        </Link>
        {" · "}
        <Link href={moduleHref(mod.id)} className="text-blue-900 underline-offset-2 hover:underline">
          {mod.id} — {topicTitle(mod)}
        </Link>
        {" · "}
        Part {mod.phase} · {phaseHeading(mod.phase)}
      </p>
      <PageHeader title={`Reflection — ${mod.id} ${topicTitle(mod)}`}>
        <p>{topicBlurb(mod)}</p>
        <p>
          Write enough that another engineer could check your reasoning. The
          worksheet saves locally and is for self-study; it is not a certificate
          or an automated grade.
        </p>
      </PageHeader>

      <div className="mb-8 flex flex-wrap gap-2">
        <Chip>{maturityLabel(mod.status)}</Chip>
        <Chip>{difficultyLabel(mod.difficulty)}</Chip>
        <Chip>{formatMinutes(mod.estimatedMinutes)}</Chip>
        {mod.masteryGate ? <Chip>Mastery gate {mod.masteryGate}</Chip> : null}
      </div>

      <section className="mb-10 rounded-2xl border border-amber-200 bg-amber-50 p-4">
        <h2 className="text-xl font-semibold text-stone-900">Before you start</h2>
        <p className="mt-2 leading-relaxed text-stone-800">
          This topic is marked {maturityLabel(mod.status).toLowerCase()}. A
          completed reflection is useful evidence, but it does not change the
          repository’s publication status.
        </p>
        <h3 className="mt-5 font-semibold text-stone-900">Prerequisites</h3>
        <ul className="mt-2 list-disc space-y-1 pl-5 leading-relaxed text-stone-800">
          {(mod.prerequisites || []).map((item) => <li key={item}>{item}</li>)}
        </ul>
      </section>

      <section className="mb-10">
        <h2 className="mb-3 text-xl font-semibold">What you should be able to show</h2>
        <ul className="list-disc space-y-2 pl-5 leading-relaxed text-stone-800">
          {(mod.outcomes || []).map((outcome) => <li key={outcome}>{outcome}</li>)}
        </ul>
      </section>

      <section className="mb-10">
        <h2 className="mb-3 text-xl font-semibold">Your reflection workbook</h2>
        <AssessmentWorkbook
          moduleId={mod.id}
          sections={assessmentPrompts(mod)}
          evidence={assessmentEvidence(mod)}
        />
      </section>

      {mod.standardsRefs?.length ? (
        <section className="mb-10">
          <h2 className="mb-3 text-xl font-semibold">Industry references named by this topic</h2>
          <div className="overflow-x-auto rounded-xl border border-line bg-paper">
            <table className="w-full min-w-[34rem] text-left text-sm">
              <caption className="sr-only">Standards references for this reflection</caption>
              <thead className="border-b border-line bg-stone-50 text-stone-600">
                <tr>
                  <th className="px-3 py-2 font-medium">Source</th>
                  <th className="px-3 py-2 font-medium">Version</th>
                  <th className="px-3 py-2 font-medium">Requirements</th>
                </tr>
              </thead>
              <tbody>
                {mod.standardsRefs.map((standard) => (
                  <tr key={`${standard.source}-${standard.version}`} className="border-b border-stone-100 last:border-0">
                    <td className="px-3 py-3 align-top">
                      <a
                        href={standard.url}
                        target="_blank"
                        rel="noreferrer"
                        className="font-medium text-blue-900 underline-offset-2 hover:underline"
                      >
                        {standard.source}
                      </a>
                    </td>
                    <td className="px-3 py-3 align-top whitespace-nowrap text-stone-700">
                      {standard.version} · {standard.status}
                    </td>
                    <td className="px-3 py-3 align-top text-stone-700">
                      {standard.requirementIds.join(", ")}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      ) : null}

      {rubric ? (
        <section className="mb-10">
          <h2 className="mb-3 text-xl font-semibold">Evidence guide</h2>
          <div className="curriculum-prose rounded-2xl border border-line bg-paper p-5">
            <Markdown source={rubric} />
          </div>
        </section>
      ) : null}

      <p>
        <ButtonLink href={moduleHref(mod.id)} variant="secondary">
          Back to the topic
        </ButtonLink>
      </p>
    </PageShell>
  );
}
