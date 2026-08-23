import Link from "next/link";
import { notFound } from "next/navigation";
import { Markdown } from "@/lib/markdown";
import {
  lessonHref,
  loadAllModules,
  loadLessons,
  loadModule,
  moduleHref,
} from "@/lib/loadCurriculum";

type Props = { params: Promise<{ id: string; lesson: string }> };

export const dynamicParams = false;

export function generateStaticParams() {
  const params: { id: string; lesson: string }[] = [];
  for (const m of loadAllModules()) {
    for (const lo of loadLessons(m)) {
      if (!lo.filename) {
        continue;
      }
      params.push({
        id: m.id,
        lesson: lo.filename.replace(/\.md$/, ""),
      });
    }
  }
  return params;
}

export default async function LessonPage({ params }: Props) {
  const { id, lesson } = await params;
  const exists = loadAllModules().some((m) => m.id === id);
  if (!exists) {
    notFound();
  }
  const mod = loadModule(id);
  const lessons = loadLessons(mod);
  const lo = lessons.find((x) => x.filename.replace(/\.md$/, "") === lesson);
  if (!lo) {
    notFound();
  }
  return (
    <article>
      <p className="mb-2 text-sm">
        <Link href={moduleHref(mod.id)} className="text-blue-900 underline">
          {mod.id} — {mod.title}
        </Link>
      </p>
      <Markdown source={lo.body || `# ${lo.title}\n\nLesson file missing.`} />
      <nav className="mt-10 border-t border-stone-300 pt-4" aria-label="Lesson list">
        <ul className="flex flex-col gap-1 text-sm">
          {lessons.map((item) =>
            item.filename ? (
              <li key={item.id}>
                <Link
                  href={lessonHref(mod.id, item.filename)}
                  className="text-blue-900 underline"
                >
                  {item.title}
                </Link>
              </li>
            ) : null,
          )}
        </ul>
      </nav>
    </article>
  );
}
