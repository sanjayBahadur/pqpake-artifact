# brute_force_test_module.py
# Brute-force attack test for Module-LWE PAKE

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "implementation")))

from module_lwe_pake import sample_matrix, sample_vector, module_mul, vector_dot, reconcile, hash_key, n, k, q

import time
import numpy as np

print("Running brute-force resistance test on Module-LWE PAKE...")

TRIALS = 1000
successful_guesses = 0
start = time.time()

for _ in range(TRIALS):
    # Shared matrix A
    A = sample_matrix(k, n)

    # Real secrets (Alice)
    s_A = sample_vector(k, n)
    B_A = module_mul(A, s_A)

    # Attacker's random guess (trying to derive s_A)
    guess = sample_vector(k, n)
    guessed_secret = vector_dot(guess, B_A) % q

    key_real = hash_key(reconcile(vector_dot(s_A, B_A) % q))
    key_guess = hash_key(reconcile(guessed_secret))

    if key_real == key_guess:
        successful_guesses += 1

end = time.time()
print(f"Completed {TRIALS} trials in {end - start:.2f} seconds.")
print(f"Successful brute-force matches: {successful_guesses}/{TRIALS}")
print(f"Success rate: {100.0 * successful_guesses / TRIALS:.5f}%")
