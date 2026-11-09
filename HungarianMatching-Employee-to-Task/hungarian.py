
# ==========================================
# HUNGARIAN ALGORITHM
# Employee-to-Task Assignment Problem
# ==========================================

# Added:
# Function: validate_matrix()
# Description: Validate the cost matrix before processing.
def validate_matrix(matrix):
    if not matrix:
        raise ValueError("Matrix cannot be empty.")

    size = len(matrix)

    if any(len(row) != size for row in matrix):
        raise ValueError("Matrix must be square (n x n).")

    for row in matrix:
        for value in row:
            if not isinstance(value, (int, float)) or isinstance(value, bool):
                raise ValueError("Matrix must contain numeric values.")

            if value < 0:
                raise ValueError("Cost values cannot be negative.")


# Added:
# Function: reduce_rows()
# Description: Subtract the minimum value of each row.
def reduce_rows(matrix):
    reduced = [row[:] for row in matrix]

    for row in reduced:
        minimum = min(row)

        for j in range(len(row)):
            row[j] -= minimum

    return reduced


# Added:
# Function: reduce_columns()
# Description: Subtract the minimum value of each column.
def reduce_columns(matrix):
    size = len(matrix)
    reduced = [row[:] for row in matrix]

    for j in range(size):
        minimum = min(reduced[i][j] for i in range(size))

        for i in range(size):
            reduced[i][j] -= minimum

    return reduced


# Added:
# Function: find_zero_matching()
# Description: Find the maximum matching among zero positions.
def find_zero_matching(matrix):
    size = len(matrix)

    row_to_col = {}
    col_to_row = {}

    def dfs(row, visited):
        for col in range(size):

            if matrix[row][col] != 0 or col in visited:
                continue

            visited.add(col)

            if col not in col_to_row or dfs(col_to_row[col], visited):
                col_to_row[col] = row
                row_to_col[row] = col
                return True

        return False

    for row in range(size):
        dfs(row, set())

    return {
        row: col
        for col, row in col_to_row.items()
    }


# Added:
# Function: cover_zeros()
# Description: Find the minimum number of lines needed
#              to cover all zero elements.
def cover_zeros(matrix, matching):
    size = len(matrix)

    col_to_row = {
        col: row
        for row, col in matching.items()
    }

    # Start from rows that are not matched.
    reachable_rows = set(
        row for row in range(size)
        if row not in matching
    )

    reachable_cols = set()
    queue = list(reachable_rows)

    # Follow alternating paths through zero positions.
    while queue:
        row = queue.pop(0)

        for col in range(size):

            # Skip the matched edge.
            if matrix[row][col] != 0:
                continue

            if matching.get(row) == col:
                continue

            if col not in reachable_cols:
                reachable_cols.add(col)

                if col in col_to_row:
                    next_row = col_to_row[col]

                    if next_row not in reachable_rows:
                        reachable_rows.add(next_row)
                        queue.append(next_row)

    # Minimum vertex cover:
    # Unreachable rows + reachable columns.
    covered_rows = set(range(size)) - reachable_rows
    covered_cols = reachable_cols

    return covered_rows, covered_cols


# Added:
# Function: adjust_matrix()
# Description: Adjust uncovered elements using the minimum
#              uncovered value.
def adjust_matrix(matrix, covered_rows, covered_cols):
    size = len(matrix)
    adjusted = [row[:] for row in matrix]

    uncovered = [
        matrix[i][j]
        for i in range(size)
        for j in range(size)
        if i not in covered_rows and j not in covered_cols
    ]

    minimum = min(uncovered)

    for i in range(size):
        for j in range(size):

            # Subtract minimum from uncovered elements.
            if i not in covered_rows and j not in covered_cols:
                adjusted[i][j] -= minimum

            # Add minimum to elements covered twice.
            elif i in covered_rows and j in covered_cols:
                adjusted[i][j] += minimum

            # Elements covered once remain unchanged.

    return adjusted


# Added:
# Function: solve_hungarian()
# Description: Execute all steps of the Hungarian Algorithm.
def solve_hungarian(cost_matrix):
    validate_matrix(cost_matrix)

    size = len(cost_matrix)

    # Preserve original costs for final calculation.
    original_matrix = [row[:] for row in cost_matrix]

    # Step 1: Construct cost matrix.
    matrix = [row[:] for row in cost_matrix]

    # Step 2: Subtract row minimums.
    matrix = reduce_rows(matrix)

    # Step 3: Subtract column minimums.
    matrix = reduce_columns(matrix)

    # Step 4 and Step 5: Cover zeros and adjust matrix.
    while True:
        matching = find_zero_matching(matrix)

        # A complete matching means an optimal assignment exists.
        if len(matching) == size:
            break

        covered_rows, covered_cols = cover_zeros(
            matrix, matching
        )

        line_count = len(covered_rows) + len(covered_cols)

        if line_count >= size:
            break

        matrix = adjust_matrix(
            matrix, covered_rows, covered_cols
        )

    # Step 6: Determine the optimal assignment.
    assignment = find_zero_matching(matrix)

    if len(assignment) != size:
        raise RuntimeError("Unable to find a complete assignment.")

    total_cost = sum(
        original_matrix[row][col]
        for row, col in assignment.items()
    )

    return assignment, total_cost


# Added:
# Function: main()
# Description: Receive user input and display the result.
def main():
    print("===================================")
    print("   HUNGARIAN ALGORITHM")
    print(" Employee-to-Task Assignment")
    print("===================================")

    size = int(input("\nEnter number of employees and tasks: "))

    if size <= 0:
        print("Matrix size must be greater than zero.")
        return

    print(f"\nEnter the cost matrix ({size} x {size}):")
    print("Enter each row separated by spaces.")

    matrix = []

    for i in range(size):
        while True:
            try:
                row = list(map(int, input(f"Employee {i + 1}: ").split()))

                if len(row) != size:
                    print(f"Please enter exactly {size} values.")
                    continue

                matrix.append(row)
                break

            except ValueError:
                print("Invalid input. Please enter integers.")

    try:
        assignment, total_cost = solve_hungarian(matrix)

        print("\n========== OPTIMAL ASSIGNMENT ==========")

        for employee, task in sorted(assignment.items()):
            cost = matrix[employee][task]

            print(
                f"Employee {employee + 1} "
                f"-> Task {task + 1} ({cost})"
            )

        print("---------------------------------------")
        print(f"Minimum Total Cost: {total_cost}")
        print("=======================================")

    except (ValueError, RuntimeError) as error:
        print(f"Error: {error}")


# Added:
# Program Entry Point
# Description: Start the program when this file is executed.
if __name__ == "__main__":
    main()
