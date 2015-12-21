#coding=utf-8
import numpy as np

__author__ = 'zjutK'
import networkx as nx
BA1=nx.random_graphs.barabasi_albert_graph(200,2)
# BA2=[]
# # nx.read_graphml('BA.gz')
# print BA1.edges()
# for i,j in BA1.edges():
#     BA2.append((i+200,j+200))
nx.write_adjlist(BA1,"BA.adjlist")
M=nx.to_numpy_matrix(BA1)
value1, vector1 = np.linalg.eig(M)
print value1
print nx.eigenvector_centrality_numpy(BA1)
# BA1=[i+200 for i in BA1.edges()]