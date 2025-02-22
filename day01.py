import numpy as np
from collections import Counter

from utils import get_input


def l1_norm(vec1: np.ndarray, vec2: np.ndarray) -> int:
    """Calculate the L1 norm (Manhattan distance) between two vectors."""
    return np.sum(np.abs(vec1 - vec2))


def aoc1():
    left_tuple, right_tuple = zip(*[map(int, row.split()) for row in get_input(day=1)])

    left_list, right_list = list(left_tuple), list(right_tuple)

    left_list.sort()
    right_list.sort()

    left_array = np.array(left_list, dtype=np.int64)
    right_array = np.array(right_list, dtype=np.int64)

    result = l1_norm(left_array, right_array)

    return result


def aoc2():
    left_tuple, right_tuple = zip(*[map(int, row.split()) for row in get_input(day=1)])

    counts = Counter(right_tuple)

    similarity_score = sum(val * counts[val] for val in left_tuple) 

    return similarity_score


if __name__ == "__main__":
    print("Answer 1:", aoc1())
    print("Answer 2:", aoc2())
