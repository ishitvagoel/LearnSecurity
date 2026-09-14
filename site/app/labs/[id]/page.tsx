import Link from "next/link";
import { notFound } from "next/navigation";
import { LastActivityMarker } from "@/components/LastActivityMarker";
import { PageHeader, PageShell } from "@/components/ui";
import { topicBlurb, topicTitle } from "@/lib/catalog";
import { loadAllModules, loadModule, moduleHref } from "@/lib/loadCurriculum";
import { learnerFacingOutcomes } from "@/lib/plainCopy";

type Props = { params: Promise<{ id: string }> };

export const dynamicParams = false;

export function generateStaticParams() {
  return loadAllModules()
    .filter((m) => m.labSpec)
    .map((m) => ({ id: m.id }));
}

export async function generateMetadata({ params }: Props) {
  const { id } = await params;
  const mod = loadAllModules().find((m) => m.id === id);
  return {
    title: mod ? `Practice — ${mod.id} ${topicTitle(mod)}` : "Practice",
    description: mod ? topicBlurb(mod) : undefined,
  };
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
      <LastActivityMarker href={`/labs/${encodeURIComponent(mod.id)}/`} title={`Practice — ${mod.id}`} />
      <p className="mb-3 text-sm text-muted">
        <Link href="/labs/" className="text-link underline-offset-2 hover:underline">
          All practice
        </Link>
        {" · "}
        <Link
          href={moduleHref(mod.id)}
          className="text-link underline-offset-2 hover:underline"
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
        <p className="mb-3 text-sm text-muted">
          The check should fail on the broken files and pass on the repaired
          ones. If both pass, the check is not catching the bug.
        </p>
        <ul className="list-disc space-y-2 pl-5 leading-relaxed">
          {learnerFacingOutcomes(mod.labSpec.forbiddenOutcomes).map((o) => (
            <li key={o}>{o}</li>
          ))}
        </ul>
      </section>
      <section>
        <h2 className="mb-3 text-xl font-semibold">Where to find it</h2>
        <p className="leading-relaxed text-muted">
          In your copy of the repository, open{" "}
          <code className="rounded bg-surface-hover px-1">
            labs/{mod.id}/{slug}/
          </code>{" "}
          and read its README. See{" "}
          <Link href="/labs/" className="font-medium text-link underline underline-offset-2">
            Practice
          </Link>{" "}
          for the steps to copy, run, and reset the files.
        </p>
      </section>
      <section className="mt-8 rounded-xl border border-line bg-surface px-4 py-4">
        <h2 className="mb-2 text-xl font-semibold">After the practice</h2>
        <p className="leading-relaxed text-muted">
          Record the intended failure and the repaired result, then use the{" "}
          <Link href={`/assess/${encodeURIComponent(mod.id)}/`} className="font-medium text-link underline underline-offset-2">
            evidence worksheet
          </Link>{" "}
          to explain what the lab proves and what it leaves open.
        </p>
      </section>
    </PageShell>
  );
}
