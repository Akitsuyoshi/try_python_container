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


print(selection_sort([65, 55, 1, 45, 35, 25, 15, 10]))
# %%


def insertion_sort(arr: list[int]) -> list[int]:
    for i in range(1, len(arr)):
        position = i
        temp_val = arr[i]

        while position > 0 and arr[position - 1] > temp_val:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = temp_val
    return arr


print(insertion_sort([65, 55, 1, 45, 35, 25, 15, 10]))

# %%


class SortableArray:
    def __init__(self, arr: list[int]) -> None:
        self.arr = arr

    def partion(self, left_pointer: int, right_pointer: int) -> int:
        pivot_position = right_pointer
        pivot = self.arr[pivot_position]
        right_pointer -= 1

        while True:
            while self.arr[left_pointer] < pivot:
                left_pointer += 1
            while self.arr[right_pointer] > pivot:
                right_pointer -= 1

            if left_pointer >= right_pointer:
                break
            else:
                self._swap(left_pointer, right_pointer)

        # As a final step, we swap th lef pointer with the pivot itself
        self._swap(left_pointer, pivot_position)

        return left_pointer

    def _swap(self, pointer_1: int, pointer_2: int) -> None:
        self.arr[pointer_1], self.arr[pointer_2] = self.arr[pointer_2], self.arr[pointer_1]

    def quicksort(self, left_idx: int, right_idx: int) -> None:
        # base case
        if right_idx - left_idx <= 0:
            return None

        pivot_position = self.partion(left_idx, right_idx)
        self.quicksort(left_idx, pivot_position - 1)
        self.quicksort(pivot_position + 1, right_idx)

    def quickselect(self, kth_lowest_position: int, left_idx: int, right_idx: int) -> int:
        # base cases
        if right_idx - left_idx <= 0:
            return self.arr[left_idx]

        pivot_position = self.partion(left_idx, right_idx)
        if kth_lowest_position < pivot_position:
            return self.quickselect(kth_lowest_position, left_idx, pivot_position - 1)
        elif kth_lowest_position > pivot_position:
            return self.quickselect(kth_lowest_position, pivot_position + 1, right_idx)
        else:
            return self.arr[pivot_position]


sortable_arr = SortableArray([0, 5, 2, 1, 6, 3, 9])
# sortable_arr.quicksort(0, len(sortable_arr.arr) - 1)
# print(sortable_arr.arr)
print(sortable_arr.quickselect(1, 0, len(sortable_arr.arr) - 1))

# %%


class Node:
    def __init__(self, data: str) -> None:
        self.data = data
        self.next_node: Union[Node, None] = None
        self.previous_node: Union[Node, None] = None


class LinkedList:
    def __init__(self, first_node: Node) -> None:
        self.first_node = first_node

    def read(self, idx: int) -> Union[str, None]:
        current_node = self.first_node
        current_idx = 0

        while current_idx < idx and current_node:
            current_node = current_node.next_node
            current_idx += 1

        if not current_node:
            return None

        return current_node.data

    def index_of(self, val: str) -> Union[int, None]:
        current_node = self.first_node
        current_idx = 0

        while current_node:
            if current_node.data == val:
                return current_idx

            current_node = current_node.next_node
            current_idx += 1

        return None

    def insert_at_index(self, idx: int, val: str) -> None:
        current_node = self.first_node
        current_idx = 0

        while current_idx < idx and current_node:
            current_node = current_node.next_node
            current_idx += 1

        if not current_node:
            return None

        new_node = Node(val)
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node

    def delete_at_index(self, idx: int) -> None:
        current_node = self.first_node
        current_idx = 0

        while current_idx < idx - 1 and current_node:
            current_node = current_node.next_node
            current_idx += 1

        if not current_node or not current_node.next_node:
            return None

        current_node.next_node = current_node.next_node.next_node


class DoubleLinkedList:
    def __init__(self, first_node: Union[Node, None] = None, last_node: Union[Node, None] = None) -> None:
        self.first_node = first_node
        self.last_node = last_node

    def insert_at_end(self, val: str) -> None:
        new_node = Node(val)

        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.first_node.next_node = new_node
            self.last_node = new_node

    def remove_from_front(self) -> Union[Node, None]:
        removed_node = self.first_node
        if removed_node:
            self.first_node = removed_node.next_node

        return removed_node


class Queque:
    def __init__(self) -> None:
        self.queque = DoubleLinkedList()

    def enque(self, val: str) -> None:
        self.queque.insert_at_end(val)

    def deque(self) -> Union[str, None]:
        if removed_node := self.queque.remove_from_front():
            return removed_node.data
        return None

    def tail(self) -> Union[str, None]:
        if last_node := self.queque.last_node:
            return last_node.data
        return None
