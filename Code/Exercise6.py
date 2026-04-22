#Bài 6
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

point = (10.7868, 106.6666)
dist = 1000  # mét
G = ox.graph_from_point(point, dist=dist, network_type="drive")
fig, ax = ox.plot_graph(
    G,
    node_size=10,
    edge_linewidth=0.8,
    bgcolor="white"
)
num_nodes = len(G.nodes)
num_edges = len(G.edges)
edge_lengths = [data["length"] for u, v, data in G.edges(data=True)]
avg_length = sum(edge_lengths) / len(edge_lengths)
total_length = sum(edge_lengths)
print("===== KẾT QUẢ PHÂN TÍCH =====")
print(f"Số nút giao: {num_nodes}")
print(f"Số đoạn đường: {num_edges}")
print(f"Chiều dài trung bình: {avg_length:.2f} m")
print(f"Tổng chiều dài: {total_length/1000:.2f} km")