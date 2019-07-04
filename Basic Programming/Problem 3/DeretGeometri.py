def tentukanDeretGeometri(arr):
    r = arr[1]/arr[0]
    a = arr[0]
    n = len(arr)
    count_temp = 0
    for i in range(0, n):
        suku_temp = a*(r**i)
        if suku_temp == arr[i]:
            count_temp += 1
    
    if count_temp == n:
        return True
    else:
        return False

print(tentukanDeretGeometri([1, 3, 9, 27, 81]))
print(tentukanDeretGeometri([2, 4, 8, 16, 32]))
print(tentukanDeretGeometri([2, 4, 6, 28]))
print(tentukanDeretGeometri([2, 6, 18, 54]))
print(tentukanDeretGeometri([1, 2, 3, 4, 7, 9]))