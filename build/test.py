# Script to install dependencies and run all major test/evaluation scripts in order

import subprocess
import sys
import os
os.makedirs("evaluation/test_vectors", exist_ok=True)

sys.path.append(os.path.abspath("implementation"))


required_packages = [
    "numpy",
    "scipy",
    "matplotlib",
    "notebook"
]

def install_dependencies():
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + required_packages)

def run_script(path):
    print(f"\nRunning: {path}")
    subprocess.run([sys.executable, path], check=True)

def main():
    install_dependencies()

    print("\n=== Executing All Tests and Evaluations ===")

    # Adjust paths as needed based on your artifact structure
    scripts = [
        "./implementation/ring_lwe_pake.py",
        "./implementation/module_lwe_pake.py",
        "./ringEval/performance_eval.py",
        "./ringEval/brute_force_test.py",
        "./ringEval/test_vectors.py",
        "./moduleEval/test_vectors.py",
        "./moduleEval/performance_eval.py",
        "./moduleEval/brute_force_test.py",
        
    ]

    for script in scripts:
        if os.path.exists(script):
            run_script(script)
        else:
            print(f"[Warning] Script not found: {script}")

    print("\nAll scripts completed successfully.")

if __name__ == "__main__":
    main()
