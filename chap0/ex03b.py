from fibonacci import findfibopoly
from readint import readinput
import math


def findconstant(num):
    """ Find a constant c < 1 such that Fn ≤ 2^(c*n) for all n ≥ 0.
    Show that your answer is correct.
    Above equation can be written as - taking log on both sides
    1. log(Fn) <= (c*n)log(2)
    2. c >= log(Fn)/n # since log(2) is 1
    Now lets find this ratio - log(Fn)/n for different values of n
    and see if get our 'c'
    """
    clist = []
    for n in range(1, num, 1000):
        fn = findfibopoly(n)
        c = math.log(fn, 2)/n
        clist.append(round(c, 2))
    return clist


def verifyc(c, num):
    dealbreaker = []
    for n in range(num+1):
        fn = findfibopoly(n)
        cn = 2 ** (c * n)
        fn = round(fn, 2)
        cn = round(cn, 2)
        if fn > cn:
            dealbreaker.append((fn, cn))
        # print ("%d:%0.2f" % (fn, cn))
    print ("Deal Breakers: ", dealbreaker)
    if len(dealbreaker) == 0:
        print ("Q.E.D")
    else:
        print (":( - ERROR! Explore more!")


def main():
    num = readinput()
    clist = findconstant(num)
    print ("showing c values: ")
    print (clist)

    c = clist[-1]
    print ("Now Lets verify if for c=%0.2f the equation Fn <= 2^(c*n) holds" %
           (c))
    print ("First lets choose \"n\" value")
    num = readinput()
    verifyc(c, num)


if __name__ == '__main__':
    main()
