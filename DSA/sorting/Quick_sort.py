# Quick sort in python
# It is based on the fac that if we can partition an array into two parts such that all elements in the first part are less than or equal to a pivot element 
# and all elements in the second part are greater than the pivot element, then we can sort the two parts independently and combine them to get the sorted array.


# Time complexity: O(n log n) which is efficient as it is linearithmic
# Space complexity: O(log n) which is efficient as it is logarithmic

def quick_sort(arr):
    
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2] # we choose the middle element as the pivot
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]

    return quick_sort[left] + middle + quick_sort[right] 