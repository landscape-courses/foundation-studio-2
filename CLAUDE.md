# Landscape Foundation Studio II — course site

Co-taught by **Zihao Zhang** and **Shahab Albahar**. Repo in the `landscape-courses` GitHub org,
served by GitHub Pages at `https://landscape-courses.github.io/foundation-studio-2/` from `main` / root
(`.nojekyll`). Hand-authored static HTML, no build step, no Jekyll. Keep it that way.

## Status: syllabus template
`index.html` is a **template**, built from agentic-design-workflows' syllabus. Every course-specific
slot reads `[TODO: …]` (`grep -n TODO index.html` lists them). First job of the next session: fill
them from course info the instructors provide; ask for whatever is missing rather than inventing it.
Remove each `[TODO]` as it is filled and update this section when none remain.

**Boilerplate is LAAR 61400's, verbatim, and must not change**: Support of Program Mission,
Grading Criteria (prose and grade scale), Classroom Expectations (incl. the Agentic AI course stance),
Support Resources and the footer. Source of truth: `zihaoooo/zihao-site` →
`teaching/laar61400/index.html` (moves to its own landscape-courses repo after Fall 2026). Never
reword these here; if the policy changes, change it in LAAR 61400 first, then copy it across.
The only course-specific slots inside them are TODOs: Attendance's meeting-pattern sentence and the
grade-breakdown weights (bar width = the percentage). Section order follows LAAR 61400.
The side-panel nav has no sections yet; add Projects / Lectures / Workshops as pages are built.

## Working rules (both instructors, every Claude session)
- **Pushing to `main`:** Zihao (repo owner) may push to `main` directly, or ask Claude to. Shahab's sessions work on a branch and open a PR for Zihao to review.
- **Every internal path starts with `/foundation-studio-2/`** (the Pages subpath). A bare `/assets/...`
  breaks on Pages.
- **Self-contained.** CSS, JS, deck system and images live in this repo. Don't hot-link assets from
  zihaozhang.cc or other course repos; copy them in.
- **Public repo.** No grades, student names, rubrics with student data, or student work. Those go in a
  private repo or a shared drive.
- Shared chrome (head, side-panel nav) is duplicated per page by design; propagate nav edits with sed.
- Images: AVIF, long edge ≤1920 (q65). Declare `width`/`height` on every `<img>`, `loading="lazy"`
  below the fold. Keep high-quality originals outside the repo.
- Find-and-replace across HTML: sed via Bash, not PowerShell (it double-encodes UTF-8).
- Credit both instructors on the syllabus and on co-authored lectures.

## Layout
- `assets/css/tokens.css` — every font and color as a variable; pages write `var(--…)`, never a font
  name or hex. `main.css` (syllabus, lecture shells), `workflow-shared.css` (step-by-step workshop
  pages), `footer.css`.
- `assets/js/nav.js` — side-panel nav active state. `wf-progress.js` — workshop step progress.
- `assets/deck/` — slide-deck system (`deck.css`, `deck.js`). **`deck-spec.md` is the spec; read it
  before building or editing any lecture deck.**
- `assets/icons/`, `favicon.ico` — site icons; every page's head links them.
- Planned: `index.html` (syllabus), `lectures/`, `workshops/`, `projects/` (studio briefs),
  `assets/img/<slug>/`. Topic-named files, no week prefixes.

## Reference implementations (read these, then copy patterns)
All public on GitHub:
- **Syllabus:** `zihaoooo/zihao-site` → `teaching/laar61400/index.html` (LAAR 61400, same program).
  Use its `syllabus-section` / `schedule-table` / `grade-breakdown` classes, and copy its policy
  prose (attendance, academic integrity, grading scale, support resources, Agentic AI stance)
  verbatim unless the instructors say otherwise. Studio-specific wording only where facts differ.
- **Lecture pages + side-panel nav:** `landscape-courses/design-research` → `lectures/*.html`.
- **Workshop pages:** `landscape-courses/agentic-design-workflows` → `workshops/coding-101.html`.

## Tasks
`tasks/` holds handoff notes for future sessions, one Markdown file per task with status, context,
steps and a "done when". Check it at the start of a session.
