from matrixmul import matrixmultiply
from readint import readinput
import math


def matrix_pow(M, n):
    res = [[1, 0], [0, 1]]
    while n > 0:
        if n & 1:
            res = matrixmultiply(res, M)
        M = matrixmultiply(M, M)
        n = n >> 1
    return res


def fibmatrix(n):
    """ initial matrix - derived from F1 = F1 and F2 = F1 + F0 """
    Mat = [[0, 1], [1, 1]]
    F = [[0], [1]]
    Fn = matrix_pow(Mat, n)
    ans = matrixmultiply(Fn, F)
    return ans[0]


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibmatrix(n)


def main():
    num = readinput("which fibonacci number")
    fib = fibonacci(num)
    print ("fib digit len: ", len(str(fib[0])))
    print ("%d fibonacci is: %d" % (num, fib[0]))
    print ("log(fib): ", math.log(fib[0], 2))


if __name__ == '__main__':
    main()
