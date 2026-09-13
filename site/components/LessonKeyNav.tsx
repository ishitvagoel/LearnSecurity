"use client";

import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { isTypingTarget } from "@/lib/dom";

export function LessonKeyNav({
  prevHref,
  nextHref,
}: {
  prevHref?: string;
  nextHref?: string;
}): null {
  const router = useRouter();

  useEffect(() => {
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
  }, [prevHref, nextHref, router]);

  return null;
}
