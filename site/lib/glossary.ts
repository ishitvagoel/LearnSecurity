export type GlossaryTerm = { term: string; def: string };

const RAW_TERMS: GlossaryTerm[] = [
  {
    term: "Rule (invariant)",
    def: "A promise the software must keep, written so another person could check it. Example: “People in company A cannot read company B’s notes.” If you cannot write a test for it, it is still a slogan.",
  },
  {
    term: "Tool (mechanism)",
    def: "A setting or library — encryption, a login package, a scanner, a cloud checkbox. These may help. They are not the same as the rule you are trying to keep.",
  },
  {
    term: "Check every path (complete mediation)",
    def: "Every path gets the same check: the website, the export, the retry, the background job. A skipped path means the rule is already broken.",
  },
  {
    term: "Fail closed (fail-safe defaults)",
    def: "If the app is unsure — expired login, missing setting, failed check — it says no. Being busy is not a reason to skip the check.",
  },
  {
    term: "What you trust (trusted computing base)",
    def: "The pieces of the system you are betting on for a given rule. A page in the browser, and a phone app someone can copy, are usually not on that list.",
  },
  {
    term: "Confused deputy",
    def: "A powerful part of the app that does what a caller asks (open this note, fetch this URL) without checking whether that caller is allowed to.",
  },
  {
    term: "What can still go wrong (residual risk)",
    def: "What still goes wrong if the main protection fails. Say how you would notice, how you would recover, and who still gets hurt. A checkbox on a form is not that sentence.",
  },
  {
    term: "Authorized lab",
    def: "Practice you are allowed to run: a local course app, an official training target, a challenge whose published rules allow it, or a system with written permission. This website is none of those. It does not run the broken apps.",
  },
  {
    term: "The notes app (SecureCollab)",
    def: "The small notes app the course keeps extending: teams, members, notes, later files and sharing. Write rules about this app, not about a vague slogan like “keep it confidential.”",
  },
  {
    term: "Injected commands (SQL injection)",
    def: "Typed-in text gets pasted straight into a database command instead of being treated as data. If someone can type a value that changes what the database does, the app is building commands out of raw text, not parameters.",
  },
  {
    term: "A page that runs someone else’s script (cross-site scripting, XSS)",
    def: "Text one person typed — a note, a comment, a name — gets shown to someone else’s browser and runs as code instead of being displayed as words. The fix is escaping what you show, not just filtering what you accept.",
  },
  {
    term: "A click that isn’t really a click (cross-site request forgery, CSRF)",
    def: "A form on another website quietly submits to your app using a browser cookie that is still logged in. The user never agreed to the action; the browser just carried the cookie along for the ride.",
  },
  {
    term: "The server fetching a trap (server-side request forgery, SSRF)",
    def: "Your server — not a user’s browser — gets tricked into requesting a URL it should not, such as the cloud provider’s internal metadata address, because a feature accepts “any URL” from the user.",
  },
  {
    term: "Climbing out of the folder (path traversal)",
    def: "A file name like `../../etc/passwd` is used to read or write outside the folder a feature was supposed to be limited to.",
  },
  {
    term: "A logged-in send-anywhere (open redirect)",
    def: "A link on your own site forwards the browser to whatever URL a query parameter names, so it can be dressed up to look trustworthy while actually pointing somewhere else.",
  },
  {
    term: "Editing fields nobody offered you (mass assignment)",
    def: "An API takes a whole JSON object and writes every field straight onto a record, so a user can set a field like `isAdmin: true` even though no screen ever showed that field.",
  },
  {
    term: "Someone else’s object, same-shaped URL (broken object-level authorization)",
    def: "Changing an id in a URL or request — `/notes/104` to `/notes/105` — returns another person’s data, because the server checked that you were logged in, not that you owned that specific note.",
  },
  {
    term: "An old login that still works (session fixation)",
    def: "An attacker hands a victim a session id before they log in. If the app keeps using that same id afterward, the attacker is now logged in too.",
  },
  {
    term: "Only the permission the task needs (least privilege)",
    def: "A person, service, or job gets the smallest set of permissions that lets it do its actual work — not admin access “to be safe,” which just makes a later mistake more expensive.",
  },
  {
    term: "More than one lock on the door (defense in depth)",
    def: "Assume any single check will eventually fail or get bypassed, so a second, independent check still catches the problem. Never rely on one gate to hold forever.",
  },
  {
    term: "Writing down who might attack (threat model)",
    def: "A short, specific list of who might attack this feature, what they can already do, and what they would try — written before you design the fix, not after a bug report.",
  },
  {
    term: "A signed claim about who you are (JSON Web Token, JWT)",
    def: "A compact, signed piece of text a server hands out after login, which a client sends back on later requests. Signed does not mean secret: anyone can read the contents, they just cannot forge a new one without the key.",
  },
  {
    term: "Telling the browser what a page may load (Content Security Policy, CSP)",
    def: "A header that limits which scripts, images, and connections a page is allowed to load, so an injected script has fewer places left to run or send stolen data.",
  },
  {
    term: "Letting another site’s page call your API (Cross-Origin Resource Sharing, CORS)",
    def: "A header-based handshake that decides whether a script running on someone else’s website is allowed to read your API’s response from inside a user’s browser.",
  },
  {
    term: "Slowing down repeat requests (rate limiting)",
    def: "Capping how many times a person or address can hit a sensitive action — login, password reset, an expensive search — in a given window, so guessing or scraping stops being free.",
  },
  {
    term: "Reading two things that changed in between (race condition)",
    def: "Code checks that something is true, then acts on it later — but between the check and the act, another request changed the thing, so the check no longer means anything.",
  },
  {
    term: "Turning stored data back into a live object (insecure deserialization)",
    def: "Loading a saved blob — a cookie, a cache entry, an uploaded file — directly back into a program object, without checking that the blob cannot be crafted to run code the moment it loads.",
  },
  {
    term: "Trusting your dependencies’ dependencies (supply chain risk)",
    def: "A library you did not write pulls in more libraries you have never heard of. A compromise in any one of them ships inside your app the next time someone installs it.",
  },
  {
    term: "Same account, different teams (multi-tenancy)",
    def: "One running copy of the app serves many separate customers or companies at once. Every query needs a company check, or one customer’s data leaks into another’s screen.",
  },
];

export const GLOSSARY_TERMS: GlossaryTerm[] = [...RAW_TERMS].sort((a, b) =>
  a.term.localeCompare(b.term),
);
