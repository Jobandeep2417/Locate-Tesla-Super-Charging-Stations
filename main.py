import folium
import pandas as pd 
from  folium.plugins import MarkerCluster


data= pd.read_excel(r"WRITE THE DATASET PATH.xlsx")
data=pd.DataFrame(data)


longitude=data['Xlongitude']

latitude=data['Ylatitude']
station = data['n_station']

# make a base map

map = folium.Map(location=[47.85183, 3.542802] , zoom_start=10, tiles = "cartodbpositron")

marker_cluster = MarkerCluster().add_to(map)

#Making clusters of Tesla markers

for latitude,longitude,station in zip(latitude,longitude,station):

	icon_path = r"WRITE THE IMAGE PATH.png"

	icon = folium.features.CustomIcon(icon_image=icon_path , icon_size=(30,30))

	folium.Marker(location=[latitude,longitude], popup=str(station) , icon=icon).add_to(marker_cluster)


#save the m


map.save("map.html")