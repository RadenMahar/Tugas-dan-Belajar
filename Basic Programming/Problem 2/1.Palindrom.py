def polindrom(kata):
    balik_kata =""
    for i in range(0, len(kata)):
        balik_kata += (kata[len(kata)-i-1])
    if balik_kata == kata:
        return 
    else:
        print(balik_kata)

polindrom("katak")
