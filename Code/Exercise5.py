#Bài 5
import folium
trungtam = [10.7769, 106.7009]
m = folium.Map(location=trungtam, zoom_start=12)
folium.Marker(location=trungtam,popup="<h1><b>Trung tâm phân phối</h></b>",icon=folium.Icon(color="red",icon="home")).add_to(m)
folium.Circle(location=trungtam,radius=10000,color="red",fill=True,fill_opacity=0.2,popup="<b>10 km</b> - Giao hàng trong vòng 20 phút").add_to(m)
folium.Circle(location=trungtam,radius=5000,color="yellow",fill=True,fill_opacity=0.2,popup="<b>5 km</b> - Giao hàng trong vòng 10 phút").add_to(m)
folium.Circle(location=trungtam,radius=3000,color="green",fill=True,fill_opacity=0.5,popup="<b>3 km</b> - Giao hàng trong vòng 5 phút").add_to(m)
m