import Link from "next/link";

export default function HomePage() {
  return (
    <article>
      <p className="mb-2 text-sm font-medium uppercase tracking-wide text-stone-700">
        LearnSecurity · blueprint 1.1
      </p>
      <h1 className="mb-4 text-4xl font-semibold">
        Security is what must stay true when someone attacks
      </h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        This is a first-principles course in building software whose{" "}
        <strong>invariants</strong> survive misuse, component failure, and an
        attacker with named capabilities. TLS, JWT, bcrypt, and scanners are
        mechanisms. They are not the property.
      </p>
      <p className="mb-6 max-w-prose leading-relaxed">
        The through-line product is <strong>SecureCollab</strong>: tenant-scoped
        notes, later files and sharing. You will keep rewriting the same
        catalogue as identity, data, APIs, and operations get real. Default
        stack: FastAPI, PostgreSQL, TypeScript/Next.js; Android/Kotlin on the
        mobile track.
      </p>

      <div className="mb-8 flex flex-wrap gap-3">
        <Link
          href="/learn/1.1/01-property-vs-mechanism/"
          className="inline-block rounded bg-blue-900 px-4 py-2 font-medium text-white"
        >
          Start module 1.1
        </Link>
        <Link
          href="/learn/0.1/"
          className="inline-block rounded border border-stone-400 bg-white px-4 py-2 font-medium text-stone-900"
        >
          Orientation (0.1)
        </Link>
      </div>

      <h2 className="mb-2 text-2xl font-semibold">How each module works</h2>
      <ol className="mb-6 max-w-prose list-decimal pl-6 leading-relaxed">
        <li>State a testable property of SecureCollab (or the elective system).</li>
        <li>Name principals, objects, and channels.</li>
        <li>Break it in an <strong>authorized local lab</strong> — not on this website.</li>
        <li>Restore the property with the smallest structural control.</li>
        <li>Verify with a test that fails on the broken fixture and passes on the fix.</li>
        <li>Detect and recover; residual risk stays explicit.</li>
        <li>Transfer the same sentence to a new channel or object—without a Top 10 slogan.</li>
      </ol>

      <h2 className="mb-2 text-2xl font-semibold">On this site</h2>
      <ul className="mb-6 list-disc pl-6 leading-relaxed">
        <li>
          <Link href="/roadmap/" className="text-blue-900 underline">
            Roadmap
          </Link>{" "}
          — phases, core / mobile / elective, what to study in order
        </li>
        <li>
          <Link href="/learn/" className="text-blue-900 underline">
            Learn
          </Link>{" "}
          — every module’s lessons, generated from the content schema
        </li>
        <li>
          <Link href="/labs/" className="text-blue-900 underline">
            Labs
          </Link>{" "}
          — briefs only; pytest runs in your git checkout
        </li>
        <li>
          <Link href="/checkpoints/" className="text-blue-900 underline">
            Checkpoints
          </Link>{" "}
          — mastery gates stay ungraded here until you have evidence
        </li>
      </ul>

      <h2 className="mb-2 text-2xl font-semibold">Safe use</h2>
      <p className="mb-4 max-w-prose leading-relaxed">
        Offensive work is limited to local course apps, official training labs,
        or systems you are written-authorized to test. This origin does not host
        or execute vulnerable lab code and does not publish examiner keys. Read{" "}
        <Link href="/policy/" className="text-blue-900 underline">
          Safe use
        </Link>
        .
      </p>
      <p className="max-w-prose text-sm text-stone-700">
        Progress checkboxes are stored in this browser only. No accounts.
      </p>
    </article>
  );
}
