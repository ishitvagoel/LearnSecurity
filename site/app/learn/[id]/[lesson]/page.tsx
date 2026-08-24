import { notFound } from "next/navigation";
import { LessonReader } from "@/components/LessonReader";
import { parseLessonLead } from "@/lib/headings";
import {
  loadAllModules,
  loadLessons,
  loadModule,
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
  if (!mod) {
    return { title: "Lesson" };
  }
  const lo = loadLessons(mod).find((x) => x.filename.replace(/\.md$/, "") === lesson);
  return { title: lo ? `${mod.id} · ${lo.title}` : `${mod.id} · ${lesson}` };
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
  const lead = parseLessonLead(lo.body || `# ${lo.title}\n\nLesson file missing.`);
  const source = lead.body || `_This lesson file is empty._`;

  return (
    <LessonReader
      moduleId={mod.id}
      moduleTitle={mod.title}
      lessonTitle={lo.title}
      kind={lead.kind || lo.kind}
      loopStep={lead.loopStep}
      standards={lead.standards}
      index={index}
      lessons={lessons.map((item) => ({
        filename: item.filename,
        title: item.title,
        kind: item.kind,
      }))}
      source={source}
    />
  );
}
