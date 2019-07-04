def pasanganbesar(num):
    str_convert = str(num)
    max_sementara = int(str_convert[0])

    for i in range(0, len(str_convert)-1):
        for j in range(1, len(str_convert)):
            if max_sementara < int(str_convert[j]):
                max_sementara = int(str_convert[j])

    index_temp = str_convert.index(str(max_sementara))
    number_wanted = str_convert[index_temp]+ str_convert[index_temp+1]
    return number_wanted

#print(pasanganbesar(641573))
#print(pasanganbesar(12783456))
#print(pasanganbesar(910233))
#print(pasanganbesar(71856421))
print(pasanganbesar(79918293))