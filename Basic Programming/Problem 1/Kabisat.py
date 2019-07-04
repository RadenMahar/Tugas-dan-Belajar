#input tahun
#x = 1804
#x = 1803
#x = 2400
x = 2490

if x % 4 == 0 and x % 100 != 0 :
    print(" Tahun Kabisat ")

elif x % 4 == 0 and x % 100 == 0 and x % 400 == 0 :
    print(" Tahun Kabisat ")

else:
    print(" Bukan Tahun Kabisat ")



