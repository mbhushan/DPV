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
