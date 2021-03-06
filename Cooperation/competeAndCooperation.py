# coding=utf-8
from matplotlib.ticker import MultipleLocator

from cooperation import *

__author__ = 'zjutK'


def paint2(M, C1, C2, C3, C4):
    plt.xlabel('m')
    plt.ylabel('C')
    plt.xlim(0, 500)
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
    number2 = 100  # 对比星形网络数量
    star2 = creat_star(number2)
    M = []
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    for i in range(3, 500):
        try:
            number1 = i
            star1 = creat_star(number1);
            coop1 = cooperation_cc(star1, star2)
            coop2 = cooperation_pp(star1, star2)
            compe = compete_cc(coop1, coop2)
            A,B,C,D=compete(compe, number1, number2, number1, number2)
            C1.append(A)
            C2.append(B)
            C3.append(C)
            C4.append(D)
            M.append(i)
            print i
        except Exception:
            print 'error'
            continue

    paint2(M, C1, C2, C3, C4)
    # paint1(compe)



    # paint(star1)
