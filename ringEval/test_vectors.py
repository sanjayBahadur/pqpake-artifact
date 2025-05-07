# test_vectors.py
# This script creates and verifies test vectors for the Ring-LWE PAKE implementation
# Useful for regression testing, debugging, and confirming correctness across versions

import sys
import os
sys.path.append(os.path.abspath("implementation"))

from ring_lwe_pake import generate_keys, derive_shared_key
import numpy as np
import json

# Save a NumPy array to a JSON file in the test_vectors directory
def save_vector(name, vector):
    with open(f"evaluation/test_vectors/{name}.json", "w") as f:
        json.dump(vector.tolist(), f, indent=2)

# Load a NumPy array from a previously saved JSON file
def load_vector(name):
    with open(f"evaluation/test_vectors/{name}.json", "r") as f:
        return np.array(json.load(f))

# Generate a full set of test vectors and write them to disk
def generate_and_save_test_vectors():
    print("Generating test vectors...")
    a, s, b = generate_keys()

    # Save polynomials used during key exchange
    save_vector("public_a", a)
    save_vector("secret_s", s)
    save_vector("public_b", b)

    # Derive and save the expected shared key
    key = derive_shared_key(a, s, b)
    with open("evaluation/test_vectors/shared_key.txt", "w") as f:
        f.write(key + "\n")

    print("Test vectors saved in evaluation/test_vectors/")

# Load the saved test vectors and verify the key still matches

def validate_test_vectors():
    print("Validating saved test vectors...")
    a = load_vector("public_a")
    s = load_vector("secret_s")
    b = load_vector("public_b")

    derived = derive_shared_key(a, s, b)
    with open("evaluation/test_vectors/shared_key.txt", "r") as f:
        expected = f.read().strip()

    print("Derived key:", derived)
    print("Expected key:", expected)
    print("Match:", derived == expected)

# Main driver: run both generation and validation together
if __name__ == "__main__":
    generate_and_save_test_vectors()
    validate_test_vectors()
