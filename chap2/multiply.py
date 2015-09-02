from readint import readinput
from binary_sum import binsum
from binary_subtract import bin_subtract


def multiply(x, y):
    """ Input: positive integers x and y, in binary
    output: their product """
    xlen = len(x)
    ylen = len(y)
    print "xlen:ylen :: ", xlen, ylen
    n = max(xlen, ylen)
    if n == 1:
        return str(int(x) * int(y))
    m = n/2
    xL, xR = x[:m], x[m:]
    yL, yR = y[:m], y[m:]

    P1 = multiply(xL, yL)
    P2 = multiply(xR, yR)
    P3 = multiply(binsum(xL, xR), binsum(yL, yR))

    P4 = binsum(P1, P2)
    a = P1 + ("0" * n)
    b = bin_subtract(P3, P4)
    b = b + ("0" * m)

    result = binsum(a, b)
    result = binsum(result, P2)
    # print ("maxlen is: ", maxlen)
    return result


def main():
    a = readinput("x value")
    b = readinput("y value")
    x = bin(a)
    y = bin(b)
    x = x[2:]
    y = y[2:]
    xlen = len(x)
    ylen = len(y)
    diff = abs(xlen - ylen)
    z = "0" * diff
    if xlen < ylen:
        x = z + x
    elif ylen < xlen:
        y = z + y
    ans = multiply(x, y)
    print ("x in bin: ", x)
    print ("y in bin: ", y)
    print ("x * y = ", ans)


if __name__ == '__main__':
    main()
