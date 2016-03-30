#coding=utf-8
import math
import numpy as np

__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
M=[]
T=[]
for i in range(3,200):
    Star1=nx.Graph();
    for j in range(2,101):
        Star1.add_edge(1,j);
    Matrix1=nx.to_numpy_matrix(Star1);
    value1, vector1 = np.linalg.eig(Matrix1);
    lanta1=max(value1)

    Star2=nx.Graph();
    for j in range(2,i+1):
        Star2.add_edge(1,j)
    Matrix2=nx.to_numpy_matrix(Star2);
    value2, vector2 = np.linalg.eig(Matrix2);
    lanta2=max(value2)
    if lanta1>=lanta2:
        try:
            print i,1/math.log(lanta1/lanta2)*20000
            T.append(1/math.log(lanta1/lanta2)*20000)
            M.append(i)
        except Exception,e:
            T.append(10000000)
            M.append(100)
    else:
        try:
            print i,1/math.log(lanta2/lanta1)*20000
            T.append(1/math.log(lanta2/lanta1)*20000)
            M.append(i)
        except Exception,e:
            print "ERROR"


    # print i,lanta1,lanta2
print M
print T
plt.xlabel('m')
plt.ylabel('Tc,t')
plt.xlim(0,200)
plt.semilogy(M,T)
ax = plt.gca()
ax.xaxis.set_minor_locator(MultipleLocator(10))
plt.show()

