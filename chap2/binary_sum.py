
def readinput(k):
    bstr = raw_input("Enter a binary string %s: " % k)
    return bstr


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


def main():
    x = readinput("x")
    y = readinput("y")
    binsum(x, y)

if __name__ == '__main__':
    main()
