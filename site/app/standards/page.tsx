import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";
import { pinStatusLabel } from "@/lib/catalog";
import { loadAllModules, loadPins, moduleHref } from "@/lib/loadCurriculum";

type Pin = {
  id: string;
  source: string;
  version: string;
  status: string;
  url: string;
};

export default function StandardsPage() {
  const raw = loadPins() as { pins?: Pin[] };
  const pins = raw.pins || [];
  const modules = loadAllModules();
  return (
    <PageShell>
      <PageHeader title="Industry lists">
        <p>
          These are the published lists and papers the course points at. A list
          of common bugs is a reminder after you have a rule — it is not the
          syllabus. A draft stays labeled as a draft.
        </p>
      </PageHeader>
      <h2 className="mb-3 text-xl font-semibold">What we point at</h2>
      <div className="overflow-x-auto rounded-xl border border-stone-200 bg-white">
        <table className="w-full min-w-[36rem] text-left text-sm">
          <caption className="sr-only">Industry lists and papers</caption>
          <thead className="border-b border-stone-200 bg-stone-50 text-stone-600">
            <tr>
              <th className="px-4 py-2 font-medium">Name</th>
              <th className="px-4 py-2 font-medium">Version</th>
              <th className="px-4 py-2 font-medium">Status</th>
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
                </td>
                <td className="px-4 py-3 whitespace-nowrap text-stone-800">{p.version}</td>
                <td className="px-4 py-3 whitespace-nowrap text-stone-800">
                  {pinStatusLabel(p.status)}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <h2 className="mt-10 mb-3 text-xl font-semibold">Where topics mention them</h2>
      <div className="overflow-x-auto rounded-xl border border-stone-200 bg-white">
        <table className="w-full min-w-[28rem] text-left text-sm">
          <caption className="sr-only">Topics and the lists they mention</caption>
          <thead className="border-b border-stone-200 bg-stone-50 text-stone-600">
            <tr>
              <th className="px-4 py-2 font-medium">Topic</th>
              <th className="px-4 py-2 font-medium">Lists</th>
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
                    .map((s) => `${s.source} ${s.version}`)
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
