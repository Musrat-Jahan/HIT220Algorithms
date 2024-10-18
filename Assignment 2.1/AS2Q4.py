def heapsort(array):
    n = len(array)
    
    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root (maximum value) with the last element
        array[0], array[i] = array[i], array[0]
        
        # Reduce the size of the heap by 1
        heapify(array, i, 0)

def heapify(array, size, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    # Check if left child is larger than root
    if left < size and array[left] > array[largest]:
        largest = left

    # Check if right child is larger than the largest so far
    if right < size and array[right] > array[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != root:
        array[root], array[largest] = array[largest], array[root]
        heapify(array, size, largest)

# Example usage
if __name__ == "__main__":
    array = [2, 7, 4, 13, 9, 10, 5, 6, 13]
    print("Original array:", array)
   
    # Build the max-heap
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    # Print final max-heap array
    print("Final Max-Heap Array:", array)
    # Perform heapsort
    heapsort(array)
    
    # Print the sorted array
    print("Sorted array:", array)
