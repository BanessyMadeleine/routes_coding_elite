import networkx as nx
import numpy as np
from itertools import combinations
import math

positions = { 'Mines Paris' : (2.33969, 48.84563),
'Observatoire de Paris' : (2.33650, 48.83730), 'Marie du 14e' : (2.32698, 48.83320),
'Gare Montparnasse TGV' : (2.32159, 48.84117), 'Mairie du 15e' : (2.29991, 48.84126)}
source = (2.36815, 48.74991)
X=[]
Y=[]
for cle in positions : 
    X.append(positions[cle][0])
    Y.append(positions[cle][1])


def distance_cartesienne(x1, x2, y1, y2):
    lat1, lon1 = math.radians(x1), math.radians(x2)
    lat2, lon2 = math.radians(y1), math.radians(y2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Rayon de la Terre en kilomètres
    R = 6371.0

    distance = R * c
    return distance
distance_cartesienne (source[0], source[1], 2.33969, 48.84563)

G = nx.DiGraph()
for (i, (xval, yval)) in enumerate(zip(X, Y)):
    G.add_edge("Source", i, cost = distance_cartesienne(xval, source [0], yval,source [1] )) 
    G.add_edge(i, "Sink", cost = distance_cartesienne(xval, source [0], yval, source [1])) 
    G.nodes[i]["demand"] = 1
for ((i, (x1, y1)), (j, (x2, y2))) in combinations(list(enumerate(zip(X, Y))), 2): 
    G.add_edge(i, j, cost = distance_cartesienne(x1, x2, y1, y2)) 
    G.add_edge(j, i, cost = distance_cartesienne(x1, x2, y1, y2))

nx.draw(G, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray', font_color='black')
#nx.draw_networkx_edge_labels(G, edge_labels=edge_labels)
#pos = nx.spring_layout(G,k=10)
#labels={e: G.edges[e]['cost'] for e in G.edges}
#nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)


