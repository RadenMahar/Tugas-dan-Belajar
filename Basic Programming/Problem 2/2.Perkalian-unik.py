def perkalian_unik(input):
    lst_temp = []
    for i in range(0, len(input)):
        list_temp2 = input[:i]+input[i+1:]
        var_sementara = list_temp2[0]
        for j in range(1, len(list_temp2)):
            var_sementara *= list_temp2[j]     
        lst_temp.append(var_sementara)
    return lst_temp

#x = [2, 4, 6]
#x = [1,2,3,4,5]
#x = [1,4,3,2,5]
#x= [1,3,3,1]
x = [2,1,8,10,2]
print(perkalian_unik(x))

        