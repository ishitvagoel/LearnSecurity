import Link from "next/link";
import { CardLink, PageHeader, PageShell } from "@/components/ui";

export default function CapstonePage() {
  return (
    <PageShell width="narrow">
      <PageHeader title="Final project">
        <p>
          This is not a new feature demo. You show that the notes app still
          keeps its promises when logins, data, APIs, background jobs, and time
          all run together: a revoked share stays revoked; a background job is
          not a logged-in user; deleting a note does not leave the text sitting
          in a leftover copy.
        </p>
        <p>
          What counts is a design defense plus the bugs you found and repaired.
          Finishing lessons on this site is not that evidence. This site does
          not grade you.
        </p>
      </PageHeader>
      <ul className="grid gap-3 sm:grid-cols-2">
        <li>
          <CardLink href="/learn/11/" title="Lessons">
            The pages for the final project.
          </CardLink>
        </li>
        <li>
          <CardLink href="/labs/11/" title="Practice note">
            Run the final-project files from git, on your computer.
          </CardLink>
        </li>
      </ul>
      <p className="mt-6 text-sm text-stone-600">
        Also see{" "}
        <Link href="/checkpoints/" className="text-blue-900 underline underline-offset-2">
          check-in 11
        </Link>
        .
      </p>
    </PageShell>
  );
}
