# ring_lwe_pake.py
# A basic Ring-LWE-based PAKE simulation for educational purposes

import numpy as np
import hashlib
import secrets

# Parameters — toy values for demonstration (not secure)
n = 256        # Polynomial ring dimension (must be power of 2)
q = 12289      # Prime modulus for coefficient arithmetic

# Generate a random small polynomial with values in {-1, 0, 1}
def sample_poly(n):
    return np.random.randint(-1, 2, size=n)

def generate_keys():
    s = sample_poly(n)
    e = sample_poly(n)
    a = np.random.randint(0, q, size=n)
    b = (poly_mul(a, s) + e) % q
    return a, s, b

# Polynomial multiplication modulo (x^n + 1), reduced mod q
def poly_mul(a, b):
    result = np.fft.ifft(np.fft.fft(a) * np.fft.fft(b)).real
    result = np.round(result).astype(int) % q
    return result[:n]

# Reconciliation function — convert polynomial to binary bits
def reconcile(v):
    return np.array([0 if (x % q) < q // 2 else 1 for x in v], dtype=np.uint8)

# Hash the bitstring into a shared 256-bit key
def hash_key(bits):
    return hashlib.sha256(bytes(bits)).hexdigest()

def derive_shared_key(a, s_other, b_other):
    u = poly_mul(a, s_other) % q
    key_bits = reconcile(u)
    return hash_key(key_bits)

# Simulate a PAKE exchange
def main():
    print("Running Ring-LWE PAKE simulation...")

    # Shared public polynomial (usually fixed in real protocols)
    a = np.random.randint(0, q, size=n)

    # Alice’s keys
    s_A = sample_poly(n)
    e_A = sample_poly(n)
    b_A = (poly_mul(a, s_A) + e_A) % q

    # Bob’s keys
    s_B = sample_poly(n)
    e_B = sample_poly(n)
    b_B = (poly_mul(a, s_B) + e_B) % q

    # Each party computes the shared secret using other's public value
    u_A = poly_mul(b_B, s_A) % q
    u_B = poly_mul(b_A, s_B) % q

    key_A = hash_key(reconcile(u_A))
    key_B = hash_key(reconcile(u_B))

    print("Alice's derived key:", key_A)
    print("Bob's derived key:  ", key_B)
    print("Keys match:", key_A == key_B)

if __name__ == "__main__":
    main()
