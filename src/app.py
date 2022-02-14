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

# %%
