def max_sum_list(arr):
    max = -float('inf')
    for i in range(len(arr)):
        sum = 0
        for j in arr[i:]:
            sum += j
            if sum > max:
                max = sum
    return max

print(max_sum_list([-2, 1, -3, 4, -1, 2, 1, -5, 4]))