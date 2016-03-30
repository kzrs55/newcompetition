#coding=utf-8
__author__ = 'zjutK'
import networkx as nx
import numpy as np
from laplacian import *
G=nx.Graph()
G.add_weighted_edges_from([('A','B',4),('A','C',2),('B','C',1),('B','D',2),('B','E',2),('E','F',1)])
# print(G.adjacency_list())
# M=nx.to_numpy_matrix(G)
# print(M)
# print(nx.laplacian_matrix(G))

#拉普拉斯中心性
# x=lap_cent(G)
# xw=lap_cent_weighted(G)
# for a,b,c in zip(G.nodes(),x,xw):
#   print a,b,c

#特征向量中心性
print nx.eigenvector_centrality_numpy(G)


import matplotlib.pyplot as plt
pos=nx.spring_layout(G) # positions for all nodes
nx.draw(G,pos=pos)
nx.draw_networkx_labels(G,pos=pos)
nx.draw_networkx_edge_labels(G,pos=pos)
plt.show()