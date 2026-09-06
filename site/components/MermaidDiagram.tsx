"use client";

import { useEffect, useId, useMemo, useState, type ReactElement } from "react";

function diagramLabel(chart: string): string {
  const line =
    chart
      .split("\n")
      .map((item) => item.trim())
      .find(
        (item) =>
          item &&
          !/^(flowchart|graph|sequenceDiagram|classDiagram|stateDiagram|erDiagram|journey|gantt|pie|gitGraph|mindmap|timeline|quadrantChart|sankey|xychart|block-beta|packet-beta|kanban|architecture-beta)\b/i.test(
            item,
          ),
      ) ?? "Lesson diagram";
  return line.replace(/["[\]]/g, " ").replace(/\s+/g, " ").trim().slice(0, 120);
}

export function MermaidDiagram({ chart }: { chart: string }): ReactElement {
  const reactId = useId().replace(/:/g, "");
  const [svg, setSvg] = useState("");
  const [failed, setFailed] = useState(false);
  const label = useMemo(() => diagramLabel(chart), [chart]);

  useEffect(() => {
    let cancelled = false;
    const run = async (): Promise<void> => {
      try {
        const mermaid = (await import("mermaid")).default;
        mermaid.initialize({
          startOnLoad: false,
          securityLevel: "strict",
          theme: "neutral",
          fontFamily: "ui-sans-serif, system-ui, sans-serif",
        });
        const rendered = await mermaid.render(`mmd-${reactId}`, chart);
        if (!cancelled) {
          setSvg(rendered.svg);
        }
      } catch {
        if (!cancelled) {
          setFailed(true);
        }
      }
    };
    void run();
    return () => {
      cancelled = true;
    };
  }, [chart, reactId]);

  if (failed) {
    return (
      <figure className="lesson-diagram-failed">
        <figcaption>This diagram could not be drawn. The source is shown so you can still read the model.</figcaption>
        <pre className="lesson-diagram">
          <code>{chart}</code>
        </pre>
      </figure>
    );
  }

  if (!svg) {
    return (
      <figure className="lesson-mermaid lesson-mermaid-loading" aria-busy="true" aria-label={label}>
        <p className="sr-only">Loading diagram: {label}</p>
      </figure>
    );
  }

  return (
    <figure
      className="lesson-mermaid"
      role="img"
      aria-label={label}
      dangerouslySetInnerHTML={{ __html: svg }}
    />
  );
}
