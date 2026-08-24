import Link from "next/link";

export default function NotFound() {
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Page not found</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        That URL is not in the published curriculum map. Try the{" "}
        <Link href="/learn/" className="text-blue-900 underline">
          module list
        </Link>{" "}
        or the{" "}
        <Link href="/" className="text-blue-900 underline">
          home page
        </Link>
        .
      </p>
    </article>
  );
}
