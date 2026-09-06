import { PageHeader, PageShell } from "@/components/ui";

const CHECKINS = [
  {
    id: "0",
    title: "Ground rules",
    detail:
      "You can say what you may practice on, and you do not point the course files at public websites.",
  },
  {
    id: "1",
    title: "Rules and who is allowed",
    detail:
      "You can write a rule about the notes app that another person could check, including who you are trusting.",
  },
  {
    id: "2",
    title: "How software actually runs",
    detail:
      "You can point at the parser, the browser, or the network path that would break a rule.",
  },
  {
    id: "3",
    title: "Design when someone might attack",
    detail:
      "A new kind of object or a new kind of user does not send you back to a “top ten bugs” list as the design.",
  },
  {
    id: "4",
    title: "Logins and access",
    detail:
      "Sessions, companies, and “sign in with…” still get checked after time passes and after someone is kicked out.",
  },
  {
    id: "5",
    title: "Data and secrets",
    detail:
      "Encoding is not encryption. Deleting something includes the copies. Keys do not live in the source tree.",
  },
  {
    id: "6",
    title: "Bad input",
    detail: "Typed-in text must not become a program in SQL, HTML, file paths, or shells.",
  },
  {
    id: "7",
    title: "APIs and background jobs",
    detail:
      "A caller may edit some fields, not every field. A webhook has to prove who sent it. A background job is not the logged-in user.",
  },
  {
    id: "8",
    title: "Phone apps (you can wait)",
    detail:
      "A phone app can be copied and changed. What the phone claims is not what the server should believe.",
  },
  {
    id: "9",
    title: "Checking your work",
    detail: "A row in a spreadsheet is not coverage. A PDF is not a retest.",
  },
  {
    id: "10",
    title: "Shipping and running it",
    detail:
      "Merge checks, lockfiles, cloud accounts, debug-off, and recovery are real rules — not a poster on the wall.",
  },
  {
    id: "11",
    title: "Final project",
    detail:
      "The notes app still keeps one company away from another after a share is revoked. This site does not grade that.",
  },
] as const;

export default function CheckpointsPage() {
  return (
    <PageShell>
      <PageHeader kicker="How you know you are ready" title="Check-ins">
        <p>
          Each part of the course has a check-in. You are not “done” because you
          opened a page. You are ready when you can show the work — a rule,
          a repair, a check that fails on the broken files. This website does
          not grade you. Answer keys are not published here.
        </p>
      </PageHeader>
      <ol className="grid gap-3 sm:grid-cols-2">
        {CHECKINS.map((g) => (
          <li
            key={g.id}
            className="rounded-xl border border-stone-200 bg-white p-4"
          >
            <p className="font-mono text-xs font-medium text-stone-600">Check-in {g.id}</p>
            <p className="mt-1 font-semibold text-stone-900">{g.title}</p>
            <p className="mt-2 text-sm leading-relaxed text-stone-700">{g.detail}</p>
          </li>
        ))}
      </ol>
    </PageShell>
  );
}
