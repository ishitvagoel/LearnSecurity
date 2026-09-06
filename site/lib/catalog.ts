import type { ModuleMeta } from "./types";

export const PHASES: Record<number, { title: string; blurb: string }> = {
  0: {
    title: "Getting started",
    blurb: "What this course is, the rules for practice, and how to find your way.",
  },
  1: {
    title: "The basics",
    blurb: "What “secure” means here, who is allowed to do what, and where trust stops.",
  },
  2: {
    title: "How software actually runs",
    blurb: "Text, browsers, the network, and timing — the places quiet bugs hide.",
  },
  3: {
    title: "Design when someone might attack",
    blurb: "Name what you are protecting, who might try to break it, and how the app is put together.",
  },
  4: {
    title: "Logins and access",
    blurb: "Accounts, staying signed in, and keeping one team’s notes away from another.",
  },
  5: {
    title: "Data and secrets",
    blurb: "What you store, how long you keep it, and when encryption actually helps.",
  },
  6: {
    title: "Bad input and abuse",
    blurb: "Stopping typed-in text from turning into commands, fake pages, or extra work the app never meant to do.",
  },
  7: {
    title: "APIs and background jobs",
    blurb:
      "Other programs calling yours, and work that runs when nobody is looking. Extra topics open after this section.",
  },
  8: {
    title: "Phone apps",
    blurb: "Apps on a phone you do not control. You can leave this until the website path is done.",
  },
  9: {
    title: "Checking your work",
    blurb: "Reviews, tests, and tools — and why a green report is not the same as a real check.",
  },
  10: {
    title: "Shipping and running it",
    blurb: "Builds, cloud accounts, settings, logs, and what you do when something goes wrong.",
  },
  11: {
    title: "Final project",
    blurb: "Put the pieces together on the notes app the course has been building.",
  },
};

/** Short names for cards and headers. Not the curriculum YAML titles. */
export const TOPIC_TITLE: Record<string, string> = {
  "0.1": "How to use this course",
  "0.2": "A first check-in",
  "1.1": "What “secure” means",
  "1.2": "Who is allowed to do what",
  "1.3": "Where trust stops",
  "1.4": "People, money, and recovery",
  "2.1": "Text, files, and parsers",
  "2.2": "The path a request takes",
  "2.3": "What a web page can do",
  "2.4": "Time and two things at once",
  "3.1": "What you are protecting",
  "3.2": "Who might attack",
  "3.3": "How to structure the app",
  "3.4": "Tricks on the happy path",
  "4.1": "Accounts",
  "4.2": "Signing in",
  "4.3": "Staying signed in",
  "4.4": "Keeping companies apart",
  "4.5": "Sign in with other apps",
  "5.1": "What you store, and for how long",
  "5.2": "What encryption does and does not do",
  "5.3": "Passwords and keys",
  "5.4": "Talking to the right place",
  "5.5": "The database",
  "6.1": "Typed-in text must not become a command",
  "6.2": "Pages must not run someone else’s script",
  "6.3": "Clicks from another site",
  "6.4": "Uploads and file names",
  "6.5": "The server fetching a URL",
  "6.6": "Two clicks and skipped checks",
  "6.7": "Asking for more than a fair share",
  "7.1": "What your API actually offers",
  "7.2": "Some fields, not every field",
  "7.3": "Other companies calling you back",
  "7.4": "Background jobs",
  "8.1": "Don’t trust the phone app",
  "8.2": "What’s stored on the device",
  "8.3": "Links that open the app",
  "8.4": "How the app is built and shipped",
  "8.5": "Checking a phone app",
  "9.1": "Each claim needs a check",
  "9.2": "Reading a change like an attacker",
  "9.3": "Tests for the bad case",
  "9.4": "Scanners are not the whole check",
  "9.5": "A test with permission, then a fix",
  "10.1": "How the team works",
  "10.2": "Git, the build, and libraries",
  "10.3": "Cloud accounts and containers",
  "10.4": "Settings in production",
  "10.5": "Logs, alerts, and getting back up",
  "11": "Putting the notes app together",
  E1: "When the app calls an AI",
  E2: "Headers, the edge, and the browser",
  E3: "Payments and health data",
  E4: "Code that copies bytes",
  E5: "Switching you into another customer",
  E6: "A risk you accept",
};

