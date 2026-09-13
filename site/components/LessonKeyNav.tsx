"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { isTypingTarget } from "@/lib/dom";

export function LessonKeyNav({
  prevHref,
  nextHref,
  currentHref,
  currentTitle,
}: {
  prevHref?: string;
  nextHref?: string;
  currentHref?: string;
  currentTitle?: string;
}): null {
  const router = useRouter();

  useEffect(() => {
    if (currentHref) {
      try {
        localStorage.setItem(
          "learnsecurity-last-activity-v1",
          JSON.stringify({ href: currentHref, title: currentTitle || "last lesson" }),
        );
      } catch {
        // Progress remains usable when browser storage is unavailable.
      }
    }
    const onKey = (event: KeyboardEvent): void => {
      if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) {
        return;
      }
      if (isTypingTarget(event.target)) {
        return;
      }
      if (event.key === "ArrowLeft" && prevHref) {
        router.push(prevHref);
      } else if (event.key === "ArrowRight" && nextHref) {
        router.push(nextHref);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [currentHref, currentTitle, prevHref, nextHref, router]);

  return null;
}
