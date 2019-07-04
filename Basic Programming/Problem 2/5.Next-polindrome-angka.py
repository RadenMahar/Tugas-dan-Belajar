def mengecek_pemenuhan_polindrom(input2):
    BalikanInterger = 0
    sisa_untuk_ngecek = 0
    var_temp = input2
    while input2 != 0 :
        sisa_untuk_ngecek = (input2)%10
        BalikanInterger = BalikanInterger*10 + sisa_untuk_ngecek
        input2 = int(input2 / 10)
    return BalikanInterger
        
def InputPolindrom(input):
    cari_polindrom = input
    if mengecek_pemenuhan_polindrom(cari_polindrom) == input:
        cari_polindrom +=1
    while True:
        if mengecek_pemenuhan_polindrom(cari_polindrom) == cari_polindrom:
            break
        else:
            cari_polindrom+=1
    return mengecek_pemenuhan_polindrom(cari_polindrom)

print(InputPolindrom(8))
print(InputPolindrom(10))
print(InputPolindrom(117))
print(InputPolindrom(175))
print(InputPolindrom(10000))



