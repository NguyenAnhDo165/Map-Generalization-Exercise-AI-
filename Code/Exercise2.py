#Bài 2
import folium
from geopy.geocoders import Nominatim
import osmnx as ox
import networkx as nx

#Lấy địa chỉ cụ thể
trungtam = (10.76117635724359, 106.6683304626097) #Đại học Kinh tế TP.HCM cơ sở B
vidotrungtam, kinhdotrungtam = trungtam[0], trungtam[1]
diachi1 = "Nhà thờ Đức Bà"
diachi2 = "Công viên Đầm Sen"
diachi3 = "Cầu Ba Son"
diachi4 = "Công viên Lê Thị Riêng"
diachi5 = "Chợ Bến Thành"
diachi6 = "The Global City, Ho Chi Minh City"
diachi7 = "Sân bay Tân Son Nhất"
diachi8 = "Chợ hoa Hồ Thị Kỷ"
diachi9 = "Phố đi bộ Bùi Viện"
diachi10 = "Công viên Sala"
diachi = [diachi1,diachi2,diachi3,diachi4,diachi5,diachi6,diachi7,diachi8,diachi9,diachi10]

# Tạo graph
G = ox.graph_from_point(trungtam, dist=15000, network_type="drive")

# Tạo map
m = folium.Map(location=trungtam, zoom_start=13)

# Chuyển đổi sang tọa độ địa lý
geolocator = Nominatim(user_agent="routing-example", timeout=10)
diem = []
viewbox_hcmc = ((10.0, 106.0), (11.0, 107.0))
for i in diachi:
  location = geolocator.geocode(i, viewbox=viewbox_hcmc, bounded=True)
  if location:
    vido = location.latitude
    kinhdo = location.longitude
    toado = (vido,kinhdo)
    diem.append(toado)
  else:
    print(f"Could not find coordinates for {i} within HCMC bounds.")

# Tạo marker cho các điểm
for i, coord in enumerate(diem):
    folium.Marker(location=coord,popup=diachi[i],icon=folium.Icon(color='blue')).add_to(m)

# Tìm quãng đường ngắn nhất
diemtrungtam = ox.distance.nearest_nodes(G, kinhdotrungtam, vidotrungtam)

for j in diem:
  diemden = ox.distance.nearest_nodes(G, j[1], j[0])
  duongdi = nx.shortest_path(G, diemtrungtam, diemden, weight="length")
  toadoduongdi = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in duongdi]
  folium.PolyLine(toadoduongdi, color="blue", weight=2.5, opacity=1).add_to(m)

folium.Marker(trungtam, popup='<b> <font face="Times" size="3" color="red"> Trường Đại học Kinh tế Thành phố Hồ Chí Minh - Cơ sở B </font> </b>', icon=folium.Icon(color='red',icon="home")).add_to(m)

display(m)