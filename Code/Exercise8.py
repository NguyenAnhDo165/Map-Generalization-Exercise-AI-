#Bài 8:
import folium
from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx

start = input("Vui lòng nhập điểm đi: ")
destination = input("Vui lòng nhập điểm đến: ")
geolocator = Nominatim(user_agent="routing-example", timeout=10)
viewbox_hcmc = ((10.0, 106.0), (11.0, 107.0))
diemdi = geolocator.geocode(start, viewbox=viewbox_hcmc, bounded=True)
if diemdi:
  toadodiemdi = (diemdi.latitude, diemdi.longitude)
else:
   print(f"Không tìm thấy tọa độ điểm đi!")
diemden = geolocator.geocode(destination, viewbox=viewbox_hcmc, bounded=True)
if diemden:
  toadodiemden = (diemden.latitude, diemden.longitude)
else:
   print(f"Không tìm thấy tọa độ điểm đến!")

m = folium.Map(location=toadodiemdi, zoom_start=15)

G = ox.graph_from_point(toadodiemdi, dist=15000, network_type="drive")

batdau = ox.distance.nearest_nodes(G, toadodiemdi[1], toadodiemdi[0])
ketthuc = ox.distance.nearest_nodes(G, toadodiemden[1], toadodiemden[0])
duongdi = nx.shortest_path(G, batdau, ketthuc, weight="length")
toadoduongdi = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in duongdi]
folium.PolyLine(toadoduongdi, color="blue", weight=2.5, opacity=1).add_to(m)

folium.Marker(toadodiemdi,icon=folium.Icon(color='blue',icon='home'), popup="Điểm đi").add_to(m)
folium.Marker(toadodiemden,icon=folium.Icon(color='red'), popup="Điểm đến").add_to(m)

m