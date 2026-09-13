import Link from "next/link";
import { notFound } from "next/navigation";
import { ProgressToggle } from "@/components/ProgressToggle";
import { ButtonLink, Chip, PageHeader, PageShell } from "@/components/ui";
import { kindLabel, parseLessonLead, spokenLessonTitle } from "@/lib/headings";
import {
  difficultyLabel,
  formatMinutes,
  maturityLabel,
  phaseHeading,
  topicBlurb,
  topicTitle,
  trackLabel,
} from "@/lib/catalog";
import {
  assessmentHref,
  lessonHref,
  loadAllModules,
  loadLessons,
  loadModule,
} from "@/lib/loadCurriculum";
import { estimateReadingMinutes } from "@/lib/text";

type Props = { params: Promise<{ id: string }> };

export const dynamicParams = false;

export function generateStaticParams() {
  return loadAllModules().map((m) => ({ id: m.id }));
}

export async function generateMetadata({ params }: Props) {
  const { id } = await params;
  const mod = loadAllModules().find((m) => m.id === id);
  return {
    title: mod ? `${mod.id} ${topicTitle(mod)}` : "Topic",
    description: mod ? topicBlurb(mod) : undefined,
  };
}

export default async function ModulePage({ params }: Props) {
  const { id } = await params;
  const exists = loadAllModules().some((m) => m.id === id);
  if (!exists) {
    notFound();
  }
  const mod = loadModule(id);
  const lessons = loadLessons(mod);
  const first = lessons.find((l) => l.filename);

  return (
    <PageShell width="narrow">
      <p className="mb-3 text-sm text-muted">
        <Link href="/learn/" className="text-link underline-offset-2 hover:underline">
          Lessons
        </Link>
        {" · "}
        Part {mod.phase} · {phaseHeading(mod.phase)}
      </p>
      <PageHeader title={`${mod.id} — ${topicTitle(mod)}`}>
        <p>{topicBlurb(mod)}</p>
        <p>
          {lessons.length} page{lessons.length === 1 ? "" : "s"}. Read them in
          order.
          {mod.labSpec
            ? " If there is practice, you run it on your computer — not on a live website."
            : ""}
        </p>
      </PageHeader>
      <div className="mb-6 flex flex-wrap gap-2">
        <Chip>{trackLabel(mod.track)}</Chip>
        <Chip>{difficultyLabel(mod.difficulty)}</Chip>
        <Chip>{formatMinutes(mod.estimatedMinutes)}</Chip>
        <Chip>{maturityLabel(mod.status)}</Chip>
      </div>
      {first ? (
        <p className="mb-4">
          <Link
            href={lessonHref(mod.id, first.filename)}
            className="inline-block rounded-lg bg-forest px-4 py-2 text-sm font-medium text-on-forest hover:bg-forest-hover"
          >
            Open the first page
          </Link>
        </p>
      ) : null}
      <ProgressToggle moduleId={mod.id} />

      <section className="mt-8">
        <h2 className="mb-3 text-xl font-semibold">Pages</h2>
        <ol className="divide-y divide-line overflow-hidden rounded-xl border border-line bg-surface">
          {lessons.map((lo, i) => {
            const spoken = spokenLessonTitle(lo.title, lo.body || "");
            const minutes = lo.body
              ? estimateReadingMinutes(parseLessonLead(lo.body).body)
              : null;
            return (
            <li key={lo.id}>
              {lo.filename ? (
                <Link
                  href={lessonHref(mod.id, lo.filename)}
                  className="flex gap-3 px-4 py-3 hover:bg-surface-hover"
                >
                  <span className="w-6 shrink-0 font-mono text-sm text-muted">
                    {i + 1}
                  </span>
                  <span>
                    <span className="block font-medium text-link">
                      {spoken}
                    </span>
                    <span className="block text-sm text-muted">
                      {kindLabel(lo.kind)}
                      {minutes ? ` · ${formatMinutes(minutes)}` : ""}
                    </span>
                  </span>
                </Link>
              ) : (
                <span className="flex gap-3 px-4 py-3 text-muted">
                  <span className="w-6 shrink-0 font-mono text-sm text-muted">
                    {i + 1}
                  </span>
                  {spoken}
                </span>
              )}
            </li>
            );
          })}
        </ol>
      </section>

      {mod.labSpec ? (
        <section className="mt-10 rounded-xl border border-amber-200 bg-amber-50 px-4 py-4">
          <h2 className="mb-2 text-xl font-semibold">Practice (on your computer)</h2>
          <p className="mb-3 leading-relaxed">
            {topicBlurb(mod)} This website does not run the broken files.
          </p>
          <p>
            <Link
              href={`/labs/${encodeURIComponent(mod.id)}/`}
              className="font-medium text-link underline underline-offset-2"
            >
              How to run the practice
            </Link>
          </p>
        </section>
      ) : null}

      <details className="mt-10 rounded-2xl border border-line bg-paper p-4">
        <summary className="cursor-pointer text-xl font-semibold text-ink">
          Outcomes, prerequisites, and assessment
        </summary>
        <div className="mt-3">
          <h3 className="font-semibold text-ink">What you should be able to show</h3>
          <ul className="mt-3 list-disc space-y-2 pl-5 leading-relaxed text-ink">
            {(mod.outcomes || []).map((outcome) => <li key={outcome}>{outcome}</li>)}
          </ul>
          <p className="mt-4 text-sm leading-relaxed text-muted">
            Prerequisites: {(mod.prerequisites || []).join(" · ") || "None listed"}
          </p>
          <p className="mt-3 text-sm leading-relaxed text-muted">
            References: {(mod.standardsRefs || []).map((standard) => `${standard.source} ${standard.version}`).join(" · ") || "None listed"}
            {mod.masteryGate ? ` · Mastery gate ${mod.masteryGate}` : ""}
          </p>
          <p className="mt-4">
            <ButtonLink href={assessmentHref(mod.id)}>Open the assessment worksheet</ButtonLink>
          </p>
        </div>
      </details>
    </PageShell>
  );
}
