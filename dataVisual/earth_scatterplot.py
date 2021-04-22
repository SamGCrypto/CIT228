from plotly.graph_objs import Scattergeo, Layout
import json
from plotly import offline

filename = "earthquake.json"
with open(filename, encoding="UTF-8") as f:
    all_equake_data=json.load(f)

all_earthquake_dicts =all_equake_data['features']

e_mag, e_lon,e_lat=[],[],[]
for eq in all_earthquake_dicts:
    mag=eq["properties"]["mag"]
    lon=eq["geometry"]["coordinates"][0]
    lat=eq["geometry"]["coordinates"][1]
    e_mag.append(mag)
    e_lon.append(lon)
    e_lat.append(lat)

data = [Scattergeo(text= e_mag,lon=e_lon,lat=e_lat)]
my_layout = Layout(title="global Earthquakes")
fig={'data':data,'layout':my_layout}
offline.plot(fig, filename="earthquake_map.html")