import { HomeContinue } from "@/components/HomeContinue";
import { ButtonLink } from "@/components/ui";
import { loadAllModules } from "@/lib/loadCurriculum";

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
            <p className="text-sm font-medium text-forest">A free course</p>
            <h1 className="mt-3 max-w-3xl font-serif text-4xl font-semibold tracking-tight text-ink sm:text-5xl sm:leading-[1.12]">
              Learn to build software that stays safe when someone tries to break it
            </h1>
            <p className="mt-5 max-w-xl text-lg leading-relaxed text-stone-700">
              Read the lessons here, in your browser. When it is time to
              practice, you use files on your own computer. You never attack a
              live website from this course.
            </p>
            <div className="mt-8 flex flex-col gap-3 sm:flex-row">
              <ButtonLink href="/learn/0.1/" className="w-full sm:w-auto">
                Start with the first lesson
              </ButtonLink>
              <ButtonLink href="/learn/" variant="secondary" className="w-full sm:w-auto">
                See all the lessons
              </ButtonLink>
            </div>
            <HomeContinue />
          </div>
          <aside className="rounded-3xl border border-line bg-paper p-6 shadow-sm">
            <p className="text-sm font-medium text-forest">What is on this site</p>
            <ul className="mt-4 space-y-4 text-sm leading-relaxed text-stone-700">
              <li>
                <strong className="block text-ink">Lessons</strong>
                Short pages you read in order.
              </li>
              <li>
                <strong className="block text-ink">Study order</strong>
                A list of what to do next, so you are not guessing.
              </li>
              <li>
                <strong className="block text-ink">Practice notes</strong>
                When a lesson asks you to try something, you clone the course
                files and run them on your computer. This website never runs
                the broken apps.
              </li>
            </ul>
            <p className="mt-5 text-xs leading-relaxed text-muted">
              {topicCount} topics. No account. If you tick “I’ve read this,” that
              stays in this browser.
            </p>
          </aside>
        </div>
      </section>

      <div className="mx-auto max-w-6xl space-y-20 px-4 py-6 pb-20">
        <section>
          <h2 className="font-serif text-3xl font-semibold tracking-tight text-ink">
            How a topic works
          </h2>
          <ol className="mt-8 max-w-3xl space-y-0 border-l border-line">
            {[
              {
                title: "Read",
                body: "Open a topic and read its pages left to right. Later topics assume you did the earlier ones.",
              },
              {
                title: "Try it — on your computer",
                body: "If there is practice, you use files from the GitHub repository. This site only tells you what to try.",
              },
              {
                title: "Fix what broke",
                body: "Change the design so the problem cannot happen the same way again. A scanner warning is not a fix.",
              },
              {
                title: "Check, then move on",
                body: "A good check fails on the broken files and passes on the repaired ones. Then open the next topic.",
              },
            ].map((step, index) => (
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
            How to begin
          </h2>
          <ol className="mt-8 grid gap-4 md:grid-cols-3">
            <li className="rounded-3xl bg-forest p-6 text-paper">
              <p className="text-sm font-medium text-emerald-100">First</p>
              <h3 className="mt-2 font-serif text-xl font-semibold">Read the ground rules</h3>
              <p className="mt-3 text-sm leading-relaxed text-emerald-50">
                What you may practice, what you must not, and how a topic is put
                together. About ten minutes.
              </p>
              <p className="mt-5">
                <ButtonLink href="/learn/0.1/" variant="inverse">
                  Open the first lesson
                </ButtonLink>
              </p>
            </li>
            <li className="rounded-3xl border border-line bg-paper p-6">
              <p className="text-sm font-medium text-forest">Then</p>
              <h3 className="mt-2 font-serif text-xl font-semibold text-ink">
                Learn what “secure” means here
              </h3>
              <p className="mt-3 text-sm leading-relaxed text-stone-700">
                The next topic is not a tool. It is how to write a rule you can
                actually check.
              </p>
              <p className="mt-5">
                <ButtonLink href="/learn/1.1/" variant="secondary">
                  Open the next topic
                </ButtonLink>
              </p>
            </li>
            <li className="rounded-3xl border border-line bg-paper p-6">
              <p className="text-sm font-medium text-forest">After that</p>
              <h3 className="mt-2 font-serif text-xl font-semibold text-ink">
                Follow the study order
              </h3>
              <p className="mt-3 text-sm leading-relaxed text-stone-700">
                Do not skip ahead to the flashy attacks. Each new idea sits on
                the last one.
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
          <h2 className="font-serif text-3xl font-semibold tracking-tight text-ink">
            Who this is for
          </h2>
          <p className="mt-4 max-w-2xl leading-relaxed text-stone-700">
            People who write or review software and want safety to be part of
            that work. You will follow one small notes app as it grows, instead
            of a pile of disconnected demos. This is not a hacking playground,
            and it is not a list of famous bugs to memorize. Read the{" "}
            <a href="/policy/" className="text-link underline underline-offset-2">
              rules
            </a>{" "}
            before you practice.
          </p>
        </section>
      </div>
    </div>
  );
}
