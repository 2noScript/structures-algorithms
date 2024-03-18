def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr = [20, 51, 54, 59, 75, 76, 77, 78, 89, 92]
target = 92
result = binarySearch(arr, target)
if result != -1:
    print("Element", target, "found at index", result)
else:
    print("Element", target, "not found in the array")

