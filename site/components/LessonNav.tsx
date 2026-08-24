import type { ReactElement } from "react";
import Link from "next/link";
import { kindLabel } from "@/lib/headings";
import { lessonHref, moduleHref } from "@/lib/loadCurriculum";

export type LessonNavItem = {
  filename: string;
  title: string;
  kind: string;
};

export function LessonNav({
  moduleId,
  moduleTitle,
  lessons,
  currentFilename,
}: {
  moduleId: string;
  moduleTitle: string;
  lessons: LessonNavItem[];
  currentFilename: string;
}): ReactElement {
  return (
    <nav aria-label="Lessons in this module" className="text-sm">
      <p className="mb-2 font-semibold text-stone-900">
        <Link
          href={moduleHref(moduleId)}
          className="text-blue-900 underline-offset-2 hover:underline"
        >
          {moduleId}
        </Link>
        <span className="mt-0.5 block text-xs font-normal leading-snug text-stone-600">
          {moduleTitle}
        </span>
      </p>
      <ol className="space-y-0.5">
        {lessons.map((lesson, index) => {
          const current = lesson.filename === currentFilename;
          return (
            <li key={lesson.filename}>
              <Link
                href={lessonHref(moduleId, lesson.filename)}
                aria-current={current ? "page" : undefined}
                className={`flex gap-2 rounded-md px-2 py-1.5 leading-snug ${
                  current
                    ? "bg-blue-50 font-medium text-stone-900 ring-1 ring-blue-200"
                    : "text-stone-800 hover:bg-stone-100"
                }`}
              >
                <span className="w-4 shrink-0 text-right font-mono text-xs text-stone-500">
                  {index + 1}
                </span>
                <span>
                  <span className="block">{lesson.title}</span>
                  <span className="block text-xs font-normal text-stone-600">
                    {kindLabel(lesson.kind)}
                  </span>
                </span>
              </Link>
            </li>
          );
        })}
      </ol>
    </nav>
  );
}

export function LessonPager({
  moduleId,
  prev,
  next,
}: {
  moduleId: string;
  prev?: LessonNavItem;
  next?: LessonNavItem;
}): ReactElement {
  return (
    <nav
      className="mt-12 grid gap-3 border-t border-stone-200 pt-6 sm:grid-cols-2"
      aria-label="Adjacent lessons"
    >
      {prev ? (
        <Link
          href={lessonHref(moduleId, prev.filename)}
          className="rounded-lg border border-stone-200 bg-white px-4 py-3 hover:border-stone-400"
        >
          <span className="block text-xs uppercase tracking-wide text-stone-600">
            Previous
          </span>
          <span className="mt-1 block font-medium text-blue-900">{prev.title}</span>
        </Link>
      ) : (
        <p className="rounded-lg border border-dashed border-stone-200 px-4 py-3 text-sm text-stone-600">
          Start of this module
        </p>
      )}
      {next ? (
        <Link
          href={lessonHref(moduleId, next.filename)}
          className="rounded-lg border border-stone-200 bg-white px-4 py-3 text-right hover:border-stone-400 sm:justify-self-stretch"
        >
          <span className="block text-xs uppercase tracking-wide text-stone-600">
            Next
          </span>
          <span className="mt-1 block font-medium text-blue-900">{next.title}</span>
        </Link>
      ) : (
        <Link
          href={moduleHref(moduleId)}
          className="rounded-lg border border-stone-200 bg-white px-4 py-3 text-right hover:border-stone-400"
        >
          <span className="block text-xs uppercase tracking-wide text-stone-600">
            Next
          </span>
          <span className="mt-1 block font-medium text-blue-900">Back to module overview</span>
        </Link>
      )}
    </nav>
  );
}
