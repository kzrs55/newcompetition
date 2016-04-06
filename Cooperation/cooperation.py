# coding=utf-8
import copy
import networkx as nx
import matplotlib.pyplot as plt

__author__ = 'zjutK'


# 建立星形网络
def creat_star(number):
    star = nx.Graph()
    for i in range(number):
        star.add_edge(0, i + 1)
    return star


# 找寻最大的节点
def find_max(arr):
    _max = 0
    index = 0
    for i in range(len(arr)):
        if _max < arr[i]:
            _max = arr[i]
            index = i
    return index


# 找寻最小的节点
def find_min(arr):
    _min = 1
    index = 0
    for i in range(len(arr)):
        if _min > arr[i]:
            _min = arr[i]
            index = i
    return index


# CC合作
def cooperation_cc(network1, network2):
    # M1 = nx.to_numpy_matrix(network1);
    # value1, vector1 = np.linalg.eig(M1);
    # M2 = nx.to_numpy_matrix(network2);
    # value2, vector2 = np.linalg.eig(M2);
    # print "A矩阵最大特征值", value1.max(), "B矩阵最大特征值", value2.max()
    network = copy.deepcopy(network1)
    eigenvector_one = nx.eigenvector_centrality_numpy(network1)
    x = find_max(eigenvector_one)
    eigenvector_two = nx.eigenvector_centrality_numpy(network2)
    y = find_max(eigenvector_two)
    num = network.number_of_nodes()
    print "CC合作连接A网络", x, "B网络", y
    network.add_edge(x, y + num)
    for i, j in network2.edges():
        network.add_edge(i + num, j + num)
    return network


# PP合作
def cooperation_pp(network1, network2):
    # M1 = nx.to_numpy_matrix(network1);
    # value1, vector1 = np.linalg.eig(M1);
    # M2 = nx.to_numpy_matrix(network2);
    # value2, vector2 = np.linalg.eig(M2);
    # print "A矩阵最大特征值", value1.max(), "B矩阵最大特征值", value2.max()
    network = copy.deepcopy(network1)
    eigenvector_one = nx.eigenvector_centrality_numpy(network1)
    x = find_min(eigenvector_one)
    eigenvector_two = nx.eigenvector_centrality_numpy(network2)
    y = find_min(eigenvector_two)
    print "PP合作连接A网络", x, "B网络", y
    num = network.number_of_nodes()
    network.add_edge(x, y + num)
    for i, j in network2.edges():
        network.add_edge(i + num, j + num)
    return network

# CC竞争
def compete_cc(network1, network2):
    # M1 = nx.to_numpy_matrix(network1);
    # value1, vector1 = np.linalg.eig(M1);
    # M2 = nx.to_numpy_matrix(network2);
    # value2, vector2 = np.linalg.eig(M2);
    # print "A矩阵最大特征值", value1.max(), "B矩阵最大特征值", value2.max()
    try:
        network = copy.deepcopy(network1)
        eigenvector_one = nx.eigenvector_centrality_numpy(network1)
        x = find_max(eigenvector_one)
        eigenvector_two = nx.eigenvector_centrality_numpy(network2)
        y = find_max(eigenvector_two)
        print "CC竞争连接A网络", x, "B网络", y
    except Exception:
        print("competeCC error")
        return False
    num = network.number_of_nodes()
    network.add_edge(x, y + num)
    # network.add_edge(x, y + num);
    for i, j in network2.edges():
        network.add_edge(i + num, j + num)
    return network

# PP竞争
def compete_pp(network1, network2):
    # M1 = nx.to_numpy_matrix(network1);
    # value1, vector1 = np.linalg.eig(M1);
    # M2 = nx.to_numpy_matrix(network2);
    # value2, vector2 = np.linalg.eig(M2);
    # print "A矩阵最大特征值", value1.max(), "B矩阵最大特征值", value2.max()
    network = copy.deepcopy(network1)
    try:
        eigenvector_one = nx.eigenvector_centrality_numpy(network1)
        x = find_min(eigenvector_one)
        eigenvector_two = nx.eigenvector_centrality_numpy(network2)
        y = find_min(eigenvector_two)
        print "PP竞争连接A网络", x, "B网络", y
    except Exception:
        return False
    num = network.number_of_nodes()
    network.add_edge(x, y + num)
    for i, j in network2.edges():
        network.add_edge(i + num, j + num)
    return network


def paint1(network):
    pos = nx.spring_layout(network)  # positions for all nodes
    nx.draw(network, pos=pos)
    nx.draw_networkx_labels(network, pos=pos)
    nx.draw_networkx_edge_labels(network, pos=pos)
    plt.show()


# 切割网络,对不同数量的节点进行计算特征向量中心性

def compete(network, num1, num2, num3, num4):
    try:
        eigenvector = nx.eigenvector_centrality_numpy(network)
    except Exception:
        print "Error"
    sum1 = 0
    for k in range(0, num1):
        sum1 = sum1 + eigenvector[k]
    sum2 = 0
    for k in range(num1, num1 + num2):
        sum2 = sum2 + eigenvector[k]
    sum3 = 0
    for k in range(num1 + num2, num1 + num2 + num3):
        sum3 = sum3 + eigenvector[k]
    sum4 = 0
    for k in range(num1 + num2 + num3, num1 + num2 + num3 + num4):
        sum4 = sum4 + eigenvector[k]
    sum_all = sum1 + sum2 + sum3 + sum4
    return sum1 / sum_all, sum2 / sum_all, sum3 / sum_all, sum4 / sum_all
