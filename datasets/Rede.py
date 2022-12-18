# Title      : Simulação de Rede Fúngica
# Install    : pip install networkx

import pandas
import networkx as nx
import matplotlib.pyplot as plt

plot1_dataframe = pandas.read_csv('/Users/josecasimiro/Downloads/Plot1_Tree_Data.csv')
adjacency_matrix_dataframe = pandas.read_csv('/Users/josecasimiro/Downloads/adjacency_matrix_plot1.csv')

#build graph 
G = nx.Graph()

#add nodes
for index, row in plot1_dataframe.iterrows():
    G.add_node(str(row[0]), pos=(row[1], row[2]), size=row[3], color=row[4])

for index, row in adjacency_matrix_dataframe.iterrows():
    currentNode = None
    for col in adjacency_matrix_dataframe.columns:
        if "P1-" in col:
            if str(row[col]) == "1":
                G.add_edge(currentNode, col, color='#bbbbbb', weight=1)
        else:
            currentNode = str(row[col])

#format graph
pos=nx.get_node_attributes(G,'pos')

color_map = []
for node in G.nodes:
    node_color = G.nodes[node]['color']
    match node_color:
        case 1:
            color_map.append('#00ff00')
        case 2:
            color_map.append('#00cc00')
        case 3:
            color_map.append('#00aa00')
        case 4:
            color_map.append('#008800')
        case _:
            color_map.append('#000000')            

node_size = []
for node in G.nodes:
    node_size.append(G.nodes[node]['size'])

edges = G.edges()
egdes_colors = [G[u][v]['color'] for u,v in edges]
egdes_weights = [G[u][v]['weight'] for u,v in edges]

#show graph
title = "Rede fúngica: " + \
    str(G.number_of_nodes()) + " Nós & " + str(G.number_of_edges()) + " Arestas."

fig, ax = plt.subplots()
ax.set_title(title)
nx.draw_networkx(G, pos, node_size=node_size, node_color=color_map, edge_color=egdes_colors, width=egdes_weights, with_labels=True)
fig.tight_layout()
plt.show()

print("Stop")