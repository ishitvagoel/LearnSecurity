export default function CheckpointsPage() {
  const gates = [
    "0 — orientation / authorized lab hygiene",
    "1 — Phase 1 invariants and authority language",
    "2 — Phase 2 mechanism literacy",
    "3 — threat model and architecture (transfer-required)",
    "4 — identity vertical (transfer-required)",
    "5 — data and crypto use",
    "6 — injection and abuse (transfer-required)",
    "7 — API / workers",
    "8 — mobile (optional until web/API milestone)",
    "9 — verification (transfer-required)",
    "10 — operate and supply chain (transfer-required)",
    "11 — capstone defense",
  ];
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Checkpoints (mastery gates)</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        Gates use four states: not-attempted, developing, competent,
        transfer-ready. There is no compensating average. This site does not
        grade you; rubrics live with each module. Keys are not published here.
      </p>
      <ol className="list-decimal pl-6">
        {gates.map((g) => (
          <li key={g} className="mb-1 max-w-prose">
            Gate {g}
          </li>
        ))}
      </ol>
    </article>
  );
}
