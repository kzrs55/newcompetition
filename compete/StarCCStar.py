#coding=utf-8
__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
M=[]
ce=[]
for i in range(1,100):
    Star=nx.Graph();
    for j in range(2,102):
        Star.add_edge(1,j);
    if i==1:
        pass
    else:
        for j in range(2,i+1):
            Star.add_edge(101,100+j)
    try:
        eigenvetor=nx.eigenvector_centrality_numpy(Star);
    except Exception,e:
        print "Error"
        continue;
    sum1=0;
    for k in range(1,101):
        sum1=sum1+eigenvetor[k]
    sum2=0
    for k in range(101,101+i):
        sum2=sum2+eigenvetor[k]
    print sum1,sum2
    C=sum2/(sum1+sum2)
    M.append(i)
    print "B网络所占特征向量中心性大小",C
    ce.append(C)
print M
print ce
plt.xlabel('m')
plt.ylabel('CA')
plt.xlim(0,500)
plt.ylim(0, 1)
ax = plt.gca()
ax.xaxis.set_minor_locator(MultipleLocator(20))
plt.scatter(M, ce)
plt.show()

