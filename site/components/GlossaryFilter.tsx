"use client";

import { useMemo, useState, type ReactElement } from "react";
import type { GlossaryTerm } from "@/lib/glossary";

export function GlossaryFilter({ terms }: { terms: GlossaryTerm[] }): ReactElement {
  const [query, setQuery] = useState("");

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) {
      return terms;
    }
    return terms.filter(
      (t) => t.term.toLowerCase().includes(q) || t.def.toLowerCase().includes(q),
    );
  }, [terms, query]);

  return (
    <div>
      <label className="mb-4 block">
        <span className="sr-only">Filter the word list</span>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder={`Filter ${terms.length} words…`}
          className="w-full rounded-xl border border-stone-200 bg-white px-4 py-2.5 text-sm text-ink outline-none placeholder:text-muted focus-visible:border-forest-accent"
        />
      </label>
      {filtered.length === 0 ? (
        <p className="rounded-xl border border-dashed border-stone-200 px-4 py-6 text-center text-sm text-muted">
          Nothing matched “{query}.”
        </p>
      ) : (
        <dl className="space-y-4">
          {filtered.map((t) => (
            <div
              key={t.term}
              className="rounded-xl border border-stone-200 bg-white px-4 py-3"
            >
              <dt className="font-semibold text-stone-900">{t.term}</dt>
              <dd className="mt-1 leading-relaxed text-stone-800">{t.def}</dd>
            </div>
          ))}
        </dl>
      )}
    </div>
  );
}
