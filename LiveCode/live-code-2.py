def remove_string(str, ch):
    newstring = ''
    for j in range(len(str)):
        if str[j] == ch:
            newstring += str[j+1:]
            break
        newstring += str[j]
    return newstring

def string_acak(stringSatu, stringDua):
    if stringSatu == stringDua:
        return False
    for i in stringSatu:
        stringDua = remove_string(stringDua, i)
    if len(stringDua) > 0:
        return False
    return True

print(string_acak('malang', 'ngalam'))
print(string_acak('alterra', 'rerlata'))
print(string_acak('alterra', 'terlata'))
print(string_acak('python', 'nothyd'))
print(string_acak('python', 'nothyp'))
