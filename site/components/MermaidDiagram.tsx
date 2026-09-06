"use client";

import { useEffect, useId, useState, type ReactElement } from "react";

export function MermaidDiagram({ chart }: { chart: string }): ReactElement {
  const reactId = useId().replace(/:/g, "");
  const [svg, setSvg] = useState("");
  const [failed, setFailed] = useState(false);

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

  if (failed || !svg) {
    return (
      <pre className="lesson-diagram" aria-hidden={failed ? undefined : true}>
        <code>{chart}</code>
      </pre>
    );
  }

  return (
    <figure
      className="lesson-mermaid"
      role="img"
      aria-label="Lesson diagram"
      dangerouslySetInnerHTML={{ __html: svg }}
    />
  );
}
