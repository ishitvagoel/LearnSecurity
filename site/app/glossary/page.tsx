import { GlossaryFilter } from "@/components/GlossaryFilter";
import { PageHeader, PageShell } from "@/components/ui";
import { GLOSSARY_TERMS } from "@/lib/glossary";

export default function GlossaryPage() {
  return (
    <PageShell width="narrow">
      <PageHeader title="Word list">
        <p>
          A few words this course uses a lot, in ordinary English, listed
          alphabetically. Prefer a sentence you can check about the notes app
          over a memorized slogan.
        </p>
      </PageHeader>
      <GlossaryFilter terms={GLOSSARY_TERMS} />
    </PageShell>
  );
}
