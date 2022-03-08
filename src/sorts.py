# %%

def insertion(arr):
    for i in range(len(arr)):
        # j = i - 1
        # while j >= 0 and arr[j] > arr[j + 1]:
        #     arr[j], arr[j + 1] = arr[j + 1], arr[j]
        #     j -= 1
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                break
    return arr


print(insertion([1, 5, 3, 6, 4, 2]))
# %%


def merge(arr, p, q, r):
    len_left = q - p + 1
    len_right = r - q
    left_arr = [0] * (len_left + 1)
    right_arr = [0] * (len_right + 1)
    print(left_arr, right_arr)

    for i in range(len_left):
        left_arr[i] = arr[p + i]
    for i in range(len_right):
        right_arr[i] = arr[q + i + 1]

    left_arr[-1] = float('inf')
    right_arr[-1] = float('inf')

    i = j = 0
    for k in range(r):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1

    print(left_arr, right_arr, arr)


merge([1, 5, 3, 6, 4, 2], 0, 2, 5)
# %%


def binarySearch(lst, elt):
    n = len(lst)
    if elt < lst[0] or elt > lst[n - 1]:
        return None
    else:
        return binarySearchHeper(lst, elt, 0, n - 1)


def binarySearchHeper(lst, elt, left, right):
    if left > right:
        return None
    else:
        mid = (left + right) // 2
        if lst[mid] == elt:
            return mid
        elif lst[mid] < elt:
            return binarySearchHeper(lst, elt, mid + 1, right)
        else:  # lst[mid] > elt
            return binarySearchHeper(lst, elt, left, mid - 1)


print("Searching for 9 in list [0,2,3,4,6,9,12]")
print(binarySearch([0, 2, 3, 4, 6, 9, 12], 9))

print("Searching for 8 in list [1, 3, 4, 6, 8, 9,10, 11, 12, 15]")
print(binarySearch([1, 3, 4, 6, 8, 9, 10, 11, 12, 15], 8))

print("Searching for 5 in list [1, 3, 4, 6, 8, 9,10, 11, 12, 15]")
print(binarySearch([1, 3, 4, 6, 8, 9, 10, 11, 12, 15], 5))

print("Searching for 0 in list [0,2]")
print(binarySearch([0, 2], 0))

print("Searching for 1 in list [0,2]")
print(binarySearch([0, 2], 1))

print("Searching for 2 in list [0,2]")
print(binarySearch([0, 2], 2))

print("Searching for 1 in list [1]")
print(binarySearch([1], 1))

print("Searching for 2 in list [1]")
print(binarySearch([1], 2))

# %%
