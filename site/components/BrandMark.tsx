import type { ReactElement } from "react";

export function BrandMark({ className = "h-8 w-8" }: { className?: string }): ReactElement {
  return (
    <svg
      className={className}
      viewBox="0 0 32 32"
      aria-hidden="true"
      focusable="false"
    >
      <rect width="32" height="32" rx="8" fill="#1f4d45" />
      <path d="M11 8.5h3.2V20.2H22V23.5H11V8.5z" fill="#fbf7f0" />
    </svg>
  );
}
