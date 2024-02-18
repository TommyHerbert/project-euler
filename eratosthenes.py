import time, math

def test(ceiling):
    start = time.time()
    sieve(ceiling)
    return time.time() - start


def sieve(ceiling):
    primes = [2]
    for n in range(3, ceiling, 2):
        if not known_factors(n, primes):
            primes.append(n)
    return primes


def known_factors(n, primes):
    root = math.sqrt(n)
    for p in primes:
        if n % p == 0:
            return True
        if p > root:
            return False
    return False
