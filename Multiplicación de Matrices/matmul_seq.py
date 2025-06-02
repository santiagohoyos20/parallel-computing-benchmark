# matmul_seq.py
import numpy as np
import sys
import time

def main():
    N = int(sys.argv[1])
    A = np.random.rand(N, N)
    B = np.random.rand(N, N)

    start = time.perf_counter()
    C = np.dot(A, B)
    end = time.perf_counter()

    print(f"Tiempo de ejecución: {(end - start)*1000:.2f} ms")

if __name__ == "__main__":
    main()
