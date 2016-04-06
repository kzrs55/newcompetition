#coding=utf-8
import random

from BACoop import cooperationCC, compete, paint2
from BACoop import cooperationPP
from BACoop import competeCC

__author__ = 'zjutK'
import copy

from matplotlib.ticker import MultipleLocator

__author__ = 'zjutK'
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
    M=[]
    C1=[]
    C2=[]
    C3=[]
    C4=[]
    for i in range(1,100):
        try:
            SM1=nx.read_adjlist("RandomBAData/7.69.adjlist",nodetype=int);
            SM2=nx.random_graphs.newman_watts_strogatz_graph(200, 6, round(random.uniform(0.15, 0.4), 2));
            M2=nx.to_numpy_matrix(SM2);
            value2, vector2 = np.linalg.eig(M2);
            print "A矩阵最大特征值",7.69,"B矩阵最大特征值",value2.max()
            coop1=cooperationCC(SM1,SM2)
            coop2=cooperationPP(SM1,SM2)
            compe=competeCC(coop1,coop2)
            A,B,C,D=compete(compe,200,200,200,200)
            C1.append(A)
            C2.append(B)
            C3.append(C)
            C4.append(D)
            M.append(value2.max())
        except Exception:
            continue
    paint2(M,C1,C2,C3,C4)
