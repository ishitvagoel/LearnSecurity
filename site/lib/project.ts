import fs from "node:fs";
import path from "node:path";
import yaml from "js-yaml";
import { contentRoot } from "./contentRoot";

export type ProjectMilestone = {
  id: string;
  title: string;
  status: "planned" | "optional" | "teaching-stand-in" | string;
  moduleId: string;
  labPath?: string;
  summary: string;
  learnerArtifacts: string[];
  revisit: string;
};

export function loadProjectMilestones(): { version: number; product: string; milestones: ProjectMilestone[] } {
  const file = path.join(contentRoot(), "reference", "securecollab", "milestones.yaml");
  const data = yaml.load(fs.readFileSync(file, "utf8")) as {
    version?: number;
    product?: string;
    milestones?: ProjectMilestone[];
  };
  return {
    version: data.version || 1,
    product: data.product || "SecureCollab",
    milestones: data.milestones || [],
  };
}
