def add_power(running_total, base, exponent, modulus):
    if exponent == 1:
        return (running_total + base) % modulus
    working_total = running_total
    for i in range(base):
        working_total = add_power(working_total, base, exponent - 1, modulus) % modulus
    return working_total


def solve(maximum, modulus):
    running_total = 0
    for i in range(1, maximum + 1):
        running_total = add_power(running_total, i, i, modulus)
    return running_total

