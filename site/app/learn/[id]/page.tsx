import Link from "next/link";
import { notFound } from "next/navigation";
import { ProgressToggle } from "@/components/ProgressToggle";
import { Chip, PageHeader, PageShell } from "@/components/ui";
import { kindLabel } from "@/lib/headings";
import {
  difficultyLabel,
  formatMinutes,
  phaseHeading,
  topicBlurb,
  topicTitle,
  trackLabel,
} from "@/lib/catalog";
import {
  lessonHref,
  loadAllModules,
  loadLessons,
  loadModule,
} from "@/lib/loadCurriculum";

type Props = { params: Promise<{ id: string }> };

export const dynamicParams = false;

export function generateStaticParams() {
  return loadAllModules().map((m) => ({ id: m.id }));
}

export async function generateMetadata({ params }: Props) {
  const { id } = await params;
  const mod = loadAllModules().find((m) => m.id === id);
  return { title: mod ? `${mod.id} ${topicTitle(mod)}` : "Topic" };
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
      <p className="mb-3 text-sm text-stone-600">
        <Link href="/learn/" className="text-blue-900 underline-offset-2 hover:underline">
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
      </div>
      {first ? (
        <p className="mb-4">
          <Link
            href={lessonHref(mod.id, first.filename)}
            className="inline-block rounded-lg bg-blue-900 px-4 py-2 text-sm font-medium text-white hover:bg-blue-800"
          >
            Open the first page
          </Link>
        </p>
      ) : null}
      <ProgressToggle moduleId={mod.id} />

      <section className="mt-10">
        <h2 className="mb-3 text-xl font-semibold">Pages</h2>
        <ol className="divide-y divide-stone-200 overflow-hidden rounded-xl border border-stone-200 bg-white">
          {lessons.map((lo, i) => (
            <li key={lo.id}>
              {lo.filename ? (
                <Link
                  href={lessonHref(mod.id, lo.filename)}
                  className="flex gap-3 px-4 py-3 hover:bg-stone-50"
                >
                  <span className="w-6 shrink-0 font-mono text-sm text-stone-500">
                    {i + 1}
                  </span>
                  <span>
                    <span className="block font-medium text-blue-900">{lo.title}</span>
                    <span className="block text-sm text-stone-600">{kindLabel(lo.kind)}</span>
                  </span>
                </Link>
              ) : (
                <span className="flex gap-3 px-4 py-3 text-stone-700">
                  <span className="w-6 shrink-0 font-mono text-sm text-stone-500">
                    {i + 1}
                  </span>
                  {lo.title}
                </span>
              )}
            </li>
          ))}
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
              className="font-medium text-blue-900 underline underline-offset-2"
            >
              How to run the practice
            </Link>
          </p>
        </section>
      ) : null}
    </PageShell>
  );
}
