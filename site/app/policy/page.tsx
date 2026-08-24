import Link from "next/link";

export default function PolicyPage() {
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Safe-use policy</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        LearnSecurity teaches cause, invariant, and repair. It does not teach
        you to attack systems you do not own. This origin is a static reading
        site. It never runs the vulnerable fixtures.
      </p>
      <h2 className="mb-2 mt-6 text-2xl font-semibold">You may</h2>
      <ul className="mb-4 list-disc pl-6 leading-relaxed">
        <li>Study lessons and briefs on this website.</li>
        <li>
          Run pytest against <code>labs/</code> in your local clone of this
          repository.
        </li>
        <li>
          Use official training applications (for example OWASP Juice Shop)
          according to their published terms.
        </li>
        <li>Test systems you own, or for which you have written authorization and a defined scope.</li>
      </ul>
      <h2 className="mb-2 mt-6 text-2xl font-semibold">You must not</h2>
      <ul className="mb-4 list-disc pl-6 leading-relaxed">
        <li>Target public, third-party, or production systems from this course.</li>
        <li>Copy weaponized payloads into learner notes or pull requests.</li>
        <li>Upload real PII, patient data, or production secrets as “evidence.”</li>
        <li>Treat examiner keys (if you obtain them) as something to publish on this origin.</li>
      </ul>
      <p className="max-w-prose leading-relaxed">
        Lab data is synthetic. Secrets in fixtures are disposable. Reset from
        git after each lab. Questions about scope: start from{" "}
        <Link href="/labs/" className="text-blue-900 underline">
          Labs
        </Link>
        .
      </p>
    </article>
  );
}
