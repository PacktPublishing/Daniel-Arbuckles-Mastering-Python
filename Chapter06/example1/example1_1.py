from concurrent import futures

def factorize(n):
    """Return the prime factors of *n*

    This is a **very** bad factoring algorithm, which makes it a good
    example of a CPU bound task.

    """
    n = int(n)

    if n == 1:
        return 1, []

    found = []

    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            if all(i % j != 0 for j in found):
                found.append(i)

    if not found:
        return n, [n]

    return n, found

if __name__ == '__main__':
    with futures.ProcessPoolExecutor() as pool:
        for number, factors in pool.map(factorize, range(1, 10001)):
            print('{}: {}'.format(number, factors))
