import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes with labels
nodes = [
    "E0", "E1", "E2", "E3",
    "E4", "E5", "E6",
    "E7", "E8", "E9",
    "E10", "E11", "E12"
]

positions = {
    "E0": (1, 2),
    "E1": (1, 0),
    "E2": (2, 0 -0.2),
    "E3": (3, 0),
    "E4": (1, -1),
    "E5": (2, -1 -0.2),
    "E6": (3, -1),
    "E7": (1, -2),
    "E8": (2, -2 -0.2),
    "E9": (3, -2),
    "E10": (1, -3),
    "E11": (2, -3 -0.2),
    "E12": (3, -3),
}


labels = {node: node for node in nodes}
G.add_nodes_from(nodes)

# Add edges with labels for transitions
edges = [
    # Arrival transitions (λ)
    ("E0", "E1", "λ1λ"),
    ("E1", "E4", "λ1λ"),
    ("E2", "E5", "λ1λ"),
    ("E3", "E6", "λ1λ"),
    ("E4", "E7", "λ1λ"),
    ("E5", "E8", "λ1λ"),
    ("E6", "E9", "λ1λ"),
    ("E7", "E10", "λ1λ"),
    ("E8", "E11", "λ1λ"),
    ("E9", "E12", "λ1λ"),
    
    # Service completion transitions (µ)
    ("E3", "E0", "µ'"),
    ("E1", "E2", "µ'"),
    ("E2", "E3", "µ'"),
    ("E6", "E1", "µ'"),
    ("E4", "E5", "µ'"),
    ("E5", "E6", "µ'"),
    ("E9", "E4", "µ'"),
    ("E7", "E8", "µ'"),
    ("E8", "E9", "µ'"),
    ("E12", "E7", "µ'"),
    ("E10", "E11", "µ'"),
    ("E11", "E12", "µ'"),
    
    # Optional: Loop transitions if needed
    # ("E12", "E12", "µ"),  # Example of staying in the same state
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
    connectionstyle="arc3,rad=0.0",
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
    connectionstyle="arc3,rad=0.2",
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
    label_pos=0.7,
    font_size=12,
    bbox=dict(boxstyle="round,pad=0.2", fc="lightgreen", alpha=0.5),
    connectionstyle="arc3,rad=0.1",
)

plt.title("Transition Graph for the System", fontsize=16)
plt.axis("off")  # Hide the axes
plt.show()
