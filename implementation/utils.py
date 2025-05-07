# utils.py
# Common utility functions used by both Ring-LWE and Module-LWE implementations

import numpy as np
import hashlib

# Basic parameters used across the project
def get_ring_params():
    return {
        'n': 256,
        'q': 12289
    }

def get_module_params():
    return {
        'n': 256,
        'q': 3329,
        'k': 2
    }

# Sample polynomial with small coefficients in {-1, 0, 1}
def sample_poly(n):
    return np.random.randint(-1, 2, n)

# Generate a vector of small polynomials

def sample_vector(k, n):
    return [sample_poly(n) for _ in range(k)]

# Polynomial multiplication using FFT (not secure; placeholder for NTT)
def poly_mul(a, b, q):
    res = np.fft.ifft(np.fft.fft(a) * np.fft.fft(b)).real
    res = np.round(res).astype(int) % q
    return res[:len(a)]

# Module multiplication: matrix-vector product with polynomial components
def module_mul(matrix, vector, q):
    result = np.zeros(len(matrix[0]), dtype=int)
    for a_row, s_col in zip(matrix, vector):
        result += poly_mul(a_row, s_col, q)
    return result % q

# Simple reconciliation: round values to nearest bit (0 or 1)
def reconcile(v, q):
    return np.array([0 if (x % q) < q // 2 else 1 for x in v])

# Convert bit array to SHA-256 key

def hash_key(bits):
    return hashlib.sha256(bytes(bits)).hexdigest()
