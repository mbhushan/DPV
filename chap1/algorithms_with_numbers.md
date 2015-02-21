Chapter 1 - Algorithms with Numbers Notes
==========================================

```py
Factoring is hard. Despite centuries of effort by some of the world’s smartest mathematicians 
and computer scientists, the fastest methods for factoring a number N take time exponential in 
the number of bits of N.

How many digits are needed to represent the number N ≥ 0 in base b? Let’s see—with k
digits in base b we can express numbers up to b^k − 1; for instance, in decimal, three digits get
us all the way up to 999 = 10^3 − 1. By solving for k, we find that LOGb(N + 1) digits (about
log b N digits, give or take 1) are needed to write N in base b.
```
```py
Two’s complement
Modular arithmetic is nicely illustrated in two’s complement, the most common format for
storing signed integers. It uses n bits to represent numbers in the range [−2^(n−1) , 2^(n−1) − 1]
and is usually described as follows:
• Positive integers, in the range 0 to 2^(n−1) − 1, are stored in regular binary and have a
leading bit of 0.
• Negative integers −x, with 1 ≤ x ≤ 2^(n−1) , are stored by first constructing x in binary,
then flipping all the bits, and finally adding 1. The leading bit in this case is 1.
(And the usual description of addition and multiplication in this format is even more arcane!)
```
```py
Here’s a much simpler way to think about it: any number in the range −2^(n−1) to 2^(n−1) − 1
is stored modulo 2^n . Negative numbers −x therefore end up as 2^n − x. Arithmetic operations
like addition and subtraction can be performed directly in this format, ignoring any overflow
bits that arise.
```
```py
Modular division theorem For any a mod N , a has a multiplicative inverse modulo N if
and only if it is relatively prime to N . When this inverse exists, it can be found in time O(n^3)
(where as usual n denotes the number of bits of N ) by running the extended Euclid algorithm.
This resolves the issue of modular division: when working modulo N , we can divide by
numbers relatively prime to N —and only by these. And to actually carry out the division, we
multiply by the inverse.
```
```py
Modern cryptography is about the following important idea: 
factoring is hard and primality is easy. We cannot factor large numbers,
but we can easily test huge numbers for primality! (Presumably, if a number is composite,
such a test will detect this without finding a factor.)
```
```py
The problem is that Fermat’s theorem is not an if-and-only-if condition; it doesn’t say what
happens when N is not prime.
It turns out that certain extremely rare composite numbers N , called Carmichael numbers, 
pass Fermat’s test for all a relatively prime to N . On such numbers our algorithm will
fail; but they are pathologically rare.
```
```py
Carmichael Numbers:
We are ignoring Carmichael numbers, so we can now assert
If N is prime, then a^(N−1) ≡ 1 mod N for all a < N .
If N is not prime, then a^(N−1) ≡ 1 mod N for at most half the values of a < N .
```
```py
a random n-bit number has roughly a one-in-n chance of being prime (actually about 1/(ln(2^n)) ≈ 1.44/n). For instance,
about 1 in 20 social security numbers is prime!

Lagrange’s prime number theorem: Let π(x) be the number of primes ≤ x . 
Then π(x) ≈ x/(ln x) , or more precisely,
lim(x→∞) (π(x) / (x/lnx)) = 1
```
```py
RSA:
Bob chooses his public and secret keys.
• He starts by picking two large (n-bit) random primes p and q.
• His public key is (N, e) where N = pq and e is a 2n-bit number relatively prime to
(p − 1)(q − 1). A common choice is e = 3 because it permits fast encoding.
• His secret key is d, the inverse of e modulo (p − 1)(q − 1), computed using the extended
Euclid algorithm.
Alice wishes to send message x to Bob.
• She looks up his public key (N, e) and sends him y = (x^e mod N ), computed using an
efficient modular exponentiation algorithm.
• He decodes the message by computing y^d mod N .
```
