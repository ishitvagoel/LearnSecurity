import Link from "next/link";
import { CardLink, PageHeader, PageShell } from "@/components/ui";
import { loadAllModules } from "@/lib/loadCurriculum";

const LOOP = [
  "State a testable property of SecureCollab (or the elective system).",
  "Name principals, objects, and channels.",
  "Break it in an authorized local lab — not on this website.",
  "Restore the property with the smallest structural control.",
  "Verify with a test that fails on the broken fixture and passes on the fix.",
  "Detect and recover; residual risk stays explicit.",
  "Transfer the same sentence to a new channel or object — without a Top 10 slogan.",
] as const;

export default function HomePage() {
  const moduleCount = loadAllModules().length;

  return (
    <PageShell>
      <PageHeader
        kicker="LearnSecurity · blueprint 1.1"
        title="Security is what must stay true when someone attacks"
      >
        <p>
          This is a first-principles course in building software whose{" "}
          <strong>invariants</strong> survive misuse, component failure, and an
          attacker with named capabilities. TLS, JWT, bcrypt, and scanners are
          mechanisms. They are not the property.
        </p>
        <p>
          The through-line product is <strong>SecureCollab</strong>: tenant-scoped
          notes, later files and sharing. You keep rewriting the same catalogue as
          identity, data, APIs, and operations get real. Default stack: FastAPI,
          PostgreSQL, TypeScript/Next.js; Android/Kotlin on the mobile track.
        </p>
      </PageHeader>

      <ul className="mb-10 grid gap-3 sm:grid-cols-3">
        <li>
          <CardLink
            href="/learn/1.1/01-property-vs-mechanism/"
            kicker="Start here"
            title="Module 1.1"
          >
            Property versus mechanism — the sentence this course repeats.
          </CardLink>
        </li>
        <li>
          <CardLink href="/learn/0.1/" kicker="Before labs" title="Orientation">
            Authorized scope, local-first progress, how a module is organized.
          </CardLink>
        </li>
        <li>
          <CardLink href="/learn/" kicker={`${moduleCount} units`} title="Full catalog">
            Every module’s lessons, generated from the content schema.
          </CardLink>
        </li>
      </ul>

      <section className="mb-10">
        <h2 className="mb-3 text-2xl font-semibold tracking-tight">How each module works</h2>
        <ol className="max-w-prose space-y-3">
          {LOOP.map((step, i) => (
            <li key={step} className="flex gap-3 text-[1.05rem] leading-relaxed">
              <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-full bg-stone-900 text-xs font-semibold text-white">
                {i + 1}
              </span>
              <span>{step}</span>
            </li>
          ))}
        </ol>
      </section>

      <section className="mb-10">
        <h2 className="mb-3 text-2xl font-semibold tracking-tight">On this site</h2>
        <ul className="grid gap-3 sm:grid-cols-2">
          <li>
            <CardLink href="/roadmap/" title="Roadmap">
              Phases, core / mobile / elective, what to study in order.
            </CardLink>
          </li>
          <li>
            <CardLink href="/labs/" title="Labs">
              Briefs only. Pytest runs in your git checkout, not here.
            </CardLink>
          </li>
          <li>
            <CardLink href="/checkpoints/" title="Checkpoints">
              Mastery gates stay ungraded here until you have evidence.
            </CardLink>
          </li>
          <li>
            <CardLink href="/glossary/" title="Glossary">
              Invariant, TCB, residual risk, and the other working terms.
            </CardLink>
          </li>
        </ul>
      </section>

      <section>
        <h2 className="mb-3 text-2xl font-semibold tracking-tight">Safe use</h2>
        <p className="mb-4 max-w-prose leading-relaxed text-stone-800">
          Offensive work is limited to local course apps, official training labs,
          or systems you are written-authorized to test. This origin does not host
          or execute vulnerable lab code and does not publish examiner keys. Read{" "}
          <Link href="/policy/" className="text-blue-900 underline underline-offset-2">
            Safe use
          </Link>
          .
        </p>
        <p className="max-w-prose text-sm text-stone-600">
          Progress checkboxes are stored in this browser only. No accounts.
        </p>
      </section>
    </PageShell>
  );
}
