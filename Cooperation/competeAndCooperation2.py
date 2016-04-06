# coding=utf-8
from BACoop import *

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
    M = []
    for i in range(3, 500):
        try:
            number1 = i
            print number1
            number2 = 100
            star1 = creat_star(number1);
            star2 = creat_star(number2)
            coop1 = cooperation_cc(star1, star2)
            coop2 = cooperation_pp(star1, star2)
            compe = compete_cc(coop1, coop2)
            compete(compe, number1, number2, number1, number2)
            M.append(i)
        except Exception:
            continue

    paint2()
    # paint1(compe)



    # paint(star1)
