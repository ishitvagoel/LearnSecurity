import Link from "next/link";
import { PageHeader, PageShell } from "@/components/ui";
import { bridgeHref, loadBridges } from "@/lib/bridges";

export const metadata = {
  title: "Tooling bridges",
  description: "Short local tasks that repair entry-skill gaps without granting security clearance.",
};

export default function BridgesPage() {
  const bridges = loadBridges();
  return (
    <PageShell width="narrow">
      <PageHeader kicker="Before the first security gate" title="Tooling bridges">
        <p>
          These small tasks check whether you can use the tools the course
          assumes. Completing one removes a tooling gap; it does not pass a
          security gate or replace the required security evidence.
        </p>
      </PageHeader>
      <ul className="grid gap-3 sm:grid-cols-2">
        {bridges.map((bridge) => (
          <li key={bridge.id} className="rounded-2xl border border-line bg-paper p-5">
            <p className="font-mono text-xs text-muted">{bridge.capability}</p>
            <h2 className="mt-1 text-lg font-semibold text-ink">
              <Link href={bridgeHref(bridge.id)} className="text-link underline-offset-2 hover:underline">
                {bridge.title}
              </Link>
            </h2>
            <p className="mt-2 text-sm leading-relaxed text-muted">{bridge.objective}</p>
          </li>
        ))}
      </ul>
    </PageShell>
  );
}
