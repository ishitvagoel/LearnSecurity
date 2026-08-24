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
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Sources and changelog</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        Research snapshot 2026-08-23. Prefer the canonical URL and version
        below over blog posts. Module-level changelog lives on each{" "}
        <code>module.yaml</code>. This site does not publish examiner keys.
      </p>
      <ul className="list-disc pl-6">
        {pins.map((p) => (
          <li key={p.id} className="mb-3 max-w-prose">
            <a href={p.url} className="text-blue-900 underline">
              {p.source}
            </a>{" "}
            {p.version} ({p.status})
            {p.reviewedAt ? ` · reviewed ${p.reviewedAt}` : ""}
            {p.notes ? (
              <span className="block text-sm text-stone-700">{p.notes}</span>
            ) : null}
          </li>
        ))}
      </ul>
    </article>
  );
}
