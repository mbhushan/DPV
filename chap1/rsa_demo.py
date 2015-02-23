from random_prime import random_prime
from readint import readinput
from gcd import gcd
from inverse_modulo import inverse_modulo
from modulo_expo import modular_exp


def relative_prime(x):
    e = 3
    for i in range(e, x):
        g = gcd(i, x)
        if g == 1:
            e = i
            break
    return e


def get_primenum():
    Y = 100000000000
    X = 1000000000
    p = random_prime(Y, X)
    return p


def send_message(e, N):
    print ("Alish wishes to send message x to Bob")
    print ("She looks up his public key (N, e) and sends him message"
           " y = x^e mod N")
    x = readinput("message x")
    y = modular_exp(x, e, N)
    return y


def main():
    print ("=============== RSA DEMO =================")
    print ("Bob chooses his public and secret keys")
    print ("He starts by picking 2 n-bit prime numbers 'p' & 'q'")
    p = get_primenum()
    q = get_primenum()
    print ("p: %d" % p)
    print ("q: %d" % q)
    N = p * q
    x = (p-1) * (q-1)
    e = relative_prime(x)
    print("His public key is (N, e) where N = pq and e is relative prime"
          " to (p-1)(q-1)")
    print ("(p-1)*(q-1): ", x)
    print ("N: ", N)
    print ("e: ", e)
    print ("His secret key is 'd', inverse of e modulo (p-1)(q-1)")
    d = inverse_modulo(e, x)
    print ("Secret key d: ", d)

    y = send_message(e, N)
    print ("Encoded mesage Y: ", y)
    print ("Finally Bob decodes the message by computing y^d mod N")
    msg = modular_exp(y, d, N)
    print ("Decoded message M: ", msg)


if __name__ == '__main__':
    main()
