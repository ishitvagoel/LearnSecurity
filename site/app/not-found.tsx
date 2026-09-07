import type { Metadata } from "next";
import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";

export const metadata: Metadata = { title: "Page not found" };

export default function NotFound() {
  return (
    <PageShell width="narrow">
      <PageHeader title="Page not found">
        <p>
          That address is not on this site. Try the{" "}
          <Link href="/learn/" className="text-blue-900 underline underline-offset-2">
            lesson list
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
