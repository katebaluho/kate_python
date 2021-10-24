# from tic_tac_toe import matrix_match
import tic_tac_toe


def test_matrix():
    matrix_tests = (
        (([1, 1, 1],
          [0, 0, 0],
          [0, 0, 0]), True),

        (([0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]), True),

        (([0, 0, 0],
          [0, 0, 0],
          [2, 2, 2]), True),

        (([0, 1, 2],
          [0, 0, 1],
          [1, 1, 2]), False),

        (([1, 0, 0],
          [1, 0, 0],
          [1, 0, 0]), True),

        (([0, 1, 0],
          [0, 1, 0],
          [0, 1, 0]), True),

        (([0, 0, 2],
          [0, 0, 2],
          [0, 0, 2]), True),
        (([2, 1, 2],
          [0, 1, 2],
          [0, 0, 1]), False),
        (([1, 1, 2],
          [0, 1, 2],
          [0, 0, 1]), True),
        (([2, 1, 1],
          [0, 1, 2],
          [1, 0, 1]), True),
    )

    for test in matrix_tests:
        assert tic_tac_toe.matrix_match(test[0]) is test[1], test[0]

test_matrix()