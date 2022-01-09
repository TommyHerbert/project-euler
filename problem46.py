from math import sqrt

primes = [2, 3]
doubled_squares = [2]


def populate_doubled_squares(ceiling):
    while doubled_squares[-1] < ceiling:
        root = len(doubled_squares) + 1
        doubled_squares.append(root * root * 2)


def solve():
    odd_number = 3
    while True:
        populate_doubled_squares(odd_number)
        populate_primes(odd_number)
        if (odd_number not in primes) and (breaks_conjecture(odd_number)):
            return odd_number
        odd_number += 2


def populate_primes(ceiling):
    prime_candidate = primes[-1] + 2
    while primes[-1] < ceiling:
        if not divides_by_known_prime(prime_candidate):
            primes.append(prime_candidate)
        prime_candidate += 2


def divides_by_known_prime(x):
    for prime in primes:
        if x % prime == 0:
            return True
    return False


def breaks_conjecture(odd_number):
    for prime in primes:
        if prime < odd_number and odd_number - prime in doubled_squares:
            return False   
    return True

