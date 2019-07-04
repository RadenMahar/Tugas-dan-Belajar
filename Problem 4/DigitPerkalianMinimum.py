def digitPerkalianMinimal(input):
    listJumlahDigit = []
    for i in range(1, input+1):
        str_temp = ""
        if input%i == 0:
            str_temp += str(i)+str(int(input/i))
            #print(str_temp)
            listJumlahDigit.append(len(str_temp))

    #print(listJumlahDigit)
    minDigit = listJumlahDigit[0]
    for i in range(1, len(listJumlahDigit)):
        if minDigit > listJumlahDigit[i]:
            minDigit = listJumlahDigit[i]
    return minDigit

print(digitPerkalianMinimal(24))
