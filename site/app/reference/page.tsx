import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";

export default function ReferencePage() {
  return (
    <PageShell width="narrow">
      <PageHeader title="The notes app">
        <p>
          The course follows one small example: a notes app used by more than
          one company. Teams, members, notes — later files and sharing. The
          design lives in the repository. This website does not host a live
          copy.
        </p>
        <p>
          When you add a new path (a background job, a spreadsheet export, a
          phone cache, a webhook), rewrite the rules that path can break. Do
          not stop at “add encryption.” Say who can read or change which note,
          on which path, after how much time.
        </p>
        <p>
          Design notes live in the course repository, in the notes-app folder.
          Start from{" "}
          <Link href="/learn/1.1/" className="text-blue-900 underline underline-offset-2">
            what “secure” means here
          </Link>
          .
        </p>
      </PageHeader>
    </PageShell>
  );
}
