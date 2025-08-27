# My DNA Sequence Assembly Project with Ternary Search Trees

**Student:** Amudhaanandheswaran Selvaraj

Welcome to my repository for the **DNA Sequence Assembly** project, developed as part of the **Advanced Programming in Python** course. This repository showcases my implementation of a **Ternary Search Tree (TST)** and its application in efficiently managing and assembling DNA sequences. I focused on a robust, performant solution with clear **time-complexity analysis** and **real-world performance** on high-performance computing (HPC) resources.

---

## Project Overview

This project implements a Python-based system for **DNA sequence assembly**. The core data structure is a custom **Ternary Search Tree (TST)**, chosen for its efficiency with string operations—critical for **searching**, **inserting**, and **prefix lookups** of DNA segments during assembly. The goal is to reconstruct a complete DNA sequence from smaller, overlapping segments, and the TST is used to accelerate overlap queries and lookups.

---

## Key Features

The `TernarySearchTree` class supports the following essential operations:

- **`insert(word)`** – Efficiently add a new DNA segment (string).
- **`search(word)`** – Quickly check whether a segment exists.
- **`__len__()`** – Return the number of **unique** stored segments.
- **`traverse()`** – Retrieve all stored segments in lexicographic order (useful for debugging/inspection).

---

## Performance Analysis & Results

- **Time Complexity Graph** (`time_complexity_graph.png`): visualizes scaling behavior as the number/length of inputs grows.
- **HPC Output Logs** (`supercomputing_results.log`): results from running the TST on HPC resources, assessing scalability on large datasets such as `corncob_lowercase.txt`.

---

## How to Run the Tests

All test cases and demonstrations are in the **correct notebook**: **`Test_1.pynb`**  


**Data files used in tests:**
- `insert_words.txt` – words inserted to verify insert/search correctness
- `not_insert_words.txt` – words *not* inserted to validate negative searches
- `corncob_lowercase.txt` – large dictionary (~50k+ words) for stress testing

**Steps:**
1. Ensure Jupyter is installed:
   ```bash
   pip install notebook
2. Clone the repository:
 git clone https://github.com/Amudhan2201/Concepts_of_datascience
 cd Concepts_of_datascience
3. Confirm the following files are present in the project directory:
   ternary_search_tree_module.py
   Test_1.pynb
   insert_words.txt
   not_insert_words.txt
   corncob_lowercase.txt
4. Launch Jupyter:
5. Open Test_1.pynb and run:

Cell → Run All

6. The notebook prints results for each test (e.g., ✅ Passed / ❌ Failed) and produces the plots/logs.

Repository Contents

ternary_search_tree_module.py – defines TSTNode and TernarySearchTree with all methods
Test_1.pynb – main notebook with tests, usage demos, and time-complexity plotting
insert_words.txt – dataset for positive insert/search tests
not_insert_words.txt – dataset for negative search tests
corncob_lowercase.txt – large dictionary for heavy-load/performance tests
time_complexity_graph.png – plot showing complexity trends
supercomputing_results.log – HPC run outputs and timings
output_1.png – example output image from the assembly workflow

Summary of Conclusions

TST Efficiency – The TST’s 3-way branching (left, eq, right) enables fast insertion and search for string keys (DNA segments), making it well-suited for sequence workloads.

Scalability on Large Data – Tests with corncob_lowercase.txt and HPC execution confirm strong scaling characteristics with tens of thousands of strings.

DNA Assembly Fit – Efficient prefix queries and rapid lookups of overlapping segments make the TST a strong backbone for assembly logic (e.g., overlap detection and contig extension).

Reproducibility – Test_1.pynb consolidates correctness/performance tests. The time-complexity plot and HPC logs document empirical behavior and support reproducible claims.