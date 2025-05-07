# Post-Quantum PAKE Artifact: Ring-LWE and Module-LWE

This artifact was developed as part of the final project for the course on Post-Quantum Cryptography. It includes full implementations and evaluation scripts for PAKE protocols based on Ring-LWE and Module-LWE assumptions.

---

## 📁 Folder Structure

```
pqpake-artifact/
├── implementation/           # Main source code for both PAKE schemes
│   ├── ring_lwe_pake.py
│   ├── module_lwe_pake.py
│   └── utils.py
├── ringEval/                 # Evaluation scripts for Ring-LWE
│   ├── performance_eval.py
│   ├── brute_force_test.py
│   └── test_vectors.py
├── moduleEval/               # Evaluation scripts for Module-LWE
│   ├── performance_eval.py
│   ├── brute_force_test.py
│   └── test_vectors.py
├── evaluation/test_vectors/  # Output vectors from tests
├── build/
│   └── test.py               # Script to run all tests automatically
├── notebooks/
│   └── Final_Ring_and_Module_LWE_simulation_+_testing.ipynb
├── proofs/
│   └── *.tex and *.pdf       # Formal security arguments (LaTeX and PDF)
├── requirement.txt           # Dependencies
├── LICENSE                   # MIT license
└── README.md                 # This file
```

---

## 🔧 Setup (Windows 11)

### Step 1 — Install Python
Make sure Python 3.10 or newer is installed. Download from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

### Step 2 — Install Dependencies

From inside the `pqpake-artifact/` folder, run:
```bash
pip install -r requirement.txt
```

No Conda or external environments are required.

---

## ▶️ Run All Tests

You can execute all simulations and evaluations using:
```bash
python build/test.py
```
This will:
- Run both Ring-LWE and Module-LWE PAKE simulations
- Perform brute-force attack resistance tests
- Evaluate performance
- Generate and save test vectors

Output will be printed to the terminal and saved under `evaluation/test_vectors/` if applicable.

