# performance_eval.py
# Benchmark performance of Ring-LWE PAKE operations

import time
import sys
import os
sys.path.append(os.path.abspath("implementation"))

from ring_lwe_pake import generate_keys, derive_shared_key
TRIALS = 1000

def benchmark_keygen():
    times = []
    for _ in range(TRIALS):
        start = time.time()
        generate_keys()
        times.append(time.time() - start)
    avg = sum(times) / TRIALS
    print(f"[KeyGen] Average time over {TRIALS} trials: {avg * 1000:.3f} ms")

def benchmark_shared_key():
    a, s, b = generate_keys()
    times = []
    for _ in range(TRIALS):
        start = time.time()
        derive_shared_key(a, s, b)
        times.append(time.time() - start)
    avg = sum(times) / TRIALS
    print(f"[Key Derivation] Average time over {TRIALS} trials: {avg * 1000:.3f} ms")

def main():
    print("Running Ring-LWE PAKE performance benchmark...")
    benchmark_keygen()
    benchmark_shared_key()

if __name__ == "__main__":
    main()
