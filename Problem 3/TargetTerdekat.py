def targetTerdekat(arr):
    list_tempat_index_x = []
    for i in range(0, len(arr)):
        if 'x' == arr[i] and 'x' in arr:
            list_tempat_index_x.append(i)
        elif 'x' in arr:
            continue
        else:
            list_tempat_index_x.append(len(arr)+1)
    
    if list_tempat_index_x[0] == len(arr)+1:
        return 0

    list_tempat_index_o = []
    for i in range(0, len(arr)): 
        if 'o' == arr[i]:
            list_tempat_index_o.append(i)

    #print(list_tempat_index_o)
    #print(list_tempat_index_x)
    list_hasil_hitung_jarak = [] 
    for i in range(0, len(list_tempat_index_x)):
        for j in range(0, len(list_tempat_index_o)):   
            list_hasil_hitung_jarak.append(abs(list_tempat_index_o[j]-list_tempat_index_x[i]))

    var_max = len(arr)
    for i in range(0, len(list_hasil_hitung_jarak)):
        if var_max > list_hasil_hitung_jarak[i]:
            var_max = list_hasil_hitung_jarak[i]
    
    return var_max

print(targetTerdekat([' ', ' ', 'o', ' ', ' ', 'x', ' ', 'x']))
print(targetTerdekat(['o', ' ', ' ', ' ', 'x', 'x', 'x']))
print(targetTerdekat(['x', ' ', 'o', ' ', 'x', 'x', 'o', ' '])) 
print(targetTerdekat([' ', ' ', 'o', ' ']))
print(targetTerdekat([' ', 'o', ' ', 'x', 'x', ' ', ' ', 'x']))
