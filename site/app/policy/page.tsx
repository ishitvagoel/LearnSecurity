import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";

export default function PolicyPage() {
  return (
    <PageShell width="narrow">
      <PageHeader title="Rules for practice">
        <p>
          This course teaches you to find a problem, understand why it happened,
          and repair it. It does not teach you to attack systems you do not own.
          This website is for reading. It never runs the broken practice apps.
        </p>
      </PageHeader>
      <div className="grid gap-4 sm:grid-cols-2">
        <section className="rounded-xl border border-emerald-200 bg-emerald-50 px-4 py-4">
          <h2 className="mb-3 text-lg font-semibold">You may</h2>
          <ul className="list-disc space-y-2 pl-5 leading-relaxed">
            <li>Study lessons on this website.</li>
            <li>
              Run the checks in{" "}
              <code className="rounded bg-white/80 px-1">labs/</code> on your own
              copy of this repository.
            </li>
            <li>
              Use official training apps (for example OWASP Juice Shop) the way
              their own rules allow.
            </li>
            <li>
              Test systems you own, or systems where you have written permission
              and a clear limit on what you may touch.
            </li>
          </ul>
        </section>
        <section className="rounded-xl border border-rose-200 bg-rose-50 px-4 py-4">
          <h2 className="mb-3 text-lg font-semibold">You must not</h2>
          <ul className="list-disc space-y-2 pl-5 leading-relaxed">
            <li>Practice on public websites, other people’s apps, or live production systems.</li>
            <li>Copy ready-made attack recipes into notes or pull requests.</li>
            <li>Upload real people’s data, patient records, or live production secrets as “evidence.”</li>
            <li>Publish answer keys on this website if you find them.</li>
          </ul>
        </section>
      </div>
      <p className="mt-6 max-w-prose leading-relaxed text-stone-800">
        Practice data is fake. Practice secrets are throwaway. Reset from git
        after each practice. Questions about what is allowed: start from{" "}
        <Link href="/labs/" className="text-blue-900 underline underline-offset-2">
          Practice
        </Link>
        .
      </p>
    </PageShell>
  );
}
