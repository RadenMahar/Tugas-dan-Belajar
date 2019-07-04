def ConverttoCoin(value):
    list_temp  = []
    x = [1, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    n = len(x) - 1
    while n > -1 :
        simpan_banyak = int(value / x[n-1])
        if int(simpan_banyak) > 0:
            for i in range(simpan_banyak):
                list_temp.append(x[n-1])
                value = value % x[n-1]
        else:
            n -= 1    
    return list_temp
    
print(ConverttoCoin(543))
print(ConverttoCoin(7752))
