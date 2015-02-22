from readint import readinput
from little_fermat import isprime
import random


def random_prime(num, y=2):
    while True:
        n = random.randint(y, num)
        if isprime(n):
            return n


def test_random_prime():
    pmap = {}
    num = 100
    for i in range(25000):
        p = random_prime(num)
        if p in pmap:
            pmap[p] += 1
        else:
            pmap[p] = 1
    print ("Total prime less than %d: %d" % (num, len(pmap)))
    for p in pmap:
        print("%d: %d" % (p, pmap[p]))


def main():
    num = readinput("n >= 2")
    p = random_prime(num)
    print ("Random Prime less than %d: %d" % (num, p))
    test_random_prime()


if __name__ == '__main__':
    main()
