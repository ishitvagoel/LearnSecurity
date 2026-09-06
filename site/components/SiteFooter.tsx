import type { ReactElement } from "react";
import Link from "next/link";
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
      <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-stone-500">{title}</p>
      <ul className="space-y-1.5">
        {links.map((link) => (
          <li key={link.href}>
            <Link href={link.href} className="text-stone-800 underline-offset-2 hover:underline">
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
    <footer className="border-t border-stone-300 bg-white px-4 py-10 text-sm text-stone-700">
      <div className="mx-auto grid max-w-[90rem] gap-8 sm:grid-cols-2 lg:grid-cols-4">
        <div>
          <p className="font-semibold text-stone-900">LearnSecurity</p>
          <p className="mt-2 max-w-xs leading-relaxed">
            A first-principles course in keeping named properties true under attack.
            Blueprint revision 1.1.
          </p>
        </div>
        <FooterGroup title="Study" links={PRIMARY_NAV} />
        <FooterGroup title="Reference" links={RESOURCE_NAV} />
        <FooterGroup title="Course" links={COURSE_NAV} />
      </div>
      <p className="mx-auto mt-8 max-w-[90rem] border-t border-stone-200 pt-6 text-stone-600">
        Authorized local labs only. This origin does not run vulnerable fixtures or
        publish examiner keys. Progress checkboxes stay in this browser.
      </p>
    </footer>
  );
}
