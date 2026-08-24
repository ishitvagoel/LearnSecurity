import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import { SiteNav } from "@/components/SiteNav";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: {
    default: "LearnSecurity — Secure Application Engineering",
    template: "%s · LearnSecurity",
  },
  description:
    "First-principles curriculum: security as invariants under adversarial conditions. Local-first progress. Labs stay off this origin.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full`}
    >
      <body className="min-h-full bg-stone-50 font-sans text-stone-900 antialiased">
        <a
          href="#main"
          className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:bg-white focus:px-3 focus:py-2 focus:text-stone-900 focus:outline focus:outline-2 focus:outline-offset-2 focus:outline-blue-800"
        >
          Skip to main content
        </a>
        <SiteNav />
        <main id="main" className="mx-auto w-full max-w-[90rem] flex-1 px-4 py-8 sm:py-10">
          {children}
        </main>
        <footer className="border-t border-stone-300 bg-white px-4 py-6 text-sm text-stone-700">
          <div className="mx-auto max-w-[90rem]">
            Authorized local labs only. Answer keys are not published on this site.
            Blueprint revision 1.1.
          </div>
        </footer>
      </body>
    </html>
  );
}
