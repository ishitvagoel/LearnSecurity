import type { ReactElement, ReactNode } from "react";
import Link from "next/link";

export function PageShell({
  children,
  width = "default",
}: {
  children: ReactNode;
  width?: "narrow" | "default" | "wide";
}): ReactElement {
  const max =
    width === "narrow"
      ? "max-w-2xl"
      : width === "wide"
        ? "max-w-[90rem]"
        : "max-w-5xl";
  return <div className={`mx-auto w-full ${max} px-4 py-10 sm:py-12`}>{children}</div>;
}

export function PageHeader({
  kicker,
  title,
  children,
}: {
  kicker?: string;
  title: string;
  children?: ReactNode;
}): ReactElement {
  return (
    <header className="mb-10">
      {kicker ? (
        <p className="mb-3 text-sm font-medium text-forest">{kicker}</p>
      ) : null}
      <h1 className="font-serif text-3xl font-semibold tracking-tight text-ink sm:text-4xl">
        {title}
      </h1>
      {children ? (
        <div className="mt-4 max-w-prose space-y-3 text-[1.05rem] leading-relaxed text-stone-700">
          {children}
        </div>
      ) : null}
    </header>
  );
}

export function Chip({ children }: { children: ReactNode }): ReactElement {
  return (
    <span className="inline-flex items-center rounded-full border border-line bg-paper px-2.5 py-0.5 text-xs font-medium text-stone-800">
      {children}
    </span>
  );
}

export function ButtonLink({
  href,
  children,
  variant = "primary",
  className = "",
}: {
  href: string;
  children: ReactNode;
  variant?: "primary" | "secondary" | "inverse";
  className?: string;
}): ReactElement {
  const styles =
    variant === "primary"
      ? "bg-forest text-paper hover:bg-forest-hover"
      : variant === "inverse"
        ? "bg-paper text-forest hover:bg-white"
        : "border border-stone-400 bg-paper text-ink hover:border-forest hover:bg-white";
  return (
    <Link
      href={href}
      className={`inline-flex items-center justify-center rounded-full px-5 py-2.5 text-sm font-medium no-underline transition-colors ${styles} ${className}`}
    >
      {children}
    </Link>
  );
}

export function CardLink({
  href,
  title,
  children,
  kicker,
}: {
  href: string;
  title: string;
  children?: ReactNode;
  kicker?: string;
}): ReactElement {
  return (
    <Link
      href={href}
      className="block h-full rounded-2xl border border-line bg-paper p-5 text-ink shadow-sm transition hover:-translate-y-0.5 hover:border-forest/40 hover:shadow-md"
    >
      {kicker ? (
        <p className="mb-1 text-xs font-medium text-forest">{kicker}</p>
      ) : null}
      <p className="font-semibold text-ink">{title}</p>
      {children ? (
        <div className="mt-2 text-sm leading-relaxed text-stone-700">{children}</div>
      ) : null}
    </Link>
  );
}

export function ProseLink({
  href,
  children,
}: {
  href: string;
  children: ReactNode;
}): ReactElement {
  return (
    <Link href={href} className="text-link underline underline-offset-2">
      {children}
    </Link>
  );
}
