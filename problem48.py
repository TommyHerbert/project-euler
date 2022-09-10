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
        running_total = add_power_2(running_total, i, i, modulus)
    return running_total


def add_power_2(running_total, base, exponent, modulus):
    working_product = 1
    for i in range(exponent):
        working_product = (working_product * base) % modulus
    return (running_total + working_product) % modulus
