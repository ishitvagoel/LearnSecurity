"use client";

import type { ReactElement } from "react";
import Link from "next/link";
import { useVisitedModuleIds } from "@/components/ProgressToggle";

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
    <p className="mt-6 text-sm text-stone-300">
      {ids.length} module{ids.length === 1 ? "" : "s"} marked visited on this device. Last
      marked:{" "}
      <Link
        href={`/learn/${encodeURIComponent(last)}/`}
        className="font-medium text-white underline underline-offset-2"
      >
        {last}
      </Link>
      .
    </p>
  );
}
