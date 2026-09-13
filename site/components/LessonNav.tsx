import type { ReactElement } from "react";
import Link from "next/link";
import { kindLabel } from "@/lib/headings";
import { plainLessonTitle } from "@/lib/plainCopy";
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
    <nav aria-label="Pages in this topic" className="text-sm">
      <p className="mb-2 font-semibold text-ink">
        <Link
          href={moduleHref(moduleId)}
          className="text-link underline-offset-2 hover:underline"
        >
          {moduleId}
        </Link>
        <span className="mt-0.5 block text-xs font-normal leading-snug text-muted">
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
                    ? "bg-forest/5 font-medium text-ink ring-1 ring-forest-accent/30"
                    : "text-ink hover:bg-surface-hover"
                }`}
              >
                <span className="w-4 shrink-0 text-right font-mono text-xs text-muted">
                  {index + 1}
                </span>
                <span>
                    <span className="block">{plainLessonTitle(lesson.title)}</span>
                  <span className="block text-xs font-normal text-muted">
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
      className="mt-12 border-t border-line pt-6"
      aria-label="Nearby pages"
    >
      <div className="grid gap-3 sm:grid-cols-2">
      {prev ? (
        <Link
          href={lessonHref(moduleId, prev.filename)}
          className="rounded-lg border border-line bg-surface px-4 py-3 hover:border-border"
        >
          <span className="block text-xs uppercase tracking-wide text-muted">
            Previous
          </span>
          <span className="mt-1 block font-medium text-link">{plainLessonTitle(prev.title)}</span>
        </Link>
      ) : (
        <p className="rounded-lg border border-dashed border-line px-4 py-3 text-sm text-muted">
          Start of this topic
        </p>
      )}
      {next ? (
        <Link
          href={lessonHref(moduleId, next.filename)}
          className="rounded-lg border border-line bg-surface px-4 py-3 text-right hover:border-border sm:justify-self-stretch"
        >
          <span className="block text-xs uppercase tracking-wide text-muted">
            Next
          </span>
          <span className="mt-1 block font-medium text-link">{plainLessonTitle(next.title)}</span>
        </Link>
      ) : (
        <Link
          href={moduleHref(moduleId)}
          className="rounded-lg border border-line bg-surface px-4 py-3 text-right hover:border-border"
        >
          <span className="block text-xs uppercase tracking-wide text-muted">
            Next
          </span>
          <span className="mt-1 block font-medium text-link">Back to the topic</span>
        </Link>
      )}
      </div>
      <p className="mt-3 hidden text-center text-xs text-muted sm:block">
        Tip: press <kbd className="rounded border border-line bg-surface px-1 py-0.5 font-mono">←</kbd>{" "}
        and <kbd className="rounded border border-line bg-surface px-1 py-0.5 font-mono">→</kbd> to move
        between pages.
      </p>
    </nav>
  );
}
