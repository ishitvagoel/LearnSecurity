import Link from "next/link";
import { notFound } from "next/navigation";
import { Markdown } from "@/lib/markdown";
import { loadAllModules, moduleHref } from "@/lib/loadCurriculum";
import { loadReferenceDoc, loadReferenceDocs } from "@/lib/referenceDocs";

 type Props = { params: Promise<{ slug: string }> };

export const dynamicParams = false;

export function generateStaticParams() {
  return loadReferenceDocs().map((doc) => ({ slug: doc.slug }));
}

export async function generateMetadata({ params }: Props) {
  const { slug } = await params;
  const doc = loadReferenceDoc(slug);
  return {
    title: doc ? `Notes app · ${doc.title}` : "Notes app reference",
    description: doc ? `SecureCollab design note: ${doc.title}.` : undefined,
  };
}

export default async function ReferenceDocPage({ params }: Props) {
  const { slug } = await params;
  const doc = loadReferenceDoc(slug);
  if (!doc) {
    notFound();
  }
  const moduleIds = new Set(loadAllModules().map((module) => module.id));
  return (
    <article className="mx-auto w-full max-w-3xl px-4 py-10 sm:py-12">
      <p className="mb-4 text-sm text-muted">
        <Link href="/reference/" className="text-link underline-offset-2 hover:underline">
          The notes app
        </Link>
        {" · "}
        Design note
        {doc.moduleId && moduleIds.has(doc.moduleId) ? (
          <>
            {" · "}
            <Link href={moduleHref(doc.moduleId)} className="text-link underline-offset-2 hover:underline">
              Topic {doc.moduleId}
            </Link>
          </>
        ) : null}
      </p>
      <header className="mb-8">
        <p className="mb-3 text-sm font-medium text-forest-accent">SecureCollab design note</p>
        <h1 className="font-serif text-3xl font-semibold tracking-tight text-ink sm:text-4xl">{doc.title}</h1>
        <p className="mt-3 text-sm text-muted">This is a reference artifact. It records design decisions and limits; it does not replace the lesson or claim production assurance.</p>
      </header>
      <div className="curriculum-prose rounded-2xl border border-line bg-paper p-5 sm:p-7">
        <Markdown source={doc.body.replace(/^# [^\n]*\n+/, "")} />
      </div>
    </article>
  );
}
