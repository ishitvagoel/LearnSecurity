import type { ReactNode } from "react";
import {
  createIdAllocator,
  plainHeadingText,
  sectionClassName,
  sectionKindFromHeading,
  type LessonSectionKind,
} from "./headings";

function safeHref(href: string): string | null {
  const trimmed = href.trim();
  if (trimmed.startsWith("/") && !trimmed.startsWith("//") && !trimmed.includes("://")) {
    return trimmed;
  }
  try {
    const url = new URL(trimmed);
    if (url.protocol === "https:" || url.protocol === "http:") {
      return url.toString();
    }
  } catch {
    return null;
  }
  return null;
}

function inline(text: string): ReactNode[] {
  const nodes: ReactNode[] = [];
  const re = /(\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))/g;
  let last = 0;
  let key = 0;
  let match: RegExpExecArray | null = re.exec(text);
  while (match) {
    if (match.index > last) {
      nodes.push(text.slice(last, match.index));
    }
    const token = match[0];
    if (token.startsWith("**")) {
      nodes.push(<strong key={key}>{token.slice(2, -2)}</strong>);
    } else if (token.startsWith("`")) {
      nodes.push(
        <code key={key} className="rounded bg-stone-200/80 px-1 py-0.5 font-mono text-[0.9em]">
          {token.slice(1, -1)}
        </code>,
      );
    } else {
      const link = /^\[([^\]]+)\]\(([^)]+)\)$/.exec(token);
      const href = link ? safeHref(link[2]) : null;
      if (link && href) {
        const external = href.startsWith("http");
        nodes.push(
          <a
            key={key}
            href={href}
            className="text-blue-900 underline decoration-blue-900/30 underline-offset-2 hover:decoration-blue-900"
            {...(external ? { rel: "noreferrer", target: "_blank" } : {})}
          >
            {link[1]}
          </a>,
        );
      } else {
        nodes.push(token);
      }
    }
    key += 1;
    last = match.index + token.length;
    match = re.exec(text);
  }
  if (last < text.length) {
    nodes.push(text.slice(last));
  }
  return nodes;
}

function isSeparatorRow(line: string): boolean {
  return /^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(line);
}

function splitRow(line: string): string[] {
  const trimmed = line.trim().replace(/^\|/, "").replace(/\|$/, "");
  return trimmed.split("|").map((c) => c.trim());
}

