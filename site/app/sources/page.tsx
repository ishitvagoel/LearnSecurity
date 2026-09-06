import { PageHeader, PageShell } from "@/components/ui";
import { pinStatusLabel } from "@/lib/catalog";
import { loadPins } from "@/lib/loadCurriculum";

type Pin = {
  id: string;
  source: string;
  version: string;
  status: string;
  reviewedAt?: string;
  url: string;
};

export default function SourcesPage() {
  const raw = loadPins() as { pins?: Pin[] };
  const pins = raw.pins || [];
  return (
    <PageShell>
      <PageHeader title="Where we got this">
        <p>
          These are the papers and lists the course cites. Prefer the link and
          version below over a blog post. This site does not publish answer
          keys.
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
              {p.version} · {pinStatusLabel(p.status)}
              {p.reviewedAt ? ` · last checked ${p.reviewedAt}` : ""}
            </p>
          </li>
        ))}
      </ul>
    </PageShell>
  );
}
