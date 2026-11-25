"""P1 site model base map: OSM context + 2 ft contours from USGS 3DEP.
Usage (from workflows/osm-map venv):  python base_map.py SIZE [FT_PER_IN] [INTERVAL_FT] [ROT_DEG]
  python base_map.py 22 20 1 29   -> 22" x 22" at 1" = 20', 1 ft contours, frame turned 29 deg to the park
ROT_DEG turns the frame counterclockwise so the park's long edge runs level; 0 keeps north up.
Coordinates: local frame in ft, origin at the frame center (EPSG:2263 point cx,cy), x along the
frame's bottom edge. World = (cx,cy) + rotate(local, -ROT_DEG). Elevation ft NAVD88."""
import sys, os, numpy as np, osmnx as ox, geopandas as gpd, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from shapely.geometry import box, LineString
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIZE=float(sys.argv[1]); FT_PER_IN=float(sys.argv[2]) if len(sys.argv)>2 else 20
INTERVAL=float(sys.argv[3]) if len(sys.argv)>3 else 1; BOARD=0.05; SHEET=(28,44)
ROT=float(sys.argv[4]) if len(sys.argv)>4 else 0; th=np.radians(ROT); ct,st=np.cos(th),np.sin(th)
from shapely import affinity
cx,cy=1002950,251037; h=SIZE*FT_PER_IN/2           # model centered on park
dem=np.flipud(np.load(ROOT+"/data/dem_3dep_1010ft.npy")*3.28084)  # 1 ft px, 505 ft half-width, row0 south
n=int(2*h)+1; U,V=np.meshgrid(np.linspace(-h,h,n),np.linspace(-h,h,n))   # local grid, row0 = bottom
C=505+ct*U+st*V; R=505-st*U+ct*V                                         # world px (col east, row north)
c0,r0=np.floor(C).astype(int),np.floor(R).astype(int); fc,fr_=C-c0,R-r0
dem=(dem[r0,c0]*(1-fc)*(1-fr_)+dem[r0,c0+1]*fc*(1-fr_)+dem[r0+1,c0]*(1-fc)*fr_+dem[r0+1,c0+1]*fc*fr_)
cx0,cy0=cx,cy; cx,cy=0,0                                                 # plot in the local frame
xs=np.linspace(-h,h,n); ys=xs
fr=box(-h,-h,h,h); tag=f"{int(SIZE)}in"+(f"_rot{ROT:g}" if ROT else "")
def loc(g): g=g.set_geometry(g.geometry.translate(-cx0,-cy0).rotate(ROT,origin=(0,0))); return g.set_crs(None,allow_override=True) if ROT else g
def get(tags):
    g=ox.features_from_point((40.85570,-73.93240),tags,dist=650).to_crs(2263); g=loc(g); return g[g.intersects(fr)].clip(fr)
