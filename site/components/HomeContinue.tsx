"use client";

import type { ReactElement } from "react";
import Link from "next/link";
import { useSyncExternalStore } from "react";
import { useVisitedModuleIds } from "@/components/ProgressToggle";
import { TOPIC_TITLE } from "@/lib/catalog";

type LastActivity = { href: string; title: string };

function isAllowedActivityHref(href: string): boolean {
  return ["/learn/", "/labs/", "/assess/", "/bridges/"].some((prefix) => href.startsWith(prefix));
}

let cachedActivityRaw: string | null | undefined;
let cachedActivity: LastActivity | null = null;

function readActivity(): LastActivity | null {
  if (typeof window === "undefined") {
    return null;
  }
  let raw: string | null;
  try {
    raw = localStorage.getItem("learnsecurity-last-activity-v1");
  } catch {
    return null;
  }
  if (raw === cachedActivityRaw) {
    return cachedActivity;
  }
  cachedActivityRaw = raw;
  cachedActivity = null;
  try {
    const parsed: unknown = JSON.parse(raw || "null");
    if (
      parsed &&
      typeof parsed === "object" &&
      "href" in parsed &&
      typeof parsed.href === "string" &&
      isAllowedActivityHref(parsed.href) &&
      "title" in parsed &&
      typeof parsed.title === "string"
    ) {
      cachedActivity = { href: parsed.href, title: parsed.title };
    }
  } catch {
    cachedActivity = null;
  }
  return cachedActivity;
}

function subscribeActivity(listener: () => void): () => void {
  window.addEventListener("storage", listener);
  return () => window.removeEventListener("storage", listener);
}

export function HomeContinue(): ReactElement | null {
  const ids = useVisitedModuleIds();
  const activity = useSyncExternalStore(subscribeActivity, readActivity, () => null);

  const last = ids[ids.length - 1];
  if (!activity && !last) {
    return null;
  }
  const href = activity?.href || `/learn/${encodeURIComponent(last || "")}/`;
  const title = activity?.title || TOPIC_TITLE[last || ""] || last;
  return (
    <p className="mt-6 max-w-xl rounded-2xl border border-line bg-paper/80 px-4 py-3 text-sm text-muted">
      {activity ? "Continue from your last activity:" : `You left off after ${ids.length} topic${ids.length === 1 ? "" : "s"}. Last one:`}{" "}
      <Link
        href={href}
        className="font-medium text-forest-accent underline underline-offset-2"
      >
        {title}
      </Link>
      .{" "}
      <Link href="/progress/" className="font-medium text-forest-accent underline underline-offset-2">
        See your progress
      </Link>
      .
    </p>
  );
}
