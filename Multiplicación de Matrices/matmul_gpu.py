# matmul_gpu.py
import cupy as cp
import sys
import time

def main():
    N = int(sys.argv[1])
    A = cp.random.rand(N, N)
    B = cp.random.rand(N, N)

    start = time.perf_counter()
    C = cp.dot(A, B)
    cp.cuda.Stream.null.synchronize()
    end = time.perf_counter()

    print(f"Tiempo de ejecución: {(end - start)*1000:.2f} ms")

if __name__ == "__main__":
    main()
