# Task: P1 site model base file and laser-cut file

**Status:** open
**Tools:** Rhino MCP (Rhino 8). Run this session on a machine with Rhino and the Rhino MCP server connected.
**Owner:** Zihao prepares the base file for students; this task is that preparation.

## Context
Foundation Studio II, Spring 2027. Two projects of 14 sessions each, sharing a conceptual spine
(movement and choreography, A to B; each project has a dominant axis, not an exclusive one).

- **P1 Vertical** (S01 to S14, Thu 1/28 to Mon 3/22): Amelia Gorman Park, a very steep hill rising from
  Broadway to Wadsworth Terrace, between West 189th and West 190th Streets, Manhattan. Students design
  and choreograph a vertical movement through landform and tectonics.
- P2 Horizontal (S15 to S28): St. Nicholas Ave, 110th to 125th. No physical model required.

## Model concept (decided)
- **Two identical site models**, one built by each section (9 to 10 students each).
- **Pancake model in chipboard**: stacked contour layers.
- **Existing topography of the design zone is cut out as a void.** Students design their own topo as an
  **insert** that plugs into the void during reviews.
- Inserts: 3D printed, hand-built or laser-cut. At least one per student at the midterm (S14);
  more iterations welcome. Both models sit side by side at the S12 pin-up and S14 midterm, and any
  insert must fit either model.
- Schedule: sections receive the file at S02 to S03 and build the model at S04 to S06.
  **Files must be ready before S02 (Mon 2/1/2027).**

## Open specs (decide first, with the instructors)
1. **Scale and contour interval.** Chipboard thickness sets the interval (e.g. 1/16" ≈ 1.5 mm per
   layer). Derive the scale from the total rise, Broadway to Wadsworth Terrace, and the laser bed size.
2. **Void footprint.** Whole park or a defined zone; rectilinear or following site lines. A simple
   outline makes inserts easier to fabricate.
3. **Interface rule.** Inserts match the void outline and meet the boundary contour heights.
   Provide a laser-cut **edge template** (frame plus boundary elevations) so all fabrication methods fit.
4. **Base datum.** Fixed insert bottom elevation, so every insert seats at the same depth.
5. Model extents (how much context beyond the park: streets, buildings, stairs to Wadsworth).

## Proposed specs
Recorded in [p1-site-model/README.md](../p1-site-model/README.md): 1" = 40', 2 ft per 0.05" board, 20" × 20" model,
30 Blick sheets for both. Rhino build: [p1-rhino-model.md](p1-rhino-model.md).

## Steps
1. Source data: NYC Open Data / NYC DoITT 1 ft contours or the topobathy DEM, plus building
   footprints and street centerlines. Record source and date.
2. In Rhino via MCP: set units, import and clip the data to the model extents, rebuild contours at the
   chosen interval.
3. Define the void boundary and the insert frame; generate the edge template.
4. Lay out the cut sheets: one curve per layer, nested to the sheet size, with layer numbers etched;
   cut (red) and etch (blue) on separate layers per the model shop's laser spec. Two full sets (one per section).
5. Export: `.3dm` base file, laser `.dxf`/`.ai` per sheet, and an insert-template `.3dm` plus `.stl`
   of the void for 3D printers.
6. Write a one-page build guide (sheet order, stacking, gluing, void, insert rules).

## Where the outputs go
- Large CAD/fabrication files: **shared drive**, not this repo (keep the repo light; it's public).
- In this repo: link to the files and the build guide/insert rules in the P1 brief
  (`projects/vertical.html`, to be built). Diagrams as AVIF per CLAUDE.md.

## Done when
Specs 1 to 5 are decided and recorded here, both cut sets and the insert template are exported and
shared, the build guide is written, and this file's status is set to done.
