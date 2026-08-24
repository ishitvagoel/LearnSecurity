import Link from "next/link";
import { notFound } from "next/navigation";
import { ProgressToggle } from "@/components/ProgressToggle";
import { Chip, PageHeader, PageShell } from "@/components/ui";
import { kindLabel } from "@/lib/headings";
import { PHASES } from "@/lib/catalog";
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
  return { title: mod ? `${mod.id} ${mod.title}` : "Module" };
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
  const phase = PHASES[mod.phase];

  return (
    <PageShell width="narrow">
      <p className="mb-3 text-sm text-stone-600">
        <Link href="/learn/" className="text-blue-900 underline-offset-2 hover:underline">
          Learn
        </Link>
        {" · "}
        Phase {mod.phase}
        {phase ? ` · ${phase.title}` : ""}
      </p>
      <PageHeader title={`${mod.id} — ${mod.title}`}>
        <p>
          This module has {lessons.length} lesson{lessons.length === 1 ? "" : "s"}.
          Read them in order. The lab, if this module has one, is a local
          fixture — not a live target.
        </p>
      </PageHeader>
      <div className="mb-6 flex flex-wrap gap-2">
        <Chip>{mod.track}</Chip>
        <Chip>{mod.difficulty}</Chip>
        <Chip>{mod.estimatedMinutes} min</Chip>
      </div>
      {first ? (
        <p className="mb-4">
          <Link
            href={lessonHref(mod.id, first.filename)}
            className="inline-block rounded-lg bg-blue-900 px-4 py-2 text-sm font-medium text-white hover:bg-blue-800"
          >
            Open first lesson
          </Link>
        </p>
      ) : null}
      <ProgressToggle moduleId={mod.id} />

      <section className="mt-10">
        <h2 className="mb-3 text-xl font-semibold">Lessons</h2>
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

      <section className="mt-10">
        <h2 className="mb-3 text-xl font-semibold">What you should be able to do</h2>
        <ul className="list-disc space-y-2 pl-5 leading-relaxed">
          {mod.outcomes.map((o) => (
            <li key={o}>{o}</li>
          ))}
        </ul>
      </section>

      <section className="mt-10">
        <h2 className="mb-3 text-xl font-semibold">Invariants this module owns</h2>
        <ul className="list-disc space-y-2 pl-5 leading-relaxed">
          {mod.invariants.map((o) => (
            <li key={o}>{o}</li>
          ))}
        </ul>
      </section>

      {mod.threatModelPrompts?.length ? (
        <section className="mt-10">
          <h2 className="mb-3 text-xl font-semibold">Threat prompts</h2>
          <ul className="list-disc space-y-2 pl-5 leading-relaxed">
            {mod.threatModelPrompts.map((o) => (
              <li key={o}>{o}</li>
            ))}
          </ul>
        </section>
      ) : null}

      {mod.labSpec ? (
        <section className="mt-10 rounded-xl border border-amber-200 bg-amber-50 px-4 py-4">
          <h2 className="mb-2 text-xl font-semibold">Lab (local only)</h2>
          <p className="mb-3 leading-relaxed">
            {mod.labSpec.summary || "See the lab brief."} Forbidden outcome is
            checked in-repo, not on this origin.
          </p>
          <p>
            <Link
              href={`/labs/${encodeURIComponent(mod.id)}/`}
              className="font-medium text-blue-900 underline underline-offset-2"
            >
              Lab brief — {mod.labSpec.slug || mod.id}
            </Link>
          </p>
        </section>
      ) : null}

      {mod.misconceptions?.length ? (
        <section className="mt-10">
          <h2 className="mb-3 text-xl font-semibold">Misconceptions this module refuses</h2>
          <ul className="list-disc space-y-2 pl-5 leading-relaxed">
            {mod.misconceptions.map((o) => (
              <li key={o}>{o}</li>
            ))}
          </ul>
        </section>
      ) : null}

      <section className="mt-10">
        <h2 className="mb-3 text-xl font-semibold">Standards</h2>
        <ul className="space-y-2">
          {mod.standardsRefs.map((s) => (
            <li key={`${s.source}-${s.version}`}>
              <a
                href={s.url}
                className="text-blue-900 underline underline-offset-2"
                rel="noreferrer"
                target="_blank"
              >
                {s.source}
              </a>{" "}
              <span className="text-stone-700">
                {s.version} ({s.status})
              </span>
            </li>
          ))}
        </ul>
      </section>
    </PageShell>
  );
}
