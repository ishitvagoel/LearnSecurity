import Link from "next/link";
import { loadAllModules } from "@/lib/loadCurriculum";

export default function LabsIndexPage() {
  const withLabs = loadAllModules().filter((m) => m.labSpec);
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Labs</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        Every lab on this course is a <strong>local, authorized fixture</strong>.
        Vulnerable and fixed trees live under <code>labs/</code> in git. This
        website only publishes the brief: the property, the forbidden outcome,
        and how to run pytest. It does not execute exploits or host a vulnerable
        server.
      </p>
      <ol className="mb-6 max-w-prose list-decimal pl-6 leading-relaxed">
        <li>Clone the repository. Work only inside the listed lab directory.</li>
        <li>
          Follow that lab’s <code>README.md</code>. The property test must{" "}
          <strong>fail</strong> on the vulnerable tree and <strong>pass</strong> on
          the fixed tree.
        </li>
        <li>Reset from git. Do not keep mutated fixtures as “production.”</li>
      </ol>
      <p className="mb-6 max-w-prose leading-relaxed">
        Data is synthetic. Secrets are disposable. Do not point these tests at
        shared, third-party, or production systems. See{" "}
        <Link href="/policy/" className="text-blue-900 underline">
          Safe use
        </Link>
        .
      </p>
      <ul className="list-disc pl-6">
        {withLabs.map((m) => (
          <li key={m.id} className="mb-2">
            <Link
              href={`/labs/${encodeURIComponent(m.id)}/`}
              className="text-blue-900 underline"
            >
              {m.id} — {m.labSpec?.slug || "lab"}
            </Link>
            {m.labSpec?.summary ? (
              <span className="text-stone-700"> — {m.labSpec.summary}</span>
            ) : null}
          </li>
        ))}
      </ul>
    </article>
  );
}
