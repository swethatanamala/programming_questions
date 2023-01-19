def get_index(arr: list[int]):
    n = len(arr)
    left, right = 0, n
    while (left < right):
        mid = (left + right)//2
        if (mid + 1 >= n) or (mid - 1 < 0):
            return mid
        else:
            if (arr[mid] > arr[mid + 1]) and (arr[mid - 1] < arr[mid]):
                return mid
            elif arr[mid - 1] < arr[mid]:
                left = mid + 1
            else:
                right = mid
    
arr = [3, 9, 10, 20, 17, 5, 1]
ind = get_index(arr)
result = arr[:ind] + arr[ind:][::-1]
print(result)