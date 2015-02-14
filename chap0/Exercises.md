Chapter 0 - Prologue: Solutions
=============================================

```
0.1. In each of the following situations, indicate whether f = O(g), or f = Ω(g),
or both (in which case f = Θ(g)).

> Graphs are drawn using: http://fooplot.com/
```

```py
a. f(n) = n-100 and g(n) = n-200
sol: f = Θ(g)
graph file: DPV/chap0/01a.pdf
```
```py
b. f(n) = n^(1/2) and g(n) = n^(2/3)
sol: f = O(g)
graph file: DPV/chap0/01b.pdf
red line: f(n)
blue line: g(n)
```
```py
c. f(n) = 100*n + log(n) and g(n) = n + (logn)^2
sol: f = Ω(g)
graph file: DPV/chap0/01c.pdf
red line: f(n)
blue line: g(n)
```
```py
d. f(n) = n*log(n) and g(n) = 10*n*log(10*n)
sol: f = O(g)
graph file: DPV/chap0/01d.pdf
red line: f(n)
blue line: g(n)
```
```py
e. f(n) = log(2*n) and g(n) = log(3*n)
sol: f = Θ(g)
graph file: DPV/chap0/01e.pdf
red line: f(n)
blue line: g(n)
```
```py
f. f(n) = 10*log(n) and g(n) = log(n*n)
sol: f = Θ(g)
graph file: DPV/chap0/01f.pdf
red line: f(n)
blue line: g(n)
```
```py
g. f(n) = n^(1.01) and g(n) = n*(log(n))^2
sol: f = O(g)
graph file: DPV/chap0/01g.pdf
red line: f(n)
blue line: g(n)
```
```py
h. f(n) = (n^2)/log(n) and g(n) = n*(log(n))^2
sol: f = Ω(g)
graph file: DPV/chap0/01h.pdf
red line: f(n)
blue line: g(n)
```
```py
i. f(n) = n^(0.1) and g(n) = (log(n))^10
sol: f = O(g)
graph file: DPV/chap0/01i.pdf
red line: f(n)
blue line: g(n)
```
```py
j. f(n) = (log(n))^log(n) and g(n) = n/(log(n))
sol: f = O(g)
graph file: DPV/chap0/01j.pdf
red line: f(n)
blue line: g(n)
```
```py
k. f(n) = n^(1/2) and g(n) = (log(n))^3
sol: f = Ω(g)
graph file: DPV/chap0/01k.pdf
red line: f(n)
blue line: g(n)
```
```py
l. f(n) = n^(1/2) and g(n) = 5^(log(n))
sol: f = O(g)
graph file: DPV/chap0/01l.pdf
red line: f(n)
blue line: g(n)
```
```py
m. f(n) = n*(2^n) and g(n) = 3^n
sol: f = O(g)
graph file: DPV/chap0/01m.pdf
red line: f(n)
blue line: g(n)
```
```py
n. f(n) = 2^n and g(n) = 2^(n+1)
sol: f = Θ(g)
graph file: DPV/chap0/01n.pdf
red line: f(n)
blue line: g(n)
```
```py
o. f(n) = n! and g(n) = 2^n
sol: f = Ω(g)
graph file: DPV/chap0/01o.pdf
red line: f(n)
blue line: g(n)
```
```py
p. f(n) = (log(n))^(log(n)) and g(n) = 2^((log(n))^2)
sol: f = O(g)
graph file: DPV/chap0/01p.pdf
red line: f(n)
blue line: g(n)
```
```py
q. f(n) = sigma(i=1,n)(i^k) and g(n) = n^(k+1)
sol: f = O(g)
graph file: no graph - let me know if you plotted somewhere.
red line: f(n)
blue line: g(n)
```

