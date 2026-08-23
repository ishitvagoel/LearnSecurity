import Link from "next/link";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";

export default function LearnIndexPage() {
  const modules = loadAllModules();
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Learn</h1>
      <p className="mb-6 max-w-prose leading-relaxed">
        Module metadata comes from schema-valid <code>module.yaml</code>. Lesson
        prose is separate. Answer keys are not linked from these pages.
      </p>
      <ol className="list-decimal pl-6">
        {modules.map((m) => (
          <li key={m.id} className="mb-2">
            <Link href={moduleHref(m.id)} className="text-blue-900 underline">
              {m.id} — {m.title}
            </Link>
          </li>
        ))}
      </ol>
    </article>
  );
}
