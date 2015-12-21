#coding=utf-8
import random
import math
import numpy as np

__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
def findmax(arr):
    max=0;
    index=0
    for i in range(len(arr)):
        if max<arr[i]:
            max=arr[i];
            index=i;
    return index;

def findmin(arr):
    min=1;
    index=0
    for i in range(len(arr)):
        if min>arr[i]:
            min=arr[i];
            index=i;
    return index;

eigen=[] #B网络最大特征值
T=[] #AB网络竞争时间

for i in range(100):
    BA1=nx.read_adjlist("RandomBAData/7.69.adjlist",nodetype=int);
    M1=nx.to_numpy_matrix(BA1);
    value1, vector1 = np.linalg.eig(M1);
    # for i in range(200):
    #     if value1[i] < 0:
    #         value1[i] = -value1[i]

    # print round(random.uniform(1,3))
    Ru=nx.random_graphs.newman_watts_strogatz_graph(200,6,round(random.uniform(0.15,0.4),2));
    print Ru.number_of_edges()
    M2=nx.to_numpy_matrix(Ru);
    value2, vector2 = np.linalg.eig(M2);
    # for i in range(200):
    #     if value2[i] < 0:
    #         value2[i] = -value2[i]
    print "A矩阵最大特征值",value1.max(),"B矩阵最大特征值",value2.max()
    eigenvetor1=nx.eigenvector_centrality_numpy(BA1);
    x=findmin(eigenvetor1)
    eigenvetor2=nx.eigenvector_centrality_numpy(Ru);
    y=findmin(eigenvetor2)
    print "连接A网络",x,"B网络",y;
    BA1.add_edge(x,y+200);
    # print value1
    # print value2
    for i,j in Ru.edges():
        BA1.add_edge(i+200,j+200);
    # M1=nx.to_numpy_matrix(BA1)
    # print M1
    try:
        eigenvetor=nx.eigenvector_centrality_numpy(BA1);
        M3=nx.to_numpy_matrix(BA1);
        value3, vector3 = np.linalg.eig(M3);
        lanta1=sorted(value3)[len(value3)-1]
        lanta2=sorted(value3)[len(value3)-2]
        print lanta1,lanta2
    except Exception,e:
        print "Error"
        continue;
    if lanta1>=lanta2:
        try:
            print 1/math.log(lanta1/lanta2)*2000
            T.append(1/math.log(lanta1/lanta2)*2000)
            eigen.append(value2.max())
        except Exception,e:
            print "ERROR"
    else:
        try:
            print 1/math.log(lanta2/lanta1)*2000
            T.append(1/math.log(lanta2/lanta1)*2000)
            eigen.append(value2.max())
        except Exception,e:
            print "ERROR"








print T
print eigen
plt.xlabel('m')
plt.ylabel('Tc,t')
plt.xlim(6.8,9.0)
plt.semilogy(100,1000000)
plt.scatter(eigen,T)
ax = plt.gca()
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
plt.show()