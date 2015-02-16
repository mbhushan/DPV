from readint import readinput


def french_mult(x, y):
    """ assumes input as 2 n-bit integers x and y where y >= 0
    returns their product. """
    if y == 0:
        return 0
    z = french_mult(x, y//2)
    if y % 2 == 0:
        return 2*z
    else:
        return x + 2*z


def main():
    x = readinput("X: ")
    y = readinput("Y: ")
    ans = french_mult(x, y)
    print ("%d x %d: %d" % (x, y, ans))


if __name__ == '__main__':
    main()
