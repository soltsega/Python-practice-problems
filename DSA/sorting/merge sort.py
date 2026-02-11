# merge sotrt is a divide and conquer algorithm that divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
# merge sort is a stable sorting algorithm, which means that it preserves the relative order of equal elements in the input array.
# merge sort is an efficient sorting algorithm with a time complexity of O(n log n) in all cases (best, average, and worst).
# merge sort is not an in-place sorting algorithm, which means that it requires additional space for the temporary arrays used for merging.
# merge sort is a recursive algorithm, which means that it calls itself for the two halves of the input array until it reaches the base case of a single element or an empty array.
# merge sort is a good choice for sorting large datasets that do not fit in memory, as it can be implemented using an external sorting algorithm that uses disk storage to handle large datasets.


# the code implementation of merge sort in python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # find the middle index of the array
    left = merge_sort(arr[:mid])  # recursively sort the left half of the array2w
    right = merge_sort(arr[mid:])

    sorted_list = []
    i = 0  # pointer for the left half of the array
    j = 0  # pointer for the right half of the array

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list