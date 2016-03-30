#coding=utf-8
__author__ = 'zjutK'
import networkx as nx
import networkx.algorithms.centrality.load as eb
G=nx.Graph()
G.add_edges_from([(1,3),(2,3),(3,4),(4,5),(3,6),(6,7),(6,8)])
# print eb._edge_betweenness(G,1,8)
# import networkx as nx

# G=nx.path_graph(4)

e=nx.edge_betweenness_centrality(G,normalized=True)

print e
total=sum(v for k,v in e.items())
print total
print 0.25*5+0.53571+0.428571
# import matplotlib.pyplot as plt
# pos=nx.spring_layout(G) # positions for all nodes
# nx.draw(G,pos=pos)
# nx.draw_networkx_labels(G,pos=pos)
# nx.draw_networkx_edge_labels(G,pos=pos)
# plt.show()