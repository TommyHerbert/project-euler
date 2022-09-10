from math import sqrt

primes = [2]


def factorise(n):
    root = sqrt(n)
    for prime in primes:
        if prime > root:
            primes.append(n)
            return set([n])
        if n % prime == 0:
            return set([prime]).union(factorise(int(n / prime)))
    primes.append(n)
    return set([n])


def solve(n):
    pointer = 2
    while True:
        count = 0
        while len(factorise(pointer + count)) == n:
            count += 1
        if count == n:
            return pointer
        pointer += 1

