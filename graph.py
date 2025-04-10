import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Data for network creation - Sheet1 (1).csv"
df = pd.read_csv(file_path)

# Create directed graph
G = nx.DiGraph()

# Add edges with export volume as weight
for _, row in df.iterrows():
    source = row['Reporter Name']
    target = row['Partner Name']
    weight = row['Export (US$ Thousand)']
    if weight > 0:
        G.add_edge(source, target, weight=weight)

# Node sizes based on degree
node_sizes = [100 + 10 * (G.degree(n)) for n in G.nodes()]
larger_node_sizes = [s * 1.5 for s in node_sizes]  # scale up for visibility

# Edge widths based on trade volume
edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
max_weight = max(edge_weights)
edge_widths_scaled = [0.5 + (w / max_weight * 8) for w in edge_weights]

# Layout for better spacing
pos = nx.spring_layout(G, seed=42, k=0.8)

# Plot the graph
plt.figure(figsize=(18, 14))
nx.draw_networkx_nodes(G, pos, node_size=larger_node_sizes, node_color='skyblue', edgecolors='black')
nx.draw_networkx_edges(G, pos, width=edge_widths_scaled, alpha=0.7, edge_color='teal')
nx.draw_networkx_labels(G, pos, font_size=10)

plt.title("Enhanced Visibility: Trade Network with Edge Widths by Export Volume", fontsize=18)
plt.axis('off')
plt.tight_layout()
plt.show()