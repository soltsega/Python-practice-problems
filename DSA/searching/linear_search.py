# Linear search is a simple searching algorithm that checks each element in a list sequentially until the target value is found or the end of the list is reached. It has a time complexity of O(n) and a space complexity of O(1). Linear search is not efficient for large datasets, but it can be useful for small lists or when the target value is likely to be found near the beginning of the list.
# 

# Assumption: the input list can contain duplicate elements. The linear search algorithm will return the index of the first occurrence of the target value in the list, even if there are multiple occurrences of the target value. Therefore, if the input list contains duplicate elements, the linear search algorithm will still work correctly and return the index of the first occurrence of the target value.
# Time complexity: O(n) which is inefficient as it is linear particularly for large datasets
# Space complexity: O(1) which is efficient as it is an in-place algorithm


def linear_search(search_list, value):
    for index in range(len(search_list)):
        if search_list[index] == value:
            return index
    return -1