primes = [2]

def factorise(n):
    
    for prime in primes:
        if n % prime == 0:
            return [prime] + factorise(n / prime)

