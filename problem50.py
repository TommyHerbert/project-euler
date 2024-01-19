class State:
    def __init__(self):
        self.start = 0
        self.length = 0
        self.total = 0
        self.left_total = 0


def get_primes(ceiling):
    primes = [2]
    for n in range(3, ceiling, 2):
        if not known_prime_factor(n, primes):
            primes.append(n)
    return primes


def known_prime_factor(n, primes):
    for p in primes:
        if n % p == 0:
            return True
    return False


class SequenceFinder:
    def __init__(self, ceiling):
        self.ceiling = ceiling

    def solve(self):
        primes = get_primes(self.ceiling)
        state = State()
        state = self.set_initial_sequence(state, primes)
        while self.searching(state, primes):
            if self.fits(state):
                state = self.shift(state, primes)
            else:
                state = self.shrink(state, primes)
        return state.total

    def set_initial_sequence(self, state, primes):
        while self.fits(state):
            state.total += primes[state.length]
            state.length += 1
        state.left_total = state.total
        return state

    def searching(self, state, primes):
        return state.total not in primes

    def fits(self, state):
        return state.total < self.ceiling

    def shift(self, old_state, primes):
        new_state = State()
        new_state.start = old_state.start + 1
        new_state.length = old_state.length
        if old_state.start == 0:
            new_state.length -= 1
        new_state.total = old_state.total - primes[old_state.start]
        if old_state.start != 0:
            new_state.total += primes[new_state.start + new_state.length - 1]
        new_state.left_total = old_state.left_total
        return new_state

    def shrink(self, old_state, primes):
        new_state = State()
        new_state.length = old_state.length - 1
        new_state.total = old_state.left_total - primes[old_state.length - 1]
        new_state.left_total = new_state.total
        return new_state
