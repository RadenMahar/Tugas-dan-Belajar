def angkaPrima(angka):
    list_temp = []
    for i in range(1, angka+1):
        if angka%i == 0:
            list_temp.append(i)
    if len(list_temp) == 2:
        return True
    else:
        return False

print(angkaPrima(1))
print(angkaPrima(3))
print(angkaPrima(7))
print(angkaPrima(6))
print(angkaPrima(23))