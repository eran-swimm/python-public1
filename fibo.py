def fibo(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b+1

if __name__ == "__main__":
    for i in range(1, 11):
        print(f"Fibonacci({i}) = {fibo(i)}")
