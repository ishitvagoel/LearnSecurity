import { phaseHeading, topicBlurb, topicTitle } from "./catalog";
import { GLOSSARY_TERMS } from "./glossary";
import { spokenLessonTitle } from "./headings";
import {
  assessmentHref,
  lessonHref,
  loadAllModules,
  loadLessons,
  moduleHref,
} from "./loadCurriculum";
import { stripMarkdown } from "./text";

export type SearchEntryType = "page" | "module" | "lesson" | "glossary";

export type SearchEntry = {
  id: string;
  type: SearchEntryType;
  title: string;
  subtitle?: string;
  href: string;
  text: string;
};

const STATIC_PAGES: { href: string; title: string; text: string }[] = [
  { href: "/", title: "Home", text: "Learn to build software that stays safe when someone tries to break it. Start here." },
  { href: "/learn/", title: "Lessons", text: "All topics, in study order. Open a topic and read its pages left to right." },
  { href: "/roadmap/", title: "Study order", text: "What to study next, and in what order. Parts 0 through 11, plus extra topics." },
  { href: "/labs/", title: "Practice", text: "Run the practice files on your own computer, from the course repository." },
  { href: "/assess/", title: "Assessments", text: "Worksheets to state the rule, explain the break, plan the fix, and collect evidence." },
  { href: "/checkpoints/", title: "Check-ins", text: "How you know you are ready to move on to the next part of the course." },
  { href: "/capstone/", title: "Final project", text: "Put the pieces together on the notes app the course has been building." },
  { href: "/policy/", title: "Rules for practice", text: "What you may and must not do when practicing. Authorized scope and safety." },
  { href: "/reference/", title: "The notes app", text: "The example app the course follows: teams, members, notes, files, and sharing." },
  { href: "/glossary/", title: "Word list", text: "A few words this course uses a lot, said in ordinary English." },
  { href: "/references/", title: "References", text: "Published lists and papers the course cites, with links, versions, and which topics mention them." },
];

const MAX_LESSON_TEXT = 3000;

export function buildSearchIndex(): SearchEntry[] {
  const modules = loadAllModules();
  const entries: SearchEntry[] = [];

  for (const page of STATIC_PAGES) {
    entries.push({
      id: `page:${page.href}`,
      type: "page",
      title: page.title,
      href: page.href,
      text: page.text,
    });
  }

  for (const term of GLOSSARY_TERMS) {
    entries.push({
      id: `glossary:${term.term}`,
      type: "glossary",
      title: term.term,
      subtitle: "Word list",
      href: "/glossary/",
      text: term.def,
    });
  }

  for (const mod of modules) {
    entries.push({
      id: `module:${mod.id}`,
      type: "module",
      title: `${mod.id} — ${topicTitle(mod)}`,
      subtitle: `Part ${mod.phase} · ${phaseHeading(mod.phase)}`,
      href: moduleHref(mod.id),
      text: [topicBlurb(mod), ...(mod.outcomes || [])].join(" "),
    });

    entries.push({
      id: `assessment:${mod.id}`,
      type: "page",
      title: `Assessment — ${mod.id} ${topicTitle(mod)}`,
      subtitle: "Assessments",
      href: assessmentHref(mod.id),
      text: `Assessment worksheet for ${topicTitle(mod)}.`,
    });

    for (const lo of loadLessons(mod)) {
      if (!lo.filename || !lo.body) {
        continue;
      }
      const title = spokenLessonTitle(lo.title, lo.body);
      const text = stripMarkdown(lo.body).slice(0, MAX_LESSON_TEXT);
      entries.push({
        id: `lesson:${mod.id}:${lo.filename}`,
        type: "lesson",
        title,
        subtitle: `${mod.id} · ${topicTitle(mod)}`,
        href: lessonHref(mod.id, lo.filename),
        text,
      });
    }
  }

  return entries;
}
