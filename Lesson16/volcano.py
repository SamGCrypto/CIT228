import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
filename ="volcano.json"
with open(filename) as f:
    all_vol_data=json.load(f)

all_vol_dicts =all_vol_data['features']
V_Names, V_Regions, V_Longs, V_Lats =[],[],[],[]

for vol_dict in all_vol_dicts:
    V_Name = vol_dict['properties']['V_Name']
    V_Region = vol_dict['properties']['Country']
    V_Lat = vol_dict['properties']['Latitude'] 
    V_Long = vol_dict['properties']['Longitude'] 
    V_Names.append(V_Name)
    V_Regions.append(V_Region)
    V_Lats.append(V_Lat)
    V_Longs.append(V_Long)



data =[Scattergeo(text=V_Names,lon= V_Longs, lat=V_Lats)]
my_layout = Layout(title="Global Volcanos")

fig={'data':data,'layout':my_layout}
offline.plot(fig, filename='global_volcanos.html')