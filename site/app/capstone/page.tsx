import Link from "next/link";

export default function CapstonePage() {
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Capstone 11 — SecureCollab</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        Integrate the seven-step loop across identity, data, API, verification,
        and operations. Evidence is an architecture defense plus repaired
        findings—not a feature demo.
      </p>
      <p className="max-w-prose leading-relaxed">
        Module page:{" "}
        <Link href="/learn/11/" className="text-blue-900 underline">
          11 — Integrating capstone
        </Link>
        . Milestones M0–M5 in STATUS remain not-attempted until a product tree
        exists.
      </p>
    </article>
  );
}
