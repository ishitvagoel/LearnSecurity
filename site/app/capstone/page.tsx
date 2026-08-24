import Link from "next/link";

export default function CapstonePage() {
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Capstone 11 — SecureCollab</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        The capstone is not a new feature demo. You show that the same
        invariants still hold when identity, data, APIs, workers, and time
        interact: a revoked share stays revoked; a worker is not a user
        session; deletion does not leave bodies in a side copy.
      </p>
      <p className="mb-4 max-w-prose leading-relaxed">
        Evidence is an architecture defense plus repaired findings. Product
        milestones M0–M5 in STATUS stay not-attempted until a real product tree
        exists. Completing lessons on this site is not that evidence.
      </p>
      <p className="max-w-prose leading-relaxed">
        Start at{" "}
        <Link href="/learn/11/" className="text-blue-900 underline">
          module 11
        </Link>
        . Run the local capstone fixture from the{" "}
        <Link href="/labs/11/" className="text-blue-900 underline">
          lab brief
        </Link>
        .
      </p>
    </article>
  );
}
