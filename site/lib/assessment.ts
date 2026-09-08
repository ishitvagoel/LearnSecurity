import type { AssessmentEvidence, AssessmentPrompt, ModuleMeta } from "./types";

function firstOr(fallback: string, values: string[] | undefined): string {
  return values?.find((value) => value.trim()) || fallback;
}

function transferTitle(mod: ModuleMeta): string {
  const transfer = (mod.learningObjects || []).find((object) => object.kind === "transfer-challenge");
  return transfer?.title || "a new system with a different trust boundary";
}

export function assessmentPrompts(mod: ModuleMeta): AssessmentPrompt[] {
  const blueprint = mod.assessmentBlueprint || {};
  return [
    {
      id: "property",
      title: "State the rule",
      prompt:
        "State this topic’s security rule in one sentence. Name the asset, the actor or action, and what must not happen.",
      hint: firstOr("A rule another engineer could check.", mod.invariants),
    },
    {
      id: "model",
      title: "Draw the model",
      prompt:
        "Describe or sketch the trust boundary, interpreter, state transition, or copy that matters here. Name what you trust and what an attacker can control.",
      hint: firstOr("Which trust boundary or interpreter is in play?", mod.threatModelPrompts),
    },
    {
      id: "break",
      title: "Explain the break",
      prompt:
        "Describe the representative failure in the local practice. What input, identity, state, or timing reaches the wrong decision, and what is the security impact?",
      hint: firstOr("Run this only inside the authorized local practice folder.", [mod.labSpec?.summary || ""]),
    },
    {
      id: "build",
      title: "Describe the structural fix",
      prompt:
        "Describe the smallest structural repair a second engineer should implement. Say what is checked at the boundary and what the repair deliberately does not prove.",
      hint: firstOr("No build detail has been recorded for this topic yet.", [blueprint.build || ""]),
    },
    {
      id: "verify",
      title: "Write the checks",
      prompt:
        "Write checks that fail on the broken files and pass on the repaired files. Include a normal case, a negative or abuse case, and a malformed or failure case where relevant.",
      hint: firstOr("Name the forbidden outcome and the oracle that catches it.", [blueprint.verify || ""]),
    },
    {
      id: "operate",
      title: "Plan detection and recovery",
      prompt:
        "Write the signal, safe log fields, owner or action, and recovery step you would use if this rule failed in a running service. Do not put secrets or user content in the log.",
      hint: firstOr("Detection and recovery notes.", mod.operationalConsiderations),
    },
    {
      id: "transfer",
      title: "Use it somewhere new",
      prompt: `Apply the same rule to ${transferTitle(mod)}. State which assumption changed, what must be rechecked, and what remains out of scope.`,
      hint: firstOr("A transfer challenge is part of the evidence.", [blueprint.communicate || ""]),
    },
  ];
}

export function assessmentEvidence(mod: ModuleMeta): AssessmentEvidence[] {
  return (mod.evidenceRequired || []).map((label, index) => ({
    id: `evidence-${index + 1}`,
    label,
  }));
}
