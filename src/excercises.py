# %%

import string
from math import sqrt
from random import randint, randrange
from typing import Any, List, Sequence, Tuple


# Checks if n is mutiple of m.
def mutiple(n: int, m: int) -> bool:
    return n % m == 0


mutiple(5, 2)
mutiple(8, 4)
# %%


def is_even(k: int) -> bool:
    return k % 2 == 0


is_even(1)
# %%


def minmax(data: Sequence[int]) -> Tuple[int, int]:
    assert len(data) > 0, 'Data should contains more than one element.'

    min_val = max_val = data[0]
    for elem in data:
        if elem < min_val:
            min_val = elem
        elif elem > max_val:
            max_val = elem

    return min_val, max_val


minmax([2, 5, 7, 1, 3, -1])
# %%


def sum_of_squared(n: int) -> int:
    assert n > 0, 'n should be positive integer.'

    return sum([i ** 2 for i in range(n)])


sum_of_squared(4)

# %%


def sum_of_odd_squared(n: int) -> int:
    assert n > 0, 'n should be positive integer.'

    return sum([i ** 2 for i in range(n) if not is_even(i)])


sum_of_odd_squared(6)
# %%


def rand_choice(data: Sequence[int]) -> int:
    assert len(data) > 0, 'Data should contains more than one element.'
    min_val, max_val = minmax(data)
    return randrange(start=min_val, stop=max_val + 1)


rand_choice([1, 2, 3])
# %%


def reverse_list(data: list[int]) -> list[int]:
    # data.reverse()
    return [data[-i] for i in range(1, len(data) + 1)]


reverse_list([1, 4, 7, 3, 5])
# %%


def is_any_odd(data: Sequence[int]) -> bool:
    # odd * odd = odd, odd * even = even, even * even = even
    odd_nums = set()
    for i in data:
        if not is_even(i):
            odd_nums.add(i)
        if len(odd_nums) >= 2:
            return True
    return False


is_any_odd([1, 4, 6])

# %%


def is_distinct_element(data: Sequence[int]) -> bool:
    return len(data) == len(set(data))


is_distinct_element((1, 4, 5, 2, 6, 11, 1))
# %%


def shuffle_using_randint(data: list[int]) -> list[int]:
    # visited_idx = set()
    visited_idx = []
    shuffled_data = []

    while len(shuffled_data) != len(data):
        rand_idx = randint(0, len(data) - 1)
        if rand_idx not in visited_idx:
            visited_idx.append(rand_idx)
            shuffled_data.append(data[rand_idx])

    return shuffled_data


shuffle_using_randint([1, 4, 7, 3, 5, 11, 50, 43, 10, 5])
# %%
# C-1.21
# Write a Python program that repeatedly reads lines from standard input until an EOFError is raised, and then outputs
# those lines in reverse order (a user can indicate end of input by typing ctrl-D).

# import sys

# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break
#     print('input' + line)
# print('Exit')
# %%


def dot_list(list_1: Sequence[int], list_2: Sequence[int]) -> Sequence[int]:
    return [elm_1 * elm_2 for elm_1, elm_2 in zip(list_1, list_2)]


print(dot_list([1, 2, 3], [4, 5, 6]))
# %%
# C-1.23


def catch_outof_bounds(list: List[Any], new_elm: Any, idx: int) -> None:
    try:
        list[idx] = new_elm
    except Exception:
        print("Don’t try buffer overflow attacks in Python!")
# %%


def count_vowels(chars: str) -> int:
    vowels = []
    for char in chars.lower():
        if char in ("a", "e", "i", "o", "u"):
            vowels.append(char)

    return len(vowels)


count_vowels('sOme')
# %%
# # C-1.25


def remove_puncs(sentence: str) -> str:
    sentence_wo_puncs = []
    for s in sentence:
        if s in string.punctuation:
            continue
        sentence_wo_puncs.append(s)
    return ''.join(sentence_wo_puncs)


remove_puncs('Hey, Geeks !, How are you?')

# %%


def factors(n):
    results = []
    for k in range(1, n + 1):
        if n % k == 0:
            results.append(k)
    return results


factors(100)
# %%


def factors_ordered(n):
    denominators = []

    k = 1
    while k * k <= n:
        if n % k == 0:
            denominators.append(k)
            yield k
        k += 1
    for d in reversed(denominators):
        yield n // d


for f in factors_ordered(100):
    print(f)

# %%


def norm(v: int, p: int) -> float:
    return sqrt(v ** 2 + p ** 2)


norm(3, 4)

# %%
