from readint import readinput
from inverse_modulo import inverse_modulo


def checkinverses(n):
    count = 0
    for i in range(1, n+1):
        inv = inverse_modulo(i, n)
        if inv is not None:
            count += 1
    return count


def main():
    n = readinput("n value")
    count = checkinverses(n)
    print ("%d integers have inverses with modulo %d" % (count, n))


if __name__ == '__main__':
    main()
