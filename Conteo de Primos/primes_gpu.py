# primes_gpu.py
import numpy as np
import math
import sys
import time
from numba import cuda

@cuda.jit
def mark_primes(start, end, results):
    idx = cuda.grid(1)
    val = start + idx
    if val >= end:
        return
    if val < 2:
        results[idx] = 0
        return
    for i in range(2, int(math.sqrt(val)) + 1):
        if val % i == 0:
            results[idx] = 0
            return
    results[idx] = 1

def main():
    D = int(sys.argv[1])
    start_val = 10**(D - 1)
    end_val = 10**D
    N = end_val - start_val

    threads_per_block = 128
    blocks_per_grid = (N + threads_per_block - 1) // threads_per_block

    results = np.zeros(N, dtype=np.uint8)
    d_results = cuda.to_device(results)

    start = time.perf_counter()
    mark_primes[blocks_per_grid, threads_per_block](start_val, end_val, d_results)
    cuda.synchronize()
    end = time.perf_counter()

    d_results.copy_to_host(results)
    count = np.sum(results)

    print(f"Primos encontrados: {count}")
    print(f"Tiempo de ejecución: {(end - start)*1000:.2f} ms")

if __name__ == "__main__":
    main()
