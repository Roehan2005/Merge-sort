# Merge Function for Normal Merge Sort
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

# Standard Merge Sort Function
def merge_sort(arr, left, right):
    """Standard Merge Sort."""
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)       # Recursively sort the left half
        merge_sort(arr, mid + 1, right)  # Recursively sort the right half
        merge(arr, left, mid, right)     # Merge the sorted halves

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Original array:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array using Normal Merge Sort:", arr)
