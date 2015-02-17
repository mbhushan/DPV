from readint import readinput


def gcd(x, y):
    """ input: 2 integers x and y with x >= y >= 0
    output: greatest common divisor of x and y """
    if (y == 0):
        return x
    return gcd(y, x % y)


def main():
    x = readinput("x")
    y = readinput("y")
    if y > x:
        x, y = y, x
    ans = gcd(x, y)
    print ("GCD of %d and %d = %d" % (x, y, ans))


if __name__ == '__main__':
    main()
