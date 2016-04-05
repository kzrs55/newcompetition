#coding=utf-8
__author__ = 'zjutK'
# coding=utf-8
import copy

from matplotlib.ticker import MultipleLocator

__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#建立星形网络
def creat_star(number):
    star = nx.Graph()
    for i in range(1, number):
        star.add_edge(1, i + 1)
    return star
#找寻最大的节点
def findmax(arr):
    max= 0
    index=0
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i];
            index = i;
    return index;

#找寻最小的节点
def findmin(arr):
    min=1;
    index=0
    for i in range(len(arr)):
        if min>arr[i]:
            min=arr[i];
            index=i;
    return index;
#CC合作
def cooperationCC(network1, network2):
    # M1 = nx.to_numpy_matrix(network1);
    # value1, vector1 = np.linalg.eig(M1);
    # M2 = nx.to_numpy_matrix(network2);
    # value2, vector2 = np.linalg.eig(M2);
    # print "A矩阵最大特征值", value1.max(), "B矩阵最大特征值", value2.max()
    network=copy.deepcopy(network1)
    eigenvetor1 = nx.eigenvector_centrality_numpy(network1);
    x = findmax(eigenvetor1)
    eigenvetor2 = nx.eigenvector_centrality_numpy(network2);
    y = findmax(eigenvetor2)
    num = network.number_of_nodes()
    print "CC合作连接A网络", x, "B网络", y;
    network.add_edge(x, y+num);
    for i, j in network2.edges():
        network.add_edge(i + num, j + num)
    return network
#PP合作
def cooperationPP(network1,network2):
    # M1 = nx.to_numpy_matrix(network1);
    # value1, vector1 = np.linalg.eig(M1);
    # M2 = nx.to_numpy_matrix(network2);
    # value2, vector2 = np.linalg.eig(M2);
    # print "A矩阵最大特征值", value1.max(), "B矩阵最大特征值", value2.max()
    network=copy.deepcopy(network1)
    eigenvetor1 = nx.eigenvector_centrality_numpy(network1);
    x = findmin(eigenvetor1)
    eigenvetor2 = nx.eigenvector_centrality_numpy(network2);
    y = findmin(eigenvetor2)
    print "PP合作连接A网络", x, "B网络", y;
    num = network.number_of_nodes()
    network.add_edge(x, y + num);
    for i, j in network2.edges():
        network.add_edge(i + num, j + num)
    return network

def competeCC(network1, network2):
    # M1 = nx.to_numpy_matrix(network1);
    # value1, vector1 = np.linalg.eig(M1);
    # M2 = nx.to_numpy_matrix(network2);
    # value2, vector2 = np.linalg.eig(M2);
    # print "A矩阵最大特征值", value1.max(), "B矩阵最大特征值", value2.max()
    try:
        network=copy.deepcopy(network1)
        eigenvetor1 = nx.eigenvector_centrality_numpy(network1);
        x = findmax(eigenvetor1)
        eigenvetor2 = nx.eigenvector_centrality_numpy(network2);
        y = findmax(eigenvetor2)
        print "CC竞争连接A网络", x, "B网络", y;
    except Exception:
        print("competeCC error")
    num = network.number_of_nodes()
    network.add_edge(x, y + num);
    for i, j in network2.edges():
        network.add_edge(i + num, j + num)
    return network

def competePP(network1,network2):
     # M1 = nx.to_numpy_matrix(network1);
    # value1, vector1 = np.linalg.eig(M1);
    # M2 = nx.to_numpy_matrix(network2);
    # value2, vector2 = np.linalg.eig(M2);
    # print "A矩阵最大特征值", value1.max(), "B矩阵最大特征值", value2.max()
    network=copy.deepcopy(network1)
    try:
        eigenvetor1 = nx.eigenvector_centrality_numpy(network1);
        x = findmin(eigenvetor1)
        eigenvetor2 = nx.eigenvector_centrality_numpy(network2);
        y = findmin(eigenvetor2)
        print "PP竞争连接A网络", x, "B网络", y;
    except Exception:
        return network
    num = network.number_of_nodes()
    network.add_edge(x, y + num);
    for i, j in network2.edges():
        network.add_edge(i + num, j + num)
    return network


def paint1(network):
    pos = nx.spring_layout(network)  # positions for all nodes
    nx.draw(network, pos=pos)
    nx.draw_networkx_labels(network, pos=pos)
    nx.draw_networkx_edge_labels(network, pos=pos)
    plt.show()
M=[]
C1=[]
C2=[]
C3=[]
C4=[]
ce=[]

def paint2():
    plt.xlabel('m')
    plt.ylabel('C')
    plt.xlim(6.8,8.8)
    plt.ylim(0, 1)
    ax = plt.gca()
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    plt.scatter(M, C1,label="A",color=np.random.rand(1,3))
    plt.scatter(M, C2,label="B",color=np.random.rand(1,3))
    plt.scatter(M, C3,label="C",color=np.random.rand(1,3))
    plt.scatter(M, C4,label="D",color=np.random.rand(1,3))
    plt.legend()
    plt.show()



def compete(network,num1,num2,num3,num4):
    try:
        eigenvetor=nx.eigenvector_centrality_numpy(network);
    except Exception,e:
        print "Error"
    sum1=0;
    for k in range(0,num1):
        sum1=sum1+eigenvetor[k]
    sum2=0;
    for k in range(num1,num1+num2):
        sum2=sum2+eigenvetor[k]
    sum3=0;
    for k in range(num1+num2,num1+num2+num3):
        sum3=sum3+eigenvetor[k]
    sum4=0
    for k in range(num1+num2+num3,num1+num2+num3+num4):
        sum4=sum4+eigenvetor[k]
    sumall=sum1+sum2+sum3+sum4
    C1.append(sum1/sumall)
    C2.append(sum2/sumall)
    C3.append(sum3/sumall)
    C4.append(sum4/sumall)
    print sum1,sum2,sum3,sum4


if __name__ == '__main__':
    for i in range(1,100):
        BA1=nx.read_adjlist("RandomBAData/7.69.adjlist",nodetype=int);
        BA2=nx.random_graphs.barabasi_albert_graph(200,2);
        M2=nx.to_numpy_matrix(BA2);
        value2, vector2 = np.linalg.eig(M2);
        print "A矩阵最大特征值",7.69,"B矩阵最大特征值",value2.max()
        coop1=cooperationCC(BA1,BA2)
        coop2=cooperationPP(BA1,BA2)
        compe=competeCC(coop1,coop2)
        compete(compe,200,200,200,200)
        M.append(value2.max())

    paint2()
        # paint1(compe)



    # paint(star1)
