#coding=utf-8
__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import laplacian as lap
M=[]
ce=[]
for i in range(1,500):
    Star=nx.Graph();
    for j in range(2,101):
        Star.add_edge(1,j);
    if i==1:
        Star.add_edge(1,101)
    else:
        Star.add_edge(2,102)
        for j in range(2,i+1):
            Star.add_edge(101,100+j)
    try:
        centrality=lap.lap_cent(Star);
    except Exception,e:
        print "Error"
        continue;
    print centrality
    sum=0
    for k in range(0,100+i):
        sum=sum+centrality[k]
    print sum
    sum1=0;
    for k in range(0,100):
        sum1=sum1+centrality[k]
    sum2=0
    for k in range(100,100+i):
        sum2=sum2+centrality[k]
    print sum1,sum2
    C=float(sum1+sum2)
    M.append(i)
    print "B网络所占特征向量中心性大小",C
    ce.append(C)
print M
print ce
plt.xlabel('m')
plt.ylabel('CA')
plt.xlim(0,500)
# plt.ylim(0, 1)
ax = plt.gca()
ax.xaxis.set_minor_locator(MultipleLocator(20))
plt.scatter(M, ce)
plt.show()

