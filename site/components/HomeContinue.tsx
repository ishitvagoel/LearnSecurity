"use client";

import type { ReactElement } from "react";
import Link from "next/link";
import { useVisitedModuleIds } from "@/components/ProgressToggle";
import { TOPIC_TITLE } from "@/lib/catalog";

export function HomeContinue(): ReactElement | null {
  const ids = useVisitedModuleIds();
  if (ids.length === 0) {
    return null;
  }
  const last = ids[ids.length - 1];
  if (!last) {
    return null;
  }
  return (
    <p className="mt-6 max-w-xl rounded-2xl border border-line bg-paper/80 px-4 py-3 text-sm text-stone-700">
      You left off after {ids.length} topic{ids.length === 1 ? "" : "s"} on this
      computer. Last one:{" "}
      <Link
        href={`/learn/${encodeURIComponent(last)}/`}
        className="font-medium text-forest underline underline-offset-2"
      >
        {TOPIC_TITLE[last] || last}
      </Link>
      .
    </p>
  );
}
