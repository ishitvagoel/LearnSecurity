import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";

export default function PolicyPage() {
  return (
    <PageShell width="narrow">
      <PageHeader title="Safe-use policy">
        <p>
          LearnSecurity teaches cause, invariant, and repair. It does not teach
          you to attack systems you do not own. This origin is a static reading
          site. It never runs the vulnerable fixtures.
        </p>
      </PageHeader>
      <div className="grid gap-4 sm:grid-cols-2">
        <section className="rounded-xl border border-emerald-200 bg-emerald-50 px-4 py-4">
          <h2 className="mb-3 text-lg font-semibold">You may</h2>
          <ul className="list-disc space-y-2 pl-5 leading-relaxed">
            <li>Study lessons and briefs on this website.</li>
            <li>
              Run pytest against{" "}
              <code className="rounded bg-white/80 px-1">labs/</code> in your local
              clone of this repository.
            </li>
            <li>
              Use official training applications (for example OWASP Juice Shop)
              according to their published terms.
            </li>
            <li>
              Test systems you own, or for which you have written authorization and
              a defined scope.
            </li>
          </ul>
        </section>
        <section className="rounded-xl border border-rose-200 bg-rose-50 px-4 py-4">
          <h2 className="mb-3 text-lg font-semibold">You must not</h2>
          <ul className="list-disc space-y-2 pl-5 leading-relaxed">
            <li>Target public, third-party, or production systems from this course.</li>
            <li>Copy weaponized payloads into learner notes or pull requests.</li>
            <li>Upload real PII, patient data, or production secrets as “evidence.”</li>
            <li>
              Treat examiner keys (if you obtain them) as something to publish on
              this origin.
            </li>
          </ul>
        </section>
      </div>
      <p className="mt-6 max-w-prose leading-relaxed text-stone-800">
        Lab data is synthetic. Secrets in fixtures are disposable. Reset from
        git after each lab. Questions about scope: start from{" "}
        <Link href="/labs/" className="text-blue-900 underline underline-offset-2">
          Labs
        </Link>
        .
      </p>
    </PageShell>
  );
}
