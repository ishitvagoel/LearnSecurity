export type StandardRef = {
  source: string;
  version: string;
  status: string;
  requirementIds: string[];
  url: string;
};

export type LearningObject = {
  id: string;
  kind: string;
  title: string;
  path?: string;
};

export type LabSpec = {
  authorizedScope?: string;
  slug?: string;
  summary?: string;
  forbiddenOutcomes?: string[];
} | null;

export type ModuleMeta = {
  id: string;
  slug: string;
  title: string;
  phase: number;
  track: string;
  difficulty: string;
  status: string;
  estimatedMinutes: number;
  prerequisites: string[];
  routeTags: string[];
  releaseMilestone: string | null;
  outcomes: string[];
  reviewTriggers: string[];
  invariants: string[];
  threatModelPrompts: string[];
  concepts: string[];
  learningObjects: LearningObject[];
  labSpec: LabSpec;
  evidenceRequired: string[];
  assessmentBlueprint: Record<string, string>;
  masteryGate: string | null;
  standardsRefs: StandardRef[];
  misconceptions: string[];
  operationalConsiderations: string[];
  author: string | null;
  reviewer: string | null;
  lastReviewedAt: string | null;
  nextReviewAt: string | null;
  changelog: { date: string; note: string }[];
  contentDir: string;
};

export type LessonFile = {
  id: string;
  title: string;
  kind: string;
  filename: string;
  body: string;
};
