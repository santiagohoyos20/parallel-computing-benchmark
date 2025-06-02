# primes_mpi.py
from mpi4py import MPI
import sys
import math
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def main():
    D = int(sys.argv[1])
    start_val = 10**(D - 1)
    end_val = 10**D
    total = end_val - start_val
    local_size = total // size
    local_start = start_val + rank * local_size
    local_end = start_val + (rank + 1) * local_size if rank != size - 1 else end_val

    if rank == 0:
        start = time.perf_counter()

    local_count = sum(1 for x in range(local_start, local_end) if is_prime(x))
    total_count = comm.reduce(local_count, op=MPI.SUM, root=0)

    if rank == 0:
        end = time.perf_counter()
        print(f"Primos encontrados: {total_count}")
        print(f"Tiempo de ejecución: {(end - start)*1000:.2f} ms")

if __name__ == "__main__":
    main()
