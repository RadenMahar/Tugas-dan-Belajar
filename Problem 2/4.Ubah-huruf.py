def ubahhuruf(input):
    stra = "abcdefghijklmnopqrstuvwxy"
    str_sementara = ""
    for i in range(len(input)):
        if input[i] == stra[-1]:
            input[i] = stra[0]
        else:
            index_sementara = stra.index(input[i])
            str_sementara += stra[index_sementara+1]
    return str_sementara

print(ubahhuruf("wow"))
print(ubahhuruf("developer"))
print(ubahhuruf("keren"))
print(ubahhuruf("semangat"))