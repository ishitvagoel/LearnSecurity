import { PageHeader, PageShell } from "@/components/ui";
import { PHASES, phaseList } from "@/lib/catalog";
import { loadAllModules } from "@/lib/loadCurriculum";
import Link from "next/link";

export default function LabsIndexPage() {
  const withLabs = loadAllModules().filter((m) => m.labSpec);
  const phases = phaseList(withLabs);

  return (
    <PageShell>
      <PageHeader kicker="Authorized fixtures" title="Labs">
        <p>
          Every lab on this course is a <strong>local, authorized fixture</strong>.
          Vulnerable and fixed trees live under <code>labs/</code> in git. This
          website only publishes the brief: the property, the forbidden outcome,
          and how to run pytest. It does not execute exploits or host a vulnerable
          server.
        </p>
      </PageHeader>
      <ol className="mb-8 max-w-prose list-decimal space-y-2 pl-5 leading-relaxed">
        <li>Clone the repository. Work only inside the listed lab directory.</li>
        <li>
          Follow that lab’s <code className="rounded bg-stone-200 px-1">README.md</code>.
          The property test must <strong>fail</strong> on the vulnerable tree and{" "}
          <strong>pass</strong> on the fixed tree.
        </li>
        <li>Reset from git. Do not keep mutated fixtures as “production.”</li>
      </ol>
      <p className="mb-8 max-w-prose leading-relaxed text-stone-800">
        Data is synthetic. Secrets are disposable. Do not point these tests at
        shared, third-party, or production systems. See{" "}
        <Link href="/policy/" className="text-blue-900 underline underline-offset-2">
          Safe use
        </Link>
        .
      </p>
      {phases.map((phase) => {
        const meta = PHASES[phase];
        const items = withLabs.filter((m) => m.phase === phase);
        return (
          <section key={phase} className="mb-10">
            <h2 className="mb-3 text-xl font-semibold">
              Phase {phase}
              {meta ? ` — ${meta.title}` : ""}
            </h2>
            <ul className="grid gap-3 sm:grid-cols-2">
              {items.map((m) => (
                <li key={m.id}>
                  <Link
                    href={`/labs/${encodeURIComponent(m.id)}/`}
                    className="block h-full rounded-xl border border-stone-200 bg-white p-4 shadow-sm hover:border-stone-400"
                  >
                    <p className="font-mono text-xs text-stone-600">{m.id}</p>
                    <p className="mt-1 font-semibold text-blue-900">
                      {m.labSpec?.slug || m.title}
                    </p>
                    {m.labSpec?.summary ? (
                      <p className="mt-2 line-clamp-3 text-sm leading-relaxed text-stone-700">
                        {m.labSpec.summary}
                      </p>
                    ) : null}
                  </Link>
                </li>
              ))}
            </ul>
          </section>
        );
      })}
    </PageShell>
  );
}
