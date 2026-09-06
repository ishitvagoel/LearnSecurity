import { HomeContinue } from "@/components/HomeContinue";
import { ButtonLink } from "@/components/ui";
import { loadAllModules } from "@/lib/loadCurriculum";

const STEPS = [
  {
    title: "Say what must stay true",
    body: "Write one clear rule for the software — something another person could check.",
  },
  {
    title: "Map who can do what",
    body: "Name the people, the data, and the paths in. Assume the browser and the phone app can lie.",
  },
  {
    title: "Watch it fail — on your computer",
    body: "A short practice file shows the rule breaking. You do not practice on live websites.",
  },
  {
    title: "Fix the actual cause",
    body: "Change the design so the rule holds, not just a setting or a scanner warning.",
  },
  {
    title: "Prove the fix",
    body: "A test should fail on the broken file and pass on the repaired one.",
  },
  {
    title: "Plan for when it still goes wrong",
    body: "Notice it, recover, and say what risk is left. Hiding leftover risk is not the same as removing it.",
  },
  {
    title: "Use the same idea somewhere new",
    body: "If the channel changes — a file export, a background job, a phone — the rule should still make sense.",
  },
] as const;

export default function HomePage() {
  const topicCount = loadAllModules().length;

  return (
    <div>
      <section className="relative overflow-hidden">
        <div
          className="pointer-events-none absolute inset-0 opacity-70"
          aria-hidden="true"
          style={{
            background:
              "radial-gradient(900px 420px at 10% -10%, #dce8e4 0%, transparent 60%), radial-gradient(700px 380px at 100% 0%, #efe4d2 0%, transparent 55%)",
          }}
        />
        <div className="relative mx-auto grid max-w-6xl gap-10 px-4 py-14 sm:py-20 lg:grid-cols-[minmax(0,1.15fr)_minmax(16rem,0.85fr)] lg:items-center">
          <div>
            <p className="text-sm font-medium text-forest">A free course for people who build software</p>
            <h1 className="mt-3 max-w-3xl font-serif text-4xl font-semibold tracking-tight text-ink sm:text-5xl sm:leading-[1.12]">
              Learn to build software that stays safe when someone tries to break it
            </h1>
            <p className="mt-5 max-w-xl text-lg leading-relaxed text-stone-700">
              LearnSecurity is a free course you read in the browser. You learn
              how to write a rule the software must keep, watch that rule fail in
              a practice lab on your own computer, then repair it. This is not a
              list of tools to memorize, and it is not a website for attacking
              live apps.
            </p>
            <div className="mt-8 flex flex-col gap-3 sm:flex-row">
              <ButtonLink href="/learn/0.1/" className="w-full sm:w-auto">
                Start with the orientation
              </ButtonLink>
              <ButtonLink href="/roadmap/" variant="secondary" className="w-full sm:w-auto">
                See what you will study
              </ButtonLink>
            </div>
            <HomeContinue />
          </div>
          <aside className="rounded-3xl border border-line bg-paper p-6 shadow-sm">
            <p className="text-sm font-medium text-forest">What this website is</p>
            <ul className="mt-4 space-y-4 text-sm leading-relaxed text-stone-700">
              <li>
                <strong className="block text-ink">The classroom</strong>
                Lessons and diagrams you can read in the browser.
              </li>
              <li>
                <strong className="block text-ink">The map</strong>
                A study order so you are not guessing what comes next.
              </li>
              <li>
                <strong className="block text-ink">Practice instructions</strong>
                When it is time to try something, you clone the course files and
                run them locally. This site never runs the broken apps.
              </li>
            </ul>
            <p className="mt-5 text-xs leading-relaxed text-muted">
              {topicCount} topics. No account. Progress stays in this browser.
            </p>
          </aside>
        </div>
      </section>

      <div className="mx-auto max-w-6xl space-y-20 px-4 py-6 pb-20">
        <section>
          <h2 className="font-serif text-3xl font-semibold tracking-tight text-ink">
            What to expect
          </h2>
          <p className="mt-3 max-w-2xl text-lg leading-relaxed text-stone-700">
            Each topic follows the same rhythm. You will get used to it. That is
            the point: security is a habit of checking a rule, not a list of
            product names.
          </p>
          <ol className="mt-8 max-w-3xl space-y-0 border-l border-line">
            {STEPS.map((step, index) => (
              <li key={step.title} className="relative py-4 pl-8">
                <span className="absolute top-5 -left-3.5 flex h-7 w-7 items-center justify-center rounded-full bg-forest text-xs font-semibold text-paper">
                  {index + 1}
                </span>
                <p className="font-semibold text-ink">{step.title}</p>
                <p className="mt-1 text-sm leading-relaxed text-stone-700">{step.body}</p>
              </li>
            ))}
          </ol>
        </section>

        <section>
          <h2 className="font-serif text-3xl font-semibold tracking-tight text-ink">
            How a week of study feels
          </h2>
          <ul className="mt-8 grid gap-4 md:grid-cols-3">
            <li className="rounded-3xl border border-line bg-paper p-6 shadow-sm">
              <p className="text-sm font-medium text-forest">Read here</p>
              <h3 className="mt-2 font-serif text-xl font-semibold text-ink">Short lessons, in order</h3>
              <p className="mt-3 text-sm leading-relaxed text-stone-700">
                Open a topic, then read its pages left to right. Later topics
                assume you did the earlier ones. Phone security can wait until
                the web and API path is solid.
              </p>
            </li>
            <li className="rounded-3xl border border-line bg-paper p-6 shadow-sm">
              <p className="text-sm font-medium text-forest">Practice there</p>
              <h3 className="mt-2 font-serif text-xl font-semibold text-ink">On your computer, not this site</h3>
              <p className="mt-3 text-sm leading-relaxed text-stone-700">
                When a lesson says to practice, you use files from the GitHub
                repository. The broken and repaired versions live there. This
                website only explains what to try and what must not happen.
              </p>
            </li>
            <li className="rounded-3xl border border-line bg-paper p-6 shadow-sm">
              <p className="text-sm font-medium text-forest">No grade here</p>
              <h3 className="mt-2 font-serif text-xl font-semibold text-ink">This site does not certify you</h3>
              <p className="mt-3 text-sm leading-relaxed text-stone-700">
                Checkboxes that say you visited a topic stay on this device.
                Passing a real checkpoint takes evidence you produce — not
                finishing a page.
              </p>
            </li>
          </ul>
        </section>

        <section>
          <h2 className="font-serif text-3xl font-semibold tracking-tight text-ink">
            How to begin
          </h2>
          <ol className="mt-8 grid gap-4 md:grid-cols-3">
            <li className="rounded-3xl bg-forest p-6 text-paper">
              <p className="text-sm font-medium text-emerald-100">Step 1</p>
              <h3 className="mt-2 font-serif text-xl font-semibold">Read the ground rules</h3>
              <p className="mt-3 text-sm leading-relaxed text-emerald-50">
                What you may practice, what you must not, and how a topic is
                put together. Ten minutes. Then you will know the shape of the rest.
              </p>
              <p className="mt-5">
                <ButtonLink href="/learn/0.1/" variant="inverse">
                  Open orientation
                </ButtonLink>
              </p>
            </li>
            <li className="rounded-3xl border border-line bg-paper p-6">
              <p className="text-sm font-medium text-forest">Step 2</p>
              <h3 className="mt-2 font-serif text-xl font-semibold text-ink">Learn what “secure” means here</h3>
              <p className="mt-3 text-sm leading-relaxed text-stone-700">
                The first real lesson is not a tool. It is how to write a rule
                you can test — and why a scanner report is not that rule.
              </p>
              <p className="mt-5">
                <ButtonLink href="/learn/1.1/" variant="secondary">
                  Open the first topic
                </ButtonLink>
              </p>
            </li>
            <li className="rounded-3xl border border-line bg-paper p-6">
              <p className="text-sm font-medium text-forest">Step 3</p>
              <h3 className="mt-2 font-serif text-xl font-semibold text-ink">Follow the study order</h3>
              <p className="mt-3 text-sm leading-relaxed text-stone-700">
                Do not skip ahead to “the interesting attacks.” The course is
                built so each new idea sits on the last one.
              </p>
              <p className="mt-5">
                <ButtonLink href="/roadmap/" variant="secondary">
                  Open the study order
                </ButtonLink>
              </p>
            </li>
          </ol>
        </section>

        <section className="rounded-3xl border border-line bg-paper px-6 py-8 sm:px-10">
          <div className="grid gap-8 lg:grid-cols-2">
            <div>
              <h2 className="font-serif text-3xl font-semibold tracking-tight text-ink">
                Who this is for
              </h2>
              <ul className="mt-4 list-disc space-y-2 pl-5 leading-relaxed text-stone-700">
                <li>People who write or review application code and want security to be part of that work.</li>
                <li>Learners who prefer a running example (a small notes app the course keeps extending) over a pile of disconnected demos.</li>
                <li>Anyone willing to practice on their own machine and stay inside the rules.</li>
              </ul>
            </div>
            <div>
              <h2 className="font-serif text-3xl font-semibold tracking-tight text-ink">
                Who this is not
              </h2>
              <ul className="mt-4 list-disc space-y-2 pl-5 leading-relaxed text-stone-700">
                <li>A playlist of “top vulnerabilities” to memorize.</li>
                <li>A website where you attack a live app in the browser.</li>
                <li>
                  Permission to test anyone else’s systems. Read{" "}
                  <a href="/policy/" className="text-link underline underline-offset-2">
                    Safe use
                  </a>{" "}
                  before you practice.
                </li>
              </ul>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}
