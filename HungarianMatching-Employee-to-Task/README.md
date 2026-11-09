# Employee-to-Task Assignment Using Hungarian Algorithm

## Algorithm Overview

### 1. Algorithm Name & Context

- **Algorithm:** Hungarian Algorithm (Kuhn-Munkres Algorithm).
- **Classification:** Combinatorial optimization algorithm for solving the assignment problem.
- **Objective:** Find the optimal assignment between employees and tasks while minimizing the total assignment cost.
- **Problem Context:**
  - Each employee must be assigned to exactly one task.
  - Each task must be assigned to exactly one employee.
  - Each assignment has an associated cost, representing the estimated completion time.
  - The objective is to minimize the total cost of all assignments.

- **Distinction:**
  - **Different from Greedy Assignment:** It does not simply select the locally cheapest assignment for each employee. Instead, it considers the overall assignment to find a globally optimal solution.
  - **Different from Maximum Matching:** It does not only maximize the number of matched vertices. It also considers the cost associated with each assignment.
  - Instead, it transforms the cost matrix through row and column reductions, zero covering, and matrix adjustments to determine an optimal assignment.

---

### 2. How the Algorithm Works

The implementation follows the six main steps of the Hungarian Algorithm.

1. **Construct the Cost Matrix:**
   - Create a square matrix representing the assignment costs between employees and tasks.
   - Each row represents an employee.
   - Each column represents a task.
   - Each element represents the cost of assigning a particular employee to a particular task.

2. **Row Reduction:**
   - Find the minimum value in each row.
   - Subtract that minimum value from every element in the corresponding row.
   - This ensures that every row contains at least one zero.

3. **Column Reduction:**
   - Find the minimum value in each column.
   - Subtract that minimum value from every element in the corresponding column.
   - This ensures that every column contains at least one zero.

4. **Cover All Zeros:**
   - Find the minimum number of horizontal and vertical lines required to cover all zero elements.
   - The implementation uses bipartite matching and an alternating-path search to determine a minimum vertex cover of the zero positions.
   - If the number of lines equals the matrix size, an optimal assignment can be determined.
   - Otherwise, proceed to Step 5.

5. **Matrix Adjustment:**
   - Find the smallest uncovered element.
   - Subtract this value from every uncovered element.
   - Add this value to elements covered by both a horizontal and a vertical line.
   - Elements covered by exactly one line remain unchanged.
   - Repeat the zero-covering and adjustment process until a complete assignment becomes possible.

6. **Determine the Optimal Assignment:**
   - Find a complete matching among the zero elements.
   - Ensure that each employee is assigned to exactly one task and each task is assigned to exactly one employee.
   - Use the original cost matrix to calculate the minimum total assignment cost.

---

### 3. Complexity

The implementation uses a zero-matching procedure based on DFS augmenting paths.

- **Time Complexity:**
  - Row Reduction: `O(n²)`.
  - Column Reduction: `O(n²)`.
  - Zero Matching: `O(n³)` per matching attempt in the dense matrix case.
  - Zero Covering: `O(n²)`.
  - Matrix Adjustment: `O(n²)`.
  - Overall: `O(R × n³)`, where `R` represents the number of matrix-adjustment rounds. This describes the implemented procedure rather than claiming the standard optimized Hungarian Algorithm's `O(n³)` bound.

- **Space Complexity:** `O(n²)` — the implementation stores the original cost matrix, reduced matrix, and temporary matrix data, with additional matching and traversal structures.

---

## Prerequisites

- Python 3.8+.
- `pytest` for running the automated test suite.
- No external optimization libraries are required to execute the Hungarian Algorithm.
- The main algorithm is implemented using Python's built-in data structures and functions.

### Installation

Install pytest:

```bash
python -m pip install pytest
```

---

## Instructions to Run

Navigate into the project directory:

```bash
cd Hungarian-Matching
```

### 1. Run the Hungarian Algorithm

```bash
python hungarian.py
```

The program will ask for the number of employees and tasks, followed by the assignment cost matrix.

### 2. Run with Custom Input

Enter the matrix size and its cost values when prompted.

Example:

```text
Enter number of employees and tasks: 4

Enter the cost matrix (4 x 4):
Employee 1: 9 2 7 8
Employee 2: 6 4 3 7
Employee 3: 5 8 1 8
Employee 4: 7 6 9 4
```

### 3. Run the Automated Test Suite

```bash
python -m pytest -v
```

The test suite verifies different matrix sizes, assignment validity, and invalid input handling.

---

## Sample Inputs

The project provides three sample cases in `input_samples.txt`.

| Sample | Matrix Size | Description |
|---|---:|---|
| Sample 1 | 3 × 3 | Small assignment problem |
| Sample 2 | 4 × 4 | Assignment problem with four employees and four tasks |
| Sample 3 | 6 × 6 | Larger assignment problem with six employees and six tasks |

The program supports dynamic square matrix sizes. The provided samples are examples and do not impose a maximum matrix size of 6 × 6.

---

## Result of Sample Run

### Sample 1: 3 × 3

**Input:**

```text
3
4 1 3
2 0 5
3 2 2
```

**Expected Output:**

```text
========== OPTIMAL ASSIGNMENT ==========

Employee 1 -> Task 2 (1)
Employee 2 -> Task 1 (2)
Employee 3 -> Task 3 (2)

---------------------------------------
Minimum Total Cost: 5
```

### Sample 2: 4 × 4

**Input:**

```text
4
9 2 7 8
6 4 3 7
5 8 1 8
7 6 9 4
```

**Expected Output:**

```text
========== OPTIMAL ASSIGNMENT ==========

Employee 1 -> Task 2 (2)
Employee 2 -> Task 1 (6)
Employee 3 -> Task 3 (1)
Employee 4 -> Task 4 (4)

---------------------------------------
Minimum Total Cost: 13
```

### Sample 3: 6 × 6

**Input:**

```text
6
14 5 8 7 15 9
2 12 6 5 9 11
7 8 3 9 6 10
9 6 12 4 8 7
6 10 7 8 5 12
11 7 9 6 10 3
```

**Expected Minimum Total Cost:**

```text
Minimum Total Cost: 22
```

The exact employee-to-task assignment may differ when multiple optimal assignments exist, but the minimum total cost should remain the same.

---

## Testing

The project includes `test_hungarian.py`, which uses pytest to verify the implementation.

The automated test suite contains nine test cases:

| Test Case | Description |
|---|---|
| `test_sample_3x3` | Tests a 3 × 3 assignment matrix |
| `test_sample_4x4` | Tests a 4 × 4 assignment matrix |
| `test_sample_6x6` | Tests a 6 × 6 assignment matrix |
| `test_single_element` | Tests a 1 × 1 matrix |
| `test_assignment_validity` | Ensures each employee and task is assigned exactly once |
| `test_empty_matrix` | Rejects an empty matrix |
| `test_non_square_matrix` | Rejects matrices with different row and column counts |
| `test_negative_cost` | Rejects negative cost values |
| `test_non_numeric_cost` | Rejects non-numeric cost values |

**Latest test result:**

```text
================ 9 passed ================
```

---

## AI Tools Usage Disclosure

In compliance with the assignment rules, AI assistance from ChatGPT and Gemini was utilized during the development of this implementation:

- **Assistance Provided:** Understanding the Hungarian Algorithm, receiving guidance on Python implementation, debugging, and preparing automated test cases.
- **Prompt History:**
  1. How does the Hungarian Algorithm work, and how can it be implemented in Python?
  2. How can I implement a dynamic employee-to-task assignment problem using the Hungarian Algorithm in Python?


