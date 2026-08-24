import type { ReactElement } from "react";
import Link from "next/link";
import { Chip } from "@/components/ui";
import { LessonNav, LessonPager, type LessonNavItem } from "@/components/LessonNav";
import { LessonToc, ReadingProgress } from "@/components/LessonToc";
import { extractHeadings, kindLabel } from "@/lib/headings";
import { Markdown } from "@/lib/markdown";
import { moduleHref } from "@/lib/loadCurriculum";

export function LessonReader({
  moduleId,
  moduleTitle,
  lessonTitle,
  kind,
  loopStep,
  standards,
  index,
  lessons,
  source,
}: {
  moduleId: string;
  moduleTitle: string;
  lessonTitle: string;
  kind: string | null;
  loopStep: string | null;
  standards: string | null;
  index: number;
  lessons: LessonNavItem[];
  source: string;
}): ReactElement {
  const headings = extractHeadings(source);
  const current = lessons[index];
  if (!current) {
    return <p className="text-stone-700">This lesson is not in the module map.</p>;
  }
  const prev = index > 0 ? lessons[index - 1] : undefined;
  const next = index < lessons.length - 1 ? lessons[index + 1] : undefined;

  return (
    <>
      <ReadingProgress />
      <div className="lg:grid lg:grid-cols-[16rem_minmax(0,42rem)_14rem] lg:justify-center lg:gap-10">
        <aside className="hidden lg:block">
          <div className="sticky top-4 max-h-[calc(100vh-2rem)] overflow-y-auto pb-8">
            <LessonNav
              moduleId={moduleId}
              moduleTitle={moduleTitle}
              lessons={lessons}
              currentFilename={current.filename}
            />
          </div>
        </aside>
        <article id="lesson-article" className="min-w-0">
          <nav className="mb-4 text-sm text-stone-700" aria-label="Breadcrumb">
            <Link href="/learn/" className="text-blue-900 underline-offset-2 hover:underline">
              Learn
            </Link>
            {" · "}
            <Link
              href={moduleHref(moduleId)}
              className="text-blue-900 underline-offset-2 hover:underline"
            >
              {moduleId}
            </Link>
            <span>
              {" "}
              · Lesson {index + 1} of {lessons.length}
            </span>
          </nav>
          <details className="mb-6 rounded-lg border border-stone-200 bg-white px-3 py-2 lg:hidden">
            <summary className="cursor-pointer font-medium text-stone-900">
              Lessons in this module
            </summary>
            <div className="mt-3">
              <LessonNav
                moduleId={moduleId}
                moduleTitle={moduleTitle}
                lessons={lessons}
                currentFilename={current.filename}
              />
            </div>
          </details>
          <LessonToc headings={headings} variant="mobile" />
          <header className="mb-8 border-b border-stone-200 pb-6">
            <h1 className="text-3xl font-semibold tracking-tight text-stone-900">
              {lessonTitle}
            </h1>
            <div className="mt-3 flex flex-wrap gap-2">
              {kind ? <Chip>{kindLabel(kind)}</Chip> : null}
              {loopStep ? <Chip>Loop · {loopStep}</Chip> : null}
              <Chip>
                {index + 1} / {lessons.length}
              </Chip>
            </div>
            {standards ? (
              <p className="mt-3 max-w-prose text-sm leading-relaxed text-stone-700">
                <span className="font-medium text-stone-900">Standards. </span>
                {standards}
              </p>
            ) : null}
          </header>
          <Markdown source={source} />
          <LessonPager moduleId={moduleId} prev={prev} next={next} />
        </article>
        <aside className="hidden lg:block">
          <LessonToc headings={headings} variant="desktop" />
        </aside>
      </div>
    </>
  );
}
