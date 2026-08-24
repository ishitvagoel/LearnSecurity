import Link from "next/link";

export default function ReferencePage() {
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">SecureCollab reference</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        SecureCollab is a small collaboration product used as the course
        spine: organizations (tenants), members, notes, later files and
        shares. It is specified in the repository; this website does not host a
        live instance.
      </p>
      <p className="mb-4 max-w-prose leading-relaxed">
        When you add a channel (worker, CSV export, offline cache, webhook),
        rewrite the affected invariant. Do not answer “add encryption.” Name
        who can read or change which object, on which path, after how much
        time.
      </p>
      <p className="max-w-prose leading-relaxed">
        Design stubs: <code>content/reference/securecollab/</code>. Spiral
        revisits are recorded in <code>content/progress/STATUS.yaml</code>. See
        also{" "}
        <Link href="/learn/1.1/" className="text-blue-900 underline">
          1.1 — invariants
        </Link>
        .
      </p>
    </article>
  );
}