```py
0.2. Show that, if c is a positive real number, then g(n) = 1 + c + c^2 + · · · + c^n is:
(a) Θ(1) if c < 1.
(b) Θ(n) if c = 1.
(c) Θ(c n ) if c > 1.
The moral: in big-Θ terms, the sum of a geometric series is simply the first term 
if the series is strictly decreasing, the last term if the series is strictly increasing,
or the number of terms if the series is unchanging.

sol: experimental validation is written in sol0_2.py - run it with different values of n 
and check for yourself.
```
```py
0.3. The Fibonacci numbers F0 , F1 , F2 , . . . , are defined by the rule
F0 = 0, F1 = 1, Fn = F(n−1) + F(n−2) .
In this problem we will confirm that this sequence grows exponentially fast and obtain some
bounds on its growth.

(a) Use induction to prove that Fn ≥ 2^(0.5*n) for n ≥ 6.
sol a. 
1. First 6 terms of the fibonacci are: 1, 1, 2, 3, 5, 8
2. Base case, n=6:
3. F6 = 8 
4. 2^(0.5*6) = 2^(3.0) = 8
5. Hence, base case is true ie F6 >= 2^(0.5*6)

6. Lets assume the equality is true for any k ie Fk >= 2^(0.5*k)
7. we need to check if it holds for (k+1) as well. Lets check it out.
8. F(k+1) = Fk + F(k-1)
9. 2^(0.5*(k+1)) = 2^(0.5*k + 0.5) = 2^(0.5*k) * 2^(0.5) 
10. Fk + F(k-1) >= 2^(0.5*k) * 2^(0.5) # from 8 and 9
11. Fk + F(k-1) >= Fk * 2^(0.5) # from 6.
12. 1 + F(k-1)/Fk >= sqrt(2) # dividing LHS by Fk
13. Now F(k-1)/Fk is the golden ratio which is equal to ~ 0.61
14. 1 + 0.61 >= 1.414 # Hence proved!!
```
```py
(b) Find a constant c < 1 such that Fn ≤ 2^(c*n) for all n ≥ 0. Show that your answer is correct.
sol b.
1. Fk + F(k-1) <= Fk * 2^c # from 11 of a. - reversed equality sign
2. 2^c >= 1 + F(k-1)/Fk
3. 2^c >= 1 + 0.61 # golden ratio is 0.61
4. c >= log(1.61) # taking log both sides
5. c >= 0.69 # log base 2 of 1.61
refer to the python script ex03b.py for experimental validation
```
```py
(c) What is the largest c you can find for which Fn = Ω(2^(c*n))?
sol c. Largest c value for which Fn = Ω(2^(c*n)) is 0.69. Please run the code in ex03b.py 
with c = 0.69 You will see that post 274th fibonacci Fn is much greater than 2^(c*n)
```
```py
0.4. Is there a faster way to compute the nth Fibonacci number than by fib2 (page 13)? One idea
involves matrices. We start by writing the equations F1 = F1 and F2 = F0 + F1 in matrix notation:
[[F1], [F2]] = [[0,1], [1, 1]] * [[F0], [F1]]
Similarly,
[[F2], [F3]] = [[0,1], [1, 1]] * [[F1], [F2]] = [[0,1], [1, 1]]^2 * [[F0], [F1]]
In general,
[[Fn], [F(n+1)]] = [[0,1], [1, 1]]^n * [[F0], [F1]]
So, in order to compute F n , it suffices to raise this 2 × 2 matrix, call it X, to the nth power.

(a) Show that two 2 × 2 matrices can be multiplied using 4 additions and 8 multiplications.
1. matrix A = [[a, b], [c, d]]
2. matrix B = [[x, y], [u, v]]
3. A * B = [[(a*x + b*u), (a*y+ b*v)], [(c*x + d*u), (c*y + d*v)]]
4. As we can see in step 3. We have 4 additions and 8 multiplications for multiplying two 2x2 matrices.
generic matrix multiplication is implemented in matrixmul.py
```
```py
But how many matrix multiplications does it take to compute X^n ?
(b) Show that O(log(n)) matrix multiplications suffice for computing X^n.(Hint: Think about computing X^8)
sol: Algorithm is implemented in numpower.py
Outline is below for computing X^n:
1. n can be written as power of 2. ie
n = 2^k1 + 2^k2 + 2^k3 ... + 2^km
2. So X^n can be expressed as:
X = X^(2^k1) * X^(2^k2) ... X^(2^km)

eg.
n = 25 = (11001)
X^n = X^25 = X^16 * X^8 * X^1

Conclusion: X^n can be determined by looking at each bit in binary representation of n, and multiplying all
X^(2^ki) together, where ki is the bit position of the ith standing bit.
```
```py 
Thus the number of arithmetic operations needed by our matrix-based algorithm, call it fib3, is
just O(log n), as compared to O(n) for fib2. Have we broken another exponential barrier?
The catch is that our new algorithm involves multiplication, not just addition; and multiplications 
of large numbers are slower than additions. We have already seen that, when the complexity 
of arithmetic operations is taken into account, the running time of fib2 becomes O(n^2).

(c) Show that all intermediate results of fib3 are O(n) bits long.
sol: You can validate this experimentally from fib_matrix.py
```
```py
(d) Let M(n) be the running time of an algorithm for multiplying n-bit numbers, and assume
that M(n) = O(n^2) (the school method for multiplication, recalled in Chapter 1, achieves
this). Prove that the running time of fib3 is O(M(n)logn).
```
