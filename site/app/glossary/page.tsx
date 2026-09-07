import type { Metadata } from "next";
import { PageHeader, PageShell } from "@/components/ui";

export const metadata: Metadata = { title: "Word list" };

const TERMS: { term: string; def: string }[] = [
  {
    term: "Rule (invariant)",
    def: "A promise the software must keep, written so another person could check it. Example: “People in company A cannot read company B’s notes.” If you cannot write a test for it, it is still a slogan.",
  },
  {
    term: "Tool (mechanism)",
    def: "A setting or library — encryption, a login package, a scanner, a cloud checkbox. These may help. They are not the same as the rule you are trying to keep.",
  },
  {
    term: "Check every path (complete mediation)",
    def: "Every path gets the same check: the website, the export, the retry, the background job. A skipped path means the rule is already broken.",
  },
  {
    term: "Fail closed (fail-safe defaults)",
    def: "If the app is unsure — expired login, missing setting, failed check — it says no. Being busy is not a reason to skip the check.",
  },
  {
    term: "What you trust (trusted computing base)",
    def: "The pieces of the system you are betting on for a given rule. A page in the browser, and a phone app someone can copy, are usually not on that list.",
  },
  {
    term: "Confused deputy",
    def: "A powerful part of the app that does what a caller asks (open this note, fetch this URL) without checking whether that caller is allowed to.",
  },
  {
    term: "What can still go wrong (residual risk)",
    def: "What still goes wrong if the main protection fails. Say how you would notice, how you would recover, and who still gets hurt. A checkbox on a form is not that sentence.",
  },
  {
    term: "Authorized lab",
    def: "Practice you are allowed to run: a local course app, an official training target, a challenge whose published rules allow it, or a system with written permission. This website is none of those. It does not run the broken apps.",
  },
  {
    term: "The notes app (SecureCollab)",
    def: "The small notes app the course keeps extending: teams, members, notes, later files and sharing. Write rules about this app, not about a vague slogan like “keep it confidential.”",
  },
];

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
        {TERMS.map((t) => (
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
