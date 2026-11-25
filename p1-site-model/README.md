# P1 site model: Amelia Gorman Park

Base maps, source data and 3D models for the two P1 chipboard pancake models.
This file is the source of truth for model specs; tasks and emails point here.

## Specs (revised 2026-11-09, Zihao)
- **Scale:** 1" = 20' (1:240).
- **Layers:** one 1 ft contour per board, 0.05" thick. The vertical scale is true.
- **Size:** 30" × 30", covering 600 ft square, about 120 ft (half a block) of context around the park.
  Elevation 76 → 200 ft in the frame: 125 layers, about 6.3" tall.
- **Laser bed:** 17.5" × 31.5". Each layer is cut as two 15" × 30" halves joined on one straight seam,
  in the same place on every layer.
- **Material:** Blick All-Purpose Chipboard, 14-ply, 0.05", 28" × 44", item 13115-2226,
  https://www.dickblick.com/items/chipboard-28-x-44-x-14-ply/ ($2.14 at 25+).
- **Park:** about 82 → 192 ft (110 ft rise). Its footprint is about 18" at scale.

**Order for both models** (purchased, from the studio's $1,000 materials fund):

| Item | Qty | Cost |
|---|---|---|
| Chipboard, 28" × 44", item 13115-2226 | 120 sheets (about 56 per model plus waste) | $256.80 |
| Elmer's Glue-All, 16 oz, item 23886-1006 | 8 bottles (beads and dots, not a full spread) | $58.40 |
| Van Aken Plastalina, 4.5 lb, ivory, item 33268-1095 | 6 blocks (27 lb) | $106.62 |
| **Total** before tax and shipping | | **$421.82** |

**Void and inserts:**
- **Void:** an 8" × 8" square (160 ft) inside the park, centered on it and rotated to its long edge (151°, i.e. 29° off the frame). Drawn by `scripts/draw_void.py` on `base-map/gorman_void_30in.svg`, which prints its corners for Rhino.
  Set 2026-11-24 (Zihao). It covers the middle of the slope, and its exact
  position is set in Rhino from the park edges. (At this scale a 6" void covers 120 ft, half the slope;
  a 12" void covers the whole slope but takes about 16 lb of clay and cannot be printed in one piece.)
- **Datum:** the void floor is the top of the base board. Inserts sit flush.
- **Inserts:** oil-based plasticine (Van Aken / Chavant NSP), which is reusable and keeps its size.
  Students fill the insert with scrap, foam or chipboard and sculpt only the top ½" in clay, about 2 lb each.
  The 27 lb order plus leftover clay covers the class. An 8" insert fits a 10" 3D-printer bed.

## Sources
- **Elevation:** USGS 3DEP 1 m DEM, from the `3DEPElevation` ImageServer `exportImage` endpoint, fetched 2026-11-04.
  Units are metres (NAVD88), resampled to 1 ft cells.
- **Context:** © OpenStreetMap contributors, via osmnx, fetched 2026-11-04. Buildings, streets, paths, park boundary.
- **Coordinates:** EPSG:2263 (NY State Plane Long Island, US ft). The model is centered at (1002950, 251037).

## Files
- `base-map/gorman_base_<size>in.svg`: base map at true model size. Each layer is its own group. There's a PNG preview next to it.
- `data/dem_3dep_1010ft.npy`: DEM, 1010 × 1010 cells of 1 ft, values in metres, row 0 = north.
- `data/contours_1ft_<size>in.geojson`: contour lines, with `elev_ft` and `index` (10 ft) attributes.
- `data/{buildings,streets,paths,park}_<size>in.geojson`: OSM context, clipped to the frame.
- `scripts/base_map.py <size> [ft_per_in] [interval_ft] [rot_deg]`: regenerates the maps, the data and the sheet estimate.
  Current set: `base_map.py 22 20 1 29`, a 22" (440 ft) frame turned 29° so its edges follow the park. Rotated outputs
  carry `_rot29` and use local feet with the origin at the frame center; `data/dem_local_22in_rot29.npy` is the frame's
  1 ft elevation grid (row 0 = bottom). The 30" north-up set and the void map stay until the model option is chosen. Run it with the `workflows/osm-map` venv from `workflows/osm-map/`,
  so osmnx reuses its OSM cache there.
- `3d/`: Rhino model, cut sheets, insert template. See [tasks/p1-rhino-model.md](../tasks/p1-rhino-model.md).

## Scoping log (2026-11-04, Zihao + Claude)
This is how the specs were reached. The outcome is in the Specs section above.
1. **Started at 1/16" = 1' with a 1 ft contour per board.** With 100 ft of context the model came to
   about 35" square with 121 layers, and both models needed about 140 sheets. Too big.
2. **1/32" = 1' with a 2 ft contour per board.** That gave a 17.5" model, and a 25" version covered about 800 ft.
   Smaller models make 3D-printed inserts practical, and more context is welcome.
3. **Blick only.** Its 14-ply board is 0.05", not 1/16". At 1/32" = 1' that would mean a 1.6 ft contour.
   Switched to **1" = 40'** so that one board is exactly 2 ft.
4. **Settled on 20" × 20"** (800 ft) rather than 25" (1,000 ft). It fits on one sheet with spare room,
   needs 30 sheets for both models, and the park (about 9") still fits a 10" printer bed.
5. The proposal went to Shahab by email. 6" rotated void and flush datum agreed (see Specs). Still open: the void's exact position
   (see [tasks/p1-site-model.md](../tasks/p1-site-model.md)).
6. **2026-11-09: moved to 1" = 20'.** 3.6" read too short. At 1" = 20' one board is 1 ft, so the model is about 6.3" tall.
   The 17.5" × 31.5" laser bed means stitching layers in any case, so the model went to 30" × 30" (half a block of context).
   Order: 120 sheets, 8 bottles of glue, 27 lb of clay. The void grows to 8" (160 ft) to keep a useful piece of the slope.