/** One plain sentence per topic, for cards. Not the curriculum outcome text. */
export const TOPIC_BLURB: Record<string, string> = {
  "0.1": "The rules for practice, and how a topic is put together.",
  "0.2": "A short check-in so you know what to review before you move on.",
  "1.1": "What we mean by “secure,” in words you can actually check.",
  "1.2": "Who is allowed to do what — and checking that every time, not once.",
  "1.3": "What you trust, what you don’t, and how big a mistake can get.",
  "1.4": "People, money, and recovery — including folks who need the app to stay usable.",
  "2.1": "How text and files get read, and how two readers can disagree.",
  "2.2": "The path a request takes, including caches that might show the wrong person’s data.",
  "2.3": "What a web page is allowed to do in the browser.",
  "2.4": "Time, retries, and two things happening at once.",
  "3.1": "What you’re protecting, and how careful you need to be with it.",
  "3.2": "Writing down who might attack, and what they would try.",
  "3.3": "Common ways to structure an app so a break doesn’t spread.",
  "3.4": "Tricks that follow the happy path but still steal or break something.",
  "4.1": "Creating, changing, and closing accounts.",
  "4.2": "Signing in in a way that’s hard to phish, and still easy to use.",
  "4.3": "Staying signed in without leaving a stolen cookie in the open.",
  "4.4": "One company must not read another company’s notes.",
  "4.5": "“Sign in with…” and apps that are not your server.",
  "5.1": "Collect less, keep it for a reason, and delete the copies too.",
  "5.2": "What encryption does and does not buy you.",
  "5.3": "Passwords and keys: store them, rotate them, don’t paste them into code.",
  "5.4": "Making sure you’re talking to the right place, not a look-alike.",
  "5.5": "The database: who can query it, and what a backup still holds.",
  "6.1": "Typed-in text must not become a command.",
  "6.2": "Pages must not run someone else’s script.",
  "6.3": "A click or a form from another site should not act as you.",
  "6.4": "Uploads, file names, and archives that try to climb out of their folder.",
  "6.5": "Your server fetching a URL the user chose.",
  "6.6": "Two clicks, a retry, or an error path that skips a check.",
  "6.7": "Someone (or a bot) asking for more than a fair share.",
  "7.1": "What your API actually offers, and keeping that list honest.",
  "7.2": "A user may edit some fields, not every field on the object.",
  "7.3": "Other companies calling you back — prove it’s really them.",
  "7.4": "Background jobs are not the logged-in user.",
  "8.1": "A phone app can be copied and changed. Don’t trust it.",
  "8.2": "What’s stored on the device, and who can read it.",
  "8.3": "Links that open the app, and talking to other apps.",
  "8.4": "How the app is built and shipped, and proving it’s yours.",
  "8.5": "Checking a phone app, including privacy.",
  "9.1": "Each claim needs a way to show it’s true.",
  "9.2": "Reading a change like someone who wants it to fail.",
  "9.3": "Tests that try the bad case, not only the happy one.",
  "9.4": "Scanners help; they don’t replace a real check.",
  "9.5": "A test with permission, then fix what you found and look again.",
  "10.1": "How the team works day to day, not a poster on the wall.",
  "10.2": "Git, the build, and the libraries you pull in.",
  "10.3": "Cloud accounts, containers, and “the app may do this.”",
  "10.4": "Settings in production: debug off, secrets out of the image.",
  "10.5": "Logs, alerts, and getting back up — without leaking notes in the log.",
  "11": "Show the notes app still keeps its promises when everything runs together.",
  E1: "When the app calls an AI, the model is not in charge of the database.",
  E2: "Headers, the edge, and the browser — and reports that don’t actually block.",
  E3: "Payments and health data: extra care, still the same kind of rule.",
  E4: "Code that copies bytes must respect the size of the box.",
  E5: "A JSON field must not switch you into another customer’s workspace.",
  E6: "A risk you accept needs an owner and a date, not a shrug.",
};

export function topicTitle(mod: ModuleMeta): string {
  return TOPIC_TITLE[mod.id] || mod.title;
}

export function topicBlurb(mod: ModuleMeta): string {
  return TOPIC_BLURB[mod.id] || mod.title;
}

export function phaseHeading(phase: number): string {
  const meta = PHASES[phase];
  return meta ? meta.title : `Part ${phase}`;
}

export function trackLabel(track: string): string {
  switch (track) {
    case "core":
      return "Core";
    case "elective":
      return "Extra";
    case "mobile":
      return "Phone";
    case "capstone":
      return "Final project";
    case "bridge":
      return "Check-in";
    default:
      return track;
  }
}

export function difficultyLabel(difficulty: string): string {
  switch (difficulty) {
    case "foundation":
      return "Beginner";
    case "intermediate":
      return "Intermediate";
    case "advanced":
      return "Advanced";
    case "capstone":
      return "Final project";
    default:
      return difficulty;
  }
}

export function formatMinutes(minutes: number): string {
  if (minutes < 60) {
    return `About ${minutes} min`;
  }
  const hours = Math.round(minutes / 60);
  return hours === 1 ? "About 1 hour" : `About ${hours} hours`;
}

export function pinStatusLabel(status: string): string {
  switch (status) {
    case "final":
      return "Published";
    case "draft":
      return "Draft";
    case "unverified":
      return "Not confirmed";
    default:
      return status;
  }
}

export function modulesInPhase(modules: ModuleMeta[], phase: number): ModuleMeta[] {
  return modules.filter((m) => m.phase === phase);
}

export function phaseList(modules: ModuleMeta[]): number[] {
  return [...new Set(modules.map((m) => m.phase))].sort((a, b) => a - b);
}

export function firstLessonHref(mod: ModuleMeta): string | null {
  const lo = (mod.learningObjects || []).find((o) => o.path);
  if (!lo?.path) {
    return null;
  }
  const slug = lo.path.replace(/^lessons\//, "").replace(/\.md$/, "");
  return `/learn/${encodeURIComponent(mod.id)}/${encodeURIComponent(slug)}/`;
}
