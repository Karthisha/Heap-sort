def heap_sort(array):
  # Build the max heap
  for i in range(len(array) - 1, -1, -1):
    heapify(array, len(array), i)
    
  # Extract the elements from the heap one by one
  for i in range(len(array) - 1, 0, -1):
    array[i], array[0] = array[0], array[i]   # Swap the root of the heap with the last element
    heapify(array, i, 0)   # Re-heapify the reduced heap
    
  return array
  
def heapify(array, heap_size, root_index):
  # Assume the root is the largest element
  largest = root_index
  left_child = 2 * root_index + 1
  right_child = 2 * root_index + 2
  
  # If the left child of the root is larger than the root, set the largest variable to the left child's index
  if left_child < heap_size and array[left_child] > array[largest]:
    largest = left_child
  
  # If the right child of the root is larger than the root, set the largest variable to the right child's index
  if right_child < heap_size and array[right_child] > array[largest]:
    largest = right_child
  
  # If the largest element is not the root, swap the root with the largest element and heapify the affected sub-tree
  if largest != root_index:
    array[root_index], array[largest] = array[largest], array[root_index]
    heapify(array, heap_size, largest)

# Test the heap_sort function
print(heap_sort([4, 6, 2, 5, 1, 3]))   # [1, 2, 3, 4, 5, 6]
