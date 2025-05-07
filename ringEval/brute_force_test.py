# brute_force_test.py
# Script to simulate brute-force attack attempts on Ring-LWE PAKE

import numpy as np
import sys
import os
sys.path.append(os.path.abspath("implementation"))

from ring_lwe_pake import generate_keys, derive_shared_key

import time

TRIALS = 1000  # Number of brute-force guesses to simulate

# Generate a small fake password dictionary (in reality, this would be hashes or shared secrets)
def generate_fake_passwords():
    return [np.random.randint(0, 2, 256) for _ in range(TRIALS)]

# Simulate brute-force trial

def brute_force_simulation():
    print("Running brute-force resistance test on Ring-LWE PAKE...")
    a, s, b = generate_keys()
    target_key = derive_shared_key(a, s, b)

    fake_attempts = generate_fake_passwords()
    success_count = 0
    start = time.time()

    for guess in fake_attempts:
        # Simulate an attacker trying to derive key from a random guess
        fake_key = derive_shared_key(a, guess, b)
        if fake_key == target_key:
            success_count += 1

    duration = time.time() - start
    print(f"Completed {TRIALS} trials in {duration:.2f} seconds.")
    print(f"Successful matches: {success_count}/{TRIALS}")
    print("Success rate: {:.4f}%".format((success_count / TRIALS) * 100))

if __name__ == "__main__":
    brute_force_simulation()
