import Link from "next/link";
import { notFound } from "next/navigation";
import { ProgressToggle } from "@/components/ProgressToggle";
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

  return (
    <article>
      <p className="mb-2 text-sm text-stone-700">
        Phase {mod.phase} · {mod.track} · {mod.difficulty} · {mod.estimatedMinutes}{" "}
        min
      </p>
      <h1 className="mb-4 text-3xl font-semibold">
        {mod.id} — {mod.title}
      </h1>
      <ProgressToggle moduleId={mod.id} />
      <h2 className="mb-2 mt-8 text-2xl font-semibold">Outcomes</h2>
      <ul className="mb-4 list-disc pl-6">
        {mod.outcomes.map((o) => (
          <li key={o} className="max-w-prose">
            {o}
          </li>
        ))}
      </ul>
      <h2 className="mb-2 mt-8 text-2xl font-semibold">Invariants</h2>
      <ul className="mb-4 list-disc pl-6">
        {mod.invariants.map((o) => (
          <li key={o} className="max-w-prose">
            {o}
          </li>
        ))}
      </ul>
      <h2 className="mb-2 mt-8 text-2xl font-semibold">Learning objects</h2>
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
        <p className="mt-4 max-w-prose">
          Lab (not executed here):{" "}
          <Link href={`/labs/${encodeURIComponent(mod.id)}/`} className="text-blue-900 underline">
            {mod.labSpec.slug || mod.id}
          </Link>
        </p>
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
