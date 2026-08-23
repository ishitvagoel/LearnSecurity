import Link from "next/link";

export default function HomePage() {
  return (
    <article>
      <h1 className="mb-4 text-4xl font-semibold">
        Security is invariants under attack
      </h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        This course teaches you to design, build, verify, deploy, and operate
        applications so named security properties remain true when someone
        misuses the system, a component fails, or an attacker with stated
        capabilities acts. Tools and Top 10 lists are regression checks, not
        the syllabus.
      </p>
      <p className="mb-4 max-w-prose leading-relaxed">
        Stack defaults: FastAPI, PostgreSQL, TypeScript/Next.js; Android/Kotlin
        on the mobile track. Progress on this site is stored only in your
        browser.
      </p>
      <h2 className="mb-2 mt-8 text-2xl font-semibold">Safe use</h2>
      <p className="mb-4 max-w-prose leading-relaxed">
        Offensive work is limited to local course apps, official training labs,
        or systems you are written-authorized to test. This website does{" "}
        <strong>not</strong> host or execute vulnerable lab code. See{" "}
        <Link href="/policy/" className="text-blue-900 underline">
          Safe use
        </Link>
        .
      </p>
      <ul className="list-disc pl-6 leading-relaxed">
        <li>
          <Link href="/roadmap/" className="text-blue-900 underline">
            Roadmap
          </Link>{" "}
          — phases, core / mobile / elective
        </li>
        <li>
          <Link href="/learn/" className="text-blue-900 underline">
            Learn
          </Link>{" "}
          — module pages from the content schema
        </li>
        <li>
          <Link href="/labs/" className="text-blue-900 underline">
            Labs
          </Link>{" "}
          — how to run fixtures in the git checkout, not here
        </li>
      </ul>
    </article>
  );
}
