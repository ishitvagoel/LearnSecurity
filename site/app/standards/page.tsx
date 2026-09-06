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
      <div className="overflow-x-auto rounded-xl border border-stone-200 bg-white">
        <table className="w-full min-w-[36rem] text-left text-sm">
          <caption className="sr-only">Pinned standards</caption>
          <thead className="border-b border-stone-200 bg-stone-50 text-stone-600">
            <tr>
              <th className="px-4 py-2 font-medium">Source</th>
              <th className="px-4 py-2 font-medium">Version</th>
              <th className="px-4 py-2 font-medium">Status</th>
              <th className="px-4 py-2 font-medium">Role</th>
            </tr>
          </thead>
          <tbody>
            {pins.map((p) => (
              <tr key={p.id} className="border-b border-stone-100 last:border-0">
                <td className="px-4 py-3">
                  <a
                    href={p.url}
                    className="font-medium text-blue-900 underline-offset-2 hover:underline"
                    rel="noreferrer"
                    target="_blank"
                  >
                    {p.source}
                  </a>
                  {p.notes ? (
                    <p className="mt-1 text-xs leading-relaxed text-stone-600">{p.notes}</p>
                  ) : null}
                </td>
                <td className="px-4 py-3 whitespace-nowrap text-stone-800">{p.version}</td>
                <td className="px-4 py-3 whitespace-nowrap text-stone-800">{p.status}</td>
                <td className="px-4 py-3 text-stone-700">{p.role || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <h2 className="mt-10 mb-3 text-xl font-semibold">Where modules cite them</h2>
      <div className="overflow-x-auto rounded-xl border border-stone-200 bg-white">
        <table className="w-full min-w-[28rem] text-left text-sm">
          <caption className="sr-only">Module citations</caption>
          <thead className="border-b border-stone-200 bg-stone-50 text-stone-600">
            <tr>
              <th className="px-4 py-2 font-medium">Module</th>
              <th className="px-4 py-2 font-medium">Pins</th>
            </tr>
          </thead>
          <tbody>
            {modules.map((m) => (
              <tr key={m.id} className="border-b border-stone-100 last:border-0">
                <td className="px-4 py-3 align-top whitespace-nowrap">
                  <Link
                    href={moduleHref(m.id)}
                    className="font-medium text-blue-900 underline-offset-2 hover:underline"
                  >
                    {m.id}
                  </Link>
                </td>
                <td className="px-4 py-3 leading-relaxed text-stone-700">
                  {m.standardsRefs
                    .map((s) => `${s.source} ${s.version} (${s.status})`)
                    .join(" · ")}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </PageShell>
  );
}
