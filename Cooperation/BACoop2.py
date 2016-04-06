# coding=utf-8
import numpy as np

from cooperation import *
__author__ = 'zjutK'

def paint2(M,C1,C2,C3,C4):
    plt.xlabel('m')
    plt.ylabel('C')
    plt.xlim(7.0,8.8)
    plt.ylim(0, 1)
    ax = plt.gca()
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    plt.scatter(M, C1,label="A",color="red")
    plt.scatter(M, C2,label="B",color="black")
    plt.scatter(M, C3,label="C",color="blue")
    plt.scatter(M, C4,label="D",color="green")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    M=[]
    C1=[]
    C2=[]
    for i in range(1, 100):
        try:
            BA1 = nx.read_adjlist("RandomBAData/7.69.adjlist", nodetype=int);
            BA2 = nx.random_graphs.barabasi_albert_graph(200, 2)
            M2 = nx.to_numpy_matrix(BA2)
            value2, vector2 = np.linalg.eig(M2)
            print "A矩阵最大特征值", 7.69, "B矩阵最大特征值", value2.max()
            coop1 = cooperation_cc(BA1, BA2)
            coop2 = cooperation_pp(BA1, BA2)
            compe = compete_cc(coop1, coop2)
            A,B,C,D=compete(compe, 200, 200, 200, 200)
            M.append(value2.max())
        except Exception:
            continue

    paint2()
    # paint1(compe)



    # paint(star1)
