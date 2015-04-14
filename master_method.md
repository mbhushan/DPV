Master Method:
================================================
Master Method is a direct way to get the recurrence solution. The master method works only for following type of recurrences or for recurrences that can be transformed to following type.

T(n) = aT(n/b) + f(n) where a >= 1 and b > 1

There are following three cases:
1. If f(n) = Θ(n^c) where c < logb(a) then T(n) = Θ(n^(logb(a)))

2. If f(n) = Θ(n^c) where c = logb(a) then T(n) = Θ(n^c * (logn))

3. If f(n) = Θ(n^c) where c > logb(a) then T(n) = Θ(f(n))
