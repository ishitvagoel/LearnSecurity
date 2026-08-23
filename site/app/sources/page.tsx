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
        Research snapshot 2026-08-23. Module changelogs live on each module
        page via <code>module.yaml</code>. This site does not publish examiner
        keys.
      </p>
      <ul className="list-disc pl-6">
        {pins.map((p) => (
          <li key={p.id} className="mb-2 max-w-prose">
            <a href={p.url} className="text-blue-900 underline">
              {p.source}
            </a>{" "}
            {p.version} ({p.status})
            {p.reviewedAt ? ` · reviewed ${p.reviewedAt}` : ""}
          </li>
        ))}
      </ul>
    </article>
  );
}
