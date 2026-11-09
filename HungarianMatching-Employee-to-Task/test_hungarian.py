
import pytest

from hungarian import solve_hungarian, validate_matrix


def test_sample_3x3():
    matrix = [
        [4, 1, 3],
        [2, 0, 5],
        [3, 2, 2]
    ]

    assignment, total_cost = solve_hungarian(matrix)

    assert total_cost == 5
    assert len(assignment) == 3


def test_sample_4x4():
    matrix = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]

    assignment, total_cost = solve_hungarian(matrix)

    assert total_cost == 13
    assert len(assignment) == 4


def test_sample_6x6():
    matrix = [
        [14, 5, 8, 7, 15, 9],
        [2, 12, 6, 5, 9, 11],
        [7, 8, 3, 9, 6, 10],
        [9, 6, 12, 4, 8, 7],
        [6, 10, 7, 8, 5, 12],
        [11, 7, 9, 6, 10, 3]
    ]

    assignment, total_cost = solve_hungarian(matrix)

    assert total_cost == 22
    assert len(assignment) == 6


def test_single_element():
    matrix = [[15]]

    assignment, total_cost = solve_hungarian(matrix)

    assert assignment == {0: 0}
    assert total_cost == 15


def test_assignment_validity():
    matrix = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ]

    assignment, total_cost = solve_hungarian(matrix)

    assert len(assignment) == len(matrix)
    assert len(set(assignment.values())) == len(matrix)

    for employee, task in assignment.items():
        assert 0 <= employee < len(matrix)
        assert 0 <= task < len(matrix)

    calculated_cost = sum(
        matrix[employee][task]
        for employee, task in assignment.items()
    )

    assert total_cost == calculated_cost


def test_empty_matrix():
    with pytest.raises(ValueError):
        validate_matrix([])


def test_non_square_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    with pytest.raises(ValueError):
        validate_matrix(matrix)


def test_negative_cost():
    matrix = [
        [1, 2],
        [3, -4]
    ]

    with pytest.raises(ValueError):
        validate_matrix(matrix)


def test_non_numeric_cost():
    matrix = [
        [1, 2],
        [3, "invalid"]
    ]

    with pytest.raises(ValueError):
        validate_matrix(matrix)
