# heap data strucutures are data structures that are used to implement priority queues. 
# A heap is a binary tree that satisfies the heap property: for a max heap, each parent node is greater than or equal to its children, and for a min heap, each parent node is less than or equal to its children. 
# Heaps are commonly used in algorithms like Dijkstra's shortest path and Prim's minimum spanning tree.

# There are two types of heap data structures: max heap and min heap. 
# A max heap is a heap where each parent node is greater than or equal to its children, and a min heap is a heap where each parent node is less than or equal to its children.



# heapq modeule in python provides an implementation of the heap data structure. It provides functions for creating and manipulating heaps, such as heappush, heappop, and heapify.
import heapq
# Example of using heapq to create a min heap
min_heap = []
heapq.heappush(min_heap, 5)  #heappush adds an element to the heap: it takes two arguments: the heap and the element to be added.
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 1)
print(min_heap)  # Output: [1, 2, 3, 5, 8]



max_heap = []
heapq.heappush(max_heap, -5)  # To create a max heap, we can push the negative of the values onto the heap. This way, the smallest value (which is the largest negative value) will be at the top of the heap.
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -1)

# heapq.heappop(max_heap) will return the smallest value in the heap, which is the largest negative value. To get the original value, we can negate it again.
print(heapq.heappop(min_heap))  # Output: 1
print(-heapq.heappop(max_heap))  # Output: 8