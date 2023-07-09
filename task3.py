from typing import List


def get_pairs(lst: List):
    if len(lst) < 2:
        return None
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]


list_1 = [1, 2, 3, 4, 5, 6]

print(get_pairs(list_1))
