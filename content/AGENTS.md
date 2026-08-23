# Content tree

This directory holds **curriculum metadata and authored learning objects**. It is not the Vercel site and not executable labs.

## Layout

| Path | Role |
|---|---|
| `schema/` | JSON Schema for module metadata (§14.2) |
| `templates/` | Pass A spec template |
| `progress/STATUS.yaml` | Iteration state; read and update every session |
| `modules/<phase>/<id>/` | One folder per module (`spec.md`, `module.yaml`, later `lessons/`, `assessment/`) |
| `standards/pins.yaml` | Pinned standard versions (created by `standards-pin`) |
| `assessment/keys/` | Answer keys and examiner notes — never linked from learner pages |
| `glossary/` | Canonical terms (later) |

Phase folder names: `0` … `11` and `e` for electives.

## Authoring rules

- Validate `module.yaml` against `schema/module.schema.json` before marking Pass A complete.
- Lesson prose starts with a security property or question, not a product command.
- Required in every publishable module: misconception list, transfer task, named attacker capabilities, mechanism limits, and standards refs with status labels.
- Do not place exploit payloads, real secrets, or PII in this tree. Break/fix code lives in `labs/`.
- Keep frontmatter/`module.yaml` as the machine-readable source; Markdown bodies are human-facing.

## Pass boundaries

- **Pass A:** `spec.md` + `module.yaml` only.
- **Pass B:** `lessons/` plus pointers to `labs/...` — no answer keys here.
- **Pass C:** learner-facing prompts and rubrics here; keys only in `assessment/keys/`.
