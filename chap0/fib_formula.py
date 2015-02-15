from readint import readinput
import math


def get_fibonacci(num):
    x = (1 + math.sqrt(5))/2
    y = (1 - math.sqrt(5))/2
    u = (1/math.sqrt(5)) * math.pow(x, num)
    v = (1/math.sqrt(5)) * math.pow(y, num)
    ans = u - v
    return ans


def main():
    num = readinput("which fibonacci? ")
    fib = get_fibonacci(num)
    print ("%d fibonacci: %d" % (num, fib))


if __name__ == '__main__':
    main()
