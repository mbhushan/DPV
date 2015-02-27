# empirical study of log(n!) = Θ(nlog(n))
from readint import readinput
import math


def factorial(n):
    if n == 0 or n == 1:
        return 1
    fact = 1
    while n > 1:
        fact *= n
        n -= 1
    return fact


def test_expression(n):
    # evaluate log(n!)
    nfact = factorial(n)
    print ("n! is: ", nfact)
    logn_fact = math.log(nfact, 2)
    nlogn = n * math.log(n, 2)
    print ("log(n!): %.2f" % logn_fact)
    print ("nlog(n): %.2f" % nlogn)


def main():
    print("empirical study of log(n!) = Θ(nlog(n))")
    n = readinput("n value")
    test_expression(n)


if __name__ == '__main__':
    main()
