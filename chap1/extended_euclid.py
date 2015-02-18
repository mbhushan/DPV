from readint import readinput


def extended_euclid(a, b):
    """ Two positive integers a and b such that a >= b >= 0
    output: integers x, y, d such that ax + by =d where d = gcd(a, b) """
    if b == 0:
        return (1, 0, a)
    x, y, d = extended_euclid(b, a % b)
    return (y, x - (a//b)*y, d)


def main():
    a = readinput("a")
    b = readinput("b")
    (x, y, d) = extended_euclid(a, b)
    print ("ax + by = d")
    print ("x=%d, y=%d, d=%d" % (x, y, d))


if __name__ == '__main__':
    main()
