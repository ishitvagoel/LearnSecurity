import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";

export default function ReferencePage() {
  return (
    <PageShell width="narrow">
      <PageHeader title="SecureCollab reference">
        <p>
          SecureCollab is a small collaboration product used as the course
          spine: organizations (tenants), members, notes, later files and
          shares. It is specified in the repository; this website does not host a
          live instance.
        </p>
        <p>
          When you add a channel (worker, CSV export, offline cache, webhook),
          rewrite the affected invariant. Do not answer “add encryption.” Name
          who can read or change which object, on which path, after how much
          time.
        </p>
        <p>
          Design stubs live in{" "}
          <code className="rounded bg-stone-200 px-1">content/reference/securecollab/</code>
          . Spiral revisits are recorded in{" "}
          <code className="rounded bg-stone-200 px-1">content/progress/STATUS.yaml</code>
          . Start from{" "}
          <Link href="/learn/1.1/" className="text-blue-900 underline underline-offset-2">
            1.1 — invariants
          </Link>
          .
        </p>
      </PageHeader>
    </PageShell>
  );
}
