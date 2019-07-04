def checkAB(stringn):
    menemukan_index_a = []
    menemukan_index_b = []
    for i in range(0, len(stringn)):
        if 'a' == stringn[i]:
            menemukan_index_a.append(i)
        elif 'b' == stringn[i]:
            menemukan_index_b.append(i)

    list_jarak = []
    for i in range(len(menemukan_index_a)):
        for j in range(len(menemukan_index_b)):
            list_jarak.append(abs(menemukan_index_a[i]-menemukan_index_b[j])-1)

    if 3 in list_jarak:
        return True
    else:
        return False


print(checkAB('lane borrowed'))
print(checkAB('i am sick'))
print(checkAB('you are boring'))
print(checkAB('barbarian'))
print(checkAB('bacon and meat'))
        