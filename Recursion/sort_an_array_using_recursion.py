# Base Case: If array size is 1 or smaller, return.
# Recursively sort first n-1 elements.
# Insert the last element at its correct position in the sorted array.

# Sort an array using Recursion
def sort_using_recursion(arr, n):
    if n <= 1:
        return
    sort_using_recursion(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = last


if __name__ == "__main__":
    arr = [7, 6, 1, 5, 2, 4, 3]
    sort_using_recursion(arr, len(arr))
    print(arr)

    # time complexity: O(n^2)
    # space complexity: O(n)
