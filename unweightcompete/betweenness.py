#coding=utf-8
__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
M=[]
ce=[]
for i in range(1,200):
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
       bet=nx.edge_betweenness_centrality(Star,normalized=True);
    except Exception,e:
        print "Error"
        continue;
    # print bet
    sum0=0
    sum1=0
    for k,v in bet.items():
        if k[0]>100 and k[1]>100:
            sum1=sum1+v
        elif k[0]<100 and k[1]>100:
            pass
        else:
            sum0=sum0+v
    print sum0,sum1
    C=sum1/(sum1+sum0)
    M.append(i)
    print "B网络所占特征向量中心性大小",C,"节点个数",i
    ce.append(C)
    # ce.append(C)
    # print "B网络所占特征向量中心性大小",C
    # ce.append(C)
    # M.append(i)
    # print "B网络所占特征向量中心性大小",C
    # ce.append(C)
    # sum1=0;
    # for k in range(1,101):
    #     sum1=sum1+bet[k]
    # sum2=0
    # for k in range(101,101+i):
    #     sum2=sum2+bet[k]
    # print sum1,sum2
    # C=sum2/(sum1+sum2)
    # M.append(i)
    # print "B网络所占特征向量中心性大小",C
    # ce.append(C)
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

