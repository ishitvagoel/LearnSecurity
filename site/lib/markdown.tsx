import type { ReactNode } from "react";

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
        <code key={key} className="rounded bg-stone-200 px-1 font-mono text-[0.95em]">
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
            className="text-blue-900 underline"
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
    <div key={key} className="mb-6 overflow-x-auto">
      <table className="w-full min-w-[36rem] border-collapse text-left text-sm">
        <thead>
          <tr>
            {header.map((cell) => (
              <th
                key={cell}
                className="border border-stone-300 bg-stone-100 px-3 py-2 font-semibold"
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
                <td key={ci} className="border border-stone-300 px-3 py-2 align-top">
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

/** Trusted, reviewed Markdown only (curriculum tree). Not MDX. */
export function Markdown({ source }: { source: string }): ReactNode {
  const lines = source.replace(/\r\n/g, "\n").split("\n");
  const nodes: ReactNode[] = [];
  let para: string[] = [];
  let list: { ordered: boolean; items: string[] } | null = null;
  let table: string[] = [];
  let inCode = false;
  let code: string[] = [];
  let quote: string[] = [];

  const flushPara = (): void => {
    if (para.length === 0) {
      return;
    }
    nodes.push(
      <p key={`p-${nodes.length}`} className="mb-4 max-w-prose leading-relaxed">
        {inline(para.join(" "))}
      </p>,
    );
    para = [];
  };
  const flushList = (): void => {
    if (!list || list.items.length === 0) {
      return;
    }
    const Tag = list.ordered ? "ol" : "ul";
    const cls = list.ordered ? "mb-4 list-decimal pl-6" : "mb-4 list-disc pl-6";
    nodes.push(
      <Tag key={`l-${nodes.length}`} className={cls}>
        {list.items.map((item, i) => (
          <li key={i} className="mb-1 max-w-prose">
            {inline(item)}
          </li>
        ))}
      </Tag>,
    );
    list = null;
  };
  const flushTable = (): void => {
    if (table.length === 0) {
      return;
    }
    const node = renderTable(table, `t-${nodes.length}`);
    if (node) {
      nodes.push(node);
    }
    table = [];
  };
  const flushQuote = (): void => {
    if (quote.length === 0) {
      return;
    }
    nodes.push(
      <blockquote
        key={`q-${nodes.length}`}
        className="mb-4 border-l-4 border-stone-400 pl-4 text-stone-800"
      >
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

  for (const line of lines) {
    if (line.startsWith("```")) {
      if (inCode) {
        nodes.push(
          <pre
            key={`pre-${nodes.length}`}
            className="mb-4 overflow-x-auto rounded border border-stone-300 bg-stone-100 p-3 font-mono text-sm"
          >
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
      nodes.push(
        <h1 key={`h1-${nodes.length}`} className="mb-4 text-3xl font-semibold">
          {inline(line.slice(2))}
        </h1>,
      );
      continue;
    }
    if (line.startsWith("## ")) {
      flushFlow();
      nodes.push(
        <h2 key={`h2-${nodes.length}`} className="mb-3 mt-8 text-2xl font-semibold">
          {inline(line.slice(3))}
        </h2>,
      );
      continue;
    }
    if (line.startsWith("### ")) {
      flushFlow();
      nodes.push(
        <h3 key={`h3-${nodes.length}`} className="mb-2 mt-6 text-xl font-semibold">
          {inline(line.slice(4))}
        </h3>,
      );
      continue;
    }
    para.push(line);
  }
  flushFlow();
  return <div className="curriculum-prose">{nodes}</div>;
}
