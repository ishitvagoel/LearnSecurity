import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";
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
    <PageShell>
      <PageHeader title="Standards explorer">
        <p>
          Pins come from{" "}
          <code className="rounded bg-stone-200 px-1">content/standards/pins.yaml</code>{" "}
          (research snapshot 2026-08-23). Drafts stay labeled draft. ASVS/MASVS
          chapters are verification language, not a shopping list. OWASP Top 10
          and CWE Top 25 are regression checks after you have a property.
        </p>
      </PageHeader>
      <h2 className="mb-3 text-xl font-semibold">Pinned sources</h2>
      <ul className="mb-10 grid gap-3 sm:grid-cols-2">
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
              {p.role ? ` — ${p.role}` : ""}
            </p>
            {p.notes ? (
              <p className="mt-2 text-sm leading-relaxed text-stone-600">{p.notes}</p>
            ) : null}
          </li>
        ))}
      </ul>
      <h2 className="mb-3 text-xl font-semibold">Where modules cite them</h2>
      <ul className="divide-y divide-stone-200 overflow-hidden rounded-xl border border-stone-200 bg-white">
        {modules.map((m) => (
          <li key={m.id} className="px-4 py-3">
            <Link
              href={moduleHref(m.id)}
              className="font-medium text-blue-900 underline-offset-2 hover:underline"
            >
              {m.id}
            </Link>
            <p className="mt-1 text-sm leading-relaxed text-stone-700">
              {m.standardsRefs
                .map((s) => `${s.source} ${s.version} (${s.status})`)
                .join(" · ")}
            </p>
          </li>
        ))}
      </ul>
    </PageShell>
  );
}
