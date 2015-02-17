from readint import readinput


def modular_exp(x, y, N):
    """ given two n-bit integers x and N, an integer exponent y
    output: x^y mod N """
    if y == 0:
        return 1
    z = modular_exp(x, y//2, N)
    if y % 2 == 0:
        return (z*z) % N
    else:
        return (x*z*z) % N


def main():
    x = readinput("X")
    y = readinput("Y")
    N = readinput("N")
    ans = modular_exp(x, y, N)
    print ("(%d^%d) %% %d = %d" % (x, y, N, ans))


if __name__ == '__main__':
    main()
