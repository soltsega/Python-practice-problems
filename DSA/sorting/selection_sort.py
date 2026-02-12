# Selection sort in python
# This works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and swapping it with the first unsorted element until the entire list is sorted.
# Selection sort is an in-place sorting algorithm, which means that it does not require additional space

# Time complexity: O(N^2) for the worst case and O(N^2/2) for the best case which is inefficient
# Space complexity: O(1) which is efficient as it is an in-place sorting algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # find teh minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap the found minimum element with the first unsorted element
        if min_index != 1:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(selection_sort([2,1,3,0,5,4]))
