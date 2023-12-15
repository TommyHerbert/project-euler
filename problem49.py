def normalise(n):
    digits = list(str(n))
    digits.sort()
    return ''.join(digits)


def known_prime_divisor(n, primes):
    for p in primes:
        if n % p == 0:
            return True
    return False


def print_sequences(floor, ceiling):
    primes = [2]
    sequences = {}
    for n in range(3, ceiling, 2):
        if not known_prime_divisor(n, primes):
            primes.append(n)
            if n > floor:
                normalised = normalise(n)
                if normalised not in sequences:
                    sequences[normalised] = []
                sequences[normalised].append(n)
                sequence = sequences[normalised]
                if len(sequence) > 2:
                    for p in sequence[1:-1]:
                        first_term = p - (n - p)
                        if first_term  in sequence:
                            print(first_term, p, n)
