import Link from "next/link";
import { CardLink, PageHeader, PageShell } from "@/components/ui";

export default function CapstonePage() {
  return (
    <PageShell width="narrow">
      <PageHeader title="Capstone 11 — SecureCollab">
        <p>
          The capstone is not a new feature demo. You show that the same
          invariants still hold when identity, data, APIs, workers, and time
          interact: a revoked share stays revoked; a worker is not a user
          session; deletion does not leave bodies in a side copy.
        </p>
        <p>
          Evidence is an architecture defense plus repaired findings. Product
          milestones M0–M5 in STATUS stay not-attempted until a real product tree
          exists. Completing lessons on this site is not that evidence.
        </p>
      </PageHeader>
      <ul className="grid gap-3 sm:grid-cols-2">
        <li>
          <CardLink href="/learn/11/" title="Module 11">
            Lessons for the capstone defense.
          </CardLink>
        </li>
        <li>
          <CardLink href="/labs/11/" title="Lab brief">
            Run the local capstone fixture from git, not from this origin.
          </CardLink>
        </li>
      </ul>
      <p className="mt-6 text-sm text-stone-600">
        Also see{" "}
        <Link href="/checkpoints/" className="text-blue-900 underline underline-offset-2">
          Gate 11
        </Link>
        .
      </p>
    </PageShell>
  );
}
