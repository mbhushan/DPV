"So what's up with that triple equal sign?"
===============================================

To insert special characters press "^K" in insert mode and then type the digraph characters.

```py
When most students first study modular math and see the congruency symbol (≡ ), it's not entirely clear what the difference is between it 
and a regular equal sign. The purpose of this page is to give a brief discussion of what it means to be "congruent modulo n", and how this is vastly different than the "equals" we have known since grade school or before.

The idea of modular arithmetic is simple enough. We know from the Division Theorem that for any two integers a and b, with b positive, we 
can write a as the product of b and some other integer plus a remainder. That is, a = bq + r, with 0 <= r < d . This is a fancy way of 
describing the long division algorithm that we know from elementary school. For example, consider a = 15 and b = 4. We see that 15 = 4 * 3 + 3, which is another way of saying that 15 divided by 4 equals 3 plus a remainder of 3. Modular division returns just that remainder. So 15 mod 4 = 3. Similarly, 28 mod 6 = 4, since 28 = 6 * 4 + 4.

From "equals" to "congruent"

Since we understand modular division, what exactly does "15≡ 3(mod 4)" mean? For starters, we read this as "15 is congruent to 3 mod 4." 
Initially, the order seems a little confusing. We know that 15 mod 4 = 3, so what's the difference? The point of congruency is the following: If we say that a≡ b (mod n), this means that in the scope of "mod n", a and b are equivalent. How is this so? Consider an extension on 
the example above. We already know that 15≡ 3 (mod 4). We can also say that 15≡ 19 (mod 4), since 15 mod 4 gives the same result as 19 mod 4, namely 3. So 15 and 19 are congruent modulo 4 because both give the same remainder when divided by 4. Note that this is starkly different from "equals", since 15 mod 4 certainly does not "equal" 19. Formally, a≡ b (mod n) if n divides (a - b). Also, a≡ b (mod n) if and only if a mod n = b mod n. From the original example, 15≡ 3 (mod 4) since 4 | (15-3), and we see that 15 mod 4 = 3 mod 4 = 3.

Why is this useful?

Without getting into the details, this is useful because it allows us to put numbers into neatly defined "equivalence classes". Continuing on the example above, we quickly see that the following numbers are all congruent modulo 4: {..., -13, -9, -5, -1, 3, 7, 11, 15, 19, 23, ...}. The reason is that all give a remainder of 3 when divided by 4. If we had to select one number from this set as a "representative" for the set, we would most likely choose 3, since the only four possible results modulo 4 are {0, 1, 2, 3}. Now for the punchline: We can replace any number with a member of its equivalence class when doing modular arithmetic.

For example, consider 15 + 18 mod 4. Since 15  3 mod 4 and 18   2 mod 4, we expect that 3 + 2 mod 4 should have the same result as 15 + 18 mod 4. Indeed, 15 + 18 = 33, and 33 mod 4 is 1, just as 3 + 2 = 5, and 5 mod 4 is 1. This is not just a coincidence - it is the beauty of congruency.
```
