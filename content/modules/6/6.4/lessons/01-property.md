# A filename is data, not a filesystem object

**Kind:** concept-model
**Loop step:** 1 Property

## The rule

The notes app stores an upload under a lab folder. The **filename is data**. After you join it to the folder and canonicalize, the object must still be that folder. An earlier topic taught data vs interpreter grammar; this week's rule is **which file object** the path parser selected.

> `resolve` must not return a path outside `/tmp/sc-lab`. A `../` name is data that tried to become a different object. This practice checks the prefix and raises; it does not read host files.

What must not happen is **a resolved path that leaves the lab folder**. That is a who-is-allowed failure of *which object*, plus whether the host store stays honest.

Awareness lists name “path walk” as a family. They are not this sentence. Industry lists ask for internally generated names or a hard check on user filenames, uploaded files not run as server code, and an extension that matches the content. Names inside zip files that walk out are a later, harder leftover — not this check. Starlette `UploadFile.filename` is not this sentence.

## Picture: path grammar mixed with data

```mermaid
flowchart TD
  Name[filename as data] --> Mix{join without canonicalize?}
  Mix -->|yes| Other["object outside lab folder"]
  Mix -->|no| Prefix["stays under /tmp/sc-lab"]
```

Who could do this: an uploader who controls a filename field. What is supposed to stop this: local `resolve()` under `/tmp/sc-lab`. Do not open host files outside this practice.

**A tool is not the rule.** A UUID stored name, an antivirus product, or a denylist of `..` is not this sentence.

## Picture: join, canonicalize, then prefix

```mermaid
flowchart LR
  Join[join to root] --> Canon[canonicalize]
  Canon --> Check{under root?}
  Check -->|yes| Allow[Allow]
  Check -->|no| Deny[Deny]
```

Stripping `..` without canonicalize still fails on encodings. UUID names without a prefix check still fail if you later join the original filename.

## Why it happens, what it costs, how you stop it, how you notice, how you recover

| Slice | For this rule |
|---|---|
| Why it happens | Path grammar mixed with data; no canonicalization |
| What has to be true first | `resolve('../outside')` leaves the folder |
| Trigger | User-supplied relative segments |
| What it costs | Who is allowed to pick which file object; the host store can change |
| How you stop it | Join + canonicalize + prefix; random stored names; never run uploads as code |
| How you notice | `path_escape_denied` |
| How you recover | Audit the store; restore |

## What the framework does vs what you still have to check

Starlette `UploadFile.filename` is hostile. FastAPI does not canonicalize for you. Content-Type is a client claim. What this practice is supposed to show: after join and canonicalize, the object is still `/tmp/sc-lab` or a child. The folder is `labs/6.4/6.4-lab`. No live walk against a public upload folder.

## What the tool cannot do

- `.png` allow-lists still fail if a processor parses XML (entity expansion) — leftover you name.
- Zip members, absolute names, UNC, symlink follow — leftover, not this practice.
- Pickle / unsafe YAML / XML entity expansion are other interpreters (same shape as the earlier data-vs-grammar topic).
- Image codecs (memory) wait for a later elective.

## Practice

Treat `../` as a test *name*, not a cookbook to fire at other hosts. Then run:

```text
python3 -m pytest labs/6.4/6.4-lab/tests --impl vulnerable
python3 -m pytest labs/6.4/6.4-lab/tests --impl fixed
```

The first command must fail. The second must pass. Tie the check to a path that left the folder, not to an awareness-list name.

## Use it somewhere new

Clinic scan upload. XML entity expansion; pickle; YAML load.

## What this page is not doing

Live filesystem trophies, zip-bomb cookbooks, dumping lab Python into notes, and treating an awareness list as the definition of security. Answer keys are not on this site.
