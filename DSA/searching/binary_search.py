# binary search is an algorithm to search a value in an iterable

# Time complexity: O(log n) which is efficient as it is logarithmic
# Space complexity: O(1) which is efficient as it is an in-place algorithm

# The return type of the binary search function is a tuple containing the path to the target value and a message indicating whether the value was found or not. The path to the target value is a list of values that were compared during the search process, which can be useful for understanding how the algorithm works and for debugging purposes. The message indicates whether the value was found at a specific index or if it was not found in the list.
# Assumpiton: the input list is sorted in ascending order. If the input list is not sorted, the binary search algorithm will not work correctly and may return incorrect results. Therefore, it is important to ensure that the input list is sorted before using the binary search algorithm.
# The implementation on binary search 
def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1

    return [], "Value not found"

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))