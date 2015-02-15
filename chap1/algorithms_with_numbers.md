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