function renderTable(rows: string[], key: string): ReactNode {
  const body = rows.filter((r) => !isSeparatorRow(r)).map(splitRow);
  if (body.length === 0) {
    return null;
  }
  const header = body[0];
  const rest = body.slice(1);
  return (
    <div key={key} className="mb-5 overflow-x-auto rounded-lg border border-stone-200">
      <table className="w-full min-w-[32rem] border-collapse text-left text-sm">
        <thead>
          <tr>
            {header.map((cell) => (
              <th
                key={cell}
                className="border-b border-stone-200 bg-stone-100 px-3 py-2 font-semibold text-stone-900"
              >
                {inline(cell)}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {rest.map((row, ri) => (
            <tr key={ri} className="odd:bg-white even:bg-stone-50">
              {row.map((cell, ci) => (
                <td key={ci} className="border-t border-stone-100 px-3 py-2 align-top text-stone-800">
                  {inline(cell)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function isMechanismAside(text: string): boolean {
  return text.startsWith("**Mechanism (not the property):**");
}

/** Trusted, reviewed Markdown only (curriculum tree). Not MDX. */
export function Markdown({ source }: { source: string }): ReactNode {
  const lines = source.replace(/\r\n/g, "\n").split("\n");
  const nodes: ReactNode[] = [];
  const alloc = createIdAllocator();
  let para: string[] = [];
  let list: { ordered: boolean; items: string[] } | null = null;
  let table: string[] = [];
  let inCode = false;
  let code: string[] = [];
  let quote: string[] = [];
  let seq = 0;
  let section: {
    kind: LessonSectionKind;
    headingId: string;
    headingText: string;
    children: ReactNode[];
  } | null = null;

  const nextKey = (prefix: string): string => {
    seq += 1;
    return `${prefix}-${seq}`;
  };

  const pushNode = (node: ReactNode): void => {
    if (section) {
      section.children.push(node);
      return;
    }
    nodes.push(node);
  };

  const flushSection = (): void => {
    if (!section) {
      return;
    }
    const current = section;
    section = null;
    nodes.push(
      <section
        key={nextKey("sec")}
        className={sectionClassName(current.kind)}
        aria-labelledby={current.headingId}
      >
        <h2 id={current.headingId} className="lesson-h2 mt-0">
          {inline(current.headingText)}
        </h2>
        {current.children}
      </section>,
    );
  };

  const flushPara = (): void => {
    if (para.length === 0) {
      return;
    }
    const text = para.join(" ");
    para = [];
    if (isMechanismAside(text)) {
      pushNode(
        <aside key={nextKey("mech")} className="lesson-mechanism">
          {inline(text)}
        </aside>,
      );
      return;
    }
    pushNode(
      <p key={nextKey("p")} className="lesson-p">
        {inline(text)}
      </p>,
    );
  };

  const flushList = (): void => {
    if (!list || list.items.length === 0) {
      return;
    }
    const Tag = list.ordered ? "ol" : "ul";
    const cls = list.ordered ? "lesson-ol" : "lesson-ul";
    pushNode(
      <Tag key={nextKey("l")} className={cls}>
        {list.items.map((item, i) => (
          <li key={i}>{inline(item)}</li>
        ))}
      </Tag>,
    );
    list = null;
  };

  const flushTable = (): void => {
    if (table.length === 0) {
      return;
    }
    const node = renderTable(table, nextKey("t"));
    if (node) {
      pushNode(node);
    }
    table = [];
  };

  const flushQuote = (): void => {
    if (quote.length === 0) {
      return;
    }
    pushNode(
      <blockquote key={nextKey("q")} className="lesson-quote">
        {inline(quote.join(" "))}
      </blockquote>,
    );
    quote = [];
  };

  const flushFlow = (): void => {
    flushPara();
    flushList();
    flushTable();
    flushQuote();
  };

  const startHeading = (level: 2 | 3, raw: string): void => {
    flushFlow();
    const kind = level === 2 ? sectionKindFromHeading(raw) : null;
    if (level === 2) {
      flushSection();
    }
    if (kind) {
      section = {
        kind,
        headingId: alloc(plainHeadingText(raw)),
        headingText: raw,
        children: [],
      };
      return;
    }
    const Tag = level === 2 ? "h2" : "h3";
    const cls = level === 2 ? "lesson-h2" : "lesson-h3";
    pushNode(
      <Tag key={nextKey("h")} id={alloc(plainHeadingText(raw))} className={cls}>
        {inline(raw)}
      </Tag>,
    );
  };

  for (const line of lines) {
    if (line.startsWith("```")) {
      if (inCode) {
        pushNode(
          <pre key={nextKey("pre")} className="lesson-pre">
            <code>{code.join("\n")}</code>
          </pre>,
        );
        code = [];
        inCode = false;
      } else {
        flushFlow();
        inCode = true;
      }
      continue;
    }
    if (inCode) {
      code.push(line);
      continue;
    }
    if (line.trim() === "") {
      flushFlow();
      continue;
    }
    if (line.startsWith("|")) {
      flushPara();
      flushList();
      flushQuote();
      table.push(line);
      continue;
    }
    if (table.length) {
      flushTable();
    }
    if (line.startsWith("> ")) {
      flushPara();
      flushList();
      quote.push(line.slice(2));
      continue;
    }
    if (quote.length) {
      flushQuote();
    }
    const ol = line.match(/^\d+\.\s+(.*)$/);
    if (ol) {
      flushPara();
      if (!list || !list.ordered) {
        flushList();
        list = { ordered: true, items: [] };
      }
      list.items.push(ol[1]);
      continue;
    }
    if (line.startsWith("- ")) {
      flushPara();
      if (!list || list.ordered) {
        flushList();
        list = { ordered: false, items: [] };
      }
      list.items.push(line.slice(2));
      continue;
    }
    if (list) {
      flushList();
    }
    if (line.startsWith("# ")) {
      flushFlow();
      flushSection();
      pushNode(
        <h1 key={nextKey("h1")} className="lesson-h1">
          {inline(line.slice(2))}
        </h1>,
      );
      continue;
    }
    if (line.startsWith("## ")) {
      startHeading(2, line.slice(3));
      continue;
    }
    if (line.startsWith("### ")) {
      startHeading(3, line.slice(4));
      continue;
    }
    para.push(line);
  }
  flushFlow();
  flushSection();
  return <div className="curriculum-prose">{nodes}</div>;
}
