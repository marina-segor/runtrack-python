from itertools import permutations


def is_safe(permutation):
    size = len(permutation)
    for i in range(size):
        for j in range(i + 1, size):
            if abs(permutation[i] - permutation[j]) == abs(i - j):
                return False
    return True


def solve(board_size):
    solutions = []
    for permutation in permutations(range(board_size)):
        if is_safe(permutation):
            solutions.append(permutation)
    return solutions


def print_solutions(solutions, board_size):
    separator = '+---' * board_size + '+'
    for solution in solutions:
        for column in solution:
            print(separator)
            print('|   ' * column + '| Q |' +
                  '   |' * (board_size - 1 - column))
        print(separator)
        print
    print("Found", len(solutions), "solutions")


size = 8
solutions = solve(size)
print_solutions(solutions, size)
