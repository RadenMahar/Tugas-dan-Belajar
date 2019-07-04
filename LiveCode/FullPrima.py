def fullPrima(bilangan):
    banyak_faktor = 0
    HasilCek = []
    for i in range(1, bilangan+1):
        if bilangan % i == 0:
            banyak_faktor += 1
    
    HasilCek.append(banyak_faktor)

    k = str(bilangan)
    
    intTemp = []

    for i in range(0, len(k)):
        intTemp.append(int(k[i]))
    
    for i in range(0, len(intTemp)):
        jumlahFaktoTemp = 0
        for j in range(1, intTemp[i]+1):
            if bilangan % j == 0:
                jumlahFaktoTemp += 1
        HasilCek.append(jumlahFaktoTemp)

    BoleanCek = []
    for i in range(0, len(HasilCek)):
        if HasilCek[i] == 2:
            BoleanCek.append(True)
        else:
            BoleanCek.append(False)
    
    if False in BoleanCek:
        return "Tidak"
    else:
        return "Ya"


print(fullPrima(101))
print(fullPrima(3))
print(fullPrima(11))




