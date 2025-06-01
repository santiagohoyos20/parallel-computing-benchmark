# Trabajo en Paralelo - Estructura del Computador II (2025-10)

Este repositorio contiene el desarrollo del proyecto de la materia **Estructura del Computador II**, cuyo objetivo es comparar el rendimiento y escalabilidad de diferentes paradigmas de programación paralela aplicados a dos cargas de trabajo clásicas: multiplicación de matrices y conteo de números primos.

## 📌 Cargas de Trabajo

### 1. Multiplicación de Matrices
Multiplicación de dos matrices cuadradas de tamaño `N × N` con valores flotantes aleatorios en el rango [0, 1).

### 2. Conteo de Primos
Cálculo del número total de primos con exactamente `D` dígitos (rango: [10⁽ᴰ⁻¹⁾, 10ᴰ – 1]).

---

## 🧪 Implementaciones

Cada carga de trabajo se implementa en tres versiones:

| Implementación | Multiplicación | Conteo de Primos |
|----------------|----------------|------------------|
| Secuencial     | `matmul_seq.py`| `primes_seq.py`  |
| MPI (mpi4py)   | `matmul_mpi.py`| `primes_mpi.py`  |
| GPU (CuPy / Numba) | `matmul_gpu.py`| `primes_gpu.py`  |

---

## ⚙️ Requisitos

- Python 3.10+
- [`numpy`](https://numpy.org/)
- [`mpi4py`](https://mpi4py.readthedocs.io/)
- [`cupy`](https://cupy.dev/) o [`numba`](https://numba.pydata.org/) (para GPU)
- Entorno con soporte para MPI y CUDA

Para instalar los paquetes necesarios:
```bash
pip install numpy mpi4py cupy numba
