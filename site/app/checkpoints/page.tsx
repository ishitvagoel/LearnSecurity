import { PageHeader, PageShell } from "@/components/ui";

const GATES = [
  {
    id: "0",
    title: "Orientation and lab hygiene",
    detail:
      "You can explain authorized scope and you do not run fixtures against public targets.",
  },
  {
    id: "1",
    title: "Invariants and authority",
    detail:
      "You can write SecureCollab properties that a reviewer could test, including who is trusted.",
  },
  {
    id: "2",
    title: "Mechanism literacy",
    detail: "You can point at the interpreter (parser, browser, HTTP) that would violate a property.",
  },
  {
    id: "3",
    title: "Threat model and architecture (transfer required)",
    detail: "A new object or principal does not send you back to a Top 10 list as the design.",
  },
  {
    id: "4",
    title: "Identity vertical (transfer required)",
    detail: "Session, tenant, and delegated access stay mediated after time and revoke.",
  },
  {
    id: "5",
    title: "Data and crypto use",
    detail: "Encoding is not encryption; deletion includes copies; keys are not hardcoded.",
  },
  {
    id: "6",
    title: "Injection and abuse (transfer required)",
    detail: "User data is not a program in SQL, HTML, paths, or shells.",
  },
  {
    id: "7",
    title: "API and workers",
    detail: "Mass assignment, field auth, webhook authenticity, and worker identity are explicit.",
  },
  {
    id: "8",
    title: "Mobile (optional until web/API milestone)",
    detail: "The APK is hostile; server attestation and storage properties are not client claims.",
  },
  {
    id: "9",
    title: "Verification (transfer required)",
    detail: "A mapping row is not coverage; a PDF is not a retest.",
  },
  {
    id: "10",
    title: "Operate and supply chain (transfer required)",
    detail: "Merge gates, lockfiles, IAM, debug-off, and recovery are properties, not posters.",
  },
  {
    id: "11",
    title: "Capstone defense",
    detail:
      "SecureCollab still isolates tenants after share-revoke. This site does not grade that defense.",
  },
] as const;

export default function CheckpointsPage() {
  return (
    <PageShell>
      <PageHeader kicker="Mastery gates" title="Checkpoints">
        <p>
          Gates use four states: not-attempted, developing, competent,
          transfer-ready. There is no compensating average. This website does not
          mark you competent. Rubrics live with each module; examiner keys are
          not published here.
        </p>
      </PageHeader>
      <ol className="grid gap-3 sm:grid-cols-2">
        {GATES.map((g) => (
          <li
            key={g.id}
            className="rounded-xl border border-stone-200 bg-white p-4"
          >
            <p className="font-mono text-xs font-medium text-stone-600">Gate {g.id}</p>
            <p className="mt-1 font-semibold text-stone-900">{g.title}</p>
            <p className="mt-2 text-sm leading-relaxed text-stone-700">{g.detail}</p>
          </li>
        ))}
      </ol>
    </PageShell>
  );
}
