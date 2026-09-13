import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";
import { loadReferenceDocs } from "@/lib/referenceDocs";

export const metadata = {
  title: "The notes app",
  description:
    "SecureCollab, the small notes app this course follows and extends — its design decisions, and which lesson each one backs.",
};

export default function ReferencePage() {
  const docs = loadReferenceDocs();
  const moduleIds = new Set(loadAllModules().map((m) => m.id));

  return (
    <PageShell width="narrow">
      <PageHeader title="The notes app">
        <p>
          The course follows one small example: a notes app used by more than
          one company. Teams, members, notes — later files and sharing. A
          short design note backs each stage; the table below lists them.
        </p>
        <p>
          When you add a new path (a background job, a spreadsheet export, a
          phone cache, a webhook), rewrite the rules that path can break. Do
          not stop at “add encryption.” Say who can read or change which note,
          on which path, after how much time.
        </p>
      </PageHeader>
      <h2 className="mb-3 text-xl font-semibold">Design decisions, by topic</h2>
      <p className="mb-4 text-sm leading-relaxed text-stone-700">
        Each row is a short internal design note: the specific rule enforced
        at that stage of the notes app, and the practice data used to test it.
        Read a note alongside its linked lesson, not instead of it — these are
        authoring notes, not lesson pages.
      </p>
      <div className="overflow-x-auto rounded-xl border border-stone-200 bg-white">
        <table className="w-full min-w-[34rem] text-left text-sm">
          <caption className="sr-only">
            Notes-app design decisions and the topics they back
          </caption>
          <thead className="border-b border-stone-200 bg-stone-50 text-stone-600">
            <tr>
              <th className="px-4 py-2 font-medium">Decision</th>
              <th className="px-4 py-2 font-medium">Backs topic</th>
              <th className="px-4 py-2 font-medium">File</th>
            </tr>
          </thead>
          <tbody>
            {docs.map((doc) => (
              <tr key={doc.slug} className="border-b border-stone-100 last:border-0">
                <td className="px-4 py-3 align-top text-stone-800">{doc.title}</td>
                <td className="px-4 py-3 align-top whitespace-nowrap">
                  {doc.moduleId && moduleIds.has(doc.moduleId) ? (
                    <Link
                      href={moduleHref(doc.moduleId)}
                      className="font-medium text-blue-900 underline-offset-2 hover:underline"
                    >
                      {doc.moduleId}
                    </Link>
                  ) : (
                    <span className="text-stone-500">—</span>
                  )}
                </td>
                <td className="px-4 py-3 align-top">
                  <code className="rounded bg-stone-100 px-1 text-xs">{doc.relativePath}</code>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </PageShell>
  );
}
