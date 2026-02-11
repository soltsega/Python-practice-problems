# bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
# bubble sort is a stable sorting algorithm, which means that it preserves the relative order of equal elements in the input array.
# bubble sort is an inefficient sorting algorithm with a time complexity of O(n^2) in the worst and average cases, and O(n) in the best case (when the input array is already sorted).
# bubble sort is an in-place sorting algorithm, which means that it does not require additional space

# Time complexity: O(N^2) which is inefficient
# Space complexity: O(1) which is efficient as it is an in-place sorting algorithm 

# let's dive in
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # flag to check if any swapping occurs
        swapped = False
        # last i elements are already in place, so we can skip them
        for j in range(0, n - i - 1):  # we made the range from 0 up to n - i - 1 because we don't want to compare the last i elements which are already sorted
            # check if arr[j] is greater than arr[j + 1]
            if arr[j] > arr[j + 1]:
                # swap arr[j] and arr[j + 1]
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
                break  # this happens when the input array is already sorted, so we can break out of the loop early: best case time complexity is O(n)
    return arr

print(bubble_sort([2,1,3,0,5,4]))