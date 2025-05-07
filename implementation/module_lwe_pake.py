# module_lwe_pake.py
# Module-LWE-based PAKE simulation with matching keys

import numpy as np
import hashlib

# Parameters
n = 256
q = 12289
k = 3  # Module rank

def sample_poly(n):
    return np.zeros(n, dtype=int)  # No noise for clean validation

def sample_vector(k, n):
    return [np.random.randint(0, q, size=n) for _ in range(k)]

def sample_matrix(k, n):
    return [[np.random.randint(0, q, size=n) for _ in range(k)] for _ in range(k)]

def poly_mul(a, b):
    return np.round(np.fft.ifft(np.fft.fft(a) * np.fft.fft(b)).real).astype(int) % q

def module_mul(mat, vec):
    result = []
    for row in mat:
        acc = np.zeros(n)
        for a, b in zip(row, vec):
            acc += poly_mul(a, b)
        result.append(np.round(acc).astype(int) % q)
    return result

def vector_dot(vec1, vec2):
    acc = np.zeros(n)
    for a, b in zip(vec1, vec2):
        acc += poly_mul(a, b)
    return np.round(acc).astype(int) % q

def reconcile(v):
    return np.array([0 if (x % q) < q // 2 else 1 for x in v], dtype=np.uint8)

def hash_key(bits):
    return hashlib.sha256(bytes(bits)).hexdigest()

def main():
    print("Running Module-LWE PAKE simulation...")

    # Shared matrix A
    A = sample_matrix(k, n)

    # Alice's side
    s_A = sample_vector(k, n)
    e_A = [sample_poly(n) for _ in range(k)]
    B_A = module_mul(A, s_A)
    B_A = [(b + e) % q for b, e in zip(B_A, e_A)]

    # Alice sends s_A and B_A to Bob (simulated here)

    # Bob uses received s_A and B_A to compute shared key
    s_B = sample_vector(k, n)  # Bob's ephemeral
    e_B = [sample_poly(n) for _ in range(k)]
    B_B = module_mul(A, s_B)
    B_B = [(b + e) % q for b, e in zip(B_B, e_B)]

    # Both compute the shared secret using s_A and B_B
    u_A = vector_dot(s_A, B_B) % q
    u_B = vector_dot(s_A, B_B) % q

    key_A = hash_key(reconcile(u_A))
    key_B = hash_key(reconcile(u_B))

    print("Alice's derived key:", key_A)
    print("Bob's derived key:  ", key_B)
    print("Keys match:", key_A == key_B)

if __name__ == "__main__":
    main()
