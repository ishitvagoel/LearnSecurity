const TERMS: { term: string; def: string }[] = [
  {
    term: "Invariant",
    def: "A system-specific sentence that must remain true under named attacker capabilities and trust assumptions. If a second person cannot write a failing test, it is still a slogan.",
  },
  {
    term: "Mechanism",
    def: "A control or product (TLS, JWT, bcrypt, a scanner, a cloud checkbox) that may or may not restore an invariant.",
  },
  {
    term: "Complete mediation",
    def: "Every security-relevant action is checked on every path, including workers, exports, and retries. A skipped indirect path is a failed property.",
  },
  {
    term: "Fail-safe defaults",
    def: "Unknown, expired, or failed policy evaluation denies. Availability pressure does not authorize fail-open.",
  },
  {
    term: "TCB (trusted computing base)",
    def: "The parts of the system you are willing to trust for a given invariant. The Next.js bundle and a hostile APK are usually outside it.",
  },
  {
    term: "Confused deputy",
    def: "A privileged component that acts on a caller-supplied identifier (tenant id, URL, object id) without checking the caller’s authority.",
  },
  {
    term: "Residual risk",
    def: "What remains if the primary control fails. Name detection, recovery, and who is still harmed. Do not hide it behind a compliance checkbox.",
  },
  {
    term: "Authorized lab",
    def: "A local course app, official training target, published challenge terms, or a system with written authorization. This website is none of those execution environments.",
  },
  {
    term: "SecureCollab",
    def: "The course through-line: a small multi-tenant notes product that grows files, sharing, workers, and mobile. Catalogue properties against it, not against a generic CIA triad.",
  },
];

export default function GlossaryPage() {
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Glossary</h1>
      <p className="mb-6 max-w-prose leading-relaxed">
        These are working definitions for this course. Prefer a testable sentence
        about SecureCollab over a memorized triad.
      </p>
      <dl>
        {TERMS.map((t) => (
          <div key={t.term} className="mb-5 max-w-prose">
            <dt className="font-semibold">{t.term}</dt>
            <dd className="leading-relaxed">{t.def}</dd>
          </div>
        ))}
      </dl>
    </article>
  );
}
