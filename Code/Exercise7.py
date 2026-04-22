#Bài 7
import osmnx as ox
import networkx as nx
import folium

center = (10.7868, 106.6666)
G = ox.graph_from_point(center, dist=1500, network_type="drive")

origin_point = (10.7895, 106.6640)
destination_point = (10.7815, 106.6725)

orig_node = ox.distance.nearest_nodes(G, origin_point[1], origin_point[0])
dest_node = ox.distance.nearest_nodes(G, destination_point[1], destination_point[0])

route_dijkstra = nx.shortest_path(G, orig_node, dest_node, weight="length")

def heuristic(u, v):
    x1, y1 = G.nodes[u]["x"], G.nodes[u]["y"]
    x2, y2 = G.nodes[v]["x"], G.nodes[v]["y"]
    return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

route_astar = nx.astar_path(G, orig_node, dest_node, heuristic=heuristic, weight="length")

length_dijkstra = nx.path_weight(G, route_dijkstra, weight="length")
length_astar = nx.path_weight(G, route_astar, weight="length")

print("Dijkstra length (m):", length_dijkstra)
print("A* length (m):", length_astar)

m = folium.Map(location=center, zoom_start=15)

folium.PolyLine(locations=[(G.nodes[n]["y"], G.nodes[n]["x"]) for n in route_dijkstra],color="red",weight=5,tooltip="Dijkstra").add_to(m)

folium.PolyLine(locations=[(G.nodes[n]["y"], G.nodes[n]["x"]) for n in route_astar],color="blue", weight=5,tooltip="A*").add_to(m)

folium.Marker(origin_point, popup="Start").add_to(m)
folium.Marker(destination_point, popup="End").add_to(m)

m