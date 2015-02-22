from readint import readinput
from extended_euclid import extended_euclid


def inverse_modulo(x, n):
    ans = extended_euclid(x, n)
    if ans[0] > 0:
        return ans[0]
    else:
        return (ans[0] + n)


def main():
    print ("To calculate: X^(-1) mod N")
    x = readinput("X")
    n = readinput("N")
    ans = inverse_modulo(x, n)
    print ("Ans: ", ans)


if __name__ == '__main__':
    main()
