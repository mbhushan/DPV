from readint import readinput
import sys
import math


def findfibonacci(num):
    if num <= 1:
        return num
    return findfibonacci(num - 1) + findfibonacci(num - 2)


def findfibopoly(num):
    if num <= 1:
        return num
    a = 0
    b = 1
    for n in range(num-1):
        f = a + b
        a = b
        b = f
    return f


def findfibexpr(num):
    if num <= 1:
        return num
    exp = 0.694 * num
    fib = int(math.floor(math.pow(2, exp)))
    return fib


def main():
    num = readinput()
    for n in range(num+1):
        fib = findfibonacci(n)
        sys.stdout.write(str(fib) + " "),
    sys.stdout.write("\n")
    print ("Finding fibonacci through expression 2**(0.694*n)")
    for n in range(num):
        fib = findfibexpr(n)
        sys.stdout.write(str(fib) + " "),
    sys.stdout.write("\n")

    print ("Enter number for fast fibonacci")
    num = readinput()
    fib = findfibopoly(num)
    print ("fib %d is: %d" % (num, fib))


if __name__ == '__main__':
    main()
