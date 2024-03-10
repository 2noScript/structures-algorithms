


def linearSearch(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
        return -1 
    

arr=[10,14,19,26,27,31,33,35,42,44]
target=33

index=linearSearch(arr,target)

print(f'index:{index}')
    