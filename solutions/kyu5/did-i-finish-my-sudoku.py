# encoding: UTF-8

"""
https://www.codewars.com/kata/did-i-finish-my-sudoku
"""

import codewars


def is_completed(block):
    return len(set(block)) == 9


def sub_board(board, i, j):
    numbers = []
    for line in board[i * 3: (i + 1) * 3]:
        numbers.extend(line[j * 3: (j + 1) * 3])
    return numbers


def _done_or_not(board):
    done = all(is_completed(line) for line in board)
    if not done:
        return False
    done = all(is_completed([line[x] for line in board]) for x in range(9))
    if not done:
        return False
    for i in range(3):
        for j in range(3):
            done = done and is_completed(sub_board(board, i, j))
            if not done:
                return False
    return True


def done_or_not(board):
    return 'Finished!' if _done_or_not(board) else 'Try again!'


with codewars.Test(namespace=globals()) as test:
    test.assert_equals(done_or_not([
        [1, 3, 2, 5, 7, 9, 4, 6, 8],
        [4, 9, 8, 2, 6, 1, 3, 7, 5],
        [7, 5, 6, 3, 8, 4, 2, 1, 9],
        [6, 4, 3, 1, 5, 8, 7, 9, 2],
        [5, 2, 1, 7, 9, 3, 8, 4, 6],
        [9, 8, 7, 4, 2, 6, 5, 3, 1],
        [2, 1, 4, 9, 3, 5, 6, 8, 7],
        [3, 6, 5, 8, 1, 7, 9, 2, 4],
        [8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!')

    test.assert_equals(done_or_not(
        [[1, 3, 2, 5, 7, 9, 4, 6, 8],
         [4, 9, 8, 2, 6, 1, 3, 7, 5],
         [7, 5, 6, 3, 8, 4, 2, 1, 9],
         [6, 4, 3, 1, 5, 8, 7, 9, 2],
         [5, 2, 1, 7, 9, 3, 8, 4, 6],
         [9, 8, 7, 4, 2, 6, 5, 3, 1],
         [2, 1, 4, 9, 3, 5, 6, 8, 7],
         [3, 6, 5, 8, 1, 7, 9, 2, 4],
         [8, 7, 9, 6, 4, 2, 1, 3, 5], ]), 'Try again!')
