> In linear search, each element of the array is sequentially checked until the target element is found or the end of the array is reached. If the target element is found, the function returns the index of that element in the array. If the target element is not found in the array, the function returns -1

<img src='https://sushrutkuchik.files.wordpress.com/2020/05/linear_search.gif?w=438'>

```py

def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return -1


arr=[10,14,19,26,27,31,33,35,42,44]
target=33

index=linearSearch(arr,target)


```
