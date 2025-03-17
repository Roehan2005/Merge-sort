# Insertion Sort for Hybrid Merge Sort
def insertion_sort(arr, left, right):
    """Helper function to perform Insertion Sort on a subarray."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Function for Hybrid Merge Sort
def merge(arr, left, mid, right):
    """Helper function to merge two sorted subarrays."""
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Hybrid Merge Sort using Insertion Sort for small subarrays
def hybrid_merge_sort(arr, left, right, threshold):
    """Hybrid Merge Sort using Insertion Sort for small subarrays."""
    if left < right:
        # If subarray is smaller than or equal to threshold, use Insertion Sort
        if right - left <= threshold:
            insertion_sort(arr, left, right)  # Use Insertion Sort for small subarrays
        else:
            mid = (left + right) // 2
            hybrid_merge_sort(arr, left, mid, threshold)       # Recursively sort the left half
            hybrid_merge_sort(arr, mid + 1, right, threshold)  # Recursively sort the right half
            merge(arr, left, mid, right)                       # Merge the sorted halves

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    threshold = 3  # Threshold for using Insertion Sort for small subarrays

    print("Original array:", arr)
    hybrid_merge_sort(arr, 0, len(arr) - 1, threshold)
    print("Sorted array using Hybrid Merge Sort:", arr)
