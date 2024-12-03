import pandas as pd
import networkx as nx

# Define the nodes
nodes = [
    "E0", "E1", "E2", "E3",
    "E4", "E5", "E6",
    "E7", "E8", "E9",
    "E10", "E11", "E12"
]


# Initialize the directed graph
G = nx.DiGraph()
G.add_nodes_from(nodes)

# Define transition rates
lambda1 = 1  # λ1
mu = 1.5       # µ

edges = [
    # Arrival transitions (λ)
    ("E0", "E1", lambda1),
    ("E1", "E4", lambda1),
    ("E2", "E5", lambda1),
    ("E3", "E6", lambda1),
    ("E4", "E7", lambda1),
    ("E5", "E8", lambda1),
    ("E6", "E9", lambda1),
    ("E7", "E10", lambda1),
    ("E8", "E11", lambda1),
    ("E9", "E12", lambda1),
    
    # Service completion transitions (µ)
    ("E3", "E0", mu),
    ("E1", "E2", mu),
    ("E2", "E3", mu),
    ("E6", "E1", mu),
    ("E4", "E5", mu),
    ("E5", "E6", mu),
    ("E9", "E4", mu),
    ("E7", "E8", mu),
    ("E8", "E9", mu),
    ("E12", "E7", mu),
    ("E10", "E11", mu),
    ("E11", "E12", mu),
    
    # Optional: Loop transitions if needed
    # ("E12", "E12", "µ"),  # Example of staying in the same state
]


# Add edges to the graph with rate as an attribute
for src, dst, rate in edges:
    G.add_edge(src, dst, rate=rate)

# Initialize the transition rate matrix with zeros
transition_matrix = pd.DataFrame(0.0, index=nodes, columns=nodes)


  
# Populate the transition rates
for src, dst, data in G.edges(data=True):
    rate = data['rate']
    transition_matrix.loc[src, dst] = rate

# Set the diagonal entries as the negative sum of outgoing rates
for node in nodes:
    outgoing_sum = transition_matrix.loc[node].sum()
    transition_matrix.loc[node, node] = -outgoing_sum

for i, j in zip(nodes, range(len(nodes))):
  transition_matrix[i][i] = j
# Display the transition rate matrix
print("Transition Rate Matrix:")
print(transition_matrix)
print(transition_matrix.to_csv())
