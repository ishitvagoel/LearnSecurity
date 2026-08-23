import Link from "next/link";
import { loadAllModules, loadPins, moduleHref } from "@/lib/loadCurriculum";

type Pin = {
  id: string;
  source: string;
  version: string;
  status: string;
  url: string;
  role?: string;
  notes?: string;
};

export default function StandardsPage() {
  const raw = loadPins() as { pins?: Pin[] };
  const pins = raw.pins || [];
  const modules = loadAllModules();
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Standards explorer</h1>
      <p className="mb-6 max-w-prose leading-relaxed">
        Pins from <code>content/standards/pins.yaml</code>. Drafts stay labeled
        draft. Awareness lists are not compliance.
      </p>
      <h2 className="mb-3 text-2xl font-semibold">Pinned sources</h2>
      <ul className="mb-8 list-disc pl-6">
        {pins.map((p) => (
          <li key={p.id} className="mb-3 max-w-prose">
            <a href={p.url} className="text-blue-900 underline">
              {p.source}
            </a>{" "}
            {p.version} ({p.status})
            {p.role ? ` — ${p.role}` : ""}
          </li>
        ))}
      </ul>
      <h2 className="mb-3 text-2xl font-semibold">Module crosswalk</h2>
      <ul className="list-disc pl-6">
        {modules.map((m) => (
          <li key={m.id} className="mb-2 max-w-prose">
            <Link href={moduleHref(m.id)} className="text-blue-900 underline">
              {m.id}
            </Link>
            {": "}
            {m.standardsRefs
              .map((s) => `${s.source} ${s.version} (${s.status})`)
              .join("; ")}
          </li>
        ))}
      </ul>
    </article>
  );
}
