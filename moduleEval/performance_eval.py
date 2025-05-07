# performance_eval_module.py
# Performance evaluation for Module-LWE PAKE implementation

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "implementation")))

from module_lwe_pake import sample_matrix, sample_vector, module_mul, vector_dot, reconcile, hash_key, n, k, q

import time

TRIALS = 100

print("Running Module-LWE performance evaluation...")

total_time = 0
keys_matched = 0

for i in range(TRIALS):
    start = time.time()

    # Shared matrix A
    A = sample_matrix(k, n)

    # Alice
    s_A = sample_vector(k, n)
    B_A = module_mul(A, s_A)

    # Bob
    s_B = sample_vector(k, n)
    B_B = module_mul(A, s_B)

    # Shared secret
    u_A = vector_dot(s_A, B_B) % q
    u_B = vector_dot(s_A, B_B) % q

    key_A = hash_key(reconcile(u_A))
    key_B = hash_key(reconcile(u_B))

    if key_A == key_B:
        keys_matched += 1

    end = time.time()
    total_time += (end - start)

avg_time = total_time / TRIALS
print(f"\nTotal trials: {TRIALS}")
print(f"Successful matches: {keys_matched}/{TRIALS}")
print(f"Success rate: {100.0 * keys_matched / TRIALS:.2f}%")
print(f"Average time per run: {avg_time:.4f} seconds")
