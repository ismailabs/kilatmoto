import { mkdir, cp, writeFile, readFile, rm } from "node:fs/promises";
import { execFileSync } from "node:child_process";
import path from "node:path";
const root = path.resolve(import.meta.dirname, "..");
const out = path.join(root, "dist");
if (out !== path.join(root, "dist")) throw new Error("Unsafe output directory");
await rm(out, { recursive: true, force: true });
await mkdir(out, { recursive: true });
for (const entry of [
  "index.html",
  "about",
  "services",
  "projects",
  "contact",
  "assets",
  "favicon.svg",
  "og-image.webp",
  "robots.txt",
  "sitemap.xml",
  "_headers",
])
  await cp(path.join(root, entry), path.join(out, entry), { recursive: true });
const sha = execFileSync("git", ["rev-parse", "HEAD"], {
  cwd: root,
  encoding: "utf8",
}).trim();
const dirty =
  execFileSync("git", ["status", "--porcelain", "--untracked-files=no"], {
    cwd: root,
    encoding: "utf8",
  }).trim() !== "";
await writeFile(
  path.join(out, "release.json"),
  JSON.stringify(
    {
      brand: "KILAT MOTORWORKS",
      repository: "ismailabs/kilatmoto",
      git_sha: sha,
      dirty,
      built_at: new Date().toISOString(),
    },
    null,
    2,
  ) + "\n",
);
await writeFile(
  path.join(out, "_headers"),
  (await readFile(path.join(out, "_headers"), "utf8")).replace(/\r\n/g, "\n").replace(
    "/*\n",
    `/*\n  X-Release-SHA: ${sha}\n`,
  ),
);
console.log(
  `Built controlled static output for ${sha}${dirty ? " (local changes)" : ""}`,
);
