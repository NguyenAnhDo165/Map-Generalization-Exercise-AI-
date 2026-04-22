#Bài 3
import folium
from folium.plugins import HeatMap

trungtam = (10.76117635724359, 106.6683304626097) #Đại học Kinh tế TP.HCM cơ sở B
diachi1 = (10.756286741170575, 106.66303577560868)
diachi2 = (10.760831845847395, 106.66331544329134)
diachi3 = (10.75689938037034, 106.66432490856758)
diachi4 = (10.763546406603451, 106.66834163635485)
diachi5 = (10.759702012672866, 106.67052732042637)

giaohang = [diachi1,diachi2,diachi3,diachi4,diachi5]

m = folium.Map(location=trungtam, zoom_start=14)
HeatMap(giaohang,radius=70,blur=10,max_zoom=1).add_to(m)
m