from readint import readinput
from modulo_expo import modular_exp
import random


def isprime(p):
    n = min(p, 100)
    for i in range(n):
        a = random.randint(1, p-1)
        lhs = modular_exp(a, p-1, p)
        if lhs != 1:
            return False
    return True


def main():
    print ("Fermat's little theorem for primality")
    print ("If p is prime then for every 1 <= a < p")
    print ("a^(p-1) ≡  1 (mod) p")
    p = readinput("prime candidate")
    if isprime(p):
        print ("%d is Prime Number" % p)
    else:
        print ("%d is Not a Prime Number" % p)


if __name__ == '__main__':
    main()
