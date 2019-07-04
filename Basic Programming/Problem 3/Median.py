def carimedian(arr):
    n = len(arr)
    
    if len(arr)%2 != 0:
        med = arr[(int((n+1)/2))-1]
        return med
    else:
        temp = (arr[(int(n/2))-1]+arr[int(n/2)])
        if temp % 2 == 0:
            med = int((1/2)*temp)
            return med
        else:
            med = (1/2)*temp
            return med
    
print(carimedian([1, 2, 3, 4, 5]))
print(carimedian([1, 3, 4, 10, 12, 13]))
print(carimedian([3, 4, 7, 6, 10]))
print(carimedian([1, 3, 3]))
print(carimedian([7, 7, 8, 8]))
