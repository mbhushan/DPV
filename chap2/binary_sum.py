
def readinput(k):
    bstr = raw_input("Enter a binary string %s: " % k)
    return bstr


def bitsum(a, b, carry):
    """ assumes a, b and carry are single bits
    returns result = (sum of bits, carry) """
    result = (0, 0)
    c = a + b
    if c == 1 and carry == 0:
        result = 1, 0
    elif c == 1 and carry == 1:
        result = 0, 1
    elif c == 2 and carry == 0:
        result = 0, 1
    elif c == 2 and carry == 1:
        result = 1, 1
    elif c == 0:
        result = carry, 0
    else:
        print "sum: ", c, " carry: ", carry
        print "ERR: Should not have come here!"
    return result


def binsum(x, y):
    """ Assumes x and y are binary strings,
    returns sum of x and y as binary string """
    xlen = len(x)
    ylen = len(y)
    diff = abs(xlen - ylen)
    z = "0" * diff
    if xlen > ylen:
        y = z + y
    elif ylen > xlen:
        x = z + x
    print "x: ", x
    print "y: ", y
    result = []
    carry = 0
    for i in range(xlen-1, -1, -1):
        # print "x, y, carry: ", x[i], " ", y[i], " ", carry
        sm, carry = bitsum(int(x[i]), int(y[i]), carry)
        # print "sum: ", sm, " carry: ", carry
        result.append(sm)
    if carry == 1:
        result.append(carry)
    result = result[::-1]
    result = ''.join(str(r) for r in result)
    return result


def main():
    x = readinput("x")
    y = readinput("y")
    result = binsum(x, y)
    print "Sum is: ", result

if __name__ == '__main__':
    main()
