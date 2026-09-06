import Link from "next/link";
import { HomeContinue } from "@/components/HomeContinue";
import { ButtonLink, CardLink } from "@/components/ui";
import { loadAllModules } from "@/lib/loadCurriculum";

const LOOP = [
  {
    title: "Property",
    body: "Write a testable sentence about SecureCollab (or the elective system).",
  },
  {
    title: "Model",
    body: "Name principals, objects, channels, authority, and time.",
  },
  {
    title: "Break",
    body: "Show the smallest failure in an authorized local lab — not on this website.",
  },
  {
    title: "Build",
    body: "Restore the property with the smallest structural control.",
  },
  {
    title: "Verify",
    body: "A test that fails on the broken fixture and passes on the fix.",
  },
  {
    title: "Operate",
    body: "Detect, recover, rotate, revoke. Residual risk stays named.",
  },
  {
    title: "Transfer",
    body: "Reuse the same sentence on a new channel or object — not a Top 10 slogan.",
  },
] as const;

export default function HomePage() {
  const moduleCount = loadAllModules().length;

  return (
    <div>
      <section className="bg-stone-900 text-stone-50">
        <div className="mx-auto max-w-5xl px-4 py-16 sm:py-20">
          <p className="text-sm font-medium uppercase tracking-wide text-stone-400">
            LearnSecurity · blueprint 1.1
          </p>
          <h1 className="mt-3 max-w-3xl text-3xl font-semibold tracking-tight text-white sm:text-5xl">
            Security is what must stay true when someone attacks
          </h1>
          <p className="mt-5 max-w-2xl text-lg leading-relaxed text-stone-300">
            This is a builder-first course in <strong className="font-medium text-white">secure application engineering</strong>:
            web, API, and later Android. You learn to name an invariant, watch it
            fail in an authorized lab, repair it, and prove the repair. TLS, JWT,
            bcrypt, and scanners are mechanisms. They are not the property.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <ButtonLink href="/learn/1.1/01-property-vs-mechanism/" onDark>
              Start with module 1.1
            </ButtonLink>
            <ButtonLink href="/learn/" variant="secondary" onDark>
              Browse {moduleCount} modules
            </ButtonLink>
            <ButtonLink href="/roadmap/" variant="secondary" onDark>
              See the roadmap
            </ButtonLink>
          </div>
          <HomeContinue />
        </div>
      </section>

      <div className="mx-auto max-w-5xl space-y-16 px-4 py-12 sm:py-16">
        <section>
          <h2 className="text-2xl font-semibold tracking-tight text-stone-900">
            What this is
          </h2>
          <p className="mt-3 max-w-prose leading-relaxed text-stone-700">
            A first-principles path, not a rotating awareness list. You ship
            vertical slices of <strong>SecureCollab</strong> — a small multi-tenant
            notes product that later grows files, sharing, workers, and mobile —
            and you rewrite the same catalogue when identity, data, or operating
            assumptions change.
          </p>
          <ul className="mt-6 grid gap-4 sm:grid-cols-3">
            <li className="rounded-xl border border-stone-200 bg-white p-4 shadow-sm">
              <p className="text-sm font-medium uppercase tracking-wide text-stone-500">
                Thesis
              </p>
              <p className="mt-2 font-semibold text-stone-900">Invariants, not tools</p>
              <p className="mt-2 text-sm leading-relaxed text-stone-700">
                Every control is derived from a threat and a required property.
                If a second person cannot write a failing test, it is still a slogan.
              </p>
            </li>
            <li className="rounded-xl border border-stone-200 bg-white p-4 shadow-sm">
              <p className="text-sm font-medium uppercase tracking-wide text-stone-500">
                Product spine
              </p>
              <p className="mt-2 font-semibold text-stone-900">SecureCollab</p>
              <p className="mt-2 text-sm leading-relaxed text-stone-700">
                Tenant-scoped notes, then files and sharing. Default stack: FastAPI,
                PostgreSQL, TypeScript/Next.js; Android/Kotlin on the mobile track.
              </p>
            </li>
            <li className="rounded-xl border border-stone-200 bg-white p-4 shadow-sm">
              <p className="text-sm font-medium uppercase tracking-wide text-stone-500">
                Assurance
              </p>
              <p className="mt-2 font-semibold text-stone-900">Pinned standards</p>
              <p className="mt-2 text-sm leading-relaxed text-stone-700">
                OWASP ASVS 5.0 (Level 2 plus selected Level 3) and MASVS 2.1 as
                verification language. Top 10 / CWE lists are regression checks
                after the cause, not the syllabus.
              </p>
            </li>
          </ul>
        </section>

        <section>
          <h2 className="text-2xl font-semibold tracking-tight text-stone-900">
            What to expect
          </h2>
          <p className="mt-3 max-w-prose leading-relaxed text-stone-700">
            Each module repeats the same seven-step loop. Lessons live here.
            Vulnerable fixtures and pytest live in your git clone. This website
            never runs exploits and never publishes examiner keys.
          </p>
          <ol className="mt-6 grid gap-3 sm:grid-cols-2">
            {LOOP.map((step, index) => (
              <li
                key={step.title}
                className="flex gap-3 rounded-xl border border-stone-200 bg-white p-4"
              >
                <span className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-stone-900 text-xs font-semibold text-white">
                  {index + 1}
                </span>
                <span>
                  <span className="block font-semibold text-stone-900">{step.title}</span>
                  <span className="mt-1 block text-sm leading-relaxed text-stone-700">
                    {step.body}
                  </span>
                </span>
              </li>
            ))}
          </ol>
          <ul className="mt-6 max-w-prose list-disc space-y-2 pl-5 leading-relaxed text-stone-800">
            <li>Work phases in order. Phase 8 (mobile) can wait on a web/API milestone. Electives open after Phase 7.</li>
            <li>Progress checkboxes are stored in this browser only. There are no accounts yet.</li>
            <li>Mastery gates on this site stay ungraded. Completing a lesson is not Gate evidence.</li>
          </ul>
        </section>

        <section>
          <h2 className="text-2xl font-semibold tracking-tight text-stone-900">
            How to start
          </h2>
          <ol className="mt-6 space-y-4">
            <li className="rounded-xl border border-stone-200 bg-white p-4">
              <p className="font-semibold text-stone-900">1. Read the orientation</p>
              <p className="mt-1 text-sm leading-relaxed text-stone-700">
                Authorized lab scope, local-first progress, and how a module is
                organized. Then the thesis module: property versus mechanism.
              </p>
              <p className="mt-3 flex flex-wrap gap-3">
                <ButtonLink href="/learn/0.1/" variant="secondary">
                  Orientation 0.1
                </ButtonLink>
                <ButtonLink href="/learn/1.1/">Module 1.1</ButtonLink>
              </p>
            </li>
            <li className="rounded-xl border border-stone-200 bg-white p-4">
              <p className="font-semibold text-stone-900">2. Follow the roadmap</p>
              <p className="mt-1 text-sm leading-relaxed text-stone-700">
                Hard order is 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 9 → 10 → 11.
                Open a module, then read its lessons left to right.
              </p>
              <p className="mt-3">
                <ButtonLink href="/roadmap/" variant="secondary">
                  Open the roadmap
                </ButtonLink>
              </p>
            </li>
            <li className="rounded-xl border border-stone-200 bg-white p-4">
              <p className="font-semibold text-stone-900">3. Run labs in your clone</p>
              <p className="mt-1 text-sm leading-relaxed text-stone-700">
                When a lesson points at a fixture, clone the repository and run
                pytest from that lab directory. The brief on this site is not a
                live target.
              </p>
              <p className="mt-3">
                <ButtonLink href="/labs/" variant="secondary">
                  Lab briefs
                </ButtonLink>
              </p>
            </li>
          </ol>
        </section>

        <section>
          <h2 className="text-2xl font-semibold tracking-tight text-stone-900">
            This site is not
          </h2>
          <ul className="mt-4 grid gap-4 sm:grid-cols-3">
            <li className="rounded-xl border border-stone-200 bg-stone-100 p-4">
              <p className="font-semibold text-stone-900">A Top 10 playlist</p>
              <p className="mt-2 text-sm leading-relaxed text-stone-700">
                Awareness lists are regression checks after you have a cause, not
                the outline of the course.
              </p>
            </li>
            <li className="rounded-xl border border-stone-200 bg-stone-100 p-4">
              <p className="font-semibold text-stone-900">A hosted vulnerable app</p>
              <p className="mt-2 text-sm leading-relaxed text-stone-700">
                Labs stay in git. This origin is a static reading site. It does
                not execute exploits.
              </p>
            </li>
            <li className="rounded-xl border border-stone-200 bg-stone-100 p-4">
              <p className="font-semibold text-stone-900">Permission to attack others</p>
              <p className="mt-2 text-sm leading-relaxed text-stone-700">
                Do not target public, third-party, or production systems. Read{" "}
                <Link href="/policy/" className="text-blue-900 underline underline-offset-2">
                  Safe use
                </Link>
                .
              </p>
            </li>
          </ul>
        </section>

        <section>
          <h2 className="mb-4 text-2xl font-semibold tracking-tight text-stone-900">
            Find your way
          </h2>
          <ul className="grid gap-3 sm:grid-cols-2">
            <li>
              <CardLink href="/learn/" kicker={`${moduleCount} units`} title="Catalog">
                Every module’s lessons, generated from the content schema.
              </CardLink>
            </li>
            <li>
              <CardLink href="/glossary/" title="Glossary">
                Invariant, TCB, residual risk, and the other working terms.
              </CardLink>
            </li>
            <li>
              <CardLink href="/checkpoints/" title="Checkpoints">
                Mastery gates stay ungraded here until you have evidence.
              </CardLink>
            </li>
            <li>
              <CardLink href="/standards/" title="Standards">
                Pinned versions and status. Drafts stay labeled draft.
              </CardLink>
            </li>
          </ul>
        </section>
      </div>
    </div>
  );
}
