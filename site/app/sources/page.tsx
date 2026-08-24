import { PageHeader, PageShell } from "@/components/ui";
import { loadPins } from "@/lib/loadCurriculum";

type Pin = {
  id: string;
  source: string;
  version: string;
  status: string;
  reviewedAt?: string;
  url: string;
  notes?: string;
};

export default function SourcesPage() {
  const raw = loadPins() as { pins?: Pin[] };
  const pins = raw.pins || [];
  return (
    <PageShell>
      <PageHeader title="Sources and changelog">
        <p>
          Research snapshot 2026-08-23. Prefer the canonical URL and version
          below over blog posts. Module-level changelog lives on each{" "}
          <code className="rounded bg-stone-200 px-1">module.yaml</code>. This
          site does not publish examiner keys.
        </p>
      </PageHeader>
      <ul className="grid gap-3 sm:grid-cols-2">
        {pins.map((p) => (
          <li
            key={p.id}
            className="rounded-xl border border-stone-200 bg-white p-4"
          >
            <a
              href={p.url}
              className="font-semibold text-blue-900 underline-offset-2 hover:underline"
              rel="noreferrer"
              target="_blank"
            >
              {p.source}
            </a>
            <p className="mt-1 text-sm text-stone-700">
              {p.version} ({p.status})
              {p.reviewedAt ? ` · reviewed ${p.reviewedAt}` : ""}
            </p>
            {p.notes ? (
              <p className="mt-2 text-sm leading-relaxed text-stone-600">{p.notes}</p>
            ) : null}
          </li>
        ))}
      </ul>
    </PageShell>
  );
}
