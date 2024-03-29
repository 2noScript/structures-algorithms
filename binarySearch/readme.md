[![Back](https://img.shields.io/badge/Back-%F0%9F%91%88-blue)](/)

- In this implementation, the binary_search function takes a sorted array (arr) and a target value (target) as inputs. The algorithm maintains two pointers, left and right, representing the indices of the subarray where the target might be found.

- The algorithm enters a while loop that continues until left is greater than right. Within each iteration, it calculates the mid index as the average of left and right. It then checks if the element at arr[mid] is equal to the target. If it is, the function returns the index mid.

- If the target is less than arr[mid], it means the target must be in the left half of the array, so the right pointer is updated to mid - 1. Similarly, if the target is greater than arr[mid], it must be in the right half, so the left pointer is updated to mid + 1.

- If the target is not found after the loop completes, the function returns -1.





<img src='https://raw.githubusercontent.com/AlvaroIsrael/binary-search/main/src/assets/binary-search-small.gif'>


```py

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



```