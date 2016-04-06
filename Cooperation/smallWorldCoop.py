# coding=utf-8
import random

from cooperation import *
from matplotlib.ticker import MultipleLocator
import networkx as nx
import numpy as np

__author__ = 'zjutK'


def paint2(M, C1, C2, C3, C4):
    plt.xlabel('m')
    plt.ylabel('C')
    plt.xlim(7.0, 8.8)
    plt.ylim(0, 1)
    ax = plt.gca()
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    plt.scatter(M, C1, label="A", color="red")
    plt.scatter(M, C2, label="B", color="black")
    plt.scatter(M, C3, label="C", color="blue")
    plt.scatter(M, C4, label="D", color="green")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    M = []
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    for i in range(1, 100):
        try:
            SM1 = nx.read_adjlist("RandomBAData/7.69.adjlist", nodetype=int)
            SM2 = nx.random_graphs.newman_watts_strogatz_graph(200, 6, round(random.uniform(0.15, 0.4), 2))
            M2 = nx.to_numpy_matrix(SM2)
            value2, vector2 = np.linalg.eig(M2)
            print "A矩阵最大特征值", 7.69, "B矩阵最大特征值", value2.max()
            coop_1 = cooperation_cc(SM1, SM2)
            coop_2 = cooperation_pp(SM1, SM2)
            compete_network = compete_cc(coop_1, coop_2)
            if compete_network is False:
                continue
            A, B, C, D = compete(compete_network, 200, 200, 200, 200)
            C1.append(A)
            C2.append(B)
            C3.append(C)
            C4.append(D)
            M.append(value2.max())
        except Exception:
            continue
    paint2(M, C1, C2, C3, C4)
