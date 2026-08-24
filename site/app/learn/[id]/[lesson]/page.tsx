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

export async function generateMetadata({ params }: Props) {
  const { id, lesson } = await params;
  const mod = loadAllModules().find((m) => m.id === id);
  return { title: mod ? `${mod.id} · ${lesson}` : "Lesson" };
}

export default async function LessonPage({ params }: Props) {
  const { id, lesson } = await params;
  const exists = loadAllModules().some((m) => m.id === id);
  if (!exists) {
    notFound();
  }
  const mod = loadModule(id);
  const lessons = loadLessons(mod).filter((x) => x.filename);
  const index = lessons.findIndex((x) => x.filename.replace(/\.md$/, "") === lesson);
  const lo = index >= 0 ? lessons[index] : undefined;
  if (!lo) {
    notFound();
  }
  const prev = index > 0 ? lessons[index - 1] : undefined;
  const next = index < lessons.length - 1 ? lessons[index + 1] : undefined;

  return (
    <article>
      <nav className="mb-4 text-sm" aria-label="Breadcrumb">
        <Link href="/learn/" className="text-blue-900 underline">
          Learn
        </Link>
        {" · "}
        <Link href={moduleHref(mod.id)} className="text-blue-900 underline">
          {mod.id} — {mod.title}
        </Link>
        <span className="text-stone-700">
          {" "}
          · Lesson {index + 1} of {lessons.length}
        </span>
      </nav>
      <Markdown source={lo.body || `# ${lo.title}\n\nLesson file missing.`} />
      <nav
        className="mt-10 flex flex-wrap justify-between gap-4 border-t border-stone-300 pt-4 text-sm"
        aria-label="Adjacent lessons"
      >
        <div>
          {prev ? (
            <Link href={lessonHref(mod.id, prev.filename)} className="text-blue-900 underline">
              Previous: {prev.title}
            </Link>
          ) : (
            <span className="text-stone-600">Start of module</span>
          )}
        </div>
        <div>
          {next ? (
            <Link href={lessonHref(mod.id, next.filename)} className="text-blue-900 underline">
              Next: {next.title}
            </Link>
          ) : (
            <Link href={moduleHref(mod.id)} className="text-blue-900 underline">
              Back to module
            </Link>
          )}
        </div>
      </nav>
    </article>
  );
}
