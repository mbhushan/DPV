def readbinary():
    while True:
        found = True
        num = input()
        for n in num:
            if n != '1' and n != '0':
                print ("Bad input. Try again..")
                found = False
                break
        if found:
            return num


def binary_sum(bin1, bin2):
    b1len = len(bin1)
    b2len = len(bin2)

    index = 1
    carry = '0'
    bsum = '0'
    total = []
    while index <= b1len and index <= b2len:
        x = bin1[-index]
        y = bin2[-index]
        bsum, carry = binsum(x, y, carry)
        total.append(bsum)
        index += 1
    for n in range(index, b1len+1):
        bsum, carry = binsum(bin1[-n], '0', carry)
        total.append(bsum)
    for n in range(index, b2len+1):
        bsum, carry = binsum(bin2[-n], '0', carry)
        total.append(bsum)
    if carry == '1':
        total.append(carry)
    result = ''.join(total)
    result = result[::-1]
    # print ("result: ", result)
    return result


def binsum(x, y, carry):
    bsum = 0
    if x == '0' and y == '0' and carry == '0':
        bsum = '0'
        carry = '0'
    elif x == '0' and y == '0' and carry == '1':
        bsum = '1'
        carry = '0'
    elif x == '1' and y == '0' and carry == '0':
        bsum = '1'
        carry = '0'
    elif x == '1' and y == '0' and carry == '1':
        bsum = '0'
        carry = '1'
    elif x == '0' and y == '1' and carry == '0':
        bsum = '1'
        carry = '0'
    elif x == '0' and y == '1' and carry == '1':
        bsum = '0'
        carry = '1'
    elif x == '1' and y == '1' and carry == '0':
        bsum = '0'
        carry = '1'
    elif x == '1' and y == '1' and carry == '1':
        bsum = '1'
        carry = '1'
    return (bsum, carry)


def main():
    print ("Enter first binary number: ")
    bin1 = readbinary()
    print ("Enter second binary number: ")
    bin2 = readbinary()
    binsum = binary_sum(bin1, bin2)
    print ("%s + %s = %s" % (bin1, bin2, binsum))


if __name__ == '__main__':
    main()
