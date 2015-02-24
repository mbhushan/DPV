# we show here that any binary number is atmost 4 times as corresponding
# decimal number. We also figure out the ratio of these lengths for very
# large numbers.
from readint import readinput


def tobinary(dec):
    blist = []
    while dec > 0:
        n = dec % 2
        dec = dec // 2
        blist.append(n)
    if dec == 1:
        blist.append(dec)
    blist = blist[::-1]
    blist = [str(i) for i in blist]
    ans = ''.join(blist)
    return ans


def test_binary_converter():
    num = readinput("decimal number")
    bnum = tobinary(num)
    print ("binary: ", bnum)


def test_ratio():
    dec = 1000000000
    low = 1
    max_num = 10000000000
    step = 1000000000
    print ("Max Ratio of binary length to corresponding decimal number digits")
    while dec <= max_num:
        max_ratio = 1
        for i in range(low, dec, 100000):
            bnum = tobinary(i)
            ratio = len(bnum) / len(str(i))
            ratio = round(ratio, 2)
            if ratio > 4:
                print ("R: %d: %s" % (i, bnum))
            if ratio > max_ratio:
                max_ratio = ratio
        print ("Range %d to %d, Max Ratio: %0.2f" % (low, dec, max_ratio))
        low = dec
        dec = dec + step
    print ("Checking Ratio for very large numbers")
    dec = 1000000000000000000000000000000000000000000000000000000000000000000000
    low = 100000000000000000000000000000000000000000000000000000000000000000000
    for i in range(low, dec+1, low):
        bnum = tobinary(i)
        ratio = len(bnum) / len(str(i))
        ratio = round(ratio, 2)
        print ("%d Ratio: %0.2f" % (i, ratio))


def main():
    test_binary_converter()
    test_ratio()


if __name__ == '__main__':
    main()
