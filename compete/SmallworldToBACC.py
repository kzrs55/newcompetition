#coding=utf-8
import random
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

ce=[] #特征向量中心性
value=[] #B网络的最大特征值

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
    except Exception,e:
        print "Error"
        continue;
    sum1=0;
    for i in range(200):
        sum1=sum1+eigenvetor[i]
    sum2=0
    print len(eigenvetor)
    print eigenvetor
    for i in range(len(eigenvetor)-200):
        if eigenvetor.has_key(i+200):
            sum2=sum2+eigenvetor[i+200]
    print sum1,sum2
    C=sum2/(sum1+sum2)
    value.append(value2.max())
    print "B网络所占特征向量中心性大小",C
    ce.append(C)
print value
print ce
plt.xlabel('m')
plt.ylabel('CA')
plt.xlim(6.8, 8.8)
plt.ylim(0, 1)
ax = plt.gca()
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
plt.scatter(value, ce)
plt.show()
