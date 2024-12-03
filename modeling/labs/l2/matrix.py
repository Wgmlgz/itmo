import pandas as pd
import networkx as nx

# Define the nodes
nodes = ["E0", "E1", "E2", "E3", "E4", "E5"]

# Initialize the directed graph
G = nx.DiGraph()
G.add_nodes_from(nodes)

# Define transition rates
lambda1 = 0.6  # λ1
lambda2 = 0.4  # λ2
mu = 0.5       # µ

# Add edges with corresponding rates
edges = [
    ("E0", "E1", lambda1),
    ("E0", "E2", lambda2),
    ("E1", "E3", lambda2),
    ("E2", "E3", lambda1),
    ("E2", "E4", lambda2),
    ("E3", "E5", lambda2),
    ("E1", "E0", mu),
    ("E2", "E0", mu),
    ("E3", "E1", mu),
    ("E3", "E2", mu),
    ("E4", "E2", mu),
    ("E5", "E4", mu),
    ("E5", "E3", mu),
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
