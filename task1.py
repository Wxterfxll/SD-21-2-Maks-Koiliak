def prime_num_generator():
    num = 2
    primes = set()
    while True:
        for prime in primes:
            if num % prime == 0:
                break
        else:
            primes.add(num)
            yield num
        num += 1

generator = prime_num_generator()
for _ in range(10):
    print(next(generator))
