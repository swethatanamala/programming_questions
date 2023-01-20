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
    
def find(arr, search):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == search:
            return mid
        elif arr[mid] < search:
            left = mid + 1
        else:
            right = mid
    return -1

arr = [5, 6, 7, 8, 9, 10, 3, 2, 1]
search = -1
ind, n = get_index(arr), len(arr)

if ind == 0:
    arr = arr[::-1]
elif ind < n - 1:
    i, j = ind, ind + 1
    tmp = arr[j]
    while (i >= -1) and (j < n):
        if (i >= 0) and (arr[i] > tmp):
            i -= 1
        else:
            k = i + 1
            place1 = arr[k]
            while k < j:
                place2 = arr[k + 1]
                arr[k + 1] = place1
                place1 = place2
                k += 1
            arr[i + 1] = tmp
            j += 1
            if j == n:
                break
            tmp = arr[j]
print(arr, search)
print(find(arr, search))

