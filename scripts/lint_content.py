#!/usr/bin/env python3
"""Mechanical content quality gate for LearnSecurity.

Implements rules L001-L017 from
.cursor/skills/content-lint/references/lint-rules.md.

The linter checks shape. It cannot tell whether 900 words carried reasoning or
restated the claim nine times -- that is the reviewer's job. L001 exists to make
room for reasoning, not to certify it.

Dependencies: stdlib + PyYAML.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

import yaml

REPO = Path(__file__).resolve().parent.parent
MODULES = REPO / "content" / "modules"
KEYS_DIR = REPO / "content" / "assessment" / "keys"
SCHEMA = REPO / "content" / "schema" / "module.schema.json"

ERROR, WARN = "ERROR", "WARN"

# Headings allowed to repeat verbatim across modules (lesson-prose.mdc).
SHARED_HEADINGS = {"## Practice", "## Check yourself"}
HEADING_REUSE_LIMIT = 20

WORD_FLOOR = 900
SHORT_SENTENCE_WORDS = 5
SHORT_SENTENCE_MAX_SHARE = 0.12
MEDIAN_SENTENCE_FLOOR = 11

LAB_MINUTES = {1: 45, 2: 120, 3: 240}


@dataclass
class Finding:
    rule: str
    level: str
    path: Path
    line: int
    message: str
    #: Stable identity for baselining. Line numbers move; this should not.
    extra: str = ""

    @property
    def rel(self) -> str:
        try:
            return str(self.path.relative_to(REPO))
        except ValueError:
            return str(self.path)

    @property
    def key(self) -> str:
        return f"{self.rel}::{self.extra}" if self.extra else self.rel

    def render(self) -> str:
        return f"{self.rel}:{self.line}: [{self.rule}] {self.message}"


# --------------------------------------------------------------------------
# Prose extraction
#
# All prose measurements exclude fenced code, Mermaid, table rows, headings,
# and the bold metadata lines at the top of a lesson.
# --------------------------------------------------------------------------

FENCE_RE = re.compile(r"^\s*```")
TABLE_RE = re.compile(r"^\s*\|")
HEADING_RE = re.compile(r"^\s*#{1,6}\s")
META_RE = re.compile(r"^\*\*[A-Z][^*]*:\*\*")
LIST_RE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")


def strip_fences(text: str) -> str:
    """Remove fenced blocks, keeping line count stable for line reporting."""
    out, in_fence = [], False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def prose_segments(text: str) -> list[str]:
    """Body prose as segments: paragraphs joined, list items handled carefully.

    A bullet run introduced by a colon and written as ";"-separated clauses is
    ONE sentence laid out vertically -- good writing, not fragments. Treating
    each bullet as its own sentence would flag the reference modules for their
    best prose, so continuation items are rejoined into the clause they belong
    to. A bullet that ends in "." stands alone.
    """
    segments: list[str] = []
    para: list[str] = []
    run: list[str] = []

    def flush_para() -> None:
        if para:
            segments.append(" ".join(para))
            para.clear()

    def flush_run() -> None:
        if run:
            segments.append(" ".join(run))
            run.clear()

    for raw in strip_fences(text).splitlines():
        line = raw.rstrip()
        if not line.strip() or TABLE_RE.match(line) or HEADING_RE.match(line) or META_RE.match(line):
            flush_para()
            flush_run()
            continue
        line = re.sub(r"^\s*>\s?", "", line)
        if LIST_RE.match(line):
            flush_para()
            item = LIST_RE.sub("", line).strip()
            run.append(item)
            # A clause ending in ";" or "," continues into the next bullet.
            if not re.search(r"[;,]$", clean_inline(item)):
                flush_run()
            continue
        flush_run()
        para.append(line.strip())
    flush_para()
    flush_run()
    return [clean_inline(s) for s in segments if s.strip()]


def clean_inline(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # keep link text
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"[*_]{1,3}", "", text)
    return re.sub(r"\s+", " ", text).strip()


SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
ABBREV = re.compile(r"\b(?:e\.g|i\.e|etc|vs|cf|Dr|Mr|Ms|No)\.$", re.I)


def sentences(text: str) -> list[str]:
    """Sentence units used by L002/L003.

    Segments ending in ":" are lead-ins to a block or list. They are structural
    signposts, not assertions, so they are excluded rather than counted as
    four-word fragments.
    """
    out: list[str] = []
    for segment in prose_segments(text):
        if segment.rstrip().endswith(":"):
            continue
        # A bare path, command, permission token, or identifier standing alone
        # is a vocabulary entry, not a sentence. Counting "membership:grant" as
        # a two-word fragment would flag a glossary list as bad prose.
        if len(segment.split()) < 3 and re.fullmatch(r"[\w./\\@:{}<>-]+", segment.strip()):
            continue
        parts = SENTENCE_SPLIT.split(segment)
        merged: list[str] = []
        for part in parts:
            if merged and ABBREV.search(merged[-1]):
                merged[-1] = f"{merged[-1]} {part}"
            else:
                merged.append(part)
        out.extend(p.strip() for p in merged if p.strip())
    return out


def body_words(text: str) -> int:
    return sum(len(s.split()) for s in prose_segments(text))


def line_of(text: str, needle: str, default: int = 1) -> int:
    for i, line in enumerate(text.splitlines(), 1):
        if needle in line:
            return i
    return default


# --------------------------------------------------------------------------
# Minimal JSON Schema subset validator
#
# The module schema uses only these keywords. Anything else raises, so the
# validator fails loudly rather than silently passing a schema it outgrew.
# --------------------------------------------------------------------------

SUPPORTED = {
    "$schema", "$id", "title", "description", "type", "properties", "required",
    "additionalProperties", "items", "enum", "pattern", "minLength", "minimum",
    "maximum", "minItems",
}

JSON_TYPES = {
    "object": dict, "array": list, "string": str, "boolean": bool,
    "number": (int, float), "integer": int,
}


def validate_schema(node: dict, data, where: str = "") -> list[str]:
    unknown = set(node) - SUPPORTED
    if unknown:
        raise ValueError(f"schema uses unsupported keywords {sorted(unknown)} at {where or '<root>'}")

    errs: list[str] = []
    loc = where or "<root>"

    expected = node.get("type")
    if expected:
        allowed = expected if isinstance(expected, list) else [expected]
        ok = False
        for name in allowed:
            if name == "null":
                ok = ok or data is None
                continue
            py = JSON_TYPES[name]
            # bool is a subclass of int in Python; the schema never means that.
            if isinstance(data, py) and (name == "boolean" or not isinstance(data, bool)):
                ok = True
        if not ok:
            return [f"{loc}: expected {expected}, got {type(data).__name__}"]

    if "enum" in node and data not in node["enum"]:
        errs.append(f"{loc}: {data!r} not in {node['enum']}")
    if "pattern" in node and isinstance(data, str) and not re.search(node["pattern"], data):
        errs.append(f"{loc}: {data!r} does not match /{node['pattern']}/")
    if "minLength" in node and isinstance(data, str) and len(data) < node["minLength"]:
        errs.append(f"{loc}: shorter than minLength {node['minLength']}")
    if "minimum" in node and isinstance(data, (int, float)) and data < node["minimum"]:
        errs.append(f"{loc}: below minimum {node['minimum']}")
    if "maximum" in node and isinstance(data, (int, float)) and data > node["maximum"]:
        errs.append(f"{loc}: above maximum {node['maximum']}")
    if "minItems" in node and isinstance(data, list) and len(data) < node["minItems"]:
        errs.append(f"{loc}: fewer than minItems {node['minItems']}")

    if isinstance(data, dict):
        for name in node.get("required", []):
            if name not in data:
                errs.append(f"{loc}: missing required field '{name}'")
        props = node.get("properties", {})
        if node.get("additionalProperties") is False:
            for name in data:
                if name not in props:
                    errs.append(f"{loc}: unexpected field '{name}'")
        for name, sub in props.items():
            if name in data:
                errs.extend(validate_schema(sub, data[name], f"{loc}.{name}"))
    elif isinstance(data, list) and "items" in node:
        for i, item in enumerate(data):
            errs.extend(validate_schema(node["items"], item, f"{loc}[{i}]"))
    return errs


# --------------------------------------------------------------------------
# Corpus
# --------------------------------------------------------------------------

@dataclass
class Corpus:
    lessons: list[Path] = field(default_factory=list)
    manifests: list[Path] = field(default_factory=list)
    markdown: list[Path] = field(default_factory=list)
    heading_census: dict[str, list[Path]] = field(default_factory=lambda: defaultdict(list))

    @classmethod
    def build(cls) -> "Corpus":
        c = cls()
        c.lessons = sorted(MODULES.glob("*/*/lessons/*.md"))
        c.manifests = sorted(MODULES.glob("*/*/module.yaml"))
        c.markdown = sorted((REPO / "content").rglob("*.md"))
        # The heading census is always repo-wide, even when linting one module:
        # "is this heading a template artifact?" is not a per-file question.
        for lesson in c.lessons:
            for heading in set(headings_of(lesson.read_text(encoding="utf-8"))):
                c.heading_census[heading].append(lesson)
        return c


def headings_of(text: str) -> list[str]:
    return [
        line.strip()
        for line in strip_fences(text).splitlines()
        if line.startswith("## ") and not line.startswith("###")
    ]


def module_of(lesson: Path) -> Path:
    return lesson.parent.parent / "module.yaml"


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - reported as a finding
        return exc


# --------------------------------------------------------------------------
# Lesson rules
# --------------------------------------------------------------------------

MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.S)
NODE_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)\s*[\[\(\{]")
SEQ_MSG_RE = re.compile(r"-{1,2}>>?|-->>")
DIAGRAM_DIRECTIVE = re.compile(
    r"^(?:flowchart|graph|subgraph|end\b|classDef|class\s|style\s|linkStyle|click\s|"
    r"direction|stateDiagram|sequenceDiagram|%%|participant|actor|note\s|autonumber)",
    re.I,
)
ARROW = re.compile(r"-{1,3}[.>ox|-]*>|={2,3}>|-{3,}|\.{3}>|~{3}")
LEADING_ID = re.compile(r"\s*([A-Za-z_][A-Za-z0-9_]*)")


def diagram_shape(body: str) -> tuple[int, int, int]:
    """Return (node count, branch/merge count, disconnected component count).

    Node count alone cannot separate a good small diagram from a bad one. A
    three-node decision tree that branches shows the discriminating test; four
    nodes in two disconnected pairs just restate the sentence above them.
    """
    nodes: set[str] = set()
    out_deg: dict[str, int] = defaultdict(int)
    in_deg: dict[str, int] = defaultdict(int)
    adjacency: dict[str, set[str]] = defaultdict(set)

    for raw in body.splitlines():
        line = raw.strip()
        if not line or DIAGRAM_DIRECTIVE.match(line):
            continue
        nodes.update(NODE_RE.findall(line))
        # Strip node labels first, then edge labels, so that "a -->|yes| b"
        # does not read "yes" as a node.
        bare = re.sub(r"\[[^\]]*\]|\([^)]*\)|\{[^}]*\}", " ", line)
        bare = re.sub(r"\|[^|]*\|", " ", bare)
        chain = [m.group(1) for m in (LEADING_ID.match(part) for part in ARROW.split(bare)) if m]
        nodes.update(chain)
        for src, dst in zip(chain, chain[1:]):
            out_deg[src] += 1
            in_deg[dst] += 1
            adjacency[src].add(dst)
            adjacency[dst].add(src)

    branches = sum(1 for n in nodes if out_deg[n] > 1 or in_deg[n] > 1)

    seen: set[str] = set()
    components = 0
    for node in nodes:
        if node in seen:
            continue
        components += 1
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            stack.extend(adjacency[cur] - seen)
    return len(nodes), branches, components


SCOPE_NOUNS = r"public|live|employer|third[- ]party|production|real (?:PII|secret|patient|clinic|user)"
SCOPE_RE = re.compile(rf"(?:Run this only inside)|(?:\bDo not\b.{{0,120}}?(?:{SCOPE_NOUNS}))", re.I)

MODULE_ID_RE = re.compile(r"(?<![\d.\w])(?:\d{1,2}\.\d{1,2}|E\d)(?![\d.\w])")
STANDARDS_WORDS = re.compile(r"ASVS|MASVS|MASTG|MASWE|NIST|RFC|OWASP|SLSA|WCAG|version|v\d", re.I)
REQ_ID_RE = re.compile(r"v\d+\.\d+(?:\.\d+)?-[\d.]+|MAS[A-Z]*-[A-Z0-9-]+|CWE-\d+")

COUNTEREXAMPLE_RE = re.compile(
    r"counterexample|counter-example|does not|do not stop|is not enough|fails when|"
    r"would not|looks like .{0,40}(?:but|and is not)|not a boundary|still fails|"
    r"passes for the wrong reason|but it fails",
    re.I,
)


def lint_lesson(path: Path, corpus: Corpus, active: set[str]) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    out: list[Finding] = []
    sents = sentences(text)

    def add(rule, level, line, msg, extra=""):
        if rule in active:
            out.append(Finding(rule, level, path, line, msg, extra))

    # L001 -- room for reasoning
    words = body_words(text)
    if words < WORD_FLOOR:
        add("L001", ERROR, 1,
            f"body prose is {words} words, floor is {WORD_FLOOR}; "
            "a lesson this short cannot carry a derivation, a worked example, "
            "a counterexample, limits, and a transfer task")

    if sents:
        # L002 -- fragments
        short = [s for s in sents if len(s.split()) <= SHORT_SENTENCE_WORDS]
        share = len(short) / len(sents)
        if share >= SHORT_SENTENCE_MAX_SHARE:
            sample = "; ".join(f'"{s}"' for s in short[:3])
            add("L002", ERROR, 1,
                f"{share:.0%} of {len(sents)} sentences are <={SHORT_SENTENCE_WORDS} words "
                f"(limit {SHORT_SENTENCE_MAX_SHARE:.0%}); fragments assert conclusions the "
                f"reader cannot re-derive. e.g. {sample}")
        # L003 -- sentence length
        median = statistics.median(len(s.split()) for s in sents)
        if median < MEDIAN_SENTENCE_FLOOR:
            add("L003", ERROR, 1,
                f"median sentence is {median:.0f} words, floor is {MEDIAN_SENTENCE_FLOOR} "
                "(reference modules 1.2/1.3 run 12)")

    # L005 -- diagrams must show what prose cannot
    for block in MERMAID_RE.finditer(text):
        body = block.group(1)
        line = text[: block.start()].count("\n") + 1
        kind = next((l.strip() for l in body.splitlines() if l.strip()), "")
        if kind.startswith("sequenceDiagram"):
            count = len(SEQ_MSG_RE.findall(body))
            if count < 4:
                add("L005", ERROR, line,
                    f"sequence diagram has {count} messages, minimum 4",
                    extra=f"mermaid@{line}")
            continue

        nodes, branches, components = diagram_shape(body)
        if components > 1 and nodes <= 2 * components:
            add("L005", ERROR, line,
                f"diagram is {components} disconnected fragments ({nodes} nodes); it lists "
                "labels instead of showing topology, sequence, or state. Connect it or "
                "write prose", extra=f"mermaid@{line}")
        elif nodes < 4 and branches == 0:
            add("L005", ERROR, line,
                f"diagram has {nodes} nodes in a straight line; it restates the sentence "
                "above it. Show a boundary, a branch, a sequence, or a state change",
                extra=f"mermaid@{line}")

    # L006 / L007 -- references the reader can follow
    fenceless = strip_fences(text)
    for m in re.finditer(r"\(([^()]{0,200}?)\)", fenceless):
        inner, line = m.group(1), fenceless[: m.start()].count("\n") + 1
        if "](" in inner or "[" in inner:
            continue
        line_start = fenceless.rfind("\n", 0, m.start()) + 1
        if fenceless.count("`", line_start, m.start()) % 2 == 1:
            # An odd number of backticks between the start of this line and
            # the match means the match sits inside an inline code span
            # (`required.discard("1.4")`) -- a Python string literal that
            # happens to look like a module id, not a bare prose citation
            # of one. L001's word count already exempts fenced code blocks
            # from this same category of false positive; inline code spans
            # need the identical exemption here.
            continue
        if m.start() > 0 and fenceless[m.start() - 1] == "]":
            # This parenthetical is a Markdown link's own destination
            # (`[title](...)`), not a bare parenthetical citation -- the
            # link already carries a title, which is what L006/L007 exist
            # to require. Without this check, any titled cross-module link
            # whose relative path contains a module id (almost all of them,
            # e.g. "../../2/2.3/lessons/01-property.md") is flagged as the
            # exact "bare ID" defect the titled link was written to avoid,
            # including the rule's own suggested-fix example.
            continue
        if re.search(r"\blater\b", inner, re.I):
            add("L006", ERROR, line,
                f'"({inner})" promises a later module without naming one; '
                "name the destination or delete the promise", extra=f"later@{inner[:40]}")
        elif MODULE_ID_RE.search(inner) and not STANDARDS_WORDS.search(inner):
            add("L007", ERROR, line,
                f'"({inner})" cites a module by bare ID; use a titled link such as '
                "[2.3 Browser cookies and the cookie jar](../../2/2.3/lessons/01-property.md)",
                extra=f"bareid@{inner[:40]}")

    # L008 -- one scope statement, not four
    # The defect is scope boilerplate crowding out teaching, which is a ratio:
    # four warnings in 450 words is the problem, three across 2,400 is not.
    # Two distinct scope statements in a long lesson is proportionate; four in
    # 450 words is the defect. Allowance scales, with a floor of two so a
    # thorough lesson is not punished for being thorough.
    scope_hits = [s for s in sents if SCOPE_RE.search(s)]
    allowance = max(2, -(-words // 700))
    if len(scope_hits) > allowance:
        add("L008", ERROR, line_of(text, scope_hits[allowance][:40]),
            f"{len(scope_hits)} authorized-scope sentences in {words} words (allowance "
            f"{allowance}); repetition crowds out teaching and trains skimming. "
            f"e.g. \"{scope_hits[allowance][:90]}\"")

    # L009 -- traceability the learner can see
    if path.name in {"01-property.md", "05-verify.md"}:
        line = line_of(text, "**Standards:**")
        if "**Standards:**" not in text:
            # 01-property is calibrated: reference module 1.3 carries one.
            # 05-verify is an improvement the reference does not yet demonstrate,
            # so it advises rather than blocks.
            level = ERROR if path.name == "01-property.md" else WARN
            add("L009", level, 1,
                "no **Standards:** line; traceability that only a build script can see "
                "does not teach (blueprint 16.4)")
        else:
            declared = set()
            manifest = load_yaml(module_of(path))
            if isinstance(manifest, dict):
                for ref in manifest.get("standardsRefs") or []:
                    declared.update(ref.get("requirementIds") or [])
            cited = set(REQ_ID_RE.findall(text.splitlines()[line - 1])) if line else set()
            stray = cited - declared
            if stray:
                add("L009", ERROR, line,
                    f"cites {sorted(stray)}, which module.yaml standardsRefs does not declare")

    # L016 -- worked reasoning (advisory)
    example = False
    for block in re.finditer(r"```(?!mermaid)[^\n]*\n.*?```", text, re.S):
        before = body_words(text[max(0, block.start() - 1200): block.start()])
        after = body_words(text[block.end(): block.end() + 1200])
        if before + after >= 60:
            example = True
            break
    if not example:
        add("L016", WARN, 1, "no worked example (a non-Mermaid code block with explanation around it)")
    if not COUNTEREXAMPLE_RE.search(text):
        add("L016", WARN, 1, "no explicit counterexample found; "
                             "the publishability rubric wants one traced example and one counterexample",
            extra="counterexample")

    return out


# --------------------------------------------------------------------------
# Manifest rules
# --------------------------------------------------------------------------

def lint_manifest(path: Path, schema: dict, active: set[str]) -> list[Finding]:
    out: list[Finding] = []
    data = load_yaml(path)

    def add(rule, level, line, msg, extra=""):
        if rule in active:
            out.append(Finding(rule, level, path, line, msg, extra))

    if isinstance(data, Exception):
        add("L012", ERROR, 1, f"unparseable YAML: {data}")
        return out
    if not isinstance(data, dict):
        add("L012", ERROR, 1, "module.yaml is not a mapping")
        return out

    text = path.read_text(encoding="utf-8")

    # L012 -- schema
    for err in validate_schema(schema, data):
        add("L012", ERROR, 1, f"schema: {err}", extra=err[:60])

    # L013 -- no review date without a review
    if "pending" in str(data.get("reviewer", "")).lower():
        for f in ("lastReviewedAt", "nextReviewAt"):
            if data.get(f):
                add("L013", ERROR, line_of(text, f),
                    f"reviewer is 'pending' but {f} is set to {data[f]!r}; "
                    "a review date for a review that did not happen is the failure the "
                    "governance model exists to prevent", extra=f)

    # L014 -- outcomes must be assessable
    title = str(data.get("title", "")).strip().lower()
    for outcome in data.get("outcomes") or []:
        text_o = str(outcome).strip()
        if text_o.lower().startswith("demonstrate:") and text_o.split(":", 1)[1].strip().lower() == title:
            add("L014", ERROR, line_of(text, text_o[:40]),
                f"outcome {text_o!r} is the module title with a verb glued on; "
                "state an observable behaviour an assessment item could evidence",
                extra="demonstrate")

    # L017 -- honest estimates (advisory)
    if "L017" in active:
        expected = estimate_minutes(path.parent, data)
        actual = data.get("estimatedMinutes")
        if expected and isinstance(actual, int) and not (0.75 * expected <= actual <= 1.25 * expected):
            add("L017", WARN, line_of(text, "estimatedMinutes"),
                f"estimatedMinutes is {actual}; the metadata-honesty formula gives ~{expected} "
                "for what this module currently contains")
    return out


def estimate_minutes(module_dir: Path, data: dict) -> int | None:
    lessons = sorted((module_dir / "lessons").glob("*.md"))
    if not lessons:
        return None
    words = sum(body_words(p.read_text(encoding="utf-8")) for p in lessons)

    lab_id = str(data.get("id", ""))
    lab_dir = next((REPO / "labs" / lab_id).glob("*/"), None) if (REPO / "labs" / lab_id).exists() else None
    tier = 1
    if lab_dir:
        impl = sorted((lab_dir / "fixed").glob("*.py")) if (lab_dir / "fixed").exists() else []
        loc = sum(len(p.read_text(encoding="utf-8").splitlines()) for p in impl)
        tier = 3 if loc > 200 else 2 if loc >= 60 else 1

    items = module_dir / "assessment" / "items.md"
    n_items = len(re.findall(r"^## \d+\.", items.read_text(encoding="utf-8"), re.M)) if items.exists() else 0

    total = words / 200 + LAB_MINUTES[tier] + n_items * 12 + 60
    return int(round(total / 30) * 30)


# --------------------------------------------------------------------------
# Repo-wide and cross-file rules
# --------------------------------------------------------------------------

BANNED = [
    (re.compile(r"\bv4\.\d+\.\d+|ASVS[ -]4\.\d"), "ASVS 4.x identifier; this course pins ASVS 5.0"),
    (re.compile(r"\bMASVS-L[12]\b"), "obsolete MASVS L1/L2 level; use MASVS 2.1 testing profiles"),
    (re.compile(r"\bMASVS-R\b"), "obsolete MASVS-R level; use MASVS 2.1 testing profiles"),
]
KEY_PHRASES = [
    re.compile(r"\banswer keys?\b", re.I),
    re.compile(r"\bintended findings?\b", re.I),
    re.compile(r"\bexpected answers?\b", re.I),
]
# Naming where the keys live, or saying they are closed, is correct practice.
# Only an actual leak is a finding.
KEY_POINTER = re.compile(
    r"assessment/keys|keys/|are not on|not on this site|live only in|stay(?:s)? (?:in|closed)|"
    r"keep .{0,20}closed|do not (?:look at|open)|never linked|not learner-facing", re.I)
# A line that rejects a term is teaching against it, not using it.
REJECTS = re.compile(
    r"\bno\b|\bnot\b|never|without|obsolete|mix(?:ed|ing)?|forbid|reject|instead of|"
    r"do not|superseded|deprecated|stop using|is not", re.I)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+?)(?:#[^)]*)?\)")


def lint_markdown(path: Path, active: set[str]) -> list[Finding]:
    out: list[Finding] = []
    raw = path.read_text(encoding="utf-8")
    # Fenced blocks and inline code spans hold examples, not live references.
    text = re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), strip_fences(raw))

    def add(rule, level, line, msg, extra=""):
        if rule in active:
            out.append(Finding(rule, level, path, line, msg, extra))

    # Plans, audits, and review artifacts quote the banned patterns in order to
    # forbid them. Linting those would flag the rulebook, so they are exempt
    # from the two content-hygiene rules while still being link-checked.
    is_process_doc = (REPO / "content" / "progress") in path.parents

    for lineno, line in enumerate(text.splitlines(), 1):
        for pattern, why in BANNED:
            if pattern.search(line) and not REJECTS.search(line) and not is_process_doc:
                add("L010", ERROR, lineno, why, extra=why[:30])

        # L011 -- key isolation. The rule targets learner-facing module content;
        # the keys tree is where this language belongs.
        if MODULES in path.parents:
            for phrase in KEY_PHRASES:
                m = phrase.search(line)
                # A line that points at the keys directory, or rejects the idea,
                # is correct practice rather than a leak.
                if m and not KEY_POINTER.search(line) and not REJECTS.search(line):
                    add("L011", ERROR, lineno,
                        f"{m.group(0)!r} in learner-facing content; answers belong only under "
                        "content/assessment/keys/", extra=m.group(0).lower())

        for m in LINK_RE.finditer(line):
            target = m.group(1)
            if target.startswith(("http://", "https://", "mailto:", "#")) or "<" in target:
                continue
            # Paths containing brackets, such as Next.js "[id]" routes, are
            # percent-encoded in Markdown links.
            if not (path.parent / unquote(target)).resolve().exists():
                add("L015", ERROR, lineno, f"link target does not exist: {target}",
                    extra=target)
    return out


def lint_heading_reuse(corpus: Corpus, active: set[str]) -> list[Finding]:
    """L004 is repo-level: 'is this heading a template artifact?' is not a
    per-file question, and attributing it to one file would blame a module for
    what 445 others did."""
    if "L004" not in active:
        return []
    out = []
    for heading, files in sorted(corpus.heading_census.items(), key=lambda kv: -len(kv[1])):
        if heading in SHARED_HEADINGS or len(files) <= HEADING_REUSE_LIMIT:
            continue
        sample = ", ".join(str(p.relative_to(REPO)) for p in files[:2])
        out.append(Finding(
            "L004", ERROR, MODULES, 1,
            f'heading "{heading}" appears in {len(files)} lesson files (limit '
            f"{HEADING_REUSE_LIMIT}); identical scaffolding forces content into cells where "
            f"it does not fit. e.g. {sample}",
            extra=heading,
        ))
    return out


# --------------------------------------------------------------------------
# Baseline
# --------------------------------------------------------------------------

def load_baseline(path: Path) -> dict[str, dict[str, int]]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("counts", {})


def apply_baseline(findings: list[Finding], baseline: dict) -> tuple[list[Finding], int]:
    """Suppress known pre-existing findings; report new or regressed ones.

    A gate that is red from the day it lands is a gate people learn to ignore.
    The baseline ratchets: deepened modules must not add findings, and the
    numbers fall as remediation lands.
    """
    seen: dict[tuple[str, str], int] = defaultdict(int)
    kept, suppressed = [], 0
    for f in findings:
        seen[(f.rule, f.key)] += 1
        allowed = baseline.get(f.rule, {}).get(f.key, 0)
        if seen[(f.rule, f.key)] <= allowed:
            suppressed += 1
        else:
            kept.append(f)
    return kept, suppressed


def build_baseline(findings: list[Finding]) -> dict:
    counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for f in findings:
        counts[f.rule][f.key] += 1
    return {
        "_comment": (
            "Known pre-existing findings, suppressed so CI fails only on new or "
            "regressed ones. Regenerate with scripts/lint_content.py --update-baseline. "
            "These numbers should only ever go down."
        ),
        "counts": {r: dict(sorted(k.items())) for r, k in sorted(counts.items())},
    }


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

ALL_RULES = [f"L{i:03d}" for i in range(1, 18)]


def in_scope(path: Path, scopes: list[Path]) -> bool:
    return not scopes or any(path == s or s in path.parents for s in scopes)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", type=Path, help="limit to these files or directories")
    ap.add_argument("--rules", help="comma-separated rule IDs, e.g. L001,L002")
    ap.add_argument("--json", action="store_true", dest="as_json")
    ap.add_argument("--baseline", type=Path, default=REPO / "scripts" / "lint_baseline.json")
    ap.add_argument("--no-baseline", action="store_true", help="report every finding")
    ap.add_argument("--update-baseline", action="store_true", help="rewrite the baseline and exit 0")
    args = ap.parse_args(argv)

    active = set(args.rules.split(",")) if args.rules else set(ALL_RULES)
    unknown = active - set(ALL_RULES)
    if unknown:
        print(f"unknown rules: {sorted(unknown)}", file=sys.stderr)
        return 2

    scopes = [p.resolve() for p in args.paths]
    corpus = Corpus.build()
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    findings: list[Finding] = []
    for lesson in corpus.lessons:
        if in_scope(lesson, scopes):
            findings.extend(lint_lesson(lesson, corpus, active))
    for manifest in corpus.manifests:
        if in_scope(manifest, scopes):
            findings.extend(lint_manifest(manifest, schema, active))
    for md in corpus.markdown:
        if in_scope(md, scopes):
            findings.extend(lint_markdown(md, active))
    # Repo-level rules only run on a full-tree lint.
    if not scopes:
        findings.extend(lint_heading_reuse(corpus, active))

    findings.sort(key=lambda f: (f.rel, f.rule, f.line))

    if args.update_baseline:
        args.baseline.write_text(json.dumps(build_baseline(findings), indent=2) + "\n", encoding="utf-8")
        print(f"wrote {args.baseline.relative_to(REPO)} with {len(findings)} findings")
        return 0

    suppressed = 0
    if not args.no_baseline:
        findings, suppressed = apply_baseline(findings, load_baseline(args.baseline))

    errors = [f for f in findings if f.level == ERROR]
    warns = [f for f in findings if f.level == WARN]

    if args.as_json:
        print(json.dumps({
            "findings": [
                {"rule": f.rule, "level": f.level, "path": f.rel, "line": f.line, "message": f.message}
                for f in findings
            ],
            "errors": len(errors), "warnings": len(warns), "suppressed": suppressed,
        }, indent=2))
    else:
        for f in findings:
            print(f.render())
        summary = f"{len(errors)} error(s), {len(warns)} warning(s)"
        if suppressed:
            summary += f", {suppressed} suppressed by baseline"
        print(f"\n{summary}", file=sys.stderr)

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
