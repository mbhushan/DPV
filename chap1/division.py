from readint import readinput


def division(x, y):
    """ input: 2 n-bit integers x and y, where y >= 1
    output: quotient and remainder when x divided by y. """
    if x == 0:
        return (0, 0)
    q, r = division(x//2, y)
    q = 2*q
    r = 2*r
    if (x % 2) == 1:
        r = r + 1
    if r >= y:
        r = r - y
        q = q + 1
    return (q, r)


def main():
    x = readinput("X")
    y = readinput("Y")
    ans = division(x, y)
    print("%d / %d = Quotient: %d, Remainder: %d" % (x, y, ans[0], ans[1]))


if __name__ == '__main__':
    main()
