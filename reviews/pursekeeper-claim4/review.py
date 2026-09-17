#!/usr/bin/env python3
import itertools
import json

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

try:
    from sympy import isprime as _sympy_isprime
except ImportError:
    _sympy_isprime = None

MR_BASES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

def is_probable_prime(n):
    if n < 2:
        return False
    small = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small:
        if n == p:
            return True
        if n % p == 0:
            return False
    d, s = n - 1, 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in MR_BASES:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def egcd(a, b):
    if b == 0:
        return (a, 1, 0)
    g, x, y = egcd(b, a % b)
    return g, y, x - (a // b) * y

def inv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise ValueError("not invertible")
    return x % m

def crt_pair(a, m, b, n):
    t = ((b - a) * inv(m % n, n)) % n
    return (a + m * t) % (m * n), m * n

def residue_for(signs, primes):
    r, mod = 0, 1
    for sign, q in zip(signs, primes):
        qmod = 8 if q == 2 else q ** 3
        target = 1 if sign > 0 else qmod - 1
        r, mod = crt_pair(r, mod, target, qmod)
    return r, mod

def primality(n):
    return bool(_sympy_isprime(n)) if _sympy_isprime is not None else is_probable_prime(n)

def smallest(n):
    primes = PRIMES[:n]
    best = None
    modulus = None
    checked = 0
    for signs in itertools.product((-1, 1), repeat=n):
        r, mod = residue_for(signs, primes)
        modulus = mod
        checked += 1
        candidate = r if r > 1 else r + mod
        while best is None or candidate < best:
            if primality(candidate):
                best = candidate
                break
            candidate += mod
    if best is None:
        raise RuntimeError(f"no prime found for n={n}")
    literal_ok = all(
        pow(best, q * q, q ** 5) in (1, q ** 5 - 1)
        for q in primes
    )
    return {
        "n": n,
        "value": int(best),
        "modulus": int(modulus),
        "classes_checked": checked,
        "prime": bool(primality(best)),
        "literal_condition": literal_ok,
        "below_modulus": best < modulus,
    }

def main():
    rows = [smallest(n) for n in range(1, len(PRIMES) + 1)]
    print(json.dumps({"primality_backend": "sympy.isprime" if _sympy_isprime is not None else "20-base Miller-Rabin", "values": [r["value"] for r in rows], "checks": rows}, sort_keys=True))

if __name__ == "__main__":
    main()



