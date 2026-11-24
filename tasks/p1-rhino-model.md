# Task: Build the P1 site model in Rhino from the base map

**Status:** open
**Tools:** Rhino 8 with the Rhino MCP server connected. Python: the `workflows/osm-map` venv (geopandas, osmnx).
**Parent:** [p1-site-model.md](p1-site-model.md) (specs and open decisions).
**Inputs:** `p1-site-model/`. Its [README](../p1-site-model/README.md) holds the scale, size, sources and the file list.

## Goal
Build a Rhino model of the chosen model size: **30" × 30" at 1" = 20'**, one 1 ft contour per board.
It should give the laser-cut layers, the void and the insert template, all from the same data.

## Steps
1. **Units and coordinates.** Set the Rhino file to feet, at real-world size, in EPSG:2263.
   Scale to inches only when exporting the cut sheets (1" = 20').
2. **Import.** Load the vector data from `p1-site-model/data/*_<size>in.geojson`:
   - contours: polylines, with each placed at `elev_ft`
   - buildings, streets, paths and park boundary
   First regenerate the data at 1" = 20' and 30" (see the README); the current files are at 1" = 40'.
   Read the GeoJSON with a Python script through MCP. The SVG is for presentation; trace it only as a fallback,
   and if you do, scale it by its own ft-per-inch from its frame.
   Put each input in its own layer: `contours_1ft`, `contours_10ft`, `buildings`, `streets`, `paths`, `park`, `frame`.
3. **Terrain.** Build a terrain mesh from the contours, or from `data/dem_3dep_1010ft.npy`.
   The DEM is 1 ft cells, values in metres, row 0 = north, 1010 ft square, centered at (1002950, 251037).
   Clip it to the model frame.
4. **Pancake layers.** For each 1 ft level from the base datum up:
   - Make the closed region above that level, clipped to the frame. Each layer is one 0.05" board.
   - Name each layer `L01…`.
   - Add the hollow option: a 2.5" band inside the contour for lower layers whose region is wider than about 8".
5. **Void and insert template.** The spec is in the README: an 8" × 8" square (160 ft), rotated about 28° to the park.
   - Place it inside the park on the slope, using the park edges. Confirm the position with Zihao.
   - Cut the void through all layers above the base board. The void floor is the top of the base.
   - Export the boundary heights as an **edge template**, plus a `.stl` of the void volume for 3D printers.
6. **Buildings.** Make them simple extrusions, on their own layer, for presentation. They are not part of the cut set.
7. **Cut sheets.** Split each layer into two 15" × 30" halves on one straight seam, the same on every layer,
   so each piece fits the 17.5" × 31.5" laser bed. Nest them onto 28" × 44" sheets at 1" = 20':
   - cut lines red, etch lines blue
   - etch the layer number and a registration mark on each layer
   Make two full sets. Count the sheets and compare with the README estimate.
8. **Export** into `p1-site-model/3d/`:
   - `gorman_site_<size>in.3dm`
   - `insert_template_<size>in.3dm` and `.stl`
   - laser `.dxf` per sheet, in a `cut-sheets/` subfolder

   Large exports go to the shared drive; link them in the README instead.

## Done when
- The `.3dm`, the cut sheets and the insert template are in `3d/` or on the shared drive, and linked.
- The sheet count is recorded in the README.
- The parent task is updated.
