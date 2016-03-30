# coding=utf-8
import copy

from matplotlib.ticker import MultipleLocator

__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def creat_star(number):
    star = nx.Graph()
    for i in range(1, number):
        star.add_edge(1, i + 1)
    return star
def findmax(arr):
    max= 0
    index=0
    for i in range(1,len(arr)+1):
        if max < arr[i]:
            max = arr[i];
            index = i;
    return index;


def findmin(arr):
    min=1;
    index=0
    for i in range(1,len(arr)+1):
        if min>arr[i]:
            min=arr[i];
            index=i;
    return index;

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
    network=copy.deepcopy(network1)
    eigenvetor1 = nx.eigenvector_centrality_numpy(network1);
    x = findmax(eigenvetor1)
    eigenvetor2 = nx.eigenvector_centrality_numpy(network2);
    y = findmax(eigenvetor2)
    num = network.number_of_nodes()
    print "CC竞争连接A网络", x, "B网络", y;
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
    eigenvetor1 = nx.eigenvector_centrality_numpy(network1);
    x = findmin(eigenvetor1)
    eigenvetor2 = nx.eigenvector_centrality_numpy(network2);
    y = findmin(eigenvetor2)
    print "PP竞争连接A网络", x, "B网络", y;
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



def compete(network,num):
    C1,C2,C3,C4,M=[]
    try:
        eigenvetor=nx.eigenvector_centrality_numpy(network);
    except Exception,e:
        print "Error"
    sum1=0;
    for k in range(1,num+1):
        sum1=sum1+eigenvetor[k]
    sum2=0;
    for k in range(num+1,num*2+1):
        sum2=sum2+eigenvetor[k]
    sum3=0;
    for k in range(num*2+1,num*3+1):
        sum3=sum3+eigenvetor[k]
    sum4=0
    for k in range(num*3+1,num*4+1):
        sum4=sum4+eigenvetor[k]
    sumall=sum1+sum2+sum3+sum4
    C1.append(sum1/sumall)
    C2.append(sum2/sumall)
    C3.append(sum3/sumall)
    C4.append(sum4/sumall)
    print i
    print sum1,sum2,sum3,sum4
    M.append()
    plt.xlabel('m')
    plt.ylabel('C')
    plt.xlim(0,500)
    plt.ylim(0, 1)
    ax = plt.gca()
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    plt.scatter(M, C1)
    plt.scatter(M, C2)
    plt.scatter(M, C3)
    plt.scatter(M, C4)
    plt.show()


if __name__ == '__main__':
    star1 = creat_star(10);
    star2 = creat_star(10)
    coop1=cooperationCC(star1,star2)
    coop2=cooperationPP(star1,star2)
    compe=competeCC(coop1,coop2)
    paint1(compe)


    # paint(star1)
