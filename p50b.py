import math, time

primes = [2]


def known_factor(n):
    root = math.sqrt(n)
    for p in primes:
        if p > root:
            return False
        if n % p == 0:
            return True
    return False


start_time = time.time()
for n in range(3, 1000000, 2):
    if not known_factor(n):
        primes.append(n)
sequence_sum = 2
end = 0
while sequence_sum < 1000000:
    end += 1
    sequence_sum += primes[end]
sequence_sum -= primes[end]
end -= 1
if sequence_sum in primes:
    print(sequence_sum)
else:
    sequence_parameters = (0, end, sequence_sum)
    sequences = [sequence_parameters]
    searching = True
    while searching:
        sequence, sequences = sequences[0], sequences[1:]
        start0, end0, sum0 = sequence

        start1 = start0 + 1
        end1 = end0
        sum1 = sum0 - primes[start0]
        if sum1 in primes:
            print(sum1)
            searching = False
        sequence1 = (start1, end1, sum1)

        start2 = start0
        end2 = end0 - 1
        sum2 = sum0 - primes[end0]
        if sum2 in primes:
            print(sum2)
            searching = False
        sequence2 = (start2, end2, sum2)
        
        sequences += [sequence1, sequence2]
print(time.time() - start_time)
