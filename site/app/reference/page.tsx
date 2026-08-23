export default function ReferencePage() {
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">SecureCollab reference</h1>
      <p className="mb-4 max-w-prose leading-relaxed">
        SecureCollab is the evolving reference system (blueprint §9). This site
        does not host a production app. Design stubs live in the repository
        under <code>content/reference/securecollab/</code>.
      </p>
      <p className="max-w-prose leading-relaxed">
        Spiral revisits are recorded in <code>content/progress/STATUS.yaml</code>{" "}
        (<code>spiral_deltas</code>). Product milestones M0–M5 stay
        not-attempted until a real product tree exists.
      </p>
    </article>
  );
}
