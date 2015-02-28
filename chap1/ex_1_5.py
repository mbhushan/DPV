import math
from readint import readinput


def harmonic_series(num):
    n = num
    i = 1
    total = 0
    while i <= n:
        total += (1/i)
        i += 1
    total = round(total, 2)

    print ("Harmonic series: 1 + 1/2 + 1/3 + 1/4 + 1/5 ...")
    print ("Summation of harmonic series")
    print ("∑(1/i) = ", total)
    gamma = 0.57721
    lnn = math.log(n, math.e)
    rhs = gamma + lnn
    rhs = round(rhs, 2)
    print ("ln(n) + γ: ", rhs)
    logn = math.log(n, 2)
    logn = round(logn, 2)
    print ("log(n): ", logn)


def main():
    num = readinput("n value for series")
    harmonic_series(num)


if __name__ == '__main__':
    main()
