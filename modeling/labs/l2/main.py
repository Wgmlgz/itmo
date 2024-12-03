import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes with labels
nodes = ["E0", "E1", "E2", "E3", "E4", "E5"]
positions = {
    "E0": (0, 0),
    "E1": (1, 1),
    "E2": (1, -1),
    "E3": (2, 0),
    "E4": (2, -2),
    "E5": (3, -1),
}
labels = {node: node for node in nodes}
G.add_nodes_from(nodes)

# Add edges with labels for transitions
edges = [
    ("E0", "E2", "λλ2"),
    ("E0", "E1", "λλ1"),
    ("E1", "E3", "λλ2"),
    ("E2", "E4", "λλ2"),
    ("E2", "E3", "λλ1"),
    ("E3", "E5", "λλ2"),
    ("E1", "E0", "µ"),
    ("E2", "E0", "µ"),
    ("E3", "E2", "µ"),
    ("E3", "E1", "µ"),
    ("E4", "E2", "µ"),
    ("E5", "E4", "µ"),
    ("E5", "E3", "µ"),
]


# Add edges with a 'label' attribute
for u, v, label in edges:
    G.add_edge(u, v, label=label)

# Separate edges by label type
lambda_edges = [(u, v) for u, v, d in G.edges(data=True) if d["label"].startswith("λ")]
mu_edges = [(u, v) for u, v, d in G.edges(data=True) if d["label"].startswith("µ")]

# Draw the graph
plt.figure(figsize=(12, 8))
nx.draw(
    G,
    pos=positions,
    with_labels=True,
    labels=labels,
    node_color="skyblue",
    node_size=2000,
    font_size=12,
    font_weight="bold",
    arrowstyle="-|>",
    arrowsize=20,
    connectionstyle="arc3,rad=0.2",
)

# Draw λ edge labels
lambda_labels = {
    (u, v): d["label"] for u, v, d in G.edges(data=True) if d["label"].startswith("λ")
}
nx.draw_networkx_edge_labels(
    G,
    pos=positions,
    edge_labels=lambda_labels,
    font_color="red",
    label_pos=0.5,
    font_size=12,
    bbox=dict(boxstyle="round,pad=0.2", fc="yellow", alpha=0.5),
    connectionstyle="arc3,rad=0.3",
)

# Draw µ edge labels
mu_labels = {
    (u, v): d["label"] for u, v, d in G.edges(data=True) if d["label"].startswith("µ")
}
nx.draw_networkx_edge_labels(
    G,
    pos=positions,
    edge_labels=mu_labels,
    font_color="blue",
    label_pos=0.5,
    font_size=12,
    bbox=dict(boxstyle="round,pad=0.2", fc="lightgreen", alpha=0.5),
    connectionstyle="arc3,rad=0.3",
)

plt.title("Transition Graph for the System", fontsize=16)
plt.axis("off")  # Hide the axes
plt.show()
