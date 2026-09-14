import Link from "next/link";
import { notFound } from "next/navigation";
import { LastActivityMarker } from "@/components/LastActivityMarker";
import { PageHeader, PageShell } from "@/components/ui";
import { loadBridges } from "@/lib/bridges";

type Props = { params: Promise<{ id: string }> };

export const dynamicParams = false;

export function generateStaticParams() {
  return loadBridges().map((bridge) => ({ id: bridge.id }));
}

export async function generateMetadata({ params }: Props) {
  const { id } = await params;
  const bridge = loadBridges().find((item) => item.id === id);
  return { title: bridge?.title || "Tooling bridge", description: bridge?.objective };
}

export default async function BridgePage({ params }: Props) {
  const { id } = await params;
  const bridge = loadBridges().find((item) => item.id === id);
  if (!bridge) notFound();
  return (
    <PageShell width="narrow">
      <LastActivityMarker href={`/bridges/${encodeURIComponent(bridge.id)}/`} title={bridge.title} />
      <p className="mb-3 text-sm text-muted">
        <Link href="/bridges/" className="text-link underline-offset-2 hover:underline">Tooling bridges</Link>
        {" · "}{bridge.capability}
      </p>
      <PageHeader title={bridge.title}>
        <p>{bridge.objective}</p>
      </PageHeader>
      <div className="space-y-6">
        <section className="rounded-2xl border border-line bg-paper p-5">
          <h2 className="text-xl font-semibold text-ink">Task</h2>
          <p className="mt-2 whitespace-pre-line leading-relaxed text-ink">{bridge.task}</p>
        </section>
        <section className="rounded-2xl border border-forest-accent/20 bg-surface p-5">
          <h2 className="text-xl font-semibold text-ink">You can move on when</h2>
          <p className="mt-2 leading-relaxed text-ink">{bridge.success}</p>
        </section>
        <section className="rounded-2xl border border-amber-200 bg-amber-50 p-5">
          <h2 className="text-xl font-semibold text-ink">If the task is blocked</h2>
          <p className="mt-2 leading-relaxed text-ink">{bridge.retry}</p>
        </section>
      </div>
      <p className="mt-8">
        <Link href="/bridges/" className="text-link underline-offset-2 hover:underline">
          Back to all tooling bridges
        </Link>
      </p>
    </PageShell>
  );
}
