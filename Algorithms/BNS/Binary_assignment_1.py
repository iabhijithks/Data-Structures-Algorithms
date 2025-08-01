def count_rot(arr):
    low = 0
    high = len(arr)-1

    while low <= high:
        if arr[low] < arr[high]:
            return low
        mid = (low + high)//2
        next = (mid+1+len(arr))%len(arr)
        prev = (mid-1+len(arr))%len(arr)

        if arr[mid]<=arr[next] and arr[mid]<=arr[prev]:
            return mid
        
        if arr[mid]>arr[low]:
            high = mid-1
        else:
            low = mid +1

print(count_rot([5, 6, 9, 0, 2, 3, 4]))  # Output: 3




