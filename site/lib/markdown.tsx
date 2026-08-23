import type { ReactNode } from "react";

function inline(text: string): ReactNode[] {
  const parts = text.split(/(\*\*[^*]+\*\*|`[^`]+`)/g);
  return parts.map((part, i) => {
    if (part.startsWith("**") && part.endsWith("**")) {
      return <strong key={i}>{part.slice(2, -2)}</strong>;
    }
    if (part.startsWith("`") && part.endsWith("`")) {
      return (
        <code key={i} className="rounded bg-stone-200 px-1 font-mono text-[0.95em]">
          {part.slice(1, -1)}
        </code>
      );
    }
    return <span key={i}>{part}</span>;
  });
}

/** Trusted, reviewed Markdown only (curriculum tree). Not MDX. */
export function Markdown({ source }: { source: string }): ReactNode {
  const lines = source.replace(/\r\n/g, "\n").split("\n");
  const nodes: ReactNode[] = [];
  let para: string[] = [];
  let list: string[] = [];
  let inCode = false;
  let code: string[] = [];

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
    if (list.length === 0) {
      return;
    }
    nodes.push(
      <ul key={`ul-${nodes.length}`} className="mb-4 list-disc pl-6">
        {list.map((item, i) => (
          <li key={i} className="mb-1 max-w-prose">
            {inline(item)}
          </li>
        ))}
      </ul>,
    );
    list = [];
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
        flushPara();
        flushList();
        inCode = true;
      }
      continue;
    }
    if (inCode) {
      code.push(line);
      continue;
    }
    if (line.trim() === "") {
      flushPara();
      flushList();
      continue;
    }
    if (line.startsWith("# ")) {
      flushPara();
      flushList();
      nodes.push(
        <h1 key={`h1-${nodes.length}`} className="mb-4 text-3xl font-semibold">
          {inline(line.slice(2))}
        </h1>,
      );
      continue;
    }
    if (line.startsWith("## ")) {
      flushPara();
      flushList();
      nodes.push(
        <h2 key={`h2-${nodes.length}`} className="mb-3 mt-8 text-2xl font-semibold">
          {inline(line.slice(3))}
        </h2>,
      );
      continue;
    }
    if (line.startsWith("### ")) {
      flushPara();
      flushList();
      nodes.push(
        <h3 key={`h3-${nodes.length}`} className="mb-2 mt-6 text-xl font-semibold">
          {inline(line.slice(4))}
        </h3>,
      );
      continue;
    }
    if (line.startsWith("|")) {
      flushPara();
      flushList();
      nodes.push(
        <p key={`tbl-${nodes.length}`} className="mb-2 max-w-prose font-mono text-sm">
          {line}
        </p>,
      );
      continue;
    }
    if (line.startsWith("- ")) {
      flushPara();
      list.push(line.slice(2));
      continue;
    }
    para.push(line);
  }
  flushPara();
  flushList();
  return <div className="curriculum-prose">{nodes}</div>;
}
