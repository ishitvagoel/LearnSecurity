import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";

export default function NotFound() {
  return (
    <PageShell width="narrow">
      <PageHeader title="Page not found">
        <p>
          That URL is not in the published curriculum map. Try the{" "}
          <Link href="/learn/" className="text-blue-900 underline underline-offset-2">
            module list
          </Link>{" "}
          or the{" "}
          <Link href="/" className="text-blue-900 underline underline-offset-2">
            home page
          </Link>
          .
        </p>
      </PageHeader>
    </PageShell>
  );
}
