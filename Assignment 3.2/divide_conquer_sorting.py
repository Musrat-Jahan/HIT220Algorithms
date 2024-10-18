# divide_conquer_sorting.py

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        print(f"Merge step: {arr}")

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        sorted_arr = quick_sort(left) + middle + quick_sort(right)
        print(f"Quick step with pivot {pivot}: {sorted_arr}")
        return sorted_arr

if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    print("Original array:", arr)

    # Merge Sort
    print("\n--- Merge Sort ---")
    merge_sort(arr.copy())

    # Quick Sort
    print("\n--- Quick Sort ---")
    quick_sort(arr.copy())
