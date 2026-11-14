# Landscape Foundation Studio II

A landscape studio co-taught by Zihao Zhang and Shahab Albahar, in two projects of 14 sessions
each on movement and choreography: P1 Move Vertically (Amelia Gorman Park) and P2 Move Horizontally
(St. Nicholas Ave, 110th to 125th). Credit both instructors on the syllabus and on co-authored lectures.

Public repo in the `landscape-courses` org, served by GitHub Pages from `main` at
`https://landscape-courses.github.io/foundation-studio-2/`. Hand-authored static HTML.

**Semester:** Spring 2027, Monday and Thursday. First class (S01): Thu 2027-01-28. Before that date
the course is in pre-semester prep; from it, count the teaching week from today's date. Session
dates live in `index.html`.

## How prep works
The instructors prepare by talking, often from a phone. State lives in `weeks/` so every session
starts from the files.

- `weeks/00-course.md` holds the whole course: frame, schedule, projects, grading.
  `weeks/week-NN.md` holds one week's sessions, created when that week is first discussed. Each
  has three sections: **Open** (raised, awaiting a decision), **Decided** (conclusions),
  **To build** (decided, and the page has yet to show it).
- Pre-semester, talk defaults to `00-course.md` and the syllabus is free to change. In semester,
  talk defaults to the coming week's file, and a change to the syllabus is raised on its own for a yes.

**Discuss (议)** is the default for any message about course content.
- Read the file first. A passing thought goes into Open with its date and who raised it, answered
  in one line.
- Each decision is restated in one sentence, written to Decided, committed and pushed at once, so
  the session can end at any moment with everything settled already saved.
- Replies fit a phone: one question at a time, a few lines, numbered options.
- Discuss edits `weeks/` only. Close by naming what sits in To build.
- Course facts come from the instructors; ask for what is missing.
- Grades, student names and student work belong in a private repo or shared drive.

**Build (建)** starts when an instructor says build, in a fresh session.
- Read the file's Decided and To build, and `assets/deck/deck-spec.md` for a lecture deck. Make the
  page, push, reply with its live URL, and empty To build.

`tasks/` holds work orders that belong to no week, such as the P1 site model; each states its
status, steps and what done means.

## Repo rules
- Both instructors push to `main`, directly or through Claude. Use a branch and PR to get the
  other's review first.
- Every internal path starts with `/foundation-studio-2/`, the Pages subpath.
- The repo is self-contained: CSS, JS, deck system and images are copied in.
- Head and side-panel nav are inline in every page, so a nav edit goes to all pages in one pass.
  Add nav sections (Projects, Lectures, Workshops) as pages are built.
- Run find-and-replace across HTML with sed in Bash; PowerShell double-encodes UTF-8.
- Colors and fonts are variables in `assets/css/tokens.css`; pages write `var(--…)`.
- Images: AVIF q65, long edge ≤1920, `width`/`height` on every `<img>`, `loading="lazy"` below the
  fold, in `assets/img/<slug>/`. Originals stay outside the repo.
- Pages are topic-named: `lectures/`, `workshops/`, `projects/` (studio briefs).

## Syllabus (`index.html`)
- Course-specific slots still read `[TODO: …]`; `grep -n TODO index.html` lists them.
- Policy prose is LAAR 61400's, verbatim: Support of Program Mission, Grading Criteria and scale,
  Classroom Expectations with the Agentic AI stance, Support Resources, the footer, in LAAR 61400's
  section order. Source: `zihaoooo/zihao-site` → `teaching/laar61400/index.html`. A policy change
  is made there first, then copied here. The course-specific parts are Attendance's meeting-pattern
  sentence and the grade-breakdown weights (bar width = the percentage).

## Patterns to copy
- Lecture pages and nav: `landscape-courses/design-research` → `lectures/*.html`.
- Week and workshop pages: `landscape-courses/agentic-design-workflows` → `workshops/SPEC.md` and
  `workshops/folders-and-claude.html`; copy the spec in with the first such page.
- On Zihao's machine these sit beside this repo (`../agentic-design-workflows/`, `../../zihao-site/`).
