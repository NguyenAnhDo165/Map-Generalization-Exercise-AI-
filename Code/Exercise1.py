#Bài 1
from google.colab import files
import folium
m = folium.Map(location=(10.761011, 106.668407),zoom_start=20)
folium.Marker([10.761113522277538, 106.66834923397425],popup = '<b> <font face="Times" size="3" color="red"> Trường Đại học Kinh tế Thành phố Hồ Chí Minh - Cơ sở B </font> </b>',tooltip="Click vào").add_to(m)
folium.Marker([10.756286741170575, 106.66303577560868],popup = "Hùng Vương Plaza",tooltip="Click vào").add_to(m)
folium.Marker([10.760831845847395, 106.66331544329134],popup = "Sân vận động Thống Nhất",tooltip="Click vào").add_to(m)
folium.Marker([10.75689938037034, 106.66432490856758],popup = "Bệnh viện Phạm Ngọc Thạch",tooltip="Click vào").add_to(m)
folium.Marker([10.763546406603451, 106.66834163635485],popup = "Văn phòng Kinh tế và Văn hóa Đài Bắc tại TP.HCM",tooltip="Click vào").add_to(m)
folium.Marker([10.759702012672866, 106.67052732042637],popup = "Trường Dự bị đại học TP. HCM",tooltip="Click vào").add_to(m)
m
