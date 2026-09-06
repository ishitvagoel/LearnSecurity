import type { ReactElement } from "react";
import Link from "next/link";
import { BrandMark } from "@/components/BrandMark";
import { COURSE_NAV, PRIMARY_NAV, RESOURCE_NAV } from "@/lib/nav";

function FooterGroup({
  title,
  links,
}: {
  title: string;
  links: { href: string; label: string }[];
}): ReactElement {
  return (
    <div>
      <p className="mb-3 text-sm font-medium text-ink">{title}</p>
      <ul className="space-y-2">
        {links.map((link) => (
          <li key={link.href}>
            <Link href={link.href} className="text-muted hover:text-ink hover:underline hover:underline-offset-2">
              {link.label}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function SiteFooter(): ReactElement {
  return (
    <footer className="border-t border-line bg-paper px-4 py-12 text-sm text-muted">
      <div className="mx-auto grid max-w-6xl gap-10 sm:grid-cols-2 lg:grid-cols-4">
        <div>
          <p className="flex items-center gap-2 font-semibold text-ink">
            <BrandMark className="h-7 w-7" />
            LearnSecurity
          </p>
          <p className="mt-3 max-w-xs leading-relaxed">
            A free course in building software that stays safe when someone tries
            to break it. Lessons live here. Practice runs on your computer.
          </p>
        </div>
        <FooterGroup title="Study" links={[{ href: "/", label: "Home" }, ...PRIMARY_NAV]} />
        <FooterGroup title="Reference" links={RESOURCE_NAV} />
        <FooterGroup title="Course" links={COURSE_NAV} />
      </div>
      <p className="mx-auto mt-10 max-w-6xl border-t border-line pt-6 leading-relaxed">
        Practice only on the files in this course, official training apps, or systems
        you have written permission to test. This website does not run broken lab
        apps or publish answer keys. “Visited” checkboxes stay in this browser.
      </p>
    </footer>
  );
}
