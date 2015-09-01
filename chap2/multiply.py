from readint import readinput


def multiply(x, y):
    """ Input: positive integers x and y, in binary
    output: their product """
    xlen = len(x)
    ylen = len(y)
    n = max(xlen, ylen)
    if n == 1:
        return int(x) * int(y)
    m = n/2
    xL, xR = x[:m], x[m:]
    yL, yR = y[:m], y[m:]

    P1 = multiply(xL, yL)
    P2 = multiply(xR, yR)
    P3 = multiply(xL+xR, yL+yR)

    print ("maxlen is: ", maxlen)
    return result


def main():
    a = readinput("x value")
    b = readinput("y value")
    x = bin(a)
    y = bin(b)
    x = x[2:]
    y = y[2:]
    ans = multiply(x, y)
    print ("x in bin: ", x)
    print ("y in bin: ", y)
    print ("x * y = ", ans)


if __name__ == '__main__':
    main()
