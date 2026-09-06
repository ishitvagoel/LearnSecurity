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
  return <div className={`mx-auto w-full ${max} px-4 py-8 sm:py-10`}>{children}</div>;
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
    <header className="mb-8">
      {kicker ? (
        <p className="mb-2 text-sm font-medium uppercase tracking-wide text-stone-600">
          {kicker}
        </p>
      ) : null}
      <h1 className="text-3xl font-semibold tracking-tight text-stone-900 sm:text-4xl">
        {title}
      </h1>
      {children ? (
        <div className="mt-4 max-w-prose space-y-3 text-[1.05rem] leading-relaxed text-stone-800">
          {children}
        </div>
      ) : null}
    </header>
  );
}

export function SectionHeading({
  kicker,
  title,
  children,
}: {
  kicker?: string;
  title: string;
  children?: ReactNode;
}): ReactElement {
  return (
    <div className="mb-6 max-w-prose">
      {kicker ? (
        <p className="mb-2 text-sm font-medium uppercase tracking-wide text-stone-600">
          {kicker}
        </p>
      ) : null}
      <h2 className="text-2xl font-semibold tracking-tight text-stone-900">{title}</h2>
      {children ? (
        <div className="mt-3 space-y-3 leading-relaxed text-stone-700">{children}</div>
      ) : null}
    </div>
  );
}

export function Chip({ children }: { children: ReactNode }): ReactElement {
  return (
    <span className="inline-flex items-center rounded-full border border-stone-300 bg-white px-2.5 py-0.5 text-xs font-medium text-stone-800">
      {children}
    </span>
  );
}

export function ButtonLink({
  href,
  children,
  variant = "primary",
  onDark = false,
}: {
  href: string;
  children: ReactNode;
  variant?: "primary" | "secondary";
  onDark?: boolean;
}): ReactElement {
  const primary = onDark
    ? "bg-white text-stone-900 hover:bg-stone-100"
    : "bg-stone-900 text-white hover:bg-stone-800";
  const secondary = onDark
    ? "border border-stone-400 text-stone-50 hover:bg-stone-800"
    : "border border-stone-300 bg-white text-stone-900 hover:border-stone-500 hover:bg-stone-50";
  return (
    <Link
      href={href}
      className={`inline-flex items-center justify-center rounded-lg px-4 py-2.5 text-sm font-medium no-underline ${
        variant === "primary" ? primary : secondary
      }`}
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
      className="block h-full rounded-xl border border-stone-200 bg-white p-4 text-stone-900 shadow-sm transition-colors hover:border-stone-400 hover:bg-stone-50"
    >
      {kicker ? (
        <p className="mb-1 text-xs font-medium uppercase tracking-wide text-stone-600">
          {kicker}
        </p>
      ) : null}
      <p className="font-semibold text-blue-900">{title}</p>
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
    <Link href={href} className="text-blue-900 underline underline-offset-2">
      {children}
    </Link>
  );
}
