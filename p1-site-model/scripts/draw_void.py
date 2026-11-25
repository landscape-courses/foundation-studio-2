"""Draw the site-model void on the base map.

Usage (from p1-site-model/): python scripts/draw_void.py [SIDE_IN=8] [DX_FT=0] [DY_FT=0]
Reads base-map/gorman_base_30in.svg and data/park_30in.geojson, writes base-map/gorman_void_30in.svg.
The void is a SIDE_IN square centered on the park, rotated to the park's long axis;
DX/DY shift it in feet (east, north). Prints its corners in EPSG:2263 for the Rhino build.
"""
import sys, math, geopandas as gpd
SIDE = float(sys.argv[1]) if len(sys.argv) > 1 else 8
DX = float(sys.argv[2]) if len(sys.argv) > 2 else 0
DY = float(sys.argv[3]) if len(sys.argv) > 3 else 0
CX, CY, H, FT_PER_IN, PX = 1002950, 251037, 300, 20, 2160   # frame from base_map.py, 30" at 72 px/in

park = gpd.read_file("data/park_30in.geojson").to_crs(2263).geometry.union_all()
rect = list(park.minimum_rotated_rectangle.exterior.coords)
edges = [(math.hypot(b[0]-a[0], b[1]-a[1]), math.atan2(b[1]-a[1], b[0]-a[0])) for a, b in zip(rect, rect[1:])]
ang = max(edges)[1]
c = park.minimum_rotated_rectangle.centroid
ox, oy, s = c.x + DX, c.y + DY, SIDE * FT_PER_IN / 2
u, v = (math.cos(ang), math.sin(ang)), (-math.sin(ang), math.cos(ang))
pts = [(ox + a*s*u[0] + b*s*v[0], oy + a*s*u[1] + b*s*v[1]) for a, b in ((-1,-1),(1,-1),(1,1),(-1,1))]
k = PX / (2 * H)
svgp = " ".join(f"{(x-(CX-H))*k:.1f},{((CY+H)-y)*k:.1f}" for x, y in pts)
src = open("base-map/gorman_base_30in.svg", encoding="utf-8").read()
tag = f'<g id="void"><polygon points="{svgp}" style="fill:none;stroke:#d9703f;stroke-width:6"/></g>\n</svg>'
open("base-map/gorman_void_30in.svg", "w", encoding="utf-8").write(src.replace("</svg>", tag))
print(f"void {SIDE:g}\" = {2*s:.0f} ft, rotation {math.degrees(ang):.1f} deg; corners (EPSG:2263):")
for x, y in pts: print(f"  {x:.1f}, {y:.1f}")
