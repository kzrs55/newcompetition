#coding=utf-8
__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import scipy
M=[]
ce=[]
for i in range(499,500):
    Star1=nx.Graph();
    for j in range(2,101):
        Star1.add_edge(1,j);
    if i==1:
        Star1.add_edge(1,101)#合作CC连接
    else:
        Star1.add_edge(1,101)#合作CC连接
        # Star1.add_edge(1,102)#合作PC连接
        for j in range(2,i+1):
            Star1.add_edge(101,100+j)
    Star2=nx.Graph();
    for j in range(2,101):
        Star2.add_edge(1,j);
    if i==1:
        Star2.add_edge(1,101)
    else:
        # Star2.add_edge(2,102)#合作PP连接
        Star2.add_edge(1,102)#合作PC连接
        for j in range(2,i+1):
            Star2.add_edge(101,100+j)
    Star1.add_edge(1,101+i)#竞争CC连接
    for j,k in Star2.edges():
        Star1.add_edge(j+100+i,k+100+i);
    try:
        eigenvetor=nx.eigenvector_centrality_numpy(Star1);
    except Exception,e:
        print "Error"
        continue;
    # print eigenvetor
    sum1=0;
    for k in range(1,101+i):
        sum1=sum1+eigenvetor[k]
    sum2=0
    for k in range(101+i,200+2*i):
        sum2=sum2+eigenvetor[k]
    print sum1,sum2
    # C=sum1+sum2
    C=sum2/(sum1+sum2)
    M.append(i)
    print "B网络所占特征向量中心性大小",C
    ce.append(C)
# print M
# print ce
# plt.xlabel('m')
# plt.ylabel('CA')
# plt.xlim(0,500)
# plt.ylim(0, 0.5)
# ax = plt.gca()
# ax.xaxis.set_minor_locator(MultipleLocator(20))
# plt.scatter(M, ce)
# plt.show()
import matplotlib.pyplot as plt
pos=nx.spring_layout(Star1) # positions for all nodes
nx.draw(Star1,pos=pos)
nx.draw_networkx_labels(Star1,pos=pos)
nx.draw_networkx_edge_labels(Star1,pos=pos)
plt.show()
