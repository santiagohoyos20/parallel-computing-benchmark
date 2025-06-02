# primes_seq.py
import sys
import time
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    D = int(sys.argv[1])
    start_val = 10**(D - 1)
    end_val = 10**D

    start = time.perf_counter()
    count = sum(1 for x in range(start_val, end_val) if is_prime(x))
    end = time.perf_counter()

    print(f"Primos encontrados: {count}")
    print(f"Tiempo de ejecución: {(end - start)*1000:.2f} ms")

if __name__ == "__main__":
    main()
