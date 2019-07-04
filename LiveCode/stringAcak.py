def SimalirtyWord(StringOne, StringTwo):
    hasilStringOne = Sortstring(StringOne)
    hasilStringTwo = Sortstring(StringTwo)

    if hasilStringOne == hasilStringTwo:
        return "Ya"
    else:
        return "Tidak"


def Sortstring(input):
    pasing = []
    for i in range(0, len(input)):
        pasing.append(input[i])

    for i in range(0, len(pasing)):
        temp = pasing[0]
        for j in range(i, len(pasing)):
            if pasing[i] > pasing[j]:
                temp = pasing[i]
                pasing[i] = pasing[j]
                pasing[j] = temp
    return pasing

print(SimalirtyWord('malang', 'ngalum'))
print(SimalirtyWord('alterra', 'rerlata'))
print(SimalirtyWord('alterra', 'terlata'))
print(SimalirtyWord('python', 'nothyd'))
print(SimalirtyWord('python', 'nothyp'))
