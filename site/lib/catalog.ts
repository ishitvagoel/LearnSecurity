import type { ModuleMeta } from "./types";

export const PHASES: Record<number, { title: string; blurb: string }> = {
  0: {
    title: "Orientation",
    blurb:
      "How this course defines security, what an authorized lab is, and how to keep work local.",
  },
  1: {
    title: "Foundations",
    blurb:
      "Name invariants, authority, trust boundaries, and residual risk for SecureCollab—before picking tools.",
  },
  2: {
    title: "How software actually runs",
    blurb:
      "Bytes, parsers, HTTP, browsers, and time. Mechanisms fail when you ignore the interpreter.",
  },
  3: {
    title: "Design under threat",
    blurb:
      "Classify assets, model attackers, choose architecture patterns, and design for abuse.",
  },
  4: {
    title: "Identity and access",
    blurb:
      "Accounts, phishing-resistant authentication, sessions, tenant isolation, and delegated access.",
  },
  5: {
    title: "Data and cryptography",
    blurb:
      "Lifecycle and privacy, cryptographic properties, keys, channels, and persistence.",
  },
  6: {
    title: "Injection and abuse",
    blurb:
      "Interpreters, browsers, files, server-side requests, workflows, and resource abuse.",
  },
  7: {
    title: "APIs and workers",
    blurb:
      "Contracts, field-level authorization, webhooks, and service identity on queues.",
  },
  8: {
    title: "Mobile",
    blurb:
      "Hostile clients, on-device storage, deep links, builds, and mobile privacy. Optional until the web/API milestone.",
  },
  9: {
    title: "Verification",
    blurb:
      "Traceability, review, security tests, tools as inputs, and retesting after repair.",
  },
  10: {
    title: "Operate and ship",
    blurb:
      "Lifecycle culture, supply chain, cloud identity, hardening, and incident recovery.",
  },
  11: {
    title: "Capstone",
    blurb:
      "Defend SecureCollab as one system: invariants that still hold after revoke, retry, and time.",
  },
};

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
