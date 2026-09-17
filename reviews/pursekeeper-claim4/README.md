# pursekeeper claim 4 independent review

Independent re-derivation of `pursekeeper/claims#3`.

The program reduces the congruence to the valid residue classes `p = ±1 mod q^3` for odd q and `p = ±1 mod 8` for q=2, enumerates every CRT sign class, and searches each arithmetic progression until it cannot beat the current minimum. It then verifies the original `p^(q^2) = ±1 mod q^5` condition directly for every q.

In the pursekeeper sandbox the code uses `sympy.isprime`; outside that environment it has a fixed-base Miller-Rabin fallback for local checking.

Local output reproduced the full sequence:

`7, 271, 1999, 85751, 1329668999, 8655839869249, 2610206352778751, 108845238471360544999, 111565602115338275478001, 698835425792323980459725999`

Verdict: reproduces the full claim through a(10).
