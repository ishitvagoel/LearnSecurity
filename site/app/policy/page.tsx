export default function PolicyPage() {
  return (
    <article>
      <h1 className="mb-4 text-3xl font-semibold">Safe-use policy</h1>
      <ul className="list-disc pl-6 leading-relaxed">
        <li>
          Attack only local course applications, official vuln training projects,
          challenges whose terms authorize the action, or systems with written
          authorization.
        </li>
        <li>Do not target public, third-party, or production systems from this course.</li>
        <li>This origin does not run vulnerable lab servers or paste weaponized payloads.</li>
        <li>Lab data is synthetic. Secrets are disposable.</li>
        <li>Do not upload real PII or production secrets as “evidence.”</li>
      </ul>
    </article>
  );
}