bld=get({"building":True}); bld=bld[bld.geom_type.isin(["Polygon","MultiPolygon"])]
park=get({"leisure":"park"}); pk=park[park["name"].fillna("").str.contains("Gorman")]
G=ox.graph_from_point((40.85570,-73.93240),dist=750,network_type="all",simplify=False)
ed=loc(ox.graph_to_gdfs(G,nodes=False).to_crs(2263)); ed=ed[ed.intersects(fr)].clip(fr)
hw=ed["highway"].astype(str)
road=ed[hw.str.contains("primary|secondary|tertiary|residential|unclassified|trunk")]
foot=ed[hw.str.contains("footway|steps|path|pedestrian")]
fig=plt.figure(figsize=(SIZE,SIZE)); ax=fig.add_axes([0,0,1,1]); ax.set_xlim(cx-h,cx+h); ax.set_ylim(cy-h,cy+h); ax.set_aspect(1); ax.axis("off")
z0=np.floor(dem.min()/INTERVAL)*INTERVAL; lv=np.arange(z0,dem.max()+INTERVAL,INTERVAL)
c=ax.contour(xs,ys,dem,levels=[l for l in lv if l%10],colors="#7a6a55",linewidths=0.6); c.set_gid(f"contours_{INTERVAL:g}ft")
ci=ax.contour(xs,ys,dem,levels=[l for l in lv if l%10==0],colors="#3d2f20",linewidths=1.4); ci.set_gid("contours_10ft")
ax.clabel(ci,fmt="%d'",fontsize=9,inline_spacing=2)
bld.plot(ax=ax,facecolor="#d9d3ca",edgecolor="#9a9288",linewidth=0.4,zorder=1.5,gid="buildings")
road.plot(ax=ax,color="#f4f1ec",linewidth=9,zorder=2,gid="streets_casing"); road.plot(ax=ax,color="#b8b0a4",linewidth=0.6,zorder=3,gid="street_centerlines")
foot.plot(ax=ax,color="#3c6e47",linewidth=0.8,linestyle=(0,(3,2)),zorder=4,gid="paths_steps")
pk.boundary.plot(ax=ax,color="#c0392b",linewidth=2,linestyle=(0,(6,3)),zorder=6,gid="park_boundary")
bx,by=cx-h+30,cy-h+30
for i in range(4): ax.add_patch(plt.Rectangle((bx+i*50,by),50,8,color="#222" if i%2==0 else "#fff",ec="#222",zorder=9))
ax.text(bx,by+14,"0",fontsize=10); ax.text(bx+200,by+14,"200 ft",fontsize=10)
nx,ny=-st,ct; ax0,ay0=cx+h-50,cy+h-70
ax.annotate("N",xy=(ax0+30*nx,ay0+30*ny),xytext=(ax0-30*nx,ay0-30*ny),ha="center",fontsize=16,arrowprops=dict(arrowstyle="-|>",color="#222",lw=2))
ax.text(bx,by+40,f"Amelia Gorman Park site model base — 1\" = {FT_PER_IN:g}'  ·  {SIZE:g}\" × {SIZE:g}\" ({2*h:,.0f} ft)  ·  {INTERVAL:g} ft contours (= one 0.05\" 14-ply board), 10 ft index\nElevation: USGS 3DEP 1 m DEM (ft, NAVD88)  ·  Base: © OpenStreetMap contributors  ·  EPSG:2263, frame turned {ROT:g}° to the park",fontsize=10,va="bottom",zorder=9,bbox=dict(fc="white",ec="none",alpha=0.8))
fig.savefig(f"{ROOT}/base-map/gorman_base_{tag}.svg"); fig.savefig(f"{ROOT}/base-map/gorman_base_{tag}_preview.png",dpi=48)
# vector data for Rhino (EPSG:2263 ft)
rows=[]
for cs,lvls in ((c,[l for l in lv if l%10]),(ci,[l for l in lv if l%10==0])):
    for z,segs in zip(lvls,cs.allsegs):
        rows+=[dict(elev_ft=float(z),index=z%10==0,geometry=LineString(s)) for s in segs if len(s)>1]
gpd.GeoDataFrame(rows,crs=None if ROT else 2263).to_file(f"{ROOT}/data/contours_{INTERVAL:g}ft_{tag}.geojson",driver="GeoJSON")
for name,g in (("buildings",bld[["geometry"]]),("streets",road[["geometry"]]),("paths",foot[["geometry"]]),("park",pk[["geometry"]])):
    g.reset_index(drop=True).to_file(f"{ROOT}/data/{name}_{tag}.geojson",driver="GeoJSON")
np.save(f"{ROOT}/data/dem_local_{tag}.npy",dem)   # 1 ft grid of the frame, row0 = bottom
# chipboard estimate: sum of layer areas (1 px = 1 sq ft)
L=len(lv)-1; area_in2=sum((dem>z0+k*INTERVAL).sum() for k in range(L))/FT_PER_IN**2 + SIZE*SIZE
sh=SHEET[0]*SHEET[1]
print(f"{tag}: {2*h:.0f} ft, z {dem.min():.0f}-{dem.max():.0f}, layers {L}+base, height {(L+1)*BOARD:.2f} in, "
      f"net {area_in2/sh:.1f} sheets, x1.3 = {area_in2*1.3/sh:.1f} per model")
