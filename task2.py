import time

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Час виконання:", end_time - start_time, "сек")
        return result
    return wrapper

@timer_wrapper
def prime_num_getter(n):
    generator = prime_num_generator()
    for _ in range(n):
        print(next(generator))

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

n = 10
prime_num_getter(n)
