from readint import readinput


def numpower(x, n):
    res = 1
    while n > 0:
        if n & 1:
            res = res * x
        x = x * x
        n = n >> 1
    return res


def test_numpower():
    while True:
        x = readinput("X")
        n = readinput("N")
        ans = numpower(x, n)
        print("%d^%d is: %d\n" % (x, n, ans))
        print("press \"n\" to exit, any other key to cont.")
        inp = input()
        if inp.strip() == 'n':
            break


def main():
    test_numpower()


if __name__ == '__main__':
    main()
