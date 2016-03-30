#coding=utf-8
import numpy as np

__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
import laplacian as lap
from matplotlib.ticker import MultipleLocator
def findmax(arr):
    max=0;
    index=0
    for i in range(len(arr)):
        if max<arr[i]:
            max=arr[i];
            index=i;
    return index;
ce=[] #特征向量中心性
value=[] #B网络的最大特征值

for i in range(500):
    BA1=nx.read_adjlist("RandomBAData/7.69.adjlist",nodetype=int);
    M1=nx.to_numpy_matrix(BA1);
    value1, vector1 = np.linalg.eig(M1);
    BA2=nx.random_graphs.barabasi_albert_graph(200,2);
    M2=nx.to_numpy_matrix(BA2);
    value2, vector2 = np.linalg.eig(M2);
    print "A矩阵最大特征值",value1.max(),"B矩阵最大特征值",value2.max()
    eigenvetor1=lap.lap_cent(BA1);
    x=findmax(eigenvetor1)
    eigenvetor2=lap.lap_cent(BA2);
    y=findmax(eigenvetor2)
    print "连接A网络",x,"B网络",y;
    BA1.add_edge(x,y+200);
    # print value1
    # print value2
    for i,j in BA2.edges():
        BA1.add_edge(i+200,j+200);
    # M1=nx.to_numpy_matrix(BA1)
    # print M1
    try:
        eigenvetor=lap.lap_cent(BA1);
    except Exception,e:
        print "Error"
        continue;
    sum1=0;
    for i in range(200):
        sum1=sum1+eigenvetor[i]
    sum2=0
    for i in range(len(eigenvetor)-200):
        sum2=sum2+eigenvetor[i+200]
    print sum1,sum2
    # C=sum2/(sum1+sum2)
    C=sum2+sum1
    value.append(value2.max())
    print "B网络所占特征向量中心性大小",C
    ce.append(C)
print value
print ce
plt.xlabel('m')
plt.ylabel('CA')
plt.xlim(6.8, 8.8)
# plt.ylim(0, 1)
ax = plt.gca()
ax.xaxis.set_minor_locator(MultipleLocator(0.2))
plt.scatter(value, ce)
plt.show()
