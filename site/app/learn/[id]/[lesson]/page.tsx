import Link from "next/link";
import { notFound } from "next/navigation";
import { LessonReader } from "@/components/LessonReader";
import { PageHeader, PageShell } from "@/components/ui";
import { parseLessonLead, spokenLessonTitle } from "@/lib/headings";
import { topicBlurb, topicTitle } from "@/lib/catalog";
import {
  loadAllModules,
  loadLessons,
  loadModule,
} from "@/lib/loadCurriculum";
import { estimateReadingMinutes } from "@/lib/text";
import { nextRouteModule } from "@/lib/route";

type Props = { params: Promise<{ id: string; lesson: string }> };

const LEGACY_LESSON_REDIRECTS: Record<string, { target: string; title: string }> = {
  "0.1/03-break": { target: "03-practice", title: "Break, repair, and verify the local host gate" },
  "0.1/04-build": { target: "04-operate-transfer-review", title: "Operate and review the scope rule" },
};

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
  for (const key of Object.keys(LEGACY_LESSON_REDIRECTS)) {
    const [id, lesson] = key.split("/");
    params.push({ id, lesson });
  }
  return params;
}

export async function generateMetadata({ params }: Props) {
  const { id, lesson } = await params;
  const mod = loadAllModules().find((m) => m.id === id);
  if (!mod) {
    return { title: "Page" };
  }
  const lo = loadLessons(mod).find((x) => x.filename.replace(/\.md$/, "") === lesson);
  if (!lo) {
    const legacy = LEGACY_LESSON_REDIRECTS[`${id}/${lesson}`];
    if (legacy) return { title: `${id} · ${legacy.title}` };
    return { title: `${mod.id} · ${lesson}` };
  }
  return {
    title: `${mod.id} · ${spokenLessonTitle(lo.title, lo.body || "")}`,
    description: topicBlurb(mod),
  };
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
    const legacy = LEGACY_LESSON_REDIRECTS[`${id}/${lesson}`];
    if (legacy) {
      return (
        <PageShell width="narrow">
          <PageHeader title="This page moved">
            <p>
              The orientation was shortened and its old page names no longer
              describe the learner task. Continue with the current page below.
            </p>
          </PageHeader>
          <p>
            <Link href={`/learn/${encodeURIComponent(id)}/${encodeURIComponent(legacy.target)}/`} className="text-link underline underline-offset-2 hover:no-underline">
              Open {legacy.title}
            </Link>
          </p>
        </PageShell>
      );
    }
    notFound();
  }
  const routeNext = nextRouteModule(loadAllModules(), mod.id);
  const nextTopic = index === lessons.length - 1
    ? mod.labSpec
      ? { href: `/labs/${encodeURIComponent(mod.id)}/`, title: "Next: run the local practice" }
      : { href: `/assess/${encodeURIComponent(mod.id)}/`, title: "Next: open the evidence worksheet" }
    : routeNext
      ? { href: `/learn/${encodeURIComponent(routeNext.id)}/`, title: `Next topic: ${topicTitle(routeNext)}` }
      : undefined;
  const lead = parseLessonLead(lo.body || `# ${lo.title}\n\nLesson file missing.`);
  const source = lead.body || `_This lesson file is empty._`;
  const lessonTitle = spokenLessonTitle(lo.title, lo.body || `# ${lo.title}\n\nLesson file missing.`);

  return (
    <LessonReader
      moduleId={mod.id}
      moduleTitle={topicTitle(mod)}
      lessonTitle={lessonTitle}
      kind={lead.kind || lo.kind}
      index={index}
      lessons={lessons.map((item) => ({
        filename: item.filename,
        title: spokenLessonTitle(item.title, item.body || ""),
        kind: item.kind,
      }))}
      source={source}
      readingMinutes={estimateReadingMinutes(source)}
      nextTopic={nextTopic}
    />
  );
}
