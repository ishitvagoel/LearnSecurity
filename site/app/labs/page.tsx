import Link from "next/link";
import { loadAllModules } from "@/lib/loadCurriculum";

export default function LabsIndexPage() {
  const withLabs = loadAllModules().filter((m) => m.labSpec);
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Labs</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        Executable vulnerable fixtures live in the git repository under{" "}
        <code>labs/</code>. They are <strong>not</strong> served or executed from
        this website origin. Clone the repo, run pytest locally, reset from git.
      </p>
      <ul className="list-disc pl-6">
        {withLabs.map((m) => (
          <li key={m.id} className="mb-1">
            <Link
              href={`/labs/${encodeURIComponent(m.id)}/`}
              className="text-blue-900 underline"
            >
              {m.id} — {m.labSpec?.slug || "lab"}
            </Link>
          </li>
        ))}
      </ul>
    </article>
  );
}
