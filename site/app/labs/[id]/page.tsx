import Link from "next/link";
import { notFound } from "next/navigation";
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
    <article>
      <p className="mb-2 text-sm">
        <Link href="/labs/" className="text-blue-900 underline">
          All labs
        </Link>
        {" · "}
        <Link href={moduleHref(mod.id)} className="text-blue-900 underline">
          {mod.id} — {mod.title}
        </Link>
      </p>
      <h1 className="mb-4 text-3xl font-semibold">Lab brief — {mod.id}</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        <strong>Authorized scope:</strong> {mod.labSpec.authorizedScope}
      </p>
      <p className="mb-4 max-w-prose leading-relaxed">{mod.labSpec.summary}</p>
      <h2 className="mb-2 text-2xl font-semibold">Forbidden outcomes</h2>
      <p className="mb-2 max-w-prose text-sm text-stone-700">
        The property test must fail on the vulnerable tree and pass on the
        fixed tree. If both pass, you are not testing the invariant.
      </p>
      <ul className="mb-4 list-disc pl-6">
        {(mod.labSpec.forbiddenOutcomes || []).map((o) => (
          <li key={o}>{o}</li>
        ))}
      </ul>
      <h2 className="mb-2 text-2xl font-semibold">Run locally (not on this origin)</h2>
      <ol className="max-w-prose list-decimal pl-6 leading-relaxed">
        <li>Clone this LearnSecurity repository.</li>
        <li>
          Open <code>labs/{mod.id}/{slug}/</code> and read its README.
        </li>
        <li>
          Run the listed pytest command against the vulnerable tree (must fail)
          then the fixed tree (must pass).
        </li>
        <li>Restore the lab directory from git. Synthetic data only.</li>
      </ol>
    </article>
  );
}
