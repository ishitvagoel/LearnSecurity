import { PageHeader, PageShell } from "@/components/ui";
import { GLOSSARY_TERMS } from "@/lib/glossary";

export default function GlossaryPage() {
  return (
    <PageShell width="narrow">
      <PageHeader title="Word list">
        <p>
          A few words this course uses a lot. Each one is named, then said in
          ordinary English. Prefer a sentence you can check about the notes app
          over a memorized slogan.
        </p>
      </PageHeader>
      <dl className="space-y-4">
        {GLOSSARY_TERMS.map((t) => (
          <div
            key={t.term}
            className="rounded-xl border border-stone-200 bg-white px-4 py-3"
          >
            <dt className="font-semibold text-stone-900">{t.term}</dt>
            <dd className="mt-1 leading-relaxed text-stone-800">{t.def}</dd>
          </div>
        ))}
      </dl>
    </PageShell>
  );
}
