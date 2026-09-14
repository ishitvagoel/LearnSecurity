"use client";

import { useEffect } from "react";

const KEY = "learnsecurity-last-activity-v1";

export function LastActivityMarker({ href, title }: { href: string; title: string }): null {
  useEffect(() => {
    try {
      window.localStorage.setItem(KEY, JSON.stringify({ href, title }));
      // The native storage event only fires in other tabs.
      window.dispatchEvent(new Event("storage"));
    } catch {
      // The page remains usable when browser storage is unavailable.
    }
  }, [href, title]);

  return null;
}
