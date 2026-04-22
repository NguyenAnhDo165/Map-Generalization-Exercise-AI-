#Bài 4
import geopandas as gpd
import pandas
import matplotlib.pyplot as plt
import folium
mapVN = "/content/gadm41_VNM_1.json"
danso = "/content/population.csv"
tinhVN = gpd.read_file(mapVN)
dansoVN = pandas.read_csv(danso)
m = folium.Map(location=[14.0583,108.2772],zoom_start=5)
folium.Choropleth(
    geo_data=tinhVN,
    name="choropleth",
    data=dansoVN,
    columns=["province","population"],
    key_on="feature.properties.NAME_1",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Dân số theo tỉnh").add_to(m)
m