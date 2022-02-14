from typing import Union

# %%


def linear_search(arr: list[int], val: int) -> Union[int, None]:
    for elm in arr:
        if elm == val:
            return val
        elif elm > val:
            break
    return None


print(linear_search([3, 17, 22, 80, 220], 25))

# %%


def binary_search(arr: list[int], val: int) -> Union[int, None]:
    lower_bound = 0
    upper_bound = len(arr) - 1

    while lower_bound <= upper_bound:
        mid_point = (upper_bound + lower_bound) // 2
        val_at_mid_point = arr[mid_point]

        if val == val_at_mid_point:
            return mid_point
        elif val < val_at_mid_point:
            upper_bound = mid_point - 1
        elif val > val_at_mid_point:
            lower_bound = mid_point + 1

    return None


print(binary_search([3, 17, 22, 80, 220], 80))
# %%


def bubble_sort(arr: list[int]) -> list[int]:
    unsorted_until_idx = len(arr) - 1

    while unsorted_until_idx != 0:
        for i in range(unsorted_until_idx):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        unsorted_until_idx -= 1
    return arr


print(bubble_sort([65, 55, 1, 45, 35, 25, 15, 10]))

# %%


def selection_sort(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        lowest_num_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_num_idx]:
                lowest_num_idx = j

        if lowest_num_idx != i:
            arr[i], arr[lowest_num_idx] = arr[lowest_num_idx], arr[i]

    return arr
