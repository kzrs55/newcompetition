#coding=utf-8
import math
import numpy as np

import scipy

__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
T=[]
M=[]
for i in range(1,200):
    Star=nx.Graph();
    for j in range(2,102):
        Star.add_edge(1,j);
    if i==1:
        pass
    else:
        for j in range(2,i+1):
            Star.add_edge(101,100+j)
    # try:
    #eigenvetor=nx.eigenvector_centrality_numpy(Star);
    Matrix=nx.to_numpy_matrix(Star);
    value, vector = scipy.linalg.eig(Matrix);
    lanta1=sorted(value)[len(value)-1]
    lanta2=sorted(value)[len(value)-2]
    print lanta1,lanta2
    # except Exception,e:
    #     print "Error...."
    #     continue;
    try:
        x=1/math.log(lanta1/lanta2)*20000/(0.433329775363)
        print '竞争时间',x,'点的个数',i
        T.append(x)
        M.append(i)
    except Exception,e:
        print "竞争时间ERROR"


print M
print T
plt.xlabel('m')
plt.ylabel('Tc,t')
plt.xlim(0,200)
plt.semilogy(M,T)
ax = plt.gca()
ax.xaxis.set_minor_locator(MultipleLocator(10))
plt.show()

