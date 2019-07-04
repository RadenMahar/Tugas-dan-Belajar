def MaksimumDeretBilangan(bill):
    temp_bill = []
    for i in range(0, len(bill)):
        for j in range(0, len(bill)):
            sum = 0
            for k in range(i, j+1):
                sum += bill[k]
            temp_bill.append(sum)
    
    var_max = 0
    for i in range(0, len(temp_bill)):
        if var_max < temp_bill[i]:
            var_max = temp_bill[i]
    
    return var_max


print(MaksimumDeretBilangan([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(MaksimumDeretBilangan([-2, -5, 6, -2, -3, 1, 5, -6]))
print(MaksimumDeretBilangan([1]))