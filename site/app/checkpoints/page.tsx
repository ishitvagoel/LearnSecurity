import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";
import { moduleHref } from "@/lib/hrefs";

export const metadata = {
  title: "Check-ins",
  description:
    "How you know you're ready to move on — a check-in for each part of the course.",
};

const CHECKINS = [
  {
    id: "0",
    title: "Ground rules",
    detail:
      "You can say what you may practice on, and you do not point the course files at public websites.",
    assessment: "0.1",
    modules: ["0.1", "0.2"],
    evidence: "Scope note, local allow/deny result, capability map, and bridge decisions.",
  },
  {
    id: "1",
    title: "Rules and who is allowed",
    detail:
      "You can write a rule about the notes app that another person could check, including who you are trusting.",
    assessment: "1.1",
    modules: ["1.1", "1.2", "1.3", "1.4"],
    evidence: "A bounded product model, authority matrix, trust-boundary review, and risk decision. The 1.1 worksheet is a starting point, not the whole gate.",
  },
  {
    id: "2",
    title: "How software actually runs",
    detail:
      "You can point at the parser, the browser, or the network path that would break a rule.",
      assessment: "2.1",
    modules: ["2.1", "2.2", "2.3", "2.4"],
    evidence: "A request trace, parser or browser policy check, and state/time failure case.",
  },
  {
    id: "3",
    title: "Design when someone might attack",
    detail:
      "A new kind of object or a new kind of user does not send you back to a “top ten bugs” list as the design.",
      assessment: "3.1",
    modules: ["3.1", "3.2", "3.3", "3.4"],
    evidence: "A versioned threat model, architecture decision, and abuse-resistant workflow test.",
  },
  {
    id: "4",
    title: "Logins and access",
    detail:
      "Sessions, companies, and “sign in with…” still get checked after time passes and after someone is kicked out.",
      assessment: "4.1",
    modules: ["4.1", "4.2", "4.3", "4.4", "4.5"],
    evidence: "Account lifecycle, session, federation, and object-authorization evidence, including revocation.",
  },
  {
    id: "5",
    title: "Data and secrets",
    detail:
      "Encoding is not encryption. Deleting something includes the copies. Keys do not live in the source tree.",
      assessment: "5.1",
    modules: ["5.1", "5.2", "5.3", "5.4", "5.5"],
    evidence: "Classification, lifecycle, secret/key handling, and parameterized persistence evidence.",
  },
  {
    id: "6",
    title: "Bad input",
    detail: "Typed-in text must not become a program in SQL, HTML, file paths, or shells.",
    assessment: "6.1",
    modules: ["6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7"],
    evidence: "Context-specific output, path, outbound-request, workflow, and resource-limit checks.",
  },
  {
    id: "7",
    title: "APIs and background jobs",
    detail:
      "A caller may edit some fields, not every field. A webhook has to prove who sent it. A background job is not the logged-in user.",
      assessment: "7.1",
    modules: ["7.1", "7.2", "7.3", "7.4"],
    evidence: "Contract, object/property/function authorization, signed callback, and worker authority evidence.",
  },
  {
    id: "8",
    title: "Phone apps (you can wait)",
    detail:
      "A phone app can be copied and changed. What the phone claims is not what the server should believe.",
      assessment: "8.1",
    modules: ["8.1", "8.2", "8.3", "8.4", "8.5"],
    evidence: "Hostile-client, local data, redirect, release, and mobile failure evidence.",
  },
  {
    id: "9",
    title: "Checking your work",
    detail: "A row in a spreadsheet is not coverage. A PDF is not a retest.",
    assessment: "9.1",
    modules: ["9.1", "9.2", "9.3", "9.4", "9.5"],
    evidence: "Scope, finding, retest, regression, and residual-risk records tied to the tested version.",
  },
  {
    id: "10",
    title: "Shipping and running it",
    detail:
      "Merge checks, lockfiles, cloud accounts, debug-off, and recovery are real rules — not a poster on the wall.",
      assessment: "10.1",
    modules: ["10.1", "10.2", "10.3", "10.4", "10.5"],
    evidence: "Release provenance, deployment restriction, runtime configuration, and recovery rehearsal.",
  },
  {
    id: "11",
    title: "Final project",
    detail:
      "The notes app still keeps one company away from another after a share is revoked. This site does not grade that.",
      assessment: "11",
    modules: ["11"],
    evidence: "Accumulated application, independent findings, repaired retests, incident scenario, and architecture defense.",
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
          not grade you. Use the{" "}
          <Link href="/assess/" className="text-link underline underline-offset-2">
            assessment worksheets
          </Link>{" "}
          to keep your own evidence. Answer keys are not published here.
        </p>
      </PageHeader>
      <ol className="grid gap-3 sm:grid-cols-2">
        {CHECKINS.map((g) => (
          <li
            key={g.id}
            className="rounded-xl border border-line bg-surface p-4"
          >
            <p className="font-mono text-xs font-medium text-muted">Check-in {g.id}</p>
            <p className="mt-1 font-semibold text-ink">{g.title}</p>
            <p className="mt-2 text-sm leading-relaxed text-muted">{g.detail}</p>
            <p className="mt-3 text-xs leading-relaxed text-ink"><span className="font-semibold">Evidence:</span> {g.evidence}</p>
            <ul className="mt-3 flex flex-wrap gap-1.5" aria-label={`Topics for check-in ${g.id}`}>
              {g.modules.map((moduleId) => (
                <li key={moduleId}>
                  <Link href={moduleHref(moduleId)} className="rounded-full border border-line bg-paper px-2 py-1 font-mono text-xs text-link hover:border-forest-accent">
                    {moduleId}
                  </Link>
                </li>
              ))}
            </ul>
            <Link
              href={`/assess/${g.assessment}/`}
              className="mt-3 inline-flex text-sm font-medium text-link underline-offset-2 hover:underline"
            >
              Open evidence worksheet →
            </Link>
          </li>
        ))}
      </ol>
    </PageShell>
  );
}
