const TERMS: { term: string; def: string }[] = [
  {
    term: "Invariant",
    def: "A system-specific property that must remain true under stated attacker capabilities and trust assumptions.",
  },
  {
    term: "Mechanism",
    def: "A control or product (TLS, JWT, scanner) that may or may not restore an invariant.",
  },
  {
    term: "Complete mediation",
    def: "Every security-relevant action is checked; skipped indirect paths are failures.",
  },
  {
    term: "Fail-safe default",
    def: "Unknown or failed policy evaluation denies.",
  },
  {
    term: "Authorized lab",
    def: "Local course app, official training target, published challenge terms, or written authorization.",
  },
];

export default function GlossaryPage() {
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Glossary and mental models</h1>
      <dl>
        {TERMS.map((t) => (
          <div key={t.term} className="mb-4 max-w-prose">
            <dt className="font-semibold">{t.term}</dt>
            <dd>{t.def}</dd>
          </div>
        ))}
      </dl>
    </article>
  );
}
