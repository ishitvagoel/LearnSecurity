import Link from "next/link";
import { notFound } from "next/navigation";
import { PageHeader, PageShell } from "@/components/ui";
import { loadAllModules, loadModule, moduleHref } from "@/lib/loadCurriculum";

type Props = { params: Promise<{ id: string }> };

export const dynamicParams = false;

export function generateStaticParams() {
  return loadAllModules()
    .filter((m) => m.labSpec)
    .map((m) => ({ id: m.id }));
}

export default async function LabBriefPage({ params }: Props) {
  const { id } = await params;
  const exists = loadAllModules().some((m) => m.id === id);
  if (!exists) {
    notFound();
  }
  const mod = loadModule(id);
  if (!mod.labSpec) {
    notFound();
  }
  const slug = mod.labSpec.slug || `${mod.id}-lab`;
  return (
    <PageShell width="narrow">
      <p className="mb-3 text-sm text-stone-600">
        <Link href="/labs/" className="text-blue-900 underline-offset-2 hover:underline">
          All labs
        </Link>
        {" · "}
        <Link
          href={moduleHref(mod.id)}
          className="text-blue-900 underline-offset-2 hover:underline"
        >
          {mod.id} — {mod.title}
        </Link>
      </p>
      <PageHeader title={`Lab brief — ${mod.id}`}>
        <p>
          <strong>Authorized scope:</strong> {mod.labSpec.authorizedScope}
        </p>
        <p>{mod.labSpec.summary}</p>
      </PageHeader>
      <section className="mb-8 rounded-xl border border-rose-200 bg-rose-50 px-4 py-4">
        <h2 className="mb-2 text-xl font-semibold">Forbidden outcomes</h2>
        <p className="mb-3 text-sm text-stone-700">
          The property test must fail on the vulnerable tree and pass on the
          fixed tree. If both pass, you are not testing the invariant.
        </p>
        <ul className="list-disc space-y-2 pl-5 leading-relaxed">
          {(mod.labSpec.forbiddenOutcomes || []).map((o) => (
            <li key={o}>{o}</li>
          ))}
        </ul>
      </section>
      <section>
        <h2 className="mb-3 text-xl font-semibold">Run locally (not on this origin)</h2>
        <ol className="list-decimal space-y-2 pl-5 leading-relaxed">
          <li>Clone this LearnSecurity repository.</li>
          <li>
            Open{" "}
            <code className="rounded bg-stone-200 px-1">
              labs/{mod.id}/{slug}/
            </code>{" "}
            and read its README.
          </li>
          <li>
            Run the listed pytest command against the vulnerable tree (must fail)
            then the fixed tree (must pass).
          </li>
          <li>Restore the lab directory from git. Synthetic data only.</li>
        </ol>
      </section>
    </PageShell>
  );
}
