import Link from "next/link";
import { notFound } from "next/navigation";
import { PageHeader, PageShell } from "@/components/ui";
import { topicBlurb, topicTitle } from "@/lib/catalog";
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
          All practice
        </Link>
        {" · "}
        <Link
          href={moduleHref(mod.id)}
          className="text-blue-900 underline-offset-2 hover:underline"
        >
          {mod.id} — {topicTitle(mod)}
        </Link>
      </p>
      <PageHeader title={`Practice — ${mod.id}`}>
        <p>{topicBlurb(mod)}</p>
        <p>
          Run this only on your computer, using the course files. Do not point
          it at a live website or anyone else’s system.
        </p>
      </PageHeader>
      <section className="mb-8 rounded-xl border border-rose-200 bg-rose-50 px-4 py-4">
        <h2 className="mb-2 text-xl font-semibold">What must not happen</h2>
        <p className="mb-3 text-sm text-stone-700">
          The check should fail on the broken files and pass on the repaired
          ones. If both pass, the check is not catching the bug.
        </p>
        <ul className="list-disc space-y-2 pl-5 leading-relaxed">
          {(mod.labSpec.forbiddenOutcomes || []).map((o) => (
            <li key={o}>{o}</li>
          ))}
        </ul>
      </section>
      <section>
        <h2 className="mb-3 text-xl font-semibold">How to run it on your computer</h2>
        <ol className="list-decimal space-y-2 pl-5 leading-relaxed">
          <li>Copy this LearnSecurity repository to your computer.</li>
          <li>
            Open{" "}
            <code className="rounded bg-stone-200 px-1">
              labs/{mod.id}/{slug}/
            </code>{" "}
            and read its README.
          </li>
          <li>
            Run the check listed in that README on the broken files (it should
            fail), then on the repaired files (it should pass).
          </li>
          <li>Restore the practice folder from git when you are done. Use only the fake data in the files.</li>
        </ol>
      </section>
    </PageShell>
  );
}
