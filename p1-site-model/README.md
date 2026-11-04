# P1 site model: Amelia Gorman Park

Base maps, source data and 3D models for the two P1 chipboard pancake models.
This file is the source of truth for model specs; tasks and emails point here.

## Specs (proposed 2026-11-04, pending Shahab)
- **Scale:** 1" = 40' (1:480).
- **Layers:** one 2 ft contour per board, 0.05" thick. The vertical scale is true.
- **Material:** Blick All-Purpose Chipboard, 14-ply, 0.05", 28" × 44", item 13115-2226,
  https://www.dickblick.com/items/chipboard-28-x-44-x-14-ply/ ($2.38; $2.14 at 25+).
- **Park:** about 82 → 192 ft (110 ft rise). Its footprint is about 9" × 9" at scale, so it fits a 256 mm printer bed.

| Size | Extent | Elevation (ft) | Layers | Height | Sheets per model (net / +30%) | Order, both models |
|---|---|---|---|---|---|---|
| **20" × 20" (chosen)** | 800 ft | 71 → 210 | 71 + base | 3.6" | 10.8 / 14 | **30 sheets ≈ $64** |
| 25" × 25" | 1,000 ft | 60 → 216 | 78 + base | 4.0" | 19.8 / 26 | 52 sheets ≈ $111 |

Sheet counts add up the area of every layer as a solid sheet. Hollow lower layers and the insert void reduce them.

## Sources
- **Elevation:** USGS 3DEP 1 m DEM, from the `3DEPElevation` ImageServer `exportImage` endpoint, fetched 2026-11-04.
  Units are metres (NAVD88), resampled to 1 ft cells.
- **Context:** © OpenStreetMap contributors, via osmnx, fetched 2026-11-04. Buildings, streets, paths, park boundary.
- **Coordinates:** EPSG:2263 (NY State Plane Long Island, US ft). The model is centered at (1002950, 251037).

## Files
- `base-map/gorman_base_<size>in.svg`: base map at true model size. Each layer is its own group. There's a PNG preview next to it.
- `data/dem_3dep_1010ft.npy`: DEM, 1010 × 1010 cells of 1 ft, values in metres, row 0 = north.
- `data/contours_2ft_<size>in.geojson`: contour lines, with `elev_ft` and `index` (10 ft) attributes.
- `data/{buildings,streets,paths,park}_<size>in.geojson`: OSM context, clipped to the frame.
- `scripts/base_map.py <size>`: regenerates the maps, the data and the sheet estimate.
  Run it with the `workflows/osm-map` venv.
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
5. The proposal went to Shahab by email. Still open: the void outline and the insert datum
   (see [tasks/p1-site-model.md](../tasks/p1-site-model.md)).
