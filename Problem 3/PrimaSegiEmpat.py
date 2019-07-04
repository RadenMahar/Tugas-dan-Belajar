def primaSegiEmpat(P, L, X):
    print("'''")
    str_temp = ""
    n = P * L
    list_temp = []
    bil_setelah_X = X + 1
    banyak_bill_ditemukan = 0
    while True:
        faktor_temp = 0
        for k in range(1, bil_setelah_X+1):
            if bil_setelah_X % k == 0:
                faktor_temp += 1

        if faktor_temp == 2:
            list_temp.append(bil_setelah_X)
            banyak_bill_ditemukan += 1
            bil_setelah_X += 1

            if banyak_bill_ditemukan == n:
                break

        else:
            bil_setelah_X += 1

    jumlah = list_temp[0]       
    for i in range(1, n):
        jumlah += list_temp[i]

    for i in range(1, n+1):
        if list_temp[i-1] < 7:
            str_temp += (str(list_temp[i-1])+"  ")   
        else:
            str_temp += (str(list_temp[i-1])+" ")
        if i%(P) == 0:
            str_temp += "\n"

    print(str_temp)
    print("Total: {}".format(jumlah))
    print("'''")

#primaSegiEmpat(2, 3, 15)
primaSegiEmpat(5, 2, 1)