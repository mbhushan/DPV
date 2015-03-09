from readint import readinput
from extended_euclid import extended_euclid
from gcd import gcd


def inverse_modulo(x, n):
    a, b = x, n
    if n > x:
        a, b = b, a
    result = gcd(a, b)
    if result != 1:
        # print ("As gcd(%d, %d) != 1, the inverse does not exists" % (x, n))
        return None

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
