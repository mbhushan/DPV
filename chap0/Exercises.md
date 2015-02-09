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

```
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
```
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
13. Now F(k-1)/Fk is the golden ratio which is equal to ~ 1.61
14. 1 + 1.61 >= 1.414 # Hence proved!!
```
