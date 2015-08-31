from binary_sum import binsum


def readinput(k):
    data = raw_input("Enter binary string %s: " % k)
    return data


def two_complement(k):
    klen = len(k)
    result = []
    for i in range(klen):
        if int(k[i]) == 0:
            result.append('1')
        else:
            result.append('0')

    one = "1"
    result = ''.join(result)
    result = binsum(result, one)
    return result


def bin_subtract(x, y):
    """ assumes x and y are binary strings """
    xlen = len(x)
    ylen = len(y)
    diff = abs(xlen - ylen)
    z = "0" * diff
    print "Z: ", z
    if xlen > ylen:
        y = z + y
    elif xlen < ylen:
        x = z + x
    print "X: ", x
    print "Y: ", y
    yc = two_complement(y)
    print "Y 2 complement: ", yc
    result = binsum(x, yc)
    print "result: ", result


def main():
    x = readinput("X")
    y = readinput("Y")
    # print "Y 2 complement: ", two_complement(y)
    bin_subtract(x, y)
    # result = bin_subract(x, y)
    # print "X - Y = ", result


if __name__ == '__main__':
    main()
