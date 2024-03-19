def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
fibonacci_sequence = [next(fib_gen) for _ in range(10)]
print(fibonacci_sequence)