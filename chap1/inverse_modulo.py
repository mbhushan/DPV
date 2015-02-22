from readint import readinput
from extended_euclid import extended_euclid


def main():
    print ("To calculate: X^(-1) mod N")
    x = readinput("X")
    n = readinput("N")
    ans = extended_euclid(x, n)
    if ans[0] > 0:
        print ("Ans: ", ans[0])
    else:
        print ("Ans: ", (ans[0] + n))


if __name__ == '__main__':
    main()
