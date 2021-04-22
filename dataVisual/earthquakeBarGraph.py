import json
from plotly.graph_objects import Bar, Layout
from plotly import offline

filename = "earthquake.json"
with open(filename, encoding="UTF-8") as f:
    all_equake_data=json.load(f)

all_earthquake_dicts =all_equake_data['features']

e_mag=[]
for i in range(1,5000):
    e_mag.append(all_earthquake_dicts[i]["properties"]["mag"])

frequencies =[]
for value in range(0,10):
    frequency = e_mag.count(value)
    frequencies.append(frequency)

x_values = list(range(0,7))
data = [Bar(x =x_values,y=frequencies)]

x_axis_config={'title':'Magnitutde of Quake','dtick':1}
y_axis_config={'title':'Frequency of Result'}
my_layout=Layout(title="Earthquake Data for the last thirty days", xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='EarthquakeData.html')