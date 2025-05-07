# test_vectors_module.py
# Generate and save test vectors for Module-LWE PAKE

import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "implementation")))

from module_lwe_pake import sample_matrix, sample_vector, module_mul, vector_dot, reconcile, hash_key, n, k, q

print("Generating Module-LWE PAKE test vectors...")

TEST_VECTOR_DIR = os.path.join(os.path.dirname(__file__), "test_vectors")
os.makedirs(TEST_VECTOR_DIR, exist_ok=True)

def save_vector(name, obj):
    with open(os.path.join(TEST_VECTOR_DIR, f"{name}.json"), "w") as f:
        json.dump([[int(x) for x in poly] for poly in obj], f)

def save_matrix(name, mat):
    with open(os.path.join(TEST_VECTOR_DIR, f"{name}.json"), "w") as f:
        json.dump([[[int(x) for x in poly] for poly in row] for row in mat], f)

def save_array(name, arr):
    with open(os.path.join(TEST_VECTOR_DIR, f"{name}.json"), "w") as f:
        json.dump([int(x) for x in arr], f)

def generate_and_save():
    A = sample_matrix(k, n)
    s = sample_vector(k, n)
    B = module_mul(A, s)
    u = vector_dot(s, B) % q
    bits = reconcile(u)
    key = hash_key(bits)

    save_matrix("matrix_A", A)
    save_vector("secret_s", s)
    save_vector("public_B", B)
    save_array("reconciled_u", u)
    save_array("bitstring", bits)
    with open(os.path.join(TEST_VECTOR_DIR, "shared_key.txt"), "w") as f:
        f.write(key)

    print("Test vectors saved in:", TEST_VECTOR_DIR)

if __name__ == "__main__":
    generate_and_save()
