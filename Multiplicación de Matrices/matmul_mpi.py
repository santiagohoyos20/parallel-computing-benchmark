# matmul_mpi.py
from mpi4py import MPI
import numpy as np
import sys
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def main():
    N = int(sys.argv[1])
    local_N = N // size

    if rank == 0:
        A = np.random.rand(N, N)
        B = np.random.rand(N, N)
    else:
        A = None
        B = np.empty((N, N), dtype=np.float64)

    local_A = np.empty((local_N, N), dtype=np.float64)

    if rank == 0:
        start = time.perf_counter()

    comm.Scatter(A, local_A, root=0)
    comm.Bcast(B, root=0)

    local_C = np.dot(local_A, B)

    if rank == 0:
        C = np.empty((N, N), dtype=np.float64)
    else:
        C = None

    comm.Gather(local_C, C, root=0)

    if rank == 0:
        end = time.perf_counter()
        print(f"Tiempo de ejecución: {(end - start)*1000:.2f} ms")

if __name__ == "__main__":
    main()
