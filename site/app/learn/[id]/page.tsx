import Link from "next/link";
import { notFound } from "next/navigation";
import { ProgressToggle } from "@/components/ProgressToggle";
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
    <article>
      <p className="mb-2 text-sm text-stone-700">
        <Link href="/learn/" className="text-blue-900 underline">
          Learn
        </Link>
        {" · "}
        Phase {mod.phase}
        {phase ? ` (${phase.title})` : ""} · {mod.track} · {mod.difficulty} ·{" "}
        {mod.estimatedMinutes} min
      </p>
      <h1 className="mb-4 text-3xl font-semibold">
        {mod.id} — {mod.title}
      </h1>
      {first ? (
        <p className="mb-4">
          <Link
            href={lessonHref(mod.id, first.filename)}
            className="inline-block rounded bg-blue-900 px-3 py-2 text-sm font-medium text-white"
          >
            Open first lesson
          </Link>
        </p>
      ) : null}
      <ProgressToggle moduleId={mod.id} />
      <h2 className="mb-2 mt-8 text-2xl font-semibold">What you should be able to do</h2>
      <ul className="mb-4 list-disc pl-6">
        {mod.outcomes.map((o) => (
          <li key={o} className="max-w-prose">
            {o}
          </li>
        ))}
      </ul>
      <h2 className="mb-2 mt-8 text-2xl font-semibold">Invariants this module owns</h2>
      <ul className="mb-4 list-disc pl-6">
        {mod.invariants.map((o) => (
          <li key={o} className="max-w-prose">
            {o}
          </li>
        ))}
      </ul>
      {mod.threatModelPrompts?.length ? (
        <>
          <h2 className="mb-2 mt-8 text-2xl font-semibold">Threat prompts</h2>
          <ul className="mb-4 list-disc pl-6">
            {mod.threatModelPrompts.map((o) => (
              <li key={o} className="max-w-prose">
                {o}
              </li>
            ))}
          </ul>
        </>
      ) : null}
      <h2 className="mb-2 mt-8 text-2xl font-semibold">Lessons</h2>
      <ol className="mb-4 list-decimal pl-6">
        {lessons.map((lo) => (
          <li key={lo.id} className="mb-1">
            {lo.filename ? (
              <Link
                href={lessonHref(mod.id, lo.filename)}
                className="text-blue-900 underline"
              >
                {lo.title}
              </Link>
            ) : (
              lo.title
            )}{" "}
            <span className="text-stone-700">({lo.kind})</span>
          </li>
        ))}
      </ol>
      {mod.labSpec ? (
        <section className="mb-6 max-w-prose">
          <h2 className="mb-2 mt-8 text-2xl font-semibold">Lab (local only)</h2>
          <p className="mb-2 leading-relaxed">
            {mod.labSpec.summary || "See the lab brief."} Forbidden outcome is
            checked in-repo, not on this origin.
          </p>
          <p>
            <Link
              href={`/labs/${encodeURIComponent(mod.id)}/`}
              className="text-blue-900 underline"
            >
              Lab brief — {mod.labSpec.slug || mod.id}
            </Link>
          </p>
        </section>
      ) : null}
      {mod.misconceptions?.length ? (
        <>
          <h2 className="mb-2 mt-8 text-2xl font-semibold">Misconceptions this module refuses</h2>
          <ul className="mb-4 list-disc pl-6">
            {mod.misconceptions.map((o) => (
              <li key={o} className="max-w-prose">
                {o}
              </li>
            ))}
          </ul>
        </>
      ) : null}
      <h2 className="mb-2 mt-8 text-2xl font-semibold">Standards</h2>
      <ul className="list-disc pl-6">
        {mod.standardsRefs.map((s) => (
          <li key={`${s.source}-${s.version}`} className="max-w-prose">
            <a href={s.url} className="text-blue-900 underline">
              {s.source}
            </a>{" "}
            {s.version} ({s.status})
          </li>
        ))}
      </ul>
    </article>
  );
}
