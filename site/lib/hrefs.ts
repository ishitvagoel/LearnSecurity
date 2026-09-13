export function moduleHref(id: string): string {
  return `/learn/${encodeURIComponent(id)}/`;
}

export function lessonHref(moduleId: string, filename: string): string {
  const slug = filename.replace(/\.md$/, "");
  return `/learn/${encodeURIComponent(moduleId)}/${encodeURIComponent(slug)}/`;
}

export function assessmentHref(id: string): string {
  return `/assess/${encodeURIComponent(id)}/`;
}
